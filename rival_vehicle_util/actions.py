from . import NewVehicleParameters, NewSensorParameters, NewVehicleControlParameters


class RivalVehicleAction:
    def __init__(self, data):
        self._type = data['action']
        self._data = data['data']

    def get_type(self) -> str:
        return self._type

    def get_new_vehicle_parameters(self) -> NewVehicleParameters:
        vehicle_data = self._data['vehicle']
        return NewVehicleParameters(blueprint=vehicle_data['blueprintId'],
                                    **vehicle_data["position"],
                                    **vehicle_data['rotation'])

    def get_new_sensor_parameters(self) -> NewSensorParameters:
        sensor_data = self._data['sensor']
        return NewSensorParameters(blueprint=sensor_data['blueprintId'],
                                   **sensor_data["position"],
                                   **sensor_data['rotation'])

    def get_new_vehicle_control_parameters(self) -> NewVehicleControlParameters:
        vehicle_steer = self._data['vehicleSteer']
        return NewVehicleControlParameters(vehicle_steer)
