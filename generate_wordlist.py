#!/usr/bin/python
# -*- coding: euc-kr -*-
#
#       Generates wordlists based on the files in "wordlist_by_category" directory
#       by Externalist

import hangul
import string, codecs
from numpy import *
from os import listdir
from os.path import isfile, join

def getPhone(s):
        phone = {  # jaum
                u'\u3131':u'g', # ��
                u'\u3132':u'gg', # ��
                u'\u3133':u'gs', # ��
                u'\u3134':u'n', # ��
                u'\u3135':u'nj', # ��
                u'\u3136':u'nh', # ��
                u'\u3137':u'd', # ��
                u'\u3138':u'dd', # ��
                u'\u3139':u'r', # ��
                u'\u313a':u'lg', # ��
                u'\u313b':u'lm', # ��
                u'\u313c':u'lb', # ��
                u'\u313d':u'ls', # ��
                u'\u313e':u'lt', # ��
                u'\u313f':u'lp', # ��
                u'\u3140':u'lh', # ��
                u'\u3141':u'm',  # ��
                u'\u3142':u'b', # ��
                u'\u3143':u'bb',  # ��
                u'\u3144':u'bs', # ��
                u'\u3145':u's',  # ��
                u'\u3146':u'ss', # ��
                u'\u3147':u'ng', # ��
                u'\u3148':u'j', # ��
                u'\u3149':u'jj', # ��
                u'\u314a':u'ch', # ��
                u'\u314b':u'k', # ��
                u'\u314c':u't',  # ��
                u'\u314d':u'p',  # ��
                u'\u314e':u'h', # ��

                # moum 
                u'\u314f':u'a', # ��
                u'\u3150':u'ae',  # ��
                u'\u3151':u'ya',  # ��
                u'\u3152':u'yae',  # ��
                u'\u3153':u'eo',  # ��
                u'\u3154':u'e', # ��
                u'\u3155':u'yeo',  # ��
                u'\u3156':u'ye',  # ��
                u'\u3157':u'o',  # ��
                u'\u3158':u'wa',  # ��
                u'\u3159':u'wae',  # ��
                u'\u315a':u'oe', # ��
                u'\u315b':u'yo',  # ��
                u'\u315c':u'u',  # ��
                u'\u315d':u'weo', # ��
                u'\u315e':u'we',  # ��
                u'\u315f':u'wi',  # ��
                u'\u3160':u'yu', # ��
                u'\u3161':u'eu',  # ��
                u'\u3162':u'yi',  # ��
                u'\u3163':u'i', # ��
        }


        re = [];
        for i in s:
                if not hangul.ishangul(i):
                        re.append(i)
                        continue
                t = hangul.split(i)
                c = 0
                for g in t:
                        c = c + 1
                        if g == u'':
                                continue

                        # �ʼ��� ������ �ö��� ���� ó��
                        if c == 1 and phone[g] == 'ng':
                                continue
                        else: 
                                if phone.has_key(g):
                                        ph = phone[g]
                                        re.append(ph)
        return re
        

def convertToEng(s):
        phone = {  # jaum
                u'\u3131':u'r', # ��
                u'\u3132':u'R', # ��
                u'\u3133':u'rt', # ��
                u'\u3134':u's', # ��
                u'\u3135':u'sw', # ��
                u'\u3136':u'sg', # ��
                u'\u3137':u'e', # ��
                u'\u3138':u'E', # ��
                u'\u3139':u'f', # ��
                u'\u313a':u'fr', # ��
                u'\u313b':u'fv', # ��
                u'\u313c':u'fq', # ��
                u'\u313d':u'ft', # ��
                u'\u313e':u'fx', # ��
                u'\u313f':u'fv', # ��
                u'\u3140':u'fg', # ��
                u'\u3141':u'a',  # ��
                u'\u3142':u'q', # ��
                u'\u3143':u'Q',  # ��
                u'\u3144':u'qt', # ��
                u'\u3145':u't',  # ��
                u'\u3146':u'T', # ��
                u'\u3147':u'd', # ��
                u'\u3148':u'w', # ��
                u'\u3149':u'W', # ��
                u'\u314a':u'c', # ��
                u'\u314b':u'z', # ��
                u'\u314c':u'x',  # ��
                u'\u314d':u'v',  # ��
                u'\u314e':u'g', # ��

                # moum 
                u'\u314f':u'k', # ��
                u'\u3150':u'o',  # ��
                u'\u3151':u'i',  # ��
                u'\u3152':u'O',  # ��
                u'\u3153':u'j',  # ��
                u'\u3154':u'p', # ��
                u'\u3155':u'u',  # ��
                u'\u3156':u'P',  # ��
                u'\u3157':u'h',  # ��
                u'\u3158':u'hk',  # ��
                u'\u3159':u'ho',  # ��
                u'\u315a':u'hl', # ��
                u'\u315b':u'y',  # ��
                u'\u315c':u'n',  # ��
                u'\u315d':u'nj', # ��
                u'\u315e':u'np',  # ��
                u'\u315f':u'nl',  # ��
                u'\u3160':u'b', # ��
                u'\u3161':u'm',  # ��
                u'\u3162':u'ml',  # ��
                u'\u3163':u'l', # ��
        }


        re = [];
        for i in s:
                if not hangul.ishangul(i):
                        re.append(i)
                        continue
                t = hangul.split(i)
                c = 0
                for g in t:
                        c = c + 1
                        if g == u'':
                                continue

                        # �ʼ��� ������ �ö��� ���� ó��
                        if c == 1 and phone[g] == 'ng':
                                continue
                        else: 
                                if phone.has_key(g):
                                        ph = phone[g]
                                        re.append(ph)
        return re


if __name__ == '__main__':
    
    mypath = "wordlist_by_category/"
    onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
    
    result_path = "wordlist_korean.txt"
    result = ''
    
    for filename in onlyfiles:
        with codecs.open(mypath + filename, 'r', encoding='cp949') as f:
            source = f.readlines()
            
        for word in source:
            dt = []
            dt = getPhone(word)
            dc = convertToEng(word)
            if len(''.join(dt).replace(' ','').strip()) <= 10:
                result += ''.join(dt).replace(' ','').strip() + '\n'
            result += ''.join(dc).replace(' ','').strip() + '\n'
    
    fw = codecs.open(result_path, 'w+', encoding='cp949')
    fw.write(result)
    fw.close()