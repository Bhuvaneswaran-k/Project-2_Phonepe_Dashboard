# Project-2_Phonepe_Dashboard

Introduction
This project transforms the data from the input JSON files into tabular form for more effective analysis. The project processes the input files using Python's modules such as glob, pandas, re,streamlit and plotly and then stores the altered data in a database using SQLAlchemy.

# Prerequisites
Before you begin, make sure you have the following components installed in your system:  

1. Python 3   
2. Pandas   
3. Re    
4. SQLAlchemy   
5. PyMySQL   
6. Glob  
7. streamlit  
8. plotly

## uses:
glob for reading multiple files in a directory  
pandas for data manipulation  
re for regular expression operations   
sqlalchemy for database connectivity  

Make sure your system has the necessary components installed before you start:
                                  pip install jupyter_dash 
                                  pip install dash_bootstrap_components
                                  pip install pandas
                                  pip install ploty
                                  pip install streamlit
                                  pip install sqlalchemy
                                  
# importation Part:   

                                  import glob 
                                  import pandas as pd
                                  import re
                                  from sqlalchemy import create_engine
                                  import streamlit as st
                                  import plotly.express as px
                                  import dash_bootstrap_components as dbc
                                  import plotly.graph_objects as go
                                  from plotly.subplots import make_subplots
The project consists of a number of functions that alter the JSON input files in various ways. These include the following:
## Glob

Using the glob library, the function aggtransyear() reads in the JSON files and extracts the pertinent data. The method concatenates all the data into a single DataFrame object called agg_yr.

## aggtransstate()  
Gets the state information from the file name and adds it as a column to the DataFrame object agg state in addition to performing a transformation similar to aggTransyear().

## agguseryear()   
This function constructs a DataFrame object called user data year that contains the information that was extracted from the input JSON files about the users.

In addition to performing a transformation identical to that of the agguseryear() method, the agguserstate() function also extracts the state information from the file name and adds it as a column to the DataFrame object user state.

## mapyear()
This function generates a DataFrame object called map data year that contains the mapping information that was taken from the input JSON files.

## Sqlalchemy
A SQLAlchemy engine is created at the beginning of the code to connect to a MySQL database with the specified parameters. The username is "root" and the password is empty. The database name is "phonepe"
## Plotly
plotly.py, colloquially referred to as Plotly, is an interactive, open-source, and browser-based graphing library.The main plus point of plotly is its interactive nature and of course visual quality. Plotly is in great demand rather than other libraries like Matplotlib and Seaborn. Plotly provides a list of charts having animations in 1D, 2D, and 3D too for more details of charts check

# Conclusion
With the help of this project, you can easily convert JSON data into tabular form for analysis. The above-mentioned libraries make the process of data transformation easier and more effective. For further study, the converted data may then be quickly recorded in a database and by the help of streamlit and plotly we can explore varoius graph which helps in analysis
