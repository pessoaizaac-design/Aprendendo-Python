# Set Comprehension

# Funcionara quase igual o Dictionary

#--------------------------------------------------------------------------

funcionarios = ["Ana", "Bruno", "Amanda", "Carlos", "Beatriz"]

# O set comprehension vai ignorar as iniciais repetidas ('A' e 'B')
letras_iniciais = {nome[0] for nome in funcionarios}

print(letras_iniciais)
# Saída (a ordem pode variar): {'B', 'C', 'A'}

#--------------------------------------------------------------------------

valores_com_duplicados = [10, 20, 10, 50, 20, 100]

# Eleva ao quadrado apenas os números únicos da lista
quadrados_unicos = {v ** 2 for v in valores_com_duplicados}

print(quadrados_unicos)
# Saída (a ordem pode variar): {10000, 100, 2500, 400}
