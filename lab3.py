import string

articol = """
Maramureșul este situat în Munții Carpați și se învecinează cu Ucraina la nord. Regiunea este caracterizată de dealuri, văi adânci și păduri dense, ceea ce o face o destinație populară pentru iubitorii de natură. Turiștii vin aici și pentru tradițiile și obiceiurile de demult de aici, care se țin la sărbătorile din Maramureș, cum ar fi Paștele, Crăciunul sau Lăsata Secului. 
"""
# 1
mijloc = len(articol) // 2
prima_parte = articol[:mijloc]
a_doua_parte = articol[mijloc:]

# Procesarea primei părți:
prima_parte = prima_parte.upper().strip()

# Procesarea celei de-a doua părți:
a_doua_parte = a_doua_parte[::-1]
a_doua_parte = a_doua_parte.capitalize()
a_doua_parte = ''.join([char for char in a_doua_parte if char not in string.punctuation])
# 2
rezultat_final = prima_parte + " " + a_doua_parte
print(rezultat_final)