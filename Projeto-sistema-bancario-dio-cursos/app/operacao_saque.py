from historico_de_transacoes import GerenciarHistoricoDepositos
from operacao_deposito import obter_dia_deposito, obter_hora_deposito


def obter_valor_do_saque() -> float:
    saque = input("\nDigite o valor para saque: ")
    formatar_string_saque = saque.replace(',', '.')
    try:
        converter_para_float = float(formatar_string_saque)
        return converter_para_float
    except ValueError as Error:
        print(f'Por favor insira apenas valores numéricos, com apenas um ponto ou virgula')
        return obter_valor_do_saque()

def validar_saque(valor_saque: float, saldo: float, limite_de_saque: int) -> bool:
    
    saque_negativo = valor_saque > 0
    limite_saque = limite_de_saque > 0
    saque_menor_que_500 = valor_saque <= 500
    saldo_menor_que_saque = saldo > valor_saque

    if saque_negativo and limite_saque and saque_menor_que_500 and saldo_menor_que_saque:
        return True
    return False
    
def realizar_saque(valor_saque: float, saldo: float) -> float:
    return saldo - valor_saque


def realizar_operacao_saque() -> bool:
    registrar = GerenciarHistoricoDepositos()
    # na primeira execução a inexistencia do arquivo vai causar um erro index error na obtenção do saldo, valor inicial definido como 0
    try:
        saldo = registrar.lista_de_registros[-1]['Novo Saldo']
        limite_saque = registrar.lista_de_registros[-1]['Limite de saques díario']
    except IndexError:
        saldo = 0
        limite_saque = 3
    
    valor_saque = obter_valor_do_saque()
    if validar_saque(valor_saque, saldo, limite_saque):
        dia = obter_dia_deposito()
        hora = obter_hora_deposito()
        limite_saque -= 1
        novo_saldo = realizar_saque(valor_saque, saldo)

        dados = {
            'Saldo anterior': saldo,
            'Valor do deposito': 0,
            'Valor do Saque': valor_saque,

            'Novo Saldo': novo_saldo,
            'Data e Hora': dia + ' ' + hora,
            'Limite de saques díario': limite_saque
        }
        registrar.adicionar_registro(dados)
        registrar.salvar_registro()
        print("Saque realizado com sucesso.")
        print(f'Se pode realizar mais {limite_saque} saques hoje.')
        return True
    else:
        print("Falha ao realizar saque!!!")
        if saldo < valor_saque:
            print(f'''Saldo insuficiente: 
                  Saldo disponivel: R$ {saldo:.2f}
                  Saque impedido: R$ {valor_saque:.2f}''')
        
        if not limite_saque:
            print("Limite de saques diarios foram esgotados")
        
        if valor_saque > 500:
            print("Passou do limite máximo por saque: R$ 500,00")
        
        return False
    


if __name__ == "__main__":
    realizar_operacao_saque()
