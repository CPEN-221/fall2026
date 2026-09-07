# Self-hosted typefaces

The syllabus offers the same two reading-type combinations as the CPEN 221
readings site:

1. IBM Plex Serif, IBM Plex Sans, and IBM Plex Mono; and
2. Google Sans Flex and Google Sans Code.

The WOFF2 files were retrieved through the Google Fonts CSS API on August 25,
2026, and copied from the readings site. Only the Latin and Latin Extended
subsets are included. Every family is distributed under the SIL Open Font
License 1.1; verbatim licence files are in `licenses/`.

The filenames record the family, style, weight, subset, and a short hash of the
source URL. To update the asset set, use `www/scripts/vendor_google_fonts.py`
from the course-materials workspace, review its output, and then copy the
reviewed files into this directory.
