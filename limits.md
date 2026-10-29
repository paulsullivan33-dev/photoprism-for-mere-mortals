# Limits

**Outcome: you can state what
PhotoPrism will not do, what it does
reluctantly, and where this guide's
own evidence runs out.**

**It is an index, not a backup.** The
originals folder is the only copy of
your photos PhotoPrism knows about,
and it adds no redundancy of its own.
Delete the library and the index is
an exquisite catalogue of nothing.
Backups are your job (recipe 1 covers
the index half).

**It barely edits.** Titles, captions,
albums, archives, people — metadata
about photos. It does not crop,
retouch, straighten or develop, and
it will not fix the photo itself. An
editor is a different tool; the XMP
sidecars are the handshake between
the two.

**Labels are guesses, and the lab has
the receipts.** Chapter 6: a sunrise
filed as Church, a lake as Office,
each with an uncertainty score, on
pictures the classifier was never
trained for. Real photos fare better;
the point stands that a label is a
search hint, not a fact, and search by
label inherits every mistake the
model makes.

**Faces are gated, probabilistic, and
— in this guide — unproven on real
people.** Chapter 7's ledger: the
pipeline ran, its gates refused every
candidate the lab offered, and no
real face was ever clustered. Even
when it works, clustering confuses
siblings, splits one person across
ages, and needs your corrections.
Plan on curating People, not merely
having it.

**Format depth is uneven.** JPEG is
home turf. Raw camera files, HEIC,
and video lean on the host's
converters and codecs — the Docker
image bundles them; the standalone
package leans on what your system
provides, and the lab, which indexed
JPEG and PNG only, makes no claim for
the rest. The package even warns that
it "does not include the system
dependencies required to make use of
all the features"; chapter 3's
libvips gap is the first instalment
of that sentence.

**SQLite has a ceiling.** One writer
at a time, roughly: on a big library
with heavy concurrent work the index
can queue behind itself, and the
project steers large installs to
MariaDB. The lab's nine photos say
nothing about ten thousand except
that nothing about the design forbids
them — see the honesty rule below.

**The standalone route is the
project's side door.** Manual updates,
no bundled defaults, and documentation
that assumes Docker first. This guide
chose it deliberately and it works;
it is fair to know the project's own
FAQ frames it as the experienced
users' option.

**Plus features exist.** The free
Community Edition is the complete
librarian this guide teaches. A paid
membership unlocks extras (the
project lists things like additional
map styles and priority support among
its member benefits, and the lab's
binary identified itself as the *Plus*
build, features gated by membership).
Nothing in these chapters needs it;
the line is named so you are not
surprised by it.

**And this guide's own limit, plainly:**
its lab library was nine files, six
of them drawings. It proves the
machinery — intake, metadata, places,
labels, search, albums, backup — and
is evidence of nothing about scale,
speed on a real archive, or accuracy
on real photographs. `criteria.md`
keeps the full ledger.
