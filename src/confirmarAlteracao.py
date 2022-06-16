# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './docs/confirmar_alteracao.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConfirmarAlteracao(object):
    def setupUi(self, ConfirmarAlteracao):
        ConfirmarAlteracao.setObjectName("ConfirmarAlteracao")
        ConfirmarAlteracao.resize(300, 300)
        ConfirmarAlteracao.setMinimumSize(QtCore.QSize(300, 300))
        ConfirmarAlteracao.setMaximumSize(QtCore.QSize(300, 550))
        ConfirmarAlteracao.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./docs/imagens/seguro-de-automovel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ConfirmarAlteracao.setWindowIcon(icon)
        ConfirmarAlteracao.setStyleSheet("background-color: rgb(242, 237, 237);")
        self.centralwidget = QtWidgets.QWidget(ConfirmarAlteracao)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 300, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(196, 196, 196);\n"
"color: rgb(75, 74, 74);\n"
"\n"
"padding: 10px;\n"
"border:none;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 211, 161))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(75, 74, 74);\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.btnFechar = QtWidgets.QPushButton(self.centralwidget)
        self.btnFechar.setGeometry(QtCore.QRect(110, 220, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnFechar.setFont(font)
        self.btnFechar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnFechar.setStyleSheet("border: none;\n"
"border-radius:10px;\n"
"background-color: rgb(53, 119, 218);\n"
"color: rgb(255, 255, 255);")
        self.btnFechar.setObjectName("btnFechar")
        ConfirmarAlteracao.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ConfirmarAlteracao)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menubar.setObjectName("menubar")
        ConfirmarAlteracao.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ConfirmarAlteracao)
        self.statusbar.setObjectName("statusbar")
        ConfirmarAlteracao.setStatusBar(self.statusbar)

        self.retranslateUi(ConfirmarAlteracao)
        QtCore.QMetaObject.connectSlotsByName(ConfirmarAlteracao)

    def retranslateUi(self, ConfirmarAlteracao):
        _translate = QtCore.QCoreApplication.translate
        ConfirmarAlteracao.setWindowTitle(_translate("ConfirmarAlteracao", "Sistema de estacionamento -Confirmação de alteração"))
        self.label.setText(_translate("ConfirmarAlteracao", "Alteração confirmada!"))
        self.label_2.setText(_translate("ConfirmarAlteracao", "A informação foi\n"
" alterada com\n"
" sucesso!\n"
"\n"
""))
        self.btnFechar.setText(_translate("ConfirmarAlteracao", "Fechar"))