print ("Masukkan Daftar Pesanan : eskrim , es teh, putih")
print ("daftar pesanan :['Eskrim', 'Es Teh', 'putih'")
print ("Masukkan pesanan ingin ditambahkan :PUTIH ")
print ("PUTIH sudah berada dalam pesanan")
                

daftar = input("Masukkan Daftar Pesanan : ")
pedagang= daftar.split()
print("Daftar Pesanan : ",pedagang)
nambah= input("Masukkan Pesanan Yang ingin ditambahkan:")
pedagang.append(nambah)
print("hasil penambahan dalam pesanan: ",pedagang)
