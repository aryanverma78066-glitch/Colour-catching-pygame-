name: Build APK

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Extract zip
      run: unzip game_project.zip -d game_project_extracted
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y \
          build-essential git zip unzip \
          openjdk-17-jdk python3-dev \
          libsdl2-dev libsdl2-image-dev \
          libsdl2-mixer-dev libsdl2-ttf-dev
    
    - name: Install buildozer
      run: |
        pip install buildozer cython==0.29.33
    
    - name: Build APK
      run: |
        cd game_project_extracted/game_project
        buildozer init
        sed -i 's/requirements = .*/requirements = python3,pygame/' buildozer.spec
        sed -i 's/source.include_exts = .*/source.include_exts = py,png,jpg,jpeg,ogg,mp3,wav,ttf,json,atlas/' buildozer.spec
        sed -i 's/#orientation = .*/orientation = landscape/' buildozer.spec
        sed -i 's/title = .*/title = MyGame/' buildozer.spec
        sed -i 's/package.name = .*/package.name = mygame/' buildozer.spec
        sed -i 's/package.domain = .*/package.domain = org.mygame/' buildozer.spec
        export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
        buildozer android debug
    
    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: game-apk
        path: game_project_extracted/game_project/bin/*.apk
