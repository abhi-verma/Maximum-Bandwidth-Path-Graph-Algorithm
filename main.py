from __future__ import print_function
from graph import Graph,Vertex,V
from heap import Heap
from kruskal import Kruskal
import math
import sys
sys.setrecursionlimit(10000)
from datetime import datetime
import random
from dijkstra import dijkstra
from dijkstra import dijkstraWithHeap

def main():
	G = Graph()
	t1 = datetime.now()
	G.createGraphG1()
	t2 = datetime.now()
	print("Time to create sparse graph G1 ", t2-t1)
	print("Source, Destination","\t\t\t","Dijkstra With Heap","\t\t\t","Dijkstra without Heap ","\t\t\t","Kruskal")
	for i in range(5):
		num1 = random.randint(0,V-1)
		num2 = random.randint(0,V-1)
		if num1 == num2:
			continue
		t3 = datetime.now()
		bw = dijkstra(G,num1,num2)
		t4 = datetime.now()
		t5 = datetime.now()
		bw1 = dijkstraWithHeap(G,num1,num2)
		t6 = datetime.now()
		t7 = datetime.now()
		bw2 = Kruskal(G,num1,num2)
		t8 = datetime.now()
		print(num1,num2,"\t\t\t",bw,t4-t3,"\t\t\t",bw1,t6-t5,"\t\t\t",bw2,t8-t7)

	t1 = datetime.now()
	T = Graph()
	T.createGraphG2()
	t2 = datetime.now()
	print("Time to create dense graph G2 ", t2-t1)
	print("Source, Destination","\t\t\t","Dijkstra With Heap","\t\t\t","Dijkstra without Heap","\t\t\t","Kruskal")
	for i in range(5):
		num1 = random.randint(0,V-1)
		num2 = random.randint(0,V-1)
		if num1 == num2:
			continue
		t3 = datetime.now()
		bw = dijkstra(T,num1,num2)
		t4 = datetime.now()
		t5 = datetime.now()
		bw1 = dijkstraWithHeap(T,num1,num2)
		t6 = datetime.now()
		t7 = datetime.now()
		bw2 = Kruskal(T,num1,num2)
		t8 = datetime.now()
		print(num1,num2,"\t\t\t",bw,t4-t3,"\t\t\t",bw1,t6-t5,"\t\t\t",bw2,t8-t7)

main()