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
from analysis2 import read_data

Data = read_data()
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

interact_manual(f, Station = ["All Stations" , 'Anacostia Mainstem', 'Anacostia Tributary' , 'Kingman Lake' , 'Potomac Mainstem' , "Potomac Tributary" , "Rock Creek" , "Rock Creek Tributary" , "Ship Channel" , "Tidal Basin"  , "Chain Bridge (USGS)", "AAG01",	"AAG02",	"ANA01",	"ANA02",	"ANA03",	"ANA04",	"ANA05",	"ANA06",	"ANA07",	"ANA08",	"ANA09",	"ANA10",	"ANA11",	"ANA12",	"ANA13",	"ANA14",	"ANA15",	"ANA16",	"ANA17",	"ANA18",	"ANA19",	"ANA20",	"ANA21",	"ANA21 ",	"ANA22",	"ANA23",	"ANA24",	"ANA25",	"ANA26",	"ANA27",	"ANA29",	"ANA30" ,"TDU01",	"TFC01",	"TFD01",	"TFE01",	"TFS01",	"THR01",	"TNA01",	"TNS01",	"TOR01",	"TPB01",	"TTX27",	"TUT01",	"TWB01",	"TWB02",	"TWB03",	"TWB04",	"TWB05",	"TWB06" , "TFS01" ,"KNG01",	"KNG02" ,"PMS01",	"PMS02",	"PMS03",	"PMS05",	"PMS07",	"PMS08",	"PMS09",	"PMS10",	"PMS11",	"PMS12",	"PMS13",	"PMS16",	"PMS18",	"PMS21",	"PMS21 ",	"PMS23",	"PMS25",	"PMS27",	"PMS29",	"PMS31",	"PMS33",	"PMS35",	"PMS37",	"PMS39",	"PMS41",	"PMS44",	"PMS46",	"PMS48",	"PMS51" , "PMS52" ,"TBK01",	"TBR01", "TCO01", "TCO06" , "TDA01" , "TDO01" , "TFB01" , "TFB02","RCR01",	"RCR04","RCR07",	"RCR09" ,"TKV01""TLU01",	"TMH01",	"TPI01",	"TPO01",	"TPY01",	"TSO01" ,"PWC04"  ,"PTB01" ,"CHAIN" ] ,\
         Constituent=["Escherichia coli",	"Total suspended solids",'Dissolved Oxygen',	"Arsenic" , "Lead" , "Cadmium" , "Chromium",'Copper','Iron','Mercury','Zinc'],\
         PlotType = ["Boxplots by year","Boxplots by month","Boxplots by station","Boxplots by Quarter","CDF and Histograms"])





#get_ipython().run_line_magic('matplotlib', 'tk') 
#f("Zinc","All Stations","CDF and Histograms")