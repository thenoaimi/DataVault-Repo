import os
from os import get_exec_path, path
from numpy import False_
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import glob
from datetime import datetime
import numpy as np

engine = create_engine('postgresql+psycopg2://postgres:smd2021@localhost:5432/SMD_SP_G14') 
# please fill the following with your own username, password, port number and databse name
# everything after :// is followed as username:password@localhost:port/database_name
# the database name is SMD_SP_G14

"""Connect to postgreSQL"""
connection = psycopg2.connect("host=localhost dbname=SMD_SP_G14 user=postgres password=smd2021 port=5432")
cur = connection.cursor()
#remember to edit argument in psycopg2.connect() to YOUR database
connection.autocommit= True
cur = connection.cursor()
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
        print()
        df2 = pd.DataFrame(d)
        df_list.append(df2)
    return df_list
def add_nts(df_list,type):
    """Adds a timestamp and name column for each df"""
    for df in df_list:
        df['time_stamp']=datetime.now()
        df['name']=type
    return df_lists
list1=[]
list3=['Exp1 Deoxy','Exp1 Oxy','Exp2 Session 1 Dat', 'Exp2 Session 2 Dat','Exp2 Session 1 WL1/2','Exp2 Session 2 WL1/2']
for i in range(617681):
    list = []
    list.append(i+1)
    list.append('HO1')
    list.append(datetime.now())
    list.append('Source 1')
    if(i<109690):
        list.append(list3[0])
    else:
        if(i-109690<109690):
            list.append(list3[1])
        else:
            if(i-109690-109690<78398):
                list.append(list3[2])

            else:
                if (i - 109690 - 109690 - 78398<63749):
                    list.append(list3[3])
                else:
                    if (i - 109690 - 109690 - 78398-63749<131392):
                        list.append(list3[4])
                    else:
                        list.append(list3[5])
    list1.append(list)

col=['fnirs_hub_key','fnirs_businesskey','loaddatetime','recordsource','name']
df2 = pd.DataFrame(list1,columns=col)
df2.to_sql('fnirs_hub',con=engine,if_exists='append') #this writes the dataframe into the postgres database