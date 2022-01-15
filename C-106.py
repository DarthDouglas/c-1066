import pandas as pa
import plotly.express as px
import numpy as np
import csv
def getDataSource(dataPath):
    Coffeeinml=[]
    sleepinhours=[]
    with open(dataPath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            Coffeeinml.append(float(row["Coffeeinml"]))
            sleepinhours.append(float(row["sleepinhours"]))
    return{"x":Coffeinml,"y":sleepinhours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee in ml vs hours of sleep :-  \n--->",correlation[0,1])

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Coffeeinml", y="sleepinhours")
        fig.show()
def setup():
    data_path  = "C:\Users\Ezra\Desktop\Python\py\correlation-master\data\cups of coffe vs hours of sleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()

