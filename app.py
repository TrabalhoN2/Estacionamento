import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from tools.mongo import buscarCliente, buscarFuncionario, cadastroCliente, cadastroFuncionario, listarCadastrosClientes, listarVagasDB, updateStatusVaga, updateVagaCliente, vagasDB, vagasCliente, updateVaga

from src.funcionario.homeFuncionario import *
from src.funcionario.cadastrosFuncionario import *
from src.funcionario.vagasFuncionario import *
from src.funcionario.estacionamentoFuncionario import *
from src.funcionario.mudarStatusFuncionario import *
from src.funcionario.alugarFuncionario import *
from src.funcionario.reservarFuncionario import *
from src.funcionario.realizarCadastroFuncionario import *

from src.cliente.homeCliente import *
from src.cliente.vagasCliente import *
from src.cliente.alugarCliente import *
from src.cliente.estacionamentoCliente import *
from src.cliente.reservasCliente import *
from src.cliente.reservarCliente import *

from src.login import *
from src.cadastrarFuncionario import *
from src.cadastrarCliente import *
from src.confirmarReserva import *
from src.confirmacaoPagamento import *
from src.confirmarPagamento import *
from src.confirmarAlteracao import *


class telaHomeFuncionario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomeFuncionario()
        self.ui.setupUi(self)

        self.ui.btnCadastros.clicked.connect(self.mudarJanelaCadastros)
        self.ui.btnVagas.clicked.connect(self.mudarJanelaVagas)
        self.ui.btnEstacionamento.clicked.connect(self.mudarJanelaEstacionamento)
        self.ui.btnAlugar.clicked.connect(self.mudarJanelaAlugar)
        self.ui.btnReservas.clicked.connect(self.mudarJanelaReservar)   # Mudar o nome do botão
        self.ui.btnSair.clicked.connect(self.sair)

    @QtCore.pyqtSlot()
    def mudarJanelaCadastros(self):
        self.janelaCadastros = telaCadastrosFuncionario()
        self.janelaCadastros.show()
        self.hide()

    @QtCore.pyqtSlot()
    def mudarJanelaVagas(self):
        self.janelaVagas = telaVagasFuncionario()
        self.janelaVagas.show()
        self.hide()

    @QtCore.pyqtSlot()
    def mudarJanelaEstacionamento(self):
        self.janelaEstacionamento = telaEstacionamentoFuncionario()
        self.janelaEstacionamento.show()
        self.hide()

    @QtCore.pyqtSlot()
    def mudarJanelaAlugar(self):
        self.janelaAlugueis = telaAlugarFuncionario()
        self.janelaAlugueis.show()
        self.hide()

    @QtCore.pyqtSlot()
    def mudarJanelaReservar(self):
        self.janelaReserva = telaReservarFuncionario()
        self.janelaReserva.show()
        self.hide()

    @QtCore.pyqtSlot()
    def sair(self):
        self.close()


class telaCadastrosFuncionario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CadastrosFuncionario()
        self.ui.setupUi(self)

        documento = listarCadastrosClientes()

        tamanho = documento.collection.count_documents({})

        self.ui.tableCadastros.setRowCount(tamanho)
        self.ui.tableCadastros.setColumnCount(5)

        i = 0
        while i < tamanho:
            self.ui.tableCadastros.setItem(i, 0, QTableWidgetItem(documento[i]["Nome"]))
            self.ui.tableCadastros.setItem(i, 1, QTableWidgetItem(documento[i]["CPF"]))
            self.ui.tableCadastros.setItem(i, 2, QTableWidgetItem(documento[i]["Telefone"]))
            self.ui.tableCadastros.setItem(i, 3, QTableWidgetItem(documento[i]["Placa"]))
            self.ui.tableCadastros.setItem(i, 4, QTableWidgetItem(documento[i]["Endereco"]))
            
            i += 1

        self.ui.btnHome.clicked.connect(self.mudarJanelaHomeFuncionario)
        self.ui.btnVagas.clicked.connect(self.mudarJanelaVagasFuncionario)
        self.ui.btnEstacionamento.clicked.connect(self.mudarJanelaEstacionamentoFuncionario)
        self.ui.btnSair.clicked.connect(self.sair)

        self.ui.btnNovoCadastro.clicked.connect(self.novoCadastro)
    
    @QtCore.pyqtSlot()
    def mudarJanelaHomeFuncionario(self):
        self.janelaHomeFuncionario = telaHomeFuncionario()
        self.janelaHomeFuncionario.show()
        self.close()

    @QtCore.pyqtSlot()
    def mudarJanelaVagasFuncionario(self):
        self.janelaVagas = telaVagasFuncionario()
        self.janelaVagas.show()
        self.close()
    
    @QtCore.pyqtSlot()
    def mudarJanelaEstacionamentoFuncionario(self):
        self.janelaEstacionamento = telaEstacionamentoFuncionario()
        self.janelaEstacionamento.show()
        self.close()

    @QtCore.pyqtSlot()
    def sair(self):
        self.close()

    @QtCore.pyqtSlot()
    def novoCadastro(self):
        self.janelaRealizarCadastro = telaRealizarCadastroFuncionario()
        self.janelaRealizarCadastro.show()
        self.close()


