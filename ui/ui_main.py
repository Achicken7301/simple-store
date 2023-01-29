# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\banhb\Documents\Projects\2023\simple-store\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1033, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.invoice_view_pdf = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.invoice_view_pdf.setFont(font)
        self.invoice_view_pdf.setObjectName("invoice_view_pdf")
        self.gridLayout.addWidget(self.invoice_view_pdf, 1, 0, 1, 1)
        self.print_invoice = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.print_invoice.setFont(font)
        self.print_invoice.setObjectName("print_invoice")
        self.gridLayout.addWidget(self.print_invoice, 1, 1, 1, 1)
        self.add_p2invoice = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.add_p2invoice.setFont(font)
        self.add_p2invoice.setObjectName("add_p2invoice")
        self.gridLayout.addWidget(self.add_p2invoice, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.invoice_name = QtWidgets.QLabel(self.centralwidget)
        self.invoice_name.setText("")
        self.invoice_name.setTextFormat(QtCore.Qt.MarkdownText)
        self.invoice_name.setObjectName("invoice_name")
        self.gridLayout.addWidget(self.invoice_name, 0, 0, 1, 4)
        self.invoice_table = QtWidgets.QTableWidget(self.centralwidget)
        self.invoice_table.setObjectName("invoice_table")
        self.invoice_table.setColumnCount(0)
        self.invoice_table.setRowCount(0)
        self.gridLayout.addWidget(self.invoice_table, 2, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1033, 21))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.dockWidget.setFont(font)
        self.dockWidget.setAcceptDrops(True)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.dockWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.cus_list = QtWidgets.QListWidget(self.dockWidgetContents)
        self.cus_list.setObjectName("cus_list")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.cus_list)
        self.cus_search_bar = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.cus_search_bar.setObjectName("cus_search_bar")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.cus_search_bar)
        self.add_cus = QtWidgets.QPushButton(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.add_cus.setFont(font)
        self.add_cus.setObjectName("add_cus")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.add_cus)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dockWidget_2.setFont(font)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.dockWidgetContents_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_2.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_3.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.p_name = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.p_name.setText("")
        self.p_name.setTextFormat(QtCore.Qt.MarkdownText)
        self.p_name.setObjectName("p_name")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.p_name)
        self.p_unit_price = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.p_unit_price.setText("")
        self.p_unit_price.setTextFormat(QtCore.Qt.MarkdownText)
        self.p_unit_price.setObjectName("p_unit_price")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.p_unit_price)
        self.p_location = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.p_location.setText("")
        self.p_location.setTextFormat(QtCore.Qt.MarkdownText)
        self.p_location.setObjectName("p_location")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.p_location)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)
        self.dockWidget_4 = QtWidgets.QDockWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.dockWidget_4.setFont(font)
        self.dockWidget_4.setAutoFillBackground(False)
        self.dockWidget_4.setObjectName("dockWidget_4")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.dockWidgetContents_4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.p_list = QtWidgets.QListWidget(self.dockWidgetContents_4)
        self.p_list.setObjectName("p_list")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.p_list)
        self.add_p = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.add_p.setObjectName("add_p")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.add_p)
        self.p_search_bar = QtWidgets.QLineEdit(self.dockWidgetContents_4)
        self.p_search_bar.setObjectName("p_search_bar")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.p_search_bar)
        self.dockWidget_4.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_4)
        self.actionTax_Setting = QtWidgets.QAction(MainWindow)
        self.actionTax_Setting.setObjectName("actionTax_Setting")
        self.menuSettings.addAction(self.actionTax_Setting)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cus_search_bar, self.cus_list)
        MainWindow.setTabOrder(self.cus_list, self.p_search_bar)
        MainWindow.setTabOrder(self.p_search_bar, self.p_list)
        MainWindow.setTabOrder(self.p_list, self.add_cus)
        MainWindow.setTabOrder(self.add_cus, self.add_p)
        MainWindow.setTabOrder(self.add_p, self.add_p2invoice)
        MainWindow.setTabOrder(self.add_p2invoice, self.invoice_table)
        MainWindow.setTabOrder(self.invoice_table, self.invoice_view_pdf)
        MainWindow.setTabOrder(self.invoice_view_pdf, self.print_invoice)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.invoice_view_pdf.setText(_translate("MainWindow", "View Invoice"))
        self.print_invoice.setText(_translate("MainWindow", "Print Invoice"))
        self.add_p2invoice.setText(_translate("MainWindow", "Add Product to Invoice"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Danh sách khách hàng"))
        self.add_cus.setText(_translate("MainWindow", "Add customer"))
        self.dockWidget_2.setWindowTitle(_translate("MainWindow", "Thông tin sản phẩm"))
        self.label.setText(_translate("MainWindow", "# Tên sản phẩm:"))
        self.label_2.setText(_translate("MainWindow", "**Đơn giá**"))
        self.label_3.setText(_translate("MainWindow", "**Vị trí trong kho**"))
        self.dockWidget_4.setWindowTitle(_translate("MainWindow", "Danh sách sản phẩm"))
        self.add_p.setText(_translate("MainWindow", "Add product"))
        self.actionTax_Setting.setText(_translate("MainWindow", "Tax Setting"))
