import base64
try:
    file_enc = "C:\\Users\\Vinir\\OneDrive\\Área de Trabalho\\teste.exe"
    f = open(file_enc, 'rb')
    dados = f.read()
    f.close()
    dados_dec = base64.b64decode(dados)
    f = open(file_enc, 'wb')    
    f.write(dados_dec)
    f.close()
except OSError as e:
    print("Endereço do arquivo está errado(ERROR:", e, ")")