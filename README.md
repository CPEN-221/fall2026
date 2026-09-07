# CPEN 221 Fall 2026 syllabus

This directory is a self-contained Jekyll site for the CPEN 221 A/B syllabus. The
student-facing content is in `index.md`; the page frame is in `_layouts/`, and the
responsive and print styles are in `assets/`. The institutional visual system uses
self-hosted fonts under `assets/fonts/`. Readers can choose IBM Plex Serif with IBM
Plex Sans and IBM Plex Mono, or Google Sans Flex with Google Sans Code. The choice
is retained in the browser and shared with the CPEN 221 readings and project sites.

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

In the repository settings, open **Pages** and choose **Deploy from a branch**.
Select the `main` branch and the `/(root)` folder. GitHub Pages will rebuild the
Jekyll site after each push to `main`.
