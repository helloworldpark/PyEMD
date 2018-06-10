import logging

from PyEMD.PyEMD.EMD import EMD
from PyEMD.PyEMD.EEMD import EEMD
from PyEMD.PyEMD.EMD2d import EMD2D
from PyEMD.PyEMD.BEMD import BEMD
from PyEMD.PyEMD.CEEMDAN import CEEMDAN

logger = logging.getLogger('pyemd')
logger.addHandler(logging.NullHandler())
if len(logger.handlers)==1:
    logging.basicConfig(level=logging.INFO)