class telaVagasFuncionario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VagasFuncionario()
        self.ui.setupUi(self)

        self.ui.tableVagas.setRowCount(20)
        self.ui.tableVagas.setColumnCount(4)

        documento = listarVagasDB()

        i = 0
        while i < 20:
            self.ui.tableVagas.setItem(i, 0, QTableWidgetItem(documento[i]["Vaga"]))
            self.ui.tableVagas.setItem(i, 1, QTableWidgetItem(documento[i]["Status"]))
            self.ui.tableVagas.setItem(i, 2, QTableWidgetItem(documento[i]["Aluguel"]))
            self.ui.tableVagas.setItem(i, 3, QTableWidgetItem(documento[i]["Tempo"]))
            i += 1

        self.ui.btnHome.clicked.connect(self.mudarJanelaHomeFuncionario)
        self.ui.btnCadastros.clicked.connect(self.mudarJanelaCadastrosFuncionario)
        self.ui.btnEstacionamento.clicked.connect(self.mudarJanelaEstacionamentoFuncionario)
        self.ui.btnSair.clicked.connect(self.sair)

        self.ui.btnMudarStatus.clicked.connect(self.mudarStatus)
        self.ui.btnAlugar.clicked.connect(self.alugarVaga)
        self.ui.btnReservar.clicked.connect(self.reservarVaga)
    
    @QtCore.pyqtSlot()
    def mudarJanelaHomeFuncionario(self):
        self.janelaHomeFuncionario = telaHomeFuncionario()
        self.janelaHomeFuncionario.show()
        self.close()

    @QtCore.pyqtSlot()
    def mudarJanelaCadastrosFuncionario(self):
        self.janelaCadastrosFuncionario = telaCadastrosFuncionario()
        self.janelaCadastrosFuncionario.show()
        self.close()
    
    @QtCore.pyqtSlot()
    def mudarJanelaEstacionamentoFuncionario(self):
        self.janelaEstacionamentoFuncionario = telaEstacionamentoFuncionario()
        self.janelaEstacionamentoFuncionario.show()
        self.close()

    @QtCore.pyqtSlot()
    def sair(self):
        self.close()

    @QtCore.pyqtSlot()
    def mudarStatus(self):
        self.janelaMudarStatus = telaMudarStatusFuncionario()
        self.janelaMudarStatus.show()
        self.close()

    @QtCore.pyqtSlot()
    def alugarVaga(self):
        self.janelaAlugarVaga = telaAlugarFuncionario()
        self.janelaAlugarVaga.show()
        self.close()
    
    @QtCore.pyqtSlot()
    def reservarVaga(self):
        self.janelaReservarVaga = telaReservarFuncionario()
        self.janelaReservarVaga.show()
        self.close()


class telaEstacionamentoFuncionario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_EstacionamentoFuncionario()
        self.ui.setupUi(self)

        self.ui.btnHome.clicked.connect(self.mudarJanelaHomeFuncionario)
        self.ui.btnCadastros.clicked.connect(self.mudarJanelaCadastrosFuncionario)
        self.ui.btnVagas.clicked.connect(self.mudarJanelaVagasFuncionario)
        self.ui.btnAlugar.clicked.connect(self.mudarJanelaAlugarFuncionario)
        self.ui.btnReservar.clicked.connect(self.mudarJanelaReservarFuncionario)
        self.ui.btnSair.clicked.connect(self.sair)

        self.ui.btnMudarStatus.clicked.connect(self.mudarJanelaMudarStatus)

    @QtCore.pyqtSlot()
    def mudarJanelaHomeFuncionario(self):
        self.janelaHomeFuncionario = telaHomeFuncionario()
        self.janelaHomeFuncionario.show()
        self.close()

    @QtCore.pyqtSlot()
    def mudarJanelaCadastrosFuncionario(self):
        self.janelaCadastros = telaCadastrosFuncionario()
        self.janelaCadastros.show()
        self.close()

    @QtCore.pyqtSlot()
    def mudarJanelaVagasFuncionario(self):
        self.janelaVagas = telaVagasFuncionario()
        self.janelaVagas.show()
        self.close()

    @QtCore.pyqtSlot()
    def mudarJanelaAlugarFuncionario(self):
        self.janelaAlugar = telaAlugarFuncionario()
        self.janelaAlugar.show()
        self.close()

    @QtCore.pyqtSlot()
    def mudarJanelaReservarFuncionario(self):
        self.janelaReservar = telaReservarFuncionario()
        self.janelaReservar.show()
        self.close()

    @QtCore.pyqtSlot()
    def sair(self):
        self.close()

    @QtCore.pyqtSlot()
    def mudarJanelaMudarStatus(self):
        self.janelaMudarStatus = telaMudarStatusFuncionario()
        self.janelaMudarStatus.show()
        self.close()


class telaMudarStatusFuncionario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MudarStatusFuncionario()
        self.ui.setupUi(self)
        
        numeroVaga = self.ui.numeroVaga.currentText()
        row = vagasDB(str(numeroVaga))
        if row["Status"] == "Vazia":
            self.ui.vagaLivre.setChecked(True)
        elif row["Status"] == "Alugada":
            self.ui.vagaOcupada.setChecked(True)
        else:
            self.ui.vagaReservada.setChecked(True)
        
        self.ui.btnVerificarVaga.clicked.connect(self.verificar)

        self.ui.btnConfirmar.clicked.connect(self.confirmarAlteracao)
        self.ui.btnCancelar.clicked.connect(self.cancelarAlteracao)
    
    @QtCore.pyqtSlot()
    def verificar(self):
        numeroVaga = self.ui.numeroVaga.currentText()
        row = vagasDB(str(numeroVaga))
        if row["Status"] == "Vazia":
            self.ui.vagaLivre.setChecked(True)
        elif row["Status"] == "Alugada":
            self.ui.vagaOcupada.setChecked(True)
        else:
            self.ui.vagaReservada.setChecked(True)

    @QtCore.pyqtSlot()
    def alteracao(self):
        vaga = str(self.ui.numeroVaga.currentText())
        status = str(self.getSituacao())
        if status == "Vazia":
            documento = {
                "Nome": "",
                "Placa": "",
                "Vaga": vaga,
                "Status": "Vazia",
                "Data": "", 
                "Tempo": "",
                "Aluguel": ""
            }
            updateVaga(documento)
        else:
            updateStatusVaga(vaga, status)

    @QtCore.pyqtSlot()
    def getSituacao(self):
        if self.ui.vagaLivre.isChecked():
            return 'Vazia'
        elif self.ui.vagaOcupada.isChecked():
            return 'Alugada'
        else:
            return 'Reservada'

    @QtCore.pyqtSlot()
    def confirmarAlteracao(self):
        self.alteracao()
        self.alteracao = telaConfirmarAlteracao()
        self.alteracao.show()
        self.close()

    @QtCore.pyqtSlot()
    def cancelarAlteracao(self):
        self.janelaHomeFuncionario = telaHomeFuncionario()
        self.janelaHomeFuncionario.show()
        self.close()


