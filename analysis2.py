# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 13:22:01 2018

@author: amirreza.sharifi
"""

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
        
    else:
        DataX =  Data[(Data['Station'] == Station)]      
    return DataX    
