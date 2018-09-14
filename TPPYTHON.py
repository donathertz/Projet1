# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
from math import sqrt
def f(x):
    return (3*x+1)/(2*x+1)
a=1
liste=[a]
liste.append(f(liste[-1]))

f= lambda x:(3*x+1)/(2*x+1)

def iteration(a,f,n):
    liste=[a]
    for i in range(n):
        liste.append(f(liste[-1]))
    return liste
        
def est_premier1(n):
    i=2
    if n==1:
        return False
    while n%i==0 and n!=2:
        i+=1
        return False
    return True

def est_premier(n):
    #if not (n.is_integer()):
     #   return "Le nombre n'est pas premier"
    if n in [0,1]or n<0:
        return False
    for k in range(2,int(sqrt(n)+1)):
        if n%k==0:
            return False
    return True
"fonction qui affiche le nombe de nombre premier < a n"
def listepremiers(n):
    liste = []#on crée une liste vide
    for k in range(2,n):
        if est_premier(k):
            liste.append(k)#pour rajouter un elt à droite de la liste
    return liste

#def erastosthème(n):
 #   i=2
  #  liste=[i]
def racine(liste):
    newliste=[]
    for a in liste:
        newliste.append(math.sqrt(a))
    return newliste

def eratosthene(n):
    l=[2]
    for i in range(3,n,2):
        for k in l:
            if i%k==0:
                break
            if k**2 > i:
                l.append(i)
                break
    return l

#import numpy as np

#np.array([[1,2],[3,4]])
#Out[3]:
#array([[1, 2],
 #      [3, 4]])

#np.linalg.det(np.array([[1,2],[2,3]]))" CALCUL DU DETERMINANT
#Out[4]: -1.0

#np.linalg.det(np.array([[1,2],[2,3]]))
#Out[5]: -1.0

#np.linalg.det(np.array([[1,2],[3,4]]))
#Out[6]: -2.0000000000000004

#1*4-3*2
#Out[7]: -2

#m=np.array([[1,2],[3,4]])

#m
#Out[9]: 
#array([[1, 2],
#       [3, 4]])

#np.linalg.eig(m) # CALCUL DES VALEURS PROPRES
#Out[10]: 
#(array([-0.37228132,  5.37228132]), array([[-0.82456484, -0.41597356],
#        [ 0.56576746, -0.90937671]]))
#
#[i**2 for i in range(5)]
#Out[11]: [0, 1, 4, 9, 16]""
 
def hilb(n):
    L=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(1/(i+j+1))
        L.append(l)
    return np.array(L)

def hilb2(n):
    L=[[1/(i+j+1) for j in range(n)] for i in range(n)]
    return np.array(L)

def dessin():
    for i in range(1,10):
        plt.plot(x,x**i,label=f'y = x**{i}')
    plt.title("un beau dessin")
    plt.xlabel("abscisse")
    plt.ylabel("ordonee")
    plt.legend()

def dessin2():
    plt.plot(x,x**2,label="x**2") #pour afficher la légende de la courbe en abscisse"
    plt.plot(x,x**3,label="x**3") #pour afficher la légende de la courbe en ordonnée"
    plt.legend() #pour afficher la légende"





        
    