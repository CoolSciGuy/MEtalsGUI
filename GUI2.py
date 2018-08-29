# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 13:40:21 2018

@author: amirreza.sharifi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 09:16:05 2018
@author: amirreza.sharifi
"""

#======================
# imports
#======================

#from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display , HTML
import numpy as np
import os.path





from analysis import  AnaVSPot4
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
    
    conditions = [Condition1 , Condition2,Condition3 , Condition4,Condition5 , Condition6, Condition7 , Condition8, Condition9, Condition10]
    choices = ['Anacostia Mainstem', 'Anacostia Tributary' , 'Kingman Lake' , 'Potomac Mainstem' , "Potomac Tributary" , "Rock Creek" , "Rock Creek Tributary" , "Ship Channel" , "Tidal Basin" , "Chain Bridge (USGS)"   ]
    Data['Watershed'] = np.select(conditions, choices)


    Data['months'] = Data.index.to_period('M')  #making monthly data
    Data['months2']=Data.index.month
    Data['year']=Data.index.year
    Data['quarter']=Data.index.quarter
    Data['YearQuart']= Data.index.to_period('q')
    Data.to_csv("allSorted.csv", sep=',')
    




DataX = Data #needed when data is displayed by quarter
PlotType = ""
text = ""

#
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')


def ff(i , j):
    text = AnaVSPot4( DataX , j , i) 
    display(text)



i=widgets.SelectMultiple(
    options=["All Stations" , 'Anacostia Mainstem', 'Anacostia Tributary' , 'Kingman Lake' , 'Potomac Mainstem' , "Potomac Tributary" , "Rock Creek" , "Rock Creek Tributary" , "Ship Channel" , "Tidal Basin" , "Chain Bridge (USGS)"  ,"AAG01",	"AAG02",	"ANA01",	"ANA02",	"ANA03",	"ANA04",	"ANA05",	"ANA06",	"ANA07",	"ANA08",	"ANA09",	"ANA10",	"ANA11",	"ANA12",	"ANA13",	"ANA14",	"ANA15",	"ANA16",	"ANA17",	"ANA18",	"ANA19",	"ANA20",	"ANA21",	"ANA21 ",	"ANA22",	"ANA23",	"ANA24",	"ANA25",	"ANA26",	"ANA27",	"ANA29",	"ANA30" ,"TDU01",	"TFC01",	"TFD01",	"TFE01",	"TFS01",	"THR01",	"TNA01",	"TNS01",	"TOR01",	"TPB01",	"TTX27",	"TUT01",	"TWB01",	"TWB02",	"TWB03",	"TWB04",	"TWB05",	"TWB06" , "TFS01" ,"KNG01",	"KNG02" ,"PMS01",	"PMS02",	"PMS03",	"PMS05",	"PMS07",	"PMS08",	"PMS09",	"PMS10",	"PMS11",	"PMS12",	"PMS13",	"PMS16",	"PMS18",	"PMS21",	"PMS21 ",	"PMS23",	"PMS25",	"PMS27",	"PMS29",	"PMS31",	"PMS33",	"PMS35",	"PMS37",	"PMS39",	"PMS41",	"PMS44",	"PMS46",	"PMS48",	"PMS51" , "PMS52" ,"TBK01",	"TBR01", "TCO01", "TCO06" , "TDA01" , "TDO01" , "TFB01" , "TFB02","RCR01",	"RCR04","RCR07",	"RCR09" ,"TKV01""TLU01",	"TMH01",	"TPI01",	"TPO01",	"TPY01",	"TSO01" ,"PWC04"  ,"PTB01" ,"CHAIN" ],
    value=[ 'Anacostia Mainstem', 'Anacostia Tributary'],
    #rows=10,
    description='Stations',
    disabled=False)
 
j=widgets.Select(
    options=["Escherichia coli",	"Total suspended solids",'Dissolved Oxygen',	"Arsenic" , "Lead" , "Cadmium" , "Chromium",'Copper','Iron','Mercury','Zinc'],
    value="Escherichia coli",
    # rows=10,
    description='Constituent',
    disabled=False)

ui = widgets.HBox([i, j])
out =widgets.interactive_output(ff, {'i': i, 'j': j }  )


display(ui, out)



#
#get_ipython().run_line_magic('matplotlib', 'tk') 
#ff("Escherichia coli","Chain Bridge (USGS)","Boxplots by month")