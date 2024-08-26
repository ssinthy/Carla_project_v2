from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
import subprocess

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()
        
    def button_clicked(self):
        try:
            # Command to start the CARLA simulator (adjust path as needed)
            # subprocess.Popen(['./CarlaUE4.sh'], cwd='/path/to/Carla/Simulator/Root')  # On Linux or MacOS
            # subprocess.Popen(['CarlaUE4.exe'], cwd='D:\\CARLA_0.9.15\\WindowsNoEditor')  # On Windows
            
            result = subprocess.run(['python', 'D:\\CARLA_0.9.15\\client\\Carla_project-v2\\CARLA_client\\main.py'], capture_output=True, text=True)

            if result.stdout:
                print("Output of carla_api_script.py:", result.stdout)
            if result.stderr:
                print("Error in carla_api_script.py:", result.stderr)

            QMessageBox.information(self, 'Success', 'CARLA API Script executed.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to run CARLA API script: {e}')
                
    def initUI(self):
        self.setGeometry(400, 400, 600, 600)
        self.setWindowTitle("Scenario Info")
        
        self.start_carla = QtWidgets.QPushButton(self)
        self.start_carla.setText("Start Simulator")
        self.start_carla.clicked.connect(self.button_clicked)
            
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()