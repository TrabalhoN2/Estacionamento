from app import telaCadastrosFuncionario, telaHomeFuncionario, telaLogin, telaMudarStatusFuncionario


def test_sair_tela_home_funcionario(qtbot):
    test_home_funcionario = telaHomeFuncionario()
    qtbot.addWidget(test_home_funcionario)
    assert test_home_funcionario.sair() == True


def test_novo_cadastro_funcionario(qtbot):
    test_novo_cadastro = telaCadastrosFuncionario()
    qtbot.addWidget(test_novo_cadastro)
    assert test_novo_cadastro.novoCadastro() == True


def test_situacao_vaga(qtbot):
    test_mudar_situacao_vaga = telaMudarStatusFuncionario()
    qtbot.addWidget(test_mudar_situacao_vaga)
    assert test_mudar_situacao_vaga.getSituacao() == 'Vazia'


def test_checar_campos_login(qtbot):
    test_checar_campos = telaLogin()
    qtbot.addWidget(test_checar_campos)
    assert test_checar_campos.checarCampos() == False


def test_entrar_funcionario(qtbot):
    test_entrar = telaLogin()
    qtbot.addWidget(test_entrar)
    assert test_entrar.fecharFrame() == None