
from transitions import Machine
from PyQt5 import QtCore, QtGui, QtWidgets
from states import Ui_Form
import threading

from time import sleep
import random,sys

# Set up logging
import logging
from transitions import logger
logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s',filename='example2.log',datefmt='%m/%d/%Y %I:%M:%S %p')
logger.setLevel(logging.INFO)


class StateDialog(Ui_Form):

    def __init__(self, dialog):
        Ui_Form.__init__(self)
        states = ['INIT', 'A', 'B', 'C']
        self.machine = Machine(model=self, states=states, initial='INIT')
        self.setupUi(dialog)
        self.machine.add_transition('advance', 'INIT', 'A')
        self.machine.add_transition('advance', 'A', 'B','is_transition_AB')
        self.machine.add_transition('advance', 'B', 'C','is_transition_BC')
        self.machine.add_transition('advance', 'C', 'A','is_loop')

        self.pushButton_start.clicked.connect(self.FSM_thread)

        #self.buttonBox.ok.connect(self.ok)
        #self.buttonBox.abort.connect(self.abort)

    def is_transition_AB(self):
        return self.pushButton_1.isChecked()

    def is_transition_BC(self):
        return self.pushButton_2.isChecked()

    def is_loop(self):
        return True

    def on_enter_A(self):
        txt="[INFO] entering A"
        self.status_msg.addItem(txt)
        self.lcdNumber_1.display(1)
        sleep(2)

    def on_exit_A(self):
        self.lcdNumber_1.display(0)

    def on_enter_B(self):
        txt="[INFO] entering B"
        self.status_msg.addItem(txt)
        self.lcdNumber_2.display(1)
        sleep(2)

    def on_exit_B(self):
        self.lcdNumber_2.display(0)

    def on_enter_C(self):
        txt= "[INFO] entering C"
        self.status_msg.addItem(txt)
        self.lcdNumber_3.display(1)
        sleep(2)

    def on_exit_C(self):
        self.lcdNumber_3.display(0)

    def run_FSM(self):
        while True:
            # update state on screen
            self.lbl_FSM_States.setText(prog.state)
            if self.pushButton_3.isChecked():
                prog.advance()
            else:
                prog.to_INIT()
                txt = "[INFO] waiting for enable.."
                self.status_msg.addItem(txt)
                sleep(3)

    def FSM_thread(self):
        t = threading.Thread(name='FSM', target=self.run_FSM)
        t.daemon = True
        txt = '[INFO] started thread ' +t.getName()
        self.status_msg.addItem(txt)
        t.start()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = StateDialog(dialog)
    dialog.show()
    sys.exit(app.exec_())