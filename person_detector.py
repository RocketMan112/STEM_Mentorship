import logging
log = logging.getLogger(__name__)


class PersonDetectorBase:
    def initialize(self):
        pass

    def name(self):
        return "Error - Base PersonDetector class, not for direct use"


class FakeFixedPersonDetector(PersonDetectorBase):
    def initialize(self):
        pass

    def name(self):
        return "FakeFixedPersonDetector"


class ComputerVisionPersonDetector(PersonDetectorBase):
    def initialize(self):
        pass

    def name(self):
        return "ComputerVisionPersonDetector"
