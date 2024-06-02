# PROGRAM MENGECEK SELISIH HARI
from datetime import datetime
import re 

def selisihTanggal(info):
    tanggalDataFind = re.findall("\d{4}-\d{2}-\d{2}", data)
    tanggalSekarang = datetime.now()
    formatTanggal = tanggalSekarang.strftime("%Y-%m-%d")
    for i in tanggalDataFind:
        tanggalData = datetime.strptime(i, "%Y-%m-%d")
        selisih = tanggalSekarang - tanggalData
        print(i, "00:00:00", "selisih", selisih.days, "hari")  
       
data = "Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)"

selisihTanggal(data)



