import cv2
import numpy as np
import os

from PIL import ImageGrab
from time import time

# Author : co2plant

os.chdir(os.path.dirname(os.path.abspath(__file__)))


loop_time  = time()
while(True):
    screenshot = ImageGrab.grab()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

print('Done.')