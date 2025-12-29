from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QSize
import sys
import os
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("SoundWave")
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(os.system("amixer sget Master"))
        self.dial.valueChanged.connect(self.sliderMoved)
        self.dial.setFixedSize(QSize(200, 200))
        self.text = QLabel(str(self.dial.value()))
        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text.setStyleSheet("font-size: 50pt;")
        layout.addWidget(self.dial, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.text)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(400, 300))
    def sliderMoved(self):
        volume = self.dial.value()
        self.text.setText(str(self.dial.value()))
        os.system(f"amixer sset 'Master' {volume}%")


app = QApplication(sys.argv)
app.setStyle('Breeze')
window = MainWindow()
window.show()
sys.exit(app.exec())
