import carla


class Tester:
    def __init__(self, world: carla.World):
        self._world = world
        self._ego_vehicle = None

    def set_ego_vehicle(self, vid):
        self._ego_vehicle = self._world.get_actor(vid)

    def scan_vehicles(self):
        vehicles: carla.ActorList = self._world.get_actors().filter("vehicle.*.*")
        for vehicle in vehicles:
            vehicle: carla.Vehicle
            print(vehicle, vehicle.get_transform())

    def scan_camera_rgb(self):
        cameras: carla.ActorList = self._world.get_actors().filter("sensor.camera.rgb")
        for camera in cameras:
            camera: carla.Vehicle
            print(camera, camera.get_transform())


if __name__ == '__main__':
    client = carla.Client("127.0.0.1", 2000)
    client.set_timeout(1)

    sim_world = client.get_world()
    t = Tester(sim_world)
    t.scan_vehicles()
