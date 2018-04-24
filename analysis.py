# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:20:59 2018
Code modified on 03-05-18 to work better with datasets that have nan values.
@author: amirreza.sharifi
"""




import numpy as np
import matplotlib.pyplot as plt

def units(Constituent,Unit):
    if Constituent == 'Turbidity': 
        Unit = ' (FNU)' 
    elif Constituent == 'E.coli':
        Unit = ' (cfu/100 ml)'
    elif Constituent == 'Nitrite':
        Unit = ' (mg/lit)'
    elif Constituent == 'Ammonia':
        Unit = ' (mg/lit)'
    elif Constituent == 'Total Phosphorus':
        Unit = ' (mg/lit)'
    elif Constituent == 'Total Soluble Phosphorus':
        Unit = ' (mg/lit)'
    elif Constituent == 'Ortho-Phosphorus':
        Unit = ' (mg/lit)'
    elif Constituent == 'BOD5':
        Unit = ' (mg/lit)'
    elif Constituent == 'TSS':
        Unit = ' (mg/lit)'
    elif Constituent == 'Chlorophyll a':
        Unit = ' (mg/m3)'
    elif Constituent == 'Phaeophytin a':
        Unit = ' (mg/lit)'
    elif Constituent == 'Hardness':
        Unit = ' (mg/lit)'
    elif Constituent == 'Alkalinity':
        Unit = ' (mg/lit)'        
    elif Constituent == 'Dissolved Oxygen':
        Unit = ' (mg/lit)'
    elif Constituent == 'Cadmium':
        Unit = ' (µg/lit)'
    elif Constituent == 'Chromium':
        Unit = ' (µg/lit)'          
    elif Constituent == 'Copper':
        Unit = ' (µg/lit)'        
    elif Constituent == 'Iron':
        Unit = ' (µg/lit)'
    elif Constituent == 'Lead':
        Unit = ' (µg/lit)'
    elif Constituent == 'Mercury':
        Unit = ' (µg/lit)'  
    elif Constituent == 'Zinc':
        Unit = ' (µg/lit)'        
    elif Constituent == 'Arsenic':
        Unit = ' (µg/lit)'
    elif Constituent == 'Selenium':
        Unit = ' (µg/lit)'
    elif Constituent == 'Phytoplankton':
        Unit = ' (# of individuals/ml)' 
    elif Constituent == 'Zooplankton':
        Unit = ' (# of individuals/ml)'        
    elif Constituent == 'Temperature':
        Unit = ' (°Celsius)'
    elif Constituent == 'pH':
        Unit = ' (pH units)'
    elif Constituent == 'Seechi Depth':
        Unit = ' (meters)' 
    return Unit    

    
    
    




def graph(Data , Station, Constituent ):
    

    Unit= ""
    Unit =  units(Constituent,Unit)

    
    DataX=Data
    if Station =='All Anacostia':
        DataX=Data[(Data['Watershed'] == "Anacostia")]
    elif Station =='All Potomac':
        DataX = Data[(Data['Watershed'] == "Potomac")] 
    elif Station !='All stations' and Station !='All Anacostia' and Station !='All Potomac':
        DataX =  Data[(Data['Station'] == Station)]  
    

    #resample the dataset
    Data2 = DataX[Constituent].as_matrix() #matrix
    Data2=Data2[~np.isnan(Data2)]
    
    
    #error if there is no data
    if Data2.sum() == 0:
        return  "No data here"  

    else:        
        
        #CDF and Histogram
   
        plt.figure(1, figsize = (12,12))
        plt.rcParams.update({'font.size': 22})
        plt.subplot(211)
        plt.title('Distribution of Ambient '+Constituent+' data' + ' ('+Station+')' )
        plt.grid(True)
        plt.hist(Data2,  50, facecolor='green', edgecolor='blue' )
        plt.ylabel('Frequency')
        
        plt.subplot(212)
        plt.plot(np.sort(Data2), np.linspace(0,1,(Data2.size)))
        plt.xlabel(Constituent+Unit + '  n= ' + str(Data2.size))
        plt.ylabel('Probability')
        plt.grid(True)
        plt.show()
        plt.rcParams.update({'font.size': 12})
        return  'Distribution of Ambient '+Constituent+' data' + ' ('+Station+')' 
        
        
def graph2(Data , Station, Constituent ):
    #grouping all data by month

    Unit= ""
    Unit =  units(Constituent,Unit)
    showflier = True  #outliers
    DataX=Data
    
    if Station =='All Anacostia':
        DataX=Data[(Data['Watershed'] == "Anacostia")]
    elif Station =='All Potomac':
        DataX = Data[(Data['Watershed'] == "Potomac")] 
    elif Station !='All stations' and Station !='All Anacostia' and Station !='All Potomac':
        DataX =  Data[(Data['Station'] == Station)] 

    if DataX[Constituent].sum() == 0:
        return  "No data here" 
    else:
        DataX.boxplot(column = [Constituent],by='months2' , figsize = (15,6),showfliers=showflier)
        plt.ylabel(Constituent+Unit)
        plt.xlabel('Months, n = ' + str(DataX[Constituent].count()))
        plt.suptitle("")
        plt.title('Boxplot of Ambient '+Constituent+' over months' + ' ('+Station+')')
        plt.gcf().autofmt_xdate()
        plt.show()
        return  'Boxplot of Ambient '+Constituent+' over months' + ' ('+Station+')' 


def graph3(Data , Station, Constituent  ):

    
    Unit= ""
    Unit =  units(Constituent,Unit)
    showflier = True  #outliers

    DataX=Data
    if Station =='All Anacostia':
        DataX=Data[(Data['Watershed'] == "Anacostia")]
    elif Station =='All Potomac':
        DataX = Data[(Data['Watershed'] == "Potomac")] 
    elif Station !='All stations' and Station !='All Anacostia' and Station !='All Potomac':
        DataX =  Data[(Data['Station'] == Station)]     

    if DataX[Constituent].sum() == 0:
        return  "No data here" 
    else:
    #grouping all data by station
        if Station =='All stations' or Station =='All Anacostia' or Station =='All Potomac':
            DataX.boxplot(column = [Constituent],by='Station' , figsize = (15,6),showfliers=showflier)
            plt.ylabel(Constituent+Unit )
            plt.suptitle("")
            plt.xlabel('Stations, n = ' + str(DataX[Constituent].count()))
            plt.title('Boxplot of Ambient '+Constituent+' by station')
            plt.gcf().autofmt_xdate()
            plt.show()
            return  'Boxplot of Ambient '+Constituent+' by station'
        else:
            return  "Option not available , select (All stations) or (All potomac) to activate"



def graph4(Data , Station, Constituent ):
    #grouping all data by year

    Unit= ""
    Unit =  units(Constituent,Unit)
    showflier = True  #outliers
    DataX = Data    
    if Station =='All Anacostia':
        DataX=Data[(Data['Watershed'] == "Anacostia")]
    elif Station =='All Potomac':
        DataX = Data[(Data['Watershed'] == "Potomac")] 
    elif Station !='All stations' and Station !='All Anacostia' and Station !='All Potomac':
        DataX =  Data[(Data['Station'] == Station)] 

    if DataX[Constituent].sum() == 0:
        return  "No data here" 
    else:
        DataX.boxplot(column = [Constituent],by='year' , figsize = (15,6),showfliers=showflier)
        plt.ylabel(Constituent+Unit)
        plt.suptitle("")
        plt.xlabel('Years, n = ' + str(DataX[Constituent].count()))
        plt.title('Boxplot of Ambient '+Constituent+' by year'+ ' ('+Station+')')
        plt.gcf().autofmt_xdate()
        plt.show()
        return     'Boxplot of Ambient '+Constituent+' by year'+ ' ('+Station+')'
            
            

#Potomac vs. Anacostia barplot
def AnaVSPot( DataX , Constituent , Station):
    import seaborn as sns
    
    
    #error if there is no data
    if DataX[Constituent].sum() == 0:
        return  "No data here"  
    else:
    
            
            
            
        Unit = ""
        Unit =  units(Constituent,Unit)
        plt.figure(3, figsize = (12,12))
        plt.rcParams.update({'font.size': 16})
        plt.title('Boxplot of Ambient '+Constituent+', Comparison between Anacostia and Potomac (all stations)')
        sns.boxplot(x="year", y= Constituent, hue="Watershed", data=DataX ,showfliers=False)    
        plt.ylabel(Constituent+Unit)
        plt.show()
        return 'Boxplot of Ambient '+Constituent+', Comparison between Anacostia and Potomac (all stations)'

            
            
#Potomac vs. Anacostia scatterplot
def AnaVSPot2( DataX , Constituent , Station ):
    import seaborn as sns
    
    
    #error if there is no data
    if DataX[Constituent].sum() == 0:
        return  "No data here" 
    else:
    
              
            
        DataX['stamp'] = (DataX['months2']-0.5)/12 + DataX['year']
        Unit = ""
        Unit =  units(Constituent,Unit)
        plt.rcParams.update({'font.size': 16})
        sns.lmplot( x="stamp", y=Constituent, data=DataX, fit_reg=False, hue='Watershed' , size = 7 , aspect = 2)    
        plt.title('Scatterplot of Ambient '+Constituent+', Comparison between Anacostia and Potomac (all stations)')
        plt.ylabel(Constituent+Unit)
        plt.show()   
        return 'Scatterplot of Ambient '+Constituent+', Comparison between Anacostia and Potomac (all stations)'   
 
    # this function draws barplots seperated by year and quarter
def AnaVSPot3( DataX , Constituent , Station):
    import seaborn as sns

    
    #error if there is no data
    if Station =='All Anacostia':
        DataX=DataX[(DataX['Watershed'] == "Anacostia")]
    elif Station =='All Potomac':
        DataX = DataX[(DataX['Watershed'] == "Potomac")] 
    elif Station !='All stations' and Station !='All Anacostia' and Station !='All Potomac':
        DataX =  DataX[(DataX['Station'] == Station)]  
    
    
    
    if DataX[Constituent].sum() == 0:
        return  "No data here"  
    else:
    

        Unit = ""
        Unit =  units(Constituent,Unit)
        plt.figure(3, figsize = (20,12))
        plt.rcParams.update({'font.size': 16})
        sns.boxplot(x="year", y= Constituent, hue="quarter", data=DataX,showfliers=False )    
        plt.title('Boxplot of Ambient '+Constituent+' by year and quarter'+ ' ('+Station+')')
        plt.ylabel(Constituent+Unit)
        plt.show() 
        return  'Boxplot of Ambient '+Constituent+' by year and quarter'+ ' ('+Station+')'  
           