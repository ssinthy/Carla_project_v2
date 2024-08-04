import carla
import time

# Connect to the CARLA server
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)

# Read the OpenDRIVE file into a string
with open('D:\\CARLA_0.9.15\\WindowsNoEditor\\PythonAPI\\util\\opendrive\\DE_Hamburg_Yellow_Split_26112023.xodr', 'r') as file:
    opendrive_string = file.read()

# Set map parameters if needed
parameters = carla.OpendriveGenerationParameters(
    vertex_distance=2.0,
    max_road_length=50.0,
    wall_height=1.0,
    additional_width=0.6,
    smooth_junctions=True,
    enable_mesh_visibility=True
)

# Generate the CARLA world from the OpenDRIVE file
world = client.generate_opendrive_world(opendrive_string, parameters)

bp_lib = world.get_blueprint_library()
spawn_points = world.get_map().get_spawn_points()
vehicle_bp = bp_lib.find('vehicle.audi.etron')
ego_vehicle = world.try_spawn_actor(vehicle_bp, spawn_points[15])
spectator = world.get_spectator()
transform = carla.Transform(ego_vehicle.get_transform().transform(carla.Location(x=-4, z=2.5)), ego_vehicle.get_transform().rotation)
spectator.set_transform(transform)
time.sleep(5)
ego_vehicle.set_autopilot(True)
time.sleep(50)