Como testar seu projeto DDOS Defender na prática
1. Prepare um servidor para testar
Você precisa de um servidor Linux (pode ser VPS, uma máquina virtual ou até um servidor local) que tenha:

SSH habilitado

Servidor web (ex: Apache) rodando com arquivo de log (/var/log/apache2/access.log) ou ajuste o caminho no código se for diferente

ufw instalado para bloqueio de IPs (no script você usa comando sudo ufw deny from IP)

2. Configure seu projeto
Tenha o script .py (ou .exe se já gerou) no seu PC local.

Se for o .exe, certifique-se que está na mesma pasta que os arquivos de log, se seu script usar algum arquivo local.

3. Execute o programa
No terminal (ou executando o .exe):

Rode python main.py (se for script)

Ou clique duas vezes no main.exe

Vai aparecer o menu:

csharp
Copiar
Editar
==========================
      DDOS TOOLBOX
==========================
[1] DDOS Defender
[2] Bloquear IPs suspeitos
[3] Gerar Logs
[4] Sair
4. Teste o DDOS Defender (opção 1)
Escolha a opção 1 para rodar o DDOS Defender.

Ele vai pedir:

IP do servidor

Usuário SSH

Senha SSH

Ele vai se conectar no servidor, analisar os logs e bloquear IPs suspeitos automaticamente.

Se encontrar IPs para bloquear, ele vai mandar bloquear via ufw e registrar o evento no arquivo de log local (ddos_defender.log).

5. Teste o IP Blocker manual (opção 2)
Você pode usar para bloquear IPs manualmente, se implementou essa funcionalidade.

6. Teste o Log Generator (opção 3)
Ele vai mostrar mensagens de log baseadas no que estiver acontecendo no sistema.

7. Verifique os logs
Abra o arquivo ddos_defender.log para ver os registros do que foi bloqueado ou dos eventos detectados.

Importante para testes reais
Para simular ataques, você pode usar ferramentas de teste de carga (ex: ab - Apache Benchmark) pra gerar muitas requisições de um IP.

Verifique se o seu servidor responde corretamente e se bloqueia os IPs como esperado.

