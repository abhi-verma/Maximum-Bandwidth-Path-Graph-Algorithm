from __future__ import print_function
# from collections import defaultdict
from graph import Graph,Vertex,V,Edge
from heap import Heap
import math
import sys
from datetime import datetime
import random
from SetUnionFind import SetUnionFind
sys.setrecursionlimit(V+3)
# Status 0:in-tree 1:fringe 2:unseen

def DFS(G,s,t,DFSstatus,bw,parent):
	if s==t:
		return
	DFSstatus[s]=1
	neighbors = G.neighbors(s)
	for vertex in neighbors:
		if DFSstatus[vertex.dst] == 2:
			bw[vertex.dst] = min(bw[s],vertex.bw)
			parent[vertex.dst] = s
			DFS(G,vertex.dst,t,DFSstatus,bw,parent)
	DFSstatus[s] = 0
	return

def heapify(E,i,n):
	largest = i
	left = 2*i+1
	right = 2*i+2
	if left < n and E[left].bw > E[largest].bw:
		largest = left
	if right < n and E[right].bw > E[largest].bw:
		largest = right
	if largest != i:
		E[i],E[largest] = E[largest],E[i]
		heapify(E,largest,n)

def heapSort(G,E):
	for v in range(0,V):
		neighbors = G.neighbors(v)
		for neighbor in neighbors:
			if neighbor.dst >= v:
				E.append(Edge(v,neighbor.dst,neighbor.bw))
	n = len(E); 
	
	for i in range(int(n/2)-1,-1,-1):
		heapify(E,i,n)
	
	for i in range(n-1,-1,-1):
		E[0],E[i] = E[i], E[0]
		heapify(E,0,i)


def Kruskal(G,s,t):
	E = list()
	bw = [0]*V
	status = [2]*V
	heapSort(G,E)
	S = SetUnionFind(V)
	T = Graph(); 
	for i in range(len(E)-1,-1,-1):
		e = E[i]; 
		x = S.Find(e.src)
		y = S.Find(e.dst)
		if x != y: 
			T.addEdge(e.src,e.dst,e.bw)
			T.addEdge(e.dst,e.src,e.bw)
			S.Union(x,y)
		
	return KruskalPath(T,s,t)
	# return 0

def KruskalPath(T,s,t):
	parent = [-1]*V
	maxBW = sys.maxsize
	BW = [0]*V
	BW[s] = sys.maxsize
	DFSstatus = [2]*V
	DFS(T,s,t,DFSstatus,BW,parent)
	path = [0]*V
	i = 0
	while t != s:
		maxBW = min(maxBW, BW[t])
		path[i] = t
		t = parent[t]
		i += 1
	path[i] = s
	return maxBW

# def main():
# 	G = Graph()
# 	G.createGraphFromFile()
# 	bw2 = Kruskal(G,0,4)
# 	print("bw= ",bw2)

# main()


