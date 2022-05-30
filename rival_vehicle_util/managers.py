import os
import weakref

import carla
carla.AttachmentType.SpringArm
from . import NewVehicleParameters, NewSensorParameters, NewVehicleControlParameters


camera = world.spawn_actor(camera_bp, relative_transform, attach_to=my_vehicle, carla.AttachmentType.Rigid)

class VehicleManager:
    def __init__(self, world: carla.World):
        self.vehicle = None
        self._world = world

    def set_vehicle(self, parameters: NewVehicleParameters):
        vehicle = parameters.new_vehicle(self._world)
        self.vehicle = vehicle

    def control_vehicle(self, parameters: NewVehicleControlParameters):
        parameters.update_control(self.vehicle)


class CameraManager:
    def __init__(self, parent_actor: carla.Actor):
        self.sensor = None
        self._parent = parent_actor
        self._default_sensor_blueprint = "sensor.camera.rgb"
        self._out_dir = r"D:\workspace2022\simulator"
        self._recording = False

    def set_sensor(self, parameters: NewSensorParameters):
        sensor = parameters.new_sensor(self._parent.get_world(), self._parent)
        self.sensor = sensor
        weak_self = weakref.ref(self)
        self.sensor.listen(lambda image: CameraManager._parse_image(weak_self, image))

    def shoot(self):
        self._recording = True

    @staticmethod
    def _parse_image(weak_self, image):
        self = weak_self()
        if not self:
            return
        if self._recording:
            print(self._recording)
            save_path = os.path.join(self._out_dir, '%08d' % image.frame)
            print(save_path)
            print(image)
            image.save_to_disk(save_path)
