import random

# ─────────────────────────────────────────────────────────────
#  ONE-POINT CROSSOVER
# ─────────────────────────────────────────────────────────────

def one_point_crossover(parent1, parent2):
    """
    Melakukan One-Point Crossover antara dua kromosom orang tua.
    
    Sebuah titik potong dipilih secara acak, kemudian gen sebelum titik potong
    diambil dari parent1, dan gen sesudahnya dari parent2 (atau sebaliknya).
    
    Args:
        parent1: Kromosom pertama (list biner)
        parent2: Kromosom kedua  (list biner)
    
    Returns:
        (child1, child2): Dua kromosom anak hasil crossover
    """
    panjang = len(parent1)
    titik_potong = random.randint(1, panjang - 1)

    child1 = parent1[:titik_potong] + parent2[titik_potong:]
    child2 = parent2[:titik_potong] + parent1[titik_potong:]

    return child1, child2


# ─────────────────────────────────────────────────────────────
#  TWO-POINT CROSSOVER
# ─────────────────────────────────────────────────────────────

def two_point_crossover(parent1, parent2):
    """
    Melakukan Two-Point Crossover antara dua kromosom orang tua.
    
    Dua titik potong dipilih secara acak, kemudian segmen di antara kedua titik
    ditukar antara parent1 dan parent2.
    
    Args:
        parent1: Kromosom pertama (list biner)
        parent2: Kromosom kedua  (list biner)
    
    Returns:
        (child1, child2): Dua kromosom anak hasil crossover
    """
    panjang = len(parent1)
    titik1, titik2 = sorted(random.sample(range(1, panjang), 2))

    child1 = parent1[:titik1] + parent2[titik1:titik2] + parent1[titik2:]
    child2 = parent2[:titik1] + parent1[titik1:titik2] + parent2[titik2:]

    return child1, child2


# ─────────────────────────────────────────────────────────────
#  UNIFORM CROSSOVER
# ─────────────────────────────────────────────────────────────

def uniform_crossover(parent1, parent2, probabilitas=0.5):
    """
    Melakukan Uniform Crossover antara dua kromosom orang tua.
    
    Untuk setiap posisi gen, dilakukan pelemparan koin (probabilitas) untuk
    menentukan apakah gen diambil dari parent1 atau parent2.
    
    Args:
        parent1     : Kromosom pertama (list biner)
        parent2     : Kromosom kedua  (list biner)
        probabilitas: Peluang gen child1 berasal dari parent1 (default 0.5)
    
    Returns:
        (child1, child2): Dua kromosom anak hasil crossover
    """
    child1 = []
    child2 = []

    for gen1, gen2 in zip(parent1, parent2):
        if random.random() < probabilitas:
            child1.append(gen1)
            child2.append(gen2)
        else:
            child1.append(gen2)
            child2.append(gen1)

    return child1, child2


# ─────────────────────────────────────────────────────────────
#  DEMO
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parent1 = [1, 0, 1, 0, 1, 0, 1, 0]
    parent2 = [0, 1, 0, 1, 0, 1, 0, 1]

    print("=== One-Point Crossover ===")
    child1, child2 = one_point_crossover(parent1, parent2)
    print(f"Parent 1 : {parent1}")
    print(f"Parent 2 : {parent2}")
    print(f"Child 1  : {child1}")
    print(f"Child 2  : {child2}")

    print()
    print("=== Two-Point Crossover ===")
    child1, child2 = two_point_crossover(parent1, parent2)
    print(f"Parent 1 : {parent1}")
    print(f"Parent 2 : {parent2}")
    print(f"Child 1  : {child1}")
    print(f"Child 2  : {child2}")

    print()
    print("=== Uniform Crossover ===")
    child1, child2 = uniform_crossover(parent1, parent2)
    print(f"Parent 1 : {parent1}")
    print(f"Parent 2 : {parent2}")
    print(f"Child 1  : {child1}")
    print(f"Child 2  : {child2}")
