# CPEN 221 Fall 2026 syllabus

This directory is a self-contained Jekyll site for the CPEN 221 A/B syllabus. The
student-facing content is in `index.md`; the page frame is in `_layouts/`, and the
responsive and print styles are in `assets/`.

## Preview locally

Use Ruby 3.3, matching the runtime in the pinned GitHub Pages builder:

```sh
bundle install
bundle exec jekyll serve --livereload
```

Then open the local address reported by Jekyll. Run the repository checks after a
content or layout change:

```sh
python3 scripts/check_site.py
```

If `_site/` exists, the checker also validates the rendered page, its landmarks,
section links, and local assets.

## Publish with GitHub Pages

The included workflow is ready when this directory is the root of its own GitHub
repository. In the repository settings, choose **GitHub Actions** as the Pages
source and push to `main`.

Within a larger repository, GitHub only discovers workflows in the repository-level
`.github/workflows/` directory. Copy the included workflow there and change the
Jekyll build action's `source` value from `.` to `./syllabus/fall2026`. A
repository can publish only one Pages site, so coordinate this with any existing
Pages workflow.

## Content note

The inherited Fall 2025 syllabus supplied the course description, schedule,
learning outcomes, assessments, policies, advice, and references. The Fall 2026
version changes the term and instructional team as requested. The obsolete exam
schedule image has been replaced by a confirmation notice, and the illustrative
Piazza screenshot has been omitted. The validation script compares the remaining
content with the inherited source so policy text cannot drift unnoticed.
