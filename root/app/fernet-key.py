#!/bin/sh
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''

from cryptography.fernet import Fernet

key = Fernet.generate_key()
print key
