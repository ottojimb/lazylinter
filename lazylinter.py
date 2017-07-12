#!/usr/bin/env python
"""Main module for lazylinter."""

from __future__ import print_function
import glob
import sys
from time import sleep
from random import randint

counter = 0

for filename in glob.iglob('**/*', recursive=True):
    counter = counter + 1
    print("Analizing file {}...".format(filename))

    if not(len(sys.argv) > 1 and sys.argv[1] == '-f'):
        sleep(randint(0, 10) * 0.1)

    print("  -> OK...")

print("\nLinter finished. Everything is OK. {} files analized."
      .format(counter))
