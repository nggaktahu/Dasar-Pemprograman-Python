def menu():
    print("==========================================================================")
    print("                            Brienna Beautys                               ")
    print("==========================================================================")
    print("--------------------------------------------------------------------------")
    print("kode Barang | Nama Barang                          | Harga")
    print("--------------------------------------------------------------------------")
    print("  A         | brienna collagen drink               | Rp. 200.000")
    print("  B         | brienna glow skin                    | Rp. 150.000")
    print("  C         | paket brienna body lightening        | Rp. 200.000")
    print("  D         | brienna slim boost                   | Rp. 300.000")
    print("  E         | brienna watermelon lip scrub         | Rp. 50.000")
    print("  F         | brienna lip serum                    | Rp. 70.000")
    print("  G         | brienna eyelash & eyebrow serum      | Rp. 105.000")
    print("  H         | brienna acne fight serum             | Rp. 160.000")
    print("  I         | brienna bright & glow serum          | Rp. 150.000")
    print("  J         | brienna glow mask greentea latte     | Rp. 50.000")
    print("  K         | brienna glow mask lovable cappuchino | Rp. 50.000")
    print("  L         | brienna juicy water tint             | RP. 80.000")
    print("  M         | brienna magic lip gloss              | Rp. 100.000 ")
    print("  N         | brienna brightening moisturizer      | Rp. 130.000")
    print("  O         | brienna acne solution moisturizer    | Rp. 140.000")
    print("  P         | brienna perfect sunscreen spf 50PA++ | Rp. 110.000")
    print("  Q         | brienna refreshing & hydrating toner | Rp. 60.000")
    print("  R         | brienna body spray 3 in 1            | Rp. 50.000")
    print("===========================================================================")
menu()
nama = input("Masukan Nama Pembeli : ")
tanggal = input("Tanggal Pembelian : ")
def garis():
    print("===========================================================================")
garis()
jumlah_beli = int(input("Masukan Jumlah transaksi : "))
kode_barang=[]
nama_barang=[]
masukan_jumlah=[]
total_belanja=[]
uang_bayar=[]
uang_kembali=[]
harga=[]
jumlah=[]
i = 0
while i<jumlah_beli:
    print("Data ke -",i+1)
    kode_barang.append(input("Masukan Kode Barang :"))
    masukan_jumlah.append(int(input("Masukan Jumlah Beli :")))
    if kode_barang[i] == "A":
        nama_barang.append("brienna collagen drink")
        harga.append("Rp. 200.000")
        jumlah.append(masukan_jumlah[i]*int(200000))
    elif kode_barang[i] == "B":
        nama_barang.append("brienna glow skin")
        harga.append("Rp. 150.000")
        jumlah.append(masukan_jumlah[i]*int(150000))
    elif kode_barang[i] == "C":
        nama_barang.append("paket brienna body lightening")
        harga.append("Rp. 200.000")
        jumlah.append(masukan_jumlah[i]*int(200000))
    elif kode_barang[i] == "D":
        nama_barang.append("brienna slim boost")
        harga.append("Rp. 300.000")
        jumlah.append(masukan_jumlah[i]*int(300000))
    elif kode_barang[i] == "E":
        nama_barang.append("brienna watermelon lip scrub")
        harga.append("Rp. 50.000")
        jumlah.append(masukan_jumlah[i]*int(50000))
    elif kode_barang[i] == "F":
        nama_barang.append("brienna lip serum")
        harga.append(" Rp. 70.000")
        jumlah.append(masukan_jumlah[i]*int(70000))
    elif kode_barang[i] == "G":
        nama_barang.append("brienna eyelash & eyebrow serum")
        harga.append("Rp. 105.000")
        jumlah.append(masukan_jumlah[i]*int(105000))
    elif kode_barang[i] == "H":
        nama_barang.append("brienna acne fight serum")
        harga.append("Rp. 160.000")
        jumlah.append(masukan_jumlah[i]*int(160000))
    elif kode_barang[i] == "I":
        nama_barang.append("brienna bright & glow serum")
        harga.append("Rp. 150.000")
        jumlah.append(masukan_jumlah[i]*int(150000))
    elif kode_barang[i] == "J":
        nama_barang.append("brienna glow mask greentea latte")
        harga.append("Rp. 50.000")
        jumlah.append(masukan_jumlah[i]*int(50000))
    elif kode_barang[i] == "K":
        nama_barang.append("brienna glow mask lovable cappuchino")
        harga.append("Rp. 50.000")
        jumlah.append(masukan_jumlah[i]*int(50000))
    elif kode_barang[i] == "L":
        nama_barang.append("brienna juicy water tint")
        harga.append("Rp. 80.000")
        jumlah.append(masukan_jumlah[i]*int(80000))
    elif kode_barang[i] == "M":
        nama_barang.append("brienna magic lip gloss")
        harga.append("Rp. 100.000")
        jumlah.append(masukan_jumlah[i]*int(100000))
    elif kode_barang[i] == "N":
        nama_barang.append("brienna brightening moisturizer")
        harga.append("Rp. 130.000")
        jumlah.append(masukan_jumlah[i]*int(130000))
    elif kode_barang[i] == "O":
        nama_barang.append("brienna acne solution moisturizer")
        harga.append("Rp. 140.000")
        jumlah.append(masukan_jumlah[i]*int(140000))
    elif kode_barang[i] == "P":
        nama_barang.append("brienna perfect sunscreen spf 50PA++")
        harga.append(" Rp. 110.000")
        jumlah.append(masukan_jumlah[i]*int(110000))
    elif kode_barang[i] == "Q":
        nama_barang.append("brienna refreshing & hydrating toner")
        harga.append("Rp. 60.000")
        jumlah.append(masukan_jumlah[i]*int(60000))
    elif kode_barang[i] == "R":
        nama_barang.append("brienna body spray")
        harga.append("Rp. 50.000")
        jumlah.append(masukan_jumlah[i]*int(50000))
    else :
        nama_barang.append("Kode Salah")
        harga.append("0")
        jumlah.append(masukan_jumlah[i]*int("0"))
    i = i+1
garis ()
print("=============================STRUK PEMBELI=================================")
print("===========================================================================")
print("Nama :", nama)
print("Tanggal :", tanggal)
def menu():
    print("---------------------------------------------------------------------------")
    print("No | Nama Barang                          | Harga       | Qty | Subtotal   ")         
    print("---------------------------------------------------------------------------")
menu()
total_belanja=0
a = 0
while a<jumlah_beli:
    total_belanja = total_belanja + jumlah[a]
    print ("%i  | %s\t\t         | %s  | %i   | Rp. %i " %(a+1, nama_barang[a], harga[a], masukan_jumlah[a], jumlah[a]))
    a = a+1
garis()
print("            Total belanjaan Rp.",total_belanja)
bayar = int(input("Masukan Uang Bayar Rp."))
uang_kembali = bayar-total_belanja
print("            Uang Kembali Rp.", uang_kembali)
garis()
print("================================TERIMAKSIH:)===============================")
print("===========================================================================")