#Ex 1
num1 =  int(input('Informe o Primeiro número: '))
num2 =  int(input('Informe o Segundo número: '))
soma = num1 + num2
subt = num1 - num2
mult = num1 * num2
div = num1 / num2
divint = num1 // num2
print(f"Soma: ",soma)
print(f"Subtração: ",subt)
print(f"Multiplicação: ",mult)
print(f"Divisão: ",div)
print(f"Divisão inteira: ",divint)


#Ex 2
mins = int(input('Indique a quantidade de minutos: '))

if (mins >= 60):
    hours = mins // 60
    minsafterhour = mins % 60
    print(hours,f"hora(s):",minsafterhour, "minutos")
elif((mins<60)and(mins>0)):
    print( f"Tempo introduzido", 0,":",mins, "minutos")
else:
    print("Tempo introduzido 0 minutos, insira um tempo válido")


    #Ex 3
nome1 = str(input("Digite o primeiro nome: "))
nome2 = str(input("Digite o segundo nome: "))

nom1 = nome1[nome1.count(nome1)-3] + nome1[::-1]
nom2 = nome2[nome2.count(nome2)-2] + nome2[::-1]

print("Nome: ", nom1, nom2)



#Ex 4

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

op = str(input("Digite o operador ((+), (-), (*), (/) sem parêntesis): "))

def operacoes(op):
    result = 0
    if(op == "+"):result = a + b
    elif(op == "-"): result =  a - b
    elif(op == "*"): result = a * b
    else:
       result = a / b
    return result

print("Resultado: ",operacoes(op))



#Ex 5

nome = str(input("Digite seu nome : "))
sobrenome = str(input("Digite seu Sobrenome: "))

print("Olá", nome, sobrenome +",","saudações")



#Ex 6
import random

num = random.randint(1,10)

user = int(input("Digite o numero que acha que estou pensando entre 1 e 10: "))
tentativas = 0

while tentativas < 3:

  if ((user >= 1 and user <= 10) and user >= num + 3 and user != num + 2 and user != num + 1):
    print("Muito alto")
    tentativas = tentativas + 1
    user = int(input("Digite o numero que acha que estou pensando entre 1 e 10: "))

  elif((user >= 1 and user <= 10) and user >= num + 2 and user != num + 3 and user != num + 1):
    print("Ainda um pouco alto")
    tentativas = tentativas + 1
    user = int(input("Digite o numero que acha que estou pensando entre 1 e 10: "))

  elif(((user >= 1 and user <= 10) and user >= num + 1 and user != num + 2 and user != num + 3) and tentativas < 3):
    print("Quase, mas Não acertou")
    tentativas = tentativas + 1
    user = int(input("Digite o numero que acha que estou pensando entre 1 e 10: "))


  if ((user >= 1 and user <= 10) and user <= num - 3 and user != num - 2 and user != num - 1):
    print("Muito Baixo")
    tentativas = tentativas + 1
    user = int(input("Digite o numero que acha que estou pensando entre 1 e 10: "))


  elif((user >= 1 and user <= 10) and user <= num - 2 and user != num - 3 and user != num - 1):
    print("Ainda um pouco baixo")
    tentativas = tentativas + 1
    user = int(input("Digite o numero que acha que estou pensando entre 1 e 10: "))


  elif((user >= 1 and user <= 10) and user <= num - 1 and user != num - 2 and user != num - 3):
    print("Quase, mas Não acertou")
    tentativas = tentativas + 1
    user = int(input("Digite o numero que acha que estou pensando entre 1 e 10: "))

  elif(user == num):
      print (f"Acertou o numero é "+ str(num) +"!!!")
      print("Parabens")
      tentativas = 3

  elif(user < 1 or user > 10):
      print("O numero digitado não esta no intervalo 1 a 10 ")
      tentativas = tentativas + 1
      user = int(input("Digite o numero que acha que estou pensando entre 1 e 10: "))

  if (tentativas == 2 and user != num):
        print("Você não acertou o numero era ", num)
        tentativas = tentativas + 1



#EX 7
peso = float(input("Digite o peso em Kilogramas: "))
altura = float(input("Digite a altura em Metros: "))
imc = peso / (altura * altura)
imcDesejado = 22
pesoDesejado = imcDesejado * (altura * altura)

difpeso = peso - pesoDesejado

