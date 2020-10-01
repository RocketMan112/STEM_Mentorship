import logging
log = logging.getLogger(__name__)

# Wire everything up with decision making. Reads values from the drone
# controller to see current status, uses the person detector and other sensors
# to determine the right next steps.


class DroneAI:
    def __init__(self, config, drone_controller, person_detector):
        log.info("Initialized DroneAI with person_detector: %s",
                 person_detector.name())
        self.person_detector = person_detector
        self.config = config

    def run(self):
        log.info("Starting DroneAI")
        log.debug("Nitty gritty details")
        log.warning("Unusual reading, ignoring")
        log.error("Aborting")
        pass
