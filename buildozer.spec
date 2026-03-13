[app]
title = MyGame
package.name = mygame
package.domain = org.mygame
source.dir = .
source.include_exts = py,png,jpg,jpeg,ogg,mp3,wav,ttf,json,atlas
version = 1.0
requirements = python3==3.10.12,kivy==2.3.0,pyjnius==1.5.0,hostpython3==3.10.12,pygame
orientation = landscape
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
