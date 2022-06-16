# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './docs/cliente/alugar_cliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AlugarVaga(object):
    def setupUi(self, AlugarVaga):
        AlugarVaga.setObjectName("AlugarVaga")
        AlugarVaga.resize(400, 600)
        AlugarVaga.setMinimumSize(QtCore.QSize(400, 600))
        AlugarVaga.setMaximumSize(QtCore.QSize(400, 600))
        AlugarVaga.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./docs/cliente/imagens/seguro-de-automovel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AlugarVaga.setWindowIcon(icon)
        AlugarVaga.setStyleSheet("background-color: rgb(242, 237, 237);\n"
"color: rgb(75, 74, 74);")
        self.centralwidget = QtWidgets.QWidget(AlugarVaga)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 431, 71))
        self.label.setStyleSheet("background-color: rgb(196, 196, 196);\n"
"color: rgb(75, 74, 74);\n"
"font: 24pt \"Segoe UI\";\n"
"padding: 10px;\n"
"border:none;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnConfirmar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConfirmar.setGeometry(QtCore.QRect(120, 390, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnConfirmar.setFont(font)
        self.btnConfirmar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnConfirmar.setStyleSheet("background-color: rgb(53, 119, 218);\n"
"border: none;\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);")
        self.btnConfirmar.setObjectName("btnConfirmar")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(120, 440, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnCancelar.setFont(font)
        self.btnCancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancelar.setStyleSheet("background-color: #FF0505;\n"
"border: none;\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);")
        self.btnCancelar.setObjectName("btnCancelar")
        self.numeroVaga = QtWidgets.QComboBox(self.centralwidget)
        self.numeroVaga.setGeometry(QtCore.QRect(40, 220, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.numeroVaga.setFont(font)
        self.numeroVaga.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.numeroVaga.setStyleSheet("border-radius:10px;\n"
"background-color:white;\n"
"color: rgb(75, 74, 74);\n"
"padding-left: 20px;\n"
"text-align:center;")
        self.numeroVaga.setEditable(False)
        self.numeroVaga.setObjectName("numeroVaga")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.nomeCliente = QtWidgets.QLineEdit(self.centralwidget)
        self.nomeCliente.setGeometry(QtCore.QRect(40, 120, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nomeCliente.setFont(font)
        self.nomeCliente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";\n"
"padding-left: 20px;\n"
"border-radius:10px;\n"
"color: rgb(75, 74, 74);")
        self.nomeCliente.setText("")
        self.nomeCliente.setObjectName("nomeCliente")
        self.placa = QtWidgets.QLineEdit(self.centralwidget)
        self.placa.setGeometry(QtCore.QRect(40, 170, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.placa.setFont(font)
        self.placa.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";\n"
"padding-left: 20px;\n"
"border-radius:10px;\n"
"color: rgb(75, 74, 74);")
        self.placa.setText("")
        self.placa.setObjectName("placa")
        self.intervaloAluguel = QtWidgets.QComboBox(self.centralwidget)
        self.intervaloAluguel.setGeometry(QtCore.QRect(210, 270, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.intervaloAluguel.setFont(font)
        self.intervaloAluguel.setStyleSheet("border-radius:10px;\n"
"background-color:white;\n"
"color: rgb(75, 74, 74);\n"
"padding-left: 20px;\n"
"text-align:center;")
        self.intervaloAluguel.setObjectName("intervaloAluguel")
        self.intervaloAluguel.addItem("")
        self.intervaloAluguel.addItem("")
        self.intervaloAluguel.addItem("")
        self.intervaloAluguel.addItem("")
        self.intervaloAluguel.addItem("")
        self.intervaloAluguel.addItem("")
        self.intervaloAluguel.addItem("")
        self.intervaloAluguel.addItem("")
        self.intervaloAluguel.addItem("")
        self.intervaloAluguel.addItem("")
        self.intervaloAluguel.addItem("")
        self.intervaloAluguel.addItem("")
        self.intervaloAluguel.addItem("")
        self.intervaloAluguel.addItem("")
        self.intervaloAluguel.addItem("")
        self.dataAluguel = QtWidgets.QDateEdit(self.centralwidget)
        self.dataAluguel.setGeometry(QtCore.QRect(40, 270, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dataAluguel.setFont(font)
        self.dataAluguel.setStyleSheet("border-radius:10px;\n"
"background-color:white;\n"
"color: rgb(75, 74, 74);\n"
"padding-left: 20px;\n"
"text-align:center;")
        self.dataAluguel.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2022, 9, 14), QtCore.QTime(12, 0, 0)))
        self.dataAluguel.setObjectName("dataAluguel")
        self.valorAluguel = QtWidgets.QLineEdit(self.centralwidget)
        self.valorAluguel.setGeometry(QtCore.QRect(40, 320, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.valorAluguel.setFont(font)
        self.valorAluguel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";\n"
"padding-left: 20px;\n"
"border-radius:10px;\n"
"color: rgb(75, 74, 74);")
        self.valorAluguel.setText("")
        self.valorAluguel.setObjectName("valorAluguel")
        AlugarVaga.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AlugarVaga)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        AlugarVaga.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AlugarVaga)
        self.statusbar.setObjectName("statusbar")
        AlugarVaga.setStatusBar(self.statusbar)

        self.retranslateUi(AlugarVaga)
        QtCore.QMetaObject.connectSlotsByName(AlugarVaga)

    def retranslateUi(self, AlugarVaga):
        _translate = QtCore.QCoreApplication.translate
        AlugarVaga.setWindowTitle(_translate("AlugarVaga", "Sistema de estacionamento - Alugar"))
        self.label.setText(_translate("AlugarVaga", "Alugar vaga"))
        self.btnConfirmar.setText(_translate("AlugarVaga", "Confirmar"))
        self.btnCancelar.setText(_translate("AlugarVaga", "Cancelar"))
        self.numeroVaga.setPlaceholderText(_translate("AlugarVaga", "Número da Vaga"))
        self.numeroVaga.setItemText(0, _translate("AlugarVaga", "01"))
        self.numeroVaga.setItemText(1, _translate("AlugarVaga", "02"))
        self.numeroVaga.setItemText(2, _translate("AlugarVaga", "03"))
        self.numeroVaga.setItemText(3, _translate("AlugarVaga", "04"))
        self.numeroVaga.setItemText(4, _translate("AlugarVaga", "05"))
        self.numeroVaga.setItemText(5, _translate("AlugarVaga", "06"))
        self.numeroVaga.setItemText(6, _translate("AlugarVaga", "07"))
        self.numeroVaga.setItemText(7, _translate("AlugarVaga", "08"))
        self.numeroVaga.setItemText(8, _translate("AlugarVaga", "09"))
        self.numeroVaga.setItemText(9, _translate("AlugarVaga", "10"))
        self.numeroVaga.setItemText(10, _translate("AlugarVaga", "11"))
        self.numeroVaga.setItemText(11, _translate("AlugarVaga", "12"))
        self.numeroVaga.setItemText(12, _translate("AlugarVaga", "13"))
        self.numeroVaga.setItemText(13, _translate("AlugarVaga", "14"))
        self.numeroVaga.setItemText(14, _translate("AlugarVaga", "15"))
        self.numeroVaga.setItemText(15, _translate("AlugarVaga", "16"))
        self.numeroVaga.setItemText(16, _translate("AlugarVaga", "17"))
        self.numeroVaga.setItemText(17, _translate("AlugarVaga", "18"))
        self.numeroVaga.setItemText(18, _translate("AlugarVaga", "19"))
        self.numeroVaga.setItemText(19, _translate("AlugarVaga", "20"))
        self.nomeCliente.setPlaceholderText(_translate("AlugarVaga", "Nome"))
        self.placa.setPlaceholderText(_translate("AlugarVaga", "Placa do veículo"))
        self.intervaloAluguel.setPlaceholderText(_translate("AlugarVaga", "Intervalo"))
        self.intervaloAluguel.setItemText(0, _translate("AlugarVaga", "08:00 - 09:00"))
        self.intervaloAluguel.setItemText(1, _translate("AlugarVaga", "09:00 - 10:00"))
        self.intervaloAluguel.setItemText(2, _translate("AlugarVaga", "10:00 - 11:00"))
        self.intervaloAluguel.setItemText(3, _translate("AlugarVaga", "11:00 - 12:00"))
        self.intervaloAluguel.setItemText(4, _translate("AlugarVaga", "12:00 - 13:00"))
        self.intervaloAluguel.setItemText(5, _translate("AlugarVaga", "13:00 - 14:00"))
        self.intervaloAluguel.setItemText(6, _translate("AlugarVaga", "14:00 - 15:00"))
        self.intervaloAluguel.setItemText(7, _translate("AlugarVaga", "15:00 - 16:00"))
        self.intervaloAluguel.setItemText(8, _translate("AlugarVaga", "16:00 - 17:00"))
        self.intervaloAluguel.setItemText(9, _translate("AlugarVaga", "17:00 - 18:00"))
        self.intervaloAluguel.setItemText(10, _translate("AlugarVaga", "18:00 - 19:00"))
        self.intervaloAluguel.setItemText(11, _translate("AlugarVaga", "19:00 - 20:00"))
        self.intervaloAluguel.setItemText(12, _translate("AlugarVaga", "20:00 - 21:00"))
        self.intervaloAluguel.setItemText(13, _translate("AlugarVaga", "21:00 - 22:00"))
        self.intervaloAluguel.setItemText(14, _translate("AlugarVaga", "22:00 - 23:00"))
        self.valorAluguel.setPlaceholderText(_translate("AlugarVaga", "Valor do aluguel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AlugarVaga = QtWidgets.QMainWindow()
    ui = Ui_AlugarVaga()
    ui.setupUi(AlugarVaga)
    AlugarVaga.show()
    sys.exit(app.exec_())
