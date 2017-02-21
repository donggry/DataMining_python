# -*- coding: utf-8 -*-

from __future__ import division
from collections import Counter
import matplotlib.pyplot as plt  # pyplot

import math, random


def random_kid():
    return random.choice(["boy", "girl"])

if __name__ == "__main__":

    both_girls = 0
    older_girl = 0
    either_girl = 0

    random.seed(0) #매번 결과가 같게 만들어준다.
    for _ in range(10000):
        younger = random_kid()#둘째
        older = random_kid()#첫째
        if older == "girl":
            older_girl += 1
        if older == "girl" and younger == "girl":
            both_girls += 1
        if older == "girl" or younger == "girl":
            either_girl += 1

    print "P(both | older):", both_girls / older_girl  # 0.514 ~ 1/2
    print "P(both | either): ", both_girls / either_girl  # 0.342 ~ 1/3
