# Recipes

**Outcome: six jobs a real PhotoPrism
household runs, each a short sequence
of things this guide has already shown
working.**

## 1. Back up the index (the one that matters)

Your photos are files — back them up
however you already do. The *index* is
one database plus your settings, and
the program backs it up itself:

```bash
photoprism backup ~/backups/photoprism-index.sql
```

The lab's run wrote a complete SQL
dump of its index (54 KB for nine
photos) and, alongside, a YAML file
per album under `storage/backup/`
(transcript t11). Schedule it like
any backup. Restoring is
`photoprism restore` against the same
file — and the reason this recipe
leads the chapter is chapter 2's:
thumbnails, sidecars and settings can
all be rebuilt, but the index holds
your albums, your people and your
edits.

## 2. The weekly tidy: purge, index, moments

After a week of adding, moving and
deleting files in originals:

```bash
photoprism purge
photoprism index
photoprism moments
```

Purge retires records of vanished
files (chapter 5 watched it flag a
renamed photo and follow the rename),
index picks up everything new, and
moments rebuilds the app's trip and
occasion collections. In that order,
on a schedule, this is the whole
maintenance routine for a healthy
library.

## 3. Fix a folder of location-less photos

Chapter 5's trap, treated in batch.
First prove the coordinates are in
the file but not the index — the
photo's page in the app shows no
place, while ExifTool reads one
straight from the file:

```bash
exiftool -GPSPosition photo.jpg
```

If ExifTool sees a position
PhotoPrism missed, rewrite the GPS
tags in place (same values, standard
layout) and re-index:

```bash
exiftool -overwrite_original -GPSLatitude=64.1466 -GPSLatitudeRef=N \
         -GPSLongitude=-21.9426 -GPSLongitudeRef=W photo.jpg
photoprism index
```

The lab's control photo went from
place *Unknown* to *Reykjavíkurborg*
by exactly this route (transcript
t07).

## 4. Serve the library read-only

Point PhotoPrism at a library nothing
is allowed to change — a backup disk,
a NAS export — by mounting it
read-only at the operating-system
level and setting the originals path
to it. Indexing never writes to
originals in the first place (chapter
6's checksums), so a read-only
originals folder is not a compromise;
it is the design with a seatbelt.

## 5. Search from a script

The command-line search speaks the
same filter language as the web app
and prints plain file names:

```bash
photoprism find "label:church"
photoprism find "year:2024 country:is"
```

The lab's first command printed the
two files the API search had already
found by the same filter (transcript
t11) — one index, two doors, which
makes `find` the right tool for
"export every photo matching X"
pipelines: feed its output to your
copy tool of choice.

## 6. Start small, then move the library

Growing out of the lab shape is three
environment variables wide: point
`PHOTOPRISM_ORIGINALS_PATH` at the
real library, keep `STORAGE_PATH`
where the good index lives, restart,
re-index. Nothing about the photos'
new home changes the index's model of
them — path, metadata, place — and
chapter 4's first run is the template
at any scale. When the library is
genuinely large, chapter 11's notes
on MariaDB and workers are the next
read, in that order.
