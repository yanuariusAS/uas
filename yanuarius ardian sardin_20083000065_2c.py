'''''
CREATED BY : YANUARIUS ARDIAN SARDIN
KELAS : 2C
NIM 20083000065
'''''
#IMPORT TGL dan OS
import datetime
import os

#SET CLEAR = CLEAR SCREEN
clear = lambda: os.system('cls')

#SET TANGGAL
tanggal_sekarang = datetime.datetime.now()

#PERULANGAN PROGRAM
jwb = 'y'
while jwb == 'y':
    
    #DAFTAR LIST
    List_kode_golongan = [1,2,3]
    List_golongan = ['Golongan 1','Golongan 2','Golongan 3']
    List_gajipokok = [2500000,4500000,6500000]

    #TAMPILAN INTERFACE
    clear()
    print("+===========================================+")
    print("\t + SLIP GAJI +")
    print("Tanggal : ",tanggal_sekarang)
    print("+===========================================+")
    
    #TAMPILKAN LIST DENGAN PERULANGAN
    idx = 0
    print("Kode","\tGolongan", "\tGaji Pokok")
    while idx < len(List_kode_golongan) :
        print(str(List_kode_golongan[idx]) + "\t" + List_golongan[idx] + "\t Rp." + str(format(List_gajipokok[idx],',.2f'))) 
        idx = idx + 1
        
    #INPUTAN NAMA DAN GOLONGAN
    print("+===========================================+")
    input_Nama = input("\n> Masukkan Nama Pegawai : ")
    input_Golongan = int(input("> Masukkan Golongan Pegawai : "))

    #KONFIRMASI INPUTAN GOLONGAN TIDAK LEBIH DARI 3
    while input_Golongan > 3 or input_Golongan < 1 :
        sts = "\n !WARNING  Inputan Golongan Pegawai hanya boleh angka 1 - 3 "
        print(sts)
        input_Golongan = int(input("> Masukkan Golongan Pegawai : "))  

    #INPUTAN JENIS KELAMIN
    input_jenisKelamin = input("> Masukkan Jenis Kelamin Pegawai : ")
    input_jenisKelamin = input_jenisKelamin.lower()

    #KONFIRMASI INPUTAN JENIS KELAMIN HANYA BOLEH LAKI-LAKI DAN PEREMPUAN
    while input_jenisKelamin != "laki-laki" and input_jenisKelamin != "perempuan" :
        sts = "\n !WARNING  Inputan jenis kelamin hanya boleh laki-laki dan perempuan "
        print(sts)
        input_jenisKelamin = input("> Masukkan Jenis Kelamin Pegawai : ")
        input_jenisKelamin = input_jenisKelamin.lower()

    #INPUTAN STATUS KAWIN
    input_statusKawin = input("> Masukkan Status Kawin Pegawai : ") 
    input_statusKawin = input_statusKawin.lower()

    #KONFIRMASI INPUTAN STATUS KAWIN HANYA BOLEH KAWIN DAN BELUM KAWIN
    while input_statusKawin != "kawin" and input_statusKawin != "belum kawin":
        sts = "\n !WARNING  Inputan status kawin hanya boleh kawin dan belum kawin "
        print(sts)
        input_statusKawin = input("> Masukkan Status Kawin Pegawai : ") 
        input_statusKawin = input_statusKawin.lower()
            
    # JIKA STATUS KAWIN = KAWIN, MAKA TAMPILKAN INPUTAN PUNYA ANAK
    if input_statusKawin == "kawin":
                
        #INPUTAN PUNYA ANAK
        input_PunyaAnak = input("> Masukkan Punya Anak atau Belum Punya Anak : ")
        input_PunyaAnak = input_PunyaAnak.lower() 
                
        #KONFIRMASI INPUTAN PUNYA ANAK HANYA BOLEH PUNYA ANAK DAN BELUM PUNYA ANAK
        while input_PunyaAnak != "punya anak" and input_PunyaAnak != "belum punya anak":
            sts = "\n !WARNING  Inputan punya anak hanya boleh punya anak dan belum punya anak "
            print(sts)
            input_PunyaAnak = input("> Masukkan Punya Anak atau Belum Punya Anak : ")
            input_PunyaAnak = input_PunyaAnak.lower() 
    else :
        pass

    #BACA BERULANG IDX DIDALAM LIST GOLONGAN
    #JIKA VALUE IDX LIST GOLONGAN = VALUE PILIHAN, AMBIL IDXNYA
    idx = 0
    while idx < len(List_golongan):
        if List_kode_golongan[idx] == input_Golongan :
            gajipokok = List_gajipokok[idx]
            gol = List_golongan[idx]
        idx = idx + 1

    #TAMPILKAN DATA PEGAWAI
    clear()
    print("================================================")
    print("+++++++++++++++++ DATA PEGAWAI ++++++++++++++++\n ")
    print("Nama          = " + input_Nama)
    print("Status        = " + input_statusKawin)
    print("Golongan      = " + gol)
    print("Jenis kelamin = " + input_jenisKelamin)
    print("Gaji Pokok    = Rp." + str(format(gajipokok,',.2f')))

    #JIKA JENIS KELAMIN LAKI-LAKI DAN SUDAH KAWIN MAKA DAPAT TUNJANGAN ISTRI
    if input_statusKawin == "kawin":
        #Tunjangan Istri
        if input_jenisKelamin == "laki-laki" and input_statusKawin == "kawin":
            if input_Golongan == 1 :
                tunjanganIstri = 0.1 * gajipokok
            elif input_Golongan == 2 :
                tunjanganIstri = 0.3 * gajipokok
            elif input_Golongan == 3 :
                tunjanganIstri = 0.5 * gajipokok
        else :
            tunjanganIstri = 0
            
        #TUNJANGAN ANAK
        if input_PunyaAnak == "punya anak" and input_statusKawin == "kawin":
            tunjanganAnak = 0.2 * gajipokok
        elif input_PunyaAnak == "belum punya anak" and input_statusKawin == "kawin":
            tunjanganAnak = 0
    #JIKA BELUM KAWIN MAKA TIDAK DAPAT TUNJANGAN ISTRI DAN TUNJANGAN ANAK 
    elif input_statusKawin == "belum kawin" :
        tunjanganAnak = 0
        tunjanganIstri = 0

    #TAMPILKAN TUNJANGAN ISTRI DAN ANAK   
    print("\nTunjangan Istri = Rp." + str(format(tunjanganIstri,',.2f')))
    print("Tunjangan Anak    = Rp." + str(format(tunjanganAnak,',.2f')))

    #GAJI BRUTO
    if input_statusKawin == "kawin" and input_PunyaAnak == "punya anak": 
        gajibruto = gajipokok + tunjanganAnak + tunjanganIstri
        
    elif input_statusKawin == "kawin" and input_PunyaAnak == "belum punya anak":
        gajibruto = gajipokok + tunjanganIstri

    else :
        gajibruto = gajipokok
        
    #BIAYA JABATAN
    biayajabatan = 0.005 * gajibruto

    #TOTAL GAJI BRUTO
    totgajibruto = gajibruto-biayajabatan

    #IURAN PENSIUN
    iuranpensiun =  15500

    #IURAN ORGANISASI
    iuranorganisasi = 3500

    #GAJI NETO
    gajineto = totgajibruto - iuranpensiun - iuranorganisasi

    #TAMPILKAN RINCIAN GAJI
    print("=========================================")
    print("\t Rincian Slip Gaji")
    print("=========================================")
    print(">>> Gaji Bruto        = Rp." + format(gajibruto,',.2f'))
    print(">> Biaya Jabatan      = Rp." + format(biayajabatan,',.2f'))
    print("> Iuran Organisasi    = Rp." + format(iuranorganisasi,',.2f'))
    print("> Iuran Pensiun       = Rp." + format(iuranpensiun,',.2f'))
    print("> Gaji Bersih         = Rp." + format(totgajibruto,',.2f'))
    print(">>> Gaji Neto         = Rp." + format(gajineto,',.2f'))
    
    #PERTANYAAN 'APAKAH INGIN MENGULANG PROGRAM'
    jwb = input("\nHitung lagi ? (y/t) : ")
    jwb = jwb.lower()
    
        #KONFIRMASI INPUTAN HANYA BOLEH JAWAB y/t
    while jwb != 'y' and jwb != 't':
        sts = "\n !WARNING  Inputan jawab hanya boleh y dan t "
        print(sts)
        jwb = input("\nHitung lagi ? (y/t) : ")
        
        #JIKA JAWAB = t MAKA PROGRAM BERAKHIR   
    if jwb == "t":
        break
print("\n==== PROGRAM TELAH BERAKHIR ====\n\t")