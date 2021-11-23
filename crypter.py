import base64
import os

try:
    file_original = str(input("Digite o endereço do arquivo a ser encriptado(base64):"))
    file_dest = str(input("Digite o endereço do novo arquivo encriptado(base64): "))
    f = open(file_original, 'rb')
    dados = f.read()
    f.close()
    dados_enc = base64.b64encode(dados)
    f = open(file_dest, 'wb')
    f.write(dados_enc)
    f.close()
except OSError as e:
    print("Endereço do arquivo errado(ERROR:", e, ")")

