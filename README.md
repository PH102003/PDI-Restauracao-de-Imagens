# 📷 PDI - Restauração de Imagens

Este projeto tem como objetivo aplicar técnicas de **Processamento Digital de Imagens (PDI)** para restaurar imagens degradadas por ruídos. Foram utilizados dois tipos de filtros:

- 🧂 **Filtro de Mediana** – Para remoção de ruído Sal e Pimenta.
- 🧠 **Filtro de Wiener** – Para redução de ruídos mais complexos e restauração baseada em estimativa estatística.

---

## 👥 Integrantes

- Pedro Henrique da Silva  
- Adele Brovelli  
- Mário Jorge  
- José Fernando  
- Lóren Gabriela  
- Gustavo Pereira  
- Bruna Lopes  

---

## 🧪 Filtros Utilizados

### 1. Filtro de Mediana

O **filtro de mediana** é eficaz contra ruído do tipo *sal e pimenta*, que se manifesta como pixels pretos e brancos isolados. Ele substitui o valor de um pixel pela mediana dos valores vizinhos, preservando bordas e detalhes importantes.

### 2. Filtro de Wiener

O **filtro de Wiener** é um filtro adaptativo que tenta minimizar o erro médio quadrático entre a imagem original e a imagem restaurada. É especialmente eficaz contra ruídos gaussiano e mistos, levando em conta a variância local da imagem.

---

## 🖼️ Exemplos de Aplicação

### ✅ Imagem com ruído Sal e Pimenta:
- Aplicação do **filtro de mediana** melhora visivelmente a qualidade.

### ✅ Imagem com ruído Gaussiano ou desconhecido:
- O **filtro de Wiener** é mais adequado por sua natureza estatística.

---

## ⚙️ Dependências

- [Python 3](https://www.python.org/)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [NumPy](https://pypi.org/project/numpy/)
- [SciPy](https://pypi.org/project/scipy/) (para o filtro de Wiener)

Instale com:

```bash
pip install opencv-python numpy scipy
