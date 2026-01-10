[app]
title = Citizen X
package.name = citizenx
package.domain = org.synthesis
source.dir = .
source.include_exts = py,png,db
version = 0.1

# REQUIREMENT DISTILLATION: Stripping all audio/video codecs
requirements = python3,kivy==2.3.0,sqlite3

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

icon.filename = %(source.dir)s/CITIZEN_X.png

# HARDWARE TARGETING
android.api = 33
android.minapi = 21
android.ndk = 25b
android.skip_update = False
android.accept_sdk_license = True

[buildozer]
# LOG_LEVEL 2 to force continuous output (prevents runner timeout)
log_level = 2
warn_on_root = 1
