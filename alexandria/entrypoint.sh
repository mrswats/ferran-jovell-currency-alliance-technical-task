#! /usr/bin/env sh

set -euo

main () {
    gunicorn "alexandria.wsgi:application"
}

main "$@"
