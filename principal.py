"""importações"""
import sys
import mysql.connector as sql
from PyQt6 import QtWidgets,uic
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
import numpy as np

def conexãoSqlInsercaoDeApuracao(Senha, Escola, Ano, Conceito_Final):
    banco = sql.connect(host="localhost", username="root", password=Senha, database="apuraçãoHistorico")
    if banco.is_connected:
        print("Conexão foi bem sucedida")
        cursor = banco.cursor()
        comando = "insert into Apurações (Escola, Ano, Conceito_Final) values (%s,%s,%s)"
        valores = (Escola, Ano, Conceito_Final)
        cursor.execute(comando,valores)
        banco.commit()
        print("A nova apuração foi inserida no banco de dados")
        cursor.close()
        banco.close()
    else:
        print("\aAlgum erro ocorreu\n")

def conecãoSqlVisualizarHistorico():
    banco = sql.connect(host="localhost", username="root",password=
                        paginaHistorico.caixaSenha.toPlainText(), database="apuraçãoHistorico")
    if banco.is_connected:
        print("\nConexão foi bem sucedida")
        curso = banco.cursor()
        curso.execute("select * from Apurações")
        apurações = curso.fetchall()
        paginaHistorico.caixaDeTexto.clear()
        for a in apurações:
            paginaHistorico.caixaDeTexto.append(str(a))
        curso.close()
        banco.close()
    else:
        print("\aAlgum erro ocorreu\n")

def botaoSobreClicado():
    paginaInicial.close()
    paginaSobreInterface()

def botaoNovaApuraçãoClicado():
    paginaInicial.close()
    paginaNovaApuraçãoInterface()

def botaoHistoricoClicado():
    paginaInicial.close()
    paginaHistoricoInterface()

def botaoVoltarNovaApuração():
    paginaNovaApuração.close()
    paginaIncialInterface()

def botaoVoltarHistorico():
    paginaHistorico.close()
    paginaIncialInterface()

def botaoVoltarSobre():
    paginaSobre.close()
    paginaIncialInterface()

