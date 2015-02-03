from setuptools import setup


setup(name='dotmicApi',
      version='0.1',
      description='python wrapper for Dotmic Api ( A product search engine. )',
      url='https://github.com/ashishsurve21/dotmicApi',
      author='pacifier',
      author_email='ashish.surve21@gmail.com',
      license='MIT',
      packages=['dotmic'],
      install_requires=['json', 'urllib3'],
      zip_safe=False
      )
