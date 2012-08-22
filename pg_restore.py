#!/usr/bin/env python

import sys

def dburl2dict(url):
    dbn, rest = url.split('://', 1)
    user, rest = rest.split(':', 1)
    pw, rest = rest.split('@', 1)
    host, rest = rest.split(':', 1)
    port, rest = rest.split('/', 1)
    db = rest
    return (pw, host, user, db, port)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        d = dburl2dict(sys.argv[1])
        cmd = "PGPASSWORD=%s pg_restore --verbose --clean --no-acl --no-owner -h %s -U %s -d %s -p %s " % d
        cmd += sys.argv[2]
        print cmd
        # TODO run command


