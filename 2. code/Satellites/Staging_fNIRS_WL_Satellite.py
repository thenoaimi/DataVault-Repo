import os
from os import get_exec_path, path
from numpy import False_
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import glob
from datetime import datetime
import numpy as np



# please fill the following with your own username, password, port number and databse name
# everything after :// is followed as username:password@localhost:port/database_name
# the database name is SMD_SP_G14
engine = create_engine('postgresql+psycopg2://postgres:smd2021@localhost:5432/SMD_SP_G14') 

connection = psycopg2.connect("host=localhost dbname=SMD_SP_G14 user=postgres password=smd2021 port=5432")
connection.autocommit= True
cur = connection.cursor()



# Please update the path to your data folder for fNIRS data here
basepath1='/Users/doris/Dropbox/-UoB/Courses/SMD/Semester Project/Provided Datasets/Dataset 2/fNIRS-Data/1raSessionDR'
basepath2='/Users/doris/Dropbox/-UoB/Courses/SMD/Semester Project/Provided Datasets/Dataset 2/fNIRS-Data/2daSessionDR'


def file_isolator(GLOB_PATH,filter):
    """Returns list of all templates types"""
    csv_list =[] #empty list
    for i in range(len(GLOB_PATH)): #checks folder for everything that is a csv file with the correct names
        if (filter in GLOB_PATH[i]):
            csv_list.append(GLOB_PATH[i])
    return csv_list

def file_reader(PATH,EXTENSION):
    g = os.walk(PATH)
    file_dic=[]
    for path, dir_list, file_list in g:
        for file_name in file_list:
            file_dic.append((os.path.join(path, file_name)))
    d=str(EXTENSION)
    file_dic=file_isolator(file_dic,d)
    return file_dic

def file_converter(csv_list):
    """Extracts filtered csv file, return as list of dataframe object"""
    df_list =[]
    for file in csv_list:
        content=open(file,'r')
        c=content.readlines()
        d=[]
        for jax in range(len(c)):
            dax=c[jax].split()
            d.append(dax)
        fa=[]
        for i in range(1,len(c[0])+1):
            fa.append(i)
        ma=np.array(fa)
        df2 = pd.DataFrame(d)
        df_list.append(df2)
    return df_list

def add_nts(df_list):
    """Adds a timestamp and name column for each df"""
    for df in df_list:
        df['time_stamp']=datetime.now()
    return df_list

def add_id(df_list,id,type):
    for df in df_list:
        df['patient_id']=id
        df['type']=type
    return df_list

def add_firstly1(filepath):
    asd = os.listdir(filepath)
    asd.pop()
    finalresult=[]
    for i in range(len(asd)):
        filename=os.path.join(filepath,asd[i])
        d=file_reader(filename,'.wl1')
        d1=file_converter(d)
        d1=add_nts(d1)
        d1=add_id(d1,i+1,'wl1')
        for j in d1:
            finalresult.append(j)
        filename = os.path.join(filepath, asd[i])
        d = file_reader(filename, '.wl2')
        d1 = file_converter(d)
        d1=add_nts(d1)
        d1=add_id(d1, i+1, 'wl2')
        for m in d1:
            finalresult.append(m)
    df_ready = pd.concat(finalresult)
    return df_ready

def add_firstly2(filepath):
    asd = os.listdir(filepath)
    asd.pop()
    finalresult=[]
    for i in range(len(asd)):
        filename=os.path.join(filepath,asd[i])
        d=file_reader(filename,'.wl1')
        d1=file_converter(d)
        d1 = add_nts(d1, 4)
        d1=add_id(d1,i+1,'wl1')
        for m in d1:
            finalresult.append(m)
        filename = os.path.join(filepath, asd[i])
        d = file_reader(filename, '.wl2')
        d1 = file_converter(d)
        d1 = add_nts(d1, 4)
        d1=add_id(d1, i+1, 'wl2')
        for m in d1:
            finalresult.append(m)
    df_ready = pd.concat(finalresult)
    return df_ready


df_ready1 = add_firstly1(basepath1)
df_ready2 = add_firstly1(basepath2)


hub_key1 = []
for i in range(361527, 492919):
    key = i+1
    hub_key1.append(key)

hub_key2 = []
for i in range(492919, 617681):
    key = i+1
    hub_key2.append(key)


df_ready1['fNIRS_Hub_Key'] = hub_key1
df_ready2['fNIRS_Hub_Key'] = hub_key2


df_ready1.to_sql('fNIRS_Exp2Sess1WL_Satellite', con=engine, if_exists='append')
df_ready2.to_sql('fNIRS_Exp2Sess2WL_Satellite', con=engine, if_exists='append')

