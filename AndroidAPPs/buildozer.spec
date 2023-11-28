[app]

# (str) Title of your application
title = HelloKivyApp

# (str) Package name
package.name = hellokivyapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas
source.dir = .

# (str) Version of your application
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if build is not optimized (default is 1)
warn_on_build = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build profiles storage, absolute or relative to spec file
# profile_dir = ./.buildozer

# (str) Path to projects storage, absolute or relative to spec file
# project_dir = ./.buildozer

# (str) Path to current project (not to be used with this recipe)
# project.source = .

# (bool) Remove .buildozer directory after successful android build (default is True)
# broadcast_cw_remove_build = true

# (str) Path to default/first target to build (default is android)
# target = android
