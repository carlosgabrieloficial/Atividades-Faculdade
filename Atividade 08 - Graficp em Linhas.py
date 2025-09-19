## funciona no Colab não sei por que ?
import matplotlib.pyplot as plt

dados_x = [1,2,3,4,5]
dados_y = [2,4,1,3,5]

plt.plot(dados_x,dados_y)

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.title("Grafico em linhas")

plt.show()
