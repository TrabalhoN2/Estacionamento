import pytest

from PyQt5 import QtCore
from app import telaHomeFuncionario

@pytest.fixture
def test_app(qtbot):
    test_home_funcionario = telaHomeFuncionario()
    test_home_funcionario.show()
    qtbot.addWidget(test_home_funcionario)


def test_sair(qtbot):
    
    assert telaHomeFuncionario.sair() == True

