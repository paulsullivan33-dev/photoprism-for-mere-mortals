# PhotoPrism for Mere Mortals

Most photo libraries live in the cloud:
you upload your pictures to someone
else's computer, and in return it
indexes them, finds the faces, and
hands you a search box. **PhotoPrism**
does the same job with the cloud left
out. It is a program you run on your
own machine. You point it at the
folder where your photos already live,
and it reads them — never moves them,
never rewrites them — building an
**index** of dates, places, labels and
faces, and serving a web app for
browsing and searching it all. No
account, no upload, and the
recognising is done by models stored
on your own disk.

This guide explains how PhotoPrism
turns a folder of files into a
searchable library, how to install it
without Docker, and how to run your
first index. Then it does something
most photo-app guides skip: it checks
the claims. The lab that wrote this
guide could not use real photographs —
its fixtures are **drawings**, six
pictures it generated itself, with
camera metadata it wrote into them by
hand so that every fact PhotoPrism
reported could be compared against
the truth the lab planted.

That turns out to be a sharper test
than it sounds. The lab verified the
program end to end: the official
standalone package running on a small
Linux machine, the first index, the
thumbnails, the index read directly
as a database, the web app and its
API, searches by year, place and
label, an album built and read back,
and a full backup of the index. Its
drawn photos carried crafted dates,
captions and GPS coordinates — and
the lab caught PhotoPrism's reader
quietly dropping the GPS from files
written by an unusual tool, proved
the cause with two control files, and
found the fix. That story is chapter
5, and it is the most useful thing in
the guide.

What the lab could not do, it did not
fake. Its drawings are not faces, and
the face pipeline — though it ran,
models and all — stored not one face
from them; chapter 7 explains the
gates it watched refuse its pictures,
and leaves judging real-face accuracy
to your own library. The library held
nine files, so nothing here is
evidence about scale. `criteria.md`
keeps the full ledger of what was run
and what was only read.

## What this guide covers

- [**What PhotoPrism is**](what-photoprism-is.md) —
  the mental model: your folder, read
  in place, an index of everything in
  it, and a web app on your own machine
- [**The moving parts**](the-moving-parts.md) —
  the program, the originals folder,
  the storage folder and its database,
  sidecar files, and the recognition
  models — and which part is precious
- [**Installing PhotoPrism**](installing-photoprism.md) —
  the standalone package, the one
  system library it does not bundle,
  and the configuration you supply
  because the package ships none
- [**Your first library**](your-first-library.md) —
  point it at a folder, run the first
  index, start the server, and sign in
- [**How indexing reads your photos**](how-indexing-reads-photos.md) —
  where dates, titles and places come
  from, the fallback when a file says
  nothing, and the GPS trap, with the
  control experiments that pin it down
- [**Search and browsing**](search-and-browsing.md) —
  finding photos by when, by where, by
  the classifier's labels, and by your
  own words — with the label results
  graded honestly
- [**Faces and people**](faces-and-people.md) —
  the three stages from a face to a
  person, the quality gates between
  them, and this chapter's own ledger
  of what the lab could not prove
- [**Albums, sharing and the archive**](albums-sharing-and-the-archive.md) —
  hand-made order that survives
  re-indexing, hiding without deleting,
  and where sharing begins
- [**Recipes**](recipes.md) — back up
  the index, the weekly tidy, fix a
  folder of location-less photos,
  read-only originals, searching from
  scripts, and growing the library
- [**The neighbours**](the-neighbours.md) —
  Immich the other librarian, a plain
  folder tree, and the clouds: what
  each does that PhotoPrism doesn't
- [**Limits**](limits.md) — an index is
  not a backup, labels are guesses,
  and the standalone route is the
  project's side door
- [**Troubleshooting**](troubleshooting.md) —
  the missing library, the missing
  places, the wrong dates, the empty
  People page, and the traps this
  guide's lab fell into
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Running PhotoPrism under Docker — the
project's main route, and a fine one;
this guide takes the standalone route
so the machinery stays visible, and
says so where the difference matters.
Developing raw photos or editing
images — PhotoPrism is a librarian,
not an editor. Rolling it out to the
internet — sharing beyond your own
network is a networking project of
its own, and chapter 8 stops honestly
at the doorstep.

## How to use this guide

Read chapters 1 and 2 before
installing anything: knowing which
part holds what turns later surprises
into named problems. Chapter 5 is the
one to read slowly even if your
library is already indexed — its
checks are how you catch a photo that
silently lost its place. The lab's
transcripts live in
`photoprism-lab/transcripts/`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Immich for Mere Mortals](https://paulsullivan33-dev.github.io/immich-for-mere-mortals/)
- [Backups for Mere Mortals](https://paulsullivan33-dev.github.io/backups-for-mere-mortals/)
- [Local AI at Home for Mere Mortals](https://paulsullivan33-dev.github.io/local-ai-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/photoprism-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/photoprism-for-mere-mortals/blob/main/LICENSE-CODE).
