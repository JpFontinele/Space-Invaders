from fase import *

#Funções
janela = Window(800, 600)
janela.set_title("Space Invaders")

#Fundo

fundo = GameImage("fundo.jpg")

#Mouse e teclado

teclas = Window.get_keyboard()
mouse = Window.get_mouse()

#Opções

jogar = Sprite("botao-jogar.png", 1)
dificuldade = Sprite("botao-dificultar.png", 1)
ranking = Sprite("botao-ranking.png", 1)
sair = Sprite("botao-sair.png", 1)

#Dificuldades

facil = Sprite("botao facil.png", 1)
medio = Sprite("botao-medio.png", 1)
dificil = Sprite("botao-dificil.png", 1)

#posição das opções

jogar.x = (janela.width / 2) - jogar.width / 2
jogar.y = janela.height - jogar.height * 5.7

dificuldade.x = (janela.width / 2) - (jogar.width / 2)
dificuldade.y = janela.height - dificuldade.height * 4.2

ranking.x = (janela.width / 2) - (jogar.width / 2)
ranking.y = janela.height - ranking.height * 2.8

sair.x = (janela.width / 2) - (jogar.width / 2)
sair.y = janela.height - sair.height * 1.4

facil.x = (janela.width / 2) - (jogar.width / 2)
facil.y = janela.height - facil.height * 5.5

medio.x = (janela.width / 2) - (jogar.width / 2)
medio.y = janela.height - medio.height * 3.5

dificil.x = (janela.width / 2) - (jogar.width / 2)
dificil.y = janela.height - dificil.height * 1.4

#Pontuação
pontuacao = []


#Gaming looping menu
while True:

    # Se o usario apertar em jogar

    if mouse.is_over_object(jogar) and mouse.is_button_pressed(1):

        # Chama o modulo contendo o gaming loop do jogo

         jogo(1)

    # Se o usario apertar em dificuldade

    if mouse.is_over_object(dificuldade) and mouse.is_button_pressed(1):

        while teclas.key_pressed("esc") == 0: #Se o usario quiser sair antes de selecionar o level do jogo

            if mouse.is_over_object(facil) and mouse.is_button_pressed(1):
                jogo(1)  # Chama o modulo contendo o gaming loop do jogo passando 1 como nivel

            if mouse.is_over_object(medio) and mouse.is_button_pressed(1):
                jogo(2)  # Chama o modulo contendo o gaming loop do jogo passando 2 como nivel

            if mouse.is_over_object(dificil) and mouse.is_button_pressed(1):
                jogo(3)  # Chama o modulo contendo o gaming loop do jogo passando 3 como nivel

            #Desenha na tela os botes de dificuldade
            fundo.draw()
            facil.draw()
            medio.draw()
            dificil.draw()
            janela.update()

     # Caso o usario aperte em ranking
    if mouse.is_over_object(ranking) and mouse.is_button_pressed(1):
        del(pontuacao[:])
        arquivo = open("pontuação.txt", "r", encoding="UTF-8")

        for linha in arquivo:
            pontuacao.append(linha.rstrip())

        arquivo.close()

        tela = 0


        while teclas.key_pressed("esc") == 0:  # Se o usario quiser sair antes de selecionar o level do jogo


            if tela < len(pontuacao):

                for i in range(len(pontuacao)):
                    sorteada = sorted(pontuacao, reverse=True)


                    fundo.draw()

                    try:
                        janela.draw_text(sorteada[0], janela.width / 4, 5, size=100, color=(250, 250, 250), font_name="Arial")
                        janela.draw_text(sorteada[1], janela.width / 4, 110, size=100, color=(250, 250, 250), font_name="Arial")
                        janela.draw_text(sorteada[2], janela.width / 4, 210, size=100, color=(250, 250, 250), font_name="Arial")
                        janela.draw_text(sorteada[3], janela.width / 4, 310, size=100, color=(250, 250, 250), font_name="Arial")
                        janela.draw_text(sorteada[4], janela.width / 4, 410, size=100, color=(250, 250, 250), font_name="Arial")
                        tela += 1

                        janela.update()
                    except:
                        None


            janela.update()

    # Caso o usario aperte em sair finaliza o programa
    if mouse.is_over_object(sair) and mouse.is_button_pressed(1):
        janela.close()

    #Desenha os arquivos do menu
    fundo.draw()
    jogar.draw()
    dificuldade.draw()
    ranking.draw()
    sair.draw()
    janela.update()