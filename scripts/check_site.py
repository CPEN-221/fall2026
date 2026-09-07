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


def fail(message: str) -> None:
    raise AssertionError(message)


def strip_front_matter(markdown: str) -> str:
    match = re.match(r"\A---\n.*?\n---\n\n?", markdown, flags=re.DOTALL)
    if not match:
        fail("index.md is missing valid YAML front matter")
    return markdown[match.end() :]


def inherited_body(markdown: str) -> str:
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

    ta_section = source.split("### Teaching Assistants", 1)[1].split("# Class Meeting Times", 1)[0]
    if len(re.findall(r"^- ", ta_section, flags=re.MULTILINE)) != 1:
        fail("the teaching-assistant section must contain exactly one named TA")

    if OLD.is_file():
        expected = inherited_body(OLD.read_text(encoding="utf-8"))
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
        fail("layout is missing the reading-type selector")
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
        fail("rendered page must contain one reading-type selector")

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
