def binarioParaDecimal(numero):
    soma = 0
    numeroInvertido = numero[::-1]
    for indice, digito in enumerate(numeroInvertido):
         digitoInteiro = int(digito)
         soma = soma + (digitoInteiro * (2**indice))
    return soma

def binarioParaOctal(numero):
    comprimento = len(numero)
    numeroModificado = ""
    basesOctais = {
         '000': '0',
         '001': '1',
         '010': '2',
         '011': '3',
         '100': '4',
         '101': '5',
         '110': '6',
         '111': '7'
    }
    
    # agora vamos converter
    
    if comprimento % 3 != 0:
        while comprimento % 3 != 0: # p/ caso a qnt de digitos n seja um múltiplo de 3 p/ dividr
            numero = '0' + numero  # adiciona zero à esquerda
            comprimento = len(numero)
    
    i = 0
    while i < comprimento: # garante que a conversão usará todos os dígitos
         grupoDeTres = numero[i:i+3] # vai pegar os 3 primeiros digitos, vai do 0 até 3-1 (2), ou seja, se tiver 100000 -> primeiramente vai pegar o 100 (0 até 2) e depois, vai de 3 ate 5
         numeroOctal = basesOctais[grupoDeTres] # vai acessar o dicionario, por exemplo, grupo de tres = '100', aí no dicionario vai procurar essa chave e pegar o seu valor correspondente
         numeroModificado = numeroModificado + numeroOctal # vamos concatenar a string e transformar no numero convertido
         i = i + 3
    return numeroModificado


def binarioParaHexadecimal(numero):
    # mesma logica do octal, só que multiplos de 4
    comprimento = len(numero)
    numeroConvertido = ""
    basesHexadecimais = {
         '0000': '0',
         '0001': '1',
         '0010': '2',
         '0011': '3',
         '0100': '4',
         '0101': '5',
         '0110': '6',
         '0111': '7',
         '1000': '8',
         '1001': '9',
         '1010': 'A',
         '1011': 'B',
         '1100': 'C',
         '1101': 'D',
         '1111': 'F'

    }
    
    if comprimento % 4 != 0:
         while comprimento % 4 != 0:
              numero = '0' + numero # vou colocar zeros à esquerda até ser multiplo de 4
              comprimento = len(numero)


    i = 0
    while i < comprimento:
         gruposDe4 = numero[i:i+4] # grupos de 4, kkkkkkkkkkk
         numeroHexadecimal = basesHexadecimais[gruposDe4] # de novo, vai acessar o dicionario com essa chave que vai pegar concatenando a string
         numeroConvertido = numeroConvertido + numeroHexadecimal
         i = i + 4
       
    return numeroConvertido
    


def decimalParaBinario(numero):
    numeroInteiro = int(numero)
    listaBinaria = []
    novaListaBinaria = []
    while numeroInteiro > 0: # finalize a divisão, lembrando: 1 % 2 = 1. 1 // 2 = 0
        resto = numeroInteiro % 2
        restoStr = str(resto)
        listaBinaria.append(restoStr)
        numeroInteiro = numeroInteiro//2 # aqui o numero vai atualizando, ele vai continuar a dividir
    novaListaBinaria = listaBinaria[::-1] # inverte
    numeroBinario = "".join(novaListaBinaria)
    
    return numeroBinario
    

def decimalParaOctal(numero):
     numeroInteiro = int(numero)
     listaOctal = []
     novaListaOctal = []
     while numeroInteiro > 0: # finalizar a divisão
          resto = numeroInteiro % 8
          restoStr = str(resto)
          listaOctal.append(restoStr)
          numeroInteiro = numeroInteiro//8 # precisa atualizar o numero
     novaListaOctal = listaOctal[::-1]
     numeroOctal = "".join(novaListaOctal) # so tirar os elementos da lista

     return numeroOctal

