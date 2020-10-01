import logging
log = logging.getLogger(__name__)


class DroneConfiguration:
    def __init__(self, udp_port):
        self.udp_port = udp_port
        pass
