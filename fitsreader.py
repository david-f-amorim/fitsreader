###basic programme for reading and displaying .fits files

##importing packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from astropy.io import fits
from astropy.utils.data import download_file 

##importing data; creating three-dimensional array with first dimension representing layers
def get_data(p=True,path="",url=""):
    if p==True:
        image_data=fits.getdata(path)
    if p==False:
        image_file=download_file(url, cache=True)
        image_data= fits.getdata(image_file)
    return image_data

##restructure data to transform into galactical coordinates
def restructure(i,p1=True,x=""):
    image_data=get_data(p=p1,path=x)
    layer=image_data[i-1]
    x=layer[:,:180]
    xf=np.flip(x,axis=1)
    y=layer[:,180:]
    yf=np.flip(y,axis=1)
    d1=np.array(xf)
    d2=np.array(yf)
    data=np.concatenate((d1,d2),axis=1)
    return data

## function to display aitoff projection of individual layer in galactical coordinates
def aitoff_layer(layer_number,lis,cmin=0,cmax=5,safe=True,filename="",local_file=True,path_or_url="",cont='n',contco='purple'):
    
    ##transforming data and plotting projection
    fig = plt.figure(figsize=(15,10))
    ax = fig.add_subplot(111, projection='aitoff')
    
    ##functions to plot sources
    #transform deg to rad
    def rad(n):
        return n*(np.pi/180)

    #transform galactical into normal coordinates
    def transform(xd):
        if xd<=np.pi:
            xd=-xd
        if xd>np.pi:
            xd=2*np.pi-xd
        if xd==2*np.pi:
            xd=0
        return xd

    #plot sources:
    def plot_source(x,y,stype,name,colour,size):
        xd=transform(rad(x))
        yd=rad(y)
        a=ax.plot(xd,yd,stype,color=colour)
        b=ax.text(xd,yd+rad(2),name,fontsize=size,color=colour)
        return a,b

    #import data from csv file into array
    def csv_to_arr(filename="sources.csv"):
        csv=pd.read_csv(filename)
        ls=[]
        for i in np.arange(0,csv.shape[0]):
            for j in np.arange(0,csv.shape[1]):
                ls.append(csv.iloc[i][j])
            plot_source(name=ls[0],x=ls[1],y=ls[2],stype=ls[3],colour=ls[4],size=ls[5])
            ls=[]
        return ls

    csv_to_arr()
    
    i=layer_number
    arr=restructure(i,p1=local_file,x=path_or_url)
    lon = np.linspace(-np.pi, np.pi,360)
    lat = np.linspace(-np.pi/2., np.pi/2.,180)
    Lon,Lat = np.meshgrid(lon,lat)
    
    
    def lis_to_list(string=lis):
        li=list(string.split(' '))
        return li
    
    li=lis_to_list()

    if cont=='yy':
        im=ax.pcolormesh(Lon,Lat,arr,vmin=cmin,vmax=cmax,cmap='coolwarm')
        im2=ax.contour(Lon,Lat,arr,colors=contco,levels=li)
        cbar2=fig.colorbar(im,shrink=0.6) 
        cbar2.ax.tick_params(labelsize=14)
        cbar2.add_lines(im2)
    elif cont=='y':
        im=ax.contour(Lon,Lat,arr,colors=contco,levels=li)
        cbar=fig.colorbar(im,shrink=0.6) 
        cbar.ax.tick_params(labelsize=14)
    elif cont=='n': 
        im= ax.pcolormesh(Lon,Lat,arr,vmin=cmin,vmax=cmax,cmap='coolwarm')
        cbar=fig.colorbar(im,shrink=0.6) 
        cbar.ax.tick_params(labelsize=14)
        
    
    plt.subplots_adjust(left = 0.1,right = 1,bottom = 0,top = 1 ,wspace = 0,hspace = 0.1)
    
    ##design specifics
    fig.patch.set_facecolor('#FFFFFF')
    x=np.linspace(-np.pi, np.pi,13)
    y=x[1:13]
    plt.xticks(y,["150$\degree$",'120$\degree$','90$\degree$','60$\degree$','30$\degree$','0$\degree$','330$\degree$','300$\degree$','270$\degree$','240$\degree$','210$\degree$'],fontsize=14)
    plt.yticks(fontsize=14)
    ax.grid(True,linestyle='-', linewidth=0.35,which='both')
    title=['Likelihood Ratio','Number of Counts', 'Error on Counts','Flux (x10^8) [ph/(cm^2*s)]', 'Error on Flux','?']
    plt.title(title[i-1],fontsize=18)
    
    ##saving the file
    if safe==True:
        plt.savefig(filename+".png")
    else: plt.show()
    
    
##asks for input variables and plots    
def start_plotting():
    dinput=pd.read_csv('input.csv')
    ls=[]
    for i in np.arange(0,dinput.shape[0]):
        for j in np.arange(0,dinput.shape[1]):
            ls.append(dinput.iloc[i][j])
        aitoff_layer(layer_number=ls[2],filename=ls[1],path_or_url=ls[0],local_file=True,cont=ls[5],contco=ls[6],lis=ls[7],safe=True,cmin=ls[4],cmax=ls[3])
        ls=[]
    
##runs when programme is initiated
def start_code():
    print('''
===========================================================================
You have initiated the programme. The information entered into the files 
'input.csv' and 'sources.csv' is being processed and the resulting images 
are being saved. Check the file 'help.txt'for more information!
===========================================================================
''')
    start_plotting()
    
##exec
start_code()




