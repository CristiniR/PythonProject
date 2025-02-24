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

def sair():
    print ('Obrigado e Volte Sempre')

# estrutura de identificação / execução do script ________________________________
if __name__ == '__main__':

   resposta = 'C'

   while resposta.upper () != 'Z':

       print('################################################')
       print('#                                              #')
       print('#    M  E  N  U    D  E    O  P  Ç  O  E  S    #')
       print('#                                              #')
       print('#    1 - Olá mundo                             #')
       print('#    2 - Área do Retângulo                     #')
       print('#    3 - Área do Quadrado                      #')
       print('#    4 - Contagem Progressiva                  #')
       print('#    5 - Apoiar Candidato                      #')
       print('#    6 - Brincar de PLIM                       #')
       print('#                                              #')
       print('#    Z - Sair                                  #')
       print('################################################')

       resposta = input('Escolha sua opção')
       print(f'A sua escolha foi: {resposta}')

       if resposta.upper() != 'Z':
            if resposta == '1':
                   print_hi('Cris')
            elif resposta == '2':
                 resultado = calcular_area_do_retangulo(8,7)
                 print(f' A Área do retangulo é de {resultado} m² ')
            elif resposta == '3':
                 resultado = calcular_area_do_quadrado(5)
                 print(f' A Área do quadrado é de {resultado} m² ')
            elif resposta == '4':
                   contagem_progressiva(10)
            elif resposta == '5':
                   apoiar_candidato('fake',5)
            elif resposta == '6':
                   brincar_de_plim(7)
            else:
                print('Voce digitou a opção invalida. Escolha uma opçao entre 1 e 6')
       else:
            print('Você escolheu sair, volte sempre!')



