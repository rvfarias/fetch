import os
import glob
import csv

#Classe de arquivos
class Arquivo:
    def __init__(self, nome, server, location, proxy):
        self.nome = nome
        self.server = server
        self.location = location
        self.proxy = proxy

#lista de objetos da classe arquivos 
list_arq = []

# Defina o caminho para a pasta onde os arquivos estão localizados
pasta = 'conf.d'

# Use glob para encontrar todos os arquivos na pasta com a extensão desejada (por exemplo, .txt)
arquivos = glob.glob(os.path.join(pasta, '*.conf'))

# Iterar sobre os arquivos e ler o conteúdo de cada um
for arquivo in arquivos:
    nome_do_arquivo = os.path.basename(arquivo)  # Extrai o nome do arquivo
    # print(f'Nome do arquivo: {nome_do_arquivo}')
    
    #Leitura de cada linha do arquivo 
    with open(arquivo, 'r') as f:
        linha = f.readline()
        count = 0
        loc_controller = False
        #Enquanto houver linhas no arquivo
        while linha:
            
            linha = f.readline()
            #Ignora linhas comentadas no arquivo
            if '#' in linha:
                continue

            #Verifica se esta no primeiro bloco de server, se sim incrementa o contador
            elif 'server_name' in linha:
                count = count +1
            #Se contador for maior que 1 que dizer que ja passou do primeiro bloco
            #Entao pega o nome do server em questao e salva  
            if 'server_name' in linha and count > 1:
                str = linha
                #Trantando a string de server_name
                aux1 = str.find('s')
                serv = str[aux1+11:]
                serv = serv.strip()

            #Verifica se ja esta na linha de location, se sim a salva
            elif 'location' in linha:
                #Variavel para controle para caso nao haja location, ignorar o server 
                loc_controller = True
                str = linha
                #Trantando a string de location
                aux1 = str.find('/')
                aux2 = str.find('{')
                loc = str[aux1:aux2]

                if len(loc) == 2:
                    loc = '/root'

                else:
                    loc = str[aux1:aux2]

            #Verifica se ja esta na linha do proxy, se sim filtra e salva
            elif 'proxy_pass' in linha:
                #Caso nao tenha encontrado nenhuma location ignora o server
                if loc_controller == False:
                    continue
                #Trantando a string do proxy
                str = linha
                aux1 = str.find('h')
                aux2 = str.find(';')
                pro = str[aux1:aux2]
                
                arq = Arquivo(nome_do_arquivo, serv, loc, pro)
                list_arq.append(arq)

with open("exemplo.txt", "w") as arquivo:
    line = "Lista com: \n\n    <NOME_ARQUIVO> ,    <SERVER_NAME>,    <LOCATION>,    <PROXY_PASS>"
    arquivo.writelines(line)
    arquivo.writelines("\n\n")
    for arq2 in list_arq:
        line = arq2.nome + ', ' + arq2.server + ' , ' + arq2.location + ', ' + arq2.proxy
        arquivo.writelines(line)
        arquivo.writelines("\n")
        
with open('teste.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter= ',')
    writer.writerow(['NOME DO ARQUIVO', 'SERVER NAME', 'LOCATION', 'PROXY PASS'])
    for arq2 in list_arq:
        writer.writerow([arq2.nome, arq2.server, arq2.location, arq2.proxy])
        
