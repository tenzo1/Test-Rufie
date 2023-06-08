from PyQt5.QtWidgets import *
from instr import*



class FinalWin(QWidget):
    def __init__(self,age,t1,t2,t3):
        super().__init__()
        self.age = age
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.initUI()

        self.set_appear()

        self.show()

    def set_appear(self):
        self.setWindowTitle(set_title)
        self.resize(win_width, win_hight)
        self.move(win_x, win_y)

    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel('Ваш результат индекса:')
        self.result = QLabel("индекс "+str((4*(int(self.t1)+int(self.t2)+int(self.t3))-200)/10))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.result)
        self.setLayout(self.layout)
