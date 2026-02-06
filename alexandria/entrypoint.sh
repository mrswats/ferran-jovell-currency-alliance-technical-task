#! /usr/bin/env sh

set -euo

main () {
    python -m manage migrate
    python -m gunicorn \
        --bind "0.0.0.0:8080" \
        "alexandria.wsgi:application"
}

main "$@"
