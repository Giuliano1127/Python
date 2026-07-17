# Sistema de Visão Computacional (OpenCV + OPC UA)

Sistema desenvolvido em **Python** utilizando **OpenCV** para detecção de objetos coloridos em tempo real e comunicação com um **PLC** através do protocolo **OPC UA**.

## 📋 Descrição

O projeto captura imagens de uma câmera IP ou webcam, realiza o processamento das imagens para identificar objetos nas cores **vermelha** e **verde** e envia o resultado da detecção para um servidor **OPC UA**, permitindo a integração com CLPs (como o **CODESYS**) e sistemas de automação industrial.

---

## 🚀 Funcionalidades

- Captura de vídeo em tempo real (Webcam ou URL/IP Camera).
- Redimensionamento da imagem para melhor desempenho.
- Aplicação de filtro **Median Blur** para redução de ruídos.
- Conversão da imagem para o espaço de cores **HSV**.
- Detecção de objetos nas cores:
  - 🔴 Vermelho
  - 🟢 Verde
- Identificação de contornos dos objetos detectados.
- Comunicação em tempo real com servidor **OPC UA**.
- Atualização automática de variáveis no PLC.
- Exibição da imagem processada com os objetos destacados.

---

## 🛠 Tecnologias Utilizadas

- Python 3
- OpenCV
- NumPy
- OPC UA (python-opcua)

---

## ▶️ Como Executar

Execute o arquivo principal:

```bash
main.py
```
---

## ⚙️ Fluxo de Funcionamento

1. Captura da imagem da câmera.
2. Redimensionamento da imagem.
3. Aplicação de filtro de suavização.
4. Conversão para HSV.
5. Segmentação das cores vermelha e verde.
6. Detecção dos contornos.
7. Atualização das variáveis via OPC UA.
8. Exibição da imagem processada.

---

## 🔧 Aplicações

- Automação Industrial
- Sistemas de Inspeção Visual
- Separação de peças por cor
- Integração entre Visão Computacional e PLC
- Indústria 4.0

---

## 📸 Exemplo de Funcionamento

- Detecção em tempo real dos objetos coloridos.
- Envio do estado da detecção para o PLC via OPC UA.
- Exibição dos contornos identificados na tela.

---

## 👤 Autor

**Giuliano Barone**

LinkedIn:  
https://linkedin.com/in/giuliano-barone-6a3a67249

---

## 📄 Licença

Este projeto é disponibilizado para fins de estudo e desenvolvimento em automação industrial e visão computacional.
