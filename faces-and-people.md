# Faces and People

**Outcome: you understand the three
stages between "a photo" and "photos
of this person", you know the quality
gates each stage applies — because the
lab watched them refuse its pictures —
and you know exactly which part of
this chapter the lab could not prove.**

This chapter is written to the
series' rules, so it starts with its
ledger. The lab ran the real face
pipeline, on the real models, over
its whole library. The pipeline
loaded, looked, and — for reasons this
chapter explains — kept nothing. A
hand-drawn portrait joined the library
as a final test, and kept nothing
either. What follows separates, at
every step, what that evidence proves
from what only the project's
documentation can tell you. Positive
detection — a real face found, grouped
and named — is in the second category,
and the chapter never pretends
otherwise.

## The pipeline, in three stages

From the project's documentation,
matching the programs the lab watched
load:

1. **Detection.** The **YuNet** model
   scans a photo's 720-pixel preview
   and marks rectangles that look like
   faces. Each becomes a **marker**.
   The lab saw the loader's own log
   lines every run: `faces: loading
   yunet on the cpu`, `faces: loading
   sface on the cpu`.
2. **Embedding.** The **SFace** and
   **FaceNet** models turn each marked
   face into an **embedding** — a list
   of numbers describing it, so faces
   can be compared by arithmetic
   rather than by looks.
3. **Clustering.** Embeddings that sit
   close together are grouped (the
   project uses DBSCAN) into an unnamed
   cluster — "these faces are one
   person" — which waits under
   **People** for you to give it a
   name. Naming a cluster makes a
   **subject**: from then on, that
   person's new photos are recognised
   as they are indexed, and
   `people:`-style browsing finds them
   all.

The command-line surface mirrors the
stages — `photoprism faces status`,
`faces index`, `faces ls`, `faces
markers`, `faces subjects` — and the
lab's `faces status` answered from its
own instance: *Face detection and
recognition are enabled*, detector
`yunet`, with the model's path inside
the installed package (transcript
t08).

## The gates — and the lab's refusal

Between a marker and a cluster stand
quality gates, and this part the lab
proves from its own log. After its
first index, the face worker reported:

```text
faces: 0 of the 10 new markers required for clustering
clear the 112 px size and 85 score thresholds
```

Ten candidate markers had been raised
across six abstract drawings —
detectors are pattern machines, and
circles and contrasts suggest faces to
them the way clouds suggest animals to
us. Not one candidate was both large
enough (112 pixels) and confident
enough (score 85) to be worth
clustering, and the index's own tables
confirm the outcome: **markers 0,
faces 0, subjects 0** (transcripts
t04, t08). The lab's drawn portrait —
a big, deliberate, cartoon face, half
a metre of pixels wide — met the same
end: no stored marker, no face.

Read that result for what it is. It
proves the gates are real and are
applied; a system that filed the
lab's fruit bowl as a person would be
telling you its people features are
noise. It does **not** prove the
pipeline recognises real faces well or
badly — drawings are not faces, and
the lab had none it was willing to
use: this guide's fixtures are
synthetic by rule, and it does not
borrow strangers' portraits to make a
demo prettier. Judging accuracy on
real family photos is, honestly, your
first evening with your own library.

## Working with people, once faces land

Documented-only, from the project's
user guide — the everyday flow once
real photos produce clusters:

- **People** lists clusters as face
  thumbnails. Naming one ("Mum",
  "Alex") creates the subject; the
  name is yours, the grouping is the
  machine's, and both can be wrong in
  opposite directions.
- A cluster can hold an impostor (an
  embedding that landed close) and one
  person can split across two clusters
  (age, glasses, a decade). The app
  lets you remove a face from a person
  and merge clusters; `photoprism
  faces conflicts` lists clusters the
  index itself finds suspicious.
- Faces the machine found but could
  not place stay as markers on the
  photo's page, where you can assign
  or dismiss them by hand.
- Recognition runs during indexing
  (the `face-run` setting the lab's
  status showed as `auto`), so a named
  person collects new appearances
  without a separate step.

## The privacy fact, stated once

Every stage of this chapter ran on the
lab's machine, against models stored
on its own disk, with the network
playing no part — the same property
chapter 1 promised for the whole
tool. Face embeddings are numbers in
your index database; they are not
uploaded, and no account exists for
them to be uploaded to. That is the
entire reason to run this feature at
home rather than in a cloud library,
and it is worth the slower hardware.

**Check:** `photoprism faces status`
on your instance should name the
`yunet` detector, and `photoprism
faces subjects` should list your named
people — an empty list simply means no
cluster has been named yet.
