# Script de Backup Automático de Imagens

Este script em Python automatiza o backup de imagens (como `.jpg`, `.png`, etc.) de um diretório de origem para um diretório de backup. Ele evita duplicidade ao verificar o conteúdo dos arquivos usando hashes (SHA-256) e mantém um log detalhado das operações realizadas.

## Funcionalidades

- **Backup Automático**: Move imagens do diretório de origem para o diretório de backup.
- **Evita Duplicidade**: Verifica se o arquivo já foi salvo no backup usando um hash único (SHA-256), garantindo que arquivos duplicados não sejam movidos.
- **Filtro por Extensão**: Apenas arquivos com extensões específicas (`.jpg`, `.jpeg`, `.png`, etc.) são processados.
- **Logs Detalhados**: Registra todas as operações em um arquivo `log.txt`, incluindo data e hora:
  - Arquivos movidos para o backup.
  - Arquivos ignorados porque já existem no backup.
- **Configurações**:
  - Diretórios de origem, filtro de arquivos e backup e log podem ser ajustados.
  - Possibilidade de desativar o registro de logs (`armazenar_log = False`).

---

## Requisitos

Para executar o script, você deve ter o <strong>Python</strong> instalado na versão 3.8 ou superior.

O script usa apenas bibliotecas nativas do Python.

---

## Como Executar

Siga os passos abaixo para configurar e executar o script:

### 1. Clone este repositório
```bash
git clone https://github.com/danbackeres/move_images_to_backup.git
```

### 2. Configure os Diretórios
No início do arquivo Python, ajuste as variáveis `dir_imagens` e `dir_backup` para apontar para os diretórios desejados:

```bash
dir_imagens = 'C:\caminho\para\pasta\origem'
dir_backup = 'C:\caminho\para\pasta\backup'
```

### 3. Execute o Script
Execute o script diretamente no terminal ou prompt de comando:

```bash
python realiza_backup_fotos.py
```

### 4. Verifique os Logs (Opcional)
Após a execução, você pode verificar a pasta `log` criada no mesmo diretório do script. Lá estará o arquivo `log.txt` com os detalhes das operações realizadas.

---

## Pontos Técnicos Importantes

1. **Hash SHA-256**  
   O script utiliza a função `hashlib.sha256()` para calcular um hash único baseado no conteúdo binário dos arquivos. Isso garante que:
   - Apenas arquivos com conteúdos diferentes sejam movidos.
   - Arquivos idênticos (mesmo com nomes diferentes) não sejam duplicados no backup.

2. **Filtro por Extensão**  
   Apenas arquivos com extensões específicas são processados. As extensões permitidas estão configuradas na variável:

```bash
extensoes_permitidas = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
```

3. **Logs**  
O registro em log pode ser ativado ou desativado ajustando a variável:

```bash
armazenar_log = True
```

---

## Observações

- Certifique-se de que você tem permissão para acessar e modificar os diretórios configurados em `dir_imagens` e `dir_backup`.
- Para agendar a execução automática do script, você pode usar ferramentas como:
  - **Agendador de Tarefas (Windows)** ou **cron (Linux)**.





