# Search and Browsing

**Outcome: you can find a photo four
different ways — by when, by where, by
what the classifier thinks is in it,
and by words you control — and you
know how much to trust each way.**

The web app's browse views are the
index wearing different hats:
**Browse** (the timeline, newest
first), **Folders** (your originals
folder structure), **Places** (a map
and a list of place names), **Labels**,
**People**, and **Albums**. Underneath
them all sits one search box with a
filter language, and this chapter
teaches the filters the lab verified —
through the same API the web app
itself uses, so every result below is
a claim you can repeat (transcripts
t09 and t11).

## By when

Timeline order is the index's
`taken_at`, which is why chapter 5's
date rules matter. The filter form is
`year:2024`:

```text
year:2024 → 3 photos
  Church / Reykjavíkurborg / 2024
  Harbour Sunrise / 2024
  City Squares / 2024
```

Exactly the three the lab dated 2024 —
the date the *file claimed*, chapter
6's PNG-by-modification-time being the
standing warning that a photo's year
is only as good as its metadata.
Months, days and ranges exist in the
same family (`before:`, `after:` and
friends, in the project's search
documentation); the shape to remember
is that time filters read the index's
date, never the file's name.

## By where

A photo with coordinates carries a
place, found offline from the
coordinates themselves — the lab's
control photo resolved to
*Reykjavíkurborg*, Iceland without the
lab providing any place name anywhere.
The verified filter:

```text
country:is → 1 photo
  Church / Reykjavíkurborg / 2024
```

(`is` is Iceland's country code; the
beach control answers to `country:za`
for South Africa.) In the app, Places
shows the same facts on a map.
Photos whose files carry no
coordinates — most of the lab's
fixtures, for the chapter 5 reason —
are absent from Places entirely, which
is the visible symptom of the GPS
trap.

## By what's in it: labels

Indexing ran the classifier over every
photo and stored its best guesses as
**labels**, each with an uncertainty
score. Search speaks them directly:

```text
label:church → 2 photos
  Church / Reykjavíkurborg / 2024
  Harbour Sunrise / 2024
```

— confirmed twice over, once through
the API and once with the command-line
search, `photoprism find
"label:church"` (transcript t11).

Now the honesty this guide owes you.
The lab's photos are *drawings*, and
the classifier — trained on real
photographs — did its sincere best
with them: the sunrise became
**Church** (and Website), the grid of
squares a **Scoreboard**, the mountain
lake an **Office**, the chart lines a
**Website**. Two fixtures got no label
at all; nothing cleared the bar. On
real photographs of real things the
same model is far more sensible — that
is what it was trained on — but the
lab cannot show you that from its own
evidence, and does not ask you to take
it on trust. What the lab *does*
establish is the mechanism and its
limits: a label is a guess with a
score, search by label finds the guess
reliably, and a wrong guess is wrong
confidently enough to file your
sunrise under Church. Treat labels as
a helpful intern's first pass:
excellent for "roughly, pictures with
water", never as evidence about a
specific photo. Your own words —
titles, captions, albums — outrank
them, which is the next way.

## By your words

Free text in the search box reads the
fields you and the files control:
titles, captions, file names. The
lab's captions were distinctive on
purpose — every drawn fixture's
description says *lab fixture* — and
that phrase, searched, is the fastest
route to the fixture set. The working
rule for a real library: a caption you
wrote beats ten labels you didn't.
Chapter 8's albums are the heavier
form of the same control — hand-picked
sets that no classifier can overrule.

**Check:** in your own library, run
three searches — a `year:` you know is
populated, a `label:` you have seen on
a photo's page, and a word from a
caption you wrote. Each should return
exactly the photos those facts
describe; if `label:` surprises you,
chapter 5's sidecar for that photo
shows what the index holds.
