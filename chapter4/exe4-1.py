# -*- coding: iso-8859-15 -*-

from __future__ import division  # want 3 / 2 == 1.5
import re, math, random  # regexes, math functions, random numbers
import matplotlib.pyplot as plt  # pyplot
from collections import defaultdict, Counter
from functools import partial

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)]
            for i in range(num_rows)]

def is_diagonal(i, j):
    return 1 if i == j else 0

def make_graph_dot_product_as_vector_projection():
    v = [2, 1]
    w = [math.sqrt(.25), math.sqrt(.75)]
    c = dot(v, w)
    vonw = scalar_multiply(c, w)
    o = [0, 0]

    plt.arrow(0, 0, v[0], v[1],width=0.02, head_width=.1, length_includes_head=True)
    # length_includes_head :화살표머리가 길이에 포함되는지 안되는지
    # width:화살표 몸통의 두께
    # head_width:화살표 머리의 크기
    plt.annotate("v", v, xytext=[v[0] + 0.1, v[1]]) #라벨링하기,라벨 위치 xytext로 미세조정하기
    plt.arrow(0, 0, w[0], w[1],width=0.002, head_width=.1, length_includes_head=True)
    plt.annotate("w", w, xytext=[w[0] - 0.1, w[1]])
    plt.arrow(0, 0, vonw[0], vonw[1], length_includes_head=True)
    plt.annotate(u"(v•w)w", vonw, xytext=[vonw[0] - 0.1, vonw[1] + 0.1])
    plt.arrow(v[0], v[1], vonw[0] - v[0], vonw[1] - v[1],
              linestyle='dotted', length_includes_head=True)
    #linestyle : 화살표 몸통의 스타일 점선 화살표
    #print zip(v, w, o)
    #>>>[(2, 0.5, 0), (1, 0.8660254037844386, 0)]
    plt.scatter(*zip(v, w, o), marker='.')
    plt.axis('equal')
    plt.show()


if __name__ == "__main__":
    make_graph_dot_product_as_vector_projection()