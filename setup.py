from setuptools import setup

APP = ['nailcam.py']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',
    'packages': ['cv2', 'mediapipe'],
    'plist': {
        'NSCameraUsageDescription': 'NailCam needs access to your camera to detect nail-biting gestures.',
        'CFBundleIconFile': 'icon',
        'CFBundleIdentifier': 'com.asifreddot.nailcam'
    }
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
