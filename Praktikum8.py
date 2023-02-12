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
