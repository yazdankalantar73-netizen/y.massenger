[app]

title = Y MESSENGER
package.name = ymessenger
package.domain = com.yazdanscript

source.dir = .
source.include_exts = py,png,jpg,jpeg,gif,kv,json,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2
warn_on_root = 1


[app:android]

android.api = 35
android.minapi = 21
android.ndk = 27c
android.archs = arm64-v8a
android.accept_sdk_license = True