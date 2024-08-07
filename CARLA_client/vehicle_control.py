import carla
import random
import numpy as np
import pygame
import time
from carla_envornmental_condition import set_up_environment

def initialize_carla():
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    world = client.load_world('Town05')

    weather = carla.WeatherParameters(
        cloudiness=0.0,
        precipitation=0.0,
        sun_altitude_angle=10.0,
        sun_azimuth_angle=70.0,
        precipitation_deposits=0.0,
        wind_intensity=0.0,
        fog_density=0.0,
        wetness=0.0,
    )
    time_of_day, rain_status, fog_condition, fog_visibility, wind_force, cloud_condition = set_up_environment(world, weather)
    return client, world, time_of_day, rain_status, fog_condition, fog_visibility, wind_force, cloud_condition

def spawn_vehicle(world, client):
    bp_lib = world.get_blueprint_library()
    spawn_points = world.get_map().get_spawn_points()
    vehicle_bp = bp_lib.find('vehicle.audi.etron')
    ego_vehicle = world.try_spawn_actor(vehicle_bp, spawn_points[108])

    # Set spectator manual navigation
    spectator = world.get_spectator()
    location = ego_vehicle.get_location()
    transform = carla.Transform(ego_vehicle.get_transform().transform(carla.Location(x=-4, z=2)), ego_vehicle.get_transform().rotation)
    # spectator.set_transform(transform)

    # Spawn an emergency vehicle
    emergency_bp = world.get_blueprint_library().find('vehicle.carlamotors.firetruck')
    emergency_vehicle = world.spawn_actor(emergency_bp, spawn_points[56])
    # ego_vehicle.set_autopilot(True)
    # Set up the traffic manager
    traffic_manager = client.get_trafficmanager()
    traffic_manager_port = traffic_manager.get_port()

    # Set the vehicle to drive 30% faster than the current speed limit
    traffic_manager.vehicle_percentage_speed_difference(emergency_vehicle, -30)  # No speed variation
    
    # Make the vehicle ignore traffic lights
    traffic_manager.ignore_lights_percentage(emergency_vehicle, 100)
    
    # Turn on the vehicle's (emergency lights)
    from carla import VehicleLightState as vls
    emergency_vehicle.set_light_state(carla.VehicleLightState(vls.Special1))
        
    emergency_vehicle.set_autopilot(True, traffic_manager_port)
    return ego_vehicle, emergency_vehicle

def set_spectator(world, vehicle):
    while vehicle is not None:
        spectator = world.get_spectator()
        transform = carla.Transform(vehicle.get_transform().transform(carla.Location(x=-20, y= 0, z=8)), vehicle.get_transform().rotation)
        spectator.set_transform(transform)
        
def setup_camera(world, vehicle):
    bp_lib = world.get_blueprint_library()
    camera_bp = bp_lib.find('sensor.camera.rgb')
    camera_init_trans = carla.Transform(carla.Location(x=-0.1, z=1.7))
    camera = world.spawn_actor(camera_bp, camera_init_trans, attach_to=vehicle)

    image_w = camera_bp.get_attribute("image_size_x").as_int()
    image_h = camera_bp.get_attribute("image_size_y").as_int()
    sensor_data = {'rgb_image': np.zeros((image_h, image_w, 4))}
    
    def rgb_callback(image):
        img = np.reshape(np.copy(image.raw_data), (image.height, image.width, 4))
        img[:, :, 3] = 255
        sensor_data['rgb_image'] = img

    camera.listen(lambda image: rgb_callback(image))
    return camera, sensor_data

def manual_control(world, ego_vehicle, sensor_data):
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.HWSURFACE | pygame.DOUBLEBUF)
    clock = pygame.time.Clock()
    done = False
    control = carla.VehicleControl()

    
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            control.throttle = min(control.throttle + 0.05, 1.0)
        else:
            control.throttle = 0.0

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            control.brake = min(control.brake + 0.2, 1.0)
        else:
            control.brake = 0.0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            control.steer = max(control.steer - 0.05, -1.0)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            control.steer = min(control.steer + 0.05, 1.0)
        else:
            control.steer = 0.0

        control.hand_brake = keys[pygame.K_SPACE]

        # Apply the control to the ego vehicle and tick the simulation
        ego_vehicle.apply_control(control)
        world.tick()

        # Update the display and check for the quit event
        pygame.display.flip()
        pygame.display.update()
                
        if sensor_data['rgb_image'] is not None:
            image = np.array(sensor_data['rgb_image'], dtype=np.uint8)[:, :, :3]
            image_surface = pygame.surfarray.make_surface(image.swapaxes(0, 1))
            display.blit(image_surface, (0, 0))
            pygame.display.flip()

        clock.tick(60)

