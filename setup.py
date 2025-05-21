from setuptools import setup

APP = ['nailcam.py']
OPTIONS = {
    # DO NOT use 'argv_emulation'
    'iconfile': 'icon.icns',
    'packages': ['cv2', 'mediapipe'],
    'includes': ['Foundation', 'AppKit'],
    'plist': {
        'CFBundleName': 'NailCam',
        'CFBundleDisplayName': 'NailCam',
        'CFBundleIdentifier': 'com.asifreddot.nailcam',
        'CFBundleIconFile': 'icon',
        'NSCameraUsageDescription': 'NailCam needs access to your camera to detect nail-biting gestures.',
    }
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
