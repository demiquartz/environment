#!/usr/bin/python3

import subprocess

subprocess.run([
    "rm",
    "-rf",
    "bin",
    "build",
    "doc",
    "lib",
    "Doxyfile"
])
