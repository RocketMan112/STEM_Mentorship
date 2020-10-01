import logging

from person_detector import FakeFixedPersonDetector
from drone_controller import DroneController
from configuration import DroneConfiguration
from ai import DroneAI

logging.basicConfig(
    format='[%(asctime)s] %(levelname)-7s (%(name)s) %(message)s',
    level=logging.DEBUG
)

log = logging.getLogger(__name__)


config = DroneConfiguration(udp_port=14550)
drone_controller = DroneController(config)

ai = DroneAI(
    config,
    drone_controller,
    FakeFixedPersonDetector()
)
ai.run()
