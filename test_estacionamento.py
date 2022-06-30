from app import telaAlugarVagasCliente, telaCadastroCliente, telaCadastrosFuncionario, telaConfirmacaoPagamento, telaConfirmarAlteracao, telaConfirmarPagamento, telaConfirmarReserva, telaEstacionamentoCliente, telaHomeCliente, telaHomeFuncionario, telaLogin, telaMudarStatusFuncionario, telaReservarVagasCliente, telaVagasCliente


def test_home_funcionario_sair(qtbot):
    test_home_funcionario = telaHomeFuncionario()
    qtbot.addWidget(test_home_funcionario)
    assert test_home_funcionario.sair() == True


def test_novo_cadastro_funcionario_novo_cadastro(qtbot):
    test_novo_cadastro = telaCadastrosFuncionario()
    qtbot.addWidget(test_novo_cadastro)
    assert test_novo_cadastro.novoCadastro() == True


def test_situacao_vaga_get_situacao(qtbot):
    test_mudar_situacao_vaga = telaMudarStatusFuncionario()
    qtbot.addWidget(test_mudar_situacao_vaga)
    assert (test_mudar_situacao_vaga.getSituacao() == 'Vazia' or 
           test_mudar_situacao_vaga.getSituacao() == 'Ocupada' or 
           test_mudar_situacao_vaga.getSituacao() == 'Reservada')


def test_sair_tela_home_cliente_sair(qtbot):
    test_home_cliente = telaHomeCliente()
    qtbot.addWidget(test_home_cliente)
    assert test_home_cliente.sair() == True


def test_checar_campos_login_checar_campos(qtbot):
    test_checar_campos = telaLogin()
    qtbot.addWidget(test_checar_campos)
    assert test_checar_campos.checarCampos() == False


def test_frame_erro__funcionario_fechar_frame(qtbot):
    test_frame = telaLogin()
    qtbot.addWidget(test_frame)
    assert test_frame.fecharFrame() == None


def test_usuario_login(qtbot):
    test_login_usuario = telaLogin()
    qtbot.addWidget(test_login_usuario)
    assert test_login_usuario.usuarioLogin() == None


def test_cadastro_cliente_cadastrar_usuario(qtbot):
    test_cadastro = telaCadastroCliente()
    qtbot.addWidget(test_cadastro)
    assert test_cadastro.cadastrarUsuario() == None


def test_cadastro_cliente_get_nome(qtbot):
    test_cadastro = telaCadastroCliente()
    qtbot.addWidget(test_cadastro)
    assert type(test_cadastro.getNome()) == type('')


def test_cadastro_cliente_get_senha(qtbot):
    test_cadastro = telaCadastroCliente()
    qtbot.addWidget(test_cadastro)
    assert type(test_cadastro.getSenha()) == type('')
    

def test_confimacao_pagamento_confirmar(qtbot):
    test_confirmacao = telaConfirmacaoPagamento()
    qtbot.addWidget(test_confirmacao)
    assert test_confirmacao.confirmar() == True


def test_cancelamento_pagamento_cancelar(qtbot):
    test_cancelamento = telaConfirmacaoPagamento()
    qtbot.addWidget(test_cancelamento)
    assert test_cancelamento.cancelar() == True


def test_confirmar_pagamento_fechar(qtbot):
    test_confirmar = telaConfirmarPagamento()
    qtbot.addWidget(test_confirmar)
    assert test_confirmar.fechar() == True


def test_confirmar_alteracao_fechar(qtbot):
    test_confirmar_alteracao = telaConfirmarAlteracao()
    qtbot.addWidget(test_confirmar_alteracao)
    assert test_confirmar_alteracao.fechar() == True


def test_confirmar_reserva_fechar(qtbot):
    test_confirmar_reserva = telaConfirmarReserva()
    qtbot.addWidget(test_confirmar_reserva)
    assert test_confirmar_reserva.fechar() == True


def test_tela_vagas_cliente_sair(qtbot):
    test_vagas_cliente_sair = telaVagasCliente()
    qtbot.addWidget(test_vagas_cliente_sair)
    assert test_vagas_cliente_sair.sair() == True


def test_alugar_vagas_cliente_cancelar(qtbot):
    test_cancelar_vaga_cliente = telaAlugarVagasCliente()
    qtbot.addWidget(test_cancelar_vaga_cliente)
    assert test_cancelar_vaga_cliente.cancelar() == True


def test_alugar_vagas_cliente_confirmar(qtbot):
    test_confirmar_vaga_cliente = telaAlugarVagasCliente()
    qtbot.addWidget(test_confirmar_vaga_cliente)
    assert test_confirmar_vaga_cliente.confirmar() == True


def test_reservar_vagas_cliente_cancelar(qtbot):
    test_cancelar_reserva_cliente = telaReservarVagasCliente()
    qtbot.addWidget(test_cancelar_reserva_cliente)
    assert test_cancelar_reserva_cliente.cancelar() == True


def test_reservar_vagas_cliente_confirmar(qtbot):
    test_confirmar_reserva_cliente = telaReservarVagasCliente()
    qtbot.addWidget(test_confirmar_reserva_cliente)
    assert test_confirmar_reserva_cliente.confirmar() == True


def test_estacionamento_cliente_sair(qtbot):
    test_sair_estacionamento_cliente = telaEstacionamentoCliente()
    qtbot.addWidget(test_sair_estacionamento_cliente)
    assert test_sair_estacionamento_cliente.sair() == True