if imc > 40.0:
  print ("Obesidade III, você tem uma diferencia de "+str(round(difpeso,2))+" kg acima do desejado ("+str(round(pesoDesejado,2))+" kg)")
elif(imc < 39.9) and (imc > 35.0):
  print ("Obesidade II, você tem uma diferencia de "+str(round(difpeso,2))+" kg acima do desejado ("+str(round(pesoDesejado,2))+"kg)")
elif (imc < 34.9) and (imc > 30.0 ):
   print ("Obesidade I, você tem uma diferencia de "+str(round(difpeso,2))+" kg acima do desejado ("+str(round(pesoDesejado,2))+"kg)")
elif(imc < 29.9) and (imc > 25.0):
  print ("Sobrepeso, você tem uma diferencia de "+str(round(difpeso,2))+" kg acima do desejado ("+str(round(pesoDesejado,2))+"kg)")
elif (imc < 29.9) and (imc > 25.0):
  print ("Normal")
elif (imc < 24.9) and (imc > 18.6):
  print ("Normal")
elif (imc > 18.5):
  print ("Abaixo do normal")



  #Ex 8
idade = int(input("Digite sua idade: "))

if(idade >= 18 and idade <= 120):
  print("Você é Maior de Idade")
elif(idade > 120):
  print("Idade fora dos parametros para humanos reais")
else:
  print("Você NÃO é Maior de Idade")




#Ex 9
def compra_com_desconto(compra_value):
    if compra_value >= 200:
        desconto = 0.20
        print("Desconto:", str(desconto *100) +"%")
    elif compra_value >= 200:
        desconto = 0.15
        print("Desconto:"+ str(desconto *100) + "%")
    elif compra_value >= 100:
        desconto = 0.10
        print("Desconto:", str(desconto *100) + "%")
    else:
        desconto = 0
        print("Sem Desconto.")

    return compra_value - (compra_value * desconto)

compra_value = float(input("Digite o valor da compra: R$ "))

valor_com_desconto = compra_com_desconto(compra_value)

print(f"O valor da compra com desconto é de R$ {valor_com_desconto:.2f}")




#Ex 10

import random

personagens = ['Kim', 'Mya', 'Belatrix', 'Layla', 'Conde Claude']
acoes = ['caminhava plácidamente', 'escapava de um dragão furioso', 'praticava a meditação profunda', 'empunhava a espada contra o escuro cabalheiro', 'estava ajudando um viajante perdido']
locais = ['na ponte de cristal da floresta encantada', 'no castelo abandonado', 'nas montanhas geladas', 'no deserto gélido de Gerudo', 'no portal do tempo na ilha misteriosa']
circunstancias = ['quando de repente apareceu o alquimista e disse -"Quanto tempo... Finalmente o momento chegou... e você é o escolhido para esta batalha final"',f'e nesse momento ouviu uma voz que se aproximava...-"Quanto precisa um cabalheiro para considerar sua vida de menos valor que a sua missão?" -Era {random.choice(personagens)} que se aproximava com toda vontade de terminar de uma vez por todas com as pendencias do passado', f'. O momento era o menos esperado mas o cheiro de problemas estava forte o suficiente para saber que era naquele dia que iria acabar com o caos gerado por {random.choice(personagens)})']

personagem = random.choice(personagens)
acao = random.choice(acoes)
local = random.choice(locais)
circunstancia =  random.choice(circunstancias)

historia = f"{personagem} {acao} {local} {circunstancia}."


print("História curiosa:")
print(historia)




#Ex 11
import random

def lancar_dado():
    return random.randint(1, 6)


lancamentos = int(input("Quantos dados você gostaria de lançar? "))

lancada = 0

print("Resultado do(s) lançamento(s):")

while (lancada < lancamentos):
    resultado = lancar_dado()
    print(f"Dado {lancada + 1}: Caiu em {resultado}")
    lancada += 1




#Ex 12

def palavras_clasificadas(palavras):
    curtas = []
    longas = []

    for palavra in palavras:
        if len(palavra) < 5:
            curtas.append(palavra)
        else:
            longas.append(palavra)

    return curtas, longas

entrada = input("Digite algumas palavras separadas por espaço: ")

lista_palavras = entrada.split()

curtas, longas = palavras_clasificadas(lista_palavras)

