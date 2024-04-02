import pendulum
import statistics
import random
from pypdf import PdfReader 
from icecream import ic 
import cowsay
import sys
#pendulum example 
"""
now=pendulum.now("Africa/Mogadishu")
#now.in_timezone("America/Toronto")
now.in_timezone("Asia/Dhaka")
print(now)
#pdf example
def parse(filename):
    reader=PdfReader(filename)
    print(f"number of pages {reader.pages[0].extract_text()} ")
#parse(r"C:\Users\hp\Downloads\Tax-interview.pdf")
#icecream example 
a=10
b=11
c=42
for i in range(80,83):
    a=a*i
    b=b*i
    c=c*i
    ans=(ic(a)+ic(b)+ic(c)/3)
    ic(ans)
    
cowsay.turkey("hello") 


list=["Ahmed","Adan","Geedi"]
random.shuffle(list)
for i in list:
 print(i)

numbers=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
print(statistics.median_low(numbers)) """

items=["banana","mango","papaya","simsim"]
random.choice(items)
print(items)