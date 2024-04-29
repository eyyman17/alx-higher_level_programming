#!/usr/bin/python3
""" a script that fetches https://alx-intranet.hbtn.io/status """


from urllib import request
with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
    content = resp.read()
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode()}")
