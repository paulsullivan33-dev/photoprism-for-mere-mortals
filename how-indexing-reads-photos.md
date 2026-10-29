# How Indexing Reads Your Photos

**Outcome: you can predict, for any
photo, where PhotoPrism will get its
date, title and place from — and you
know the one trap that can silently
cost a photo its location.**

## What it reads, in what order

Indexing treats each file as a small
archive of claims. The claims it
trusts most are the ones the camera
wrote inside the file — the **EXIF**
block — helped by any XMP or
PhotoPrism sidecar travelling with the
photo. From those it takes, per photo:

- **When** — `DateTimeOriginal`, the
  moment the shutter fired.
- **What it is called** — a title it
  builds (below), plus the file's own
  caption or description when one
  exists.
- **Where** — GPS coordinates, which
  it turns into a named place.
- **How** — camera and lens, which it
  files under Cameras and shows in the
  photo's details.

The lab's fixtures make each claim
checkable, because the lab *wrote*
them: six drawn pictures, five JPEGs
carrying crafted EXIF (dates in 2023,
2024 and 2025, a camera called
`LabCamera LC-1`, descriptions), and
one PNG with no metadata at all. Every
JPEG's date arrived in the index
exactly as written, and the caption
arrived word for word (transcripts
t01, t04, t05). PhotoPrism also writes
what it extracted into its own YAML
sidecar in `storage/sidecar/` — the
lab's harbour photo's sidecar records
`TakenAt: 2024-06-14T06:12:00Z`,
`TakenSrc: meta`, and the caption,
marked as coming from the file. That
paper trail is the chapter's recurring
check: if a fact looks wrong in the
app, the sidecar shows what the file
actually said.

## When the file says nothing

The lab's sixth fixture, a PNG with no
metadata, was indexed with the date of
the file's **modification time**, and
the log said so in plain words:

```text
media: chart-lines.png was taken at 2026-10-29 18:37:08 +0000 UTC (file mod time)
```

That fallback is the rule: no EXIF
date → the file's own timestamps → the
moment of indexing. Scanned photos,
screenshots and exports from other
apps often live on this path, and it
is why their dates in the timeline are
"when the file was made", which may
not be when the picture was taken.
The fix lives in the file: set the
date in the photo's metadata with an
editor or `exiftool`, then re-index.

## Titles are built, not found

Unless a file carries a real title,
PhotoPrism constructs one. The lab
watched the recipe change with the
ingredients:

- File name + year, cleaned up:
  `harbour-sunrise.jpg` became
  **Harbour Sunrise / 2024**.
- With a place, the place joins in —
  and the photo's strongest label
  leads: the GPS-corrected harbour
  photo became **Church /
  Reykjavíkurborg / 2024**, and the
  project's own beach sample became
  **Seashore / South Africa / 2017**.
- No date, no title: the PNG is
  simply **Chart Lines**.

You can edit any title in the app;
the constructed one is a starting
point, and knowing the recipe explains
the timeline's stranger names.

## The GPS trap — read this one slowly

Here is the finding this guide most
wants you to keep. The lab's five
fixtures carried carefully written GPS
coordinates. Two independent tools —
ExifTool, and Python's PIL — read
those coordinates back perfectly. It
is a fact that they were in the files.

PhotoPrism indexed the photos with
**no coordinates at all**: latitude
and longitude zero, place unknown. The
only clue was one log line per file:

```text
metadata: EOF in city-squares.jpg, starting brute-force search (parse jpeg)
```

What happened, as far as the evidence
reaches: PhotoPrism's own JPEG reader
tripped over the segment layout that
the lab's Python library writes — a
layout other readers accept without
complaint — and fell back to a
brute-force scan. The scan recovered
the dates, captions and camera. It did
not recover the GPS block.

The control experiments pin it down:

- The **same photo**, its GPS
  rewritten by **ExifTool** (same
  values), indexed with the
  coordinates exact to the digit —
  64.1466, −21.9426 — resolved
  offline into the place
  *Reykjavíkurborg*, country Iceland
  (transcript t07).
- A **real camera file** — one of the
  sample photos PhotoPrism ships for
  its own tests — indexed with its
  coordinates matching the project's
  published expected values to the
  last decimal (transcript t05).

So the lesson is not "PhotoPrism
loses GPS". Camera files — the thing
a photo library is actually made of —
index completely. The lesson is that
**the writer matters**: files produced
by unusual tools can be perfectly
legal and still fall into a parser's
fallback path, and location is what
the fallback drops. If a batch of
photos lands with no places, check
one file with ExifTool. If the
coordinates are there, rewriting them
with ExifTool (a lossless metadata
operation) and re-indexing is the
demonstrated fix. This is also why
chapter 3 calls ExifTool the one
optional tool worth having.

## Your originals, untouched — the proof

Chapter 1 promised indexing never
modifies originals. The lab did not
take it on faith: it checksummed its
originals before the first index and
after several more runs. Identical
hashes, and the folder held no new
files — no sidecars scattered among
the photos (transcript t03).
Everything PhotoPrism had to say, it
said in its own storage.

## When files move or vanish

The lab also renamed a photo between
runs, and watched the housekeeping
keep up: `photoprism purge` flagged
the old name as missing, the photo's
YAML sidecar was *moved* to the new
name, and a re-index updated the
record rather than duplicating the
photo (transcript t07). Renames and
moves inside originals are normal
life; purge-then-index is the tidy-up
pair, and chapter 9 puts them in a
schedule.

**Check:** pick one placed photo in
your library and compare: the app's
coordinates, the sidecar in
`storage/sidecar/`, and
`exiftool -GPSPosition` on the file
should all agree. When they don't,
this chapter has told you which of
the three to believe — the file.
