[app]
title = Citizen X
package.name = citizenx
package.domain = org.synthesis
source.dir = .
source.include_exts = py,png,db
version = 0.1

# CORE ANCHORS - Added sqlite3 for NDK linking
requirements = python3,kivy==2.3.0,hostpython3,libffi,sqlite3,cython==0.29.33,pyjnius==1.6.0

orientation = portrait
icon.filename = icon.png
presplash.filename = icon.png

# HARDWARE TARGETING
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.skip_update = False

[buildozer]
log_level = 2
