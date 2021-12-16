#!/usr/bin/python3
""" Takes an argument and returns exit status """
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)
    elif not os.path.exists("./README.md"):
        print("Missing README.md")
        sys.exit(1)
    else:
        sys.exit(0)
