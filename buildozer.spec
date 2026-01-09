[app]
title = Citizen X
package.name = citizenx
package.domain = org.synthesis
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1

# SOVEREIGN REQUIREMENTS
requirements = python3,kivy==2.3.0,requests,urllib3,certifi,charset-normalizer,idna

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# NDK/SDK Anchors
android.api = 33
android.minapi = 21
android.ndk = 25b
android.skip_update = False
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
