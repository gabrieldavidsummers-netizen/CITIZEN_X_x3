[app]
title = CITIZEN_X
package.name = citizen_x_x3
package.domain = org.sovereign
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
requirements = python3,kivy==2.3.0,hostpython3,openssl,sqlite3
version = 1.0.0
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET, WAKE_LOCK, WRITE_EXTERNAL_STORAGE
android.allow_backup = False
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
