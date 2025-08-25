# 2-Crie um programa que solicita a idade de uma pessoa e classifica-a em uma das seguintes
# categorias:

# Até 12 anos: "Criança"

# Entre 13 e 17 anos: "Adolescente"

# Entre 18 e 59 anos: "Adulto"

# 60 anos ou mais: "Idoso"

age = int(input('Quantos anos você tem ? '))

if age <=12 :
    print('Criança')
elif age >=13 and age <=17 :  
    print('Adolescente')
elif age >= 18 and age <= 59 :
    print('Adulto')
else:
    print('Idoso')