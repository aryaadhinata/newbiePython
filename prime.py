def cek_bilangan_prima(n):
    # Bilangan kurang dari 2 bukan bilangan prima
    if n <= 1:
        return False
    # Bilangan 2 adalah bilangan prima
    if n == 2:
        return True
    # Jika bilangan genap dan lebih dari 2 bukan bilangan prima
    if n % 2 == 0:
        return False
    # Periksa pembagi dari 3 hingga akar kuadrat dari n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print("="*10 + "Bilangan Prima" + "="*10)

bilangan = int(input("masukan bilangan :"))
if cek_bilangan_prima(bilangan):
    print(f"{bilangan} adalah bilangan prima.")
else:
    print(f"{bilangan} bukan bilangan prima.")

print("=" *34)