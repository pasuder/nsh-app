#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    print 'No setuptools installed, use distutils'
    from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
        name='nsh_app',
        packages=[
            'nsh_app',
            'nsh_app.function',
            'nsh_app.network',
            'nsh_app.sh',
            'nsh_app.tools',
            'nsh_app.trainer',
            'nsh_app.tests'
        ],
        package_dir={
            'nsh_app': 'src/nsh_app',
            'nsh_app.function': 'src/nsh_app/function',
            'nsh_app.network': 'src/nsh_app/network',
            'nsh_app.sh': 'src/nsh_app/sh',
            'nsh_app.tools': 'src/nsh_app/tools',
            'nsh_app.trainer': 'src/nsh_app/trainer',
            'nsh_app.tests': 'src/nsh_app/tests'

        },
        package_data={'': [
            'src/nsh_app/nsh_app.ini'
        ]},
        data_files=[
            ('', [
                'src/nsh_app/nsh_app.ini'
            ]),
        ],
        test_suite="nsh_app.tests",
        include_package_data=True,
        install_requires=required,
        version='1.0',
        description='Neural network app',
        author=u'Paweł Suder',
        author_email='pawel@suder.info',
        url='http://github.com/SuderPawel/nsh-app',
        download_url='http://github.com/SuderPawel/nsh-app',
        keywords=[
            'skeleton'
        ],
        classifiers=[
            'Programming Language :: Python',
            'Development Status :: 4 - Beta',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
        long_description='''\
'''
)
