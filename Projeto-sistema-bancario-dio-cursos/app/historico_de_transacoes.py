import json
import os

HISTORICO_DEPOSITO = 'dados/historico_deposito.json'

class GerenciarHistoricoDepositos():
    def __init__(self):
        """
        Inicia a classe
        - Cria um arquivo json caso ainda não existe
        - Carrega os registros de historico
        """
        # se não existir cria
        if not os.path.exists(HISTORICO_DEPOSITO):
            self.lista_de_registros = []
            with open(HISTORICO_DEPOSITO, 'w', encoding='utf-8') as registro:
                json.dump(self.lista_de_registros, registro, ensure_ascii=False, indent=4)
        
        # se existir carrega o registro
        with open(HISTORICO_DEPOSITO, 'r', encoding='utf-8') as registro:
            self.lista_de_registros = json.load(registro)
    
    def adicionar_registro(self, registro: dict):
        self.lista_de_registros.append(registro)
        

    def salvar_registro(self):
        with open(HISTORICO_DEPOSITO, 'w', encoding='utf-8') as registro:
            json.dump(self.lista_de_registros, registro, ensure_ascii=False, indent=4)
    
    def exibir_registro(self):
        sorted(self.lista_de_registros, key=lambda x: x["Data e Hora"])
        for registro in self.lista_de_registros:
                if registro["Valor do deposito"]:
                    exibir = f"""Deposito Realizado: 
{'-'* 30}
Dia e Hora: {registro['Data e Hora']}
Valor Depositado: R$ {registro['Valor do deposito']:,.2f}
Saldo disponivel: R$ {registro['Novo Saldo']:,.2f}
"""
                    print(exibir, end='')
                else:
                    exibir = f"""{'-'* 30}
Saque Realizado
{'-'* 30}
Dia e Hora: {registro['Data e Hora']}
Valor Sacado: R$ {registro['Valor do Saque']:,.2f}
Saldo disponivel: R$ {registro['Novo Saldo']:,.2f}
{'-'* 30}
"""
                    print(exibir, end='')
if __name__ == "__main__":
    r = GerenciarHistoricoDepositos()
    r.exibir_registro()        

        
