from PyQt5.QtWidgets import QMessageBox


def WarningView(msg: str):
    msgBox = QMessageBox()
    msgBox.setWindowTitle("Warning!!!")
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msgBox.setText(msg)
    if msgBox.exec():
        print("OK")
    else:
        print("Cancel")
