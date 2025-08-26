# Sua solução aqui
massa = float(input())
contador = 0
while massa >= 0.5:
    massa = massa - 0.5 * massa
    contador += 1

segundostot = 50 * contador
horas = segundostot// 3600
minutos = (segundostot % 3600) // 60
segundos = segundostot % 60

print(f"{horas}h  {minutos}m  {segundos}s")
