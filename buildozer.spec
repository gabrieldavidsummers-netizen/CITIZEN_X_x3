[app]

# (str) Title of your application
title = CITIZEN_X : SIG-13579

# (str) Package name
package.name = citizen_x_sovereign

# (str) Package domain (needed for android/ios packaging)
package.domain = org.glitch

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (list) Application requirements
# Added openssl for potential secure socket layer logic
requirements = python3,kivy==2.3.0,hostpython3,openssl

# (str) Application versioning
version = 1.0.0

# (list) Permissions
# WAKE_LOCK ensures the logic doesn't time out during heavy processing
android.permissions = INTERNET, WAKE_LOCK

# (int) Orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (list) Android archs to build for (Standard for most modern phones)
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = False

[buildozer]
log_level = 2
warn_on_root = 1
