from PyQt5.QtWidgets import *
from instr import*
from final_win import*
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(set_title)
        self.resize(win_width, win_hight)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()

        self.label_fill_name = QLabel(txt_fill_name)
        self.l_line.addWidget(self.label_fill_name)

        self.fill_name = QLineEdit(txt_fill_name_edit)
        self.fill_name.setMaximumWidth(50)
        self.l_line.addWidget(self.fill_name)
        

        self.label_fill_name = QLabel(txt_fill_age)
        
        self.l_line.addWidget(self.label_fill_name)

        self.fill_age = QLineEdit(txt_fill_age_edit)
        self.fill_age.setMaximumWidth(50)
        self.l_line.addWidget(self.fill_age)

        self.label_instuctions = QLabel(txt_fill_insturctions)
        self.l_line.addWidget(self.label_instuctions)

        self.test_try = QPushButton(txt_test_try)
        self.l_line.addWidget(self.test_try)

        self.fill_seconds = QLineEdit(txt_fill_seconds_edit)
        self.fill_seconds.setMaximumWidth(50)
        self.l_line.addWidget(self.fill_seconds)

        self.label_second_instruction = QLabel(txt_fill_seconds_instruction)
        self.l_line.addWidget(self.label_second_instruction)

        self.test_jump = QPushButton(txt_start_jump)
        self.l_line.addWidget(self.test_jump)

        self.jump_instruction = QLabel(txt_jump_instruction)
        self.l_line.addWidget(self.jump_instruction)

        self.final_test = QPushButton(txt_final_test)
        self.l_line.addWidget(self.final_test)

        self.fill_one_line = QLineEdit(txt_fill_one_line)
        self.fill_one_line.setMaximumWidth(50)
        self.l_line.addWidget(self.fill_one_line)

        self.fill_second_line = QLineEdit(txt_fill_second_line)
        self.fill_second_line.setMaximumWidth(50)
        self.l_line.addWidget(self.fill_second_line)
        
        self.get_results = QPushButton(txt_get_results)
        self.l_line.addWidget(self.get_results)

        self.timer = QLabel(txt_timer)
        self.timer.setFont(QFont('Times',15,QFont.Bold))
        self.timer.setStyleSheet('color: rgb(0,0,0)')
        self.r_line.addWidget(self.timer)

        

        






        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    
    def connects(self):
        self.get_results.clicked.connect( self.next_click)
        self.test_try.clicked.connect(self.first_timer)
        self.test_jump.clicked.connect(self.secondtimer)
        self.final_test.clicked.connect(self.thirdtimer)
        
    def first_timer(self):
        global time
        time = QTime(0,0,16)
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.timerchange)
        self.timer1.start(1000)


    def timerchange(self):
        global time 
        time = time.addSecs(-1)
        self.timer.setText(time.toString('hh:mm:ss'))
        self.timer.setFont(QFont('Times',35,QFont.Bold)) 
        self.timer.setStyleSheet('color: rgb(255,84,84)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer1.stop()
            self.timer.setStyleSheet('color: rgb(0,0,0)')


    def timercolorful(self):
        global time 
        time = time.addSecs(-1)
        self.timer.setText(time.toString('hh:mm:ss'))
        self.timer.setFont(QFont('Times',35,QFont.Bold)) 
        if time.toString('hh:mm:ss') == "00:00:58":
            self.timer.setStyleSheet('color: rgb(140, 252, 3)')
        if time.toString('hh:mm:ss') == '00:00:45':
            #self.timer1.stop()
            self.timer.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:15':
            self.timer.setStyleSheet('color: rgb(140,252,3)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer1.stop()
            self.timer.setStyleSheet('color: rgb(0,0,0')

    


    def secondtimer(self):
        global time
        time = QTime(0,0,30)
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.timerchange)
        self.timer1.start(1000)

    def thirdtimer(self):
        global time
        time = QTime(0,0,59)
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.timercolorful)
        self.timer1.start(1000)



    def next_click(self):
        self.hide()
        self.fw = FinalWin(self.fill_age.text() ,self.fill_seconds.text(),self.fill_one_line.text(),self.fill_second_line.text())
        
    
    


