def decimalParaHexadecimal(numero):
     numeroInteiro = int(numero)
     listaHexa = []
     novaListaHexa = []
     
     excecoes = {
          10: 'A',
          11: 'B',
          12: 'C',
          13: 'D',
          14: 'E',
          15: 'F'
     }
     
     while numeroInteiro > 0: # finalizar a divisão
          resto = numeroInteiro % 16
          if resto < 10:
               restoStr = str(resto)
               listaHexa.append(restoStr)
               numeroInteiro = numeroInteiro//16 # precisa atualizar o numero
          else:
               listaHexa.append(excecoes[resto])
               numeroInteiro = numeroInteiro//16 # precisa atualizar o numero
     novaListaHexa = listaHexa[::-1]
     numeroHexadecimal = "".join(novaListaHexa) # so tirar os elementos da lista

     return numeroHexadecimal


def octalParaBinario(numero):
     # octal > binario -> separar os digitos, por exemplo, 2335 = 2 = 010; 3 = 011, 3 = 011, 5 = 101, a9 junta
     # 010 + 011 + 011 + 101
     numeroConvertido = ""
     bases = {
         '0': '000',
         '1': '001',
         '2': '010',
         '3': '011',
         '4': '100',
         '5': '101',
         '6': '110',
         '7': '111'
    }
    
     for indice in numero:
          digitos = bases[indice] # vou acessar o dicionario cada vez que meu indice percorre, por exemplo, em 2335, se meu indice for '2', ele vai procurar no dicionario o valor correspondente a essa chave
          numeroConvertido = numeroConvertido + digitos
     
     return numeroConvertido

def octalParaDecimal(numero):
    soma = 0
    numeroInvertido = numero[::-1]
    for indice, digito in enumerate(numeroInvertido):
         digitoInteiro = int(digito)
         soma = soma + (digitoInteiro * (8**indice))
    
    return soma

     
def octalParaHexadecimal(numeroOctal): 
    numeroEmBinario =  octalParaBinario(numeroOctal)
    numeroHexadecimal = binarioParaHexadecimal(numeroEmBinario)

    return numeroHexadecimal

def hexadecimalParaBinario(numero):
    numeroConvertido = ""
    bases = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    for i in numero:
        numeroConvertido = numeroConvertido + bases[i]
     
    return numeroConvertido
     

def hexadecimalParaDecimal(numero):
    numeroInvertido = numero[::-1]
    listaNumerica = []
    soma = 0
    letras = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    for digito in numeroInvertido:
        if digito.isdigit() == True:
            digitoInt = int(digito)
            listaNumerica.append(digitoInt)
        else:
            letraConvertida = letras[digito]
            listaNumerica.append(letraConvertida)
     # todos os elementos adicionados

    for indice, digito in enumerate(listaNumerica):
        soma = soma + digito*(16**indice)

    return soma

def hexadecimalParaOctal(numeroHexa):
    numeroEmBinario = hexadecimalParaBinario(numeroHexa)
    numeroEmOctal = binarioParaOctal(numeroEmBinario)
    
    return numeroEmOctal

