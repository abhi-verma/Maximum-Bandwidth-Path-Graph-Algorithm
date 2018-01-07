from __future__ import print_function
# from collections import defaultdict
from graph import Graph,Vertex,V
from heap import Heap
import math
import sys
from datetime import datetime
import random

# Status 0:in-tree 1:fringe 2:unseen

def maxfringe(bw,status):
	tempBW=0;TempStatus=0
	for i in range(V):
		if status[i] == 1 and tempBW<bw[i]:
			tempBW = bw[i]
			TempStatus = i
	return TempStatus


def dijkstra(G,s,t):
	bw = [0]*V
	parent = [-1]*V
	status = [2]*V
	
	status[s] = 0
	bw[s] = sys.maxsize

	neighbors = G.neighbors(s)
	for vertices in neighbors:
		bw[vertices.dst] =  vertices.bw
		parent[vertices.dst] = s
		status[vertices.dst] = 1

	while status[t] != 0:
		v = maxfringe(bw,status)
		status[v] = 0
		neighbors = G.neighbors(v)
		# print(v,len(neighbors))
		for i in range(len(neighbors)):
			w = neighbors[i].dst
			if status[w] == 2:
				bw[w] = min(bw[v],neighbors[i].bw)
				parent[w] = v
				status[w] = 1
			elif status[w] == 1 and bw[w]< min(bw[v], neighbors[i].bw):
				bw[w] = min(bw[v],neighbors[i].bw)
				parent[w] = v
	return bw[t]

def dijkstraWithHeap(G,s,t):
	bw = [0]*V
	parent = [-1]*V
	status = [2]*V
	heap = Heap()

	status[s] = 0
	bw[s] = sys.maxsize

	neighbors = G.neighbors(s)
	for vertices in neighbors:
		bw[vertices.dst] =  vertices.bw
		parent[vertices.dst] = s
		status[vertices.dst] = 1
		heap.insert(vertices.dst, bw[vertices.dst])

	while status[t] != 0:
		v = maxfringe(bw,status)
		# print(v,end=" ")
		status[v] = 0
		neighbors = G.neighbors(v)
		for i in range(len(neighbors)):
			w = neighbors[i].dst
			if status[w] == 2:
				bw[w] = min(bw[v],neighbors[i].bw)
				parent[w] = v
				status[w] = 1
				heap.insert(w,bw[w])
			elif status[w] == 1 and bw[w]< min(bw[v], neighbors[i].bw):
				heap.delete(w)
				bw[w] = min(bw[v],neighbors[i].bw)
				parent[w] = v
				heap.insert(w,bw[w])
	return bw[t]

# def main():
# 	G = Graph()
# 	t1 = datetime.now()
# 	G.createGraphG2()
# 	t2 = datetime.now()
# 	print("To create graph ", t2-t1)
# 	for i in range(5):
# 		num1 = random.randint(0,V-1)
# 		num2 = random.randint(0,V-1)
# 		if num1 == num2:
# 			continue
# 		t3 = datetime.now()
# 		bw = dijkstra(G,num1,num2)
# 		t4 = datetime.now()
# 		print("bw = ",bw)
# 		print("Dijkstra ",t4-t3)
# 		t5 = datetime.now()
# 		bw1 = dijkstraWithHeap(G,num1,num2)
# 		t6 = datetime.now()
# 		print("bw1 = ",bw1)
# 		print("dijkstraWithHeap ",t6-t5)

# main()

