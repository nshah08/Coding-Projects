import random
import copy
import time
import sys
from collections import defaultdict


class board:
    def __init__(self,dim):
        self.dim=dim
        self.board=[]
        self.pstate=[]
        self.visited=[]
        self.new=[]
        self.num=0

    def create(self):
        random.seed()
        for i in range(self.dim):
            self.board.append([])
            for j in range(self.dim):
                self.board[i].append(1)
        x=random.randint(0, self.dim-1)
        y=random.randint(0,self.dim-1)
        self.board[x][y]=0
        
    def print(self,printer):
        for i in printer:
            print(i)
        print("\n")
    
    def completed(self,check):
        count=0
        for i in range (self.dim):
            for j in range(self.dim):
                if((check[i][j])==1):
                    count+=1
        if(count>1):
            return False
        else:  
            return True
    
    def succesor(self,state):
        self.pstate.append(state.copy())

    def movement(self,i,j,move): 
        if((move[i][j]==0)):
            if(i-1>0 and i-2>=0):
                if ((move[i-1][j]==1) and (move[i-2][j]==1)): #UP Movement FROM 0
                    self.new=copy.deepcopy(move)
                    self.new[i-1][j]=0
                    self.new[i-2][j]=0
                    self.new[i][j]=1
                    self.succesor(self.new)
                    self.print(self.new)
                    self.queue.append(self.new.copy())
                    self.new.clear()
                    print("(" ,i-2, "," ,j, ") to (",i,"," , j, ")")
            elif(j+1<self.dim and j+2<self.dim):
                if((move[i][j+1]==1) and (move[i][j+2]==1)): #Right Movement from 0
                    self.new = copy.deepcopy(move)
                    self.new[i][j]=1
                    self.new[i][j+1]=0
                    self.new[i][j+2]=0
                    self.succesor(self.new)
                    self.print(self.new)
                    self.queue.append(self.new.copy())
                    self.new.clear()
                    print("(" ,i, "," ,j+2, ") to (",i,"," , j, ")")
            elif(i+2<self.dim and i+1<self.dim):
                if((move[i+1][j]==1) and (move[i+2][j]==1)): #DOWN MOVEMENT FROM 0
                    self.new = copy.deepcopy(move)
                    self.new[i+1][j]=0
                    self.new[i][j]=1
                    self.new[i+2][j]=0
                    self.succesor(self.new)
                    self.print(self.new)
                    self.queue.append(self.new.copy())
                    self.new.clear()
                    print("(" ,i+2, "," ,j, ") to (",i,"," , j, ")")
            elif(j-1>0 and j-2>=0):
                if((move[i][j-1]==1) and (move[i][j-2]==1)): #LEFT MOVEMENT FROM 0
                    self.new = copy.deepcopy(move)
                    self.new[i][j]=1
                    self.new[i][j-1]=0
                    self.new[i][j-2]=0
                    self.succesor(self.new)
                    self.print(self.new)
                    self.queue.append(self.new.copy())
                    self.new.clear()
                    print("(" ,i, "," ,j-2, ") to (",i,"," , j, ")")
        elif(move[i][j]==1):
            if(i+2<self.dim and i+1<self.dim):
                if ((move[i+1][j]==1) and (move[i+2][j]==0)): #DOWN Movement FROM 1
                    self.new = copy.deepcopy(move)
                    self.new[i+1][j]=0
                    self.new[i+2][j]=1
                    self.new[i][j]=0
                    self.succesor(self.new)
                    self.print(self.new)
                    self.queue.append(self.new.copy())
                    self.new.clear()
                    print("(" ,i, "," ,j, ") to (",i+2,"," , j, ")")
            elif(j-1>0 and j-2>=0): #LEFT MOVEMENT FROM 1
                if((move[i][j-1]==1) and (move[i][j-2]==0)):
                    self.new = copy.deepcopy(move)
                    self.new[i][j]=0
                    self.new[i][j-1]=0
                    self.new[i][j-2]=1
                    self.succesor(self.new)
                    self.print(self.new)
                    self.queue.append(self.new.copy())
                    self.new.clear()
                    print("(" ,i, "," ,j, ") to (",i,"," , j-2, ")")
            elif(i+1<self.dim and i+2<self.dim):
                if((move[i-1][j]==1) and (move[i-2][j]==0)): #UP MOVEMENT FROM 1
                    self.new = copy.deepcopy(move)
                    self.new[i-1][j]=0
                    self.new[i][j]=0
                    self.new[i-2][j]=1
                    self.succesor(self.new)
                    self.print(self.new)
                    self.queue.append(self.new.copy())
                    self.new.clear()
                    print("(" ,i, "," ,j, ") to (",i-2,"," , j, ")")
            elif(j+2<self.dim and j+1<self.dim):
                if((move[i][j+2]==0) and (move[i][j+1]==1)): #RIGHT MOVEMENT FROM 1
                    self.new = copy.deepcopy(move)
                    self.new[i][j]=0
                    self.new[i][j+1]=0
                    self.new[i][j+2]=1
                    self.succesor(self.new)
                    self.print(self.new)
                    self.queue.append(self.new.copy())
                    self.new.clear()
                    print("(" ,i, "," ,j, ") to (",i,"," , j+2, ")")

    def bfs(self):
        bstate=[]
        self.queue=[]
        nexplored=0
        self.queue.append(self.board.copy())
        start=time.time()
        while self.queue:
            bstate=self.queue.pop(0)
            if(self.completed(bstate)==True):
                end=time.time()
                self.print(bstate)
                print("Solution Found")
                print("Nodes Visited: ", nexplored)
                print("Execution Time: ", end-start, " seconds")
                sys.exit()
            nexplored+=1
            if bstate not in self.visited:
                self.visited.append(bstate.copy())
                for i in range(self.dim):
                    for j in range(self.dim):
                        self.movement(i,j,bstate)
        if(self.completed(bstate)==False):
                end=time.time()
                self.print(bstate)
                print("No Solution Found")
                print("Nodes Visited: ", nexplored)
                print("Execution Time: ", end-start, " seconds")

    
    def dfs(self):
        dstate=copy.deepcopy(self.board)
        nexplored=0
        self.print(dstate)
        start = time.time()
        nexplored=self.dfsmovement(dstate,nexplored,start)
        end=time.time()
        print("No Solution Found")
        print("Nodes Visited: ", nexplored)
        print("Execution Time: ", end-start, " seconds")




    def dfsmovement(self,move,nexplored,start):
        if self.completed(move)==True:
            end=time.time()
            for item in self.visited:
                self.print(item)
            print("Solution Found")
            print("Nodes Visited: ", nexplored)
            print("Execution Time: ", end-start, " seconds")
            sys.exit()
            return nexplored

        else:
            for i in range(self.dim):
                for j in range(self.dim):
                    if((move[i][j]==0)):
                        if(i-1>0 and i-2>=0):
                            if ((move[i-1][j]==1) and (move[i-2][j]==1)): 
                                new=copy.deepcopy(move)
                                new[i-1][j]=0
                                new[i-2][j]=0
                                new[i][j]=1
                                if new not in self.visited:
                                    nexplored+=1
                                    self.visited.append(new)
                                    nexplored=self.dfsmovement(new,nexplored,start)
                                    self.visited.remove(new)
                        elif(j+1<self.dim and j+2<self.dim):
                            if((move[i][j+1]==1) and (move[i][j+2]==1)): 
                                new = copy.deepcopy(move)
                                new[i][j]=1
                                new[i][j+1]=0
                                new[i][j+2]=0
                                if new not in self.visited:
                                    nexplored+=1
                                    self.visited.append(new)
                                    nexplored=self.dfsmovement(new,nexplored,start)
                                    self.visited.remove(new)
                        elif(i+2<self.dim and i+1<self.dim):
                            if((move[i+1][j]==1) and (move[i+2][j]==1)): 
                                new = copy.deepcopy(move)
                                new[i+1][j]=0
                                new[i][j]=1
                                new[i+2][j]=0
                                if new not in self.visited:
                                    nexplored+=1
                                    self.visited.append(new)
                                    nexplored=self.dfsmovement(new,nexplored,start)
                                    self.visited.remove(new)
                        elif(j-1>0 and j-2>=0):
                            if((move[i][j-1]==1) and (move[i][j-2]==1)): 
                                new = copy.deepcopy(move)
                                new[i][j]=1
                                new[i][j-1]=0
                                new[i][j-2]=0
                                if new not in self.visited:
                                    nexplored+=1
                                    self.visited.append(new)
                                    nexplored=self.dfsmovement(new,nexplored,start)
                                    self.visited.remove(new)
                    elif(move[i][j]==1):
                        if(i+2<self.dim and i+1<self.dim):
                            if ((move[i+1][j]==1) and (move[i+2][j]==0)): 
                                new = copy.deepcopy(move)
                                new[i+1][j]=0
                                new[i+2][j]=1
                                new[i][j]=0
                                if new not in self.visited:
                                    nexplored+=1
                                    self.visited.append(new)
                                    nexplored=self.dfsmovement(new,nexplored,start)
                                    self.visited.remove(new)
                        elif(j-1>0 and j-2>=0): 
                            if((move[i][j-1]==1) and (move[i][j-2]==0)):
                                new = copy.deepcopy(move)
                                new[i][j]=0
                                new[i][j-1]=0
                                new[i][j-2]=1
                                if new not in self.visited:
                                    nexplored+=1
                                    self.visited.append(new)
                                    nexplored=self.dfsmovement(new,nexplored,start)
                                    self.visited.remove(new)
                        elif(i+1<self.dim and i+2<self.dim):
                            if((move[i-1][j]==1) and (move[i-2][j]==0)): 
                                new = copy.deepcopy(move)
                                new[i-1][j]=0
                                new[i][j]=0
                                new[i-2][j]=1
                                if new not in self.visited:
                                    nexplored+=1
                                    self.visited.append(new)
                                    nexplored=self.dfsmovement(new,nexplored,start)
                                    self.visited.remove(new)
                        elif(j+2<self.dim and j+1<self.dim):
                            if((move[i][j+2]==0) and (move[i][j+1]==1)): 
                                new = copy.deepcopy(move)
                                new[i][j]=0
                                new[i][j+1]=0
                                new[i][j+2]=1
                                if new not in self.visited:
                                    nexplored+=1
                                    self.visited.append(new)
                                    nexplored=self.dfsmovement(new,nexplored,start)
                                    self.visited.remove(new)
            return nexplored