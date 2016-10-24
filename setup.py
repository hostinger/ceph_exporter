# -*- mode: python; coding: utf-8 -*-

# Copyright © 2016 by Jeffrey C. Ollie
#
# This file is part of ceph_exporter.
#
# ceph_exporter is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# ceph_exporter is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ceph_exporter.  If not, see
# <http://www.gnu.org/licenses/>.

from setuptools import setup

setup(name = 'ceph_exporter',
      version = '0.1',
      author = 'Jeffrey C. Ollie',
      author_email = 'jeff@ocjtech.us',
      license = 'GPLv3',
      url = 'https://github.com/jcollie/ceph_exporter',
      packages = ['ceph_exporter',
                  'ceph_exporter.ceph',
                  'ceph_exporter.ceph.commands',
                  'ceph_exporter.ceph.metrics'],
      data_files = [('etc', ['ceph_exporter.service'])],
      entry_points = {
          'console_scripts': ['ceph_exporter=ceph_exporter.main:main']
      },
      install_requires = ['Twisted[tls]',
                          'service-identity',
                          'arrow'],
      classifiers = ['Development Status :: 4 - Beta'])
