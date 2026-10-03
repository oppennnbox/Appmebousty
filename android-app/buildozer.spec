[app]

# Название приложения
title = My First App

# Имя пакета (без пробелов, строчные буквы)
package.name = myfirstapp

# Домен (любой, обычно в обратном порядке)
package.domain = org.test

# Исходники
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

# Версия
version = 0.1

# Зависимости
requirements = python3,kivy==2.3.0

# Ориентация экрана
orientation = portrait

# На весь экран
fullscreen = 0

# Иконка и заставка (файлы должны существовать, если указываете)
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

# Разрешения (пусто, так как ничего не нужно)
android.permissions =

# Версии Android
android.api = 34
android.minapi = 31
android.ndk_api = 24

# Архитектуры
android.archs = arm64-v8a, armeabi-v7a

# Разрешить сборку отладочного APK
android.debug = True

# Release подпись (для debug не нужна)
# android.release_artifact = apk
# android.debug_artifact = apk

# Не запрашивать ввод в интерактивном режиме
p4a.branch = master

[buildozer]

log_level = 2
warn_on_root = 1
