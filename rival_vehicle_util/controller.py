from . import RivalVehicleAction


class RivalVehicleController:
    def __init__(self, world, ego_vehicle):
        self.world = world
        self.ego_vehicle = ego_vehicle
        self._handlers = {}

    def register(self, action):
        def decorator(f):
            self._handlers[action] = f
            return f

        return decorator

    def distribute(self, data):
        action: RivalVehicleAction = RivalVehicleAction(data)
        # 业务分发
        handler = self._handlers.get(action.get_type())
        if handler is not None:
            handler(action)
