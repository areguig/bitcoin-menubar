from setuptools import setup

APP = ['bitcoin_price.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
        'CFBundleName': 'Bitcoin Price',
        'CFBundleDisplayName': 'Bitcoin Price',
        'CFBundleGetInfoString': "Bitcoin price in your menu bar",
        'CFBundleIdentifier': "com.github.bitcoin-price-menubar",
        'CFBundleVersion': "1.0.0",
        'CFBundleShortVersionString': "1.0.0",
        'NSHumanReadableCopyright': 'MIT License'
    },
    'packages': ['rumps', 'requests'],
}

setup(
    name='BitcoinPrice',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=['rumps==0.4.0', 'requests==2.31.0'],
    version='1.0.0',
    author='Your Name',
    description='Bitcoin price menubar app for macOS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/bitcoin-price-menubar',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3',
    ],
)
