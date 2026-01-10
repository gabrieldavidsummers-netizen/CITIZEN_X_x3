[app]
title = Citizen X
package.name = citizenx
package.domain = org.synthesis
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,db
version = 0.1

requirements = python3,kivy==2.3.0,sqlite3,requests,certifi

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# ASSET ANCHORS
icon.filename = %(source.dir)s/CITIZEN_X.png

# PATH LOCKDOWN (Prevents the 30s crash)
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.2.9519653
android.api = 33
android.minapi = 21
android.ndk = 25b
android.skip_update = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
