import datetime as dt

def hidup() :

    print("===================")
    print("Menghitung Berapa Umur Anda Sekarang")
    
    nama = str(input("Masukan Nama Anda : "))
    tanggal = int(input("Masukan Tanggal Lahir : "))
    bulan = int(input("Masukan Bulan Lahir : "))
    tahun = int(input("Masukan Tahun Lahir : "))
    tanggal_lahir = dt.date(tahun, bulan, tanggal)

    print("==========Hasil=========")
    print(f"Halo {nama}")
    print(f"Anda Lahir Pada : {tanggal_lahir}")
    hari_ini = dt.date.today()

    lama_hidup = hari_ini - tanggal_lahir

    tahun_lahir = lama_hidup.days // 365
    bulan_lahir = (lama_hidup.days % 365) // 30

    print(f"Anda lahir pada hari : {tanggal_lahir:%A}")
    print(f"Anda telah hidup selama : {lama_hidup}, {bulan_lahir} bulan")
    print(f"Usia Anda : {tahun_lahir} tahun")

while True:
    hidup()
    print('''
    Ingin mengulanginya? :
    1. YA
    2. Tidak
    ''')

    data = int(input("Ingin mengulanginya? 1/2 : "))
    if data > 1:
        print("Terimakasih")
        break
