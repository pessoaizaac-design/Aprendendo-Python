# add(adiciona), update(atualiza), clear, discard
# union : (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não estão em amnbos)

# Add and Discard
s1 = set()
s1.add('Higor')
s1.add(18)
s1.discard(18)

print(s1)
# Saída = {'Higor'}

# Update
s2 = set()
s2.update([1,2,3,4,5] , {5,6})

print(s2)
# Saída = {1, 2, 3, 4, 5, 6}

# Union
s3 = {1,2,3,4,5}
s4 = {1,2,3,4,5,6,7,8}
s5 = s3 | s4

print(s5)
# Saída = {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection
s6 = {1,2,3,4,5}
s7 = {1,2,3,4,5,6,7,8}
s8 = s6 & s7 

print(s8)
# Saída = {1, 2, 3, 4, 5}


# Difference
s9 = {1,2,3,4,5}
s10 = {1,2,3,4,5,6,7,8}
s11 = s9 - s10 

print(s8)
# Saída = {1, 2, 3, 4, 5}

# Difference
s12 = {1,2,3,4,5,9}
s13 = {1,2,3,4,5,6,7,8}
s14 = s12 ^ s13 

print(s14)
# Saída = {6, 7, 8, 9}