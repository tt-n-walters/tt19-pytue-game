import os

# Open the correct folder, so Python knows where to loads images from
correct_location = os.path.dirname(os.path.abspath(__file__))
os.chdir(correct_location)


import monkeypatch

import game
