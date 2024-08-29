from vehicle_control import *
from road_info import monitor_odd
from scenario_info import get_scenario_info
from scenario_info_manager_gui import Ui_MainWindow
import threading
from PyQt5 import QtCore, QtGui, QtWidgets

def main():
    
    threading.Thread(target=monitor_odd, args=[ego_vehicle, emergency_vehicle, world]).start()
    threading.Thread(target=set_spectator, args=[world, ego_vehicle]).start()
    
if __name__ == '__main__':
    scenario_info = {
                "road_type": "Motorway",
                "ego_position": "Approaching Intersection",
                "emv_position": "Cross Road",
                "emv_travel_direction": "Approaches Intersection"
            }
     # Main execution
    carla_town, ego_vehicle_spwan_point, emv_spawn_point = get_scenario_info(scenario_info)
    
    client, world = initialize_carla(carla_town)
    ego_vehicle, emergency_vehicle = spawn_vehicle(world, client, ego_vehicle_spwan_point, emv_spawn_point)
    camera, sensor_data = setup_camera(world, ego_vehicle)
    manual_control(world, ego_vehicle, sensor_data)
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
    # Cleanup
    # camera.stop()
    # ego_vehicle.destroy()

