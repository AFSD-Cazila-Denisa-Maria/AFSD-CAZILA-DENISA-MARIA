import random

# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

# Afișarea șablonului inițial
print(" ".join(progres))

# Buclă principală de joc
while incercari_ramase > 0 and "_" in progres:
    # Cererea unei litere
    litera = input("Introdu o literă: ").lower()

    # Verificarea validității
    if len(litera) != 1 or not litera.isalpha():
        print("Te rog să introduci o singură literă.")
        continue
    if litera in litere_incercate:
        print("Ai încercat deja această literă. Încearcă alta.")
        continue

    # Adaugarea literei în lista de încercări
    litere_incercate.append(litera)

    # Verificarea literei în cuvânt
    if litera in cuvant_de_ghicit:
        for i, c in enumerate(cuvant_de_ghicit):
            if c == litera:
                progres[i] = litera
        print("Corect!")
    else:
        incercari_ramase -= 1
        print("Litera nu se află în cuvânt. Încercări rămase:", incercari_ramase)

    # Afișarea progresului și a încercărilor rămase
    print(" ".join(progres))

# Încheierea jocului
if "_" not in progres:
    print("Felicitări! Ai ghicit cuvântul:", cuvant_de_ghicit)
else:
    print("Ai pierdut! Cuvântul era:", cuvant_de_ghicit)
