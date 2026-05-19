# Fungsi untuk menghitung nilai fitness
def hitung_fitness(kromosom, barang, kapasitas_tas):
    total_harga = 0
    total_bobot = 0

    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_harga += barang[i][1]
            total_bobot += barang[i][2]

    if total_bobot > kapasitas_tas:
        return 0 # Penalti jika melebihi kapasitas
    else:
        return total_harga

# Contoh penggunaan
if __name__ == "__main__":
    # Data barang (nama, harga, bobot)
    barang = [("Barang 1", 60, 10),
              ("Barang 2", 100, 20),
              ("Barang 3", 120, 30),
              ("Barang 4", 90, 25),
              ("Barang 5", 70, 15)]

    kapasitas_tas = 50 # Kapasitas maksimum tas

    # Definisi contoh populasi awal
    populasi_awal = [[1, 0, 1, 0, 1], # Contoh kromosom individu
                     [0, 1, 0, 1, 0],
                     [1, 1, 0, 0, 1]]

    # Contoh penggunaan
    fitness_populasi = [hitung_fitness(individu, barang, kapasitas_tas) for individu in populasi_awal]

    # Menampilkan nilai fitness
    print("\nNilai Fitness:")
    for idx, fitness in enumerate(fitness_populasi):
        print(f"Individu {idx+1}: Fitness = {fitness}")
