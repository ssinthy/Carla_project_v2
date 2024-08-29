# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scenario_info_manager_v1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 445)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labe_ego_position = QtWidgets.QLabel(self.centralwidget)
        self.labe_ego_position.setGeometry(QtCore.QRect(20, 80, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labe_ego_position.setFont(font)
        self.labe_ego_position.setObjectName("labe_ego_position")
        self.comboBox_ego_position = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_ego_position.setGeometry(QtCore.QRect(260, 80, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_ego_position.setFont(font)
        self.comboBox_ego_position.setObjectName("comboBox_ego_position")
        self.comboBox_ego_position.addItem("")
        self.comboBox_ego_position.addItem("")
        self.comboBox_ego_position.addItem("")
        self.road_type_label = QtWidgets.QLabel(self.centralwidget)
        self.road_type_label.setGeometry(QtCore.QRect(20, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.road_type_label.setFont(font)
        self.road_type_label.setObjectName("road_type_label")
        self.comboBox_road_type = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_road_type.setGeometry(QtCore.QRect(260, 30, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_road_type.setFont(font)
        self.comboBox_road_type.setObjectName("comboBox_road_type")
        self.comboBox_road_type.addItem("")
        self.comboBox_road_type.addItem("")
        self.comboBox_road_type.addItem("")
        self.label_weather = QtWidgets.QLabel(self.centralwidget)
        self.label_weather.setGeometry(QtCore.QRect(20, 230, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_weather.setFont(font)
        self.label_weather.setObjectName("label_weather")
        self.comboBox_weather = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_weather.setGeometry(QtCore.QRect(260, 220, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_weather.setFont(font)
        self.comboBox_weather.setObjectName("comboBox_weather")
        self.comboBox_weather.addItem("")
        self.comboBox_weather.addItem("")
        self.comboBox_weather.addItem("")
        self.comboBox_weather.addItem("")
        self.comboBox_weather.addItem("")
        self.label_day_time = QtWidgets.QLabel(self.centralwidget)
        self.label_day_time.setGeometry(QtCore.QRect(20, 270, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_day_time.setFont(font)
        self.label_day_time.setObjectName("label_day_time")
        self.comboBox_time_of_day = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_time_of_day.setGeometry(QtCore.QRect(260, 270, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_time_of_day.setFont(font)
        self.comboBox_time_of_day.setObjectName("comboBox_time_of_day")
        self.comboBox_time_of_day.addItem("")
        self.comboBox_time_of_day.addItem("")
        self.label_emv_travel_direction = QtWidgets.QLabel(self.centralwidget)
        self.label_emv_travel_direction.setGeometry(QtCore.QRect(20, 180, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_emv_travel_direction.setFont(font)
        self.label_emv_travel_direction.setObjectName("label_emv_travel_direction")
        self.comboBox_emv_travel_direction = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_emv_travel_direction.setGeometry(QtCore.QRect(260, 180, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_emv_travel_direction.setFont(font)
        self.comboBox_emv_travel_direction.setObjectName("comboBox_emv_travel_direction")
        self.comboBox_emv_travel_direction.addItem("")
        self.comboBox_emv_travel_direction.addItem("")
        self.comboBox_emv_travel_direction.addItem("")
        self.comboBox_emv_travel_direction.addItem("")
        self.comboBox_emv_travel_direction.addItem("")
        self.comboBox_emv_travel_direction.addItem("")
        self.comboBox_emv_travel_direction.addItem("")
        self.set_up_scenario = QtWidgets.QPushButton(self.centralwidget)
        self.set_up_scenario.setGeometry(QtCore.QRect(220, 350, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.set_up_scenario.setFont(font)
        self.set_up_scenario.setObjectName("set_up_scenario")
        self.spinBox_safety_distance = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_safety_distance.setGeometry(QtCore.QRect(260, 310, 48, 20))
        self.spinBox_safety_distance.setObjectName("spinBox_safety_distance")
        self.Label_Safety_Distance = QtWidgets.QLabel(self.centralwidget)
        self.Label_Safety_Distance.setGeometry(QtCore.QRect(20, 310, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_Safety_Distance.setFont(font)
        self.Label_Safety_Distance.setObjectName("Label_Safety_Distance")
        self.label_emv_position_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_emv_position_2.setGeometry(QtCore.QRect(20, 130, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_emv_position_2.setFont(font)
        self.label_emv_position_2.setObjectName("label_emv_position_2")
        self.comboBox_ego_position_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_ego_position_2.setGeometry(QtCore.QRect(260, 130, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_ego_position_2.setFont(font)
        self.comboBox_ego_position_2.setObjectName("comboBox_ego_position_2")
        self.comboBox_ego_position_2.addItem("")
        self.comboBox_ego_position_2.addItem("")
        self.comboBox_ego_position_2.addItem("")
        self.comboBox_ego_position_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ScenarioInfoManager"))
        self.labe_ego_position.setText(_translate("MainWindow", "Ego Vehicle Position"))
        self.comboBox_ego_position.setItemText(0, _translate("MainWindow", "Traffic Lane"))
        self.comboBox_ego_position.setItemText(1, _translate("MainWindow", "Approaching Intersection"))
        self.comboBox_ego_position.setItemText(2, _translate("MainWindow", "Approaching T-Junction"))
        self.road_type_label.setText(_translate("MainWindow", "Road Type"))
        self.comboBox_road_type.setItemText(0, _translate("MainWindow", "Motorway"))
        self.comboBox_road_type.setItemText(1, _translate("MainWindow", "Expressway"))
        self.comboBox_road_type.setItemText(2, _translate("MainWindow", "local Road"))
        self.label_weather.setText(_translate("MainWindow", "Weather Condition"))
        self.comboBox_weather.setItemText(0, _translate("MainWindow", "Clear"))
        self.comboBox_weather.setItemText(1, _translate("MainWindow", "Cloudy"))
        self.comboBox_weather.setItemText(2, _translate("MainWindow", "Light Rain"))
        self.comboBox_weather.setItemText(3, _translate("MainWindow", "Moderate Rain"))
        self.comboBox_weather.setItemText(4, _translate("MainWindow", "Heavy Rain"))
        self.label_day_time.setText(_translate("MainWindow", "Time of Day"))
        self.comboBox_time_of_day.setItemText(0, _translate("MainWindow", "Day time"))
        self.comboBox_time_of_day.setItemText(1, _translate("MainWindow", "Night time"))
        self.label_emv_travel_direction.setText(_translate("MainWindow", "EMV Travel Direction"))
        self.comboBox_emv_travel_direction.setItemText(0, _translate("MainWindow", "Approaches from Behind"))
        self.comboBox_emv_travel_direction.setItemText(1, _translate("MainWindow", "As Lead Vehicle"))
        self.comboBox_emv_travel_direction.setItemText(2, _translate("MainWindow", "Approaches from Right Lane"))
        self.comboBox_emv_travel_direction.setItemText(3, _translate("MainWindow", "Approaches from Left Lane"))
        self.comboBox_emv_travel_direction.setItemText(4, _translate("MainWindow", "Approaches on Opposite Lane"))
        self.comboBox_emv_travel_direction.setItemText(5, _translate("MainWindow", "Approaches Intersection"))
        self.comboBox_emv_travel_direction.setItemText(6, _translate("MainWindow", "Approaches T-Junction"))
        self.set_up_scenario.setText(_translate("MainWindow", "Set Up Scenario"))
        self.Label_Safety_Distance.setText(_translate("MainWindow", "Safety Distance (m)"))
        self.label_emv_position_2.setText(_translate("MainWindow", "Emergency Vehicle Position"))
        self.comboBox_ego_position_2.setItemText(0, _translate("MainWindow", "Same Road"))
        self.comboBox_ego_position_2.setItemText(1, _translate("MainWindow", "Parallel Road"))
        self.comboBox_ego_position_2.setItemText(2, _translate("MainWindow", "Opposite Road"))
        self.comboBox_ego_position_2.setItemText(3, _translate("MainWindow", "Cross Road"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
