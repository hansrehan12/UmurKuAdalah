import datetime as dt
import os

# Fungsi untuk membersihkan layar (berfungsi di sistem Windows dan Unix-like)
def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk memastikan input adalah angka dan sesuai rentang nilai
def input_angka(prompt, min_value=None, max_value=None):
    while True:
        try:
            nilai = int(input(prompt))
            if min_value is not None and nilai < min_value:
                print(f"❗ Nilai harus lebih besar atau sama dengan {min_value}.")
            elif max_value is not None and nilai > max_value:
                print(f"❗ Nilai harus lebih kecil atau sama dengan {max_value}.")
            else:
                return nilai
        except ValueError:
            print("❗ Masukkan angka yang valid.")

# Fungsi utama untuk menghitung umur
def hitung_umur():
    bersihkan_layar()  # Bersihkan layar sebelum mulai

    print("============================")
    print("     Hitung Umur Anda     ")
    print("============================\n")

    # Ambil data input dari pengguna
    nama = input("Masukkan Nama Anda: ").capitalize()
    tanggal = input_angka("Masukkan Tanggal Lahir (1-31): ", 1, 31)
    bulan = input_angka("Masukkan Bulan Lahir (1-12): ", 1, 12)
    tahun = input_angka(f"Masukkan Tahun Lahir (1900 - {dt.date.today().year}): ", 1900, dt.date.today().year)
    
    try:
        tanggal_lahir = dt.date(tahun, bulan, tanggal)
    except ValueError:
        print("❗ Tanggal tidak valid, misal bulan Februari hanya sampai 28/29.")
        return
    
    hari_ini = dt.date.today()

    # Menghitung umur
    lama_hidup = hari_ini - tanggal_lahir
    tahun_hidup = lama_hidup.days // 365
    sisa_hari = lama_hidup.days % 365
    bulan_hidup = sisa_hari // 30
    hari_hidup = sisa_hari % 30

    # Tampilkan hasil perhitungan
    print("\n========== Hasil ==========")
    print(f"👋 Halo {nama}, Anda lahir pada {tanggal_lahir:%A, %d %B %Y}")
    print(f"🗓️ Hari ini: {hari_ini:%A, %d %B %Y}")
    print(f"🎉 Usia Anda: {tahun_hidup} tahun, {bulan_hidup} bulan, dan {hari_hidup} hari")
    print("============================\n")

# Looping untuk menjalankan program secara berulang
while True:
    hitung_umur()
    print('''
    🔄 Ingin menghitung ulang?
    1. YA
    2. TIDAK
    ''')

    pilihan = input_angka("Pilih opsi (1/2): ", 1, 2)
    if pilihan == 2:
        print("\n✨ Terima kasih telah menggunakan program ini! ✨")
        break
