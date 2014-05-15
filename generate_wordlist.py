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
                u'\u3131':u'g', # ㄱ
                u'\u3132':u'gg', # ㄲ
                u'\u3133':u'gs', # ㄳ
                u'\u3134':u'n', # ㄴ
                u'\u3135':u'nj', # ㄵ
                u'\u3136':u'nh', # ㄶ
                u'\u3137':u'd', # ㄷ
                u'\u3138':u'dd', # ㄸ
                u'\u3139':u'r', # ㄹ
                u'\u313a':u'lg', # ㄺ
                u'\u313b':u'lm', # ㄻ
                u'\u313c':u'lb', # ㄼ
                u'\u313d':u'ls', # ㄽ
                u'\u313e':u'lt', # ㄾ
                u'\u313f':u'lp', # ㄿ
                u'\u3140':u'lh', # ㅀ
                u'\u3141':u'm',  # ㅁ
                u'\u3142':u'b', # ㅂ
                u'\u3143':u'bb',  # ㅃ
                u'\u3144':u'bs', # ㅄ
                u'\u3145':u's',  # ㅅ
                u'\u3146':u'ss', # ㅆ
                u'\u3147':u'ng', # ㅇ
                u'\u3148':u'j', # ㅈ
                u'\u3149':u'jj', # ㅉ
                u'\u314a':u'ch', # ㅊ
                u'\u314b':u'k', # ㅋ
                u'\u314c':u't',  # ㅌ
                u'\u314d':u'p',  # ㅍ
                u'\u314e':u'h', # ㅎ

                # moum 
                u'\u314f':u'a', # ㅏ
                u'\u3150':u'ae',  # ㅐ
                u'\u3151':u'ya',  # ㅑ
                u'\u3152':u'yae',  # ㅒ
                u'\u3153':u'eo',  # ㅓ
                u'\u3154':u'e', # ㅔ
                u'\u3155':u'yeo',  # ㅕ
                u'\u3156':u'ye',  # ㅖ
                u'\u3157':u'o',  # ㅗ
                u'\u3158':u'wa',  # ㅘ
                u'\u3159':u'wae',  # ㅙ
                u'\u315a':u'oe', # ㅚ
                u'\u315b':u'yo',  # ㅛ
                u'\u315c':u'u',  # ㅜ
                u'\u315d':u'weo', # ㅝ
                u'\u315e':u'we',  # ㅞ
                u'\u315f':u'wi',  # ㅟ
                u'\u3160':u'yu', # ㅠ
                u'\u3161':u'eu',  # ㅡ
                u'\u3162':u'yi',  # ㅢ
                u'\u3163':u'i', # ㅣ
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

                        # 초성에 이응이 올때는 무음 처리
                        if c == 1 and phone[g] == 'ng':
                                continue
                        else: 
                                if phone.has_key(g):
                                        ph = phone[g]
                                        re.append(ph)
        return re
        

def convertToEng(s):
        phone = {  # jaum
                u'\u3131':u'r', # ㄱ
                u'\u3132':u'R', # ㄲ
                u'\u3133':u'rt', # ㄳ
                u'\u3134':u's', # ㄴ
                u'\u3135':u'sw', # ㄵ
                u'\u3136':u'sg', # ㄶ
                u'\u3137':u'e', # ㄷ
                u'\u3138':u'E', # ㄸ
                u'\u3139':u'f', # ㄹ
                u'\u313a':u'fr', # ㄺ
                u'\u313b':u'fv', # ㄻ
                u'\u313c':u'fq', # ㄼ
                u'\u313d':u'ft', # ㄽ
                u'\u313e':u'fx', # ㄾ
                u'\u313f':u'fv', # ㄿ
                u'\u3140':u'fg', # ㅀ
                u'\u3141':u'a',  # ㅁ
                u'\u3142':u'q', # ㅂ
                u'\u3143':u'Q',  # ㅃ
                u'\u3144':u'qt', # ㅄ
                u'\u3145':u't',  # ㅅ
                u'\u3146':u'T', # ㅆ
                u'\u3147':u'd', # ㅇ
                u'\u3148':u'w', # ㅈ
                u'\u3149':u'W', # ㅉ
                u'\u314a':u'c', # ㅊ
                u'\u314b':u'z', # ㅋ
                u'\u314c':u'x',  # ㅌ
                u'\u314d':u'v',  # ㅍ
                u'\u314e':u'g', # ㅎ

                # moum 
                u'\u314f':u'k', # ㅏ
                u'\u3150':u'o',  # ㅐ
                u'\u3151':u'i',  # ㅑ
                u'\u3152':u'O',  # ㅒ
                u'\u3153':u'j',  # ㅓ
                u'\u3154':u'p', # ㅔ
                u'\u3155':u'u',  # ㅕ
                u'\u3156':u'P',  # ㅖ
                u'\u3157':u'h',  # ㅗ
                u'\u3158':u'hk',  # ㅘ
                u'\u3159':u'ho',  # ㅙ
                u'\u315a':u'hl', # ㅚ
                u'\u315b':u'y',  # ㅛ
                u'\u315c':u'n',  # ㅜ
                u'\u315d':u'nj', # ㅝ
                u'\u315e':u'np',  # ㅞ
                u'\u315f':u'nl',  # ㅟ
                u'\u3160':u'b', # ㅠ
                u'\u3161':u'm',  # ㅡ
                u'\u3162':u'ml',  # ㅢ
                u'\u3163':u'l', # ㅣ
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

                        # 초성에 이응이 올때는 무음 처리
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