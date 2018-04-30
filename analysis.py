# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:20:59 2018
Code modified on 03-05-18 to work better with datasets that have nan values.
@author: amirreza.sharifi
"""




import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython
import Tkinter as tk
import ttk

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

    
    
    
#pop up message if there is no data
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x",  padx=8, pady=8)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()




def graph(Data , Station, Constituent , save, cdf , barMonth , barStation , barYear , barQuarter , barallMonths ,timeseries ,resolution):

    if save==1:
        get_ipython().run_line_magic('matplotlib', 'inline')
    else:
        get_ipython().run_line_magic('matplotlib', 'tk')
    
    Unit= ""
    Unit =  units(Constituent,Unit)

    
    
    #Universal image resolution
    resolution  =int(resolution)
    showflier = True  #outliers
    
        
    #resample the dataset
    if Station =='All Anacostia':
        Data=Data[(Data['Watershed'] == "Anacostia")]
    elif Station =='All Potomac':
        Data = Data[(Data['Watershed'] == "Potomac")] 
    elif Station <>'All stations' and Station <>'All Anacostia' and Station <>'All Potomac':
        Data =  Data[(Data['Station'] == Station)]      
    

    #resample the dataset
    Data2 = Data[Constituent].as_matrix() #matrix
    Data2=Data2[~np.isnan(Data2)]
    
    
    #error if there is no data
    if Data2.sum() == 0:
        popupmsg("No data here")  
    elif cdf +barMonth +barStation +barYear +barQuarter +barallMonths+timeseries ==0:
        popupmsg("No selections were made") 
    else:
        
        
        #CDF and Histogram
        if cdf ==1:
            
            
            fig=plt.figure(1, figsize = (12,12))
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
        
            if save==1:
                fig.savefig(Station+' Ambient ' + Constituent+ ' CDF and Histogram.jpg', dpi=resolution  )
                popupmsg("Graph was saved!")
        
        plt.rcParams.update({'font.size': 12})
       
        
        #grouping all data by month
        if barMonth==1:
            
            axes = Data.boxplot(column = [Constituent],by='months2' , figsize = (15,6),showfliers=showflier)
            plt.ylabel(Constituent+Unit)
            plt.xlabel('Months, n = ' + str(Data[Constituent].count()))
            plt.suptitle("")
            plt.title('Boxplot of Ambient '+Constituent+' over months' + ' ('+Station+')')
            plt.gcf().autofmt_xdate()
            #plt.show()
            if save==1:
                plt.savefig(Station+' Ambient '+Constituent+' Boxplot by months.jpg', dpi=resolution  )
                #popupmsg("Graph was saved!")
       
        #grouping all data by station
        if barStation==1:
            
            if Station =='All stations' or Station =='All Anacostia' or Station =='All Potomac':
                axes = Data.boxplot(column = [Constituent],by='Station' , figsize = (15,6),showfliers=showflier)
                plt.ylabel(Constituent+Unit )
                plt.suptitle("")
                plt.xlabel('Stations, n = ' + str(Data[Constituent].count()))
                plt.title('Boxplot of Ambient '+Constituent+' by station')
                plt.gcf().autofmt_xdate()
                #plt.show()
                if save==1:
                    plt.savefig(Station+' Ambient '+Constituent+' by station.jpg', dpi=resolution  )
                    #popupmsg("Graph was saved!")
        
                
        #grouping all data by year
        if barYear==1:
            axes = Data.boxplot(column = [Constituent],by='year' , figsize = (15,6),showfliers=showflier)
            plt.ylabel(Constituent+Unit)
            plt.suptitle("")
            plt.xlabel('Years, n = ' + str(Data[Constituent].count()))
            plt.title('Boxplot of Ambient '+Constituent+' by year'+ ' ('+Station+')')
            plt.gcf().autofmt_xdate()
            #plt.show()
            if save==1:
                plt.savefig(Station+' Ambient '+Constituent+' by year.jpg', dpi=resolution  )
#                popupmsg("Graph was saved!")
        
        #grouping all data by quarter
        if barQuarter==1:
            Data.boxplot(column = [Constituent],by='quarter' , figsize = (15,6),showfliers=showflier)
            plt.ylabel(Constituent+Unit)
            plt.suptitle("")
            plt.xlabel('quarters, n = ' + str(Data[Constituent].count()))
            plt.title('Boxplot of Ambient '+Constituent+' by quarter'+ ' ('+Station+')')
            plt.gcf().autofmt_xdate()
            #plt.show()
            if save==1:
                plt.savefig(Station+' Ambient '+Constituent+' by quarter.jpg', dpi=resolution  )
#                popupmsg("Graph was saved!")
        

        #grouping all data by year and month
        if barallMonths==1:
            for i in range(2008,2016):
                phrase = Station+ ' Ambient '+Constituent+ " "+   str(i) + ".jpg"
                resample =  Data[(Data.year == i)]
                resample.boxplot(column = [Constituent],by='months' , figsize = (15,6),showfliers=False)
                plt.ylabel(Constituent+Unit)
                oi =  Data[(Data['year'] == i)]
                plt.xlabel('Months, n = ' + str(oi[Constituent].count()))
                plt.title( 'Ambient '+Constituent+' Boxplot for year ' + str(i)+ ' ('+Station+')')
                plt.suptitle("")
                #plt.show()
                #axes.set_ylim(Data2[~np.isnan(Data2)].min(), Data2[~np.isnan(Data2)].max())
                if save==1:
                    plt.savefig(phrase, dpi=resolution  )

        #Timeseries
        if timeseries==1:
            fig=plt.figure(2, figsize = (12,6))
            plt.scatter(Data.index, Data[Constituent])
            plt.ylabel(Constituent+Unit)
            plt.suptitle("")
            plt.xlabel('quarters, n = ' + str(Data[Constituent].count()))
            plt.title('Scatterplot of Ambient '+Constituent+' over time for'+ ' ('+Station+')')
            plt.gcf().autofmt_xdate()
            #plt.show()
            if save==1:
                plt.savefig(Station+' Ambient '+Constituent+' Scatterplot.jpg', dpi=resolution  )
#                popupmsg("Graph was saved!")

        if save==1:
            popupmsg("Graph was saved!")

#Potomac vs. Anacostia
def AnaVSPot(save , DataX , Constituent , Station, resolution ):
    import seaborn as sns
    
    
    #error if there is no data
    if DataX[Constituent].sum() == 0:
        popupmsg("No data here")  
    else:
    
        if save==1:
            get_ipython().run_line_magic('matplotlib', 'inline')
        else:
            get_ipython().run_line_magic('matplotlib', 'tk')                
            
        resolution  =int(resolution)
              
        Unit = ""
        Unit =  units(Constituent,Unit)
        plt.figure(3, figsize = (12,12))
        plt.rcParams.update({'font.size': 16})
        sns.boxplot(x="year", y= Constituent, hue="Watershed", data=DataX ,showfliers=False)    
        plt.ylabel(Constituent+Unit)
        if save==1:
            plt.savefig('All stations Ambient '+Constituent+' by year - comparison.jpg', dpi=resolution  )  
            popupmsg("Graph was saved!")
            
            
#Potomac vs. Anacostia scatterplot
def AnaVSPot2(save , DataX , Constituent , Station ,resolution):
    import seaborn as sns
    
    
    #error if there is no data
    if DataX[Constituent].sum() == 0:
        popupmsg("No data here")  
    else:
    
        if save==1:
            get_ipython().run_line_magic('matplotlib', 'inline')
        else:
            get_ipython().run_line_magic('matplotlib', 'tk')                
            
        resolution  =int(resolution)
        DataX['stamp'] = (DataX['months2']-0.5)/12 + DataX['year']
        Unit = ""
        Unit =  units(Constituent,Unit)
#        plt.figure(figsize = (12,12))
        plt.rcParams.update({'font.size': 16})
        sns.lmplot( x="stamp", y=Constituent, data=DataX, fit_reg=False, hue='Watershed' , size = 7 , aspect = 2)    
        plt.ylabel(Constituent+Unit)
        if save==1:
            plt.savefig('All stations Ambient '+Constituent+' scatterplot - comparison.jpg', dpi=resolution  )  
            popupmsg("Graph was saved.")            
            
 

def AnaVSPot3(save , DataX , Constituent , Station ,resolution):
    import seaborn as sns
    
    
    #error if there is no data
    if Station =='All Anacostia':
        DataX=DataX[(DataX['Watershed'] == "Anacostia")]
    elif Station =='All Potomac':
        DataX = DataX[(DataX['Watershed'] == "Potomac")] 
    elif Station <>'All stations' and Station <>'All Anacostia' and Station <>'All Potomac':
        DataX =  DataX[(DataX['Station'] == Station)]  
    
    
    
    if DataX[Constituent].sum() == 0:
        popupmsg("No data here")  
    else:
    
        if save==1:
            get_ipython().run_line_magic('matplotlib', 'inline')
        else:
            get_ipython().run_line_magic('matplotlib', 'tk')                
            
        resolution  =int(resolution)
        Unit = ""
        Unit =  units(Constituent,Unit)
        plt.figure(3, figsize = (12,12))
        plt.rcParams.update({'font.size': 16})
        sns.boxplot(x="year", y= Constituent, hue="quarter", data=DataX,showfliers=False )    
        plt.ylabel(Constituent+Unit)
        if save==1:
            plt.savefig(Station+ 'Ambient '+Constituent+' by quarter.jpg', dpi=resolution  )  
            popupmsg("Graph was saved!")            
            
           