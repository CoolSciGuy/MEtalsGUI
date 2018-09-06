# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 13:22:01 2018

@author: amirreza.sharifi
"""


def read_data():
    import os.path
    import numpy as np
    import pandas as pd
    
    if os.path.isfile("allSorted.csv"):   #if the pivoted file exits, read it
        Data = pd.read_csv("allSorted.csv")
        Data['Date'] = pd.to_datetime(Data['Date'])
        Data.index = Data['Date']
        del Data['Date']

    else:   #make a pivoted file
    
        Data = pd.read_csv('all+chain.csv')
        Data = Data.pivot_table( values = ['Result Value'], columns = 'Characteristic Name', index=['Station' , 'Date']).reset_index()
        Data['Date'] = pd.to_datetime(Data['Date'])
        Data.index = Data['Date']
        del Data['Date']

        Data.columns = ['{}'.format(x[1]) for x in Data.columns]   #fix titles
        Data.columns.values[0] = 'Station' #title of first column is 'Station'



    #assign stations to categories
        Condition1 = Data['Station'].isin(["AAG01",	"AAG02",	"ANA01",	"ANA02",	"ANA03",	"ANA04",	"ANA05",	"ANA06",	"ANA07",	"ANA08",	"ANA09",	"ANA10",	"ANA11",	"ANA12",	"ANA13",	"ANA14",	"ANA15",	"ANA16",	"ANA17",	"ANA18",	"ANA19",	"ANA20",	"ANA21",	"ANA21 ",	"ANA22",	"ANA23",	"ANA24",	"ANA25",	"ANA26",	"ANA27",	"ANA29",	"ANA30"]) # Anacostia
        Condition2 = Data['Station'].isin(["TDU01",	"TFC01",	"TFD01",	"TFE01",	"TFS01",	"THR01",	"TNA01",	"TNS01",	"TOR01",	"TPB01",	"TTX27",	"TUT01",	"TWB01",	"TWB02",	"TWB03",	"TWB04",	"TWB05",	"TWB06" , "TFS01"]) #Anacostia Trib
        Condition3 = Data['Station'].isin(["KNG01",	"KNG02"]) # Kingman Island
        Condition4 = Data['Station'].isin(["PMS01",	"PMS02",	"PMS03",	"PMS05",	"PMS07",	"PMS08",	"PMS09",	"PMS10",	"PMS11",	"PMS12",	"PMS13",	"PMS16",	"PMS18",	"PMS21",	"PMS21 ",	"PMS23",	"PMS25",	"PMS27",	"PMS29",	"PMS31",	"PMS33",	"PMS35",	"PMS37",	"PMS39",	"PMS41",	"PMS44",	"PMS46",	"PMS48",	"PMS51" , "PMS52"]) # Potomac
        Condition5 = Data['Station'].isin(["TBK01",	"TBR01", "TCO01", "TCO06" , "TDA01" , "TDO01" , "TFB01" , "TFB02"]) # Potomac Trib
        Condition6 = Data['Station'].isin(["RCR01",	"RCR04","RCR07",	"RCR09"]) # Rock Creek
        Condition7 = Data['Station'].isin(["TKV01",	"TLU01",	"TMH01",	"TPI01",	"TPO01",	"TPY01",	"TSO01"]) # Rock Creek Trib
        Condition8 = Data['Station'].isin(["PWC04"]) # Ship Channel
        Condition9 = Data['Station'].isin(["PTB01"]) # Tidal Basin
        Condition10 = Data['Station'].isin(["CHAIN"]) # USGS chain Bridge
    
        conditions = [Condition1 , Condition2,Condition3 , Condition4,Condition5 , Condition6, Condition7 , Condition8, Condition9,Condition10]
        choices = ['Anacostia Mainstem', 'Anacostia Tributary' , 'Kingman Lake' , 'Potomac Mainstem' , "Potomac Tributary" , "Rock Creek" , "Rock Creek Tributary" , "Ship Channel" , "Tidal Basin"   , "Chain Bridge (USGS)"   ]
        Data['Watershed'] = np.select(conditions, choices)


        Data['months'] = Data.index.to_period('M')  #making monthly data
        Data['month']=Data.index.month
        Data['year']=Data.index.year
        Data['quarter']=Data.index.quarter
        Data['YearQuart']= Data.index.to_period('q')
        Data.to_csv("allSorted.csv", sep=',')

    return Data









def units(Constituent):
    thresholdmin = 0
    thresholdmax = 0
    if Constituent == 'Turbidity': 
        Unit = ' (NTU)' 
        thresholdmax = 20   #Turbidity increase above ambient (NTU) 
        
        Class = "A,B,C"  #done
    elif Constituent == 'Escherichia coli':
        Unit = ' (MPN/100 ml)'  
        thresholdmax = 410      #done
        Class = "A"
    elif Constituent == 'Nitrite':
        Unit = ' (mg/lit)'
        thresholdmax = 0        
        Class = "NA"   #not in DC standard
    elif Constituent == 'Ammonia':
        Unit = ' (mg/lit)'
        thresholdmax = 0     
        Class = "C,D"    #complicated, revisit later
    elif Constituent == 'Total Phosphorus':
        Unit = ' (mg/lit)'
        thresholdmax = 0     
        Class = "NA"
    elif Constituent == 'Total Soluble Phosphorus':
        Unit = ' (mg/lit)'
        thresholdmax = 0     
        Class = "NA"
    elif Constituent == 'Ortho-Phosphorus':
        Unit = ' (mg/lit)'
        thresholdmax = 0     
        Class = "NA"
    elif Constituent == 'BOD5':
        Unit = ' (mg/lit)'
        thresholdmax = 0     
        Class = "NA"
    elif Constituent == 'Total suspended solids':
        Unit = ' (mg/lit)'
        thresholdmax = 0     
        Class = "NA"
    elif Constituent == 'Chlorophyll a':
        Unit = ' (mg/m3)'
        thresholdmax = 25     
        Class = "C" #done
    elif Constituent == 'Phaeophytin a':
        Unit = ' (mg/lit)'
        thresholdmax = 0     
        Class = "NA"
    elif Constituent == 'Hardness':
        Unit = ' (mg/lit)'
        thresholdmax = 0     
        Class = "NA"
    elif Constituent == 'Alkalinity':
        Unit = ' (mg/lit)' 
        thresholdmax = 0     
        Class = "NA"
    elif Constituent == 'Dissolved Oxygen':
        Unit = ' (mg/lit)'
        thresholdmin = 5     
        Class = "C" # done
    elif Constituent == 'Cadmium':
        Unit = ' (µg/lit)'
        thresholdmax = 0     
        Class = "NA"
    elif Constituent == 'Chromium':
        Unit = ' (µg/lit)'
        thresholdmax = 0     
        Class = "NA"          
    elif Constituent == 'Copper':
        Unit = ' (µg/lit)' 
        thresholdmax = 0     
        Class = "NA" 
    elif Constituent == 'Iron':
        Unit = ' (µg/lit)'
        thresholdmax = 0     
        Class = "NA" 
    elif Constituent == 'Lead':
        Unit = ' (µg/lit)'
        thresholdmax = 0     
        Class = "NA" 
    elif Constituent == 'Mercury':
        Unit = ' (µg/lit)'  
        thresholdmax = 0     
        Class = "NA" 
    elif Constituent == 'Zinc':
        Unit = ' (µg/lit)'    
        thresholdmax = 0     
        Class = "NA" 
    elif Constituent == 'Arsenic':
        Unit = ' (µg/lit)'
        thresholdmax = 0     
        Class = "NA" 
        
    elif Constituent == 'Selenium':
        Unit = ' (µg/lit)'
        thresholdmax = 0     
        Class = "NA" 
    elif Constituent == 'Phytoplankton':
        Unit = ' (# of individuals/ml)' 
        thresholdmax = 0     
        Class = "NA" 
    elif Constituent == 'Zooplankton':
        Unit = ' (# of individuals/ml)' 
        thresholdmax = 0     
        Class = "NA" 
    elif Constituent == 'Temperature':
        Unit = ' (°Celsius)'
        thresholdmax = 32.2     
        Class = "C" #done 
    elif Constituent == 'pH':
        Unit = ' (pH units)'
        thresholdmin = 6
        thresholdmax = 8.5
        Class = "A,B,C" # done 
    elif Constituent == 'Seechi Depth':
        Unit = ' (meters)' 
        thresholdmin = 0.8     
        Class = "C"  #done
    return Unit  , thresholdmin, thresholdmax  ,Class

    
# calculate subset of data    
def data(Data , Station)   :
    
    
    if Station =='All Stations':
        DataX=Data

    elif Station =='Anacostia Mainstem':
        DataX = Data[(Data['Watershed'] == "Anacostia Mainstem")] 

        
    elif Station =='Anacostia Tributary':
        DataX = Data[(Data['Watershed'] == "Anacostia Tributary")] 

    elif Station =='Kingman Lake':
        DataX = Data[(Data['Watershed'] == "Kingman Lake")] 

    elif Station =='Potomac Mainstem':
        DataX = Data[(Data['Watershed'] == "Potomac Mainstem")] 
        
    elif Station =='Potomac Tributary':
        DataX = Data[(Data['Watershed'] == "Potomac Tributary")] 
        
    elif Station =='Rock Creek':
        DataX = Data[(Data['Watershed'] == "Rock Creek")] 
        
    elif Station =='Rock Creek Tributary':
        DataX = Data[(Data['Watershed'] == "Rock Creek Tributary")] 

    elif Station =='Ship Channel':
        DataX = Data[(Data['Watershed'] == "Ship Channel")] 

    elif Station =='Tidal Basin':
        DataX = Data[(Data['Watershed'] == "Tidal Basin")] 

    elif Station =='Chain Bridge (USGS)':
        DataX = Data[(Data['Watershed'] == "Chain Bridge (USGS)")]         
    else:
        DataX =  Data[(Data['Station'] == Station)]      
    return DataX    
