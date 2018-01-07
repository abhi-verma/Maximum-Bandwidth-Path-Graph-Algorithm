from __future__ import print_function
from collections import defaultdict
import random
 
V = 5000

class Vertex:
	def __init__(self,dst=0,bw=0):
		self.dst = dst
		self.bw = bw

class Edge:
	def __init__(self,src,dst,bw):
		self.src = src
		self.dst = dst
		self.bw = bw

# This class represents a directed graph using adjacency
# list representation
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def neighbors(self,u):
		return self.graph[u]

	def exists(self,i,j):
		vertices = self.graph[i]
		for v in vertices:
			if v.dst == j:
				return True
		return False

	# function to add an edge to graph
	def addEdge(self,u,v,bw):
		temp = Vertex(v,bw)
		self.graph[u].append(temp)

	def createGraphG1(self):
		for i in range(int(V/2)):
			while len(self.graph[i])<8:
				j = random.randint(0,V-1)
				if j != i and self.exists(i,j) == False and len(self.graph[j])<8:
					w = random.randint(1,1000)
					self.addEdge(i,j,w)
					self.addEdge(j,i,w)

	def createGraphG2(self):
		# deg = [0]*V
		for i in range(int(V/2)):
			# cnt = 0
			while len(self.graph[i])<0.2*V:
				j = random.randint(0,V-1)
				if j != i and self.exists(i,j) == False and len(self.graph[j])<0.2*V:
					w = random.randint(1,1000)
					self.addEdge(i,j,w)
					self.addEdge(j,i,w)
				# cnt +=1
			# print(i,cnt,end="  ")

	def createGraphFromFile(self):
		with open("InputGraph.txt") as f:
			content = f.readlines()
			content = [x.strip() for x in content]
			for line in content:
				i = int(line[0]); j = int(line[2]); w = int(line[4])
				self.addEdge(i,j,w)
				self.addEdge(j,i,w)



	def printGraph(self):
		for i in range(len(self.graph)):
			for j in self.graph[i]:
				print(j.dst,"->",j.bw,end=" ")
			print("\n")
		# print(len(self.graph), len(self.graph[0]))

# def main():
# 	g = Graph()
# 	g.createGraphFromFile()
# 	g.printGraph()

# main()

