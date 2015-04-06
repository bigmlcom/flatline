from setuptools import setup

setup(name='flatline',
      description='Python bridge for the flatline javascript interpreter',
      author='jao',
      url='http://github.com/bigmlcom/flatline',
      download_url='http://github.com/bigmlcom/flatline',
      author_email='jao@bigml.com',
      version='0.1',
      license='Apache',
      install_requires=['PyExecJS', 'nose', 'bigml'],
      packages=['flatline'],
      packages_data={'flatline':['flatline.js']},
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      scripts=[],
      use_2to3=True
)
