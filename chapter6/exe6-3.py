# -*- coding: utf-8 -*-

from __future__ import division
from collections import Counter
import matplotlib.pyplot as plt  # pyplot

import math, random

def normal_cdf(x, mu=0, sigma=1):
    #PYTHON의 오차함수를 이용하면 MATH.ERF로 누적분포함수를 쉽게 구할 수 있음
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

#####중심극한 정리에 대한 이해 #######
#이항 확률 변수(binomial random variable) 는 n과 p두가지 파라미터로 구성되어있다.
#단순히 n개의 독립적인 베르누이 확률 변수를 더한것이다.
"""
베르누이 분포(Bernoulli Distribution)는 확률론과 통계학에서 매 시행마다 오직 두 가지의 가능한 결과만 일어난다고 할 때,
이러한 실험을 1회 시행하여 일어난 두 가지 결과에 의해 그 값이 각각 0과 1로 결정되는 확률변수 X에 대해서
결과가 0이 되는 경우의 확률은  p, 1 이되는 경우의 확률은 1-p
를 만족하는 확률변수 X가 따르는 확률분포를 의미하며, 이항 분포의 특수한 사례에 속한다.
"""
def bernoulli_trial(p):
    return 1 if random.random() < p else 0


def binomial(p, n):
    return sum(bernoulli_trial(p) for _ in range(n))


def make_hist(p, n, num_points):
    data = [binomial(p, n) for _ in range(num_points)]

    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            0.8,
            color='0.75')

    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
          for i in xs]
    plt.plot(xs, ys)
    plt.show()
if __name__ == "__main__":
     make_hist(0.75,100,10000)