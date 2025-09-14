texto = ('Explorando a diversidade de linguagens de programação com Pyhton')
        
print(f'Tamanho do texto = {len(texto)}')
print(f'Python in texto = {'Python'in texto}')
print(f'Quantidade de e no texto = {texto.count('e')}')
print(f'As 5 primeiras letras são: {texto[:5]}')


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
cores = ["Vermelho", "Azul", "Verde", "Amarelo", "Rcxo"]

for cor in cores :
    print(f"A Posição = {cores.index(cor)},a cor é {cor}")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

linguagens = ["Python","Java","JavaScriy","C","C#","C##","Swift","Go"]

linguagens = [item.lower() for item in linguagens]

print(linguagens)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

valor_em_dolar = [100,50,75,120]

taxa_cambio = 5.25

valor_em_real = list(map(lambda x : x*taxa_cambio,valor_em_dolar))

print(valor_em_real)

#map para aplicar uma função lambda que multiplica cada preçoem dólares pela taxa de câmbio. Depois, convertemos o resultado em uma lista. O resultado seráuma lista com os preços em reais

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

numero = [1,2,3,4,5,6,7,8,9,10]

numero_pares = list(filter(lambda x : x % 2 == 0, numero))

print(numero_pares)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

vogais = ("a","e","i","o","u")

for posicao , valor in enumerate(vogais):
    print(f"posicao/index {posicao}, valor/letra = {valor}")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

convidados = ("Alice","Bob","Carol","Eve")

confirmados = ("Bob","Carol")

#nao_confimado = [ convidado for convidado in convidados if convidado not is confirmados]

#print("Não confimaram")
#for pessoa in nao_confimado :
#    print(pessoa)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
