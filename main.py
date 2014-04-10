from pytesser import *
from spellchecker import *
import re

def words(text): return re.findall('[a-z]+', text.lower()) 

im = Image.open('C:\\Users\\deepakSattiraju\\Desktop\\Pytesser\\1.png')
im = im.convert('1')
text = image_to_string(im)

l = words(text)
output = ""
for word in l:
    output += correct(word) + " "


print output
