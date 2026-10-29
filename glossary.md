# Glossary

The terms, collected in one place. Each
is defined the way this guide uses it.

**Album.** A named set of photos you
choose by hand. An album is a list in
the index; the photos stay where they
are.

**Archive (the verb).** PhotoPrism's
soft-hide: an archived photo leaves the
timeline and search but stays in the
library and can be restored.

**Cluster (faces).** A group of face
embeddings the program believes belong
to one person, waiting for you to name
them — or to say it guessed wrong.

**Embedding.** The list of numbers a
recognition model makes from a face (or
an image). Embeddings that sit close
together are treated as similar.

**EXIF.** The metadata block cameras
write inside a photo file: date taken,
camera and lens, exposure, sometimes
GPS. PhotoPrism's first source of facts
about every photo.

**Face.** In the index, one detected
face in one photo — a position plus an
embedding — as distinct from the
**person** it may belong to.

**Index (the noun).** Everything
PhotoPrism knows about your library,
held in its database: dates, places,
labels, faces, albums, stacks. The
index can be rebuilt from the originals;
the originals cannot be rebuilt from
the index.

**Indexing (the verb).** The scan that
walks the originals folder, reads
metadata, generates thumbnails and runs
the recognition models, writing it all
into the index.

**Label.** A word the classifier
attaches to a photo — *water*, *sky*,
*mountain* — with a confidence score.
Labels power search by content.

**Live photo / motion photo.** A still
with a short video attached, from a
phone. PhotoPrism pairs the parts and
plays the clip in the viewer.

**Marker.** A face the program found
but has not clustered or named yet.

**Metadata.** Data about the photo that
is not the picture itself: EXIF from
the camera, XMP from editors, and the
facts PhotoPrism derives, like place
names from coordinates.

**Model.** A fixed, pre-trained
recognition file shipped with the
program — YuNet and SFace for faces,
FaceNet for comparing them,
EfficientFormerV2 for labels. Models do
not learn from your library.

**Originals.** Your photo files, exactly
as they are on disk. PhotoPrism reads
them and never modifies them.

**Place.** The named location —
city, region, country — PhotoPrism
derives from a photo's GPS coordinates.

**Sidecar.** A small companion file
(`.xmp`, `.json`) that carries metadata
alongside a photo, instead of inside
it.

**SQLite / MariaDB.** The two database
engines the index can live in: SQLite
as one file, no server; MariaDB as a
service, for large libraries.

**Stack.** Several files PhotoPrism
treats as one photo — the same shot in
JPEG and raw, or the frames of a burst
— shown once, files kept together.

**Subject (person).** A named person in
the index. Naming a cluster turns its
faces into that person's photos.

**Thumbnail.** A small preview copy
PhotoPrism generates from an original
and actually serves in the web app,
stored by content hash in the storage
folder.

**XMP.** Adobe's open format for
metadata in a sidecar file — title,
caption, rating — readable by other
tools, so facts written there outlive
PhotoPrism.
