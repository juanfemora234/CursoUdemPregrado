alcancia = [1000, 500, 200]
meta = 2000

total = sum(alcancia)

if total >= meta:
    print("¡Felicidades! Alcanzaste tu meta de ahorro.")
else:
    falta = meta - total
    print(f"Te faltan {falta} pesos para alcanzar tu meta.")