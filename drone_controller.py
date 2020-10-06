import dronekit
import logging
log = logging.getLogger(__name__)

# Connects and controls the drone via Mavlink via Dronelink


class DroneController:
    def __init__(self, config):
        self.config = config
        self.connect()

    def connect(self):
        listen_address = '127.0.0.1:' + str(self.config.udp_port)
        log.debug("Starting to listen for the drone at %s", listen_address)
        self.vehicle = dronekit.connect(listen_address, wait_ready=True)
        log.info("Connected to Drone")

    def mode(self):
        return self.vehicle.mode.name

    def fly_forward(self, distance):
        pass
