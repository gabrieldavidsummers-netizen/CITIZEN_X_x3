[app]
title = Citizen X
package.name = citizenx
package.domain = org.synthesis
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,db
version = 0.1
requirements = python3,kivy==2.3.0,sqlite3
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
icon.filename = %(source.dir)s/CITIZEN_X.png
android.api = 33
android.minapi = 21
android.ndk = 25b
android.skip_update = False
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
