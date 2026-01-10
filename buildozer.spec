[app]
title = Citizen X
package.name = citizenx
package.domain = org.synthesis
source.dir = .
source.include_exts = py,png,db
version = 0.1

# PINNED REQUIREMENTS
requirements = python3,kivy==2.3.0,sqlite3,hostpython3,cython==0.29.33,pyjnius==1.6.0

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b
android.skip_update = False
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
