import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import folium


def scatterYearsWithKanton(year,wannaPlot):
    """
    This function does a scatter 
    plot with the passed year. wannaPlot can be True if the result 
    should be plotted or False if not.
    """
    
    
    df = pd.read_csv('preprocessed/processed_data.csv')
    del df['Unnamed: 0']
    
    kantons = ["AG","AI","AR","BE","BL","BS","FR","GE","GL","GR","JU","LU","NE","NW","OW","SG","SH","SO","SZ","TG","TI","UR","VD","VS","ZG","ZH"]
    
    data = {'Kanton': [],
        year: []
        }

    df2 = pd.DataFrame(data)
    
    
    for i in kantons:
        x = df.loc[df['Kanton'] == i, year].sum()

        dfLoop= pd.DataFrame({"Kanton":[i],
                              year:[x]})
        
        df2 = df2.append(dfLoop)
        

    if(wannaPlot):
        df2.plot(kind='scatter', x='Kanton', y=year ,color='red',figsize=(10,10))
        
def dfPerYear(year):
    """
    This function returns a dataframe looking as followed:
    
    Kanton    Year
    AG        547493.0
    AI        ...
    ...       ...
    
    The Kantons are fixed but the year can be passed to the function. It will show the population of that Kanton in the given Year under "Years"
    """
    
    
    df = pd.read_csv('preprocessed/processed_data.csv')
    del df['Unnamed: 0']
    
    kantons = ["AG","AI","AR","BE","BL","BS","FR","GE","GL","GR","JU","LU","NE","NW","OW","SG","SH","SO","SZ","TG","TI","UR","VD","VS","ZG","ZH"]
    
    data = {'Kanton': [],
        year: []
        }

    df2 = pd.DataFrame(data)
    
    for i in kantons:
        x = df.loc[df['Kanton'] == i, year].sum()

        dfLoop= pd.DataFrame({"Kanton":[i],
                              year:[x]})
        
        df2 = df2.append(dfLoop)
        
    return df2

def dfHeatMapCantons():
    """
    This function returns a dataframe looking as followed:
    
    Kanton    1850            1860            ...
    AG        199852.000000   194208.000000	
    AI        ...             ...             ...
    ...       ...             ...             ...
    
    It represents each Kanton with its population of each Year. It is the combination of the function "dfPerYear" for each year.
    """
    
    years = ["1860","1870", "1880","1890","1900","1910","1920","1930","1940","1950","1960","1970","1980","1990","2000"]

    dfYears = dfPerYear('1850')

    for i in years:
        dfUnused = dfPerYear(i)
        dfYears = pd.merge(dfYears,dfUnused, on= 'Kanton')    
    
    return dfYears

def BarYearsWithKanton(year,wannaPlot):
    """
    This function is similar to the "scatterYearsWithKanton" function just with bars.
    wannaPlot can be True if the result 
    should be plotted or False if not, in that case the function returns a dataframe looking as followed:
    
    Kanton    Year
    AG        547493.0
    AI        ...
    ...       ...
    
    Where as Year is the population of the passed Year.
    
    It does also plot a Boxplot with the available data if wannaPlot is True
    """
    
    
    df = pd.read_csv('preprocessed/processed_data.csv')
    del df['Unnamed: 0']
    
    years = ["1860","1870", "1880","1890","1900","1910","1920","1930","1940","1950","1960","1970","1980","1990","2000"]
    kantons = ["AG","AI","AR","BE","BL","BS","FR","GE","GL","GR","JU","LU","NE","NW","OW","SG","SH","SO","SZ","TG","TI","UR","VD","VS","ZG","ZH"]

    
    data = {'Kanton': [],
        year: []}

    df2 = pd.DataFrame(data)
    
    for i in kantons:
        x = df.loc[df['Kanton'] == i, year].sum()

        dfLoop= pd.DataFrame({"Kanton":[i],
                              year:[x]})
        df2 = df2.append(dfLoop)
        
    median = df2[year].median()
    mittelwert = df2[year].mean()
    quart_1, quart_u = np.percentile(df2[year],[25,75])
    
    df3 = df2.sort_values(by = year)
        
    if(wannaPlot):

        df3.plot(kind='bar', x='Kanton', y=year ,color='red',figsize=(10,10))
        plt.ylabel("Einwohner")
        plt.axhline(y = median, color = 'b', linestyle = '-',label="Median")    
        plt.axhline(y = mittelwert, color = 'g', linestyle = '-',label="Mittelwert")
        plt.axhline(y = quart_1, color = 'yellow', linestyle = '-',label="25%-Quartil")
        plt.axhline(y = quart_u, color = 'orange', linestyle = '-',label="75%-Quartil")
        
        plt.legend(loc='best')
        plt.show()
        
        print("Median: ",median)
        print("Mittelwert: ",mittelwert)
        print("25% Quartil:",quart_1)
        print("75% Quartil:", quart_u)
        
        df3.plot(kind='box', x='Kanton', y=year ,figsize=(10,10))
        plt.ylabel("Jahr")
        plt.ylabel("Einwohner")
  
    else:
        return df3
            
    
    
