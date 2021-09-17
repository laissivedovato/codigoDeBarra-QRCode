from barcode import EAN13
from barcode.writer import ImageWriter #irá permitir converter a extensão da imagem de svg para png

#fornrcer 12 digitos e o EAN13 irá gerar o 13º número
codigo_barra = EAN13("123123123123", writer=ImageWriter())
codigo_barra.save("codigo_barra") #salvar com o nome final do arquivo

