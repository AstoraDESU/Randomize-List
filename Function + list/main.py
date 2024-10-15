import random

#Isi list default
list1 = [1, 2, 3, 4]
list2 = ["A", "B", "C", "D"]
list3 = ["Kopi", 1, "Beruang", 6, True, False]

#Untuk merandomize list dan memberikan syarat JACKPOT
def kotak_random(list1, list2, list3):
    item1 = random.choice(list1)
    item2 = random.choice(list2)
    item3 = random.choice(list3)
    if item1 == 1 and item2 == "C" and item3 == "Kopi":
        print(f"Hasil list = {item1}, {item2}, {item3} - JACKPOT!")
    else:
        print(f"Hasil list = {item1}, {item2}, {item3}")

#Function buat nambah isi list dari input
def tambah_list():
    jawab1 = input("Apakah Anda ingin memasukkan nilai ke list pertama? (y/n): ").lower()
    if jawab1 == 'y':
        nama1 = input("Masukkan nilai untuk list pertama: ")
        list1.append(nama1)

    jawab2 = input("Apakah Anda ingin memasukkan nilai ke list kedua? (y/n): ").lower()
    if jawab2 == 'y':
        nama2 = input("Masukkan nilai untuk list kedua: ")
        list2.append(nama2)

    jawab3 = input("Apakah Anda ingin memasukkan nilai ke list ketiga? (y/n): ").lower()
    if jawab3 == 'y':
        nama3 = input("Masukkan nilai untuk list ketiga: ")
        list3.append(nama3)

    print("Berhasil ditambahkan, jika ada input!")
    
    
#Memanggil function
tambah_list()
kotak_random(list1, list2, list3)
