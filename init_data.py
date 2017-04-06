# -*- coding:utf-8 -*-
#encoding:utf-8
import os
import codecs

def deleteDuplicate(input_folder,filename,output_folder):
    print('cleaning ' + input_folder + filename)
    rows,count = [],0#temp data rows
    g=file( output_folder + filename,"w+")
    with open(input_folder + filename, 'r') as f:
        line = f.readline()
        while line:
            line = line.replace('\n','').replace('\r','')
            if line not in rows:
                rows.append(line)
                g.writelines(line)
                g.writelines('\n')
                if len(rows) >= 200:rows = []
            else:count += 1
            line = f.readline()
    print(filename+' had cleaned '+ str(count) + ' duplicate data.')
    g.close()

def pipeFiles(data_folder,cb,output_folder):
    for i in os.listdir(data_folder):
        if i.endswith('.csv'):
            cb(data_folder,i,output_folder)


if __name__=='__main__':
    if not os.path.exists('./data/'):
        os.mkdir("./data/")
    pipeFiles("./original_data/",deleteDuplicate,"./data/")
    os.system("iconv -f GB2312 -t UTF-8 ./data/JData_User.csv > ./data/JData_User2.csv;rm ./data/JData_User.csv;mv ./data/JData_User2.csv ./data/JData_User.csv")
