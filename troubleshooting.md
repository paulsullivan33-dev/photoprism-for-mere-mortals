# Troubleshooting

**Outcome: the failures this guide's
lab actually met, and the ones the
documentation warns about, each with
the check that names it.**

## `photoprism` won't start: libvips.so.42

```text
error while loading shared libraries: libvips.so.42:
cannot open shared object file
```

The standalone package needs the
system libvips it does not bundle
(chapter 3). Install it —
`sudo apt install libvips42t64` on
Ubuntu 24.04, `libvips42` on Debian —
and the same command answers with the
version. If it still fails, a
dependency of libvips itself is
missing; `ldd` on the binary lists
every library it cannot find, which
is how the lab walked the chain.

## Photos indexed, but no places

Chapter 5's trap. Work it in order:

1. Look at the index log for
   `metadata: EOF in <file>, starting
   brute-force search`. That line
   marks a file whose layout sent the
   reader down the fallback path.
2. Check the file itself:
   `exiftool -GPSPosition photo.jpg`.
   No output → the file truly has no
   coordinates, and no setting will
   invent them.
3. Coordinates present → rewrite them
   with ExifTool (recipe 3) and
   re-index. The lab's control photo
   gained its place by exactly this
   route.

Real camera files do not trip this;
suspect it for files written by
scripts, chatty exporters, and other
unusual tools.

## A photo's date is the day you copied it

The file had no EXIF date, so the
index used the file's modification
time — chapter 5's PNG. Confirm from
the photo's sidecar in
`storage/sidecar/` (`TakenSrc` will
not say `meta`). Fix the date in the
file's metadata, then re-index.

## The index log says a file was "updated", not added — after a rename

Working as designed: the photo's
record followed the file. Run
`photoprism purge` before `photoprism
index` in your tidy-ups (recipe 2) so
the missing-file bookkeeping stays
honest, especially after deletions —
a deleted photo that is never purged
lingers as a missing entry.

## People is empty, though the photos have faces

Three honest possibilities, in the
order the lab would check them:

1. **The gates.** Detection stores a
   marker only above its thresholds,
   and clustering asks for 112 px and
   a score of 85 (chapter 7).
   `photoprism faces audit` and
   `faces markers` show what, if
   anything, is waiting. Small,
   turned, or soft faces fail fairly.
2. **Faces not yet run.** Recognition
   works through the library over
   time; `photoprism faces index`
   forces a pass.
3. **It is off.** `photoprism faces
   status` says, in its first line,
   whether detection and recognition
   are enabled — the lab's said they
   were.

## Search by label returns something odd

It will, eventually — chapter 6's
Church-for-a-sunrise is the tame
version. Labels are the classifier's
guesses; check the photo's own page
for its labels and their place in its
details, and remember free-text
search over titles and captions is
the precise instrument. A label you
disagree with can be removed from the
photo in the app.

## The web app answers, but login loops or fails

Confirm the basics the lab verified:
the root URL returns **307** to the
login page (healthy), the admin
account is created on *first* start
from `PHOTOPRISM_ADMIN_PASSWORD`, and
`photoprism config` shows `auth-mode
password`. Changed the password
variable after first start? The
account already exists — change it
with `photoprism passwd` instead.

## Everything is slow on the first index

The first run pays for model loading
and every thumbnail at once; the
lab's six small photos took about a
minute, most of it the models.
`PHOTOPRISM_WORKERS` sets how many
indexing workers run — the lab used
2 on a shared, memory-tight machine.
Later runs process only changes and
are not comparable.
