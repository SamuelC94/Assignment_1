from distutils.core import setup

setup(name='Interpreter',
      version='1.0',
      description='Assignment 1 - Team Guido FTW!',
      author='Wesley, James, Sam',
      author_email='wew248@arastudent.ac.nz',
      url='https://github.com/BustahBoi/BCPR301---Assignment-1',
      packages=['pickler', 'prompt', 'tests'],
      package_dir={'tests': 'test_pickle'}
     )

