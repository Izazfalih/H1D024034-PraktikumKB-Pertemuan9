import random

def inisiasi_populasi(ukuran_populasi, jumlah_gen):
    """
    Menginisialisasi populasi secara acak dengan kromosom berbasis biner.
    
    Args:
        ukuran_populasi: Jumlah individu dalam populasi
        jumlah_gen: Jumlah gen (sama dengan jumlah item)
    
    Returns:
        populasi: List berisi kromosom (setiap kromosom adalah list biner)
    """
    populasi = []
    for _ in range(ukuran_populasi):
        kromosom = [random.randint(0, 1) for _ in range(jumlah_gen)]
        populasi.append(kromosom)
    return populasi


if __name__ == "__main__":
    # Contoh penggunaan
    ukuran_populasi = 5
    jumlah_gen = 8

    populasi = inisiasi_populasi(ukuran_populasi, jumlah_gen)

    print("=== Inisiasi Populasi ===")
    print(f"Ukuran Populasi : {ukuran_populasi}")
    print(f"Jumlah Gen      : {jumlah_gen}")
    print()

    for i, kromosom in enumerate(populasi):
        print(f"Individu {i+1}: {kromosom}")
