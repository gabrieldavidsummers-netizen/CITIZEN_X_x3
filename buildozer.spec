[app]

# (str) Title of your application
title = CITIZEN_X

# (str) Package name
package.name = citizen_x

# (str) Package domain (needed for android/ios packaging)
package.domain = org.vault

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let's ensure the lexicon is packed)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Application requirements
# Note: Ensure you have any specific encryption libs here if needed
requirements = python3,kivy,hostpython3

# (str) Application versioning
version = 1.0.0-Σ∞

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# (int) Orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (str) Custom image for the loader
# presplash.filename = %(source.dir)s/CITIZEN_X.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/CITIZEN_X.png

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
