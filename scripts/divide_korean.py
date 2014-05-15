# -*- coding:utf-8 -*- 
import os , sys
import unicodedata
import hangul
 
str = "°¡"
line = ""
  
for ss in unicode(str,'cp949') :
    cc = hangul.split(ss)

    for i in cc:
        line += i.encode('cp949')

print line