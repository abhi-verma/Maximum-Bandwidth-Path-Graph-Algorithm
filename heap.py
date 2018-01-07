from __future__ import print_function
# from collections import defaultdict
from graph import Vertex,V
import math


def parent(i):
	return math.ceil((i/2)-1)

class Heap:

	def __init__(self):
		self.heap = list()
		self.position = [-1 for i in range(V)]

	def heapify(self,i):
		largest = i
		left = 2*i+1
		right = 2*i+2

		if left<len(self.heap) and self.heap[left].bw > self.heap[largest].bw:
			largest = left
		if right<len(self.heap) and self.heap[right].bw > self.heap[largest].bw:
			largest = right
		if largest != i:
			self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
			self.position[self.heap[i].dst] = i
			self.position[self.heap[largest].dst] = largest
			self.heapify(largest)

	def insert(self, v, bw):
		if len(self.heap) == V:
			return
		vertex = Vertex(v,bw)
		self.heap.append(vertex)
		i = len(self.heap)-1
		self.position[v] = i
		while i!=0 and self.heap[parent(i)].bw < self.heap[i].bw:
			self.heap[i], self.heap[parent(i)] = self.heap[parent(i)], self.heap[i]
			self.position[self.heap[i].dst] = i
			self.position[self.heap[parent(i)].dst] = parent(i)
			i = parent(i)

	def delete(self, v):
		positionInHeap = self.position[v]
		if positionInHeap > V:
			return
		i = len(self.heap)-1
		self.heap[i],self.heap[positionInHeap] = self.heap[positionInHeap], self.heap[i]
		self.position[self.heap[positionInHeap].dst] = positionInHeap
		self.heap.pop()
		self.position[v] = -1
		self.heapify(positionInHeap)
		return

	def maximum(self):
		return self.heap[0].dst

# def main():
# 	heap = Heap();
# 	heap.insert(2,4)
# 	heap.insert(1,7)
# 	heap.insert(8,7)
# 	heap.insert(3,100)
# 	heap.insert(4,2)
# 	heap.insert(6,14)

# 	print(heap.maximum())
# 	heap.delete(3)
# 	heap.delete(6)
# 	print(heap.maximum())

# main()





