
import cv2
import numpy as np
from opcua import Client

# Configurações
TAMANHO_KERNEL = 9
URL = "https:// CAMERAIP" 
THRESHOLD_DETECCAO = 500

# Conexão
URL_OPC = "opc.tcp:// SEU SERVIDOR OPCUA"
client = Client(URL_OPC)
client.connect()

#Nós
node_verde = client.get_node("ns=4;s=|var|CODESYS Control Win V3.Application.GVL.DETECTA_VERDE")
node_vermelho = client.get_node("ns=4;s=|var|CODESYS Control Win V3.Application.GVL.DETECTA_VERMELHO")

cap = cv2.VideoCapture(URL)
print("Sistema iniciado. Pressione 'q' para sair.")

if not client.connect():
    print("Conexão perdida!")

while True:
    
    sucesso, frame = cap.read() 
    if not sucesso:
        continue # Tenta capturar o próximo frame em vez de fechar
    
    frame_pequeno = cv2.resize(frame, (0, 0), fx=0.3, fy=0.3) #define tamanho do frame
    frame_filtrado = cv2.medianBlur(frame_pequeno, TAMANHO_KERNEL) #filtro mediana
    hsv = cv2.cvtColor(frame_filtrado, cv2.COLOR_BGR2HSV)# conversão para hsv
    
    #faixa de cores
    mascara_vermelha = cv2.inRange(hsv, np.array([165, 50, 50]), np.array([179, 255, 255]))
    mascara_verde = cv2.inRange(hsv, np.array([35, 50, 50]), np.array([85, 255, 255]))

    #detecta se pixels maior que 500
    tem_vermelho = cv2.countNonZero(mascara_vermelha) > THRESHOLD_DETECCAO
    tem_verde = cv2.countNonZero(mascara_verde) > THRESHOLD_DETECCAO

    # Muda estado dos contatos 
    node_verde.set_value(tem_verde)
    node_vermelho.set_value(tem_vermelho)

    # desenha contorno vermelho
    if tem_vermelho:
        contornos, _ = cv2.findContours(mascara_vermelha, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in contornos:
            if cv2.contourArea(c) > THRESHOLD_DETECCAO:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame_pequeno, (x, y), (x + w, y + h), (0, 0, 255), 2)

    #desenha contorno verde
    if tem_verde:
        contornos, _ = cv2.findContours(mascara_verde, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in contornos:
            if cv2.contourArea(c) > THRESHOLD_DETECCAO:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame_pequeno, (x, y), (x + w, y + h), (0, 255, 0), 2)

    #exibe frame
    cv2.imshow("Original", frame_pequeno)
    #aguarda q para fechar
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
#limpa memória 
client.disconnect()
cap.release()
cv2.destroyAllWindows()
