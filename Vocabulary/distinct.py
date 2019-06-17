# coding:utf8
import numpy as np
#

file_dir='C:/Users/PeiYu/Desktop/newss/'
f_name_in='stopword525_.txt'
f_name_out='stopword525.txt'

with open(file_dir + f_name_in, 'r', encoding='utf8') as input_f:
    data = input_f.readlines()
    words = np.array(data)
    set_words = set(words)
    result_txt= ''.join(set_words)
    print(result_txt)
    with open(file_dir+f_name_out, 'w', encoding='utf_8_sig', newline='') as output_f:
        output_f.write(result_txt)


# with open(file_dir+f_name_in, 'r', encoding='utf8') as input_f:
#     data = input_f.readlines()
    # words=[]
    # for i in data:
    #     # print(i.strip())
    #     # print(len(i.strip()))
    #     if len(i.strip())==1:
    #         continue
    #     words.append(i.replace('\n',''))
    #     set_words = set(words)
    #     result_txt='\n'.join(words)
    #     # print(st)
    #     print(">")
    #
    # with open(file_dir+f_name_out, 'w', encoding='utf_8_sig', newline='') as output_f:
    #     output_f.write(result_txt)
