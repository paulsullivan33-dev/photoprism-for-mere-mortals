# Albums, Sharing and the Archive

**Outcome: you can gather photos into
albums that survive re-indexing, hide
the ones you don't want in the
timeline without deleting anything,
and you know where sharing begins —
and what it costs in trust.**

## Albums: your words, made permanent

Labels are the machine's opinion;
**albums** are yours. An album is a
named list in the index — the photos
stay exactly where they are in
originals, which is why an album
costs nothing in disk and survives
re-indexing, renaming and every
classifier mood.

The lab built its album the way the
web app does it, but through the API
so the steps are on record
(transcript t10): create the album,
then add a photo to it, then read it
back:

```text
album created: "Lab Favourites"
photo added:   Church / Reykjavíkurborg / 2024
read back:     Lab Favourites | photos: 1
```

In the app the same work is selecting
photos and choosing *Add to Album*.
Two album flavours exist in the
project's design: **manual** albums
like the lab's, and **smart** albums
whose contents are a saved search —
an album that is really a question
("year:2024 and country:is") and
refills itself as the library grows.
Moments — the app's auto-built
collections of trips and occasions —
are a third, generated for you;
chapter 9 lists the `photoprism
moments` command that builds them.

Albums also leave the machine safely:
the backup command writes each album
to a YAML file (the lab's backup
folder gained
`albums/album/<uid>.yml`), so your
hand-made organisation is data, not
folklore trapped in a database
(transcript t11).

## The archive: hiding without deleting

Every library has photos that should
exist but not greet you: the blurry
duplicates, the screenshots, the
receipts. PhotoPrism's **Archive**
removes a photo from the timeline,
search and labels while keeping its
file, its index record and its album
memberships intact; **Restore** brings
it back. It is the reversible answer
to "I don't want to see this", as
distinct from deleting the file from
originals — which indexing will
dutifully notice, and purge will
tidy, permanently. The private flag
is the archive's narrower cousin:
private photos stay browsable by you
and are withheld from shared views.

## Sharing — described, with its boundary

The lab ran a single-user instance on
loopback and did not click through
sharing, so this section is
documented-only and says so. From the
project's documentation, the shapes
of sharing are:

- **Users.** Beyond the admin, you can
  add accounts (including restricted
  ones) under Settings; each signs in
  and sees the library as their role
  allows. This is a household feature,
  not a public one.
- **Share links.** An album can be
  given a secret link — anyone holding
  it can view that album without an
  account, optionally with downloads,
  and the link can be given an expiry.
  The link *is* the credential: treat
  it like a key, because it is one.
- **WebDAV.** PhotoPrism can serve the
  library over WebDAV, so file managers
  and sync apps (the project's docs
  name PhotoSync for phone backup) can
  read and add photos as if it were a
  network drive.

One boundary belongs in bold. The
instance you have built answers only
on your own machine. Sharing beyond
the house means putting it on a
network — a reverse proxy with real
TLS, in front of an application that
now guards your entire photo archive.
That is a networking project with its
own guide's worth of care; this one
deliberately stops at your doorstep,
and chapter 9's recipes include the
backup habit to adopt *before* any
such move.

**Check:** create an album, add two
photos, and restart the server. The
album and its count are unchanged —
proof it lives in the index, not in
the session. Then archive one photo
and confirm it leaves the timeline
but is still listed under the app's
Archive view.
