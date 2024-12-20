"""
Setup script for building macOS application using py2app
"""
from setuptools import setup

APP = ['bitcoin_price.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'plist': {
        'LSUIElement': True,
        'CFBundleName': 'Bitcoin Price',
        'CFBundleDisplayName': 'Bitcoin Price',
        'CFBundleIdentifier': 'com.areguig.bitcoin-price',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
    },
    'packages': ['rumps', 'requests'],
    'includes': ['WebKit'],
    'frameworks': [],
    'semi_standalone': False,
    'site_packages': True,
}

setup(
    app=APP,
    name="Bitcoin Price",
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=[
        'rumps',
        'requests',
        'pyobjc-framework-Cocoa',
    ],
)
