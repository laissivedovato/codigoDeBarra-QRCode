from barcode import EAN13
from barcode.writer import ImageWriter #irá permitir converter a extensão da imagem de svg para png

#teste
#fornecer 12 digitos e o EAN13 irá gerar o 13º número
'''
codigo_barra = EAN13("123123123123", writer=ImageWriter())
codigo_barra.save("codigo_barra") #salvar com o nome final do arquivo
'''

# gerando código de barras em massa
codigo_produtos = {
  "jarra": "551746544444",
  "garrafa": "665789011111",
  "copo": "665887111111",
  "caneca": "998556211111"
}

for produto in codigo_produtos:
  codigo = codigo_produtos[produto]
  codigo_barra = EAN13(codigo, writer=ImageWriter())
  codigo_barra.save(f"codigo_barra_{produto}")
