import re
import random
import string

def buatUsername(email):
    # Membuat username dari alamat email
    username = email.split("@")[0]
    return username
def buatPassword():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(8))
    return password
def prosesData (data):
    # Mengambil Email dari Data
    alamatEmail = re.findall("\S+@\S+", data)
    for i in alamatEmail:
        username = buatUsername(i)
        password = buatPassword()
        print(f"{i} username: {username}, password: {password}")

data = "anton@mail.com dimiliki oleh antonius\nbudi@gmail.co.id dimiliki oleh budi anwari\nslamet@getnada.com dimiliki oleh slamet slumut\nmatahari@tokopedia.com dimiliki oleh toko matahari"

prosesData(data)


