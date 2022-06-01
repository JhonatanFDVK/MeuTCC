import cv2
import numpy as np


def empty(a):
    pass


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("H min", "TrackBars", 25, 179, empty)
cv2.createTrackbar("H max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("S min", "TrackBars", 17, 179, empty)
cv2.createTrackbar("S max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("L min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("L max", "TrackBars", 255, 255, empty)


while True:
    # Lendo as imagens
    imagem1 = cv2.imread("../Imagens/Imagem1.jpeg")
    imagem2 = cv2.imread("../Imagens/Imagem2.jpeg")
    imagem3 = cv2.imread("../Imagens/Imagem3.jpeg")
    imagem4 = cv2.imread("../Imagens/Imagem4.jpeg")
    imagem5 = cv2.imread("../Imagens/Imagem5.jpeg")
    imagem6 = cv2.imread("../Imagens/Imagem6.jpeg")


    # Definindo largura e altura
    imagemRedimensionada1 = cv2.resize(imagem1, (640, 480))
    imagemRedimensionada2 = cv2.resize(imagem2, (640, 480))
    imagemRedimensionada3 = cv2.resize(imagem3, (640, 480))
    imagemRedimensionada4 = cv2.resize(imagem4, (640, 480))
    imagemRedimensionada5 = cv2.resize(imagem5, (640, 480))
    imagemRedimensionada6 = cv2.resize(imagem6, (640, 480))


    # Cortando 25% das imagens de baixo pra cima
    imagemCortada1 = imagemRedimensionada1[0:360, : ]
    imagemCortada2 = imagemRedimensionada2[0:360, : ]
    imagemCortada3 = imagemRedimensionada3[0:360, : ]
    imagemCortada4 = imagemRedimensionada4[0:360, : ]
    imagemCortada5 = imagemRedimensionada5[0:360, : ]
    imagemCortada6 = imagemRedimensionada6[0:360, : ]


    # Convertendo as imagens para o formato HLS
    imagemHLS1 = cv2.cvtColor(imagemCortada1, cv2.COLOR_BGR2HLS)
    imagemHLS2 = cv2.cvtColor(imagemCortada2, cv2.COLOR_BGR2HLS)
    imagemHLS3 = cv2.cvtColor(imagemCortada3, cv2.COLOR_BGR2HLS)
    imagemHLS4 = cv2.cvtColor(imagemCortada4, cv2.COLOR_BGR2HLS)
    imagemHLS5 = cv2.cvtColor(imagemCortada5, cv2.COLOR_BGR2HLS)
    imagemHLS6 = cv2.cvtColor(imagemCortada6, cv2.COLOR_BGR2HLS)

    # Aplicando filtro de suavização

    # Filtro de mediana
    #imagemTratada1 = cv2.medianBlur(imagemCortadaHLS1, 5)
    #imagemTratada2 = cv2.medianBlur(imagemCortadaHLS2, 5)
    #imagemTratada3 = cv2.medianBlur(imagemCortadaHLS3, 5)

    # Filtro bilateral
    #imagemTratada1 = cv2.bilateralFilter(imagemCortadaHLS1, 9, 75, 75)
    #imagemTratada2 = cv2.bilateralFilter(imagemCortadaHLS2, 9, 75, 75)
    #imagemTratada3 = cv2.bilateralFilter(imagemCortadaHLS3, 9, 75, 75)

    # Filtro gaussiano
    #imagemTratada1 = cv2.GaussianBlur(imagemCortadaHLS1, (5,5), 0)
    #imagemTratada2 = cv2.GaussianBlur(imagemCortadaHLS2, (5,5), 0)
    #imagemTratada3 = cv2.GaussianBlur(imagemCortadaHLS3, (5,5), 0)

    # Filtro de média
    imagemSuavizada1 = cv2.blur(imagemHLS1, (31, 31))
    imagemSuavizada2 = cv2.blur(imagemHLS2, (31, 31))
    imagemSuavizada3 = cv2.blur(imagemHLS3, (31, 31))
    imagemSuavizada4 = cv2.blur(imagemHLS4, (31, 31))
    imagemSuavizada5 = cv2.blur(imagemHLS5, (31, 31))
    imagemSuavizada6 = cv2.blur(imagemHLS6, (31, 31))

    h_min = cv2.getTrackbarPos("H min", "TrackBars")
    h_max = cv2.getTrackbarPos("H max", "TrackBars")
    s_min = cv2.getTrackbarPos("S min", "TrackBars")
    s_max = cv2.getTrackbarPos("S max", "TrackBars")
    l_min = cv2.getTrackbarPos("L min", "TrackBars")
    l_max = cv2.getTrackbarPos("L max", "TrackBars")

    print(h_min, h_max, s_min, s_max, l_min, l_max)
    
    lower = np.array([h_min, s_min, l_min])
    upper = np.array([h_max, s_max, l_max])

    # Aplicando uma máscara em todas as imagens
    mask1 = cv2.inRange(imagemSuavizada1, lower, upper)
    mask2 = cv2.inRange(imagemSuavizada2, lower, upper)
    mask3 = cv2.inRange(imagemSuavizada3, lower, upper)
    mask4 = cv2.inRange(imagemSuavizada4, lower, upper)
    mask5 = cv2.inRange(imagemSuavizada5, lower, upper)
    mask6 = cv2.inRange(imagemSuavizada6, lower, upper)

    # Aplicando dilatação e erosão
    Kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (60, 60))

    mask1_dilatacao = cv2.dilate(mask1, Kernel, iterations=1)
    mask1_erosao = cv2.erode(mask1_dilatacao, Kernel, iterations=1)
    mask2_dilatacao = cv2.dilate(mask2, Kernel, iterations=1)
    mask2_erosao = cv2.erode(mask2_dilatacao, Kernel, iterations=1)
    mask3_dilatacao = cv2.dilate(mask3, Kernel, iterations=1)
    mask3_erosao = cv2.erode(mask3_dilatacao, Kernel, iterations=1)
    mask4_dilatacao = cv2.dilate(mask4, Kernel, iterations=1)
    mask4_erosao = cv2.erode(mask4_dilatacao, Kernel, iterations=1)
    mask5_dilatacao = cv2.dilate(mask5, Kernel, iterations=1)
    mask5_erosao = cv2.erode(mask5_dilatacao, Kernel, iterations=1)
    mask6_dilatacao = cv2.dilate(mask6, Kernel, iterations=1)
    mask6_erosao = cv2.erode(mask6_dilatacao, Kernel, iterations=1)
    
    # Destacando o original da imagem onde a parte branca prevaleceu
    imagemDestacada1 = cv2.bitwise_and(imagemCortada1, imagemCortada1, mask=mask1_erosao)
    imagemDestacada2 = cv2.bitwise_and(imagemCortada2, imagemCortada2, mask=mask2_erosao)
    imagemDestacada3 = cv2.bitwise_and(imagemCortada3, imagemCortada3, mask=mask3_erosao)
    imagemDestacada4 = cv2.bitwise_and(imagemCortada4, imagemCortada4, mask=mask4_erosao)
    imagemDestacada5 = cv2.bitwise_and(imagemCortada5, imagemCortada5, mask=mask5_erosao)
    imagemDestacada6 = cv2.bitwise_and(imagemCortada6, imagemCortada6, mask=mask6_erosao)

    # Mostrando as imagens com a mascara
    cv2.imshow("Mask 1", mask1_erosao)
    cv2.imshow("Mask 2", mask2_erosao)
    cv2.imshow("Mask 3", mask3_erosao)
    cv2.imshow("Mask 4", mask4_erosao)
    cv2.imshow("Mask 5", mask5_erosao)
    cv2.imshow("Mask 6", mask6_erosao)

    # Mostrando as imagens com a área original destacada onde o branco da mascara foi aplicado. 
    cv2.imshow("Imagem destacada 1", imagemDestacada1)
    cv2.imshow("Imagem destacada 2", imagemDestacada2)
    cv2.imshow("Imagem destacada 3", imagemDestacada3)
    cv2.imshow("Imagem destacada 4", imagemDestacada4)
    cv2.imshow("Imagem destacada 5", imagemDestacada5)
    cv2.imshow("Imagem destacada 6", imagemDestacada6)
    
    cv2.waitKey(1)