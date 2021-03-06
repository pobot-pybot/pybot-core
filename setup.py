# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='pybot-core',
      setup_requires=['setuptools_scm'],
      use_scm_version=True,
      description='PyBot packages collection common stuff',
      license='LGPL',
      author='Eric Pascual',
      author_email='eric@pobot.org',
      url='http://www.pobot.org',
      download_url='https://github.com/Pobot/PyBot',
      packages=find_packages("src"),
      package_dir={'': 'src'}
      )
