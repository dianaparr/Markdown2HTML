#!/usr/bin/python3
""" Takes an argument and returns exit status """
import sys
import os
from typing import Counter

if __name__ == "__main__":
    file_html = []
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)
    if not os.path.exists("./README.md"):
        print("Missing README.md")
        sys.exit(1)
    with open("./README.md", "r") as file:
        for rows in file.readlines():
            counter_tag = 0
            for row in rows:
                for chr in range(len(row)):
                    if row[chr] == '#':
                        counter_tag += 1
            rows = rows.rstrip('\r\n')
            file_html.append(f"<h{counter_tag}>\
{rows.replace('#','')}</h{counter_tag}>")
        with open("./README.html", "a") as file:
            for row in file_html:
                file.write(f"{row}\n")
        sys.exit(0)
