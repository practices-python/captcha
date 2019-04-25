#this code can get the number of the simple captchas
__author__="Ali Reza Bahrami"


from PIL import Image
from os import getcwd as current_dir
image1=Image.open(current_dir()+"\\captcha.jpg")
width,height=image1.size
bucket=[]
best_match=[]
number=""

def apply_blackwhite_filter(img):
    for y in range(height):
        for x in range(width):
            r,g,b=img.getpixel((x,y))
            if r<=127.5 and g<=127.5 and b<=127.5:
                img.putpixel((x,y),(255,255,255))
            else:
                img.putpixel((x,y),(0,0,0))

                
def split_numbers(img):
    is_first=0
    order=0
    start=False
    for x in range(width):
        if x>1:
            if len(set(bucket))!=1:
                start=True
                is_first+=1
                if is_first==1:
                    point=x
            else:
                if start:
                    order+=1
                    start=False
                    cropped=img.crop((point,0,x,y))
                    cropped.save("number{}.png".format(order))
                    is_first=0
            bucket.clear()
        for y in range(height):
            bucket.append(img.getpixel((x,y)))
            

def compare(splited_number):#splited_number is wich we extract from the original picture
    compare_list=[]
    w,h=splited_number.size
    one_pixel_percent=100/(w*h)
    for number in range(10):
        source_number=Image.open(current_dir()+"\\numbers\\{}.png".format(number))
        source_number=source_number.resize((w,h))
        similarity=0
        for x in range(w):
            for y in range(h):
                if source_number.getpixel((x,y))==splited_number.getpixel((x,y)):
                    similarity+=one_pixel_percent
        compare_list.append(similarity)
    best_match.append(str(compare_list.index(max(compare_list))))
def num_creator():
    number=int("".join(best_match))
    print("captcha is: {}".format(number))
    
apply_blackwhite_filter(image1)
split_numbers(image1)
for i in range(1,4):
    splited_number=Image.open(current_dir()+"\\number{}.png".format(i))
    compare(splited_number)
num_creator()
