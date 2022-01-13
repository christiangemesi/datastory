import pandas as pd
import numpy as np

def dfPerYear(year):
    
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