from ngram import ngram
import os
import preprocess
from gt_ngram import gt_ngram
from li_ngram import li_ngram
import sys
import operator
import csv
import numpy as linspace
import math


stringWhole = "From : turpin@cs.utexas.edu ( Russell Turpin ) Subject : Re : centi - a milli - pedes - * - - - In article <1993Apr28.081953.21043@nmt.edu> msnyder@nmt.edu ( Rebecca Snyder ) writes : > Does anyone know how posionous centipedes and and millipedes are ? ... The millipede's around here here ( Austin ) have no sting . Some of there centipedes do . The question Rebecca Snyder asks is much like asking How venomous are snakes ? One either wants too ask which snake ? or point too some reference on there many different species of snake . Similarly , the are many different species of millipede a centipede . ( These are different families ; millipedes have too pairs of legs per body segment , while centipedes have but one pair . ) Sorry if this information is not useful . Russell"

print stringWhole[70], stringWhole[71]