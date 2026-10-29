# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's photos are drawings it generated, with stock
   coordinates and a fictional camera.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 11 names what the tool
   cannot do: it is an index, not a backup; it barely edits;
   labels are guesses; faces are gated and unproven here on
   real people; format depth is uneven; SQLite has a ceiling;
   and the standalone route is the project's side door.
8. **The ethics rule is in the text, early.** PhotoPrism's
   whole point is that a family's photo archive — the most
   personal data most households own — stays on their own
   machine: chapter 1 states the no-upload property before any
   procedure depends on it, chapter 8 repeats it for face
   embeddings specifically, and the lab used no real person's
   photo at any point.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu 24.04 sandbox,
shared with other work while the lab ran (timings are therefore
ranges, and the guide says so). PhotoPrism
**261007-65faaae5d-Linux-AMD64-Plus** was installed from the
project's official standalone package
(`dl.photoprism.app/pkg/linux/amd64.tar.gz`, 421,508,754 bytes,
SHA-256 `03dd5d319eeee7f1dfb51a1628ee598a33c9d94299a323b7083e9c65ed2d8f52`)
and run unmodified against the SQLite database driver. All
transcripts live in `photoprism-lab/transcripts/`.

The package bundles its TensorFlow 2.18 and ONNX runtimes and
all four recognition models (YuNet, SFace, FaceNet,
EfficientFormerV2, plus the NSFW model — sizes read off the
disk in transcript t00's notes and chapter 2). It does **not**
bundle libvips: the binary refuses to start without
`libvips.so.42`. The sandbox's package-manager lock was held by
another process throughout, so the lab fetched Ubuntu's
`libvips42t64` package and its dependency chain (libcfitsio,
libcgif, libexif, libmatio, libspng, libhdf5, libsz, libaec) as
.deb files, extracted them under the lab directory, and pointed
`LD_LIBRARY_PATH` at them — the identical library files an
`apt install libvips42t64` provides, which is the instruction
chapter 3 gives readers.

The lab library was built, not found. `make_photos.py` (in
`photoprism-lab/`, beside the transcripts) drew six pictures with PIL — a
harbour sunrise, a mountain lake, a grid of squares, a red
circle, a still life, and a set of chart lines — and wrote
crafted EXIF into five of them with piexif: three distinct
dates (2023, 2024, 2025), a camera named "LabCamera LC-1",
descriptions, and GPS for two real cities' coordinates,
Reykjavík and Kyoto. The sixth, a PNG, carried no metadata.
Two further files joined later as controls, each described
where it is used: `beach_sand.jpg`, one of the sample photos
PhotoPrism ships in its own package for testing, and a copy of
the harbour drawing whose GPS ExifTool rewrote. A ninth file,
a large hand-drawn portrait, tested the face pipeline. No real
person's photo was used at any point.

Run for real, with transcripts as evidence:

- Version, the full `--help` command surface, the bundled
  model inventory, and the libvips failure and resolution
  (t00). Fixture generation with the EXIF read back by an
  independent library (t01).
- First index of the six fixtures: database migrations, 7
  thumbnails generated per photo, classifier labels per photo,
  and the summary counts (t02). `photoprism config` printed
  the effective configuration (t03).
- The originals promise, proven: SHA-256 checksums of every
  original identical before and after indexing, and no new
  files in the originals folder; 42 thumbnail files (420 KB)
  in `storage/cache/thumbnails/`, named by content hash;
  one YAML sidecar per photo in `storage/sidecar/`, the
  harbour sidecar showing `TakenAt` exact to the crafted
  second, `TakenSrc: meta`, and the planted caption verbatim
  (t03, t04).
- The index read directly: all six dates exact; titles built
  as chapter 5 describes; labels with their uncertainty
  scores — the classifier called the sunrise "Church", the
  squares "Scoreboard", the lake "Office" — and markers,
  faces and subjects all zero (t04, t05).
- The GPS trap and its controls (t05, t06, t07): the drawn
  fixtures' GPS, though read perfectly by ExifTool 12.76 and
  PIL, was not picked up — the index log shows the reader's
  `metadata: EOF … brute-force search` fallback for each such
  file, and their rows carry latitude/longitude 0. The same
  photo with GPS rewritten by ExifTool indexed at exactly
  64.1466, −21.9426, resolved offline to the place
  "Reykjavíkurborg", country Iceland, and retitled in the
  place form. The shipped camera sample indexed at
  −29.2824777777778, 31.4436361111111 — the values in the
  project's own published expected-metadata dump for that
  file — as "Seashore / South Africa / 2017".
- Rename housekeeping: a renamed file was flagged by
  `photoprism purge`, its sidecar moved to the new name, and
  the record updated in place rather than duplicated (t07).
- Faces: YuNet and SFace loaded at every index; the worker
  reported 10 candidate markers of which 0 cleared the
  112 px / score-85 clustering gates; the markers, faces and
  subjects tables are empty; `photoprism faces status`
  confirms detection and recognition enabled with the YuNet
  detector; the drawn portrait produced no stored face (t08).
- The server on loopback: root URL answering 307 to the
  login page, page title "PhotoPrism"; API login with the
  lab admin account; the photo list (9 photos with titles,
  dates and coordinates); searches `label:church` (2
  photos), `country:is` (1), `year:2024` (3); subjects and
  faces endpoints returning empty (t09).
- Albums through the API: create, add the placed photo, read
  back with a photo count of 1 (t10). Command-line search
  `photoprism find "label:church"` returning the same two
  files as the API; `photoprism backup <file>` writing a
  complete SQL dump of the index plus per-album YAML backups
  (t11).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- **Positive face recognition.** No real face was ever
  detected, clustered or named in this lab: the fixtures are
  drawings by design, and the guide does not borrow real
  portraits. Chapter 8's naming, merging and correcting flow
  is from the project's user guide. The pipeline's loading,
  gating and refusal are live-verified; its accuracy on real
  people is not measured here at all.
- The Docker installation route (this sandbox runs no
  containers) — chapter 3 teaches the standalone package and
  characterises Docker from the project's own pages.
- The MariaDB database engine; this lab used SQLite only.
- Sharing in the UI: additional user accounts, album share
  links and their expiry, WebDAV access, and phone backup
  apps. The lab instance was single-user on loopback.
- Raw camera files, HEIC and video as originals: the lab
  indexed JPEG and PNG only. PhotoPrism ships samples of the
  other formats, but the lab did not index them.
- Moments generation, smart albums, the import workflow
  (`photoprism import`/`copy`), and the map view in the
  browser: place *resolution* is verified from the index and
  API; the rendered map was not exercised.
- PhotoPrism+ member features, and everything about running
  at scale: the lab library held nine files.

Fixtures are this guide's own and deliberately generic:
drawn shapes and landscapes, a pangram-free zone — stock
coordinates in two cities, a camera that does not exist, and
captions that say "lab fixture" out loud. Nothing was
modelled on any real person, household, or photo library.
