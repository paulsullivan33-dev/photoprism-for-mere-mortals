# Lab environment for the standalone PhotoPrism run.
# Source this before every photoprism command so they all share one config.
LAB="$HOME/workspace/photoprism-lab-work"

export LD_LIBRARY_PATH="$LAB/vips/root/usr/lib/x86_64-linux-gnu"
export PATH="$LAB/pkg/bin:$PATH"

export PHOTOPRISM_ASSETS_PATH="$LAB/pkg/assets"
export PHOTOPRISM_STORAGE_PATH="$LAB/storage"
export PHOTOPRISM_ORIGINALS_PATH="$LAB/originals"
export PHOTOPRISM_IMPORT_PATH="$LAB/import"
export PHOTOPRISM_DATABASE_DRIVER="sqlite"
export PHOTOPRISM_ADMIN_USER="admin"
# Throwaway lab password, stated in the guide text as such. Local loopback only.
export PHOTOPRISM_ADMIN_PASSWORD="photoprism-lab-password"
export PHOTOPRISM_AUTH_MODE="password"
export PHOTOPRISM_SITE_URL="http://127.0.0.1:2342/"
export PHOTOPRISM_HTTP_HOST="127.0.0.1"
export PHOTOPRISM_HTTP_PORT="2342"
export PHOTOPRISM_WORKERS="2"
export PHOTOPRISM_LOG_LEVEL="info"
