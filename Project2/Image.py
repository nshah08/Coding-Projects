import Triangles
import genetic
from PIL import Image, ImageDraw,ImageColor

def main():
    name=input("Enter the full name of the Image: ")
    print("What reproduction would you like?")
    print("1.Asexual")
    print("2.Sexual")
    selection=int(input("Enter Number: "))
    target= Image.open(name)
    target=target.resize((256,256))
    target=target.convert("RGBA")
    parent_img=[]
    parent_triangles=[]
    for i in range(20):
        parent_triangles.append([])
        for j in range(100):
            parent_triangles[i].append(Triangles.Triangle())
        parent_img.append(Triangles.Triangle().drawtri(parent_triangles[i]))
    match_rates=[]
    for i in range(20):
        match_rates.append(genetic.genes().fitness(target,parent_img[i]))
    parent=parent_triangles[match_rates.index(min(match_rates))]
    parent_triangles.remove(parent)
    parent2=parent_triangles[match_rates.index(min(match_rates))]
    del parent_img
    del parent_triangles 
    if(selection==1):
        mutate_rate=0.5
        for count in range(3000000):
            child_img=[]
            child_triangles=[]
            for i in range(10):
                child_triangles.append([])
                for j in range(100):
                    child_triangles[i].append(genetic.genes().mutate(mutate_rate,parent[j]))
                child_img.append(Triangles.Triangle().drawtri(child_triangles[i]))
            match_rates=[]
            for i in range(10):
                match_rates.append(genetic.genes().fitness(target,child_img[i]))
            if(genetic.genes().fitness(Triangles.Triangle().drawtri(parent),target)>min(match_rates)):
                parent=child_triangles[match_rates.index(min(match_rates))]
            del child_triangles
            del child_img
            if(count%100==0): 
                save_img=Triangles.Triangle().drawtri(parent)
                save_img.save(str(count) + ".png")
    elif(selection==2):
        mutate_rate=0.05
        for count in range(999999999999999):
            child_img=[]
            child_triangles=[]
            for i in range(10):
                child_triangles.append([])
                for j in range(100):
                    if(j<=50):
                        child_triangles[i].append(genetic.genes().crossover(mutate_rate,parent))
                    elif(j>50):
                        child_triangles[i].append(genetic.genes().crossover(mutate_rate,parent2))
                child_img.append(Triangles.Triangle().drawtri(child_triangles[i]))
            match_rates=[]
            for i in range(10):
                match_rates.append(genetic.genes().fitness(target,child_img[i]))
            if(genetic.genes().fitness(Triangles.Triangle().drawtri(parent),target)>min(match_rates)):
                parent=child_triangles[match_rates.index(min(match_rates))]
                l2=seclowest(match_rates)
                parent2=child_triangles[match_rates.index(l2)]
            del child_triangles
            del child_img
            if(count%100==0): 
                save_img=Triangles.Triangle().drawtri(parent)
                save_img.save(str(count) + ".png")


def seclowest(list1):
    list1.sort() 
    return (list1[1])




main()