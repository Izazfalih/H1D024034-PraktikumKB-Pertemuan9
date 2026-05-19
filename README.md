# 🧬 Algoritma Genetika — Knapsack Problem

> **Praktikum Kecerdasan Buatan — Pertemuan 9**
> Implementasi Algoritma Genetika (Genetic Algorithm) untuk menyelesaikan masalah *0/1 Knapsack Problem*.

---

## 📋 Deskripsi

Algoritma Genetika (GA) adalah metode pencarian heuristik yang terinspirasi dari proses seleksi alam dan evolusi biologis. GA menggunakan mekanisme seperti seleksi, persilangan (*crossover*), dan mutasi untuk menghasilkan solusi yang semakin baik dari generasi ke generasi.

Pada praktikum ini, GA diterapkan untuk memecahkan **0/1 Knapsack Problem**, yaitu masalah optimasi kombinatorial yang bertujuan **memaksimalkan total nilai barang** yang dimasukkan ke dalam tas, dengan batasan **total berat tidak melebihi kapasitas maksimum**.

---

## 🧩 Representasi Kromosom

Setiap kromosom direpresentasikan sebagai **string biner** dengan panjang sama dengan jumlah item:

```
Kromosom : [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
              ↑     ↑  ↑     ↑          ↑  ↑
              item dipilih (gen = 1)
```

| Gen | Nilai | Keterangan            |
|-----|-------|-----------------------|
| `1` | Dipilih | Item dimasukkan ke knapsack |
| `0` | Tidak dipilih | Item tidak diambil  |

---

## 📁 Struktur File

```
Pertemuan9/
├── InisiasiPopulasi.py   # Inisialisasi populasi secara acak
├── EvaluasiFitness.py    # Fungsi evaluasi fitness (nilai knapsack)
├── selection.py          # Operator seleksi (Roulette Wheel & Tournament)
├── crossover.py          # Operator crossover (One-Point, Two-Point, Uniform)
├── mutation.py           # Operator mutasi (Swap, Inversion, Uniform)
├── main.py               # Program utama — loop GA lengkap
├── fitness_history.png   # Grafik hasil eksperimen
└── README.md             # Dokumentasi proyek
```

---

## ⚙️ Komponen Algoritma Genetika

### 1. 🔢 Inisiasi Populasi (`InisiasiPopulasi.py`)

Membuat populasi awal yang terdiri atas sejumlah kromosom dengan gen biner yang dibangkitkan secara acak.

```python
populasi = inisiasi_populasi(ukuran_populasi=20, jumlah_gen=10)
```

---

### 2. 📊 Evaluasi Fitness (`EvaluasiFitness.py`)

Menghitung nilai fitness setiap kromosom berdasarkan:
- **Total nilai** item yang dipilih (gen = 1)
- **Penalti**: jika total berat melebihi kapasitas, fitness = **0**

```python
fitness = evaluasi_fitness(kromosom, nilai_item, berat_item, kapasitas_maks)
```

---

### 3. 🎯 Seleksi (`selection.py`)

Dua metode seleksi orang tua tersedia:

| Metode | Deskripsi |
|--------|-----------|
| **Roulette Wheel** | Probabilitas terpilih ∝ nilai fitness individu |
| **Tournament** | Pilih individu terbaik dari sampel turnamen acak |

```python
# Roulette Wheel
p1, p2 = roulette_wheel_selection_pasangan(populasi, fitness)

# Tournament (ukuran turnamen = 3)
p1, p2 = tournament_selection_pasangan(populasi, fitness, ukuran_turnamen=3)
```

---

### 4. 🔀 Crossover (`crossover.py`)

Tiga metode crossover tersedia:

| Metode | Deskripsi |
|--------|-----------|
| **One-Point** | Satu titik potong; gen sebelum titik dari parent1, sisanya dari parent2 |
| **Two-Point** | Dua titik potong; segmen tengah ditukar antar orang tua |
| **Uniform** | Setiap gen dipilih secara acak dari salah satu orang tua |

```python
child1, child2 = one_point_crossover(parent1, parent2)
child1, child2 = two_point_crossover(parent1, parent2)
child1, child2 = uniform_crossover(parent1, parent2)
```

---

### 5. 🔬 Mutasi (`mutation.py`)

Tiga metode mutasi tersedia:

| Metode | Deskripsi |
|--------|-----------|
| **Swap** | Menukar nilai dua gen yang dipilih secara acak |
| **Inversion** | Membalik urutan gen dalam segmen acak |
| **Uniform** | Setiap gen memiliki peluang untuk di-flip (0↔1) |

```python
kromosom_baru = swap_mutation(kromosom, probabilitas_mutasi=0.1)
kromosom_baru = inversion_mutation(kromosom, probabilitas_mutasi=0.1)
kromosom_baru = uniform_mutation(kromosom, probabilitas_mutasi=0.1)
```

---

## 🔧 Konfigurasi Parameter

