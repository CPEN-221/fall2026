#!/usr/bin/env python3
"""Validate the Fall 2026 syllabus source and, when present, its Jekyll output."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.md"
OLD = ROOT.parent / "old" / "Course Syllabus" / "Course Syllabus.md"

REQUIRED_FILES = (
    "_config.yml",
    "_layouts/default.html",
    "assets/css/main.scss",
    "assets/fonts/fonts.css",
    "assets/fonts/licenses/googlesanscode-OFL.txt",
    "assets/fonts/licenses/googlesansflex-OFL.txt",
    "assets/fonts/licenses/ibmplexmono-OFL.txt",
    "assets/fonts/licenses/ibmplexsans-OFL.txt",
    "assets/fonts/licenses/ibmplexserif-OFL.txt",
    "assets/js/site.js",
    "assets/js/typeface-switcher.js",
    "Gemfile",
)

REQUIRED_SECTIONS = (
    "instructional-team",
    "class-meeting-times",
    "core-topics",
    "learning-outcomes",
    "policies",
    "assessment-and-grading",
    "use-of-generative-ai",
    "late-submissions-and-missed-exams",
    "course-communication",
    "collaboration",
    "books",
    "land-acknowledgement",
)

REMOVED_STAFF = (
    "Mohammad Shahrad",
    "Changyuan Lin",
    "Geoffrey Bian",
    "Rhys Byers",
    "Donghwa Kim",
    "Agastya Rai",
    "Shreya Shah",
    "Grace Wang",
    "Simon Hathout Willard",
)

OLD_JAVA_STARTING_POINT = (
    "Learning a new language is sometimes difficult, but one can easily navigate "
    "this task by separating the high-level problem-solving approach from the syntax "
    "of a particular language. Once you do this, you can take the solution approach "
    "and find the appropriate language features you need to use. Suppose you know C "
    "and are able to articulate a solution in C, then you can quickly map C code to "
    "Java code by relying on one of many Java resources on the WWW or a Java textbook. "
    "We recommend [Think Java](http://greenteapress.com/wp/think-java/) or [Head First "
    "Java](http://www.headfirstlabs.com/books/hfjava/) to get started. We have made "
    "available numerous slide decks to help you in this process. You can also practice "
    "Java syntax at [CodingBat](http://codingbat.com/)."
)

NEW_JAVA_STARTING_POINT = (
    "Learning a new language is sometimes difficult, but one can navigate this task "
    "by separating the high-level problem-solving approach from the syntax of a "
    "particular language. Once you do this, you can take the solution approach and "
    "find the appropriate language features you need to use. Suppose you know C and "
    "can articulate a solution in C. You can then map that code to Java with the CPEN "
    "221 onboarding guides provided with the course, which cover the required Java 25 "
    "language material and development tools. The [current Java references](#books) "
    "below can answer more detailed questions. You can also practise short Java "
    "problems at [CodingBat](https://codingbat.com/java)."
)

OLD_DOCUMENTATION_HINT = (
    "4. Learn to read software documentation. The [official Java tutorial]"
    "(http://docs.oracle.com/javase/tutorial/getStarted/index.html) and the "
    "[Java SE API documentation](http://docs.oracle.com/javase/8/docs/api/index.html) "
    "are rather good."
)

NEW_DOCUMENTATION_HINT = (
    "4. Learn to read software documentation. Use [dev.java](https://dev.java/learn/) "
    "for explanatory material and the [Java SE 25 API documentation]"
    "(https://docs.oracle.com/en/java/javase/25/docs/api/index.html) to determine what "
    "library types and methods provide."
)

REQUIRED_READING_LINKS = (
    "https://link.springer.com/book/9783032118202",
    "https://www.oreilly.com/library/view/java-in-a/0642572255992/",
    "https://www.informit.com/store/core-java-vol.-i-fundamentals-9780135558577",
    "https://www.oreilly.com/library/view/effective-software-testing/9781633439931/",
    "https://www.oreilly.com/library/view/program-development-in/9780768685299/",
    "https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/",
    "https://martinfowler.com/books/refactoring.html",
    "https://web.stanford.edu/~ouster/cgi-bin/aposd.php",
    "https://github.com/johnousterhout/aposd-vs-clean-code",
    "https://abseil.io/resources/swe-book",
    "https://htdp.org/2022-2-9/Book/index.html",
    "https://www.debuggingbook.org/",
    "https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/",
    "https://dev.java/learn/",
    "https://docs.oracle.com/en/java/javase/25/docs/api/index.html",
    "https://docs.oracle.com/en/java/javase/25/docs/specs/index.html",
    "https://docs.junit.org/6.1.3/overview.html",
    "https://guides.library.ubc.ca/az/oreilly-for-higher-education",
)

RETIRED_READING_TEXT = (
    "Core Java 2",
    "The Java Programming Language, 4th edition",
    "Java SE 8 edition",
    "Code Complete",
    "When Programs Fail",
    "Design Patterns: Elements of Reusable Object-Oriented Software",
    "ocw.mit.edu",
    "6.102",
)


def fail(message: str) -> None:
    raise AssertionError(message)


def strip_front_matter(markdown: str) -> str:
    match = re.match(r"\A---\n.*?\n---\n\n?", markdown, flags=re.DOTALL)
    if not match:
        fail("index.md is missing valid YAML front matter")
    return markdown[match.end() :]


def extract_section(markdown: str, heading: str, next_heading: str) -> str:
    try:
        start = markdown.index(heading)
        end = markdown.index(next_heading, start)
    except ValueError as error:
        raise AssertionError(f"could not locate section {heading.strip()}") from error
    return markdown[start:end]


def inherited_body(markdown: str, approved_books: str) -> str:
    lines = markdown.replace("\r\n", "\n").splitlines()
    try:
        start = lines.index("> # Instructional Team")
    except ValueError as error:
        raise AssertionError("could not locate the inherited syllabus body") from error

    normalized = []
    for line in lines[start:]:
        line = re.sub(r"^(\s*(?:(?:[-*+]|\d+\.)\s+))>+\s?", r"\1", line)
        line = re.sub(r"^(\s*)>+\s?", r"\1", line)
        normalized.append(line)
    body = "\n".join(normalized)

    body = body.replace(
        "- Prof. Mohammad Shahrad\n- Prof. Karthik Pattabiraman",
        "- Prof. Karthik Pattabiraman\n- Prof. Simon Oya",
    )
    body = re.sub(
        r"- Rudransh Kumar, MASc student, Electrical and Computer Engineering "
        r"\[Head TA\]\n(?:- .+\n){8}",
        "- Rudransh Kumar, MASc student, Electrical and Computer Engineering "
        "[Head TA]\n",
        body,
    )
    body = re.sub(
        r"!\[Screenshot 2025-09-22 at 5\.32\.58 PM\.png\]\([^)]+\)",
        "> **Fall 2026 exam schedule:** Dates and locations will be posted here "
        "after they are confirmed.",
        body,
    )
    body = re.sub(
        r"!\[Screenshot 2025-08-29 at 5\.13\.17 PM\.png\]\([^)]+\)\n?",
        "",
        body,
    )
    body = body.replace(
        "[Equity, Diversity, Inclusion + Indigeneity (EDI.I) | UBC Applied Science]",
        "[Equity, Diversity, Inclusion + Indigeneity (EDI.I) \\| UBC Applied Science]",
    )
    for old, new in (
        (OLD_JAVA_STARTING_POINT, NEW_JAVA_STARTING_POINT),
        (OLD_DOCUMENTATION_HINT, NEW_DOCUMENTATION_HINT),
    ):
        if old not in body:
            fail("could not locate inherited reading recommendation")
        body = body.replace(old, new, 1)
    inherited_books = extract_section(body, "# Books\n", "# Land Acknowledgement\n")
    body = body.replace(inherited_books, approved_books, 1)
    return re.sub(r"\n{4,}", "\n\n\n", body).rstrip() + "\n"


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.hrefs: list[str] = []
        self.tags: set[str] = set()
        self.title_text: list[str] = []
        self.typeface_pickers = 0
        self._in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.add(tag)
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if values.get("href"):
            self.hrefs.append(values["href"] or "")
        if tag == "select" and "data-typeface-picker" in values:
            self.typeface_pickers += 1
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_text.append(data)


def check_source() -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            fail(f"missing required source file: {relative}")

    source = INDEX.read_text(encoding="utf-8")
    for required in ("Fall 2026", "Karthik Pattabiraman", "Simon Oya", "Rudransh Kumar"):
        if required not in source:
            fail(f"index.md is missing required text: {required}")
    for name in REMOVED_STAFF:
        if name in source:
            fail(f"removed staff member still appears in index.md: {name}")

    books = extract_section(source, "# Books\n", "# Land Acknowledgement\n")
    for link in REQUIRED_READING_LINKS:
        if link not in books:
            fail(f"books section is missing required link: {link}")
    for retired in RETIRED_READING_TEXT:
        if retired in books:
            fail(f"books section retains retired reading text: {retired}")
    normalized_books = " ".join(books.split())
    if "The course readings are the textbook for CPEN 221" not in normalized_books:
        fail("books section must state that the course readings are the textbook")
    if "You do not need to buy another book" not in normalized_books:
        fail("books section must state that no book purchase is required")

    ta_section = source.split("### Teaching Assistants", 1)[1].split("# Class Meeting Times", 1)[0]
    if len(re.findall(r"^- ", ta_section, flags=re.MULTILINE)) != 1:
        fail("the teaching-assistant section must contain exactly one named TA")

    if OLD.is_file():
        expected = inherited_body(OLD.read_text(encoding="utf-8"), books)
        actual = strip_front_matter(source).rstrip() + "\n"
        if actual != expected:
            fail("student-facing content has drifted from the inherited syllabus")

    css = (ROOT / "assets/css/main.scss").read_text(encoding="utf-8")
    if css.count("{") != css.count("}"):
        fail("stylesheet braces are unbalanced")

    font_css_path = ROOT / "assets/fonts/fonts.css"
    font_css = font_css_path.read_text(encoding="utf-8")
    for family in (
        "IBM Plex Serif",
        "IBM Plex Sans",
        "IBM Plex Mono",
        "Google Sans Flex",
        "Google Sans Code",
    ):
        if family not in font_css:
            fail(f"font stylesheet does not define {family}")
    if re.search(r"(?:@import|https?://)", font_css):
        fail("font stylesheet must use only self-hosted assets")
    for relative in re.findall(r'src:\s*url\(["\']?([^"\')]+)', font_css):
        if not (font_css_path.parent / relative).is_file():
            fail(f"font stylesheet references a missing asset: {relative}")

    layout = (ROOT / "_layouts/default.html").read_text(encoding="utf-8")
    if "data-typeface-picker" not in layout:
        fail("layout is missing the typeface-option selector")
    if "<span>Typeface option</span>" not in layout:
        fail("layout is missing the typeface-option label")
    if not (
        layout.find("</main>")
        < layout.find('class="typeface-tools"')
        < layout.find('class="site-footer"')
    ):
        fail("typeface option must appear after the page content and before the footer")
    for value in ('value="plex"', 'value="google-sans"'):
        if value not in layout:
            fail(f"layout is missing typeface option {value}")
    if "typeface-switcher.js" not in layout:
        fail("layout does not load the typeface switcher")

    switcher = (ROOT / "assets/js/typeface-switcher.js").read_text(encoding="utf-8")
    for value in ('"plex"', '"google-sans"', '"cpen221-typeface"'):
        if value not in switcher:
            fail(f"typeface switcher is missing {value}")
    for value in (
        'html[data-typeface="plex"]',
        'html[data-typeface="google-sans"]',
    ):
        if value not in css:
            fail(f"stylesheet is missing the mapping for {value}")


def check_built_site() -> None:
    output = ROOT / "_site"
    if not output.exists():
        print("Rendered-site checks skipped: _site/ does not exist.")
        return

    html_path = output / "index.html"
    if not html_path.is_file():
        fail("Jekyll output is missing index.html")

    parser = SiteParser()
    parser.feed(html_path.read_text(encoding="utf-8"))
    config = (ROOT / "_config.yml").read_text(encoding="utf-8")
    baseurl_match = re.search(r'^baseurl:\s*["\']?([^"\'\n]*)', config, flags=re.MULTILINE)
    baseurl = baseurl_match.group(1).rstrip("/") if baseurl_match else ""
    for landmark in ("header", "nav", "main", "footer"):
        if landmark not in parser.tags:
            fail(f"rendered page is missing the {landmark} landmark")
    for section in REQUIRED_SECTIONS:
        if section not in parser.ids:
            fail(f"rendered page is missing section id #{section}")

    title = "".join(parser.title_text)
    if "Course syllabus" not in title or "CPEN 221" not in title:
        fail("rendered page title does not identify the syllabus and course")
    if parser.typeface_pickers != 1:
        fail("rendered page must contain one typeface-option selector")

    for href in parser.hrefs:
        parsed = urlparse(href)
        if parsed.scheme or parsed.netloc:
            continue
        local_path = unquote(parsed.path)
        if baseurl and (local_path == baseurl or local_path.startswith(baseurl + "/")):
            local_path = local_path[len(baseurl) :] or "/"
        if local_path in ("", "/"):
            if parsed.fragment and parsed.fragment not in parser.ids:
                fail(f"broken section link: {href}")
            continue
        target = output / local_path.lstrip("/")
        if target.is_dir():
            target /= "index.html"
        if not target.exists():
            fail(f"broken local link or asset: {href}")


def main() -> int:
    try:
        check_source()
        check_built_site()
    except AssertionError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Fall 2026 syllabus source and available build output passed validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
