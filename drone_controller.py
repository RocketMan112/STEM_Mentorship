import logging
log = logging.getLogger(__name__)

# Connects and controls the drone via Mavlink via Dronelink


class DroneController:
    def __init__(self, config):
        self.config = config

    def fly_forward(self, distance):
        pass
