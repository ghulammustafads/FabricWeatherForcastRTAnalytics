# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "jupyter",
# META     "jupyter_kernel_name": "python3.12"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "2eef2f20-6602-48be-9242-f1c3a7763e83",
# META       "default_lakehouse_name": "WeatherRTDataStore_bronze",
# META       "default_lakehouse_workspace_id": "78467d4c-62c3-435f-bebf-c9b75dd8aded",
# META       "known_lakehouses": [
# META         {
# META           "id": "2eef2f20-6602-48be-9242-f1c3a7763e83"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# # Weather Api Data Scraping (Realtime Anlaytics) Event Stream Feed  

# CELL ********************

import requests 
import json 
import pandas as pd
import matplotlib.pyplot as plt

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

lat = 69.345116
lon = 30.375321
api_key = '3a14cb94a140bd614abc13e0a9c9a5f2'
url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}"
response = requests.get(url)
if response.status_code == 200:
    data=response.json()
    print('Connection Successful')
else : 
    print('Connection Failed , Error code : ',response.status_code)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

data

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

json_clean_data ={

   'sky': data['weather'][0]['main'],
   'description':data['weather'][0]['description'],
   'base':data['base'],
   'feels_like':data['main']['feels_like'],
   'temp_min':data['main']['temp_min'],
   'temp_max':data['main']['temp_max'],
   'pressure':data['main']['pressure'],
   'humidity':data['main']['humidity'],
   'sea_level':data['main']['sea_level'],
   'grnd_level':data['main']['wind']['speed'],
   'wind':data['main']['sea_level'],
   'country':data['main']['sea_level'],
   'name':data['main']['name']
   
}





# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

df=pd.DataFrame(json_clean_data,index=[0])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

df.head()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

import 

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

response

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

print('changes are occured')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }
