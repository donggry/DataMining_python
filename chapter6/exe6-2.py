# -*- coding: utf-8 -*-

from __future__ import division
from collections import Counter
import matplotlib.pyplot as plt  # pyplot

import math, random
#균등분포(uniform distribution)-0과 1 사이의 모든값에 동등한 비중을 준 분포
#확률밀도함수 (probability density dunction -pdf)

def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0

def uniform_cdf(x):
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1
#균등분포의 누적분포함수
def plot_uniform_cdf(plt):
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [uniform_cdf(x) for x in xs], '-')
    plt.axis([-2, 3, -1, 2])
    plt.show()

def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

#정규분포 그리기
def plot_normal_pdfs(plt):
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
    plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
    plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1,sigma=1')
    plt.legend()
    plt.show()

def normal_cdf(x, mu=0, sigma=1):
    #PYTHON의 오차함수를 이용하면 MATH.ERF로 누적분포함수를 쉽게 구할 수 있음
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

#정규분포의 누적분포함수  그리기
def plot_normal_cdfs(plt):
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
    plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
    plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
    plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-.', label='mu=-1,sigma=1')
    plt.legend(loc=4)  # bottom right
    plt.show()

####중요!!!
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
#표준정규분포는 평균과 편차로 표현할 수 있고, 허용 오차는 0.00001 범위 내에서 확률변수를 찾아낸다.
#이진 탐색알고리즘을 이용하여 역함수를 근사함-누적분포함수가 연속 및 증가함수라는 점을 이용
#원하는 확률 값에 가까워 질 때까지 표준정규분포의 구간을 반복적으로 이등분한다.
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0 #-10의 누적분포함수 값은 0에 근접
    hi_z, hi_p = 10.0, 1 #10의 누적분포함수 값은 1에 근접
    while hi_z - low_z > tolerance: #허용 오차 범위 내에 들어갈 때 까지 반복수행
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z

if __name__ == "__main__":
    plot_uniform_cdf(plt)
    plot_normal_pdfs(plt)
    plot_normal_cdfs(plt)
    print inverse_normal_cdf(0.7,5,10)
