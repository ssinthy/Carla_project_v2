from vehicle_control import *
from road_info import monitor_odd
from scenario_info import get_scenario_info
from GUI.scenario_info_manager_gui import Ui_MainWindow
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

scenario_info_intersection = {
            "road_type": "Motorway",
            "ego_position": "Approaching Intersection",
            "emv_position": "Cross Road",
            "emv_travel_direction": "Approaches Intersection"
        }

scenario_info_default = {
            "road_type": "Motorway",
            "ego_position": "Traffic Lane",
            "emv_position": "Same Road",
            "emv_travel_direction": "Approaches from Behind"
        }
    # Main execution
carla_town, ego_vehicle_spwan_point, emv_spawn_point = get_scenario_info(scenario_info_default)

client, world = initialize_carla(carla_town)
ego_vehicle, emergency_vehicle = spawn_vehicle(world, client, ego_vehicle_spwan_point, emv_spawn_point)
camera, sensor_data = setup_camera(world, ego_vehicle)
threading.Thread(target=monitor_odd, args=[ego_vehicle, emergency_vehicle, world]).start()
threading.Thread(target=set_spectator, args=[world, ego_vehicle]).start()
threading.Thread(target=manual_control, args=[world, ego_vehicle, sensor_data]).start()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

# Cleanup
# camera.stop()
# ego_vehicle.destroy()

