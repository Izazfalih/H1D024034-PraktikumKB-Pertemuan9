import random

# Swap Mutation
def swap_mutation(kromosom):
    # Pastikan kromosom adalah list
    kromosom = list(kromosom) # Konversi ke list jika perlu
    
    # Pilih dua posisi untuk swap
    posisi1, posisi2 = random.sample(range(len(kromosom)), 2)
    
    # Melakukan swap
    kromosom[posisi1], kromosom[posisi2] = kromosom[posisi2], kromosom[posisi1]
    
    return kromosom

# Inversion Mutation
def inversion_mutation(kromosom):
    posisi1 = random.randint(0, len(kromosom) - 2)
    posisi2 = random.randint(posisi1 + 1, len(kromosom) - 1)
    
    # Perbaikan di sini: konversi hasil reversed ke list
    kromosom[posisi1:posisi2] = list(reversed(kromosom[posisi1:posisi2]))
    
    return kromosom

# Uniform Mutation
def uniform_mutation(kromosom, mutation_rate=0.1):
    # Pastikan kromosom adalah list
    kromosom = list(kromosom) # Konversi ke list jika perlu
    
    for i in range(len(kromosom)):
        if random.random() < mutation_rate:
            kromosom[i] = 1 - kromosom[i] # Membalik nilai gen
            
    return kromosom
