# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:10:46 2022

@author: J SRI THRISHNA
"""




def printMaxActivities(s, f ):
	n = len(f)
	print ("The following activities are selected")
	i = 0
	print( i)
	for j in range(n):
		if s[j] >= f[i]:
			print (j)
			i = j

# Driver program to test above function
s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
printMaxActivities(s, f)

