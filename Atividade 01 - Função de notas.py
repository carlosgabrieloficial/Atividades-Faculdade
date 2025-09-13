notas = [ 7.5, 8.0, 6.5, 9.0, 7.0]

##programa para media da nota

def calculo_media(notas):
    soma_notas = sum(notas)
    media_notas = soma_notas/len(notas)

    return(media_notas)


##programa para arredondar a media da nota
    
arredondar_media = lambda media_notas:round(media_notas, 2)

## calcular a media

media = calculo_media(notas)

media_arredondada = arredondar_media(media)

##situação do estudante

print(notas)
print(media_arredondada)

