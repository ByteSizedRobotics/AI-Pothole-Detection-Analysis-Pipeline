
## Local Classification Model
#### 1) Deploy flask local_app.py on local web server without Docker 
(need to install dependencies 1st.. see Setup Virtual Env Steps)
Works for windows + linux
- cd to deployment\local-app
- python local_app.py
- go to the specified web address (ex: http://127.0.0.1:5000/)

#### 2) Running python script locally (not on web server but just as python script)
- cd to deployment\testing
- python local-model-testing.py

## Docker Classification Model
Only the live inference with video is done in the container due to permission/access complexities for providing access to host files/folder within the container. For now, a bind mount is used as the location to share access between the host and the container for the detected/saved images. NOTE: you need to login to Docker 1st (i.e Docker login)
#### 1) Building and Pushing Docker Container (Docker desktop might need to be running)
- cd to pothole-detection/deployment/raspi
- docker buildx build --platform linux/arm64 -t [dockerUSERNAME]/pothole-classifier-app-arm64 .
- docker push [dockerUSERNAME]/pothole-classifier-app-arm64:latest

#### 2) Deploy app.py on Docker Container on Raspberry Pi 
- docker pull --platform linux/arm64 [dockerUSERNAME]/pothole-classifier-app-arm64:latest
- docker run -d --name flask-pothole --device=/dev/video0 -p 5000:5000 -v [PATH ON HOST TO SAVE IMAGES]:/app/saved_images [dockerUSERNAME]/pothole-classifier-app-arm64

### Important NOTES for Raspberry Pi: 
When running the app on the raspberry pi, it might take several attempts for video camera to startup
Gives the error [ WARN:0@56.032] global cap_v4l.cpp:1048 tryIoctl VIDEOIO(V4L2:/dev/video0): select() timeout.
JUST KEEP TRYING... (keep clicking 'start live inference' after it fails)
Tried playing with parameters based on this, didn't seem to help
https://forums.raspberrypi.com/viewtopic.php?t=35689

need to connect the usb webcam to the 3.0 usbc port and also works with the ___ Ubuntu account

## Setup Virtual Env and install dependencies
#### WINDOWS
1) python -m venv venv
2) Set-ExecutionPolicy Unrestricted -Scope Process
3) .\venv\Scripts\Activate
4) cd pothole-detection\deployment\local-app
5) pip install -r requirements.txt

#### LINUX
1) python3 -m venv venv
2) . venv/bin/activate
3) cd pothole-detection\deployment\local-app
4) pip install -r requirements.txt

NOTE: can deactivate whenever with: deactive

## Camera IMX-219 setup with Raspi 5
### Installing libcamera
Tried the following based on https://forums.raspberrypi.com/viewtopic.php?t=339606, still not working

git clone https://git.libcamera.org/libcamera/libcamera.git
git clone https://github.com/raspberrypi/libcamera-apps.git

cd libcamera
meson setup build
ninja -C build
sudo ninja -C build install

cd ../../libcamera-apps
meson setup build
ninja -C build
sudo ninja -C build install
