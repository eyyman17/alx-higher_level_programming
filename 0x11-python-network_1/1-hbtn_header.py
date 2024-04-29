#!/usr/bin/python3
""" Response header Value """

from urllib import request, parse
import sys
if __name__ == "__main__":
    data = parse.urlendcode({'email':sys.argv[2]}).encode()
    req = request.Request(sys.argv[1], data=data)
    with request.urlopen(req) as res:
        print(f"{res.read().decode()}")
