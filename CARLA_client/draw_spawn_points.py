import carla
import time

def draw_string(world, location, text="first"):
    world.debug.draw_string(location, text, draw_shadow=False, color=carla.Color(255,0,0), life_time=50.0)

def draw_point(world, location, size=0.1):
    world.debug.draw_point(location, size, carla.Color(255, 0, 0, 0), life_time=50.0)
    
def draw_hud_box(world, location, thickness=0.1):
    box_size = carla.Vector3D(2.0, 2.0, 0.0)
    box = carla.BoundingBox(location, box_size)
    rotation = carla.Rotation(yaw = -155)
    world.debug.draw_box(box, rotation, thickness, carla.Color(255, 0, 0, 0), life_time=50.0)

# Connect to the CARLA server
client = carla.Client('localhost', 2000)
client.set_timeout(20.0)

# Get the world and map
world = client.load_world('Town05')
carla_map = world.get_map()
# Get the map's spawn points
spawn_points = world.get_map().get_spawn_points()

first_spawn_point = spawn_points[0]

# Get spectator
spectator = world.get_spectator()

spectator_pos = carla.Transform(first_spawn_point.location + carla.Location(x=20,y=10,z=4),
                            carla.Rotation(yaw = first_spawn_point.rotation.yaw -155))
spectator.set_transform(spectator_pos)


for i in range(0, len(spawn_points)):
    str = f"point {i}"
    draw_string(world, spawn_points[i].location, str)


# draw_hud_box(world, first_spawn_point.location)
# Add some delay to visualize the changes
#time.sleep(50)

