#! /usr/bin/env sh

set -euo

main () {
    python -m manage migrate
    gunicorn "alexandria.wsgi:application"
}

main "$@"
