import random

# ─────────────────────────────────────────────────────────────
#  SWAP MUTATION
# ─────────────────────────────────────────────────────────────

def swap_mutation(kromosom, probabilitas_mutasi=0.1):
    """
    Melakukan Swap Mutation pada kromosom.
    
    Dua posisi gen dipilih secara acak, kemudian nilai keduanya ditukar.
    Mutasi dilakukan jika nilai acak lebih kecil dari probabilitas_mutasi.
    
    Args:
        kromosom          : Kromosom yang akan dimutasi (list biner)
        probabilitas_mutasi: Peluang terjadinya mutasi (default 0.1)
    
    Returns:
        kromosom_baru: Kromosom hasil mutasi (atau salinan asli jika tidak termutasi)
    """
    kromosom_baru = kromosom.copy()
    if random.random() < probabilitas_mutasi:
        idx1, idx2 = random.sample(range(len(kromosom_baru)), 2)
        kromosom_baru[idx1], kromosom_baru[idx2] = kromosom_baru[idx2], kromosom_baru[idx1]
    return kromosom_baru


# ─────────────────────────────────────────────────────────────
#  INVERSION MUTATION
# ─────────────────────────────────────────────────────────────

def inversion_mutation(kromosom, probabilitas_mutasi=0.1):
    """
    Melakukan Inversion Mutation pada kromosom.
    
    Sebuah segmen dipilih secara acak, kemudian urutan gen dalam segmen tersebut
    dibalik (reversed). Mutasi dilakukan jika nilai acak < probabilitas_mutasi.
    
    Args:
        kromosom          : Kromosom yang akan dimutasi (list biner)
        probabilitas_mutasi: Peluang terjadinya mutasi (default 0.1)
    
    Returns:
        kromosom_baru: Kromosom hasil mutasi (atau salinan asli jika tidak termutasi)
    """
    kromosom_baru = kromosom.copy()
    if random.random() < probabilitas_mutasi:
        panjang = len(kromosom_baru)
        idx1, idx2 = sorted(random.sample(range(panjang), 2))
        kromosom_baru[idx1:idx2 + 1] = kromosom_baru[idx1:idx2 + 1][::-1]
    return kromosom_baru


# ─────────────────────────────────────────────────────────────
#  UNIFORM MUTATION
# ─────────────────────────────────────────────────────────────

def uniform_mutation(kromosom, probabilitas_mutasi=0.1):
    """
    Melakukan Uniform Mutation pada kromosom.
    
    Setiap gen memiliki peluang sebesar probabilitas_mutasi untuk di-flip
    (0 → 1 atau 1 → 0) secara independen.
    
    Args:
        kromosom          : Kromosom yang akan dimutasi (list biner)
        probabilitas_mutasi: Peluang flip per gen (default 0.1)
    
    Returns:
        kromosom_baru: Kromosom hasil mutasi
    """
    kromosom_baru = kromosom.copy()
    for i in range(len(kromosom_baru)):
        if random.random() < probabilitas_mutasi:
            kromosom_baru[i] = 1 - kromosom_baru[i]
    return kromosom_baru


# ─────────────────────────────────────────────────────────────
#  DEMO
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    kromosom = [1, 0, 1, 0, 1, 0, 1, 0]

    print("=== Swap Mutation ===")
    print(f"Sebelum : {kromosom}")
    hasil = swap_mutation(kromosom, probabilitas_mutasi=1.0)   # paksa mutasi
    print(f"Sesudah : {hasil}")

    print()
    print("=== Inversion Mutation ===")
    print(f"Sebelum : {kromosom}")
    hasil = inversion_mutation(kromosom, probabilitas_mutasi=1.0)
    print(f"Sesudah : {hasil}")

    print()
    print("=== Uniform Mutation ===")
    print(f"Sebelum : {kromosom}")
    hasil = uniform_mutation(kromosom, probabilitas_mutasi=0.5)
    print(f"Sesudah : {hasil}")
