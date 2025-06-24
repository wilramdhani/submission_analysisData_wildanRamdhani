import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Data Loading and Preparation (with caching and error handling)


@st.cache_data
def load_data():
    try:
        hour_data = pd.read_csv('hour.csv')
        hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])
        hour_data['year'] = hour_data['dteday'].dt.year
        hour_data['month'] = hour_data['dteday'].dt.month
        hour_data['day'] = hour_data['dteday'].dt.day
        hour_data['day_of_week'] = hour_data['dteday'].dt.dayofweek
        # Keep the season column for filtering
        hour_data['season'] = hour_data['season']
        return hour_data
    except FileNotFoundError:
        st.error(
            "Error: 'data/hour.csv' not found. Make sure the file is in the 'data' folder.")
        st.stop()


hour_data = load_data()

st.title('Dashboard Analisis Bike Sharing Dataset (WILDAN RAMDHANI)')

# --- INTERACTIVE FEATURE: Date Range Filtering ---
date_range = st.date_input(
    "Pilih Rentang Tanggal:",
    # Default to the full date range
    [hour_data['dteday'].min(), hour_data['dteday'].max()]
)

# Handle the case where only one date is selected
if len(date_range) == 1:
    start_date = pd.to_datetime(date_range[0])  # Convert to datetime
    end_date = pd.to_datetime(date_range[0])  # Convert to datetime
else:
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])

filtered_data = hour_data[(hour_data['dteday'] >= start_date) & (
    hour_data['dteday'] <= end_date)]

# --- Visualizations ---

st.subheader('Jumlah Peminjaman Sepeda per Bulan')
plt.figure(figsize=(12, 6))
sns.lineplot(data=filtered_data, x='month', y='cnt', marker='o')
plt.title('Jumlah Peminjaman Sepeda per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Peminjaman')
plt.grid(True)
st.pyplot(plt)

st.subheader('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda')
plt.figure(figsize=(12, 6))
sns.boxplot(data=filtered_data, x='weathersit', y='cnt')
plt.title('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda')
plt.xlabel('Cuaca')
plt.ylabel('Jumlah Peminjaman')
plt.grid(True)
weather_map = {
    1: 'Hujan hari yang sangat berawan / hujan hari yang berawan',
    2: 'Hujan hari yang ringan / cuaca sedikit berawan',
    3: 'Cuaca yang cerah',
    4: 'Cuaca Buruk (Hujan, Es, Petir, Kabut)'
}
plt.xticks([1, 2, 3, 4], [weather_map[i] for i in [1, 2, 3, 4]])
st.pyplot(plt)

st.subheader('Pengaruh Suhu terhadap Jumlah Peminjaman Sepeda')
plt.figure(figsize=(12, 6))
sns.scatterplot(data=filtered_data, x='temp', y='cnt', alpha=0.5)
plt.title('Pengaruh Suhu terhadap Jumlah Peminjaman Sepeda')
plt.xlabel('Suhu (Normalized)')
plt.ylabel('Jumlah Peminjaman')
plt.grid(True)
st.pyplot(plt)
