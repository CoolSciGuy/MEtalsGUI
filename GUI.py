# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 09:16:05 2018
@author: amirreza.sharifi
"""

#======================
# imports
#======================

from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display , HTML
import numpy as np
import os.path






from analysis import graph , graph2 , graph3, graph4 , AnaVSPot,AnaVSPot2, AnaVSPot3
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
    Data['months2']=Data.index.month
    Data['year']=Data.index.year
    Data['quarter']=Data.index.quarter
    Data['YearQuart']= Data.index.to_period('q')
    Data.to_csv("allSorted.csv", sep=',')
    




DataX = Data #needed when data is displayed by quarter
PlotType = ""
text = ""


def f(Constituent,Station,PlotType):
    

    
    
    
    if PlotType == "CDF and Histograms":
        text =graph(Data , Station, Constituent  )
        display(text)
    
    elif PlotType == "Boxplots by month":
        stats1 , stats2  =graph2(Data , Station, Constituent  )
        if stats1.empty:
            display(HTML('<h1>No data here</h1>'))
        else:
            text = '<h1>' + 'Descriptive Statistics for ' + Constituent+ ' (' + Station + ')</h1>'
            display(HTML(text))
            display(HTML(stats1.to_html()))
            text = '<h1>' + 'Descriptive Statistics for ' + Constituent+ ' (' + Station + ')(whole period)</h1>'
            display(HTML(text))
            display(HTML(stats2.to_html()))
            text = '<h1>' + 'Statistics for Exceedence of ' + Constituent+ ' over DC water quality standards(' + Station + ')(whole period)</h1>'
#            display(HTML(text))
#            display(HTML(stats3.to_html()))
            
            
    elif PlotType == "Boxplots by station":
        stats1 , stats2 = graph3(Data , Station, Constituent  )
        if stats1.empty:
            display(HTML('<h1>No data here</h1>'))
        else:        
            
            text = '<h1>' + 'Descriptive Statistics for ' + Constituent+ ' (' + Station + ')</h1>'
            display(HTML(text))
            display(HTML(stats1.to_html()))
            text = '<h1>' + 'Descriptive Statistics for ' + Constituent+ ' (' + Station + ')(whole period)</h1>'
            display(HTML(text))
            display(HTML(stats2.to_html()))
            text = '<h1>' + 'Statistics for Exceedence of ' + Constituent+ ' over DC water quality standards(' + Station + ')(whole period)</h1>'
#            display(HTML(text))
#            display(HTML(stats3.to_html()))
    
    elif PlotType == "Boxplots by year":
        stats1 , stats2  =graph4(Data , Station, Constituent  )
        if stats1.empty:
            display(HTML('<h1>No data here</h1>'))
        else:        
            
            text = '<h1>' + 'Descriptive Statistics for ' + Constituent+ ' (' + Station + ')</h1>'
            display(HTML(text))
            display(HTML(stats1.to_html()))
            text = '<h1>' + 'Descriptive Statistics for ' + Constituent+ ' (' + Station + ')(whole period)</h1>'
            display(HTML(text))
            display(HTML(stats2.to_html()))
            text = '<h1>' + 'Statistics for Exceedence of ' + Constituent+ ' over DC water quality standards(' + Station + ')(whole period)</h1>'
#            display(HTML(text))
#            display(HTML(stats3.to_html()))
    
    elif PlotType == "Boxplots by Quarter":
        stats1 , stats2  = AnaVSPot3( DataX , Constituent , Station) 
        if stats1.empty:
            display(HTML('<h1>No data here</h1>'))
        else:        
            text = '<h1>' + 'Descriptive Statistics for ' + Constituent+ ' (' + Station + ')</h1>'
            display(HTML(text))
            display(HTML(stats1.to_html()))
            text = '<h1>' + 'Descriptive Statistics for ' + Constituent+ ' (' + Station + ')(whole period)</h1>'
            display(HTML(text))
            display(HTML(stats2.to_html()))
            text = '<h1>' + 'Statistics for Exceedence of ' + Constituent+ ' over DC water quality standards(' + Station + ')(whole period)</h1>'
#            display(HTML(text))
#            display(HTML(stats3.to_html()))
    
    elif PlotType == "Draw Scatterplot (A vs P)":
        text =AnaVSPot2( DataX , Constituent , Station)    
        display(text)
    
    elif PlotType == "Draw Boxplot (A vs P)":
        text = AnaVSPot( DataX , Constituent , Station) 
        display(text)



#
#
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

interact_manual(f, Station = ["All Stations" , 'Anacostia Mainstem', 'Anacostia Tributary' , 'Kingman Lake' , 'Potomac Mainstem' , "Potomac Tributary" , "Rock Creek" , "Rock Creek Tributary" , "Ship Channel" , "Tidal Basin"  , "Chain Bridge (USGS)"] ,\
         Constituent=["Escherichia coli",	"Total suspended solids",	"Arsenic" , "Lead" , "Cadmium" , "Chromium",'Copper','Iron','Mercury','Zinc'],\
         PlotType = ["Boxplots by year","Boxplots by month","Boxplots by station","Boxplots by Quarter","CDF and Histograms"])





##get_ipython().run_line_magic('matplotlib', 'tk') 
#f("Lead","Anacostia Mainstem","Boxplots by month")