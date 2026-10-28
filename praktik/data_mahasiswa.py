def cari_mahasiswa(data, nim):
    """Mencari data mahasiswa berdasarkan NIM menggunakan method get()"""
    return data.get(nim)

def rata_rata_nilai(data):
    """Menghitung rata-rata nilai seluruh mahasiswa dalam dictionary"""
    if len(data) == 0:
        return 0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)

# Inisialisasi data mahasiswa dengan NIM sebagai key utama
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# 1. Uji Pencarian (Tersedia & Tidak Tersedia)
print("--- UJI PENCARIAN ---")
nim_cari = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim_cari)
if hasil is not None:
    print(f"Data {nim_cari} ditemukan: {hasil}")
else:
    print(f"Data {nim_cari}: Data tidak ditemukan")

nim_tidak_ada = "A999"
hasil_2 = cari_mahasiswa(data_mahasiswa, nim_tidak_ada)
if hasil_2 is not None:
    print(f"Data {nim_tidak_ada}: {hasil_2}")
else:
    print(f"Data {nim_tidak_ada}: Data tidak ditemukan")

# 2. Tambah Mahasiswa Baru
data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}

# 3. Ubah Nilai Mahasiswa Tertentu (A002 menjadi 82)
data_mahasiswa["A002"]["nilai"] = 82

# 4. Tampilkan Seluruh Data Menggunakan items()
print("\n--- REKAP SELURUH DATA MAHASISWA ---")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} | Info: {info}")

# 5. Hitung dan Tampilkan Rata-rata Kelas
rerata = rata_rata_nilai(data_mahasiswa)
print(f"\nRata-rata nilai kelas = {rerata:.2f}")