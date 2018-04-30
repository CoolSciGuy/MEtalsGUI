# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 09:16:05 2018

@author: amirreza.sharifi
"""

#======================
# imports
#======================
import Tkinter as tk
import ttk
from analysis import graph , AnaVSPot, AnaVSPot2, AnaVSPot3
#from PIL import  Image
import pandas as pd


# Create instance
win = tk.Tk()   
win.geometry("450x600")
win.wm_iconbitmap('DOEE.ico')  #icon
win.wm_title('DOEE water quality graphing tool')

#Style
s = ttk.Style()
s.configure('my.TButton', font=('Calibri', 11))

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



#-----------------------First Box -------------------------------------------------
mighty = ttk.LabelFrame(win, text='Settings')
mighty.grid(column=0, row=0, padx=8, pady=4)



# Creating Station names
ttk.Label(mighty, text="Station").grid(column=0, row=0)
station = tk.StringVar()
station_chosen = ttk.Combobox(mighty, width=20, textvariable=station, state='readonly')
station_chosen['values'] = ("All stations" , "ANA01", "ANA08", "ANA14", "ANA21", "ANA29","All Anacostia" , "PMS01" , "PMS10", "PMS21", "PMS29" , "All Potomac")
station_chosen.grid(column=0, row=1)
station_chosen.current(0)


# Creating constituent names
ttk.Label(mighty, text="Constituent").grid(column=1, row=0)
constituent = tk.StringVar()
constituent_chosen = ttk.Combobox(mighty, width=25, textvariable=constituent, state='readonly')
constituent_chosen['values'] = ("E.coli",	"Nitrite"	,"Ammonia"	,"Total Phosphorus"	,"Total Soluble Phosphorus",	"Ortho-Phosphorus",	"BOD5"	,"TSS",	"Chlorophyll a"	,"Phaeophytin a"	,"Hardness"	"Alkalinity"	,"Turbidity",	"Dissolved Oxygen"	,"Cadmium"	,"Chromium",	"Copper",	"Iron"	,"Lead",	"Mercury",	"Zinc"	,"Arsenic",	"Selenium",	"Phytoplankton",	"Zooplankton",	"Temperature"	,"pH",	"Seechi Depth")
constituent_chosen.grid(column=1, row=1)
constituent_chosen.current(0)



# resolution (dpi)
ttk.Label(mighty, text="Resolution (dpi)").grid(column=1, row=2)
resolution = tk.StringVar()
resolution_chosen = ttk.Combobox(mighty, width=25, textvariable=resolution, state='readonly')
resolution_chosen['values'] = ("200",	"300"	,"600"	,"1000")
resolution_chosen.grid(column=1, row=3)
resolution_chosen.current(0)



# What graphs to be drawn

# save graph?
radVar = tk.IntVar()
rad1 = tk.Checkbutton(mighty, text="Save graphs (will not display)", variable=radVar , font =  "Times 10 bold" )
rad1.grid(column=0, row=3, sticky=tk.W, padx=8, pady=4) 



#----------------------- Box 1.5 -------------------------------------------------
mightyonepointfive = ttk.LabelFrame(win, text='Select Graphs')
mightyonepointfive.grid(column=0, row=1, padx=8, pady=4)





radVar2 = tk.IntVar()
rad2 = tk.Checkbutton(mightyonepointfive, text="CDF and Histograms", variable=radVar2,width = 50 , anchor = 'w')
rad2.grid(column=0, row=0, sticky=tk.W, columnspan=200) 

radVar3 = tk.IntVar()
rad3 = tk.Checkbutton(mightyonepointfive, text="Boxplots by month", variable=radVar3)
rad3.grid(column=0, row=1, sticky=tk.W, columnspan=100) 

radVar4 = tk.IntVar()
rad4 = tk.Checkbutton(mightyonepointfive, text="Boxplots by station", variable=radVar4)
rad4.grid(column=0, row=2, sticky=tk.W, columnspan=100) 
#
radVar5 = tk.IntVar()
rad5 = tk.Checkbutton(mightyonepointfive, text="Boxplots by year", variable=radVar5)
rad5.grid(column=0, row=3, sticky=tk.W, columnspan=100) 

radVar6 = tk.IntVar()
rad6 = tk.Checkbutton(mightyonepointfive, text="Boxplots by Quarter", variable=radVar6)
rad6.grid(column=0, row=4, sticky=tk.W, columnspan=100) 

radVar7 = tk.IntVar()
rad7 = tk.Checkbutton(mightyonepointfive, text="Boxplots for all months", variable=radVar7)
rad7.grid(column=0, row=5, sticky=tk.W, columnspan=100) 

radVar8 = tk.IntVar()
rad8 = tk.Checkbutton(mightyonepointfive, text="Scatterplot", variable=radVar8)
rad8.grid(column=0, row=6, sticky=tk.W, columnspan=100) 


# Draw graph command
def click_me(): 
    graph(Data , station_chosen.get() , constituent_chosen.get() , radVar.get() , radVar2.get()  ,radVar3.get() ,radVar4.get() ,radVar5.get() ,radVar6.get() ,radVar7.get() ,radVar8.get() ,resolution.get() )

# Adding a Button
action = ttk.Button(mightyonepointfive, text="Produce graphs", command=click_me,  width = 30,style='my.TButton')   
action.grid(column=0, row=7, ipadx=2, ipady=2)    


  
#-------------------------------------- Second box --------------------------------------
mighty2 = ttk.LabelFrame(win, text='Anacostia vs. Potomac')
mighty2.grid(column=0, row=2, padx=8, pady=4, sticky='W')

ttk.Label(mighty2, text="Anacostia vs. Potomac (includes all data for all stations)                      ").grid(column=0, row=0 , padx=8, pady=4)



def compare():
    AnaVSPot(radVar.get() , DataX , constituent_chosen.get() , station_chosen.get()  ,resolution.get())

mapshow = ttk.Button(mighty2, text="Draw Boxplot", command= compare , width = 30 ,style='my.TButton')   
mapshow.grid(column=0, row=1,sticky='W', ipadx=2, ipady=2 , pady=2) 


def compare2():
    AnaVSPot2(radVar.get() , DataX , constituent_chosen.get() , station_chosen.get()  ,resolution.get())


mapshow = ttk.Button(mighty2, text="Draw Scatterplot", command= compare2 , width = 30 ,style='my.TButton')   
mapshow.grid(column=0, row=2,sticky='W', ipadx=2, ipady=2) 

def compare3():
    AnaVSPot3(radVar.get() , DataX , constituent_chosen.get() , station_chosen.get()  ,resolution.get())


mapshow = ttk.Button(mightyonepointfive, text="Draw Boxplot by quarter", command= compare3 , width = 30 ,style='my.TButton')   
mapshow.grid(column=0, row=8,sticky='W', ipadx=2, ipady=2) 





#------------------------------------ Third box -------------------------------
# We are creating a container frame to hold all other widgets
mighty3 = ttk.LabelFrame(win , text = "Options")
mighty3.grid(column=0, row=3, padx=8, pady=4)

ttk.Label(mighty3, text="Need to see a map?                                                                                     " ).grid(column=0, row=0, padx=8, pady=4)

def showmapofdc():
    import os
    cwd = os.getcwd()
    path = cwd +"\\Stations.jpg"
#    im=Image.open(path)  
#    im = Image.open(open(path, 'rb'))
    os.system("start " + path)
#    im.show()

#show map
mapshow = ttk.Button(mighty3, text="Show map", command=showmapofdc, width = 30 ,style='my.TButton' )   
mapshow.grid(column=0, row=1,sticky='W', ipadx=5, ipady=5)  




win.mainloop()