def botaoApurarClicado():
    """definção das variáveis de entrada"""
    comissao = ctrl.Antecedent(np.arange(0, 11, 1), 'Comissão de Frente')
    harmonia = ctrl.Antecedent(np.arange(0, 11, 1), 'Harmonia')
    enredo = ctrl.Antecedent(np.arange(0, 11, 1), 'Enredo')
    evolução = ctrl.Antecedent(np.arange(0, 11, 1), 'Evolução')
    """saída"""
    global conceito
    conceito = ctrl.Consequent(np.arange(0, 11, 0.5), 'Conceito Final')

    """definicao dos conjuntos"""
    comissao.automf(number=3, names=['Ruim', 'Mediano', 'Bom'])
    """-----------------------"""
    harmonia.automf(number=3, names=['Ruim', 'Mediana', 'Boa'])
    """-----------------------"""
    enredo.automf(number=3, names=['Ruim', 'Mediano', 'Bom'])
    """-----------------------"""
    evolução.automf(number=3, names=['Ruim', 'Mediano', 'Bom'])
    """-----------------------"""
    conceito["Ruim"] = fuzzy.trimf(conceito.universe,[0,2.5,5])
    conceito["Mediano"]= fuzzy.trimf(conceito.universe,[2.5,5,7.5])
    conceito["Bom"] = fuzzy.trimf(conceito.universe,[5,7.5,10])

    """definiçao das regras"""
    regra1 = ctrl.Rule(enredo['Ruim'] & comissao['Ruim'] & evolução['Ruim'] & harmonia['Ruim'], conceito['Ruim'])
    regra2 = ctrl.Rule(enredo['Ruim'] & comissao['Ruim'] & evolução['Ruim'] & harmonia['Mediana'], conceito['Ruim'])
    regra3 = ctrl.Rule(enredo['Ruim'] & comissao['Ruim'] & evolução['Ruim'] & harmonia['Boa'], conceito['Ruim'])
    regra4 = ctrl.Rule(enredo['Ruim'] & comissao['Ruim'] & evolução['Mediano'] & harmonia['Ruim'], conceito['Ruim'])
    regra5 = ctrl.Rule(enredo['Ruim'] & comissao['Ruim'] & evolução['Mediano'] & harmonia['Mediana'], conceito['Ruim'])
    regra6 = ctrl.Rule(enredo['Ruim'] & comissao['Ruim'] & evolução['Mediano'] & harmonia['Boa'], conceito['Mediano'])
    regra7 = ctrl.Rule(enredo['Ruim'] & comissao['Ruim'] & evolução['Bom'] & harmonia['Ruim'], conceito['Ruim'])
    regra8 = ctrl.Rule(enredo['Ruim'] & comissao['Ruim'] & evolução['Bom'] & harmonia['Mediana'], conceito['Mediano'])
    regra9 = ctrl.Rule(enredo['Ruim'] & comissao['Ruim'] & evolução['Bom'] & harmonia['Boa'], conceito['Mediano'])
    regra10 = ctrl.Rule(enredo['Ruim'] & comissao['Mediano'] & evolução['Ruim'] & harmonia['Ruim'], conceito['Ruim'])
    regra11 = ctrl.Rule(enredo['Ruim'] & comissao['Mediano'] & evolução['Ruim'] & harmonia['Mediana'], conceito['Ruim'])
    regra12 = ctrl.Rule(enredo['Ruim'] & comissao['Mediano'] & evolução['Ruim'] & harmonia['Boa'], conceito['Mediano'])
    regra13 = ctrl.Rule(enredo['Ruim'] & comissao['Mediano'] & evolução['Mediano'] & harmonia['Ruim'], conceito['Ruim'])
    regra14 = ctrl.Rule(enredo['Ruim'] & comissao['Mediano'] & evolução['Mediano'] & harmonia['Mediana'], conceito['Mediano'])
    regra15 = ctrl.Rule(enredo['Ruim'] & comissao['Mediano'] & evolução['Mediano'] & harmonia['Boa'], conceito['Mediano'])
    regra16 = ctrl.Rule(enredo['Ruim'] & comissao['Mediano'] & evolução['Bom'] & harmonia['Ruim'], conceito['Mediano'])
    regra17 = ctrl.Rule(enredo['Ruim'] & comissao['Mediano'] & evolução['Bom'] & harmonia['Mediana'], conceito['Mediano'])
    regra18 = ctrl.Rule(enredo['Ruim'] & comissao['Mediano'] & evolução['Bom'] & harmonia['Boa'], conceito['Bom'])
    regra19 = ctrl.Rule(enredo['Ruim'] & comissao['Bom'] & evolução['Ruim'] & harmonia['Ruim'], conceito['Ruim'])
    regra20 = ctrl.Rule(enredo['Ruim'] & comissao['Bom'] & evolução['Ruim'] & harmonia['Mediana'], conceito['Mediano'])
    regra21 = ctrl.Rule(enredo['Ruim'] & comissao['Bom'] & evolução['Ruim'] & harmonia['Boa'], conceito['Mediano'])
    regra22 = ctrl.Rule(enredo['Ruim'] & comissao['Bom'] & evolução['Mediano'] & harmonia['Ruim'], conceito['Mediano'])
    regra23 = ctrl.Rule(enredo['Ruim'] & comissao['Bom'] & evolução['Mediano'] & harmonia['Mediana'], conceito['Mediano'])
    regra24 = ctrl.Rule(enredo['Ruim'] & comissao['Bom'] & evolução['Mediano'] & harmonia['Boa'], conceito['Bom'])
    regra25 = ctrl.Rule(enredo['Ruim'] & comissao['Bom'] & evolução['Bom'] & harmonia['Ruim'], conceito['Mediano'])
    regra26 = ctrl.Rule(enredo['Ruim'] & comissao['Bom'] & evolução['Bom'] & harmonia['Mediana'], conceito['Bom'])
    regra27 = ctrl.Rule(enredo['Ruim'] & comissao['Bom'] & evolução['Bom'] & harmonia['Boa'], conceito['Bom'])
    regra28 = ctrl.Rule(enredo['Mediano'] & comissao['Ruim'] & evolução['Ruim'] & harmonia['Ruim'], conceito['Ruim'])
    regra29 = ctrl.Rule(enredo['Mediano'] & comissao['Ruim'] & evolução['Ruim'] & harmonia['Mediana'], conceito['Ruim'])
    regra30 = ctrl.Rule(enredo['Mediano'] & comissao['Ruim'] & evolução['Ruim'] & harmonia['Boa'], conceito['Mediano'])
    regra31 = ctrl.Rule(enredo['Mediano'] & comissao['Ruim'] & evolução['Mediano'] & harmonia['Ruim'], conceito['Ruim'])
    regra32 = ctrl.Rule(enredo['Mediano'] & comissao['Ruim'] & evolução['Mediano'] & harmonia['Mediana'], conceito['Mediano'])
    regra33 = ctrl.Rule(enredo['Mediano'] & comissao['Ruim'] & evolução['Mediano'] & harmonia['Boa'], conceito['Mediano'])
    regra34 = ctrl.Rule(enredo['Mediano'] & comissao['Ruim'] & evolução['Bom'] & harmonia['Ruim'], conceito['Mediano'])
    regra35 = ctrl.Rule(enredo['Mediano'] & comissao['Ruim'] & evolução['Bom'] & harmonia['Mediana'], conceito['Mediano'])
    regra36 = ctrl.Rule(enredo['Mediano'] & comissao['Ruim'] & evolução['Bom'] & harmonia['Boa'], conceito['Bom'])
    regra37 = ctrl.Rule(enredo['Mediano'] & comissao['Mediano'] & evolução['Ruim'] & harmonia['Ruim'], conceito['Ruim'])
    regra38 = ctrl.Rule(enredo['Mediano'] & comissao['Mediano'] & evolução['Ruim'] & harmonia['Mediana'], conceito['Mediano'])
    regra39 = ctrl.Rule(enredo['Mediano'] & comissao['Mediano'] & evolução['Ruim'] & harmonia['Boa'], conceito['Mediano'])
    regra40 = ctrl.Rule(enredo['Mediano'] & comissao['Mediano'] & evolução['Mediano'] & harmonia['Ruim'], conceito['Mediano'])
    regra41 = ctrl.Rule(enredo['Mediano'] & comissao['Mediano'] & evolução['Mediano'] & harmonia['Mediana'], conceito['Mediano'])
    regra42 = ctrl.Rule(enredo['Mediano'] & comissao['Mediano'] & evolução['Mediano'] & harmonia['Boa'], conceito['Mediano'])
    regra43 = ctrl.Rule(enredo['Mediano'] & comissao['Mediano'] & evolução['Bom'] & harmonia['Ruim'], conceito['Mediano'])
    regra44 = ctrl.Rule(enredo['Mediano'] & comissao['Mediano'] & evolução['Bom'] & harmonia['Mediana'], conceito['Mediano'])
    regra45 = ctrl.Rule(enredo['Mediano'] & comissao['Mediano'] & evolução['Bom'] & harmonia['Boa'], conceito['Bom'])
    regra46 = ctrl.Rule(enredo['Mediano'] & comissao['Bom'] & evolução['Ruim'] & harmonia['Ruim'], conceito['Mediano'])
    regra47 = ctrl.Rule(enredo['Mediano'] & comissao['Bom'] & evolução['Ruim'] & harmonia['Mediana'], conceito['Mediano'])
    regra48 = ctrl.Rule(enredo['Mediano'] & comissao['Bom'] & evolução['Ruim'] & harmonia['Boa'], conceito['Bom'])
    regra49 = ctrl.Rule(enredo['Mediano'] & comissao['Bom'] & evolução['Mediano'] & harmonia['Ruim'], conceito['Mediano'])
    regra50 = ctrl.Rule(enredo['Mediano'] & comissao['Bom'] & evolução['Mediano'] & harmonia['Mediana'], conceito['Mediano'])
    regra51 = ctrl.Rule(enredo['Mediano'] & comissao['Bom'] & evolução['Mediano'] & harmonia['Boa'], conceito['Bom'])
    regra52 = ctrl.Rule(enredo['Mediano'] & comissao['Bom'] & evolução['Bom'] & harmonia['Ruim'], conceito['Bom'])
    regra53 = ctrl.Rule(enredo['Mediano'] & comissao['Bom'] & evolução['Bom'] & harmonia['Mediana'], conceito['Bom'])
    regra54 = ctrl.Rule(enredo['Mediano'] & comissao['Bom'] & evolução['Bom'] & harmonia['Boa'], conceito['Bom'])
    regra55 = ctrl.Rule(enredo['Bom'] & comissao['Ruim'] & evolução['Ruim'] & harmonia['Ruim'], conceito['Ruim'])
    regra56 = ctrl.Rule(enredo['Bom'] & comissao['Ruim'] & evolução['Ruim'] & harmonia['Mediana'], conceito['Mediano'])
    regra57 = ctrl.Rule(enredo['Bom'] & comissao['Ruim'] & evolução['Ruim'] & harmonia['Boa'], conceito['Mediano'])
    regra58 = ctrl.Rule(enredo['Bom'] & comissao['Ruim'] & evolução['Mediano'] & harmonia['Ruim'], conceito['Mediano'])
    regra59 = ctrl.Rule(enredo['Bom'] & comissao['Ruim'] & evolução['Mediano'] & harmonia['Mediana'], conceito['Mediano'])
    regra60 = ctrl.Rule(enredo['Bom'] & comissao['Ruim'] & evolução['Mediano'] & harmonia['Boa'], conceito['Bom'])
    regra61 = ctrl.Rule(enredo['Bom'] & comissao['Ruim'] & evolução['Bom'] & harmonia['Ruim'], conceito['Mediano'])
    regra62 = ctrl.Rule(enredo['Bom'] & comissao['Ruim'] & evolução['Bom'] & harmonia['Mediana'], conceito['Bom'])
    regra63 = ctrl.Rule(enredo['Bom'] & comissao['Ruim'] & evolução['Bom'] & harmonia['Boa'], conceito['Bom'])
    regra64 = ctrl.Rule(enredo['Bom'] & comissao['Mediano'] & evolução['Ruim'] & harmonia['Ruim'], conceito['Mediano'])
    regra65 = ctrl.Rule(enredo['Bom'] & comissao['Mediano'] & evolução['Ruim'] & harmonia['Mediana'], conceito['Mediano'])
    regra66 = ctrl.Rule(enredo['Bom'] & comissao['Mediano'] & evolução['Ruim'] & harmonia['Boa'], conceito['Bom'])
    regra67 = ctrl.Rule(enredo['Bom'] & comissao['Mediano'] & evolução['Mediano'] & harmonia['Ruim'], conceito['Mediano'])
    regra68 = ctrl.Rule(enredo['Bom'] & comissao['Mediano'] & evolução['Mediano'] & harmonia['Mediana'], conceito['Mediano'])
    regra69 = ctrl.Rule(enredo['Bom'] & comissao['Mediano'] & evolução['Mediano'] & harmonia['Boa'], conceito['Bom'])
    regra70 = ctrl.Rule(enredo['Bom'] & comissao['Mediano'] & evolução['Bom'] & harmonia['Ruim'], conceito['Bom'])
    regra71 = ctrl.Rule(enredo['Bom'] & comissao['Mediano'] & evolução['Bom'] & harmonia['Mediana'], conceito['Bom'])
    regra72 = ctrl.Rule(enredo['Bom'] & comissao['Mediano'] & evolução['Bom'] & harmonia['Boa'], conceito['Bom'])
    regra73 = ctrl.Rule(enredo['Bom'] & comissao['Bom'] & evolução['Ruim'] & harmonia['Ruim'], conceito['Mediano'])
    regra74 = ctrl.Rule(enredo['Bom'] & comissao['Bom'] & evolução['Ruim'] & harmonia['Mediana'], conceito['Bom'])
    regra75 = ctrl.Rule(enredo['Bom'] & comissao['Bom'] & evolução['Ruim'] & harmonia['Boa'], conceito['Bom'])
    regra76 = ctrl.Rule(enredo['Bom'] & comissao['Bom'] & evolução['Mediano'] & harmonia['Ruim'], conceito['Bom'])
    regra77 = ctrl.Rule(enredo['Bom'] & comissao['Bom'] & evolução['Mediano'] & harmonia['Mediana'], conceito['Bom'])
    regra78 = ctrl.Rule(enredo['Bom'] & comissao['Bom'] & evolução['Mediano'] & harmonia['Boa'], conceito['Bom'])
    regra79 = ctrl.Rule(enredo['Bom'] & comissao['Bom'] & evolução['Bom'] & harmonia['Ruim'], conceito['Bom'])
    regra80 = ctrl.Rule(enredo['Bom'] & comissao['Bom'] & evolução['Bom'] & harmonia['Mediana'], conceito['Bom'])
    regra81 = ctrl.Rule(enredo['Bom'] & comissao['Bom'] & evolução['Bom'] & harmonia['Boa'], conceito['Bom'])
   
    """----- Analisador -------"""
    analisador = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, 
    regra8, regra9, regra10,
    regra11, regra12, regra13, regra14, regra15, regra16, regra17,
    regra18, regra19, regra20, regra21, regra22, regra23, regra24, regra25, regra26, 
    regra27, regra28, regra29, regra30,
    regra31, regra32, regra33, regra34, regra35, regra36, regra37, regra38, regra39, regra40,
    regra41, regra42, regra43, regra44, regra45, regra46, regra47, regra48, regra49, 
    regra50, regra51, regra52, regra53, regra54, regra55, regra56, regra57, regra58, regra59, regra60,
    regra61, regra62, regra63, regra64, regra65, regra66, regra67, regra68, regra69, regra70,
    regra71, regra72, regra73, regra74, regra75, regra76, regra77, regra78, regra79, regra80,
    regra81])
    
    apurador = ctrl.ControlSystemSimulation(analisador)

    """------ inserção dos valores-------"""
    apurador.input["Comissão de Frente"]=paginaNovaApuração.boxComissao.value()
    apurador.input["Evolução"]=paginaNovaApuração.boxEvolucao.value()
    apurador.input["Harmonia"]=paginaNovaApuração.boxHarmonia.value()
    apurador.input["Enredo"]=paginaNovaApuração.boxEnredo.value()

    apurador.compute()
    print("conceito final: ",apurador.output["Conceito Final"])
    conceito.view(sim=apurador)

    conexãoSqlInsercaoDeApuracao(paginaNovaApuração.boxSenha.toPlainText(),
                                 paginaNovaApuração.boxEscola.toPlainText(),
                                 paginaNovaApuração.boxAno.toPlainText(),
                                 round(apurador.output["Conceito Final"],2))
    
