#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5.QtCore import pyqtSlot

class myAppWindow(QMainWindow):

	def __init__(self):
		super().__init__()

		self.topo = 100
		self.esquerda = 100
		self.largura = 300
		self.altura = 300
		self.titulo = 'Window title'

		botao1 = QPushButton('Botao 1', self)
		botao1.move(100, 100)
		botao1.resize(150, 80)
		botao1.setStyleSheet('QPushButton {background-color:#0FB328; font:bold; font-size:15px}')
		botao1.clicked.connect(self.botao1_click)

		botao2 = QPushButton('Botao 2', self)
		botao2.move(100, 200)
		botao2.resize(150, 80)
		botao2.setStyleSheet('QPushButton {background-color:#0FB328; font:bold; font-size:15px}')
		botao2.clicked.connect(self.botao2_click)

		# label_1 is 'self' because we need to access it into botao1_click() and botao2_click() functions
		self.label_1 = QLabel(self)
		self.label_1.setText("Click em um botao")
		self.label_1.move(10, 10)
		self.label_1.setStyleSheet('QLabel {font:bold; font:italic; font-size:15px}')
		self.label_1.resize(300, 100)

		self.CarregarJanela()

	def CarregarJanela(self):
		self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
		self.setWindowTitle(self.titulo)

		self.show()

	@pyqtSlot()
	def botao1_click(self):
		self.label_1.setStyleSheet('QLabel {font:bold; font-size:15px; color:"red"}')
		self.label_1.setText("Botao 1!")

	@pyqtSlot()
	def botao2_click(self):
		self.label_1.setStyleSheet('QLabel {font:bold; font-size:15px; color:"blue"}')
		self.label_1.setText("Botao 2!")
		pass

myApp = QApplication(sys.argv)
app = myAppWindow()
sys.exit(myApp.exec_())
