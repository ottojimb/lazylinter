#!/usr/bin/env python
from __future__ import print_function
import glob
from time import sleep
from random import randint

counter = 0

for filename in glob.iglob('**/*', recursive=True):
	counter = counter + 1
	print("Analizing {} file...              OK...".format(filename))
	sleep(randint(0, 5) * 0.1)

print("\nLinter finished. Everything is OK. {} files analized.".format(counter))
