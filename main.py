import pandas as pd   
import chart_studio.plotly as py  
import plotly.graph_objs as go  
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot  

   
# get data from that url  (as a list)
df = pd.read_html('https://www.worldometers.info/coronavirus/#countries')  
   

# indexing 
df = df[0]  
type(df)  
df.info()  
df.rename(columns = {"Country,Other": "COUNTRY"}, inplace=True)  
# fill NaN and Change columntype 
#  
df["NewCases"] = df["NewCases"].fillna(0).astype('int')  
df["TotalDeaths"] = df["TotalDeaths"].fillna(0).astype('int')  
df["NewDeaths"] =df["NewDeaths"].fillna(0).astype('int')  
df["TotalRecovered"] = df["TotalRecovered"].fillna(0).astype('int')  
df["ActiveCases"] = df["ActiveCases"].fillna(0).astype('int')  
df["Serious,Critical"] =df["Serious,Critical"].fillna(0).astype('int')  
df.info()  
df['text'] = df.apply(lambda r : "Deaths: " + str(r.TotalDeaths + r.NewDeaths) + " Suspected: " + " " + str(r.NewCases + r.ActiveCases),  
axis = 1)  


country_code=pd.read_csv("countrycode.csv")  
# dataframe to dictionary  
country_code.set_index('COUNTRY', inplace=True)  
dict_country_code = country_code.to_dict()  
REPLACE_LIST = dict_country_code['CODE']   
  
# Replace Country with Codes  
df.replace(REPLACE_LIST, inplace=True)  
 
data = dict(  
   type = 'choropleth',  
   colorscale = 'ylorrd',  
   locations = df['COUNTRY'].values,  
   z = df['TotalCases'],  
   text = df['text'],  
   colorbar = {'title' : 'Corona Total Cases'},  
)  




layout = dict(  
   title = 'Global Corona stats',  
   geo = dict(  
               showframe = False,  
               projection = {'type':'natural earth'}  
            )  
   )  
   
choromap = go.Figure(data = [data],layout = layout)  
plot(choromap)  