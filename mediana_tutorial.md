# Remoção de Ruído Sal e Pimenta com Filtro de Mediana em Python

## 🧠 O que é Ruído Sal e Pimenta?

O **ruído sal e pimenta** (salt-and-pepper noise) é um tipo de distorção que aparece em imagens digitais como pixels pretos e brancos espalhados aleatoriamente. Isso pode ocorrer por falhas na captura da imagem, transmissão de dados ou sensores defeituosos.

## 🎯 Objetivo

Neste tutorial, vamos aplicar o **filtro de mediana**, um dos métodos mais eficazes para remover ruído sal e pimenta preservando as bordas da imagem.

---

## 🧪 Por que o Filtro de Mediana?

O **filtro de mediana** substitui o valor de um pixel pela **mediana dos valores vizinhos** dentro de uma janela (por exemplo, 3×3, 5×5, etc.). Ele é eficaz para remover valores extremos (como 0 e 255) sem borrar a imagem como o filtro de média faria.

### ✅ Vantagens:
- Remove ruídos isolados (especialmente sal e pimenta).
- Mantém as bordas e detalhes importantes da imagem.
- Simples e eficiente.

---

## 📦 Dependências

Você precisa do Python 3 e da biblioteca OpenCV. Para instalar, use:

```bash
pip install opencv-python
