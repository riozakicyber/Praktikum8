Nama    : Rio Rinto Saki

NIM     : 312210715

Kelas   : TI.22.C.9

# Praktikum 8

Pada praktek kali ini, saya mencoba membuat program sederhana dengan mengaplikasikan penggunaan class, program ini dibuat untuk menambah, mengubah, menghapus, dan menampilkan daftar nama dan nilai mahasiswa. 

- Source Code
```
class DaftarNilai:
    def __init__(self):
        self.data = []

    def tambah(self, nama, nilai):
        self.data.append({"nama": nama, "nilai": nilai})

    def tampilkan(self):
        if not self.data:
            print("Data Tidak Ditemukan")
        else:
            print("Daftar Nilai: ")
            for i, item in enumerate(self.data):
                print(f"{i+1}. {item['nama']} : {item['nilai']}")

    def hapus(self, nama):
        found = False
        for i, item in enumerate(self.data):
            if item["nama"] == nama:
                found = True
                del self.data[i]
                break
        if not found:
            print(f"Data {nama} Tidak Ditemukan")

    def ubah(self, nama, nilai):
        found = False
        for i, item in enumerate(self.data):
            if item["nama"] == nama:
                found = True
                self.data[i]["nilai"] = nilai
                break
        if not found:
            print(f"Data {nama} Tidak Ditemukan")

if __name__ == "__main__":
    daftar_nilai = DaftarNilai()
    while True:
        print("=" * 22)
        print("Daftar Nilai Mahasiswa")
        print("=" * 22)
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("0. Keluar")
        pilihan = int(input("Pilihan: "))
        if pilihan == 1:
            nama = input("Nama: ")
            nilai = int(input("Nilai: "))
            daftar_nilai.tambah(nama, nilai)
        elif pilihan == 2:
            daftar_nilai.tampilkan()
        elif pilihan == 3:
            nama = input("Nama: ")
            daftar_nilai.hapus(nama)
        elif pilihan == 4:
            nama = input("Nama: ")
            nilai = int(input("Nilai Baru: "))
            daftar_nilai.ubah(nama, nilai)
        elif pilihan == 0:
            break
        else:
            print("Pilihan salah")
```


- Flowchart
![Flowchart Praktikum7](https://user-images.githubusercontent.com/123881535/218322881-3cf209ba-b107-4040-b763-270afb28a639.png)


- Hasil Input

![Screenshot (64)](https://user-images.githubusercontent.com/123881535/218320400-b4bfe133-755e-4e72-bd03-006472363246.png)
![Screenshot (65)](https://user-images.githubusercontent.com/123881535/218320407-183bc7a0-6970-409f-9cfe-8bd8ca239d17.png)


- Hasil Output

![Screenshot (66)](https://user-images.githubusercontent.com/123881535/218320476-3ba98e3f-75ef-4e46-a6eb-460ca155accd.png)
![Screenshot (67)](https://user-images.githubusercontent.com/123881535/218320488-bac226dc-16a9-42ff-884f-80aae47e051e.png)

