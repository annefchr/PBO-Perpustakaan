import sqlite3
connection = sqlite3.connect('buku.db')
class Buku():
    def __init__(self):
            pass

    @staticmethod
    def dataPengarang():
        global connection
        for row in connection.execute('SELECT * FROM pengarang'):
            print(row)

    @staticmethod
    def dataBuku():
        global connection
        for row in connection.execute('SELECT * FROM buku JOIN pengarang on buku.id_pengarang = pengarang.id'):
            print(row)

    @staticmethod
    def tambahDataPengarang():
        global connection
        nama = input('Nama Pengarang: ')
        daerah = input('Daerah Asal Pengarang: ')
        umur = input ('Umur Pengarang: ')
        queryStr = f'INSERT INTO pengarang(nama, daerah, umur) VALUES ("{nama}", "{daerah}", "{umur}")'
        connection.execute(queryStr)
        connection.commit()

    @staticmethod
    def tambahDataBuku():
        global connection
        judul = input('Judul Buku: ')
        id_pengarang = int(input('ID pengarang: '))
        harga = int(input('Harga Buku (Tulis tanpa koma atau titik): '))
        tebal = int(input('Tebal Buku: '))
        tanggal = input('Tanggal Buku: ') # Y-m-d H:i:s
        ISBN = int(input('ISBN Buku: '))
        penerbit = input('Penerbit Buku: ')
        query = f'INSERT INTO buku(judul, id_pengarang, harga, tebal_halaman, tanggal_terbit, ISBN, penerbit) VALUES ("{judul}", {id_pengarang}, {harga}, {tebal}, "{tanggal}", "{ISBN}", "{penerbit}")'
        connection.execute(query)
        connection.commit()

    @staticmethod
    def ubahBuku():
        global connection
        IdBuku = int(input('Id Buku :  '))
        judulBaru = input('Judul Buku Baru: ')
        idPengarangBaru = int(input('ID pengarang Baru: '))
        hargaBaru = int(input('Harga Buku Baru: '))
        tebalBaru = int(input('Tebal Buku Baru: '))
        tanggalBaru = input('Tanggal Buku Baru: ') # Y-m-d H:i:s
        ISBNBaru = int(input('ISBN Buku Baru: '))
        penerbitBaru = input('Penerbit Buku Baru: ')
        connection.execute("update buku set judul=?, id_pengarang=?, harga=?, tebal_halaman=?, tanggal_terbit=?, ISBN=?, penerbit=? where id =?",
        (judulBaru, idPengarangBaru, hargaBaru, tebalBaru, tanggalBaru, ISBNBaru, penerbitBaru, IdBuku))
        connection.commit()

    @staticmethod
    def ubahPengarang():
        global connection
        idPengarang = int(input('ID Pengarang: '))
        namaBaru= input('Nama Asal Pengarang Baru:  ')
        daerahBaru = input('Daerah Pengarang Baru:')
        umurBaru = input('Umur Pengarang Baru: ')
        connection.execute("update pengarang set nama=?, daerah=?, umur=? where id =?",
        (namaBaru, daerahBaru, umurBaru ,idPengarang ))
        connection.commit()

    @staticmethod
    def hapusBuku():
        global connection
        IdBuku =int(input('Id Buku :  '))
        cu = connection.cursor()
        cu.execute("delete from buku where buku.id=?",(IdBuku,))
        connection.commit()

    @staticmethod
    def hapusPengarang():
        global connection
        idPengarang=int(input('Id Pengarang :  '))
        cu = connection.cursor()
        cu.execute("delete from pengarang where pengarang.id=?",(idPengarang,))
        connection.commit()

def main():       
    while True:
        # def main():
        print("""
        Selamat datang di Perpustakaan Anne Lintang, siapa kamu?
        1. Pustakawan
        2. Anggota
        """)
        role = int(input('Siapa kamu?: '))
        if (role == 1):
            print("Halo, Kakak Pustakawan! Ingin melakukan apa?")
            print("""
                1. Melihat data pengarang
                2. Melihat data buku
                3. Menambah data pengarang
                4. Menambah data buku
                5. Mengubah data buku menurut id buku
                6. Mengubah data buku menurut id pengarang 
                7. Menghapus data buku berdasarkan id buku 
                8. Menghapus data pengarang berdasarkan id pengarang 
                9. Keluar
            """)
            pilihan = int(input('Pilihan: '))
            if (pilihan == 1):
                Buku.dataPengarang()
            elif (pilihan == 2):
                Buku.dataBuku()
            elif (pilihan == 3):
                Buku.tambahDataPengarang()
            elif (pilihan == 4):
                Buku.tambahDataBuku()
            elif (pilihan == 5):
                Buku.ubahBuku()
            elif (pilihan == 6):
                Buku.ubahPengarang()
            elif (pilihan == 7):
                Buku.hapusBuku()
            elif (pilihan == 8):
                Buku.hapusPengarang()
            elif (pilihan == 9):
                exit()
            else:
                print('Menu tidak valid!')
        else:
            print("Halo, Anggota! Ingin melakukan apa?")
            print("""
                1. Melihat data pengarang
                2. Melihat data buku 
                3. Keluar
            """)
            pilihan = int(input('Pilihan: '))
            if (pilihan == 1):
                Buku.dataPengarang()
            elif (pilihan == 2):
                Buku.dataBuku()
            elif (pilihan == 3):
                exit()
            else:
                print('Menu tidak valid!') 
            
main()


