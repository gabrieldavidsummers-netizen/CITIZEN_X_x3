[app]
title = CITIZEN_X
package.name = citizen_x
package.domain = org.sovereign
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 4.6
REQUIREMENTS: Ensure Kivy and Android dependencies are locked
requirements = python3,kivy==2.3.0,hostpython3,android
ORIENTATION: Portrait only for high-intensity vertical operations
orientation = portrait
ICON: Ensure your 'citizen_x_icon.png' is in the same directory as main.py
icon.filename = %(source.dir)s/citizen_x_icon.png
PERMISSIONS
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
APP LOGO / PRE-LOAD
android.presplash_color = #020202
[buildozer]
log_level = 2
warn_on_root = 1
