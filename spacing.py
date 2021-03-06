#!/usr/bin/env python3
import sys

from PyQt5.QtWidgets import QApplication, QCheckBox, QTabWidget, QVBoxLayout, QWidget, QFormLayout, QLineEdit, QLabel

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("QFormLayout Example")
		self.resize(270, 110)
		# Create a QHBoxLayout instance
		layout = QFormLayout()
		# Add widgets to the layout
		layout.setVerticalSpacing(30)
		layout.addRow("Name:", QLineEdit())
		layout.addRow("Job:", QLineEdit())
		emailLabel = QLabel("Email:")
		layout.addRow(emailLabel, QLineEdit())
		# Set the layout on the application's window
		self.setLayout(layout)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())
