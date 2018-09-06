# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:20:59 2018
Code modified on 03-05-18 to work better with datasets that have nan values.
@author: amirreza.sharifi
"""



import numpy as np
import matplotlib.pyplot as plt

from analysis2 import units, data



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#CDF and Histogram
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def graph(Data , Station, Constituent ):
    
    Unit= ""
    Unit =  units(Constituent )
    Data= Data.dropna(subset = [Constituent])

    DataX = data(Data , Station)
     
    Data2 = DataX[Constituent].values #matrix
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


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#grouping all data by month        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
def graph2(Data , Station, Constituent ):
    

    Unit= ""
    Unit =  units(Constituent )    
    showflier = False  #outliers
    Data= Data.dropna(subset = [Constituent]) 
    DataX = data(Data , Station)
    
    if DataX[Constituent].sum() == 0:
        import pandas as pd
        return  pd.DataFrame({'A' : []}) , pd.DataFrame({'A' : []}) 
    else:
        DataX.boxplot(column = [Constituent],by='month' , figsize = (15,6),showfliers=showflier)
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
         
        stats = DataX [[ Constituent , 'month']].groupby('month').describe()
        stats2 = DataX [[ Constituent ]].describe()
        
        Violation = DataX[DataX[Constituent].gt(Unit[2])]             
        #stats3 = Violation[[ Constituent , 'month']].groupby('month').describe()
        #stats3['% Exceedence'] = stats3[stats3.columns[0]]/stats[stats.columns[0]]*100
        return  stats.round(decimals=2) , stats2.round(decimals=2)   #, stats3.round(decimals=2) 
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#grouping all data by station
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        
def graph3(Data , Station, Constituent  ):

    
    Unit= ""
    Unit =  units(Constituent )
    showflier = False  #outliers

    Data= Data.dropna(subset = [Constituent]) 
    DataX = data(Data , Station)


    if DataX[Constituent].sum() == 0:
        import pandas as pd
        return  pd.DataFrame({'A' : []}) , pd.DataFrame({'A' : []}) 
    else:


        DataX.boxplot(column = [Constituent],by='Station' , figsize = (15,6),showfliers=showflier)
        plt.ylabel(Constituent+Unit[0] )
        plt.suptitle("")
        plt.xlabel('Stations, n = ' + str(DataX[Constituent].count()))
        plt.title('Boxplot of Ambient '+Constituent+' by station' + " ("+Station + ")")
        plt.gcf().autofmt_xdate()
        if Unit[1]!=0:
            plt.axhline(y=Unit[1], color='r', linestyle=':')
        if Unit[2]!=0:
            plt.axhline(y=Unit[2], color='r', linestyle=':') 
        plt.show()
        
        stats = DataX [[ Constituent , 'Station']].groupby('Station').describe()
        stats2 = DataX [[ Constituent ]].describe()

        Violation = DataX[DataX[Constituent].gt(Unit[2])] 
#        stats3 = Violation[[ Constituent , 'Station']].groupby('Station').describe()
        
#        stats3['% Exceedence'] = stats3[stats3.columns[0]]/stats[stats.columns[0]]*100
        

            
        return  stats.round(decimals=2) , stats2.round(decimals=2)   #, stats3.round(decimals=2)        


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#grouping all data by year
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def graph4(Data , Station, Constituent ):


    Unit= ""
    Unit =  units(Constituent )
    showflier = False  #outliers
    Data = Data.dropna(subset = [Constituent])  
    DataX = data(Data , Station)
    


    if DataX[Constituent].sum() == 0:
        import pandas as pd
        return  pd.DataFrame({'A' : []}) , pd.DataFrame({'A' : []}) 
    else:
        ax=DataX.boxplot(column = [Constituent],by='year' , figsize = (15,6),showfliers=showflier)
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
#        stats3 = Violation[[ Constituent , 'year']].groupby('year').describe()
        
#        stats3['% Exceedence'] = stats3[stats3.columns[0]]/stats[stats.columns[0]]*100
        
        
            
        return  stats.round(decimals=2) , stats2.round(decimals=2)  # , stats3.round(decimals=2)
            
            
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Potomac vs. Anacostia barplot
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------        
def AnaVSPot( DataX , Constituent , Station):
    import seaborn as sns
    
    Data= DataX.dropna(subset = [Constituent]) 
    DataX=Data
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

            
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------           
#Potomac vs. Anacostia scatterplot
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        
def AnaVSPot2( DataX , Constituent , Station ):
    import seaborn as sns
    
    Data= DataX.dropna(subset = [Constituent]) 
    DataX=Data
    #error if there is no data
    if DataX[Constituent].sum() == 0:
        return  "No data here" 
    else:
    
              
            
        DataX['stamp'] = (DataX['month']-0.5)/12 + DataX['year']
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


#----------------------------------------------------------------------------------------------------------------------------------------------------------------- 
# this function draws barplots seperated by year and quarter
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        
    
def AnaVSPot3( DataX , Constituent , Station):
    import seaborn as sns

    
    Data= DataX.dropna(subset = [Constituent]) 
    DataX = data(Data , Station)
    
    
    if DataX[Constituent].sum() == 0:
        import pandas as pd
        return  pd.DataFrame({'A' : []}) , pd.DataFrame({'A' : []}) 
    else:
    

        Unit = ""
        Unit =  units(Constituent )
        plt.figure(3, figsize = (20,12))
        plt.rcParams.update({'font.size': 16})
        ax = sns.boxplot(x="year", y= Constituent, hue="quarter", data=DataX,showfliers=False )    
        ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
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

#        Violation = DataX[DataX[Constituent].gt(Unit[2])]             
#        stats3 = Violation[[ Constituent , 'quarter']].groupby('quarter').describe()
#        stats3['% Exceedence'] = stats3[stats3.columns[0]]/stats[stats.columns[0]]*100
        
        return  stats.round(decimals=2) , stats2.round(decimals=2)  # , stats3.round(decimals=2)         
        
        

        
def AnaVSPot4( DataX , Constituent , Station):
    import seaborn as sns
    Data= DataX.dropna(subset = [Constituent]) 
    DataX=Data
    
    
    #error if there is no data
    if DataX[Constituent].sum() == 0:
        return  "No data here"  
    else:
    
        if Station[0] =='All Stations':
            DataX=Data
        elif Station[0] in {"AAG01",	"AAG02",	"ANA01",	"ANA02",	"ANA03",	"ANA04",	"ANA05",	"ANA06",	"ANA07",	"ANA08",	"ANA09",	"ANA10",	"ANA11",	"ANA12",	"ANA13",	"ANA14",	"ANA15",	"ANA16",	"ANA17",	"ANA18",	"ANA19",	"ANA20",	"ANA21",	"ANA21 ",	"ANA22",	"ANA23",	"ANA24",	"ANA25",	"ANA26",	"ANA27",	"ANA29",	"ANA30" ,"TDU01",	"TFC01",	"TFD01",	"TFE01",	"TFS01",	"THR01",	"TNA01",	"TNS01",	"TOR01",	"TPB01",	"TTX27",	"TUT01",	"TWB01",	"TWB02",	"TWB03",	"TWB04",	"TWB05",	"TWB06" , "TFS01" ,"KNG01",	"KNG02" ,"PMS01",	"PMS02",	"PMS03",	"PMS05",	"PMS07",	"PMS08",	"PMS09",	"PMS10",	"PMS11",	"PMS12",	"PMS13",	"PMS16",	"PMS18",	"PMS21",	"PMS21 ",	"PMS23",	"PMS25",	"PMS27",	"PMS29",	"PMS31",	"PMS33",	"PMS35",	"PMS37",	"PMS39",	"PMS41",	"PMS44",	"PMS46",	"PMS48",	"PMS51" , "PMS52" ,"TBK01",	"TBR01", "TCO01", "TCO06" , "TDA01" , "TDO01" , "TFB01" , "TFB02","RCR01",	"RCR04","RCR07",	"RCR09" ,"TKV01""TLU01",	"TMH01",	"TPI01",	"TPO01",	"TPY01",	"TSO01" ,"PWC04"  ,"PTB01" ,"CHAIN"}:
            DataX =DataX[DataX['Station'].isin(Station)]
        else:
            DataX =DataX[DataX['Watershed'].isin(Station)]
            
    if DataX[Constituent].sum() == 0:
        return  "No data here" 
            
            
    Unit = ""
    Unit =  units(Constituent )
    plt.figure(3, figsize = (12,12))
    plt.rcParams.update({'font.size': 16})
    plt.title('Boxplot of Ambient '+Constituent+', Comparison between Anacostia and Potomac (all stations)')
    ax = sns.boxplot(x="year", y= Constituent, hue="Watershed", data=DataX ,showfliers=False)    
    ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
    plt.ylabel(Constituent+Unit[0])
    plt.xlabel('Years, n = ' + str(DataX[Constituent].count()))
    if Unit[1]!=0:
        plt.axhline(y=Unit[1], color='r', linestyle=':')
    if Unit[2]!=0:
        plt.axhline(y=Unit[2], color='r', linestyle=':')        
    plt.show()
    return 'Boxplot of Ambient '+Constituent+', Comparison between Anacostia and Potomac (all stations)'

         


def AnaVSPot5( DataX ,   Station , Constituent , time ):
    

    
    
    import seaborn as sns
    
    
    Data= DataX.dropna(subset = [Constituent]) 
    DataX=Data
    

    #error if there is no data
    if DataX[Constituent].sum() == 0:
        return  "No data here"  
    
    
    else:
    
        if Station[0] =='All Stations':
            DataX=Data
        elif Station[0] in {"AAG01",	"AAG02",	"ANA01",	"ANA02",	"ANA03",	"ANA04",	"ANA05",	"ANA06",	"ANA07",	"ANA08",	"ANA09",	"ANA10",	"ANA11",	"ANA12",	"ANA13",	"ANA14",	"ANA15",	"ANA16",	"ANA17",	"ANA18",	"ANA19",	"ANA20",	"ANA21",	"ANA21 ",	"ANA22",	"ANA23",	"ANA24",	"ANA25",	"ANA26",	"ANA27",	"ANA29",	"ANA30" ,"TDU01",	"TFC01",	"TFD01",	"TFE01",	"TFS01",	"THR01",	"TNA01",	"TNS01",	"TOR01",	"TPB01",	"TTX27",	"TUT01",	"TWB01",	"TWB02",	"TWB03",	"TWB04",	"TWB05",	"TWB06" , "TFS01" ,"KNG01",	"KNG02" ,"PMS01",	"PMS02",	"PMS03",	"PMS05",	"PMS07",	"PMS08",	"PMS09",	"PMS10",	"PMS11",	"PMS12",	"PMS13",	"PMS16",	"PMS18",	"PMS21",	"PMS21 ",	"PMS23",	"PMS25",	"PMS27",	"PMS29",	"PMS31",	"PMS33",	"PMS35",	"PMS37",	"PMS39",	"PMS41",	"PMS44",	"PMS46",	"PMS48",	"PMS51" , "PMS52" ,"TBK01",	"TBR01", "TCO01", "TCO06" , "TDA01" , "TDO01" , "TFB01" , "TFB02","RCR01",	"RCR04","RCR07",	"RCR09" ,"TKV01""TLU01",	"TMH01",	"TPI01",	"TPO01",	"TPY01",	"TSO01" ,"PWC04"  ,"PTB01" ,"CHAIN"}:
            DataX =DataX[DataX['Station'].isin(Station)]
        else:
            DataX =DataX[DataX['Watershed'].isin(Station)]
            
    if DataX[Constituent].sum() == 0:
        return  "No data here" 
            
    Unit = ""
    Unit =  units(Constituent)

#    plt.figure(3, figsize = (12,12))
#    plt.title('Boxplot of Ambient '+Constituent+', Comparison between Anacostia and Potomac (all stations)')
    sns.set(style="darkgrid")
    ax = sns.FacetGrid( DataX ,  row=time, col="Watershed", margin_titles=True) 
    bins = np.linspace(0, DataX[Constituent].max(), 10)
    ax.map(plt.hist, Constituent, color="steelblue", bins=bins)


#    plt.ylabel(Constituent+Unit[0])
#    plt.xlabel('Years, n = ' + str(DataX[Constituent].count()))
#    if Unit[1]!=0:
#        plt.axhline(y=Unit[1], color='r', linestyle=':')
#    if Unit[2]!=0:
#        plt.axhline(y=Unit[2], color='r', linestyle=':')        
#    plt.show()
    return 'Boxplot of Ambient '+Constituent+', Comparison between Anacostia and Potomac (all stations)'

