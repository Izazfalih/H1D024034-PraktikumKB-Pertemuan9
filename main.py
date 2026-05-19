"""
main.py — Algoritma Genetika untuk Knapsack Problem
====================================================
Menggabungkan seluruh operator GA:
  • Inisiasi Populasi
  • Evaluasi Fitness
  • Seleksi (Roulette Wheel / Tournament)
  • Crossover (One-Point / Two-Point / Uniform)
  • Mutasi (Swap / Inversion / Uniform)

Hasil akhir ditampilkan berupa:
  • Grafik fitness (Best, Average, Worst) per generasi
  • Item terbaik yang dimasukkan ke dalam knapsack
"""

import random
import matplotlib.pyplot as plt

from InisiasiPopulasi import inisiasi_populasi
from EvaluasiFitness   import evaluasi_fitness, evaluasi_populasi
from selection         import (roulette_wheel_selection_pasangan,
                               tournament_selection_pasangan)
from crossover         import (one_point_crossover,
                               two_point_crossover,
                               uniform_crossover)
from mutation          import (swap_mutation,
                               inversion_mutation,
                               uniform_mutation)

# ─────────────────────────────────────────────────────────────
#  KONFIGURASI PROBLEM
# ─────────────────────────────────────────────────────────────

# Data item: (nama, nilai, berat)
ITEMS = [
    ("Laptop",    300, 10),
    ("HP",        150,  4),
    ("Tablet",    200,  7),
    ("Charger",    80,  2),
    ("Headphone", 120,  3),
    ("Kamera",    250,  6),
    ("Drone",     400, 15),
    ("Speaker",    90,  4),
    ("Powerbank",  60,  2),
    ("Jam Tangan", 180,  1),
]

NAMA_ITEM   = [item[0] for item in ITEMS]
NILAI_ITEM  = [item[1] for item in ITEMS]
BERAT_ITEM  = [item[2] for item in ITEMS]
KAPASITAS   = 30          # kapasitas maksimum knapsack (kg)
JUMLAH_GEN  = len(ITEMS)  # panjang kromosom = jumlah item

# ─────────────────────────────────────────────────────────────
#  PARAMETER ALGORITMA GENETIKA
# ─────────────────────────────────────────────────────────────

UKURAN_POPULASI   = 20
JUMLAH_GENERASI   = 50
PROB_CROSSOVER    = 0.8
PROB_MUTASI       = 0.1

# Pilihan metode: 'roulette' atau 'tournament'
METODE_SELEKSI    = 'roulette'
# Pilihan metode: 'one_point', 'two_point', atau 'uniform'
METODE_CROSSOVER  = 'two_point'
# Pilihan metode: 'swap', 'inversion', atau 'uniform'
METODE_MUTASI     = 'uniform'


# ─────────────────────────────────────────────────────────────
#  FUNGSI BANTU
# ─────────────────────────────────────────────────────────────

def pilih_orang_tua(populasi, fitness):
    if METODE_SELEKSI == 'roulette':
        return roulette_wheel_selection_pasangan(populasi, fitness)
    else:
        return tournament_selection_pasangan(populasi, fitness, ukuran_turnamen=3)


def lakukan_crossover(p1, p2):
    if random.random() < PROB_CROSSOVER:
        if METODE_CROSSOVER == 'one_point':
            return one_point_crossover(p1, p2)
        elif METODE_CROSSOVER == 'two_point':
            return two_point_crossover(p1, p2)
        else:
            return uniform_crossover(p1, p2)
    return p1.copy(), p2.copy()


def lakukan_mutasi(kromosom):
    if METODE_MUTASI == 'swap':
        return swap_mutation(kromosom, PROB_MUTASI)
    elif METODE_MUTASI == 'inversion':
        return inversion_mutation(kromosom, PROB_MUTASI)
    else:
        return uniform_mutation(kromosom, PROB_MUTASI)


# ─────────────────────────────────────────────────────────────
#  MAIN — LOOP ALGORITMA GENETIKA
# ─────────────────────────────────────────────────────────────

