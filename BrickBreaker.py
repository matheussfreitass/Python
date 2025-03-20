import pygame

#inicializar
pygame.init()

tamanho_tela=(800,800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Brick Breaker")

tamanho_bola = 15
bola = pygame.Rect(100,500,tamanho_bola,tamanho_bola)
tamanho_jogador=100
jogador = pygame.Rect(0,750,tamanho_jogador,15)

qtde_blocos_linha=8
qtde_linhas_blocos= 5

qtde_total_blocos = qtde_blocos_linha * qtde_linhas_blocos

def criar_blocos(qtde_blocos_linha,qtde_linhas_blocos):
    altura_tela = tamanho_tela[1]
    largura_tela = tamanho_tela[0]
    distancia_entre_blocos = 5
    largura_bloco= largura_tela/8 - distancia_entre_blocos
    altura_bloco = 15
    distacia_entre_linhas = altura_bloco+10
    blocos=[]

    #criar os blocos
    for j in range(qtde_linhas_blocos):
        for i in range(qtde_blocos_linha):
            #cria bloco
            bloco=pygame.Rect(i * (largura_bloco + distancia_entre_blocos),j* distacia_entre_linhas,largura_bloco,altura_bloco)
            #ADICIONA bloco na lista
            blocos.append(bloco)
    return blocos

#RGB
cores = {
    "branco": (255,255,255),
    "preto":(0,0,0),
    "amarelo": (255,255,0),
    "azul": (0,0,255),
    "verde":(0,255,0)
}
fim_jogo = False
pontuacao = 0
movimento_bola=[1,-1]




#desenhas as coisas na tela
def desenhar_inicio_jogo():
    tela.fill(cores["preto"])
    pygame.draw.rect(tela,cores["azul"],jogador)
    pygame.draw.rect(tela,cores["branco"],bola)

def desenhar_blocos(blocos):
    for bloco in blocos:
        pygame.draw.rect(tela,cores['verde'],bloco)


#criar um loop infinito

#criar funções do jogo
def movimentar_jogador(evento):
    if evento.type == pygame.KEYDOWN:
        if evento.key ==pygame.K_RIGHT:
            if jogador.x + tamanho_jogador < tamanho_tela[0]:
                jogador.x = jogador.x+2
        if evento.key == pygame.K_LEFT:
            if jogador.x > 0 :
                jogador.x = jogador.x-2

    pass

def movimentar_bola(bola):
    movimento = movimento_bola
    bola.x = bola.x + movimento[0]
    bola.y = bola.y + movimento[1]

    if bola.x <= 0:
        movimento[0] = -movimento[0]
    if bola.y <=0 :
        movimento[1] = -movimento[1]
    if bola.x + tamanho_bola >= tamanho_tela[0]:
        movimento[0] =- movimento[0]
    if bola.y + tamanho_bola >= tamanho_tela[1]:
        movimento = None

    if jogador.collidepoint(bola.x,bola.y):
        movimento[1] = - movimento[1]
    for bloco in blocos:
        if bloco.collidepoint(bola.x,bola.y):
            blocos.remove(bloco)
            movimento[1] = - movimento[1]

    return  movimento
    pass
def atualizar_pontaucao(pontuacao):
    fonte = pygame.font.Font(None,30)
    texto = fonte.render(f"Pontuacao: {pontuacao}", 1 , cores["amarelo"])
    tela.blit(texto, (0,780))
    if pontuacao >= qtde_total_blocos:
        return True
    else:
        return False
    pass

blocos = criar_blocos(qtde_blocos_linha,qtde_linhas_blocos)

while not fim_jogo:
    desenhar_inicio_jogo()
    desenhar_blocos(blocos)
    fim_jogo = atualizar_pontaucao(qtde_total_blocos - len(blocos))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = TRUE

    if not movimento_bola:
        fim_jogo= true
    movimentar_jogador(evento)
    movimento_bola = movimentar_bola(bola)
    pygame.time.wait(1)
    pygame.display.flip()

pygame.quit()