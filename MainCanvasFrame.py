import sys
import OCRtest_eng

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        label1 = QLabel(OCRtest_eng.text, self)
        label1.setAlignment(Qt.AlignCenter)

        self.setWindowTitle('ENTERPRISE LINKAGE PROJECT')
        self.move(300, 300)
        self.resize(400, 300)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())