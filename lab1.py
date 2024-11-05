import string
sir = "Autoritățile au anunțat măsuri suplimentare pentru prevenirea răspândirii virusului. Aceasta include noi restricții de circulație și recomandări stricte privind distanțarea socială."

mid = len(sir) // 2
prima_parte = sir[:mid]
a_doua_parte = sir[mid:]

print("Prima parte:", prima_parte)
print("A doua parte:", a_doua_parte)
