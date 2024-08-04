import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
import carla

actor_list = []

class CarlaGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Carla Client GUI')
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        
        self.connect_button = QPushButton('Connect to Carla', self)
        self.connect_button.clicked.connect(self.connect_to_carla)
        layout.addWidget(self.connect_button)
        
        self.spawn_ego_button = QPushButton('Spawn Ego Vehicle', self)
        self.spawn_ego_button.clicked.connect(self.spawn_ego_vehicle)
        layout.addWidget(self.spawn_ego_button)

        self.spawn_emergency_vehicle_button = QPushButton('Spawn Emergency Vehicle', self)
        self.spawn_emergency_vehicle_button.clicked.connect(self.spawn_emergency_vehicle)
        layout.addWidget(self.spawn_emergency_vehicle_button)

        self.destroy_button = QPushButton('Destroy Vehicle', self)
        self.destroy_button.clicked.connect(self.destroy_vehicle)
        layout.addWidget(self.destroy_button)
        
        self.setGeometry(400, 400, 300, 200)
        
    def connect_to_carla(self):
        try:
            self.client = carla.Client('localhost', 2000)
            self.client.set_timeout(10.0)
            self.world = self.client.get_world()
            QMessageBox.information(self, "Info", "Connected to Carla")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to connect to Carla: {e}")

    def spawn_ego_vehicle(self):
        try:
            if not hasattr(self, 'world'):
                QMessageBox.critical(self, "Error", "Not connected to Carla")
                return
            
            blueprint_library = self.world.get_blueprint_library()
            bp = blueprint_library.filter('vehicle')[0]
            transform = self.world.get_map().get_spawn_points()[0]
            vehicle = self.world.spawn_actor(bp, transform)
            actor_list.append(vehicle)
            QMessageBox.information(self, "Info", f"Vehicle {vehicle.type_id} spawned")

            # Get spectator
            spectator = self.world.get_spectator()

            spectator_pos = carla.Transform(transform.location + carla.Location(x=20,y=10,z=4),
                                carla.Rotation(yaw = transform.rotation.yaw -155))
            spectator.set_transform(spectator_pos)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to spawn vehicle: {e}")


    def spawn_emergency_vehicle(self):
        try:
            if not hasattr(self, 'world'):
                QMessageBox.critical(self, "Error", "Not connected to Carla")
                return
            
            blueprint_library = self.world.get_blueprint_library()
            bp = blueprint_library.find('vehicle.carlamotors.firetruck')
            transform = self.world.get_map().get_spawn_points()[2]
            vehicle = self.world.spawn_actor(bp, transform)
            actor_list.append(vehicle)
            QMessageBox.information(self, "Info", f"Emergency Vehicle {vehicle.type_id} spawned")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to spawn emergency vehicle: {e}")

    def destroy_vehicle(self):
        try:
            for actor in actor_list:
                actor.destroy()
                QMessageBox.information(self, "Info", f"Vehicle {actor.type_id} cleaned up")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed destroy vehicle: {e}")


def window():
    app = QApplication(sys.argv)
    win = CarlaGUI()
    win.show()
    sys.exit(app.exec_())

window()