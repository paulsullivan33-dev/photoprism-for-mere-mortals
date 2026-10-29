# Installing PhotoPrism

**Outcome: the PhotoPrism program is on
your machine, answers its version, and
is configured — before it ever starts —
to use a folder and database you chose.**

## The two routes, honestly

Most PhotoPrism documentation assumes
**Docker**: one compose file starts
PhotoPrism and its database together,
and the image bundles every support
program. If you run Docker already,
that route is the project's home turf
and nothing in this guide argues with
it.

This guide takes the other route: the
project's official **installation
packages** for Linux — a tarball holding
the program, its recognition libraries
and models, and the web app's files. The
project's own FAQ offers it for
experienced users, with three warnings
this guide takes seriously: the package
**must be updated by hand**, it comes
with **no default configuration**, and
it does **not include every system
dependency** its features can use. In
exchange you get one program you can
start, stop, and inspect like any other
— which suits a guide that wants to
show you the moving parts.

## What you need

- A 64-bit Linux machine (the lab used
  Ubuntu 24.04; the package needs glibc
  2.35 or newer, so Ubuntu 22.04 and
  Debian Bookworm are the floor).
- About 1 GB of disk for the unpacked
  package (the archive itself is about
  420 MB), plus room for thumbnails —
  roughly a tenth of your library's
  size, in the lab's small experience.
- The system **libvips** library, which
  the program loads at startup for image
  resizing:

```bash
sudo apt install libvips42t64
```

On Debian the same package is
`libvips42`. If `photoprism --version`
answers with `libvips.so.42: cannot open
shared object file`, this step is the
one that was missed — the lab met that
exact error first, and it is in the
transcripts.

Optional, for wider format coverage
(chapter 11): `exiftool`, `ffmpeg`,
and raw converters. JPEG photos need
none of them.

## Download and unpack

```bash
mkdir -p ~/photoprism-app
cd ~/photoprism-app
curl -LO https://dl.photoprism.app/pkg/linux/amd64.tar.gz
tar -xzf amd64.tar.gz
```

(On an ARM machine the file is
`arm64.tar.gz` instead.) The unpacked
tree is the whole application:

- `bin/photoprism` — the program;
- `lib/` — the TensorFlow and ONNX
  runtimes it bundles for itself, so
  recognition needs nothing from your
  system;
- `assets/` — the web app, and
  `assets/models/`, the recognition
  models themselves (about 200 MB of
  the total).

## Configure before you start

The package ships no configuration, so
you supply it — as a config file or as
**environment variables**, which is
what this guide uses, because every
setting stays visible in one place.
PhotoPrism reads variables named
`PHOTOPRISM_` plus the option name in
capitals. The lab ran with exactly
these (paths under the lab's home; a
real install would point originals at
the real library):

```bash
export PHOTOPRISM_ASSETS_PATH="$HOME/photoprism-app/assets"
export PHOTOPRISM_ORIGINALS_PATH="$HOME/photos"
export PHOTOPRISM_STORAGE_PATH="$HOME/photoprism-storage"
export PHOTOPRISM_DATABASE_DRIVER="sqlite"
export PHOTOPRISM_ADMIN_USER="admin"
export PHOTOPRISM_ADMIN_PASSWORD="choose-a-real-one"
export PHOTOPRISM_SITE_URL="http://127.0.0.1:2342/"
export PHOTOPRISM_HTTP_HOST="127.0.0.1"
export PHOTOPRISM_HTTP_PORT="2342"
```

Three of these deserve a sentence each.
**`DATABASE_DRIVER=sqlite`** keeps the
index in one file and removes the
database server from your life until
chapter 11 says otherwise. The
**admin password** is set at first
start and is the only login until you
add users — make it a real one; the
lab's was a stated throwaway. And
binding the **HTTP host to 127.0.0.1**
means the web app answers only on this
machine until you deliberately put a
reverse proxy in front of it (a recipe
points the way; exposing it is a
networking decision, not a default).

## The check

```bash
~/photoprism-app/bin/photoprism --version
```

The lab's run answered with its build
version and commit (transcript t00).
Then ask the program to repeat your
configuration back:

```bash
photoprism config
```

It prints every effective option —
paths, database driver, site URL — and
that table is the guide's recurring
check: whenever PhotoPrism surprises
you, `photoprism config` shows the
machine it thinks it is running on,
which is usually where the surprise
lives.

**Check:** `--version` answers, and
`photoprism config` shows *your*
originals and storage paths, not the
defaults. Chapter 4 starts the server
against a first small library.
