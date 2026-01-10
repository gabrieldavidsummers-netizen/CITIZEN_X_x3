[app]
title = Citizen X
package.name = citizenx
package.domain = org.synthesis
source.dir = .
source.include_exts = py,png,db
version = 0.1

# CORE ANCHORS - Fixed versions for NDK 25b stability
requirements = python3==3.10.12,kivy==2.3.0,sqlite3,hostpython3==3.10.12,libffi,pyjnius==1.6.0

orientation = portrait
icon.filename = icon.png
presplash.filename = icon.png

# HARDWARE TARGETING - Locked to avoid API 35/36 drift
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_path = 
android.sdk_path = 
android.accept_sdk_license = True
android.skip_update = False

[buildozer]
log_level = 2
