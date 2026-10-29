# Your First Library

**Outcome: PhotoPrism is running
against a real folder of photos, the
first index is built, and you have
signed in to the web app and seen your
photos in it.**

Work through this with a *small* folder
first — a few dozen photos copied
somewhere you can afford to experiment
on — even though indexing never
modifies originals. Small means a
mistake costs a minute, and everything
in this chapter works the same at ten
thousand photos; it just takes longer.

## Point it at the photos

With the environment from chapter 3
exported (originals, storage, SQLite,
an admin password), the program needs
to know nothing else. Confirm the
configuration it will use:

```bash
photoprism config
```

The lab's table showed `auth-mode
password`, the lab's own storage and
originals paths, and the admin user —
if a path is wrong, this is the moment
it is cheap to fix (transcript t03).

## Run the first index

Indexing can be driven from the
command line, which is what this guide
does, because its progress is written
down where you can read it:

```bash
photoprism index
```

The first run also builds the database
(the log shows its schema migrations
being applied, once). Then, for each
file, expect three beats in the log —
the lab's first run, over six photos,
produced exactly these shapes:

```text
media: generated 7 thumbnails for harbour-sunrise.jpg
vision: generated 2 labels for harbour-sunrise.jpg
index: added main jpg file harbour-sunrise.jpg
```

…ending with a summary:

```text
index: updated 6 files
library: indexed 7 files in …
```

(The second number counts a sidecar
among the files handled; the photos
themselves were six.) Six small photos
took the lab's shared machine about a
minute, most of it loading the
recognition models the first time. A
real library's first index is an
overnight-shaped job, not a coffee
one — chapter 5 explains what it is
doing with the time, and later runs
only process what changed.

**Check:** your storage folder now
holds `index.db`, and
`storage/cache/thumbnails/` holds
files. If the index found no photos,
the originals path in `photoprism
config` is the first suspect — it must
name the folder the photos are *in*.

## Start the server and sign in

```bash
photoprism start
```

Open the site URL from your
configuration — the lab's was
`http://127.0.0.1:2342/`. The lab
checked its instance the way you can
check yours, without a browser:

```bash
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:2342/
curl -sL http://127.0.0.1:2342/ | grep -o '<title>[^<]*</title>'
```

The root answers **307**, redirecting
to the login page — that is health,
not an error — and the page's title is
simply **PhotoPrism** (transcript
t09). Sign in as `admin` with the
password from your configuration.
(The account is created on this first
start, from those settings.)

What you should see is the **Browse**
timeline: your photos, newest first,
as thumbnails — the copies from the
storage cache, not your originals,
which is why scrolling is quick.
Open one. The viewer shows the photo
with the facts the index holds: its
date, and — down in the details — the
camera and description if the file
carried them. The lab's six drawn
fixtures appeared with the exact dates
their files claimed, including one
dated by nothing but its file's
modification time (transcript t09's
listing shows all nine photos the
lab's library eventually held, with
dates and coordinates side by side).

**Check:** the timeline's count of
photos matches the number of photo
files in your originals folder, and
the newest and oldest dates look
right. Wrong dates are a metadata
story, and chapter 5 is where they get
explained.
