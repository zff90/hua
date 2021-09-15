#####################################################################################
## Procedure Name : 
## Purpose        : 
## Arguments      : 
## Returns        : 
## Comments       : 
## Version        : 1.0
## FilePath       : \huawei-platform-script\LRR\get_most_popular.py
## Author         : FANG
## Date           : 2021-07-04 23:14:15
## LastEditors    : FANG
## LastEditTime   : 2021-07-05 00:16:38
#####################################################################################
import os
import re
def CrossOver(dir,fl):
    for i in os.listdir(dir):  #遍历整个文件夹
        path = os.path.join(dir, i)
        if os.path.isfile(path) :  #判断是否为一个文件，排除文件夹
            if path[-4:] == ".tcl":
                fl.append(path)
                print(path)
        elif os.path.isdir(path):
            newdir=path
            CrossOver(newdir,fl)
    return fl
def get_modify_command(file):
    with open(file,'r') as f:
        lines = f.read()
        #res = re.findall('\*[a-z][a-z,A-Z,0-9,_]+',lines)
        res = re.findall('hm_[a-z,A-Z][a-z,A-Z,0-9,_]+',lines)
    return res

 
    
directory="D:\\Program Files\\Altair\\2019\\hm\\scripts"  #文件夹名称
filelist=[]
output=CrossOver(directory,filelist)
print(len(output))
modify_command_list = []
for file in output:
    try:
        res = get_modify_command(file)
        for i in res:
            modify_command_list.append(i)
    except:
        print('open failed')
a={}
for i in modify_command_list:
    a[i] = modify_command_list.count(i)
print(a)
sortedClassCount = sorted(a.items(),key = lambda e:e[1], reverse=True)
new_list = []
for i in sortedClassCount:
    new_list.append(i[0]+', '+str(i[1])+'\n')

with open('d:/res.txt','w') as f:
    f.writelines(new_list)
    
    
    