Ubah parameter di bagian atas `main.py` sesuai kebutuhan:

| Parameter | Default | Keterangan |
|-----------|---------|------------|
| `UKURAN_POPULASI` | `20` | Jumlah individu per generasi |
| `JUMLAH_GENERASI` | `50` | Banyak generasi yang dijalankan |
| `PROB_CROSSOVER` | `0.8` | Probabilitas crossover |
| `PROB_MUTASI` | `0.1` | Probabilitas mutasi |
| `KAPASITAS` | `30 kg` | Kapasitas maksimum knapsack |
| `METODE_SELEKSI` | `'roulette'` | `'roulette'` atau `'tournament'` |
| `METODE_CROSSOVER` | `'two_point'` | `'one_point'`, `'two_point'`, atau `'uniform'` |
| `METODE_MUTASI` | `'uniform'` | `'swap'`, `'inversion'`, atau `'uniform'` |

---

## 🚀 Cara Menjalankan

### Prasyarat

Pastikan Python 3 dan `matplotlib` terinstall:

```bash
pip install matplotlib
```

### Menjalankan Program Utama

```bash
python main.py
```

### Menjalankan Modul Secara Individual

```bash
python InisiasiPopulasi.py   # Demo inisiasi populasi
python EvaluasiFitness.py    # Demo evaluasi fitness
python selection.py          # Demo seleksi
python crossover.py          # Demo crossover
python mutation.py           # Demo mutasi
```

---

## 📦 Data Item (Knapsack)

| No | Item | Nilai | Berat |
|----|------|-------|-------|
| 1 | Laptop | 300 | 10 kg |
| 2 | HP | 150 | 4 kg |
| 3 | Tablet | 200 | 7 kg |
| 4 | Charger | 80 | 2 kg |
| 5 | Headphone | 120 | 3 kg |
| 6 | Kamera | 250 | 6 kg |
| 7 | Drone | 400 | 15 kg |
| 8 | Speaker | 90 | 4 kg |
| 9 | Powerbank | 60 | 2 kg |
| 10 | Jam Tangan | 180 | 1 kg |

**Kapasitas Knapsack:** 30 kg

---

## 📈 Hasil Eksperimen

Output setelah menjalankan `main.py` (50 generasi, populasi 20):

```
============================================================
   ALGORITMA GENETIKA — KNAPSACK PROBLEM
   Populasi: 20 | Generasi: 50
   Kapasitas: 30 kg | Item: 10
============================================================
Generasi   1 | Best: 1030.0 | Avg:  398.0 | Worst:    0.0
Generasi  10 | Best: 1130.0 | Avg:  632.5 | Worst:    0.0
Generasi  20 | Best: 1130.0 | Avg:  852.5 | Worst:    0.0
Generasi  30 | Best: 1170.0 | Avg:  894.5 | Worst:    0.0
Generasi  40 | Best: 1170.0 | Avg:  709.5 | Worst:    0.0
Generasi  50 | Best: 1170.0 | Avg:  832.5 | Worst:    0.0

============================================================
   SOLUSI TERBAIK
============================================================
Kromosom    : [1, 1, 0, 1, 1, 1, 0, 1, 0, 1]
Total Nilai : 1170
Total Berat : 30 kg (Kapasitas: 30 kg)
Item yang dipilih:
  ✓ Laptop          | Nilai:  300 | Berat: 10 kg
  ✓ HP              | Nilai:  150 | Berat:  4 kg
  ✓ Charger         | Nilai:   80 | Berat:  2 kg
  ✓ Headphone       | Nilai:  120 | Berat:  3 kg
  ✓ Kamera          | Nilai:  250 | Berat:  6 kg
  ✓ Speaker         | Nilai:   90 | Berat:  4 kg
  ✓ Jam Tangan      | Nilai:  180 | Berat:  1 kg
```

Grafik konvergensi fitness disimpan sebagai `fitness_history.png`.

---

## 🔄 Alur Algoritma Genetika

```
1. Inisiasi Populasi Awal (acak)
         ↓
2. Evaluasi Fitness setiap kromosom
         ↓
3. Cek kondisi berhenti? (generasi maks tercapai?)
   ├── YA  → Tampilkan solusi terbaik & grafik
   └── TIDAK ↓
4. Seleksi orang tua (Roulette Wheel / Tournament)
         ↓
5. Crossover → hasilkan anak baru
         ↓
6. Mutasi → variasi pada anak baru
         ↓
7. Elitisme → pertahankan 2 individu terbaik
         ↓
8. Bentuk populasi generasi berikutnya
         ↓
   Kembali ke langkah 2
```

---

## 👤 Informasi

| | |
|---|---|
| **Mata Kuliah** | Praktikum Kecerdasan Buatan |
| **Pertemuan** | 9 — Algoritma Genetika |
| **Bahasa** | Python 3 |
| **Library** | `random`, `matplotlib` (built-in + standard) |
