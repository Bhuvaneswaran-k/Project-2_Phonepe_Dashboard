import streamlit as st
import mysql.connector
from pandas import DataFrame
import plotly.express as px


mydatabase=mysql.connector.connect(
host="localhost",
user="root",
port="3306",
password="",
)
mycursor= mydatabase.cursor(buffered=True)

st.title('Phonepe Data Analysis - Leaderboards')

col1, col2 =st.columns(2)

with col1:
    data = st.radio("Select to Explore Data",("Transcation","User"))
with col2:
    year = st.radio("Select year", (2018,2019,2020,2021) ,horizontal=True)
    quarter = st.radio("Select Quarter", (1, 2, 3, 4), horizontal=True)

if data == "Transcation":
    tab1, tab2, tab3 = st.tabs(["Pincode", "City","District"])

    with tab1:
        mycursor.execute(f"SELECT Pincode,Count,amount FROM phonepe_pulse.trans_in_pin_statewise WHERE Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out,columns=("Pincode", "Count", "Amount"))
        type = st.radio("Select Type",("PinCode Count","PinCode Amount"),horizontal=True)

        if type == "PinCode Count":
            df = df.sort_values(by=['Count'],ascending=False).head(100)
            df.reindex()
            st.dataframe(df.reset_index())
        else:
            df = df.sort_values(by=['Amount'],ascending=False).head(100)
            st.dataframe(df.reset_index())


    with tab2:
        mycursor.execute(f"SELECT City,Count,amount FROM phonepe_pulse.trans_in_city_statewise WHERE Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out, columns=("City", "Count", "Amount"))
        type = st.radio("Select Type",("City Count","City Amount"),horizontal=True)
        if type == "City Count":
            df = df.sort_values(by=['Count'],ascending=False).head(100)
            st.dataframe(df)
        else:
            df = df.sort_values(by=['Amount'],ascending=False).head(100)
            st.dataframe(df)


    with tab3:
        mycursor.execute(f"SELECT District,Count,amount FROM phonepe_pulse.trans_in_district_statewise WHERE Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out, columns=("District", "Count", "Amount"))
        type = st.radio("Select Type",("Count","Amount"),horizontal=True)
        if type == "Count":
            df = df.sort_values(by=['Count'],ascending=False).head(100)
            st.dataframe(df)
        else:
            df = df.sort_values(by=['Amount'],ascending=False).head(100)
            st.dataframe(df)

if data == "User":
    tab1, tab2, tab3 = st.tabs(["Pincode", "City","District"])

    with tab1:
        mycursor.execute(f"SELECT Pincodes,PincodeRegUser FROM phonepe_pulse.user_in_pin_statewise WHERE Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out, columns=("Pincode", "PincodeRegUser"))
        df = df.sort_values(by=['PincodeRegUser'], ascending=False)
        st.dataframe(df)


    with tab2:
        mycursor.execute(f"SELECT District,DistrictRegUser FROM phonepe_pulse.user_in_city_statewise WHERE Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out, columns=("City", "DistrictRegUser"))
        df = df.sort_values(by=['DistrictRegUser'], ascending=False)
        st.dataframe(df)

    with tab3:
        mycursor.execute(f"SELECT City,RegUser,AppOpens FROM phonepe_pulse.user_in_district_statewise WHERE Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out, columns=("District", "RegUser", "AppOpens"))
        type = st.radio("Select Type", ("Reg User", "App Opens"), horizontal=True)
        if type == "Reg User":
            df = df.sort_values(by=['RegUser'], ascending=False).head(100)
            st.dataframe(df)
        else:
            df = df.sort_values(by=['AppOpens'], ascending=False).head(100)
            st.dataframe(df)