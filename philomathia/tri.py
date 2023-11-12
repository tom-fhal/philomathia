import numpy as np  
import random as random


def insertionsort(tab) :
    for i in range(1,len(tab)):
        x = tab[i]
        j = i-1
        while j>=0 and x<tab[j] :
            tab[j+1] = tab[j]
            j -= 1
        tab[j+1] = x
      
    return tab


def bubblesort(tab):

    for i in range(len(tab)):
        for j in range(len(tab)-1):

            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]

    return tab

def mergesort(tab):
    #diviser la liste tab en deux
    if len(tab)<=1:
        return tab
    mid = len(tab)//2
    right = tab[mid:]
    left = tab[:mid]
    
    mergesort(right)
    mergesort(left)

    i=0
    j=0
    k=0

    while i<len(right) and j<len(left):
        if right[i]<left[j]:
            tab[k]=right[i]
            i+=1
        else:
            tab[k]=left[j]
            j+=1
        k+=1

    while i<len(right):
        tab[k]=right[i]
        i+=1
        k+=1

    while j<len(left):
        tab[k]=left[j]
        j+=1
        k+=1

    return tab

def quicksort(tab):
    if len(tab)<=1:
        return tab
    x = tab[0]
    left = []
    right = []
    for i in range(1,len(tab)):
        if tab[i]<x:

            left.append(tab[i])
        else:
            right.append(tab[i])
    
    return quicksort(left)+[x]+quicksort(right)

