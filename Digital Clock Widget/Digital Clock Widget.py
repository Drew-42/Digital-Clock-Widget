import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

# Defining the widget class

class DigitalClock(QWidget):

	def __init__(self):
		super().__init__()
		self.time_label = QLabel(self)
		self.timer = QTimer(self)
		self.initUI()

# Initialisation of UI, here the content of the window is configured and aligned

	def initUI(self):
		self.setWindowTitle('Digital Clock')
		self.setGeometry(600, 400, 300, 100)

# Setting up the layout of the window and the design of the label

		vbox = QVBoxLayout()
		vbox.addWidget(self.time_label)
		self.setLayout(vbox)

		self.time_label.setAlignment(Qt.AlignCenter)

		self.time_label.setStyleSheet('font-size: 150px;'
									  'color: hsl(125, 100%, 50%)')
		self.setStyleSheet('background-color: black;')
		
		font_id = QFontDatabase.addApplicationFont('DS-DIGIT.TTF')
		font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
		my_font = QFont(font_family, 150)
		self.time_label.setFont(my_font)

		self.timer.timeout.connect(self.update_time)
		self.timer.start(1000)

		self.update_time()

# The function that updates the label with the current time of the machine (expressed as 
# hh:mm:ss), every second (see self.initUI())

	def update_time(self):
		current_time = QTime.currentTime().toString('hh:mm:ss AP')
		self.time_label.setText(current_time)

# The widget opens only when the file runs as a script, not imported as a module

if __name__ == '__main__':
	app = QApplication(sys.argv)
	clock = DigitalClock()
	clock.show()
	sys.exit(app.exec_())