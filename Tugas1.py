# Alpro_Pizza
# PizzStAR kel 9
# Tugas 1 alpro
# anggota kelompok:
# 1. RISQON ABDY PRATAMA (24091397115)
# 2. ANATOLY AQUILA KATIMIN (24091397125)
# 3. MUHAMMAD MUSONNIF AMINUDDIN (24091397135)

# selamat datang di PizzStAR/greeting
def intro():
    print("============================")
    print("Selamat Datang di PizzStAR!")
    print("============================")
intro()

# apa mau buat pesanan?
def user_order():
    print("Buat pesanan")
    order = input("Apakah Anda ingin membuat pesanan baru? (ya/tidak): ")
    if order.lower() == "ya" :
        print("Silahkan lanjutkan pesanan Anda")
    elif order.lower() == "tidak" :
        print("Semoga Hari Anda Menyenangkan!")
        print("Terimakasih Telah Berkunjung")
        # order berakhir
        # mengembalikan ke menu awal untuk order baru
        intro()
        user_order()  
    else:
        print("Tolong masukkan ya/tidak :)")
        return user_order()   # mengembalikan ke menu pilh opsi buat pesanan karena input tak sesuai
    print("============================")
user_order()

# pesanan baru
def buyer_name():
    print("Pesanan Baru")
    name = input("Pesanan atas nama: ")
    print("============================")
    return name
name = buyer_name()

# dine in atau dine out
def serving_method ():
    print("Penyajian Pesanan Anda")
    method = input ("Pilih cara penyajian pesanan Anda (dine in / takeaway): ")
    
    # memvalidasi input
    if method.lower() == "dine in":
        method = "Dine In"
        print("Silahkan lanjutkan pesanan Anda")
        print("============================")    
        return method
    elif method.lower() == "takeaway":
        method = "Takeaway"
        print("Silahkan lanjutkan pesanan Anda")
        print("============================")
        return method
    else:
        print("Tolong masukkan sesuai opsi :)")
        print("============================")
        return serving_method ()    # mengembalikan ke menu pilh opsi metode penyajian karena input tak sesuai
method = serving_method()

# daftar menu dan harga 
def menu_list():
    print("Daftar Menu")
    print("===Ukuran===")
    print("1. Small: 50000")
    print("2. Medium: 75000")
    print("3. Large: 100000")
    print("===Topping===")
    print("1. Frankfurter: 15000")
    print("2. Meat Monsta: 20000")
    print("3. Super Supreme Chicken: 25000")
    print("4. Cheeseburger: 22000")
    print("===Crust===")
    print("1. Thin Crust: 6000")
    print("2. Thick Crust: 6000")
    print("3. Cheese Crust: 10000")
    print("============================")
menu_list()

# mendeklarasikan harga tiap elemen
pizza_price = {"Small": 50000, "Medium": 75000, "Large": 100000}
topping_price = {'Frankfurter': 15000, 'Meat Monsta': 20000, 'Super Supreme Chicken': 25000, 'Cheeseburger': 22000}
cheese_price = 13000
crust_price = {"Thin": 6000, "Thick": 6000, "Cheese": 10000}

# Input dari pengguna untuk ukuran
def size_option():
    print("Pilih ukuran pizza: ")
    print("1. Small (S)")
    print("2. Medium (M)")
    print("3. Large (L)")
    # input dari pengguna di opsi size
    size_choice = (input("Masukkan kode ukuran yang dipilih (S/M/L): "))
    # memvalidasi input
    if size_choice.upper() == "S" :
        size = "Small"
        print("Silahkan lanjutkan pesanan Anda")
        print("============================")    
        return size
    elif size_choice.upper() == "M" :
        size = "Medium"
        print("Silahkan lanjutkan pesanan Anda")
        print("============================")
        return size
    elif size_choice.upper() == "L" :
        size = "Large"
        print("Silahkan lanjutkan pesanan Anda")
        print("============================")
        return size
    else:
        print("Tolong masukkan sesuai opsi :)")
        print("============================")
        return size_option()   # mengembalikan ke menu pilh opsi ukuran karena input tak sesuai
