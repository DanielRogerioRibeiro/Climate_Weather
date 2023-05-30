#Esse é um o Programa de Consulta da Previsão do tempo.

from PyQt5 import  uic,QtWidgets


app=QtWidgets.QApplication([])
main=uic.loadUi("main.ui")
main.pushButton.clicked.connect(funcao_principal)
#formulario.pushButton_2.clicked.connect(chama_segunda_tela)

main.show()
app.exec()