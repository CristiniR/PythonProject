

# def = definition = definição
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





# estrutura de identificação / execução do script
if __name__ == '__main__':
   print_hi('Cris')

   resultado = calcular_area_do_retangulo (3, 4)
   print(f'A area do retângulo é de {resultado} m²')

   resultado = calcular_area_do_quadrado(5)
   print(f'A area do quadrado é de {resultado} m²')

   contagem_progressiva(10)

   apoiar_candidato('fake',100)

   brincar_de_plim(100)


