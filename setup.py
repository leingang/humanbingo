#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'jinja2>=2.9.6',
    'pyyaml>=3.12',  # more stable, old
    'ruamel.yaml>=0.15.23',  # newer, supports !!omap
    'weasyprint>=0.39',
]

setup_requirements = [
    # TODO(leingang): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='humanbingo',
    version='3.0.1',
    description='Create cards for the "Human Bingo" icebreaker game, with customizable properties and templating',  # noqa
    long_description=readme + '\n\n' + history,
    author="Matthew Leingang",
    author_email='mleingang@gmail.com',
    url='https://github.com/leingang/humanbingo',
    packages=find_packages(include=['humanbingo']),
    entry_points={
        'console_scripts': [
            'humanbingo=humanbingo.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='humanbingo',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
