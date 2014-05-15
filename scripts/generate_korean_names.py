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
        surname_list = [u'��',u'��',u'��',u'��',u'��',u'��',u'��',u'��',u'��',u'��',u'��',u'��',u'��',u'��',u'��',u'Ȳ',u'��',u'��',u'��',u'ȫ',u'��',u'��',u'��',u'��',u'��',u'��',u'��',u'��',u'��',u'��']
        
        '''
        surname_list = [
                u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��',
                u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��',
                u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��',
                u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��' ,u'��',
                u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��',
                u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��',
                u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��',
                u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��',
                u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��',
                u'��', u'â', u'ä', u'ô', u'õ', u'��', u'��', u'��', u'��',
                u'��', u'Ź', u'ź', u'��', u'��', u'��', u'��', u'��', u'��', u'ǥ', u'ǳ', u'��', u'��',
                u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'��', u'ȣ', u'ȫ', u'ȭ', u'ȯ', u'Ȳ', u'��', u'��',
                u'����', u'����', u'����', u'����', u'����', u'���', u'����', u'����', u'�Һ�', u'���', u'���', u'����', u'Ȳ��'
                ]
        '''
                
        jaum = [
                u'\u3131', # ��
                u'\u3134', # ��
                u'\u3137', # ��
                u'\u3139', # ��
                u'\u3141',  # ��
                u'\u3142', # ��
                u'\u3145',  # ��
                u'\u3147', # ��
                u'\u3148', # ��
                u'\u314a', # ��
                u'\u314b', # ��
                u'\u314c',  # ��
                u'\u314d',  # ��
                u'\u314e' # ��
        ]
        
        jaum_last = [
                u'\u3131', # ��
                u'\u3134', # ��
                u'\u3139', # ��
                u'\u3141',  # ��
                u'\u3142', # ��
                u'\u3147', # ��
        ]

        moum = [
                u'\u314f', # ��
                u'\u3150',  # ��
                u'\u3151',  # ��
                u'\u3152',  # ��
                u'\u3153',  # ��
                u'\u3154', # ��
                u'\u3155',  # ��
                u'\u3156',  # ��
                u'\u3157',  # ��
                u'\u3158',  # ��
                u'\u3159',  # ��
                u'\u315a', # ��
                u'\u315b',  # ��
                u'\u315c',  # ��
                u'\u315d', # ��
                u'\u315e',  # ��
                u'\u315f',  # ��
                u'\u3160', # ��
                u'\u3161',  # ��
                u'\u3162',  # ��
                u'\u3163'   # ��
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