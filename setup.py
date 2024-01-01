# from distutils.core import setup
from setuptools import find_packages, setup
import os

setup(name='THD-Flow',
      version=open('VERSION').read().strip() if os.path.isfile('VERSION') else 'UNKNOWN',
      description='A modular CI CLI providing versioning, quality analysis, security analysis, packaging, building, '
                  'deployment and communication',
      author='Andrew Turner',
      author_email='andrew_m_turner@homedepot.com',
      url='https://www.homedepot.com',
      license='Apache',
      keywords='ci cd continuous integration deployment delivery flow jenkins concourse',
      packages=find_packages(exclude=['images', 'scripts', 'test-results', 'tests*']),
      install_requires = ["appdirs==1.4.3",
                          "argh==0.26.2",
                          "colorama==0.3.7",
                          "colorlog==2.10.0",
                          "cookies==2.2.1",
                          "docopt==0.6.2",
                          "gitdb==0.6.4",
                          "GitPython==2.0.2",
                          "mock==2.0.0",
                          "multi-key-dict==2.0.3",
                          "packaging==16.8",
                          "pathtools==0.1.2",
                          "pbr==1.10.0",
                          "py==1.10.0",
                          "PyDispatcher==2.0.5",
                          "pyparsing==2.2.0",
                          "pytest==7.4.4",
                          "pytest-mock==1.2",
                          "pytest-watch==4.1.0",
                          "python-jenkins==0.4.13",
                          "PyYAML>=4.2b1",
                          "requests>=2.20.0",
                          "requests-toolbelt==0.7.1",
                          "responses==0.5.1",
                          "six==1.10.0",
                          "smmap==0.9.0",
                          "splunk-handler==1.1.3",
                          "urllib3==1.26.5",
                          "watchdog==0.8.3",
                          ],
      data_files=['flow/settings.ini'],
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'flow=flow.aggregator:main',
          ],
        },
      )
