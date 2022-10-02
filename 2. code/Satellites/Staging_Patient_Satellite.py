from os import get_exec_path, name, path
from numpy import False_
import numpy
from numpy.lib.arraysetops import unique
from numpy.lib.shape_base import column_stack
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import glob
from datetime import datetime, time
import numpy as np

# please fill the following with your own username, password, port number and databse name
# everything after :// is followed as username:password@localhost:port/database_name
# the database name is SMD_SP_G14
engine = create_engine('postgresql+psycopg2://postgres:smd2021@localhost:5432/SMD_SP_G14') 

connection = psycopg2.connect("host=localhost dbname=SMD_SP_G14 user=postgres password=smd2021 port=5432")
connection.autocommit= True
cur = connection.cursor()



# Please paste the path to your data folder VMData here
PATH ='/Users/doris/Dropbox/-UoB/Courses/SMD/Semester Project/Provided Datasets/Dataset 1/VMData/'


EXTENSION = '.csv' 
GLOB_PATH =glob.glob(PATH + '/*csv') 


def csv_isolator(GLOB_PATH,filter):
    """Returns list of all template types"""
    csv_list =[] 
    for i in range(len(GLOB_PATH)): 
        if (filter in GLOB_PATH[i]):
            csv_list.append(GLOB_PATH[i])
    return csv_list

def meta_converter(csv_list):
    """Returns a list of df"""
    meta_list=[]
    index = range(len(csv_list))
    for i in index:
        df = pd.read_csv(csv_list[i],header=None,sep='\n',nrows=31)
        df = df[0].str.split(',', expand=True)
        meta_list.append(df.T)
    return meta_list


def add_ts(df_list):
    """Adds a timestamp and name column for each df, returns list of df"""
    for df in df_list:
        df['time_stamp']=datetime.now()
    return df_list

def add_patientid(df_list):
    """Adds patient ID column and fills it for each patient's file, returns a list of df"""
    index = range(len(df_list))
    for i in index[0:16:1]:
        df_list[i]['patient_id']=1
    for i in index[16:32:1]:
        df_list[i]['patient_id']=2
    for i in index[32:48:1]:
        df_list[i]['patient_id']=3
    for i in index[48:64:1]:
        df_list[i]['patient_id']=4
    for i in index[64:80:1]:
        df_list[i]['patient_id']=5
    for i in index[80:96:1]:
        df_list[i]['patient_id']=6
    for i in index[96:112:1]:
        df_list[i]['patient_id']=7
    for i in index[112:128:1]:
        df_list[i]['patient_id']=8
    for i in index[128:144:1]:
        df_list[i]['patient_id']=9
    for i in index[144:160:1]:
        df_list[i]['patient_id']=10
    return df_list

def get_values(array,filter):
    """Gets a list of unqiue column values and type without None values"""
    column_values = np.array(array[filter].values)

    return np.array(column_values)


csv_list = csv_isolator(GLOB_PATH,'csv')
metadf_list =meta_converter(csv_list)
metadf_listv1 = add_ts(metadf_list)
metadf_listv2 = add_patientid(metadf_listv1)
metadf_ready = pd.concat(metadf_listv2)


metadf_ready = metadf_ready.rename(columns={0:'Header', 1:'File Version', 2:'Patient Information', 3:'ID', 4:'Name', 5:'Comment', 6:'Age',
                    7:'Sex', 8:'Analyze Information', 9:'AnalyzeMode', 10:'Pre Time[s]', 11:'Post Time[s]', 12:'Recovery Time[s]',
                    13:'Base Time[s]', 14:'Fitting Degree', 15:'HPF[Hz]', 16:'LPF[Hz]', 17:'Moving Average[s]', 18:'Measure Information',
                    19:'Date', 20:'Mode', 21:'Wave[nm]', 22:'Wave Length', 23:'Analog Gain', 24:'Digital Gain', 25:'Sampling Period[s]',
                    26:'StimType', 27:'Stim Time[s]', 28:'A', 29:'Repeat Count', 30:'Exception Ch'})
metadf_ready = metadf_ready.drop([0])


names= get_values(metadf_ready,'Name')
age =get_values(metadf_ready,'Age')
sex=get_values(metadf_ready,'Sex')
id=get_values(metadf_ready,'ID')


pa0 =np.vstack((id,names))
pa1 = np.vstack((sex,age))
patient_array1 = np.vstack((pa0,pa1)).T


patient_df = pd.DataFrame(patient_array1)
patient_df.dropna(inplace=True)
patient_df.drop_duplicates(inplace=True)
patient_df.reset_index(inplace=True)


patient_dfv1=patient_df.iloc[[0,4,8,12,16,20,24,28,32,36]]

patient_dfv1.reset_index(inplace=True)


del patient_dfv1['index']
del patient_dfv1['level_0']

i = 0
while i < 43:
    patient_dfv1.loc[patient_dfv1.shape[0]] = [None, None, None, None]
    i = i+1

patient_dfv1['TimeStamp'] = datetime.now()

ind = []
for i in range(53):
    ind.append(i)
patient_dfv1['Patient_Hub_Key'] = ind


patient_dfv1 = patient_dfv1.rename(columns={0:'Patient_ID', 1:'Name', 2:'SEX', 3:'Age'})


patient_dfv1.to_sql('Patient_Satellite',con=engine)

