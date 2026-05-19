def evaluasi_fitness(kromosom, nilai_item, berat_item, kapasitas_maks):
    """
    Mengevaluasi fitness dari sebuah kromosom untuk Knapsack Problem.
    
    Jika total berat melebihi kapasitas maksimum, fitness = 0 (penalti).
    Jika tidak, fitness = total nilai item yang dipilih.
    
    Args:
        kromosom    : List biner (0/1) yang merepresentasikan item yang dipilih
        nilai_item  : List nilai setiap item
        berat_item  : List berat setiap item
        kapasitas_maks: Kapasitas maksimum knapsack
    
    Returns:
        fitness: Nilai fitness (total nilai item yang valid, atau 0 jika overweight)
    """
    total_nilai = 0
    total_berat = 0

    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_nilai += nilai_item[i]
            total_berat += berat_item[i]

    if total_berat > kapasitas_maks:
        return 0
    else:
        return total_nilai


def evaluasi_populasi(populasi, nilai_item, berat_item, kapasitas_maks):
    """
    Mengevaluasi fitness seluruh populasi.
    
    Args:
        populasi      : List kromosom
        nilai_item    : List nilai item
        berat_item    : List berat item
        kapasitas_maks: Kapasitas maksimum knapsack
    
    Returns:
        fitness_populasi: List nilai fitness untuk setiap kromosom
    """
    fitness_populasi = []
    for kromosom in populasi:
        fitness = evaluasi_fitness(kromosom, nilai_item, berat_item, kapasitas_maks)
        fitness_populasi.append(fitness)
    return fitness_populasi


if __name__ == "__main__":
    # Contoh item: (nilai, berat)
    nilai_item  = [10, 20, 30, 40, 50, 25, 15, 35]
    berat_item  = [5,  10, 15, 20, 25, 12,  7, 18]
    kapasitas_maks = 50

    # Contoh kromosom
    kromosom1 = [1, 0, 1, 0, 0, 1, 1, 0]   # valid
    kromosom2 = [1, 1, 1, 1, 1, 1, 1, 1]   # overweight

    print("=== Evaluasi Fitness ===")
    print(f"Kromosom 1 : {kromosom1}")
    print(f"Fitness 1  : {evaluasi_fitness(kromosom1, nilai_item, berat_item, kapasitas_maks)}")
    print()
    print(f"Kromosom 2 : {kromosom2}")
    print(f"Fitness 2  : {evaluasi_fitness(kromosom2, nilai_item, berat_item, kapasitas_maks)}")
