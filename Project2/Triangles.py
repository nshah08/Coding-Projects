from PIL import Image,ImageDraw
import random

class Triangle():
    def __init__(self):
        self.x1= random.randint(0,255)
        self.x2= random.randint(0,255)
        self.x3= random.randint(0,255)
        self.y1= random.randint(0,255)
        self.y2= random.randint(0,255)
        self.y3= random.randint(0,255)
        self.r= random.randint(0,255)
        self.g= random.randint(0,255)
        self.b= random.randint(0,255)
        self.t= random.randint(0,255)

    def drawtri(self,triangles):
        img=Image.new('RGBA',size=((256,256)))
        draw_img=ImageDraw.Draw(img)
        draw_img.polygon([(0,0),(0,255),(255,255),(255,0)], fill=(255,255,255,255))
        for triangle in triangles:
            triangle_img=Image.new('RGBA',size=((256,256)))
            draw_triangle = ImageDraw.Draw (triangle_img)
            draw_triangle.polygon ([(triangle.x1, triangle.y1) ,
                       (triangle.x2, triangle.y2),
                        (triangle.x3, triangle.y3)],
                        fill=(triangle.r,triangle.g,triangle.b,triangle.t))
            img= Image.alpha_composite(img,triangle_img)
        return img     

