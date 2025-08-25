# 1-Você foi contratado para desenvolver um sistema simples de pagamento online. O sistema deve
# identificar o método de pagamento escolhido pelo usuário e exibir a mensagem correspondente:

# Se o usuário escolher "cartao", o programa deve exibir: "Processando pagamento no cartão...".

# Se o usuário escolher "boleto", o programa deve exibir: "Gerando boleto bancário...".

# Para qualquer outro método, o programa deve exibir: "Método de pagamento não reconhecido.".

n1= input('Bom Dia, qual vai ser o método de pagamento? ')

if n1 == 'cartao':
 print('Processando pagamento no cartão...')
elif n1 == 'boleto':
  print('Gerando boleto bancário...')
elif n1 == 'PIX':
    print('Processando seu PIX...')
else:
  print('pagamento não reconhecido.')