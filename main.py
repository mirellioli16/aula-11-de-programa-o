_author_ = 'mirelli' 'isabella'

a = int(input('digite um numero: '))
print('o numero digitado foi: ',a)
b = int(input('digite um numero: '))
print('digite um numero: ',b)

c = a + b

print(c)

print('========================================')

sal = float(input('digite seu salario: ').replace(',','.'))
print('seu salario é de R$ %.f2 '%sal)
porc = float(input('digite a porcentagem do aumeto: ').replace(',','.'))
print('seu aumento foi de: ', porc, 'porcento')
novosal = sal*porc+sal
print('O aumento do seu salário foi de R$%.2f '%novosal)