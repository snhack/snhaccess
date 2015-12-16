import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'wtforms==2.0.2',
    'webhelpers2==2.0',
    'paginate==0.5',
    'paginate_sqlalchemy==0.2.0'
    ]

setup(name='snhack_access',
      version='0.0',
      description='snhack_access',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='snhack_access',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = snhack_access:main
      [console_scripts]
      initialize_snhack_access_db = snhack_access.scripts.initializedb:main
      """,
      )
