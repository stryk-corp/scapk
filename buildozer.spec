[app]

title = Scholarverse Dashboard
package.name = scholarversedashboard
package.domain = app.scholarverse
source.dir = .
source.include_exts = py
source.exclude_dirs = __pycache__,.github,bin,.buildozer
version = 1.0.0
# requests needs its dependencies listed explicitly on Android
requirements = python3,kivy,requests,urllib3,chardet,idna,certifi
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 34
android.minapi = 23
android.ndk_api = 23
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