def paginaHistoricoInterface():
    global paginaHistorico
    paginaHistorico = uic.loadUi("paginaHistorico.ui")
    paginaHistorico.show()
    paginaHistorico.botaoVoltar.clicked.connect(botaoVoltarHistorico)
    paginaHistorico.botaoIr.clicked.connect(conecãoSqlVisualizarHistorico)

def paginaSobreInterface():
    global paginaSobre
    paginaSobre = uic.loadUi("Sobre.ui")
    paginaSobre.show()
    paginaSobre.voltarBotao.clicked.connect(botaoVoltarSobre)

def paginaIncialInterface ():
    global paginaInicial
    paginaInicial = uic.loadUi("paginainicial.ui")
    paginaInicial.show()
    paginaInicial.novaApuracaoBotao.clicked.connect(botaoNovaApuraçãoClicado)
    paginaInicial.historicoBotao.clicked.connect(botaoHistoricoClicado)
    paginaInicial.Sobre.clicked.connect(paginaSobreInterface)

def paginaNovaApuraçãoInterface():
    global paginaNovaApuração
    paginaNovaApuração = uic.loadUi("novaApuração.ui")
    paginaNovaApuração.show()
    paginaNovaApuração.botaoApurar.clicked.connect(botaoApurarClicado)
    paginaNovaApuração.botaoVoltar.clicked.connect(botaoVoltarNovaApuração)

def incicialzação():
    aplicação = QtWidgets.QApplication(sys.argv)
    paginaIncialInterface()
    aplicação.exec()

incicialzação()