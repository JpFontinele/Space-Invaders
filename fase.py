from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from random import randint

def jogo(nivel=1): #Pega os valores de dificuldade, caso o usario nao informe a dificuldade o jogo começa na dificuldade facil

    # Funções
    janela = Window(800, 600)
    janela.set_title("Space Invaders")

    #Teclado
    teclas = Window.get_keyboard()

    # Fundo
    fundo = GameImage("fundo-jogo.jpg")

    # Sprites
    nave = Sprite("aviao.png", 1)
    inimigo1 = Sprite("inimigo1.png", 1)
    inimigo2 = Sprite("inimigo2.png", 1)

    # Posições
    nave.x = (janela.width / 2) - (nave.width / 2)
    nave.y = janela.height - nave.height

    # Velocidades
    velNave = 500
    velTiro = 200
    velInimigo = 0.3
    velTiroInimigo = 0.4

    #Tempo
    inicio = contador = 0
    tempoDeRecarga = 1.2 * nivel
    tempoDeJogo = tempoDeTiro = tempoImortal = tempoPiscador = 0

    #lista
    listaTiroInimigo = []
    listaTiro = []
    listaInimigo = [[], [], []]

    #Distancia
    distancia = inimigo1.width * 2
    distanciaInimigo = inimigo1.width * 2

    #Pontuação
    pontuacao = 0



    #valores
    aumenta = False
    diminui = True
    resete = True
    jogado = False

    # Vida
    vidas = 3
    imortal = False

    while True:


        if teclas.key_pressed("esc") == 1: #Caso o usario aperte esc acaba o gaming looping

            arquivoDeTempo = open("tempo.txt", "w")
            arquivoDeTempo.write(str(tempoDeJogo))
            arquivoDeTempo.close()

            return

        fundo.draw()

        if resete:
            # Monstros
            for i in range(6):  # Coloca 6 monstros em cada fileira

                listaInimigo[0].append(Sprite("inimigo1.png", 1))
                listaInimigo[1].append(Sprite("inimigo2.png", 1))
                listaInimigo[2].append(Sprite("inimigo3.png", 1))


                listaInimigo[0][i].x = distanciaInimigo
                listaInimigo[0][i].y = inimigo2.height * 2

                listaInimigo[1][i].x = distanciaInimigo
                listaInimigo[1][i].y = inimigo2.height

                listaInimigo[2][i].x = distanciaInimigo
                listaInimigo[2][i].y = 0

                distanciaInimigo += distancia

                resete = False

        # Controles

        if teclas.key_pressed("A"): #Nave vai pra esquerda
            nave.x -= velNave * janela.delta_time() #Velocidade do aviao

            if nave.x < 0: #Se bater na parede esquerda
                nave.x = janela.width - nave.width

        if teclas.key_pressed("D"):
            nave.x += velNave * janela.delta_time() #Velocidade do aviao

            if nave.x + nave.width > janela.width: #Se bater na parede direita
                nave.x = 0

        # Se ele apertar o botao do tiro

        if teclas.key_pressed("space") and int(contador) == 0:
            #Tempo de recarga
            inicio = 1
            contador = tempoDeRecarga

            #Lista do tiro
            listaTiro.append(Sprite("tiro.png", 1))

            #Posição do tiro
            listaTiro[len(listaTiro) - 1].x = nave.x + 30
            listaTiro[len(listaTiro) - 1].y = nave.y

        #Se a horda acabar
        if len(listaInimigo[0]) == 0 and len(listaInimigo[1]) == 0 and len(listaInimigo[2]) == 0:
            velInimigo = 0.2
            velInimigo += 0.01
            distanciaInimigo = inimigo1.width * 2
            resete = True

        # Movimentação dos montros

        tempoDeTiroA = randint(2, 5)
      
        for i in listaInimigo:

            for j in i:

                # Todos os inimigos
                inimigos = j
           

                # Desenha os inimigos
                inimigos.draw()

                #Se colidir com a nave
                if inimigos.collided(nave):
                    arquivo = open("pontuação.txt", "a", encoding="UTF-8")
                    arquivo.write(str(pontuacao))
                    arquivo.write(" ")
                    arquivo.write(" - ")
                    arquivo.write(input("Digite seu nome: "))
                    arquivo.write("\n")

                    arquivo.close()
                    return None

                #Posições de batidas
                if len(listaInimigo[2]) != 0: #Se ainda tiver monstros na ultima fileira
                    esquerda = listaInimigo[2][0]
                    direita = listaInimigo[2][-1]
                else:
                    if len(listaInimigo[1]) != 0: #Se ainda tiver monstros na  fileira do meio
                        esquerda = listaInimigo[1][0]
                        direita = listaInimigo[1][-1]
                    else:
                        if len(listaInimigo[0]) != 0: #Se ainda tiver monstros na primeira fileira
                            esquerda = listaInimigo[0][0]
                            direita = listaInimigo[0][-1]

                # Velocidade dos inimigos de um lado pro outro
                inimigos.x += velInimigo

                if direita.x + direita.width >= janela.width:  # Se bater na direita
                    diminui = True
                    aumenta = False
                    direita.x += velInimigo * -1
                    velInimigo *= -1

                    for l in range(len(listaInimigo[0])):
                        listaInimigo[0][l].y += 40

                    for l in range(len(listaInimigo[1])):
                        listaInimigo[1][l].y += 40

                    for l in range(len(listaInimigo[2])):
                        listaInimigo[2][l].y += 40

                if esquerda.x <= 0:  # Se bater na esquerda
                    aumenta = True
                    diminui = False
                    esquerda.x += velInimigo * -1
                    velInimigo *= -1

                    for l in range(len(listaInimigo[0])):
                            listaInimigo[0][l].y += 40

                    for l in range(len(listaInimigo[1])):
                        listaInimigo[1][l].y += 40

                    for l in range(len(listaInimigo[2])):
                        listaInimigo[2][l].y += 40

                # Tiros dos montros

                if int(tempoDeTiro) == tempoDeTiroA:

                    # Lista de tiro
                    listaTiroInimigo.append(Sprite("tiro.png", 1))

                    # Posição do tiro

                    try:

                        larguraDoTiro = listaInimigo[2][randint(0, 5)].x + 20
                        alturaDoTiro = listaInimigo[randint(0, 2)][randint(0, 5)].y + 20

                        listaTiroInimigo[len(listaTiroInimigo) - 1].x = larguraDoTiro
                        listaTiroInimigo[len(listaTiroInimigo) - 1].y = alturaDoTiro
                        tempoDeTiro = 0

                    except:
                        listaTiroInimigo[len(listaTiroInimigo) - 1].x = inimigos.x + 20
                        listaTiroInimigo[len(listaTiroInimigo) - 1].y = inimigos.y + 20
                        tempoDeTiro = 0

        #Tiros Inimigos

        if tempoDeTiro > 5:
            tempoDeTiro = 0

        for tiroI in listaTiroInimigo:

            # Velocidade dos tiros
            tiroI.y += velTiroInimigo

            # Desenha os tiros
            tiroI.draw()

            #Se o tiro sair da tela
            if tiroI.y + tiroI.height < 0:
                listaTiroInimigo.remove(tiroI)

            #Se o tiro acertar a nave
            if tiroI.collided(nave):
                listaTiroInimigo.remove(tiroI)

                if not imortal:

                    vidas -= 1

                    #Coloca no meio
                    nave.x = (janela.width / 2) - (nave.width / 2)
                    nave.y = janela.height - nave.height
                    imortal = True

        #Tiros

        for i in listaTiro:
            i.y -= velTiro * janela.delta_time()
            i.draw() #Desenha os tiros
            if i.y + i.height < 0:
                listaTiro.remove(i)

            for k in listaInimigo:
                for j in k:

                    inimigos = j #Todos os inimigos
                    if i != 0:
                        if inimigos.collided(i):
                            if aumenta:
                                velInimigo += 0.01
                            if diminui:
                                velInimigo -= 0.01

                            velTiroInimigo += 0.05

                            k.remove(inimigos)
                            listaTiro.remove(i)
                            i = 0
                            pontuacao += 10


        #Contagem

        if int(tempoDeTiro) == tempoDeTiroA:

            tempoDeTiro = 0

        if inicio == 1 and int(contador) > 0:

            contador -= janela.delta_time()

        tempoDeJogo += janela.delta_time()


        tempoDeTiro += janela.delta_time()

        #Imortalidade
        if imortal:
            tempoImortal += janela.delta_time()

            #Pisca a nave
            tempoPiscador += janela.delta_time()

            if round(tempoPiscador, 2) < 0.01:

                piscador = True
            else:
                piscador = False
                tempoPiscador = 0


            #Tempo imortal
            if int(tempoImortal) == 2:
                tempoImortal = 0
                imortal = False
        else:
            piscador = False

        if not piscador:
            nave.draw()

        #Se perder
        if vidas == 0:
            arquivo = open("pontuação.txt", "a", encoding="UTF-8")
            arquivo.write(str(pontuacao))
            arquivo.write(" ")
            arquivo.write(" - ")
            arquivo.write(input("Digite seu nome: "))
            arquivo.write("\n")

            arquivo.close()

            return None

        janela.draw_text("Vidas:", 2, 0, size=20,color=(250, 250, 250), font_name="Arial")
        janela.draw_text(str(vidas), 50, 0,  size=20,color=(250, 250, 250), font_name="Arial")

        janela.draw_text("PONTUAÇÃO:", janela.width - janela.width / 3 + 100, janela.height - janela.height, size=20,color=(250, 250, 250), font_name="Arial")
        janela.draw_text(str(pontuacao), janela.width - janela.width / 3 + 220, janela.height - janela.height, size=20, color=(250, 250, 250), font_name="Arial")

        janela.update()