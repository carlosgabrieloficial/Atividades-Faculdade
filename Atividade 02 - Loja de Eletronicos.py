# Você trabalha em uma loja de eletrodomésticos e precisa criar uma calculadora de desconto em Python para ajudar os vendedores a calcularem o valor final de uma compra com base no preço do produto e em um desconto percentual oferecido.

total_valor_produto = []


while True:

    valor_produto = int(input("Digite o valor do produto"))

    total_valor_produto.append(valor_produto)
    soma_valor =sum(total_valor_produto)



    continua = str(input("Continua [S/N]:"))

    if continua in "Nn":

        porcetual_desconto = float(input("Quanto de desconto você recebeu ?"))

        if porcetual_desconto > 0 or porcetual_desconto > 100 :

            desconto = soma_valor * (porcetual_desconto / 100)


        continua = str(input("Continua [S/N]:"))

        if continua in "Nn":
            print("FIM DO PROGRAMA" )
            break


print(f"Esse é a lista de preço que você comprou{total_valor_produto}")

print(f"Essa é soma dos valores antes do desconto{soma_valor}")

print(f"Esse é valor depois do desconto {desconto}")
