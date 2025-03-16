from operacao_deposito import realizar_operacao_de_deposito
from operacao_saque import realizar_operacao_saque
from historico_de_transacoes import GerenciarHistoricoDepositos

while True:
    detalhes_da_conta = GerenciarHistoricoDepositos()
    try:
        obter_saldo = detalhes_da_conta.lista_de_registros[-1]['Novo Saldo']
    except IndexError:
        obter_saldo = 0

    menu = f"""
    Bem vindo ao banco do valtinho
    {'-'*35}
    Saldo Disponivel: R$ {obter_saldo:,.2f}
    {'-'*35}
    0 - SAIR
    1 - DEPOSITAR
    2 - SACAR
    3 - EXIBIR ULTIMAS TRANSAÇÕES
    {'-'*35}
    """
    print(menu)
    escolha = int(input("Escolha uma opção: "))
    if not escolha:
        break
    elif escolha == 1:
        realizar_operacao_de_deposito()
    elif escolha == 2:
        realizar_operacao_saque()
    elif escolha == 3:
        registros = GerenciarHistoricoDepositos()
        registros.exibir_registro()
    else:
        print("Informe um Número valido --> 0/1/2/3")