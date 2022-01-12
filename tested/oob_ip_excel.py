import os
import pandas as pd
from oobip import oob_ip_post


def RegisterOOB(fileName, username, password):
    # Registerfile = "Netops\\aci\\data\\"+fileName
    file = "data\\"+fileName
    print(os.getcwd())
    print(file)
    dataframe = pd.read_excel(file, sheet_name='OOB_IP')
    # APIC	NodeID	PodID	OOB_IP	MASK	Gateway

    TAB_APIC_ADDRESS = list(dataframe['APIC'])
    TAB_NodeID = list(dataframe['NodeID'])
    TAB_PodID = list(dataframe['PodID'])
    TAB_OOB_IP = list(dataframe['OOB_IP'])
    TAB_MASK = list(dataframe['MASK'])
    TAB_Gateway = list(dataframe['Gateway'])

    for i in range(0, len(TAB_APIC_ADDRESS)):
        oob_ip_post(
        str(TAB_APIC_ADDRESS[i]),
        username,
        password,
        str(TAB_NodeID[i]),
        str(TAB_PodID[i]),
        str(TAB_OOB_IP[i]),
        str(TAB_MASK[i]),
        str(TAB_Gateway[i])
        )
    

if __name__ == '__main__':
    print(os.getcwd())
    username = 'admin'
    # password = 'ciscopsdt'
    password = 'C1sco12345'
    myfile = 'data.xlsx'
    RegisterOOB(myfile,username, password)
    

print("---------------------------Completed---------------------------")