def form(kanton,wannaPlot):
    """
    This function is similar to the "BarYearsWithKanton" function. This time the Kanton can be passed
    and the function will plot a bar plot with the added Kanton in combination with all available years (1850-2000) 
    
    wannaPlot can be True if the result 
    should be plotted or False if not, in that case the function returns a dataframe looking as followed:
    
    	Menge       Year   Kanton
        ...         1850 .0   BE
    	413887.0	1860.0	  BE
        ...         1870.0
    
    Where as Menge is the population of the Year shown to the right of the passed kanton.
    
    It does also plot a Boxplot with the available data if wannaPlot is True
    
    """
    years = ["1850","1860","1870", "1880","1890","1900","1910","1920","1930","1940","1950","1960","1970","1980","1990","2000"]
    kantons = ["AG","AI","AR","BE","BL","BS","FR","GE","GL","GR","JU","LU","NE","NW","OW","SG","SH","SO","SZ","TG","TI","UR","VD","VS","ZG","ZH"]
    
    df = pd.read_csv('preprocessed/processed_data.csv')
    del df['Unnamed: 0']
    
    data = {'Menge': [],
            'Year': [],
            'Kanton': []
           }

    df2 = pd.DataFrame(data)
    
    for i in years:
        x = df.loc[df['Kanton'] == kanton, i].sum()
        
        dfLoop= pd.DataFrame({"Year":[i],
                              'Menge':[x],
                              'Kanton': kanton})

        df2 = df2.append(dfLoop)
        
    df2 = df2.astype({'Year':float})
    
    
    median = df2['Menge'].median()
    mittelwert = df2['Menge'].mean()
    quart_1, quart_u = np.percentile(df2['Menge'],[25,75])
    
    
    if(wannaPlot):
        df2.plot(kind='bar', x='Year', y='Menge' ,color='red',figsize=(10,10))
        plt.axhline(y = median, color = 'b', linestyle = '-',label="Median")    
        plt.axhline(y = mittelwert, color = 'g', linestyle = '-',label="Mittelwert")
        plt.axhline(y = quart_1, color = 'yellow', linestyle = '-',label="25%-Quartil")
        plt.axhline(y = quart_u, color = 'orange', linestyle = '-',label="75%-Quartil")
        
        plt.legend(loc='best')
        plt.show()
        
        
        print("Median: ",median)
        print("Mittelwert: ",mittelwert)
        print("25% Quartil:",quart_1)
        print("75% Quartil:", quart_u)
        
        df2.plot(kind='box', x='Kanton', y='Menge' ,figsize=(10,10))
        plt.ylabel("Jahr")
        plt.ylabel("Einwohner")
        
    else:
        return df2
        
    
