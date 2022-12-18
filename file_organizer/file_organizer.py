
# Importação das libs necessárias
import os
import pyautogui as pg

# Listando Diretórios Existêntes
list_files = os.listdir()
list_files

# Criando listas de extensões
extensoes = {'ipynb'}
for file in list_files:
    # Armazenando cada extensão contida no diretório
    file = file.split('.')
    last_idx = len(file)
    file = file[last_idx-1]
    extensoes.add(file)

# Excluindo a extensão de notebook devido aos erros que geraram no teste.
if 'ipynb' in extensoes:
    try:
        extensoes.remove('ipynb_checkpoints')
    except:
        pass
    
# Contador de Diretórios
n_dirs = 0

# Nome dos diretórios em forma de Conjunto para não ter duplicação de Informações.
name_dirs = set()

# Condicional de existência de Diretório
for extensao in extensoes:
    # Caso o diretório exista
    if os.path.isdir(extensao):
        pass
    # Caso não exista
    else:
        try:
            os.mkdir(extensao)
            name_dirs.add(extensao)
            n_dirs +=1
        except:
            pg.alert(text =f"{extensao} não possui extensão!", title = "Erro ao criar diretório!!")
            
confirm = pg.confirm(text= f"Foram criados {n_dirs} diretórios!" +"\n"+"\n".join(name_dirs))
if confirm == 'Cancel':
    quit()
# Organizando as os arquivos

# Conjunto com as extensões
excessoes = set()

# Contador de arquivos não movidos
n_unmove_files = 0


for file in list_files:
    for extensao in extensoes:
        # Verificando se a extensão encontra-se no arquivo
        if extensao in file:
            try:
                os.rename(f"{file}",f"{extensao}/{file}")
            except:
                excessoes.add(extensao)
                n_unmove_files +=1
                
confirm = pg.confirm(text=f"Não foi possível mover os {n_unmove_files} arquivos a seguir:"+"\n"+"\n".join(excessoes),
         title='Erro ao Mover arquivos!')

if confirm == 'Cancel':
    quit()

# Excluindo Diretórios Vazios
empty_files = []
for file in list_files:
    file_path = os.getcwd() + f"/{file}"
    try:
        os.removedirs(file_path)
        empty_files.append(file_path)
    except:
        pass 

confirm = pg.confirm(text= f"Os diretórios!\n "+"\n".join(empty_files) + "\n \n estavam vazios e foram deletados.")
if confirm == 'Cancel':
    quit()

