import os

import appdirs

# The default directory for application data (i.e., configuration).
DATA_DIR = appdirs.user_data_dir(appname="mu", appauthor="python")

# The name of the default virtual environment used by Mu.
VENV_NAME = "mu_venv"

# The directory containing default virtual environment.
VENV_DIR = os.path.join(DATA_DIR, VENV_NAME)

# Maximum line length for using both in Check and Tidy
MAX_LINE_LENGTH = 88

# Vertical edge settings - vertical lines to limit assist maximum line length
# Check https://www.scintilla.org/ScintillaDoc.html#SCI_SETEDGEMODE
# EDGE_NONE = 0; EDGE_LINE = 1; EDGE_BACKGROUND = 2; EDGE_MULTILINE = 3
# EDGE_MULTILINE not yet implemented - please limit choice to 0, 1 or 2
LONG_LINES_EDGE_MODE = 0

# The user's home directory.
HOME_DIRECTORY = os.path.expanduser("~")

# Name of the directory within the home folder to use by default
WORKSPACE_NAME = "mu_code"

# Minimum window width and height values
# Float values to relative factor, integers for pixels
# Ex: screen resolution is 1366x768 pixels
# a) MIN_WINDOW_WIDTH = 2.0 --> window_width = 1366 // 2.0 = 683
# b) MIN_WINDOW_WIDTH = 640 --> window_width = 640
# Note: the application will apply a minimum of 600x400 pixels to allow 
# readability
MIN_WINDOW_WIDTH = 4.0
MIN_WINDOW_HEIGHT = 4.0

# Icon and font size
MAX_ICON_SIZE_PX = 64
MAX_ICON_SIZE_REL_WIDTH = 24
MAX_ICON_SIZE_REL_HEIGHT = 24
MAX_FONT_SIZE_REL_ICON = 4