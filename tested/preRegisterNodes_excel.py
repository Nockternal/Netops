import os
import pandas as pd
from preregisterNode import preRegisterNode


def RegisterNodes_Excel(fileName, username, password):
    file = "Netops\\aci\\data\\"+fileName
    print(os.getcwd())
    print(file)
    dataframe = pd.read_excel(file, sheet_name='RegisterNodes')
    TAB_APIC_ADDRESS = list(dataframe['APIC'])
    TAB_POD_ID = list(dataframe['Serial'])
    TAB_SERIAL = list(dataframe['NodeName'])
    TAB_NODE_ID = list(dataframe['NodeId'])
    TAB_SWITCH_NAME = list(dataframe['PodId'])

    for i in range(0, len(TAB_APIC_ADDRESS)):
        preRegisterNode(
        str(TAB_APIC_ADDRESS[i]),
        username,
        password,
        str(TAB_SERIAL[i]),
        str(TAB_SWITCH_NAME[i]),
        str(TAB_NODE_ID[i]),
        str(TAB_POD_ID[i])
        )
    

if __name__ == '__main__':
    username = 'admin'
    password = 'ciscopsdt'
    myfile = 'data.xlsx'
    RegisterNodes_Excel(myfile,username, password)
    

print("---------------------------Completed---------------------------")

