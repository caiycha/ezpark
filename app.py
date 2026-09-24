import streamlit as st

# Judul dan Deskripsi Aplikasi
st.title("⚡ EZPark: Smart Parking Calculator")
st.write("Sering bingung berapa total biaya parkir? EZPark menghitung tarif parkir kamu secara presisi, otomatis, dan transparan!")

# Input angka jam parkir dari pengguna
jam_parkir = st.number_input("Masukkan lama parkir (jam):", min_value=1, value=1, step=1)

# Logika Perhitungan Tarif Parkir
if jam_parkir <= 1:
    total_biaya = 5000
    rincian = "Tarif Dasar (1 Jam Pertama): Rp 5.000"
else:
    biaya_dasar = 5000
    biaya_tambahan = (jam_parkir - 1) * 3000
    total_biaya = biaya_dasar + biaya_tambahan
    rincian = f"1 Jam Pertama: Rp 5.000 | Tambahan {jam_parkir - 1} Jam: Rp {biaya_tambahan:,}"

# Cek Diskon jika parkir > 5 jam
ada_diskon = False
if jam_parkir > 5:
    total_biaya -= 2000
    ada_diskon = True

# Tombol Eksekusi
if st.button("Hitung Biaya Parkir"):
    st.info(f"📌 **Rincian:** {rincian}")
    
    if ada_diskon:
        st.success("🎉 **Selamat! Kamu mendapatkan Diskon Parkir Lama (> 5 Jam) sebesar Rp 2.000!**")
    
    st.markdown(f"### 💰 **Total Biaya Parkir Akhir: Rp {total_biaya:,}**")
