import logging

from .EMD import EMD
from .EEMD import EEMD
from .EMD2d import EMD2D
from .BEMD import BEMD
from .CEEMDAN import CEEMDAN

logger = logging.getLogger('pyemd')
logger.addHandler(logging.NullHandler())
if len(logger.handlers)==1:
    logging.basicConfig(level=logging.INFO)

