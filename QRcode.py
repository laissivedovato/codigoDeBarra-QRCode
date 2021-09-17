import qrcode

'''
#teste
imagem_qrcode = qrcode.make("https://excelparaestagio.klickpages.com.br/inscricao-basico-cta-att?origemurl=hashtag_yt_org_minibasico2_videoqrcode")
imagem_qrcode.save("qrcode_python.png")
'''

links_produtos = {
  "Excel": "https://excelparaestagio.klickpages.com.br/inscricao-basico-cta-att?origemurl=hashtag_yt_org_minibasico2_videoqrcode",
  "VBA": "https://pages.hashtagtreinamentos.com/inscricao-minicurso-formulario?origemurl=hashtag_yt_org_miniform_videoqrcode",
  "Power BI": "https://excelparaestagio.klickpages.com.br/inscricao-minicurso-power-bi?origemurl=hashtag_yt_org_minicursopbi_videoqrcode",
  "Python": "https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_videoqrcod",
  "SQL": "https://excelparaestagio.klickpages.com.br/inscricao-minicurso-sql?origemurl=hashtag_yt_org_minisql_videoqrcode"

}

for produto in links_produtos:
  link = links_produtos[produto]
  imagem_qrcode = qrcode.make(link)
  imagem_qrcode.save(f"qrcode_{produto}.png")



