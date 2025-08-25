# 3-Uma loja online permite que seus clientes escolham entre dois tipos de entrega:

# "padrão": Custa R$10,00.

# "expresso": Custa R$20,00.

# Qualquer outra opção deve exibir: "Opção de entrega inválida.".

enter = input('Qual tipo de entrega vc quer ? (temos expresso e padrão)  ')

if enter == 'expresso' or enter == 'Expresso':
    print('Certo, você escolheu o expresso, ele custa 20R$')
elif enter == 'padrão' or enter == 'Padrão':
    print('Certo, você escolheu o Padrão , ele custa 20R$')
else:
    print('Opção Inválida')