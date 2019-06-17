# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:51:11 2019

@author: Student
"""
import os
import json

FolderPath = ('C:/Users/PeiYu/Desktop/www/')
filenames = os.listdir(FolderPath)

paths=[]
for i in filenames:
    paths.append(FolderPath+i)

counter=0
na_counter=0
for i in paths:    
    print('>>')
    with open (i,"r",encoding='utf8') as jsonfile:
        data = json.load(jsonfile)
        print('有',len(data.keys()),'篇')

        counter += len(data.keys())        
        print(f'acc_article > {counter}')
        #if there still are news with no text
        # for i in data.keys():
        #     if data[i]['text']=='':
        #         na_counter += 1
        # print(f'acc_no_text > {na_counter}')
        #
print(f'totally have {counter} articles')

        
        