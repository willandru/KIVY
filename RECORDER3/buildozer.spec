# (str) Title of your application
title = AudioRecorderApp

# (str) Package name
package.name = audiorecorderapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3, kivy, audiostream, soundfile, cython

# (str) Application versioning (method 1)
version = 1.0

# (list) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# comma separated e.g. internet, Camera
android.permissions = RECORD_AUDIO, INTERNET

# (list) Services to declare
services =

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
