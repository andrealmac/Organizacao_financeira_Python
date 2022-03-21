from datetime import datetime
import json
from re import A

#carteira = {}
#id_transacao = 1 
try:
    with open('carteira.json', 'r') as arquivo:
        carteira = json.loads(arquivo.read())
        
    id_transacao = carteira["idtransacao"]
    carteira.pop("idtransacao")
except:
    carteira = {}
    id_transacao = 1 

def listarTransacoes():
    if len(carteira) == 0:
        print('\nSem transações!')
        return
    print('\nSuas transações: ')
    
    for transacao in sorted(
        carteira.values(),
        key = lambda transacao: str(transacao["identificador"]),
        reverse=True):
        print(f'{transacao["identificador"]} - {transacao["data"]} - {transacao["descricao"]}: R${transacao["valor"]:.2f}')

def adicionarTransacoes():
    global id_transacao
    
    descricao = input('\nDigite a descrição da transação: ')
    valor = float(input('Digite o valor da transação (com o sinal de - se for despesa): '))
    data = str(datetime.now())
    
    transacao = {
        "valor": valor,
        "descricao": descricao,
        "data": data,
        "identificador": str(id_transacao)
    }
    
    carteira["id_"+str(id_transacao)] = transacao
    id_transacao +=1
    print('Transação adicionada com sucesso!')

def deletarTransacoes():
    identificador = "id_" + input('\nDigite o id da transação que quer deletar: ')
    
    transacao = carteira.pop(identificador)
    
    print(f'{transacao["identificador"]} - {transacao["data"]} - {transacao["descricao"]}: R${transacao["valor"]:.2f} foi EXCLUIDA!')
    
def editarTransacoes():
    id_transacao = int(input('\nDigite o id da transação que quer editar: '))
    identificador = "id_" + str(id_transacao)
    
    descricao = input('\nDigite uma nova descrição da transação: ')
    valor = float(input('Digite um novo valor da transação: '))
    mudar_data = input('Digite S para mudar a data da transação para a data atual ou N para manter a data antiga: ').upper()
    if mudar_data == 'S':
        data = str(datetime.now())
    else:
        data = carteira[identificador]["data"]
        
    transacao = {
        "valor": valor,
        "descricao": descricao,
        "data": data,
        "identificador": str(id_transacao)
    }
    carteira["id_"+str(id_transacao)] = transacao
    print('Transação {} editada com sucesso!'.format(id_transacao))

def consultarSaldo():
    saldo = 0
    for transacao in carteira.values():
        saldo += transacao["valor"]
    print(f'\nSeu saldo atual é R${saldo:.2f}')

def salvarCarteira():
    c = carteira.copy()
    c["idtransacao"] = id_transacao
    
    with open('carteira.json', 'w') as arquivo:
        arquivo.write(json.dumps(c))
    

#repetir o menu
while True:
    op = input('''\nDigite:
               \rL - Listar transações
               \rA - Adicionar transações
               \rD - Deletar transações
               \rE - Editar transações
               \rS - Consultar saldo atual
               \rQ - Sair do programa
               \rSua entrada:  ''').upper()
    if op == 'A':
        adicionarTransacoes()
        salvarCarteira()
        
    elif op == 'D':
        deletarTransacoes()
        salvarCarteira()
        
    elif op == 'E':
        editarTransacoes()
        salvarCarteira()
        
    elif op == 'L':
        listarTransacoes()
        
    elif op == 'S':
        consultarSaldo()
        
    elif op == 'Q':
        exit()
    else :
        print('Operação inválida!')