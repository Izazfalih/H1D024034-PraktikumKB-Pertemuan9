import random

# ─────────────────────────────────────────────────────────────
#  ROULETTE WHEEL SELECTION (Fitness-Proportionate Selection)
# ─────────────────────────────────────────────────────────────

def roulette_wheel_selection(populasi, fitness_populasi):
    """
    Memilih satu individu menggunakan metode Roulette Wheel Selection.
    
    Setiap individu mendapat probabilitas terpilih sebanding dengan nilai
    fitness-nya terhadap total fitness seluruh populasi.
    
    Args:
        populasi          : List kromosom
        fitness_populasi  : List nilai fitness yang bersesuaian
    
    Returns:
        Kromosom terpilih (list biner)
    """
    total_fitness = sum(fitness_populasi)

    if total_fitness == 0:
        return random.choice(populasi)

    probabilitas = [f / total_fitness for f in fitness_populasi]

    nilai_acak = random.random()
    kumulatif  = 0.0
    for i, prob in enumerate(probabilitas):
        kumulatif += prob
        if nilai_acak <= kumulatif:
            return populasi[i]

    return populasi[-1]


def roulette_wheel_selection_pasangan(populasi, fitness_populasi):
    """
    Memilih dua individu (pasangan orang tua) menggunakan Roulette Wheel.
    
    Returns:
        (parent1, parent2): Dua kromosom yang terpilih
    """
    parent1 = roulette_wheel_selection(populasi, fitness_populasi)
    parent2 = roulette_wheel_selection(populasi, fitness_populasi)
    return parent1, parent2


# ─────────────────────────────────────────────────────────────
#  TOURNAMENT SELECTION
# ─────────────────────────────────────────────────────────────

def tournament_selection(populasi, fitness_populasi, ukuran_turnamen=3):
    """
    Memilih satu individu terbaik dari sampel turnamen secara acak.
    
    Args:
        populasi          : List kromosom
        fitness_populasi  : List nilai fitness yang bersesuaian
        ukuran_turnamen   : Jumlah individu yang masuk ke dalam turnamen
    
    Returns:
        Kromosom pemenang turnamen
    """
    peserta_idx = random.sample(range(len(populasi)), ukuran_turnamen)
    pemenang_idx = max(peserta_idx, key=lambda i: fitness_populasi[i])
    return populasi[pemenang_idx]


def tournament_selection_pasangan(populasi, fitness_populasi, ukuran_turnamen=3):
    """
    Memilih dua individu (pasangan orang tua) menggunakan Tournament Selection.
    
    Returns:
        (parent1, parent2): Dua kromosom pemenang turnamen
    """
    parent1 = tournament_selection(populasi, fitness_populasi, ukuran_turnamen)
    parent2 = tournament_selection(populasi, fitness_populasi, ukuran_turnamen)
    return parent1, parent2


# ─────────────────────────────────────────────────────────────
#  DEMO
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    populasi = [
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 1],
    ]
    fitness_populasi = [80, 45, 60, 30, 70]

    print("=== Roulette Wheel Selection ===")
    p1, p2 = roulette_wheel_selection_pasangan(populasi, fitness_populasi)
    print(f"Parent 1 : {p1}")
    print(f"Parent 2 : {p2}")

    print()
    print("=== Tournament Selection (ukuran turnamen = 3) ===")
    p1, p2 = tournament_selection_pasangan(populasi, fitness_populasi, ukuran_turnamen=3)
    print(f"Parent 1 : {p1}")
    print(f"Parent 2 : {p2}")
