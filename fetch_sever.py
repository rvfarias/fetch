import os
import glob
from pathlib import Path
#lista de objetos da classe arquivos 
# list_arq = []

# Defina o caminho para a pasta onde os arquivos estão localizados
pasta = Path("/home/rafael-farias/Documentos/fetch/linkpagamento")

# # Define o caminho da pasta raiz
# pasta_raiz = Path("/caminho/para/pasta")

# Itera sobre todos os arquivos (inclusive nas subpastas)
# Filtra apenas arquivos .txt
for arquivo in pasta.rglob("*.yaml"):
    caminho = arquivo
    with arquivo.open("r") as f:
        linhas = f.readlines()
        i = 0
        for linha in linhas:
        #Entao pega o nome do server em questao e salva  
            if 'server' in linha:
                indice = linha.find(':')
                str = linha[0:indice+1] + "\n"
                print(linha)
                linha = str
                linhas[i] = linha
                i = i + 1     
            else:
                i = i + 1
                continue
        with caminho.open("w") as f:
            f.writelines(linhas)

# # Use glob para encontrar todos os arquivos na pasta com a extensão desejada (por exemplo, .txt)
# arquivos = glob.glob(os.path.join(pasta, '*.yaml'))

# # Iterar sobre os arquivos e ler o conteúdo de cada um
# for arquivo in arquivos:
#     nome_do_arquivo = os.path.basename(arquivo)  # Extrai o nome do arquivo
#     print(f'Nome do arquivo: {nome_do_arquivo}')
#     if nome_do_arquivo == "values.yaml":
#         #Leitura de cada linha do arquivo 
#         with open(arquivo, 'r') as f:
#             linhas = f.readlines()
#             #Enquanto houver linhas no arquivo
#             i = 0
#             for linha in linhas:
#                 #Entao pega o nome do server em questao e salva  
#                 if 'replica' in linha:
#                     indice = linha.find('#')
#                     if indice > -1:
#                         indice = linha.find(':')
#                         str = linha[1:indice+1] + " 0"
#                         print(str)
#                         linha = str 
#                     else:
#                         indice = linha.find(':')
#                         str = linha[0:indice+1] + " 0"
#                         print(str)
#                         linha = str

#                     # if len(linha) == 16:
#                     #     str = linha[:14] + "0"
#                     #     print(str)
#                     #     linha = str
                    
#                     # elif len(linha) > 16:
#                     #     str = linha[1:15] + "0"
#                     #     str[15] = "0"
#                     #     linha = str
#                     linhas[i] = linha
#                     i = i + 1               
#                 else:
#                     i = i + 1
#                     continue
        
    #     with open("/home/rafael-farias/Documentos/fetch/api-v2/values.yaml", "w") as f:
    #         f.writelines(linhas)
            
    # else:
    #     continue
    


        
        