size = size_option()

# Input dari pengguna untuk topping
def topping_option():
    print("Pilih topping pizza: ")
    print("1. Frankfurter (F)")
    print("2. Meat Monsta (M)")
    print("3. Super Supreme Chicken (S)")
    print("4. Cheeseburger (C)")
    # input dari pengguna di opsi topping
    topping_choice = (input("Masukkan kode topping yang dipilih (F/M/S/C): "))
    # memvalidasi input
    if topping_choice.upper() == "F" :
        topping = "Frankfurter"
        print("Silahkan lanjutkan pesanan Anda")
        print("============================")    
        return topping
    elif topping_choice.upper() == "M" :
        topping = "Meat Monsta"
        print("Silahkan lanjutkan pesanan Anda")
        print("============================")
        return topping
    elif topping_choice.upper() == "S" :
        topping = "Super Supreme Chicken"
        print("Silahkan lanjutkan pesanan Anda")
        print("============================")
        return topping
    elif topping_choice.upper() == "C" :
        topping = "Cheeseburger"
        print("Silahkan lanjutkan pesanan Anda")
        print("============================")
        return topping
    else:
        print("Tolong masukkan sesuai opsi :)")
        print("============================")
        return topping_option()
topping = topping_option()

# Input dari pengguna untuk crust
def crust_option():
    print("Pilih crust pizza: ")
    print("(a) Thin")
    print("(b) Thick")
    print("(c) Cheese")
    # input dari pengguna di opsi crust
    crust_choice = (input("Masukkan kode crust yang dipilih (a/b/c): "))
    # memvalidasi input
    if crust_choice.lower() == "a" :
        crust = "Thin"
        print("Silahkan lanjutkan pesanan Anda")
        print("============================")    
        return crust
    elif crust_choice.lower() == "b" :
        crust = "Thick"
        print("Silahkan lanjutkan pesanan Anda")
        print("============================")
        return crust
    elif crust_choice.lower() == "c" :
        crust = "Cheese"
        print("Silahkan lanjutkan pesanan Anda")
        print("============================")
        return crust
    else:
        print("Tolong masukkan sesuai opsi :)")
        print("============================")
        return crust_option()     # mengembalikan ke menu pilh opsi crust karena input tak sesuai
crust = crust_option()

# Opsi tambahan keju
def cheese_option():
    print("Apakah ingin tambahan keju?")
    addons_cheese = input("Rp 13000 (ya/tidak): ")
    # memvalidasi opsi keju tambahan
    if addons_cheese.lower() == "ya" :
        cheese = "ya"
        print("Silahkan lanjutkan pesanan Anda")
        print("============================")    
        return cheese
    elif addons_cheese.lower() == "b" :
        cheese = "tidak"
        print("Silahkan lanjutkan pesanan Anda")
        print("============================")
        return cheese
cheese = cheese_option()

# Hitung total harga
def bill():
    if topping and size and crust:
        total_price = pizza_price[size] + topping_price[topping] + crust_price[crust]
        if cheese == "ya":
            total_price += cheese_price
    # Tampilkan pesanan dan total harga
    print("===PizzStAR===\n")
    print(f"Pesanan atas nama: {name}")
    print(f"Penyajian: {method}")
    print(f"Pesanan Anda: Pizza {size} dengan topping {topping} dengan crust {crust}")
    if cheese == "ya":
        print("Tambahan: Extra Cheese")
        print(f"Total Harga: Rp{total_price}") 
        print("============================") 
        # Tambahkan pesan terima kasih
        print("\nTerimakasih telah berbelanja di Toko Pizza kami!")
    else:
        print("\nPesanan Anda tidak valid, silakan coba lagi.")  
total = bill()
