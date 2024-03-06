import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned datasets
hour_data = pd.read_csv('cleaned_hour_data.csv')
day_data = pd.read_csv('cleaned_day_data.csv')

# Set page title
st.title('Proyek Analisis Data: Bike Data Sharing')

# Sidebar
st.sidebar.header('Menu')
selected_analysis = st.sidebar.selectbox('Pilih Analisis Data:', ('Tren Penggunaan Sepeda Selama Musim', 'Perbedaan Penggunaan Sepeda antara Hari Kerja dan Akhir Pekan', 'Pengaruh Kondisi Cuaca terhadap Penggunaan Sepeda', 'Korelasi antara Suhu dan Jumlah Pengguna Sepeda'))

# Main content based on selected analysis
if selected_analysis == 'Tren Penggunaan Sepeda Selama Musim':
    st.header('Tren Penggunaan Sepeda Selama Musim-Musim Tertentu')
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='dteday', y='cnt', hue='season', data=hour_data, palette='viridis')
    plt.title('Tren Penggunaan Sepeda Selama Musim-Musim Tertentu')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(plt)

elif selected_analysis == 'Perbedaan Penggunaan Sepeda antara Hari Kerja dan Akhir Pekan':
    st.header('Perbedaan Penggunaan Sepeda antara Hari Kerja dan Akhir Pekan')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weekday', y='cnt', data=day_data, palette='Set2')
    plt.title('Perbedaan Penggunaan Sepeda antara Hari Kerja dan Akhir Pekan')
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Jumlah Pengguna Sepeda')
    plt.xticks(ticks=range(0, 7), labels=['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'])
    st.pyplot(plt)

elif selected_analysis == 'Pengaruh Kondisi Cuaca terhadap Penggunaan Sepeda':
    st.header('Pengaruh Kondisi Cuaca terhadap Penggunaan Sepeda')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=hour_data, palette='coolwarm')
    plt.title('Distribusi Pengguna Sepeda Berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(plt)

elif selected_analysis == 'Korelasi antara Suhu dan Jumlah Pengguna Sepeda':
    st.header('Korelasi antara Suhu dan Jumlah Pengguna Sepeda')
    correlation_temp_cnt = hour_data['temp'].corr(hour_data['cnt'])
    st.write(f"Korelasi antara Suhu dan Jumlah Pengguna Sepeda: {correlation_temp_cnt}")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', data=hour_data, color='coral')
    plt.title('Korelasi antara Suhu dan Jumlah Pengguna Sepeda')
    plt.xlabel('Suhu (Normalized)')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(plt)
