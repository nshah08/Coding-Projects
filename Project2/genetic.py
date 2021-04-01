from PIL import Image
import Triangles
import numpy as np
import random

class genes():
    def __init__(self):
        self.population=10

    
    def fitness(self,target,test):
        gene_pixel = np.array([])     
        for p in test.split()[:-1]:    
            gene_pixel = np . hstack((gene_pixel, np.hstack(np.array(p)))) 
        target_pixel = np.array([])
        for p in target.split()[:-1 ]:
            target_pixel = np.hstack((target_pixel, np.hstack(np.array(p))) )
        return np.sum (np.square (np.subtract (gene_pixel, target_pixel)))
    
    
    def mutate(self,rate,triangle):
        if rate>random.random():
            child=Triangles.Triangle()
            child.x1=max(0,min(255,triangle.x1+random.randint(-20,20)))
            child.x2=max(0,min(255,triangle.x2+random.randint(-20,20)))
            child.x3=max(0,min(255,triangle.x3+random.randint(-20,20)))
            child.y1=max(0,min(255,triangle.y1+random.randint(-20,20)))
            child.y2=max(0,min(255,triangle.y2+random.randint(-20,20)))
            child.y3=max(0,min(255,triangle.y3+random.randint(-20,20)))
            child.r=max(0,min(255,triangle.r+random.randint(-10,10),255))
            child.g=max(0,min(255,triangle.g+random.randint(-10,10),255))
            child.b=max(0,min(255,triangle.b+random.randint(-10,10),255))
            child.t=max(0,min(255,triangle.t+random.randint(-10,10),120))
            return child
        return triangle

    def crossover(self,rate,parent):
        selecter=random.randint(0,99)
        child=Triangles.Triangle()
        child=self.mutate(rate,parent[selecter])
        return child
        
            




