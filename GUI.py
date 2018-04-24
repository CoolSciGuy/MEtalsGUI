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
from IPython.display import display



from analysis import graph , graph2 , graph3, graph4 , AnaVSPot,AnaVSPot2, AnaVSPot3
import pandas as pd



#---------------------read data-------------------------------------------------------------
Data = pd.read_csv('ambient.csv')
Data['Date'] = pd.to_datetime(Data['Date'])
Data.index = Data['Date']
del Data['Date']
Data['months'] = Data.index.to_period('M')  #making monthly data
Data['months2']=Data.index.month
Data['year']=Data.index.year
Data['quarter']=Data.index.quarter
DataX = Data
 
PlotType = ""
text = ""

def f(Constituent,Station,PlotType):
    

    
    
    
    if PlotType == "CDF and Histograms":
        text =graph(Data , Station, Constituent  )
        display(text)
    elif PlotType == "Boxplots by month":
        text =graph2(Data , Station, Constituent  )
        display(text)
    elif PlotType == "Boxplots by station":
        text = graph3(Data , Station, Constituent  )
        display(text)
    elif PlotType == "Boxplots by year":
        text =graph4(Data , Station, Constituent  )
        display(text)
    elif PlotType == "Boxplots by Quarter":
        text =AnaVSPot3( DataX , Constituent , Station) 
        display(text)
    elif PlotType == "Draw Scatterplot (A vs P)":
        text =AnaVSPot2( DataX , Constituent , Station)    
        display(text)
    elif PlotType == "Draw Boxplot (A vs P)":
        text =AnaVSPot( DataX , Constituent , Station) 
        display(text)


interact_manual(f, Station = ["All stations" , "ANA01", "ANA08", "ANA14", "ANA21", "ANA29","All Anacostia" , "PMS01" , "PMS10", "PMS21", "PMS29" , "All Potomac"] ,\
         Constituent=["E.coli",	"Nitrite"	,"Ammonia"	,"Total Phosphorus"	,"Total Soluble Phosphorus",	"Ortho-Phosphorus",	"BOD5"	,"TSS",	"Chlorophyll a"	,"Phaeophytin a"	,"Hardness"	,"Alkalinity"	,"Turbidity",	"Dissolved Oxygen"	,"Cadmium"	,"Chromium",	"Copper",	"Iron"	,"Lead",	"Mercury",	"Zinc"	,"Arsenic",	"Selenium",	"Phytoplankton",	"Zooplankton",	"Temperature"	,"pH",	"Seechi Depth"],\
         PlotType = ["CDF and Histograms","Boxplots by month","Boxplots by station","Boxplots by year","Boxplots by Quarter","Draw Boxplot (A vs P)","Draw Scatterplot (A vs P)"])




#f("E.coli","ANA01","Draw Scatterplot (A vs P)")






