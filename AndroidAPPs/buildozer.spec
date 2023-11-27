[app]

# Title of your application
title = MyKivyApp

# Package name
package.name = mykivyapp

# Package domain (needed for android/ios packaging)
package.domain = org.test

# Source code directory
source.dir = .

# Source files to include (let empty to include all the files)
source.include_exts = py,kv

# Application version
version = 1.0

# Application requirements
requirements = python3,kivy==2.0.0,pyjnius==1.5.0

# Specify Cython version
cython.depends = kivy==2.0.0,pyjnius==1.5.0

# Permissions
android.permissions = INTERNET

# Supported orientations
orientation = portrait

# Android specific settings
fullscreen = 0
android.api = 30
android.minapi = 21
android.archs = armeabi-v7a

[buildozer]

# Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
