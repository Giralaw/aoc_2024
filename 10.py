#! /usr/bin/env python3

# Advent of Code 2024 Day 10

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]

dirs2 = [(-1,0),(0,1),(1,0),(0,-1)]

# neighbor directions ordered to go clockwise start from right in a
# list-of-lists grid (i.e. (0,0) is top left corner)
adj8 = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

import sys, string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *
from statistics import mode, multimode

infile = sys.argv[1] if len(sys.argv)>=2 else '10.in'

data = open(infile).read().strip()
G = data.split('\n')

p1 = 0
p2 = 0

# this option assumes each line should be treated separately
for line in G:
    words = line.split()
    pass

# if you want input file to be one long string instead, use this and comment prev section
#''.join(lines)

for line in G:
    pass


print('p1 is ', p1)
print('p2 is ', p2)