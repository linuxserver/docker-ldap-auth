#!/bin/sh
''''which python  >/dev/null && exec python  "$0" "$@" # '''

from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key.decode())
