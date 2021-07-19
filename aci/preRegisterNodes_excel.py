import pandas as pd
import os
import time
from preregisterNode import preRegisterNode

def registerNodes_excel(filename, username, password):
    
    file = "Netops\\aci\\data\\"+filename
    dataframe = pd.read_excel(file, sheet_name='RegisterNodes')
    # APIC	Serial	NodeName	NodeId	PodId
    tab_url = list(dataframe['APIC'])
    tab_serial = list(dataframe['Serial'])
    tab_NodeName = list(dataframe['NodeName'])
    tab_NodeId = list(dataframe['NodeId'])
    tab_PodId = list(dataframe['PodId'])

    for i in range(0, len(tab_url)):
        preRegisterNode(
            str(tab_url[i]),
            username,
            password,
            str(tab_serial[i]),
            str(tab_NodeName[i]),
            str(tab_NodeId[i]),
            str(tab_PodId[i])
        )
        time.sleep(2)

if __name__ == '__main__':
    username = 'admin'
    password = 'ciscopsdt'
    myfile = "data.xlsx"
    registerNodes_excel(myfile, username, password)
    print("==============Completed==============")