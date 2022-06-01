import cv2
import numpy as np

def pipeline(img):
    # Definindo uma largura e altura
    imagemRedimensionada = cv2.resize(img, (640, 480))

    # Cortando a imagem em 25% de baixo pra cima.
    imagemCortada = imagemRedimensionada[0:360, :]

    # Convertendo a imagem para o formato HLS
    imagemHLS = cv2.cvtColor(imagemCortada, cv2.COLOR_BGR2HLS)

    # Aplicando um filtro de suavização - filtro média
    imagemSuavizada = cv2.blur(imagemHLS, (31, 31))

    # aplicando uma mascara - segmentação
    lower = np.array([25, 17, 0])
    upper = np.array([177, 255, 255])

    mask = cv2.inRange(imagemSuavizada, lower, upper)

    # aplicando dilatação e erosão - closing
    Kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (70, 70))  # 10,10

    mask_dilatacao = cv2.dilate(mask, Kernel, iterations=1)
    mask_erosao = cv2.erode(mask_dilatacao, Kernel, iterations=1)

    margem = 100
    X = 90
    Y = 320

    contadorDeTransicao = 0
    indicePrimeiratransicao = 0
    indiceSegundatransicao = 0

    for i in range(638):
        if (mask_erosao[X][i] != mask_erosao[X][i+1]):
            contadorDeTransicao += 1
            if (contadorDeTransicao == 1):
                indicePrimeiratransicao = i
            if (contadorDeTransicao == 2):
                indiceSegundatransicao = i
                break

    Y2 = ((indiceSegundatransicao - indicePrimeiratransicao) / 2) + indicePrimeiratransicao
    Y2 = int(Y2)

    ya = Y - margem
    yb = Y + margem


    if(Y2 > yb):
        print("Mais para a esquerda")
    if(Y2 < ya):
        print("Mais para a direita")
    if(Y2 <= yb and Y2 >= ya):
        print("Está no centro")

    print(X)
    print(Y2)

    mask_rgb = cv2.merge([mask_erosao, mask_erosao, mask_erosao])
    mask_rgb2 = cv2.circle(mask_rgb, (Y2, X), radius=6, color=(0, 0, 255), thickness=-1)

    # Adicionando linhas na direita e na esquerda
    cv2.line(mask_rgb2, (ya, 0), (ya, 359), (255, 0, 0), 4)
    cv2.line(mask_rgb2, (yb, 0), (yb, 359), (255, 0, 255), 4)

    # linha seguidora
    cv2.line(mask_rgb2, (Y2, 97), (320, 350), (0, 255, 255), 4)
    cv2.circle(mask_rgb2, (320, 355), radius=6, color=(0, 0, 200), thickness=-1)


    # adiciona uma borda na imagem
    cv2.rectangle(mask_rgb2, (0, 360), (638, 0), (255, 255, 0), 4)

    cv2.imshow("Imagem com ponto vermelho", mask_rgb2)

"""imagem = cv2.imread("../Imagens/Imagem4.jpeg")

pipeline(imagem)

cv2.waitKey(0)
cv2.destroyAllWindows() """

cap = cv2.VideoCapture('../Imagens/video.mp4')

if (cap.isOpened() == False):
    print("Erro ao abrir o arquivo de vídeo.")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        #cv2.imshow("Frame", frame)
        pipeline(frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
           break


cap.release()

cv2.destroyAllWindows()


