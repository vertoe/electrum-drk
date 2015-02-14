#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')
util = imp.load_source('util', 'lib/util.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: electrum_drk requires Python version >= 2.7.0...")



if (len(sys.argv) > 1) and (sys.argv[1] == "install"): 
    # or (platform.system() != 'Windows' and platform.system() != 'Darwin'):
    print "Including all files"
    data_files = []
    usr_share = util.usr_share_dir()
    if not os.access(usr_share, os.W_OK):
        try:
            os.mkdir(usr_share)
        except:
            sys.exit("Error: cannot write to %s.\nIf you do not have root permissions, you may install electrum_drk in a virtualenv.\nAlso, please note that you can run electrum_drk without installing it on your system."%usr_share)

    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum_drk.desktop']),
        (os.path.join(usr_share, 'app-install', 'icons/'), ['icons/electrum.png'])
    ]
    if not os.path.exists('locale'):
        os.mkdir('locale')
    for lang in os.listdir('locale'):
        if os.path.exists('locale/%s/LC_MESSAGES/electrum_drk.mo' % lang):
            data_files.append((os.path.join(usr_share, 'locale/%s/LC_MESSAGES' % lang), ['locale/%s/LC_MESSAGES/electrum_drk.mo' % lang]))


    appdata_dir = os.path.join(usr_share, "electrum_drk")
    data_files += [
        (appdata_dir, ["data/README"]),
        (os.path.join(appdata_dir, "cleanlook"), [
            "data/cleanlook/name.cfg",
            "data/cleanlook/style.css"
        ]),
        (os.path.join(appdata_dir, "sahara"), [
            "data/sahara/name.cfg",
            "data/sahara/style.css"
        ]),
        (os.path.join(appdata_dir, "dark"), [
            "data/dark/name.cfg",
            "data/dark/style.css"
        ])
    ]

    for lang in os.listdir('data/wordlist'):
        data_files.append((os.path.join(appdata_dir, 'wordlist'), ['data/wordlist/%s' % lang]))
else:
    data_files = []

setup(
    name="Electrum_DRK",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'pyasn1-modules',
        'pyasn1',
        'qrcode',
        'SocksiPy-branch',
        'protobuf',
        'tlslite'
    ],
    package_dir={
        'electrum_drk': 'lib',
        'electrum_drk_gui': 'gui',
        'electrum_drk_plugins': 'plugins',
    },
    scripts=['electrum_drk'],
    data_files=data_files,
    py_modules=[
        'electrum_drk.account',
        'electrum_drk.bitcoin',
        'electrum_drk.blockchain',
        'electrum_drk.bmp',
        'electrum_drk.commands',
        'electrum_drk.daemon',
        'electrum_drk.i18n',
        'electrum_drk.interface',
        'electrum_drk.mnemonic',
        'electrum_drk.msqr',
        'electrum_drk.network',
        'electrum_drk.network_proxy',
        'electrum_drk.old_mnemonic',
        'electrum_drk.paymentrequest',
        'electrum_drk.paymentrequest_pb2',
        'electrum_drk.plugins',
        'electrum_drk.qrscanner',
        'electrum_drk.simple_config',
        'electrum_drk.synchronizer',
        'electrum_drk.transaction',
        'electrum_drk.util',
        'electrum_drk.verifier',
        'electrum_drk.version',
        'electrum_drk.wallet',
        'electrum_drk.x509',
        'electrum_drk_gui.gtk',
        'electrum_drk_gui.qt.__init__',
        'electrum_drk_gui.qt.amountedit',
        'electrum_drk_gui.qt.console',
        'electrum_drk_gui.qt.history_widget',
        'electrum_drk_gui.qt.icons_rc',
        'electrum_drk_gui.qt.installwizard',
        'electrum_drk_gui.qt.lite_window',
        'electrum_drk_gui.qt.main_window',
        'electrum_drk_gui.qt.network_dialog',
        'electrum_drk_gui.qt.password_dialog',
        'electrum_drk_gui.qt.paytoedit',
        'electrum_drk_gui.qt.qrcodewidget',
        'electrum_drk_gui.qt.qrtextedit',
        'electrum_drk_gui.qt.qrwindow',
        'electrum_drk_gui.qt.receiving_widget',
        'electrum_drk_gui.qt.seed_dialog',
        'electrum_drk_gui.qt.transaction_dialog',
        'electrum_drk_gui.qt.util',
        'electrum_drk_gui.qt.version_getter',
        'electrum_drk_gui.stdio',
        'electrum_drk_gui.text',
        'electrum_drk_plugins.btchipwallet',
        'electrum_drk_plugins.coinbase_buyback',
        'electrum_drk_plugins.cosigner_pool',
        'electrum_drk_plugins.exchange_rate',
        'electrum_drk_plugins.greenaddress_instant',
        'electrum_drk_plugins.labels',
        'electrum_drk_plugins.trezor',
        'electrum_drk_plugins.virtualkeyboard',
        'electrum_drk_plugins.plot',

    ],
    description="Lightweight Darkcoin Wallet",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU GPLv3",
    url="https://electrum.org",
    long_description="""Lightweight Darkcoin Wallet"""
)
