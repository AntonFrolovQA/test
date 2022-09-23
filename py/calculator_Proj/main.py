from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from pip import main
from calc_UI import Ui_CalculatorForm



def main():

    # Create Application
    app = QtWidgets.QApplication(sys.argv)

    # Create form and init UI
    CalculatorForm = QtWidgets.QWidget()
    ui = Ui_CalculatorForm()
    ui.setupUi(CalculatorForm)
    CalculatorForm.show()

    # Hook logic
    outputResult = []
    def inputInteger():
        ui.ShowResultSpace.setText("some integer")
    def inputOperator():
        ui.ShowResultSpace.setText("some operator")
    def inputCancel():
        ui.ShowResultSpace.clear()

    ui.Button_0.clicked.connect(inputInteger)
    ui.Button_C.clicked.connect(inputCancel)
    ui.Button_Plus.clicked.connect(inputOperator)

    # Run main loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()