import os
import shutil
import hashlib
from datetime import datetime

#### Diretórios
dir_imagens = 'C:\\temp\\script_backup_fotos'
# O diretório de backup pode ser um dispositivo externo e mapeado no sistema
dir_backup = 'C:\\temp\\script_backup_fotos\\backup'
# Local de log no mesmo diretório do script
dir_log = os.path.join(os.getcwd(), 'log')  

#### Configuração
armazenar_log = True
extensoes_permitidas = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

def calcular_hash(arquivo):
    """Calcula o hash SHA256 de um arquivo."""
    sha256 = hashlib.sha256()
    with open(arquivo, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def registrar_log(mensagem):
    """Registra mensagens no arquivo log.txt com data e hora."""
    if armazenar_log:
        if not os.path.exists(dir_log):
            os.makedirs(dir_log)
        caminho_log = os.path.join(dir_log, 'log.txt')
        data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        mensagem_completa = f"{data_hora} - {mensagem}"
        with open(caminho_log, 'a') as log_file:
            log_file.write(mensagem_completa + '\n')

def realizar_backup():
    """Copia arquivos não duplicados para o backup e remove da origem."""
    # Garante que a pasta de backup existe
    if not os.path.exists(dir_backup):
        os.makedirs(dir_backup)

    # Calcula hashes dos arquivos já presentes no backup
    arquivos_backup = {calcular_hash(os.path.join(dir_backup, f)) for f in os.listdir(dir_backup)}

    for arquivo in os.listdir(dir_imagens):
        caminho_origem = os.path.join(dir_imagens, arquivo)

        # Verifica se é um arquivo e se tem uma extensão permitida
        if os.path.isfile(caminho_origem) and arquivo.lower().endswith(extensoes_permitidas):
            hash_arquivo = calcular_hash(caminho_origem)

            if hash_arquivo not in arquivos_backup:
                caminho_destino = os.path.join(dir_backup, arquivo)
                shutil.move(caminho_origem, caminho_destino)  # Move o arquivo
                mensagem = f"Arquivo {arquivo} movido para o backup."
                print(mensagem)
                registrar_log(mensagem)
            else:
                mensagem = f"Arquivo {arquivo} já existe no backup."
                print(mensagem)
                registrar_log(mensagem)

realizar_backup()
