# def = definition = definição___________________________________________________________
def print_hi(name):
    print(f'Oi, {name}')

def calcular_area_do_retangulo(largura, comprimento):
        return largura * comprimento

def calcular_area_do_quadrado(lado):
    return lado ** 2

def contagem_progressiva(fim):
    for numero in range (fim):
        print(numero)

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        if numero < 9:
            print(f'00{numero + 1} - {nome}')
        elif numero < 99:
            print(f'0{numero + 1} - {nome}')
        else:
            print(numero + 1,'-',nome)

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>3}'.format(numero))

def exibir_dia_da_semana_if (numero):
    if numero == 1:
        print('0 dia é segunda')
    elif numero == 2:
        print('O dia é Terça')
    elif numero == 3:
        print('O dia é Quarta')
    elif numero == 4:
        print('O dia é Quinta')
    elif numero == 5:
         print('O dia é Sexta')
    elif numero == 6:
        print('O dia é Sábado')
    elif numero == 7:
        print('O dia é Domingo')
    else:
         print('Número de dia inválido. Digite um numero de 1 a 7')

def exibir_dia_da_semana_match(numero):

    match numero:
        case 1:
            print('O dia é segunda')
            exit()
        case 2:
            print('O dia é terça')
            exit()
        case 3:
            print('O dia é quarta')
            exit()
        case 4:
            print('O dia é quinta')
            exit()
        case 5:
            print('O dia é sexta')
            exit()
        case 6:
            print('O dia é sábado')
            exit()
        case 7:
            print('O dia é domingo')
            exit()
        case _:
            print('Número de dia inválido. Digite um numero de 1 a 7')


def brincar_de_para_ou_continua():
    resposta = 'C'

    while resposta == 'C' or resposta == 'c':
        resposta = input('Digite C para continuar ou qualquer outro caracter para parar')

        print('Você decidiu parar com a brincadeira')






# estrutura de identificação / execução do script ________________________________



if __name__ == '__main__':
   print_hi('Cris')

   resultado = calcular_area_do_retangulo (3, 4)
   print(f'A area do retângulo é de {resultado} m²')

   resultado = calcular_area_do_quadrado(5)
   print(f'A area do quadrado é de {resultado} m²')

   contagem_progressiva(10)

   apoiar_candidato('fake',100)

   brincar_de_plim(100)

   exibir_dia_da_semana_if(7)

   exibir_dia_da_semana_match(1)

   brincar_de_para_ou_continua()

