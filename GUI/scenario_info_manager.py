from pymongo import MongoClient
from bson.objectid import ObjectId

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client['scenario']
        self.collection = self.db['scenario_info']

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(558, 438)
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
        self.label_weather.setGeometry(QtCore.QRect(20, 200, 151, 16))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_weather.setFont(font)
        self.label_weather.setObjectName("label_weather")
        self.comboBox_weather = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_weather.setGeometry(QtCore.QRect(260, 190, 181, 23))
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
        self.label_day_time.setGeometry(QtCore.QRect(20, 250, 121, 16))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_day_time.setFont(font)
        self.label_day_time.setObjectName("label_day_time")
        self.comboBox_time_of_day = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_time_of_day.setGeometry(QtCore.QRect(260, 250, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_time_of_day.setFont(font)
        self.comboBox_time_of_day.setObjectName("comboBox_time_of_day")
        self.comboBox_time_of_day.addItem("")
        self.comboBox_time_of_day.addItem("")
        self.label_emv_position = QtWidgets.QLabel(self.centralwidget)
        self.label_emv_position.setGeometry(QtCore.QRect(20, 136, 211, 20))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_emv_position.setFont(font)
        self.label_emv_position.setObjectName("label_emv_position")
        self.comboBox_emv_position = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_emv_position.setGeometry(QtCore.QRect(260, 130, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_emv_position.setFont(font)
        self.comboBox_emv_position.setObjectName("comboBox_emv_position")
        self.comboBox_emv_position.addItem("")
        self.comboBox_emv_position.addItem("")
        self.comboBox_emv_position.addItem("")
        self.comboBox_emv_position.addItem("")
        self.comboBox_emv_position.addItem("")
        self.set_up_scenario = QtWidgets.QPushButton(self.centralwidget)
        self.set_up_scenario.setGeometry(QtCore.QRect(170, 340, 131, 23))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.set_up_scenario.setFont(font)
        self.set_up_scenario.setObjectName("set_up_scenario")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.set_up_scenario.clicked.connect(self.pressed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ScenarioInfoManager"))
        self.labe_ego_position.setText(_translate("MainWindow", "Ego Vehicle Position"))
        self.comboBox_ego_position.setItemText(0, _translate("MainWindow", "Subject Lane"))
        self.comboBox_ego_position.setItemText(1, _translate("MainWindow", "Left Lane"))
        self.comboBox_ego_position.setItemText(2, _translate("MainWindow", "Right Lane"))
        self.comboBox_ego_position.setItemText(3, _translate("MainWindow", "Opposite Lane"))
        self.comboBox_ego_position.setItemText(4, _translate("MainWindow", "Intersection"))
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
        self.label_emv_position.setText(_translate("MainWindow", "Emergency Vehicle Position"))
        self.comboBox_emv_position.setItemText(0, _translate("MainWindow", "Subject Lane"))
        self.comboBox_emv_position.setItemText(1, _translate("MainWindow", "Left Lane"))
        self.comboBox_emv_position.setItemText(2, _translate("MainWindow", "Right Lane"))
        self.comboBox_emv_position.setItemText(3, _translate("MainWindow", "Opposite Lane"))
        self.comboBox_emv_position.setItemText(4, _translate("MainWindow", "Intersection"))
        self.set_up_scenario.setText(_translate("MainWindow", "Set Up Scenario"))

    def pressed(self):
        road_type = self.comboBox_road_type.currentText()
        ego_position = self.comboBox_ego_position.currentText()
        emv_position = self.comboBox_emv_position.currentText()
        weather_condition = self.comboBox_weather.currentText()
        time_of_day = self.comboBox_time_of_day.currentText()
        print(road_type, ego_position, emv_position)
        

        try:
            filter = {'_id': ObjectId("66cdd2f14f8c5939fc9b1150")}
            # Insert the selected value into MongoDB
            new_data = {"$set": {
                    "road_type": road_type,
                    "ego_position": ego_position,
                    "emv_position": emv_position
                }
            }
            
            self.collection.update_one(filter, new_data, upsert=True)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to save to MongoDB: {e}')




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
