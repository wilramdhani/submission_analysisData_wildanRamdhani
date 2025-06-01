
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

hour_data = pd.read_csv('data/hour.csv')

hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])

hour_data['year'] = hour_data['dteday'].dt.year
hour_data['month'] = hour_data['dteday'].dt.month
hour_data['day'] = hour_data['dteday'].dt.day
hour_data['day_of_week'] = hour_data['dteday'].dt.dayofweek

st.title('Dashboard Analisis Bike Sharing Dataset (WILDAN RAMDHANI)')

st.subheader('Jumlah Peminjaman Sepeda per Bulan (2012)')
plt.figure(figsize=(12, 6))
sns.lineplot(data=hour_data[hour_data['year'] ==
             2012], x='month', y='cnt', marker='o')
plt.title('Jumlah Peminjaman Sepeda per Bulan (2012)')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Peminjaman')
plt.grid(True)
st.pyplot(plt)

st.subheader('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda')
plt.figure(figsize=(12, 6))
sns.boxplot(data=hour_data, x='weathersit', y='cnt')
plt.title('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda')
plt.xlabel('Cuaca')
plt.ylabel('Jumlah Peminjaman')
plt.grid(True)
plt.xticks([1, 2, 3, 4], ['Hujan hari yang sangat berawan / hujan hari yang berawan',
           'Hujan hari yang ringan / cuaca sedikit berawan', 'Cuaca yang cerah', 'Cuaca Buruk (Hujan, Es, Petir, Kabut)'])
st.pyplot(plt)

st.subheader('Pengaruh Suhu terhadap Jumlah Peminjaman Sepeda')
plt.figure(figsize=(12, 6))
sns.scatterplot(data=hour_data, x='temp', y='cnt', alpha=0.5)
plt.title('Pengaruh Suhu terhadap Jumlah Peminjaman Sepeda')
plt.xlabel('Suhu (Normalized)')
plt.ylabel('Jumlah Peminjaman')
plt.grid(True)
st.pyplot(plt)