def main():
    random.seed(42)

    # 1. Inisiasi populasi
    populasi = inisiasi_populasi(UKURAN_POPULASI, JUMLAH_GEN)

    riwayat_best  = []
    riwayat_avg   = []
    riwayat_worst = []

    print("=" * 60)
    print("   ALGORITMA GENETIKA — KNAPSACK PROBLEM")
    print(f"   Populasi: {UKURAN_POPULASI} | Generasi: {JUMLAH_GENERASI}")
    print(f"   Kapasitas: {KAPASITAS} kg | Item: {JUMLAH_GEN}")
    print("=" * 60)

    for gen in range(JUMLAH_GENERASI):

        # 2. Evaluasi fitness
        fitness = evaluasi_populasi(populasi, NILAI_ITEM, BERAT_ITEM, KAPASITAS)

        best  = max(fitness)
        avg   = sum(fitness) / len(fitness)
        worst = min(fitness)

        riwayat_best.append(best)
        riwayat_avg.append(avg)
        riwayat_worst.append(worst)

        if (gen + 1) % 10 == 0 or gen == 0:
            print(f"Generasi {gen+1:3d} | Best: {best:6.1f} | "
                  f"Avg: {avg:6.1f} | Worst: {worst:6.1f}")

        # 3. Buat populasi baru
        populasi_baru = []

        # Elitisme: pertahankan 2 individu terbaik
        sorted_pop = sorted(
            zip(fitness, populasi), key=lambda x: x[0], reverse=True
        )
        for f, k in sorted_pop[:2]:
            populasi_baru.append(k)

        # Isi sisa populasi
        while len(populasi_baru) < UKURAN_POPULASI:
            p1, p2 = pilih_orang_tua(populasi, fitness)
            c1, c2 = lakukan_crossover(p1, p2)
            c1 = lakukan_mutasi(c1)
            c2 = lakukan_mutasi(c2)
            populasi_baru.append(c1)
            if len(populasi_baru) < UKURAN_POPULASI:
                populasi_baru.append(c2)

        populasi = populasi_baru

    # ── Evaluasi generasi terakhir ──────────────────────────
    fitness = evaluasi_populasi(populasi, NILAI_ITEM, BERAT_ITEM, KAPASITAS)
    idx_terbaik   = fitness.index(max(fitness))
    kromosom_terbaik = populasi[idx_terbaik]

    total_nilai  = sum(v * g for v, g in zip(NILAI_ITEM, kromosom_terbaik))
    total_berat  = sum(w * g for w, g in zip(BERAT_ITEM, kromosom_terbaik))
    item_terpilih = [NAMA_ITEM[i] for i, g in enumerate(kromosom_terbaik) if g == 1]

    print()
    print("=" * 60)
    print("   SOLUSI TERBAIK")
    print("=" * 60)
    print(f"Kromosom    : {kromosom_terbaik}")
    print(f"Total Nilai : {total_nilai}")
    print(f"Total Berat : {total_berat} kg (Kapasitas: {KAPASITAS} kg)")
    print(f"Item yang dipilih:")
    for nama in item_terpilih:
        idx = NAMA_ITEM.index(nama)
        print(f"  ✓ {nama:15s} | Nilai: {NILAI_ITEM[idx]:4d} | "
              f"Berat: {BERAT_ITEM[idx]:2d} kg")

    # ── Plot Fitness ─────────────────────────────────────────
    generasi = list(range(1, JUMLAH_GENERASI + 1))

    plt.figure(figsize=(10, 6))
    plt.plot(generasi, riwayat_best,  color='#2ecc71', linewidth=2.0, label='Best Fitness')
    plt.plot(generasi, riwayat_avg,   color='#3498db', linewidth=1.5,
             linestyle='--', label='Average Fitness')
    plt.plot(generasi, riwayat_worst, color='#e74c3c', linewidth=1.5,
             linestyle=':',  label='Worst Fitness')

    plt.title('Algoritma Genetika — Knapsack Problem\nFitness per Generasi',
              fontsize=14, fontweight='bold')
    plt.xlabel('Generasi', fontsize=12)
    plt.ylabel('Fitness (Total Nilai)', fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('fitness_history.png', dpi=150)
    plt.show()
    print("\nGrafik disimpan sebagai 'fitness_history.png'")


if __name__ == "__main__":
    main()
