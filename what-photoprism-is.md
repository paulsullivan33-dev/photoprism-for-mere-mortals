# What PhotoPrism Is

**Outcome: you can say what PhotoPrism
does with a folder of photos, what it
never does to them, and where its
intelligence lives — all on your own
machine.**

## The problem it solves

Photos pile up. A camera, two phones, a
scanner, a decade of backups — thousands
of files in folders named by nobody's
system, findable only by remembering
roughly when they were taken. The big
cloud libraries solve this by taking the
photos away: upload everything, and a
company's computers index it, recognise
the faces, and hand you a search box —
along with an account, a subscription,
and your family archive on someone
else's disk.

**PhotoPrism** is the same idea with the
cloud left out. It is a program you run
on your own machine — a home server, a
small PC, a NAS. You point it at the
folder where your photos already live.
It reads every file, records what it
learns in a **database** (its index),
builds smaller preview copies, and
serves a web app you open in a browser:
a timeline, a search box, maps, albums,
and the faces it found. Nothing is
uploaded anywhere. The searching and
recognising happen on your hardware,
with models that ship inside the
program.

## The promise it keeps

The single most important fact in this
guide: **your original files are not
modified.** Indexing reads them. It does
not rename them, move them, re-encode
them, or write into them. Everything
PhotoPrism learns goes into its own
database and its own storage folder;
everything it writes about a photo —
captions, labels, corrections — lives
there too, or in **sidecar files** it
keeps beside its own copies of the data,
never inside your originals. Delete
PhotoPrism tomorrow and your photo
folder is exactly as it was. (Chapter 2
shows the layout; chapter 5 shows the
evidence from this guide's own lab.)

That promise shapes its personality.
PhotoPrism is a *library and index*
first and an editor hardly at all. It
will not crop, retouch, or fix a photo.
It organises, searches, and shows.

## What it does with a photo

For each file it finds, PhotoPrism:

- reads the **metadata** cameras embed
  in the file — the date taken, the
  camera, the lens, the GPS coordinates
  if the camera recorded them;
- records the photo in its index with a
  date, a place (worked out from the
  coordinates), and a title;
- generates **thumbnails** — the small
  copies the web app actually displays,
  so browsing never decodes your huge
  originals;
- runs its **image classification** to
  attach labels — *mountain*, *water*,
  *sky* and the like — so searches can
  find photos by what is in them;
- looks for **faces**, and groups the
  similar ones so you can name a person
  once and find them everywhere.

Chapters 5 to 8 walk that pipeline one
stage at a time, with checks.

## What it runs on

PhotoPrism is one program with a web
front end. The project's normal route is
a Docker container, and most of its
documentation assumes it. It also
publishes plain installation packages
for Linux — one program file plus its
libraries and models — and that is the
route this guide installs and tests
(chapter 3). Behind the web app sits a
database: **SQLite** for a small library
(one file, nothing else to run) or
**MariaDB** for a large one. This guide
uses SQLite, and says plainly where the
choice starts to matter.

## The honest edges, up front

Three limits belong here, before any
procedure depends on them; chapter 11
has the full list.

- PhotoPrism is at its best with photos
  in folders it can simply read. It is a
  *viewer and index* for a library, not
  a backup system, and not a phone sync
  tool of the kind some neighbours lead
  with (chapter 10).
- The face and label features are
  machine learning: good, not perfect.
  A label is a guess with a score, and
  the guide treats it as one.
- It is developed by a small team and
  funded by a membership (PhotoPrism+)
  that unlocks a few extras; the free
  Community Edition this guide uses is
  the complete librarian — the extras
  are listed in chapter 11, from the
  project's own pages.

A **check**: none needed yet — chapter 2
names every part, and chapter 3 ends
with the program running and answering
its version.
