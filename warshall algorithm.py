# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 11:47:51 2022

@author: J SRI THRISHNA
"""

nv=3
INF=999
def floyd(G):
    dist=list(map(lambda p: list(map(lambda q: q,p)),G))
    for r in range(nv):
        for p in range(nv):
            for q in range(nv):
                dist[p][q]=min(dist[p][q],dist[p][r]+dist[r][q])
    sol(dist)

def sol(dist):
    for p in range(nv):
        for q in range(nv):
            if(dist[p][q]==INF):
                print("INF", end=" ")
            else: 
                print(dist[p][q],end=" ")
        print(" ")

G=eval(input()) # should be in the matrix form [[],[],[]]
floyd(G)














