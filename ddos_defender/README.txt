 _____  _____   ____   _____ 
|  __ \|  __ \ / __ \ / ____|
| |  | | |  | | |  | | (___  
| |  | | |  | | |  | |\___ \ 
| |__| | |__| | |__| |____) |
|_____/|_____/ \____/|_____/ 
██████╗ ███████╗███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║  ██║█████╗  █████╗  █████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║  ██║██╔══╝  ██╔══╝  ██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██████╔╝███████╗██║     ███████╗██║ ╚████║██████╔╝███████╗██║  ██║
╚═════╝ ╚══════╝╚═╝     ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝

**DDOS Defender** é uma ferramenta avançada de segurança automatizada que protege servidores contra ataques de negação de serviço (DDoS) via análise de logs, bloqueio de IPs suspeitos e geração de registros detalhados.

---

## ⚙️ Funcionalidades

- 🔎 **Detecção automática** de IPs com comportamentos suspeitos
- 🚫 **Bloqueio de IPs maliciosos** usando regras de firewall (UFW)
- 🧾 **Geração automática de logs** de atividade e ações
- 📊 Menu interativo para acesso rápido às funções principais
- 🔐 Conexão via SSH para atuar diretamente no servidor

---

## 📁 Estrutura

O projeto está contido em um único arquivo:  o "main.py"

Este script inclui três módulos principais:

- **DDOS Defender**: Detecta e responde automaticamente a ataques
- **IP Blocker**: Bloqueia manualmente IPs informados pelo usuário
- **Log Generator**: Gera registros de eventos importantes

---

## 🖥️ Requisitos

- Python 3.8 ou superior
- Sistema operacional Windows, Linux ou MacOS
- Acesso SSH ao servidor que será protegido

### 📦 Bibliotecas necessárias:

```bash
pip install paramiko

para abrir:  
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
python main.py


escolher as opções do menu: 
[1] DDOS Defender
[2] Bloquear IPs suspeitos
[3] Gerar Logs
[4] Sair

🔐 Exemplo de uso
O DDOS Defender acessa o log do Apache (/var/log/apache2/access.log)

Conta o número de acessos por IP

Bloqueia automaticamente IPs que ultrapassarem o limite configurado

Registra a ação em um arquivo .log local

você pode usar esses comandos pra executar em linux
temos também o arquivo.exe pra Windows :3 aqui a baixo
https://www.mediafire.com/folder/6kq8k9ofqa5s7/dist


👨‍💻 Autor
Joshua Davi Santos Selistre

Desenvolvedor Python

Brasil – 🇧🇷
