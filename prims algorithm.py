# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 12:01:09 2022

@author: J SRI THRISHNA
"""

import sys
class Graph():
    def __init__(self, vertices):
        self.v=vertices
        self.graph=[[0 for column in range(vertices)]
                    for row in range(vertices)]
        
        
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1,self.v):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
            
            
    def  minkey(self, key, mstSet):
        min= sys.maxsize
        for v in range(self.v):
            if key[v]< min and mstSet[v] == False:
                min=key[v]
                min_index=v
        return min_index
        
    def primMST(self):
        key=[sys.maxsize]*self.v
        parent=[None]*self.v
        key[0]=0
        mstSet =[False]* self.v
        parent[0]=-1

        for count in range(self.v):
            u=self.minkey(key, mstSet)
            mstSet[u]=True
            for v in range(self.v):
                if self.graph[u][v]>0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v]=self.graph[u][v]
                    parent[v]=u
        self.printMST(parent)
        
g= Graph(5)
g.graph=[[0,2,0,6,0],
         [2,0,3,8,5],
         [0,3,0,0,7],
         [6,8,0,0,9],
         [0,5,7,9,0]]
g.primMST()
        
                
    