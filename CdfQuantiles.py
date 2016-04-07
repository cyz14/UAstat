#!/usr/bin python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def cdf_quantiles(array):
	# quantiles needed
	ppfx = [0.1, 0.2, 0.5, 0.8, 0.9, 0.99]

	xk = np.array(array)
	# print xk
	unique, counts = np.unique(xk, return_counts=True)
	# print counts
	total = np.sum(counts)
	pk = [1.0 * p / total for p in counts]
	# print unique
	# print pk
	custm = stats.rv_discrete(name='custm', values=(unique, pk))
	return [custm.ppf(x) for x in ppfx]


def test():
	ll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	print cdf_quantiles(ll)
