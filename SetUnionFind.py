from __future__ import print_function
from collections import defaultdict
from graph import Graph,Vertex,V
from heap import Heap
import math
import sys
from datetime import datetime
import random

class SetUnionFind:
	def __init__(self):
		self.parent = [i for i in range(0,V)]
		self.rank = [1 for i in range(0,V)]
		self.max_size = V
	
	def __init__(self,size):
		self.parent = [i for i in range(0,V)]
		self.rank = [1 for i in range(0,V)]
		self.max_size = size

	def MakeSet(self,i):
		self.parent[i] = i
		self.rank[i] = 1

	def Union(self,i,j):
		if self.rank[i] > self.rank[j]:
			self.parent[j] = i
		elif self.rank[i] < self.rank[j]:
			self.parent[i] = j
		else:
			self.parent[j] = i
			self.rank[i] += 1

	def Find(self,i):
		w = i
		temp = list()
		while self.parent[w] != w:
			temp.append(w)
			w = self.parent[w]
		while len(temp)>0:
			i = temp[len(temp)-1]
			temp.pop()
			self.parent[i] = w
		return w





