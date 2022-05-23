import time

from . import RivalVehicleController
from . import RivalVehicleAction
from . import VehicleManager, CameraManager


def register_handlers(controller: RivalVehicleController):
    @controller.register("rotation/manual")
    def rotation_manual(action: RivalVehicleAction):
        print(action.get_type())
        camera_manager = CameraManager(controller.ego_vehicle)
        camera_manager.set_sensor(action.get_new_sensor_parameters())
        vehicle_manager = VehicleManager(controller.world)
        vehicle_manager.set_vehicle(action.get_new_vehicle_parameters())
        vehicle_manager.control_vehicle(action.get_new_vehicle_control_parameters())
        time.sleep(0.5)
        camera_manager.shoot()

    @controller.register("rotation/randSensorPosition")
    def rand_sensor_position(action: RivalVehicleAction):
        ...
