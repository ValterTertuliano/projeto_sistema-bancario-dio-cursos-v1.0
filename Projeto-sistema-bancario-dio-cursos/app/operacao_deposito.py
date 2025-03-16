from datetime import datetime
from historico_de_transacoes import GerenciarHistoricoDepositos


# obter valor do deposito
def obter_valor_do_deposito() -> float:
    deposito = input("\nDigite o valor para deposito: ")
    formatar_string_deposito = deposito.replace(',', '.')
    try:
        converter_para_float = float(formatar_string_deposito)
        return converter_para_float
    except ValueError as Error:
        print(f'Por favor insira apenas valores numéricos, com ponto ou virgula')
        return obter_valor_do_deposito()
    
    
# verificar se o deposito é maior que 0
def deposito_valido(valor_deposito: float) -> bool:
    if valor_deposito > 0:
        return True
    return False

# Somar o deposito com o saldo
def realizar_deposito(valor_deposito: float, saldo: float) -> float:
    return valor_deposito + saldo

# Registrar historico de depositos

# obter dia do deposito
def obter_dia_deposito() -> str:
    return datetime.now().strftime("%d:%m:%Y")

# obter hora do deposito
def obter_hora_deposito() -> str:
    return datetime.now().strftime("%H:%M:%S")

def realizar_operacao_de_deposito() -> bool:
    registrar = GerenciarHistoricoDepositos()
    # na primeira execução a inexistencia do arquivo vai causar um erro index error na obtenção do saldo, valor inicial definido como 0
    try:
        saldo = registrar.lista_de_registros[-1]['Novo Saldo']
        limite_saque = registrar.lista_de_registros[-1]['Limite de saques díario']
    except IndexError:
        saldo = 0
        limite_saque = 3   
    deposito = obter_valor_do_deposito()
    if deposito_valido(deposito):
        novo_saldo = realizar_deposito(deposito, saldo)
        hora = obter_hora_deposito()
        dia = obter_dia_deposito()
        

        dados = {
            'Saldo anterior': saldo,
            'Valor do deposito': deposito,
            'Valor do Saque': 0,
            'Novo Saldo': novo_saldo,
            'Data e Hora': dia + ' ' + hora,
            'Limite de saques díario': limite_saque
        }
        
        registrar.adicionar_registro(dados)
        registrar.salvar_registro()
        print("Deposito feito com feito com sucesso")
        return True
    else:
        print("Por favor informa um valor de deposito valido: ")
        print("""
        - Informe apenas valores acima de 0
        - Informe apenas numeros
        - Digite no maximo uma virgula ou ponto
        """)
        return False
    
if __name__ == "__main__":
    realizar_operacao_de_deposito()