class telaAlugarFuncionario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AlugarVaga()
        self.ui.setupUi(self)

        self.ui.btnConfirmar.clicked.connect(self.confirmar)
        self.ui.btnCancelar.clicked.connect(self.cancelar)

    @QtCore.pyqtSlot()
    def getNome(self):
        return self.ui.nomeCliente.text()

    @QtCore.pyqtSlot()
    def getPlaca(self):
        return self.ui.placa.text()
    
    @QtCore.pyqtSlot()
    def getNumeroVaga(self):
        return self.ui.numeroVaga.currentText()
    
    @QtCore.pyqtSlot()
    def getData(self):
        return self.ui.dataAluguel.text()
    
    @QtCore.pyqtSlot()
    def getIntervaloTempo(self):
        return self.ui.intervaloAluguel.currentText()

    @QtCore.pyqtSlot()
    def getValor(self):
        return self.ui.valorAluguel.text()

    @QtCore.pyqtSlot()
    def confirmar(self):
        documento = {
            'Nome': str(self.getNome()),
            'Placa': str(self.getPlaca()),
            'Vaga': str(self.getNumeroVaga()),
            'Status': 'Alugada',
            'Data': str(self.getData()),
            'Tempo': str(self.getIntervaloTempo()),
            'Aluguel': str(self.getValor()),
        }
        updateVaga(documento)
        self.confirmacaoPagamento = telaConfirmacaoPagamento()
        self.confirmacaoPagamento.show()
        self.close()

    @QtCore.pyqtSlot()
    def cancelar(self):
        self.janelaHomeFuncionario = telaHomeFuncionario()
        self.janelaHomeFuncionario.show()
        self.close()


class telaReservarFuncionario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ReservarVaga()
        self.ui.setupUi(self)

        self.ui.btnConfirmar.clicked.connect(self.confirmar)
        self.ui.btnCancelar.clicked.connect(self.cancelar)

    @QtCore.pyqtSlot()
    def getNome(self):
        return self.ui.nomeCliente.text()
    
    @QtCore.pyqtSlot()
    def getPlaca(self):
        return self.ui.placa.text()

    @QtCore.pyqtSlot()
    def getNumeroVaga(self):
        return self.ui.numeroVaga.currentText()

    @QtCore.pyqtSlot()
    def getData(self):
        return self.ui.dataReserva.text()

    @QtCore.pyqtSlot()
    def getIntervaloTempo(self):
        return self.ui.intervaloReserva.currentText()

    @QtCore.pyqtSlot()
    def confirmar(self):
        documento = {
            'Nome': str(self.getNome()),
            'Placa': str(self.getPlaca()),
            'Status': 'Reservada',
            'Vaga': str(self.getNumeroVaga()),
            'Data': str(self.getData()),
            'Tempo': str(self.getIntervaloTempo()),
            'Aluguel': "",
        }
        updateVaga(documento)
        self.janelaConfirmarReserva = telaConfirmarReserva()
        self.janelaConfirmarReserva.show()
        self.close()
    
    @QtCore.pyqtSlot()
    def cancelar(self):
        self.janelaHomeFuncionario = telaHomeFuncionario()
        self.janelaHomeFuncionario.show()
        self.close()


class telaRealizarCadastroFuncionario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CadastrarCliente()
        self.ui.setupUi(self)

        self.ui.vip.setChecked(True)  # Seleciona a opção de torna-se Vip por padrão
        self.ui.btnSalvar.clicked.connect(self.salvar)  # Quando clicar no botão salvar

    @QtCore.pyqtSlot()           
    def getNomeCompleto(self):          # Fuções para pegar o texto digitado nos campos
        return self.ui.nome_completo.text()
    
    @QtCore.pyqtSlot()
    def getCPF(self):
        return self.ui.cpf.text()

    @QtCore.pyqtSlot()
    def getPlacaVeiculo(self):
        return self.ui.placa.text()

    @QtCore.pyqtSlot()
    def getNumeroTelefone(self):
        return self.ui.telefone.text()

    @QtCore.pyqtSlot()
    def getEndereco(self):
        return self.ui.endereco.text()

    @QtCore.pyqtSlot()
    def getCategoria(self):
        return self.ui.vip.isChecked()

    @QtCore.pyqtSlot()
    def salvar(self):           # Função que envia um documento para o MongoDB(base de dados)
        documento = {'Nome': str(self.getNomeCompleto()),
                     'CPF': str(self.getCPF()),
                     'Placa': str(self.getPlacaVeiculo()),
                     'Telefone': str(self.getNumeroTelefone()),
                     'Endereco': str(self.getEndereco()),
                     'VIP': str(self.getCategoria())
                    }
        cadastroCliente(documento)     
        self.janelaCadastro = telaCadastrosFuncionario()
        self.janelaCadastro.show()
        self.close()


class telaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.radioButtonCliente.setChecked(True)
        self.ui.frameErro.hide()

        self.ui.btnCadastrar.clicked.connect(self.mudarJanelaCadastrar)  # Quando clicar no botão cadastra-se
        self.ui.btnEntrar.clicked.connect(self.usuarioLogin)

    @QtCore.pyqtSlot()
    def getUsuario(self):
        return self.ui.nome_usuario.text()

    @QtCore.pyqtSlot()
    def getSenha(self):
        return self.ui.senha_usuario.text()

    @QtCore.pyqtSlot()
    def usuarioLogin(self):
        if (self.ui.radioButtonCliente.isChecked()):
            self.entrarCliente()
        else:
            self.entrarFuncionario()

    @QtCore.pyqtSlot()
    def mudarJanelaCadastrar(self):
        if (self.ui.radioButtonCliente.isCheckable()):
            self.janelaCadastro = telaCadastroCliente()  # Cria uma referência para a janela de cadastro
            self.janelaCadastro.show()  # Chama a janela de cadastro
            self.hide()  # Esconde a janela de login
        elif (self.ui.radioButtonFuncionario.isCheckable()):
            self.janelaCadastro = telaCadastroFuncionario()  # Cria uma referência para a janela de cadastro
            self.janelaCadastro.show()  # Chama a janela de cadastro
            self.hide()  # Esconde a janela de login

    @QtCore.pyqtSlot()
    def fecharFrame(self):
        self.ui.frameErro.hide()

    @QtCore.pyqtSlot()
    def entrarCliente(self):
        if self.checarCampos():
            usuario = str(self.getUsuario())
            senha = str(self.getSenha())
            if (buscarCliente(usuario, senha)):
                self.janelaHomeCliente = telaHomeCliente([usuario, senha])
                self.janelaHomeCliente.show()
                self.close()
            else:
                self.mostrarMensagem("Usuário não cadastrado.")
                self.ui.btnFecharFrameErro.clicked.connect(self.fecharFrame)
        else:
            self.ui.btnFecharFrameErro.clicked.connect(self.fecharFrame)

    @QtCore.pyqtSlot()
    def entrarFuncionario(self):
        if self.checarCampos():
            usuario = str(self.getUsuario())
            senha = str(self.getSenha())
            if (buscarFuncionario(usuario, senha)):
                self.janelaHomeFuncionario = telaHomeFuncionario()
                self.janelaHomeFuncionario.show()
                self.close()
            else:
                self.mostrarMensagem("Usuário não cadastrado.")
                self.ui.btnFecharFrameErro.clicked.connect(self.fecharFrame)
        else:
            self.ui.btnFecharFrameErro.clicked.connect(self.fecharFrame)

    @QtCore.pyqtSlot()
    def mostrarMensagem(self, mensagem):
        self.ui.frameErro.show()
        self.ui.loginIncorreto.setText(mensagem)

    @QtCore.pyqtSlot()
    def checarCampos(self):
        campoUsuario = ''
        campoSenha = ''

        if not self.ui.nome_usuario.text():
            campoUsuario = ' Campo de Usuário Vazio. '
        else:
            campoUsuario = ''

        if not self.ui.senha_usuario.text():
            campoSenha = ' Campo de Senha Vazio. '
        else:
            campoSenha = ''

        if campoUsuario + campoSenha != '':
            mensagem = campoUsuario + campoSenha
            self.mostrarMensagem(mensagem)
            return False
        else:
            mensagem = ' Login Ok. '
            self.mostrarMensagem(mensagem)
            return True


class telaCadastroFuncionario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CadastrarFuncionario()
        self.ui.setupUi(self)

        self.ui.btnCadastrar.clicked.connect(self.cadastrarFuncionario)    # Quando clicar no botão
        self.ui.btnCadastrar.clicked.connect(self.mudarJanelaLogin)  # Quando clicar no botão

    @QtCore.pyqtSlot()
    def mudarJanelaLogin(self):          # Função que esconde a janela de cadastro após o cadastro e volta para a de login
        self.telaLogin = telaLogin()
        self.telaLogin.show()
        self.close()

    @QtCore.pyqtSlot()
    def closeEvent(self, evento):   # Função que fecha a janela de cadastro e volta para a de login
        self.telaLogin = telaLogin()
        self.telaLogin.show()
        evento.accept()

    @QtCore.pyqtSlot()
    def getNome(self):       # Fuções para pegar o texto digitado nos campos
        return self.ui.nome_usuario.text()

    @QtCore.pyqtSlot()
    def getSenha(self):
        return self.ui.senha.text()

    @QtCore.pyqtSlot()       # Função que envia um documento para o MongoDB(base de dados)
    def cadastrarFuncionario(self):
        documento = {
            "UserName": str(self.getNome()),
            "Password": str(self.getSenha()),
        }
        cadastroFuncionario(documento)