def main():
    print("Bem vindo ao menu de conversão de números ")
    print("Escolha uma base e depois escolha uma das conversões abaixo: ")
    print("")
    print("Aperte 2 para escolher um número de base binária")
    print("Aperte 10 para escolher um número de base decimal")
    print("Aperte 8 para escolher um número de base octal")
    print("Aperte 16 para escolher um número de base hexadecimal")
    while True:
            escolha = int(input())
            if escolha != 2 and escolha != 10 and escolha != 16 and escolha != 8:
                 print("")
                 print("Valor inválido.")
                 print("Digite o primeiro valor novamente.")
                 print("")
            else:
               print("")
               print("Maravilha! Vamos converter para qual outra base? ")
               print("")
               print("Aperte 2 para converter um número em base binária")
               print("Aperte 10 para converter um número em base decimal")
               print("Aperte 8 para converter um número em base octal")
               print("Aperte 16 para converter um número em base hexadecimal")
               conversao = int(input())
               print("")
               if escolha == conversao:
                    print("Ops! As bases são iguais!")
                    print("Escolha novamente a primeira base a ser convertida: ")
                    print("")
               elif escolha == 2 and conversao == 10:
                    numero = input("Digite o seu número em binario para converter em decimal ")
                    numeroConvertido = binarioParaDecimal(numero)
                    print(f"Legal! O seu numero {numero} em binario para decimal fica: {numeroConvertido}")   
                    
               elif escolha == 2 and conversao == 8:
                    numero = input("Digite o seu número em binario para converter em octal ")
                    numeroConvertido = binarioParaOctal(numero)
                    print(f"Legal! O seu numero {numero} em binario para octal fica: {numeroConvertido}")
                    
               elif escolha == 2 and conversao == 16:
                    numero = input("Digite o seu número em binario para converter em hexadecimal ")
                    numeroConvertido = binarioParaHexadecimal(numero)
                    print(f"Legal! O seu numero {numero} em binario para hexadecimal fica: {numeroConvertido}")
                    
               elif escolha == 10 and conversao == 2:
                    numero = input("Digite o seu número em decimal para converter em binario ")
                    numeroConvertido = decimalParaBinario(numero)
                    print(f"Legal! O seu numero {numero} em decimal para binário fica: {numeroConvertido}")
                    
               elif escolha == 10 and conversao == 8:
                    numero = input("Digite o seu número em decimal para converter em octal ")
                    numeroConvertido = decimalParaOctal(numero)
                    print(f"Legal! O seu numero {numero} em decimal para octal fica: {numeroConvertido}")
                    
               elif escolha == 10 and conversao == 16:
                    numero = input("Digite o seu número em decimal para converter em hexadecimal ")
                    numeroConvertido = decimalParaHexadecimal(numero)
                    print(f"Legal! O seu numero {numero} em decimal para hexadecimal fica: {numeroConvertido}")
                    
               elif escolha == 8 and conversao == 2:
                    numero = input("Digite o seu número em octal para converter em binario ")
                    numeroConvertido = octalParaBinario(numero)
                    print(f"Legal! O seu numero {numero} em octal para binario fica: {numeroConvertido}")
                    
               elif escolha == 8 and conversao == 10:
                    numero = input("Digite o seu número em octal para converter em decimal ")
                    numeroConvertido = octalParaDecimal(numero)
                    print(f"Legal! O seu numero {numero} em octal para decimal fica: {numeroConvertido}")
                    
               elif escolha == 8 and conversao == 16:
                    numero = input("Digite o seu número em octal para converter em hexadecimal ")
                    numeroConvertido = octalParaHexadecimal(numero)
                    print(f"Legal! O seu numero {numero} em octal para hexadecimal fica: {numeroConvertido}")
                    
               elif escolha == 16 and conversao == 2:
                    numero = input("Digite o seu número em hexadecimal para converter em binario ")
                    numeroConvertido = hexadecimalParaBinario(numero)
                    print(f"Legal! O seu numero {numero} em octal para hexadecimal fica: {numeroConvertido}")
                    
               elif escolha == 16 and conversao == 10:
                    numero = input("Digite o seu número em hexadecimal para converter em decimal ")
                    numeroConvertido = hexadecimalParaDecimal(numero)
                    print(f"Legal! O seu numero {numero} em hexadecimal para decimal fica: {numeroConvertido}")
                    
               elif escolha == 16 and conversao == 8:
                    numero = input("Digite o seu número em hexadecimal para converter em octal ")
                    numeroConvertido = hexadecimalParaOctal(numero)
                    print(f"Legal! O seu numero {numero} em hexadecimal para octal fica: {numeroConvertido}")
                    
               else:
                    print("Segundo valor inválido.")
                    print("Digite novamente.")
                    print("")
               print("Quer fazer outra conversão? [S/N]")
               querFazer = input("").upper()
               if querFazer == "N":
                    break
               elif querFazer == "S":
                    main()
               else:
                    print("Engraçadinho, vou fechar agora p/ você parar de graça! >:(")
                    break
main()