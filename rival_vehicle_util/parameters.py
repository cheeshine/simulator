import carla


class BaseNewActorParameters:
    def __init__(self, blueprint=None, x=None, y=None, z=None, pitch=None, yaw=None, roll=None):
        self.blueprint = blueprint
        self.x = x
        self.y = y
        self.z = z
        self.pitch = pitch
        self.yaw = yaw
        self.roll = roll

    def get_transform(self) -> carla.Transform:
        return carla.Transform(carla.Location(x=self.x, y=self.y, z=self.z),
                               carla.Rotation(pitch=self.pitch, yaw=self.yaw, roll=self.roll))


class NewSensorParameters(BaseNewActorParameters):
    def new_sensor(self, world: carla.World, attach_to) -> carla.Actor:
        transform = self.get_transform()
        blueprint = world.get_blueprint_library().find(self.blueprint or "sensor.camera.rgb")
        return world.spawn_actor(blueprint, transform, attach_to=attach_to)


class NewVehicleParameters(BaseNewActorParameters):
    def new_vehicle(self, world: carla.World) -> carla.Actor:
        transform = self.get_transform()
        blueprint = world.get_blueprint_library().find(self.blueprint)
        return world.spawn_actor(blueprint, transform)


class NewVehicleControlParameters:
    def __init__(self, steer=None):
        self.steer = steer

    def update_control(self, control: carla.VehicleControl) -> carla.VehicleControl:
        control.steer = self.steer
        return control