def BarYearsWithStaedte(year,kanton,wannaPlot):
    """
    This function shows all cities of the given kanton and the given year in a bar plot if wannaPlot is True.
    if WannaPlot is False the function returns a dataframe looking as followed:
    
    
    Menge     Stadt      Year
    9735.0    Aesch (BL) 2000
    ....      ....       2000
    
    """
    
    
    
    df = pd.read_csv('preprocessed/processed_data.csv')
    del df['Unnamed: 0']
    
    y = df.loc[(df['Kanton'] == kanton)]
    staedte = y.Stadt.unique()
    
    data = {'Menge': [],
            'Stadt': [],
            'Year': [],
           }
    
    df2 = pd.DataFrame(data)
    
    for i in staedte:
        x = df.loc[(df['Kanton'] == kanton) & (df['Stadt'] == i) , year].sum()
        
        dfLoop= pd.DataFrame({"Year":[year],
                              'Menge':[x],
                              'Stadt': [i],
                             })
        df2 = df2.append(dfLoop)
        
    median = df2['Menge'].median()
    mittelwert = df2['Menge'].mean()
    quart_1, quart_u = np.percentile(df2['Menge'],[25,75])
    
    df3 = df2.sort_values(by = 'Menge',ascending = False)
    
    if(wannaPlot):
        df3.plot(kind='bar', x='Stadt', y='Menge' ,color='red',figsize=(70,10))
        plt.axhline(y = median, color = 'b', linestyle = '-',label="Median")    
        plt.axhline(y = mittelwert, color = 'g', linestyle = '-',label="Mittelwert")
        plt.axhline(y = quart_1, color = 'yellow', linestyle = '-',label="25%-Quartil")
        plt.axhline(y = quart_u, color = 'orange', linestyle = '-',label="75%-Quartil")
        plt.legend(loc='best')
        plt.show()
        
        print("Median: ",median)
        print("Mittelwert: ",mittelwert)
        print("25% Quartil:",quart_1)
        print("75% Quartil:", quart_u)
        
        df3.plot(kind='box', x='Stadt', y='Menge' ,figsize=(10,10))
        plt.ylabel("Jahr")
        plt.ylabel("Einwohner")
        
        
    else:
        return df3
        
    
def plotBubbleMap(year):
    """
    This function shows the population of Switzerland of the given year in a bubble map
    
    """
    
    
    
    dfplot= BarYearsWithKanton(year,False)
    
    dfplot = dfplot.sort_values(by=['Kanton'])
    
    dfplot['north'] = [47.3877,47.3162,47.3665,46.7989,47.4418,47.5619,46.6817,46.2180,47.0404,46.6570,47.3444,47.0796,46.9900,46.9267,46.8779, 47.1456, 47.7009, 47.3321, 47.0724, 47.6038, 46.3317, 46.7739, 46.5613, 46.1905, 47.1662, 47.3769]
    dfplot['east'] = [8.2554, 9.4317, 9.3001, 7.7081, 7.5928, 7.5886, 7.1173, 6.1217, 9.0672, 9.5780, 7.1431, 8.1662, 6.9293, 8.3850, 8.2512, 9.3504, 8.5680, 7.6388, 8.7904, 9.0557, 8.8005, 8.6025, 6.5368, 7.5449, 8.5155, 8.6356]
    
    mapObj = folium.Map(location=[46.8182,8.2275], zoom_start =8)

    borderStyle={
        "geight":2,
        "fill":False
    }


    folium.GeoJson(data="switzerland.geojson",
                   name="Borders",
                   style_function=lambda x:borderStyle).add_to(mapObj)

    plantsLayer = folium.FeatureGroup("Power Plants").add_to(mapObj)

    for i in range (len(dfplot)):
        northVal= dfplot.iloc[i]["north"]
        eastVal = dfplot.iloc[i]["east"]
        populationStr = dfplot.iloc[i][year]
        kantonStr = dfplot.iloc[i]['Kanton']
        cRad =populationStr/40

        html = kantonStr, populationStr

        folium.Circle(
            location=[northVal,eastVal],
            radius=cRad,
            color='green',
            weight=2,
            fill=True,
            popup= html
        ).add_to(plantsLayer)
    folium.LayerControl().add_to(mapObj)
    
    return mapObj

    