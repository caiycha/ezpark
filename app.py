import streamlit as st

# Judul dan Deskripsi Aplikasi
st.title("⚡ EZPark: Smart Parking Calculator")
st.write("Sering bingung berapa total biaya parkir? EZPark menghitung tarif parkir kamu secara presisi, otomatis, dan transparan!")

# Input angka jam parkir dari pengguna
jam_parkir = st.number_input("Masukkan lama parkir (jam):", min_value=1, value=1, step=1)

# Logika Perhitungan Tarif Parkir
if jam_parkir <= 1:
    total_biaya = 5000
else:
    total_biaya = 5000 + (jam_parkir - 1) * 3000

# Pengaplikasian Diskon jika parkir > 5 jam
if jam_parkir > 5:
    total_biaya -= 2000

# Tombol Eksekusi
if st.button("Hitung Biaya Parkir"):
    st.success(f"Total Biaya Parkir Akhir: Rp {total_biaya:,}")
