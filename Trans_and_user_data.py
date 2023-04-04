import streamlit as st
import mysql.connector
from pandas import DataFrame
import plotly.express as px
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  port="3306",
  database="phonepe_pulse"
)

# Creating a cursor object
mycursor = mydb.cursor()

st.title('Phonepe Data Analysis - India')

col1, col2 =st.columns(2)

with col1:
    data = st.radio("Select to Explore Data",("Transcation","User"))
with col2:
    year = st.radio("Select year", (2018,2019,2020,2021) ,horizontal=True)
    quarter = st.radio("Select Quarter", (1, 2, 3, 4), horizontal=True)

if data == "Transcation":

    mycursor.execute(f"SELECT count,amount,name,Year,State,Quater FROM phonepe_pulse.payments_type_statewise WHERE Year = {year} and Quater = {quarter}")
    out = mycursor.fetchall()
    df = DataFrame(out,columns=("Count","Amount","Name","Year","State","Quater"))
    df["State"] = df["State"].str.title()
    df["State"] = df["State"].str.replace("-", " ")

    tab1, tab2, tab3, tab4, tab5, tab6= st.tabs(["Total","Peer to Peer","Recharge & bill","Merchant payments","Financial Services","Others"])


    with tab1:
        tab1.subheader("Total Transcation Done in India By State")

        map = pd.pivot_table(df, index=["State"], values=["Amount", "Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Amount',
            hover_data=["Amount","Count"],
            color_continuous_scale=px.colors.sequential.Plasma
        )

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)


    with tab2:
        tab2.subheader("Peer to Peer Transcation By state")

        mycursor.execute(f"SELECT count,amount,name,Year,State,Quater FROM phonepe_pulse.payments_type_statewise WHERE name = 'Peer-to-peer payments' and Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out,columns=("Count","Amount","Name","Year","State","Quater"))
        df["State"] = df["State"].str.title()
        df["State"] = df["State"].str.replace("-", " ")

        map = pd.pivot_table(df, index=["State"], values=["Amount", "Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Amount',
            color_continuous_scale='reds'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        tab3.subheader("Recharge & bill payments By state")

        mycursor.execute(f"SELECT count,amount,name,Year,State,Quater FROM phonepe_pulse.payments_type_statewise WHERE name = 'Recharge & bill payments' and Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out,columns=("Count","Amount","Name","Year","State","Quater"))
        df["State"] = df["State"].str.title()
        df["State"] = df["State"].str.replace("-", " ")

        map = pd.pivot_table(df, index=["State"], values=["Amount", "Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Amount',
            color_continuous_scale='reds'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)


    with tab4:
        tab4.subheader("Merchant payments By state")

        mycursor.execute(f"SELECT count,amount,name,Year,State,Quater FROM phonepe_pulse.payments_type_statewise WHERE name = 'Merchant payments' and Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out,columns=("Count","Amount","Name","Year","State","Quater"))
        df["State"] = df["State"].str.title()
        df["State"] = df["State"].str.replace("-", " ")

        map = pd.pivot_table(df, index=["State"], values=["Amount", "Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Amount',
            color_continuous_scale='reds'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)


    with tab5:
        tab5.subheader("Financial Services")
        mycursor.execute(f"SELECT count,amount,name,Year,State,Quater FROM phonepe_pulse.payments_type_statewise WHERE name = 'Financial Services' and Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out,columns=("Count","Amount","Name","Year","State","Quater"))
        df["State"] = df["State"].str.title()
        df["State"] = df["State"].str.replace("-", " ")

        map = pd.pivot_table(df, index=["State"], values=["Amount", "Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Amount',
            color_continuous_scale='reds'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)

    with tab6:
        tab6.subheader("Others By state")

        mycursor.execute(f"SELECT count,amount,name,Year,State,Quater FROM phonepe_pulse.payments_type_statewise WHERE name = 'Others' and Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out,columns=("Count","Amount","Name","Year","State","Quater"))
        df["State"] = df["State"].str.title()
        df["State"] = df["State"].str.replace("-", " ")

        map = pd.pivot_table(df, index=["State"], values=["Amount", "Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Amount',
            color_continuous_scale='reds'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)

elif data == "User":

    mycursor.execute(f"SELECT count,brand,Year,State,Quater FROM phonepe_pulse.users_by_device_statewise WHERE Year = {year} and Quater = {quarter}")
    out = mycursor.fetchall()
    df = DataFrame(out,columns=("Count","Brand","Year","State","Quater"))
    df["State"] = df["State"].str.title()
    df["State"] = df["State"].str.replace("-", " ")

    tab1, tab2, tab3, tab4, tab5, tab6,tab7, tab8, tab9, tab10, tab11,tab12 = st.tabs(["Total","Xiaomi","Samsung","Vivo","Oppo","OnePlus","Realme","Apple","Motorola","Lenovo","Huawei","Others"])

    with tab1:
        tab1.subheader("Total Users in India By State")

        map = pd.pivot_table(df, index=["State"], values=["Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Count',
            hover_data=["Count"],
            color_continuous_scale=px.colors.sequential.Plasma
        )

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True  )

    with tab2:
        tab2.subheader("Xiaomi Users By state")

        mycursor.execute(f"SELECT count,brand,Year,State,Quater FROM phonepe_pulse.users_by_device_statewise WHERE brand = 'Xiaomi' and Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out,columns=("Count","brand","Year","State","Quater"))
        df["State"] = df["State"].str.title()
        df["State"] = df["State"].str.replace("-", " ")

        map = pd.pivot_table(df, index=["State"], values=["Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Count',
            color_continuous_scale='reds'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)


    with tab3:
        tab3.subheader("Samsung Users By state")

        mycursor.execute(f"SELECT count,brand,Year,State,Quater FROM phonepe_pulse.users_by_device_statewise WHERE brand = 'Samsung' and Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out,columns=("Count","brand","Year","State","Quater"))
        df["State"] = df["State"].str.title()
        df["State"] = df["State"].str.replace("-", " ")

        map = pd.pivot_table(df, index=["State"], values=["Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Count',
            color_continuous_scale='reds'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)

    with tab4:
        tab4.subheader("Vivo Users By state")

        mycursor.execute(f"SELECT count,brand,Year,State,Quater FROM phonepe_pulse.users_by_device_statewise WHERE brand = 'Vivo' and Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out,columns=("Count","brand","Year","State","Quater"))
        df["State"] = df["State"].str.title()
        df["State"] = df["State"].str.replace("-", " ")

        map = pd.pivot_table(df, index=["State"], values=["Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Count',
            color_continuous_scale='reds'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)

    with tab5:
        tab5.subheader("Oppo Users By state")

        mycursor.execute(f"SELECT count,brand,Year,State,Quater FROM phonepe_pulse.users_by_device_statewise WHERE brand = 'Oppo' and Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out,columns=("Count","brand","Year","State","Quater"))
        df["State"] = df["State"].str.title()
        df["State"] = df["State"].str.replace("-", " ")

        map = pd.pivot_table(df, index=["State"], values=["Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Count',
            color_continuous_scale='reds'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)

    with tab6:
        tab6.subheader("OnePlus Users By state")

        mycursor.execute(f"SELECT count,brand,Year,State,Quater FROM phonepe_pulse.users_by_device_statewise WHERE brand = 'OnePlus' and Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out,columns=("Count","brand","Year","State","Quater"))
        df["State"] = df["State"].str.title()
        df["State"] = df["State"].str.replace("-", " ")

        map = pd.pivot_table(df, index=["State"], values=["Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Count',
            color_continuous_scale='reds'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)

    with tab7:
        tab7.subheader("Realme Users By state")

        mycursor.execute(f"SELECT count,brand,Year,State,Quater FROM phonepe_pulse.users_by_device_statewise WHERE brand = 'Realme' and Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out,columns=("Count","brand","Year","State","Quater"))
        df["State"] = df["State"].str.title()
        df["State"] = df["State"].str.replace("-", " ")

        map = pd.pivot_table(df, index=["State"], values=["Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Count',
            color_continuous_scale='reds'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)

    with tab8:
        tab8.subheader("Apple Users By state")

        mycursor.execute(f"SELECT count,brand,Year,State,Quater FROM phonepe_pulse.users_by_device_statewise WHERE brand = 'Apple' and Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out,columns=("Count","brand","Year","State","Quater"))
        df["State"] = df["State"].str.title()
        df["State"] = df["State"].str.replace("-", " ")

        map = pd.pivot_table(df, index=["State"], values=["Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Count',
            color_continuous_scale='reds'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)


    with tab9:
        tab9.subheader("Motorola Users By state")

        mycursor.execute(f"SELECT count,brand,Year,State,Quater FROM phonepe_pulse.users_by_device_statewise WHERE brand = 'Motorola' and Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out,columns=("Count","brand","Year","State","Quater"))
        df["State"] = df["State"].str.title()
        df["State"] = df["State"].str.replace("-", " ")

        map = pd.pivot_table(df, index=["State"], values=["Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Count',
            color_continuous_scale='reds'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)

    with tab10:
        tab10.subheader("Lenovo Users By state")

        mycursor.execute(f"SELECT count,brand,Year,State,Quater FROM phonepe_pulse.users_by_device_statewise WHERE brand = 'Lenovo' and Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out,columns=("Count","brand","Year","State","Quater"))
        df["State"] = df["State"].str.title()
        df["State"] = df["State"].str.replace("-", " ")

        map = pd.pivot_table(df, index=["State"], values=["Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Count',
            color_continuous_scale='reds'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)

    with tab11:
        tab11.subheader("Huawei Users By state")

        mycursor.execute(f"SELECT count,brand,Year,State,Quater FROM phonepe_pulse.users_by_device_statewise WHERE brand = 'Huawei' and Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out,columns=("Count","brand","Year","State","Quater"))
        df["State"] = df["State"].str.title()
        df["State"] = df["State"].str.replace("-", " ")

        map = pd.pivot_table(df, index=["State"], values=["Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Count',
            color_continuous_scale='reds'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)

    with tab12:
        tab12.subheader("Others Users By state")

        mycursor.execute(f"SELECT count,brand,Year,State,Quater FROM phonepe_pulse.users_by_device_statewise WHERE brand = 'Others' and Year = {year} and Quater = {quarter}")
        out = mycursor.fetchall()
        df = DataFrame(out,columns=("Count","brand","Year","State","Quater"))
        df["State"] = df["State"].str.title()
        df["State"] = df["State"].str.replace("-", " ")

        map = pd.pivot_table(df, index=["State"], values=["Count"], aggfunc="sum")
        map = map.reset_index()

        fig = px.choropleth(
            map,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Count',
            color_continuous_scale='reds'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)