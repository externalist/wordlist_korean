#!/usr/bin/python
# -*- coding: cp949 -*-
#
#       Generates a list of all combinations of 3 lettered Korean names.
#       by Externalist


import hangul
import string, codecs, unicodedata
from numpy import *
from os import listdir
from os.path import isfile, join
import pprint

def create_names():
        surname_list = [u'김',u'이',u'박',u'최',u'정',u'강',u'조',u'윤',u'장',u'임',u'한',u'신',u'오',u'서',u'권',u'황',u'송',u'안',u'유',u'홍',u'전',u'고',u'문',u'손',u'양',u'배',u'백',u'조',u'허',u'남']
        
        '''
        surname_list = [
                u'가', u'간', u'갈', u'감', u'강', u'개', u'견', u'경', u'계', u'고', u'곡', u'공', u'곽', u'교', u'구', u'국', u'군', u'궁', u'궉', u'권', u'근', u'금', u'기', u'길', u'김',
                u'나', u'난', u'남', u'낭', u'내', u'노', u'뇌', u'누',
                u'단', u'담', u'당', u'대', u'도', u'돈', u'동', u'두',
                u'라', u'량', u'려', u'련', u'렴', u'로', u'룡', u'루', u'류', u'륙', u'리' ,u'림',
                u'마', u'만', u'매', u'맹', u'명', u'모', u'목', u'묘', u'묵', u'문', u'미', u'민',
                u'박', u'반', u'방', u'배', u'백', u'범', u'변', u'복', u'봉', u'부', u'비', u'빈', u'빙',
                u'사', u'삼', u'상', u'서', u'석', u'선', u'설', u'섭', u'성', u'소', u'손', u'송', u'수', u'순', u'승', u'시', u'신', u'심', u'십',
                u'아', u'안', u'애', u'야', u'양', u'어', u'엄', u'여', u'연', u'염', u'엽', u'영', u'예', u'오', u'옥', u'온', u'옹', u'왕', u'요', u'용', u'우', u'운', u'원', u'위', u'유', u'육', u'윤', u'은', u'음', u'이', u'인', u'임',
                u'자', u'장', u'저', u'전', u'점', u'정', u'제', u'조', u'종', u'좌', u'주', u'준', u'즙', u'증', u'지', u'진',
                u'차', u'창', u'채', u'척', u'천', u'초', u'최', u'추', u'춘',
                u'쾌', u'탁', u'탄', u'태', u'판', u'팽', u'편', u'평', u'포', u'표', u'풍', u'피', u'필',
                u'하', u'학', u'한', u'함', u'해', u'허', u'현', u'형', u'호', u'홍', u'화', u'환', u'황', u'후', u'흥',
                u'강전', u'남궁', u'독고', u'동방', u'망절', u'사공', u'서문', u'선우', u'소봉', u'어금', u'장곡', u'제갈', u'황보'
                ]
        '''
                
        jaum = [
                u'\u3131', # ㄱ
                u'\u3134', # ㄴ
                u'\u3137', # ㄷ
                u'\u3139', # ㄹ
                u'\u3141',  # ㅁ
                u'\u3142', # ㅂ
                u'\u3145',  # ㅅ
                u'\u3147', # ㅇ
                u'\u3148', # ㅈ
                u'\u314a', # ㅊ
                u'\u314b', # ㅋ
                u'\u314c',  # ㅌ
                u'\u314d',  # ㅍ
                u'\u314e' # ㅎ
        ]
        
        jaum_last = [
                u'\u3131', # ㄱ
                u'\u3134', # ㄴ
                u'\u3139', # ㄹ
                u'\u3141',  # ㅁ
                u'\u3142', # ㅂ
                u'\u3147', # ㅇ
        ]

        moum = [
                u'\u314f', # ㅏ
                u'\u3150',  # ㅐ
                u'\u3151',  # ㅑ
                u'\u3152',  # ㅒ
                u'\u3153',  # ㅓ
                u'\u3154', # ㅔ
                u'\u3155',  # ㅕ
                u'\u3156',  # ㅖ
                u'\u3157',  # ㅗ
                u'\u3158',  # ㅘ
                u'\u3159',  # ㅙ
                u'\u315a', # ㅚ
                u'\u315b',  # ㅛ
                u'\u315c',  # ㅜ
                u'\u315d', # ㅝ
                u'\u315e',  # ㅞ
                u'\u315f',  # ㅟ
                u'\u3160', # ㅠ
                u'\u3161',  # ㅡ
                u'\u3162',  # ㅢ
                u'\u3163'   # ㅣ
        ]
        
        fullname_list = []
        givenname_list = []
        all_combinations_list = []
        twoletter_list = []
        threeletter_list = []
        
        for i in xrange(0,len(jaum)):
            for j in xrange(0,len(moum)):
                twoletter_list.append(hangul.join(jaum[i] + moum[j]))
        for i in xrange(0,len(jaum)):
            for j in xrange(0,len(moum)):
                for k in xrange(0,len(jaum_last)):
                    threeletter_list.append(hangul.join(jaum[i] + moum[j] + jaum_last[k]))
        
        for i in xrange(0,10):#len(twoletter_list)):
            for j in xrange(0,len(twoletter_list)):
                givenname_list.append(twoletter_list[i] + twoletter_list[j])
        for i in xrange(0,len(twoletter_list)):
            for j in xrange(0,len(threeletter_list)):
                givenname_list.append(twoletter_list[i] + threeletter_list[j])
        for i in xrange(0,len(threeletter_list)):
            for j in xrange(0,len(twoletter_list)):
                givenname_list.append(threeletter_list[i] + twoletter_list[j])
        for i in xrange(0,len(threeletter_list)):
            for j in xrange(0,len(threeletter_list)):
                givenname_list.append(threeletter_list[i] + threeletter_list[j])
                            
        for i in xrange(0,len(surname_list)):
            for j in xrange(0,len(givenname_list)):
                fullname_list.append(surname_list[i] + givenname_list[j])
                
        all_combinations_list = surname_list + givenname_list + fullname_list
        
        return all_combinations_list
        

if __name__ == '__main__':
    
    result_path = "../wordlist_by_category/optional/autogenerated_names.txt"
    result = ''
    
    result = create_names()
    fw = codecs.open(result_path, 'w+', encoding='cp949')
    fw.write('\n'.join(result))
    fw.close()