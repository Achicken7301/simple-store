from PyQt5.QtWidgets import QMessageBox


class NotificationView:
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

    def NotiView(msg: str):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Notification!!!")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.setText(msg)
        if msgBox.exec():
            print("OK")
        else:
            print("Cancel")
