# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:20:59 2018
Code modified on 03-05-18 to work better with datasets that have nan values.
@author: amirreza.sharifi
"""




import numpy as np
import matplotlib.pyplot as plt

def units(Constituent):
    thresholdmin = 0
    thresholdmax = 0
    if Constituent == 'Turbidity': 
        Unit = ' (NTU)' 
        thresholdmax = 20   #Turbidity increase above ambient (NTU) 
        
        Class = "A,B,C"  #done
    elif Constituent == 'E.coli':
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
    elif Constituent == 'TSS':
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

    
    
    



#CDF and Histogram
def graph(Data , Station, Constituent ):
    
    Unit= ""
    Unit =  units(Constituent )
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
        if Unit[1]!=0:
            plt.axvline(x=Unit[1], color='r', linestyle=':')
        if Unit[2]!=0:
            plt.axvline(x=Unit[2], color='r', linestyle=':')
        
        plt.subplot(212)
        plt.plot(np.sort(Data2), np.linspace(0,1,(Data2.size)))
        plt.xlabel(Constituent+Unit[0] + '  n= ' + str(Data2.size))
        plt.ylabel('Probability')
        plt.grid(True)
        
        if Unit[1]!=0:
            plt.axvline(x=Unit[1], color='r', linestyle=':',linewidth=2)
        if Unit[2]!=0:
            plt.axvline(x=Unit[2], color='r', linestyle=':',linewidth=2)
        plt.show()
        
        plt.rcParams.update({'font.size': 12})
        
        fifthP = np.nanpercentile(Data2,5)
        tenthP = np.nanpercentile(Data2,10)
        twentyfifthP = np.nanpercentile(Data2,25)
        fiftiethP = np.nanpercentile(Data2,50)
        SeventyFifthP = np.nanpercentile(Data2,75)
        NintiethP = np.nanpercentile(Data2,90)
        NintyfifthP = np.nanpercentile(Data2,95)
        Average = np.average(Data2)
        
        stats = '5th Pi = ' + str(round(fifthP,2))+'10th Pi = ' + str(round(tenthP,2)) + ', 25th Pi = ' + str(round(twentyfifthP,2)) +', Median = ' + str(round(fiftiethP,2)) +', 75th Pi = ' + str(round(SeventyFifthP,2)) +', 90th Pi = ' + str(round(NintiethP,2))+', 95th Pi = ' + str(round(NintyfifthP,2)) +', Average = ' + str(round(Average,2))  
        #return  'Distribution of Ambient '+Constituent+' data' + ' ('+Station+')' 
        
        return stats

#grouping all data by month        
def graph2(Data , Station, Constituent ):
    

    Unit= ""

    Unit =  units(Constituent )
    
    showflier = False  #outliers
    DataX=Data
    
    if Station =='All Anacostia':
        DataX=Data[(Data['Watershed'] == "Anacostia")]
    elif Station =='All Potomac':
        DataX = Data[(Data['Watershed'] == "Potomac")] 
    elif Station !='All stations' and Station !='All Anacostia' and Station !='All Potomac':
        DataX =  Data[(Data['Station'] == Station)] 

    if DataX[Constituent].sum() == 0:
        import pandas as pd
        return  pd.DataFrame({'A' : []}) , pd.DataFrame({'A' : []}) 

    else:
        DataX.boxplot(column = [Constituent],by='months2' , figsize = (15,6),showfliers=showflier)
        plt.ylabel(Constituent+Unit[0])
        plt.xlabel('Months, n = ' + str(DataX[Constituent].count()))
        plt.suptitle("")
        plt.title('Boxplot of Ambient '+Constituent+' over months' + ' ('+Station+')')
        plt.gcf().autofmt_xdate()
        if Unit[1]!=0:
            plt.axhline(y=Unit[1], color='r', linestyle=':')
        if Unit[2]!=0:
            plt.axhline(y=Unit[2], color='r', linestyle=':')           
        
        plt.show()
        
        

        
        stats = DataX [[ Constituent , 'months2']].groupby('months2').describe()
        stats2 = DataX [[ Constituent ]].describe()
        
        Violation = DataX[DataX[Constituent].gt(Unit[2])]             
        stats3 = Violation[[ Constituent , 'months2']].groupby('months2').describe()
        stats3['% Exceedence'] = stats3[stats3.columns[0]]/stats[stats.columns[0]]*100
        return  stats.round(decimals=2) , stats2.round(decimals=2)   , stats3.round(decimals=2) 
        

#grouping all data by station
def graph3(Data , Station, Constituent  ):

    
    Unit= ""
    Unit =  units(Constituent )
    showflier = False  #outliers

    DataX=Data
    if Station =='All Anacostia':
        DataX=Data[(Data['Watershed'] == "Anacostia")]
    elif Station =='All Potomac':
        DataX = Data[(Data['Watershed'] == "Potomac")] 
    elif Station !='All stations' and Station !='All Anacostia' and Station !='All Potomac':
        DataX =  Data[(Data['Station'] == Station)]     

    if DataX[Constituent].sum() == 0:
        import pandas as pd
        return  pd.DataFrame({'A' : []}) , pd.DataFrame({'A' : []}) 
    else:


        DataX.boxplot(column = [Constituent],by='Station' , figsize = (15,6),showfliers=showflier)
        plt.ylabel(Constituent+Unit[0] )
        plt.suptitle("")
        plt.xlabel('Stations, n = ' + str(DataX[Constituent].count()))
        plt.title('Boxplot of Ambient '+Constituent+' by station')
        plt.gcf().autofmt_xdate()
        if Unit[1]!=0:
            plt.axhline(y=Unit[1], color='r', linestyle=':')
        if Unit[2]!=0:
            plt.axhline(y=Unit[2], color='r', linestyle=':') 
        plt.show()
        
        


        
        stats = DataX [[ Constituent , 'Station']].groupby('Station').describe()
        stats2 = DataX [[ Constituent ]].describe()


        Violation = DataX[DataX[Constituent].gt(Unit[2])] 
        stats3 = Violation[[ Constituent , 'Station']].groupby('Station').describe()
        
        stats3['% Exceedence'] = stats3[stats3.columns[0]]/stats[stats.columns[0]]*100
        

            
        return  stats.round(decimals=2) , stats2.round(decimals=2)   , stats3.round(decimals=2)        



#grouping all data by year
def graph4(Data , Station, Constituent ):


    Unit= ""
    Unit =  units(Constituent )
    showflier = False  #outliers
    DataX = Data    
    if Station =='All Anacostia':
        DataX=Data[(Data['Watershed'] == "Anacostia")]
    elif Station =='All Potomac':
        DataX = Data[(Data['Watershed'] == "Potomac")] 
    elif Station !='All stations' and Station !='All Anacostia' and Station !='All Potomac':
        DataX =  Data[(Data['Station'] == Station)] 

    if DataX[Constituent].sum() == 0:
        import pandas as pd
        return  pd.DataFrame({'A' : []}) , pd.DataFrame({'A' : []}) 
    else:
        DataX.boxplot(column = [Constituent],by='year' , figsize = (15,6),showfliers=showflier)
        plt.ylabel(Constituent+Unit[0])
        plt.suptitle("")
        plt.xlabel('Years, n = ' + str(DataX[Constituent].count()))
        plt.title('Boxplot of Ambient '+Constituent+' by year'+ ' ('+Station+')')
        plt.gcf().autofmt_xdate()
        if Unit[1]!=0:
            plt.axhline(y=Unit[1], color='r', linestyle=':')
        if Unit[2]!=0:
            plt.axhline(y=Unit[2], color='r', linestyle=':')        
        plt.show()
        
        stats = DataX [[ Constituent , 'year']].groupby('year').describe()
        stats2 = DataX [[ Constituent ]].describe()        
        
        Violation = DataX[DataX[Constituent].gt(Unit[2])] 
        stats3 = Violation[[ Constituent , 'year']].groupby('year').describe()
        
        stats3['% Exceedence'] = stats3[stats3.columns[0]]/stats[stats.columns[0]]*100
        

            
        return  stats.round(decimals=2) , stats2.round(decimals=2)   , stats3.round(decimals=2)
            
            

#Potomac vs. Anacostia barplot
def AnaVSPot( DataX , Constituent , Station):
    import seaborn as sns
    
    
    #error if there is no data
    if DataX[Constituent].sum() == 0:
        return  "No data here"  
    else:
    
            
            
            
        Unit = ""
        Unit =  units(Constituent )
        plt.figure(3, figsize = (12,12))
        plt.rcParams.update({'font.size': 16})
        plt.title('Boxplot of Ambient '+Constituent+', Comparison between Anacostia and Potomac (all stations)')
        sns.boxplot(x="year", y= Constituent, hue="Watershed", data=DataX ,showfliers=False)    
        plt.ylabel(Constituent+Unit[0])
        if Unit[1]!=0:
            plt.axhline(y=Unit[1], color='r', linestyle=':')
        if Unit[2]!=0:
            plt.axhline(y=Unit[2], color='r', linestyle=':')        
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
        Unit =  units(Constituent)
        plt.rcParams.update({'font.size': 16})
        sns.lmplot( x="stamp", y=Constituent, data=DataX, fit_reg=False, hue='Watershed' , size = 7 , aspect = 2)    
        plt.title('Scatterplot of Ambient '+Constituent+', Comparison between Anacostia and Potomac (all stations)')
        plt.ylabel(Constituent+Unit[0])
        if Unit[1]!=0:
            plt.axhline(y=Unit[1], color='r', linestyle=':')
        if Unit[2]!=0:
            plt.axhline(y=Unit[2], color='r', linestyle=':')        
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
        import pandas as pd
        return  pd.DataFrame({'A' : []}) , pd.DataFrame({'A' : []}) 
    else:
    

        Unit = ""
        Unit =  units(Constituent )
        plt.figure(3, figsize = (20,12))
        plt.rcParams.update({'font.size': 16})
        sns.boxplot(x="year", y= Constituent, hue="quarter", data=DataX,showfliers=False )    
        plt.title('Boxplot of Ambient '+Constituent+' by year and quarter'+ ' ('+Station+')')
        plt.ylabel(Constituent+Unit[0])
        if Unit[1]!=0:
            plt.axhline(y=Unit[1], color='r', linestyle=':')
        if Unit[2]!=0:
            plt.axhline(y=Unit[2], color='r', linestyle=':')        
        plt.show() 
        
 
        stats = DataX [[ Constituent , 'quarter']].groupby('quarter').describe()
        stats2 = DataX [[ Constituent ]].describe()
#        stats3 = DataX [[ Constituent , 'YearQuart']].groupby('YearQuart').describe()

        Violation = DataX[DataX[Constituent].gt(Unit[2])]             
        stats3 = Violation[[ Constituent , 'quarter']].groupby('quarter').describe()
        stats3['% Exceedence'] = stats3[stats3.columns[0]]/stats[stats.columns[0]]*100
        
        
        return  stats.round(decimals=2) , stats2.round(decimals=2)   , stats3.round(decimals=2)         
        
        

        
        
