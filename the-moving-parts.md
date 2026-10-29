# The Moving Parts

**Outcome: you can name the places
PhotoPrism keeps things, say which one
is precious and which are rebuildable,
and predict where a new photo's facts
will land.**

## The program

One binary does nearly everything: it
serves the web app, runs the indexer,
answers the API the front end talks to,
and carries the command-line tools the
chapters use (`photoprism index`,
`photoprism faces`, `photoprism find`,
and friends). The installation package
bundles the heavy support libraries for
itself — the **TensorFlow** and **ONNX**
runtimes its recognition models need —
in its own `lib/` folder. One system
library it does *not* bundle is
**libvips**, which it loads at startup
to resize images; chapter 3 installs
it. Optional external tools widen what
it can read: `exiftool` for deeper
metadata work (chapter 5 shows why it
earns its place), `ffmpeg` for video,
converters for raw camera files. Plain
JPEG photos need none of them, and the
lab proved that by running without
them.

## The originals folder

`originals/` is your photo library,
exactly as it already exists.
PhotoPrism only reads it. Folders
inside it are meaningful: they appear
in the app under **Folders**, and many
people keep a year-and-month layout
there. Because indexing never writes
here, the folder can live on a
read-only mount or a NAS share. It is
the one part of the system that is
*yours*, not PhotoPrism's — chapter 5
shows the lab's originals carrying
identical checksums before and after a
full index run.

## The storage folder

`storage/` is PhotoPrism's own
workspace. Everything in it is either
rebuildable, or covered by backing up
one database file:

- `storage/index.db` — with the SQLite
  driver, the **index** itself: every
  photo's date, place, labels, faces,
  albums, and your edits, in a single
  file of well under a megabyte for the
  lab's library. This file *is* the
  library's brain. Back it up (chapter
  9 shows the program's own backup
  command doing it).
- `storage/cache/thumbnails/` — the
  preview copies, one set per photo,
  named by the photo's content hash
  rather than its file name. The lab's
  six photos produced 42 thumbnail
  files, about 420 KB in all.
  Rebuildable: delete them and they
  return on demand, at the cost of
  time.
- `storage/sidecar/` — one small YAML
  file per photo, holding the metadata
  PhotoPrism extracted (chapter 5 reads
  one in full).
- `storage/config/` — the options and
  settings the program writes for
  itself, and `storage/backup/` —
  where its backups land.

## Sidecar files

Some facts travel in **sidecars**:
small files that carry metadata
alongside the data they describe,
instead of inside it. The ones this
guide meets are the **YAML sidecars**
above — written in PhotoPrism's own
storage, never in your originals — and
**XMP sidecars**, the open Adobe format
other editors read, which PhotoPrism
reads on the way in and can write on
import and export. The rule from
chapter 1 holds throughout: sidecars
live in PhotoPrism's territory. Your
library does not sprout new files.

## The database

The index is a real database with two
supported engines. **SQLite** stores
it in the single `index.db` file: no
server to install, nothing to tune,
and the right choice for a personal
library — this guide's choice.
**MariaDB** is the project's
recommended engine for large libraries
and many simultaneous users, and the
one its Docker route runs by default.
The trade is operational, not
functional: the same photos, labels
and faces either way. Chapter 11 is
honest about where SQLite starts to
creak — chiefly when heavy jobs want
to write at once.

## The models

Recognition is done by **models**:
fixed, pre-trained files that ship
with the program. They never learn
from your library, and they never
phone home. The package this guide
installed carries these, with sizes
the lab read off its own disk:

- **YuNet** (under 1 MB) — finds the
  faces in a photo.
- **SFace** (37 MB) and **FaceNet**
  (92 MB) — turn each face into an
  **embedding**, the list of numbers
  faces are compared by.
- **EfficientFormerV2** (49 MB) — the
  image classifier that produces
  labels.
- An NSFW model (23 MB) that flags
  sensitive images so they can be
  kept out of shared views.

Because the models are files, their
behaviour is fixed for a given
release: the same photo gets the same
labels on any machine. Chapters 6 and
7 cover what that does — and does
not — prove.

**Check:** none yet. After chapter 4
you will run `photoprism config` and
watch it print these very paths —
originals, storage, database — from
your own instance.
