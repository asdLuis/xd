def promedio(num):
  suma = 0
  for i in num:
    suma += i
  return suma/len(num)

print(f"El promedio es: {promedio([1, 2, 3])}")



