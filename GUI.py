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



from analysis import graph , graph2 , graph3, graph4 , AnaVSPot,AnaVSPot2, AnaVSPot3
import pandas as pd



#---------------------read data-------------------------------------------------------------
Data = pd.read_csv('ambient2.csv')
Data['Date'] = pd.to_datetime(Data['Date'])
Data.index = Data['Date']
del Data['Date']
Data['months'] = Data.index.to_period('M')  #making monthly data
Data['months2']=Data.index.month
Data['year']=Data.index.year
Data['quarter']=Data.index.quarter
Data['YearQuart']= Data.index.to_period('q')
DataX = Data
 
PlotType = ""
text = ""

def f(Constituent,Station,PlotType):
    

    
    
    
    if PlotType == "CDF and Histograms":
        text =graph(Data , Station, Constituent  )
        display(text)
    
    elif PlotType == "Boxplots by month":
        stats1 , stats2 , stats3 =graph2(Data , Station, Constituent  )
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
            display(HTML(text))
            display(HTML(stats3.to_html()))
            
            
    elif PlotType == "Boxplots by station":
        stats1 , stats2 , stats3= graph3(Data , Station, Constituent  )
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
            display(HTML(text))
            display(HTML(stats3.to_html()))
    
    elif PlotType == "Boxplots by year":
        stats1 , stats2 , stats3 =graph4(Data , Station, Constituent  )
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
            display(HTML(text))
            display(HTML(stats3.to_html()))
    
    elif PlotType == "Boxplots by Quarter":
        stats1 , stats2 , stats3 = AnaVSPot3( DataX , Constituent , Station) 
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
            display(HTML(text))
            display(HTML(stats3.to_html()))
    
    elif PlotType == "Draw Scatterplot (A vs P)":
        text =AnaVSPot2( DataX , Constituent , Station)    
        display(text)
    
    elif PlotType == "Draw Boxplot (A vs P)":
        text = AnaVSPot( DataX , Constituent , Station) 
        display(text)


interact_manual(f, Station = ["All stations" , "ANA01", "ANA08", "ANA14", "ANA21", "ANA29","All Anacostia" , "PMS01" , "PMS10", "PMS21", "PMS29" , "All Potomac"] ,\
         Constituent=["E.coli",	"Nitrite"	,"Ammonia"	,	"BOD5"	,"TSS",	"Chlorophyll a"		,"Hardness"	,"Alkalinity"	,"Turbidity",	"Dissolved Oxygen"	,	"Temperature"	,"pH",	"Seechi Depth","Cadmium"	,"Chromium",	"Copper",	"Iron"	,"Lead",	"Mercury",	"Zinc"	,"Arsenic",	"Selenium",	"Phytoplankton",	"Zooplankton","Total Phosphorus"	,"Total Soluble Phosphorus",	"Ortho-Phosphorus","Phaeophytin a"],\
         PlotType = ["Boxplots by year","Boxplots by month","Boxplots by station","Boxplots by Quarter","CDF and Histograms","Draw Boxplot (A vs P)","Draw Scatterplot (A vs P)"])
#


#get_ipython().run_line_magic('matplotlib', 'tk') 
#f("E.coli","All Anacostia","Boxplots by station")