class telaCadastroCliente(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CadastrarCliente()
        self.ui.setupUi(self)

        self.ui.btnCadastrar.clicked.connect(self.cadastrarCliente)    # Quando clicar no botão
        self.ui.btnCadastrar.clicked.connect(self.mudarJanelaLogin)  # Quando clicar no botão

    @QtCore.pyqtSlot()
    def mudarJanelaLogin(self):          # Função que esconde a janela de cadastro após o cadastro e volta para a de login
        self.telaLogin = telaLogin()
        self.telaLogin.show()
        self.close()

    @QtCore.pyqtSlot()
    def closeEvent(self, evento):   # Função que fecha a janela de cadastro e volta para a de login
        self.telaLogin = telaLogin()
        self.telaLogin.show()
        evento.accept()

    @QtCore.pyqtSlot()
    def getNome(self):       # Fuções para pegar o texto digitado nos campos
        return self.ui.nome_usuario.text()

    @QtCore.pyqtSlot()
    def getSenha(self):
        return self.ui.senha.text()

    @QtCore.pyqtSlot()       # Função que envia um documento para o MongoDB(base de dados)
    def cadastrarCliente(self):
        documento = {
            "user": str(self.getNome()),
            "password": str(self.getSenha()),
        }
        cadastroCliente(documento)


class telaConfirmacaoPagamento(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ConfirmacaoPagamento()
        self.ui.setupUi(self)

        self.ui.btnConfirmar.clicked.connect(self.confirmar)
        self.ui.btnCancelar.clicked.connect(self.cancelar)
    
    @QtCore.pyqtSlot()
    def confirmar(self):
        self.janelaConfirmar = telaConfirmarPagamento()
        self.janelaConfirmar.show()
        self.close()
    
    @QtCore.pyqtSlot()
    def cancelar(self):
        self.janelaHome = telaHomeFuncionario()
        self.janelaHome.show()
        self.close()


class telaConfirmarPagamento(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ConfirmarPagamento()
        self.ui.setupUi(self)

        self.ui.btnFechar.clicked.connect(self.fechar)

    @QtCore.pyqtSlot()
    def fechar(self):
        self.janelaHome = telaHomeFuncionario()
        self.janelaHome.show()
        self.close()


class telaConfirmarAlteracao(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ConfirmarAlteracao()
        self.ui.setupUi(self)

        self.ui.btnFechar.clicked.connect(self.fechar)

    @QtCore.pyqtSlot()
    def fechar(self):
        self.janelaHome = telaHomeFuncionario()
        self.janelaHome.show()
        self.close()


class telaConfirmarReserva(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ConfirmarReserva()
        self.ui.setupUi(self)

        self.ui.btnFechar.clicked.connect(self.fechar)

    @QtCore.pyqtSlot()
    def fechar(self):
        self.janelaHomeFuncionario = telaHomeFuncionario()
        self.janelaHomeFuncionario.show()
        self.close()


class telaHomeCliente(QMainWindow):
    def __init__(self, informacao:list):
        super().__init__()
        self.ui = Ui_HomeCliente()
        self.ui.setupUi(self)

        self.user = informacao[0]
        self.password = informacao[1]

        self.ui.btnVagas.clicked.connect(self.mudarJanelaVagas)
        self.ui.btnEstacionamento.clicked.connect(self.mudarJanelaEstacionamento)
        self.ui.btnMinhaReserva.clicked.connect(self.mudarJanelaMinhaReserva)
        self.ui.btnSair.clicked.connect(self.sair)

    @QtCore.pyqtSlot()
    def mudarJanelaVagas(self):
        self.janelaVagas = telaVagasCliente([self.user, self.password])
        self.janelaVagas.show()
        self.hide()
    
    @QtCore.pyqtSlot()
    def mudarJanelaEstacionamento(self):
        self.janelaEstacionamento = telaEstacionamentoCliente([self.user, self.password])
        self.janelaEstacionamento.show()
        self.hide()
    
    @QtCore.pyqtSlot()
    def mudarJanelaMinhaReserva(self):
        self.janelaMinhaReserva = telaMinhaReserva([self.user, self.password])
        self.janelaMinhaReserva.show()
        self.hide()

    @QtCore.pyqtSlot()
    def sair(self):
        self.close()


class telaVagasCliente(QMainWindow):
    def __init__(self, informacao:list):
        super().__init__()
        self.ui = Ui_VagasCliente()
        self.ui.setupUi(self)

        self.user = informacao[0] 
        self.password = [1]
        
        self.ui.tableVagas.setRowCount(20)
        self.ui.tableVagas.setColumnCount(4)

        documento = listarVagasDB()
        
        self.ui.tableVagas.setItem(0, 0, QtWidgets.QTableWidgetItem(documento[0]["Vaga"]))
        self.ui.tableVagas.setItem(0, 1, QtWidgets.QTableWidgetItem(documento[0]["Status"]))
        self.ui.tableVagas.setItem(0, 2, QtWidgets.QTableWidgetItem(documento[0]["Aluguel"]))
        self.ui.tableVagas.setItem(0, 3, QtWidgets.QTableWidgetItem(documento[0]["Tempo"]))
        
        self.ui.tableVagas.setItem(1, 0, QtWidgets.QTableWidgetItem(documento[1]["Vaga"]))
        self.ui.tableVagas.setItem(1, 1, QtWidgets.QTableWidgetItem(documento[1]["Status"]))
        self.ui.tableVagas.setItem(1, 2, QtWidgets.QTableWidgetItem(documento[1]["Aluguel"]))
        self.ui.tableVagas.setItem(1, 3, QtWidgets.QTableWidgetItem(documento[1]["Tempo"]))
                
        self.ui.tableVagas.setItem(2, 0, QtWidgets.QTableWidgetItem(documento[2]["Vaga"]))
        self.ui.tableVagas.setItem(2, 1, QtWidgets.QTableWidgetItem(documento[2]["Status"]))
        self.ui.tableVagas.setItem(2, 2, QtWidgets.QTableWidgetItem(documento[2]["Aluguel"]))
        self.ui.tableVagas.setItem(2, 3, QtWidgets.QTableWidgetItem(documento[2]["Tempo"]))
                
        self.ui.tableVagas.setItem(3, 0, QtWidgets.QTableWidgetItem(documento[3]["Vaga"]))
        self.ui.tableVagas.setItem(3, 1, QtWidgets.QTableWidgetItem(documento[3]["Status"]))
        self.ui.tableVagas.setItem(3, 2, QtWidgets.QTableWidgetItem(documento[3]["Aluguel"]))
        self.ui.tableVagas.setItem(3, 3, QtWidgets.QTableWidgetItem(documento[3]["Tempo"]))
                
        self.ui.tableVagas.setItem(4, 0, QtWidgets.QTableWidgetItem(documento[4]["Vaga"]))
        self.ui.tableVagas.setItem(4, 1, QtWidgets.QTableWidgetItem(documento[4]["Status"]))
        self.ui.tableVagas.setItem(4, 2, QtWidgets.QTableWidgetItem(documento[4]["Aluguel"]))
        self.ui.tableVagas.setItem(4, 3, QtWidgets.QTableWidgetItem(documento[4]["Tempo"]))
                
        self.ui.tableVagas.setItem(5, 0, QtWidgets.QTableWidgetItem(documento[5]["Vaga"]))
        self.ui.tableVagas.setItem(5, 1, QtWidgets.QTableWidgetItem(documento[5]["Status"]))
        self.ui.tableVagas.setItem(5, 2, QtWidgets.QTableWidgetItem(documento[5]["Aluguel"]))
        self.ui.tableVagas.setItem(5, 3, QtWidgets.QTableWidgetItem(documento[5]["Tempo"]))
                
        self.ui.tableVagas.setItem(6, 0, QtWidgets.QTableWidgetItem(documento[6]["Vaga"]))
        self.ui.tableVagas.setItem(6, 1, QtWidgets.QTableWidgetItem(documento[6]["Status"]))
        self.ui.tableVagas.setItem(6, 2, QtWidgets.QTableWidgetItem(documento[6]["Aluguel"]))
        self.ui.tableVagas.setItem(6, 3, QtWidgets.QTableWidgetItem(documento[6]["Tempo"]))
                
        self.ui.tableVagas.setItem(7, 0, QtWidgets.QTableWidgetItem(documento[7]["Vaga"]))
        self.ui.tableVagas.setItem(7, 1, QtWidgets.QTableWidgetItem(documento[7]["Status"]))
        self.ui.tableVagas.setItem(7, 2, QtWidgets.QTableWidgetItem(documento[7]["Aluguel"]))
        self.ui.tableVagas.setItem(7, 3, QtWidgets.QTableWidgetItem(documento[7]["Tempo"]))
                
        self.ui.tableVagas.setItem(8, 0, QtWidgets.QTableWidgetItem(documento[8]["Vaga"]))
        self.ui.tableVagas.setItem(8, 1, QtWidgets.QTableWidgetItem(documento[8]["Status"]))
        self.ui.tableVagas.setItem(8, 2, QtWidgets.QTableWidgetItem(documento[8]["Aluguel"]))
        self.ui.tableVagas.setItem(8, 3, QtWidgets.QTableWidgetItem(documento[8]["Tempo"]))
                
        self.ui.tableVagas.setItem(9, 0, QtWidgets.QTableWidgetItem(documento[9]["Vaga"]))
        self.ui.tableVagas.setItem(9, 1, QtWidgets.QTableWidgetItem(documento[9]["Status"]))
        self.ui.tableVagas.setItem(9, 2, QtWidgets.QTableWidgetItem(documento[9]["Aluguel"]))
        self.ui.tableVagas.setItem(9, 3, QtWidgets.QTableWidgetItem(documento[9]["Tempo"]))
                
        self.ui.tableVagas.setItem(10, 0, QtWidgets.QTableWidgetItem(documento[10]["Vaga"]))
        self.ui.tableVagas.setItem(10, 1, QtWidgets.QTableWidgetItem(documento[10]["Status"]))
        self.ui.tableVagas.setItem(10, 2, QtWidgets.QTableWidgetItem(documento[10]["Aluguel"]))
        self.ui.tableVagas.setItem(10, 3, QtWidgets.QTableWidgetItem(documento[10]["Tempo"]))
                
        self.ui.tableVagas.setItem(11, 0, QtWidgets.QTableWidgetItem(documento[11]["Vaga"]))
        self.ui.tableVagas.setItem(11, 1, QtWidgets.QTableWidgetItem(documento[11]["Status"]))
        self.ui.tableVagas.setItem(11, 2, QtWidgets.QTableWidgetItem(documento[11]["Aluguel"]))
        self.ui.tableVagas.setItem(11, 3, QtWidgets.QTableWidgetItem(documento[11]["Tempo"]))
                
        self.ui.tableVagas.setItem(12, 0, QtWidgets.QTableWidgetItem(documento[12]["Vaga"]))
        self.ui.tableVagas.setItem(12, 1, QtWidgets.QTableWidgetItem(documento[12]["Status"]))
        self.ui.tableVagas.setItem(12, 2, QtWidgets.QTableWidgetItem(documento[12]["Aluguel"]))
        self.ui.tableVagas.setItem(12, 3, QtWidgets.QTableWidgetItem(documento[12]["Tempo"]))
                
        self.ui.tableVagas.setItem(13, 0, QtWidgets.QTableWidgetItem(documento[13]["Vaga"]))
        self.ui.tableVagas.setItem(13, 1, QtWidgets.QTableWidgetItem(documento[13]["Status"]))
        self.ui.tableVagas.setItem(13, 2, QtWidgets.QTableWidgetItem(documento[13]["Aluguel"]))
        self.ui.tableVagas.setItem(13, 3, QtWidgets.QTableWidgetItem(documento[13]["Tempo"]))
                
        self.ui.tableVagas.setItem(14, 0, QtWidgets.QTableWidgetItem(documento[14]["Vaga"]))
        self.ui.tableVagas.setItem(14, 1, QtWidgets.QTableWidgetItem(documento[14]["Status"]))
        self.ui.tableVagas.setItem(14, 2, QtWidgets.QTableWidgetItem(documento[14]["Aluguel"]))
        self.ui.tableVagas.setItem(14, 3, QtWidgets.QTableWidgetItem(documento[14]["Tempo"]))
                
        self.ui.tableVagas.setItem(15, 0, QtWidgets.QTableWidgetItem(documento[15]["Vaga"]))
        self.ui.tableVagas.setItem(15, 1, QtWidgets.QTableWidgetItem(documento[15]["Status"]))
        self.ui.tableVagas.setItem(15, 2, QtWidgets.QTableWidgetItem(documento[15]["Aluguel"]))
        self.ui.tableVagas.setItem(15, 3, QtWidgets.QTableWidgetItem(documento[15]["Tempo"]))
                
        self.ui.tableVagas.setItem(16, 0, QtWidgets.QTableWidgetItem(documento[16]["Vaga"]))
        self.ui.tableVagas.setItem(16, 1, QtWidgets.QTableWidgetItem(documento[16]["Status"]))
        self.ui.tableVagas.setItem(16, 2, QtWidgets.QTableWidgetItem(documento[16]["Aluguel"]))
        self.ui.tableVagas.setItem(16, 3, QtWidgets.QTableWidgetItem(documento[16]["Tempo"]))
                
        self.ui.tableVagas.setItem(17, 0, QtWidgets.QTableWidgetItem(documento[17]["Vaga"]))
        self.ui.tableVagas.setItem(17, 1, QtWidgets.QTableWidgetItem(documento[17]["Status"]))
        self.ui.tableVagas.setItem(17, 2, QtWidgets.QTableWidgetItem(documento[17]["Aluguel"]))
        self.ui.tableVagas.setItem(17, 3, QtWidgets.QTableWidgetItem(documento[17]["Tempo"]))
                
        self.ui.tableVagas.setItem(18, 0, QtWidgets.QTableWidgetItem(documento[18]["Vaga"]))
        self.ui.tableVagas.setItem(18, 1, QtWidgets.QTableWidgetItem(documento[18]["Status"]))
        self.ui.tableVagas.setItem(18, 2, QtWidgets.QTableWidgetItem(documento[18]["Aluguel"]))
        self.ui.tableVagas.setItem(18, 3, QtWidgets.QTableWidgetItem(documento[18]["Tempo"]))
                
        self.ui.tableVagas.setItem(19, 0, QtWidgets.QTableWidgetItem(documento[19]["Vaga"]))
        self.ui.tableVagas.setItem(19, 1, QtWidgets.QTableWidgetItem(documento[19]["Status"]))
        self.ui.tableVagas.setItem(19, 2, QtWidgets.QTableWidgetItem(documento[19]["Aluguel"]))
        self.ui.tableVagas.setItem(19, 3, QtWidgets.QTableWidgetItem(documento[19]["Tempo"]))

        self.ui.btnHome.clicked.connect(self.mudarJanelaHomeCliente)
        self.ui.btnEstacionamento.clicked.connect(self.mudarJanelaEstacionamentoCliente)
        self.ui.btnReservas.clicked.connect(self.mudarJanelaMinhaReserva)
        self.ui.btnSair.clicked.connect(self.sair)

        self.ui.btnAlugar.clicked.connect(self.mudarJanelaAlugarVaga)
        self.ui.btnReservar.clicked.connect(self.mudarJanelaReservarVaga)
        
    
    @QtCore.pyqtSlot()
    def mudarJanelaHomeCliente(self):
        self.janelaHomeCliente = telaHomeCliente([self.user, self.password])
        self.janelaHomeCliente.show()
        self.close()
    
    @QtCore.pyqtSlot()
    def mudarJanelaEstacionamentoCliente(self):
        self.janelaEstacionamento = telaEstacionamentoCliente([self.user, self.password])
        self.janelaEstacionamento.show()
        self.close()

    @QtCore.pyqtSlot()
    def mudarJanelaMinhaReserva(self):
        self.janelaMinhaReserva = telaMinhaReserva([self.user, self.password])
        self.janelaMinhaReserva.show()
        self.close()

    @QtCore.pyqtSlot()
    def mudarJanelaAlugarVaga(self):
        self.janelaAlugar = telaAlugarVagasCliente([self.user, self.password])
        self.janelaAlugar.show()
        self.hide()

    @QtCore.pyqtSlot()
    def mudarJanelaReservarVaga(self):
        self.janelaReserva = telaReservarVagasCliente([self.user, self.password])
        self.janelaReserva.show()
        self.hide()

    @QtCore.pyqtSlot()
    def sair(self):
        self.close()


class telaEstacionamentoCliente(QMainWindow):
    def __init__(self, informacao:list):
        super().__init__()
        self.ui = Ui_EstacionamentoCliente()
        self.ui.setupUi(self)

        self.user = informacao[0]
        self.password = informacao[1]

        self.ui.btnHome.clicked.connect(self.mudarJanelaHome)
        self.ui.btnVagas.clicked.connect(self.mudarJanelaVagas)
        self.ui.btnMinhaReserva.clicked.connect(self.mudarJanelaMinhaReserva)
        self.ui.btnSair.clicked.connect(self.sair)

        self.ui.btnAlugar.clicked.connect(self.alugarVaga)
        self.ui.btnReservar.clicked.connect(self.reservarVaga)

    @QtCore.pyqtSlot()
    def mudarJanelaHome(self):
        self.janelaHome = telaHomeCliente([self.user, self.password])
        self.janelaHome.show()
        self.close()
    
    @QtCore.pyqtSlot()
    def mudarJanelaVagas(self):
        self.janelaVagas = telaVagasCliente([self.user, self.password])
        self.janelaVagas.show()
        self.close()
    
    @QtCore.pyqtSlot()
    def mudarJanelaMinhaReserva(self):
        self.janelaMinhaReserva = telaMinhaReserva([self.user, self.password])
        self.janelaMinhaReserva.show()
        self.close()

    @QtCore.pyqtSlot()
    def alugarVaga(self):
        self.alugarVaga = telaAlugarVagasCliente([self.user, self.password])
        self.alugarVaga.show()
        self.close()

    @QtCore.pyqtSlot()
    def reservarVaga(self):
        self.reservarVaga = telaReservarVagasCliente([self.user, self.password])
        self.reservarVaga.show()
        self.close()

    @QtCore.pyqtSlot()
    def sair(self):
        self.close()


class telaMinhaReserva(QMainWindow):
    def __init__(self, informacao:list):
        super().__init__()
        self.ui = Ui_ReservasCliente()
        self.ui.setupUi(self)

        self.user = informacao[0] 
        self.password = informacao[1]

        self.ui.tableReservaCliente.setRowCount(1)
        self.ui.tableReservaCliente.setColumnCount(4)

        row = vagasCliente([self.user, self.password])
        
        self.ui.tableReservaCliente.setItem(0, 0, QTableWidgetItem(row["Vaga"]))
        self.ui.tableReservaCliente.setItem(0, 1, QTableWidgetItem(row["Data"]))
        self.ui.tableReservaCliente.setItem(0, 2, QTableWidgetItem(row["Tempo"]))
        self.ui.tableReservaCliente.setItem(0, 3, QTableWidgetItem(row["Aluguel"]))

        self.vaga = row["Vaga"]

        self.ui.btnHome.clicked.connect(self.mudarJanelaHomeCliente)
        self.ui.btnVagas.clicked.connect(self.mudarJanelaVagasCliente)
        self.ui.btnEstacionamento.clicked.connect(self.mudarJanelaEstacionamentoCliente)
        self.ui.btnSair.clicked.connect(self.sair)

        self.ui.btnAtualizarReserva.clicked.connect(self.atualizarReserva)
        self.ui.btnCancelarReserva.clicked.connect(self.cancelarReserva)

    @QtCore.pyqtSlot()
    def mudarJanelaHomeCliente(self):
        self.janelaHomeCliente = telaHomeCliente([self.user, self.password])
        self.janelaHomeCliente.show()
        self.close()

    @QtCore.pyqtSlot()
    def mudarJanelaVagasCliente(self):
        self.janelaVagasCliente = telaVagasCliente([self.user, self.password])
        self.janelaVagasCliente.show()
        self.close()
    
    @QtCore.pyqtSlot()
    def mudarJanelaEstacionamentoCliente(self):
        self.janelaEstacionamentoCliente = telaEstacionamentoCliente([self.user, self.password])
        self.janelaEstacionamentoCliente.show()
        self.close()

    @QtCore.pyqtSlot()
    def sair(self):
        self.close()

    @QtCore.pyqtSlot()
    def atualizarReserva(self):
        self.janelaReservarCliente = telaReservarVagasCliente([self.user, self.password])
        self.janelaReservarCliente.show()
        self.close()

    @QtCore.pyqtSlot()
    def cancelarReserva(self):
        documentoVagas = {
            'Nome': str(''),
            'Placa': str(''),
            'Vaga': str(self.vaga),
            'Status': 'Vazia',
            'Data': str(''),
            'Tempo': str(''),
            'Aluguel': str(''),
        }
        documentoVagaCliente = {
            'user': str(self.user),
            'password': str(self.password),
            'Nome': str(''),
            'Placa': str(''),
            'Vaga': str(''),
            'Status': 'Vazia',
            'Data': str(''),
            'Tempo': str(''),
            'Aluguel': str(''),
        }
        updateVagaCliente(documentoVagaCliente)
        updateVaga(documentoVagas)
        self.janelaHome = telaHomeCliente([self.user, self.password])
        self.janelaHome.show()
        self.close()


class telaAlugarVagasCliente(QMainWindow):
    def __init__(self, informacao:list):
        super().__init__()
        self.ui = Ui_AlugarVaga()
        self.ui.setupUi(self)

        self.user = informacao[0] 
        self.password = informacao[1]

        self.ui.btnConfirmar.clicked.connect(self.confirmar)
        self.ui.btnCancelar.clicked.connect(self.cancelar)

    @QtCore.pyqtSlot()
    def confirmar(self):
        self.alugar()
        self.janelaHomeCliente = telaHomeCliente([self.user, self.password])
        self.janelaHomeCliente.show()
        self.close()

    @QtCore.pyqtSlot()
    def cancelar(self):
        self.janelaHomeCliente = telaHomeCliente([self.user, self.password])
        self.janelaHomeCliente.show()
        self.close()

    @QtCore.pyqtSlot()
    def getNome(self):
        return self.ui.nomeCliente.text()

    @QtCore.pyqtSlot()
    def getPlaca(self):
        return self.ui.placa.text()

    @QtCore.pyqtSlot()
    def getNumeroVaga(self):
        return self.ui.numeroVaga.currentText()

    @QtCore.pyqtSlot()
    def getData(self):
        return self.ui.dataAluguel.text()

    @QtCore.pyqtSlot()
    def getIntervaloTempo(self):
        return self.ui.intervaloAluguel.currentText()

    @QtCore.pyqtSlot()
    def getValor(self):
        return self.ui.valorAluguel.text()

    @QtCore.pyqtSlot()
    def alugar(self):
        documentoVagas = {
            'Nome': str(self.getNome()),
            'Placa': str(self.getPlaca()),
            'Vaga': str(self.getNumeroVaga()),
            'Status': 'Alugada',
            'Data': str(self.getData()),
            'Tempo': str(self.getIntervaloTempo()),
            'Aluguel': str(self.getValor()),
        }
        documentoVagaCliente = {
            'user': str(self.user),
            'password': str(self.password),
            'Nome': str(self.getNome()),
            'Placa': str(self.getPlaca()),
            'Vaga': str(self.getNumeroVaga()),
            'Status': 'Alugada',
            'Data': str(self.getData()),
            'Tempo': str(self.getIntervaloTempo()),
            'Aluguel': str(self.getValor()),
        }
        updateVagaCliente(documentoVagaCliente)
        updateVaga(documentoVagas)


class telaReservarVagasCliente(QMainWindow):
    def __init__(self, informacao:list):
        super().__init__()
        self.ui = Ui_ReservarVaga()
        self.ui.setupUi(self)

        self.user = informacao[0] 
        self.password = informacao[1]

        self.ui.btnConfirmar.clicked.connect(self.confirmar)
        self.ui.btnCancelar.clicked.connect(self.cancelar)

    @QtCore.pyqtSlot()
    def confirmar(self):
        self.reservar()
        self.janelaHomeCliente = telaHomeCliente([self.user, self.password])
        self.janelaHomeCliente.show()
        self.close()

    @QtCore.pyqtSlot()
    def cancelar(self):
        self.janelaHomeCliente = telaHomeCliente([self.user, self.password])
        self.janelaHomeCliente.show()
        self.close()

    @QtCore.pyqtSlot()
    def getNome(self):
        return self.ui.nomeCliente.text()

    @QtCore.pyqtSlot()
    def getPlaca(self):
        return self.ui.placa.text()

    @QtCore.pyqtSlot()
    def getNumeroVaga(self):
        return self.ui.numeroVaga.currentText()

    @QtCore.pyqtSlot()
    def getData(self):
        return self.ui.dataReserva.text()

    @QtCore.pyqtSlot()
    def getIntervaloTempo(self):
        return self.ui.intervaloReserva.currentText()

    @QtCore.pyqtSlot()
    def reservar(self):
        documentoVagaCliente = {
            'user': str(self.user),
            'password': str(self.password),
            'Nome': str(self.getNome()),
            'Placa': str(self.getPlaca()),
            'Vaga': str(self.getNumeroVaga()),
            'Status': 'Reservada',
            'Data': str(self.getData()),
            'Tempo': str(self.getIntervaloTempo()),
            'Aluguel': str('')
        }
        documentoVagas = {
            'Nome': str(self.getNome()),
            'Placa': str(self.getPlaca()),
            'Vaga': str(self.getNumeroVaga()),
            'Status': 'Reservada',
            'Data': str(self.getData()),
            'Tempo': str(self.getIntervaloTempo()),
            'Aluguel': str('')
        }
        updateVaga(documentoVagas)
        updateVagaCliente(documentoVagaCliente)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = telaLogin()
    janela.show()
    sys.exit(app.exec_())