print("Palavras curtas:", str(curtas).replace('[', '').replace(']', '').replace("'", ""))
print("Palavras longas:", str(longas).replace('[', '').replace(']', '').replace("'", ""))



#Ex 13
def is_palindromo(texto):
  texto_desformatado = texto.replace(" ", "").replace(",","").replace(".","").replace("-","").replace("ô","o").replace("ê","e").replace("â","a").replace("í","i").replace("û","u").replace("á","a").replace("é","e").replace("ó","o").replace("ú","u").lower()
  return texto_desformatado == texto_desformatado[::-1]

text = str(input("Digite a palavra ou frase a verificar se é palindromo: "))

if is_palindromo(text):
  print("Este texto é palíndromo")
else:
  print("Este texto *NÃO* é palíndromo")



#Ex 14

def contagem_votacao():
   
    votos_opcao1 = 0
    votos_opcao2 = 0
    votos_opcao3 = 0

    
    while True:
        print("Opções de voto:")
        print("1. Opção 1: (Vermelho)")
        print("2. Opção 2: (Azul)")
        print("3. Opção 3: (Verde)")
        print("0. Encerrar votação")

        voto = input("Digite o número da sua opção de voto: ")

        
        if voto == '0':
            break

        
        if voto == '1':
            votos_opcao1 += 1
        elif voto == '2':
            votos_opcao2 += 1
        elif voto == '3':
            votos_opcao3 += 1
        else:
            print("Opção inválida!")

    
    print("\nResultados da votação:")
    print("Opção 1:", votos_opcao1, "votos")
    print("Opção 2:", votos_opcao2, "votos")
    print("Opção 3:", votos_opcao3, "votos")


contagem_votacao()




#Ex 15

def historia():
    print("Bem-vindo à aventura!")
    print("Você acorda em uma sala estranhamente decorada, com móveis antigos e tapeçarias coloridas. À sua frente, há duas portas.Você anda até ")
    print("1. A porta da esquerda")
    print("2. A porta da direita")

    escolha1 = input("Digite o número da sua escolha: ")

    if escolha1 == '1':
        print("\nVocê escolhe a porta da esquerda. Encontra ao abrir a porta da esquerda, um corredor escuro.. O que você faz?")
        print("1. Seguir em frente pelo corredor..")
        print("2. Voltar e abrir a outra porta.")

        escolha2 = input("Digite o número da sua escolha: ")

        if escolha2 == '1':
            print("\nVocê avança pelo corredor escuro, iluminando o caminho com uma lanterna que você encontrou. No final do corredor, você descobre uma sala secreta cheia de tesouros antigos. Parabéns, você encontrou o tesouro escondido!!")
        elif escolha2 == '2':
            print("\nVocê decide não arriscar seguir pelo corredor escuro e volta para a sala principal. Ao abrir a outra porta, você se depara com um jardim exuberante. Você decide explorar o jardim e confiado vai correndo ate o final do jardim, infelizmente existe um precipicio e você não cai, mas agora com a porta fechada por completo não conseguira voltar e viverá aqui para sempre")
        else:
            print("\nEscolha inválida! Fim da aventura.")

    elif escolha1 == '2':
        print("\nVocê decide abrir a porta da direita, e se depara com uma escadaria que desce para um porão misterioso.")
        print("1. Descer a escadaria para explorar o porão.")
        print("2. Voltar e abrir a outra porta.")

        escolha3 = input("Digite o número da sua escolha: ")

        if escolha3 == '1':
            print("\nVocê desce as escadas para o porão misterioso. Lá embaixo, você encontra uma sala sombria com uma única caixa de madeira no centro. Curioso, você abre a caixa e encontra um milhão de reais ocultos na caixa. Parabéns, você desvendou um mistério e ganhou 1 🌽!!")
        elif escolha3 == '2':
            print("\nVocê decide não arriscar explorar o porão misterioso e volta para a sala principal. Ao abrir a outra porta, você se depara com uma biblioteca antiga. Você decide passar um tempo explorando os livros e encontra uma nota que diz 'afortunado e desafortunado quem nesta sala tenha entrado, pois terá o conhecimento do mundo a disposição, mas nunca sairá desta casa, em compensação. Apenas quando o proximo jogador chegar terá a sua liberdade' ")
        else:
            print("\nEscolha inválida! Fim da aventura.")

    else:
        print("\nEscolha inválida! Fim da aventura.")


historia()