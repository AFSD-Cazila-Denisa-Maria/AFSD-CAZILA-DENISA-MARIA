import string
articol =""""
Autoritățile au anunțat măsuri suplimentare pentru prevenirea răspândirii virusului.
Aceasta include noi restricții de circulație și recomandări stricte privind distanțarea socială.
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