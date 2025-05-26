import paramiko
import re
import smtplib
from email.message import EmailMessage
from datetime import datetime
import getpass

# Cores para terminal
purple = "\033[95m"
green = "\033[92m"
reset = "\033[0m"

ARQUIVO_LOG = "ddos_defender.log"
LIMITE_ACESSOS = 100  # Limite para considerar ataque

def gerar_log(mensagem):
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{agora}] {mensagem}\n"
    with open(ARQUIVO_LOG, "a") as f:
        f.write(linha)

def enviar_alerta(email_remetente, senha_remetente, email_destino, assunto, corpo):
    try:
        msg = EmailMessage()
        msg.set_content(corpo)
        msg["Subject"] = assunto
        msg["From"] = email_remetente
        msg["To"] = email_destino

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(email_remetente, senha_remetente)
        server.send_message(msg)
        server.quit()
        print(f"{green}[+] Alerta enviado para {email_destino}{reset}")
        gerar_log(f"Alerta enviado para {email_destino}: {assunto}")
    except smtplib.SMTPAuthenticationError as e:
        print(f"[ERRO] Falha de autenticação ao enviar alerta: {e}")
        gerar_log(f"Erro de autenticação no envio de alerta: {e}")
    except Exception as e:
        print(f"[ERRO] Falha ao enviar alerta: {e}")
        gerar_log(f"Erro ao enviar alerta: {e}")

def conectar_ssh(ip, usuario, senha):
    cliente = paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        cliente.connect(ip, username=usuario, password=senha)
        print(f"{green}[+] Conectado ao servidor {ip}{reset}")
        return cliente
    except Exception as e:
        print(f"[ERRO] Falha na conexão SSH: {e}")
        return None

def analisar_logs(cliente):
    print("[*] Analisando logs do servidor...")
    comando = "cat /var/log/apache2/access.log"
    stdin, stdout, stderr = cliente.exec_command(comando)
    logs = stdout.read().decode()
    ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', logs)

    contagem_ips = {}
    for ip in ips:
        contagem_ips[ip] = contagem_ips.get(ip, 0) + 1

    suspeitos = [ip for ip, count in contagem_ips.items() if count > LIMITE_ACESSOS]
    return suspeitos

def bloquear_ip(cliente, ip):
    comando = f"echo 'sua_senha_sudo' | sudo -S ufw deny from {ip}"
    stdin, stdout, stderr = cliente.exec_command(comando)
    erro = stderr.read().decode()
    if erro:
        print(f"[ERRO] ao bloquear {ip}: {erro}")
        gerar_log(f"Erro ao bloquear IP {ip}: {erro}")
    else:
        print(f"{green}[+] IP {ip} bloqueado com sucesso!{reset}")
        gerar_log(f"IP bloqueado: {ip}")

def ddos_defender():
    print(green + r"""
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
""" + reset)

    ip_servidor = input("IP do servidor: ")
    usuario = input("Usuário SSH: ")
    senha = getpass.getpass("Senha SSH: ")
    email_remetente = input("Email remetente (para enviar alertas): ")
    senha_email = getpass.getpass("Senha do email remetente: ")
    email_destino = input("Email destino para alertas: ")

    cliente = conectar_ssh(ip_servidor, usuario, senha)
    if not cliente:
        return

    suspeitos = analisar_logs(cliente)
    if not suspeitos:
        print("Nenhum IP suspeito detectado.")
        gerar_log("Nenhum IP suspeito detectado.")
    else:
        for ip in suspeitos:
            bloquear_ip(cliente, ip)
            enviar_alerta(
                email_remetente, senha_email, email_destino,
                "Alerta DDoS - IP Bloqueado",
                f"O IP {ip} foi bloqueado por exceder o limite de requisições."
            )

    cliente.close()

def ip_blocker():
    print(purple + r"""
 _         _     _            _              
(_)_ __   | |__ | | ___   ___| | _____ _ __ 
| | '_ \  | '_ \| |/ _ \ / __| |/ / _ \ '__|
| | |_) | | |_) | | (_) | (__|   <  __/ |   
|_| .__/  |_.__/|_|\___/ \___|_|\_\___|_|   
  |_|                                       
""" + reset)
    print("Funcionalidade: Bloquear IPs manualmente.")
    cliente = conectar_ssh(
        input("IP do servidor: "),
        input("Usuário SSH: "),
        getpass.getpass("Senha SSH: ")
    )
    if not cliente:
        return
    while True:
        ip_para_bloquear = input("Digite o IP para bloquear (ou 'sair' para voltar): ")
        if ip_para_bloquear.lower() == "sair":
            break
        bloquear_ip(cliente, ip_para_bloquear)
    cliente.close()

def log_generator():
    print("Log Generator integrado, não necessita ação manual.")
    print("As mensagens de log são geradas automaticamente pelo DDOS Defender e IP Blocker.")

def menu():
    print("""
==========================
      DDOS TOOLBOX
==========================
[1] DDOS Defender
[2] Bloquear IPs manualmente (IP Blocker)
[3] Mostrar informações do Log Generator
[4] Sair
""")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            ddos_defender()
        elif escolha == "2":
            ip_blocker()
        elif escolha == "3":
            log_generator()
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
