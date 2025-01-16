from setuptools import setup

setup(name='bloodhound',
      version='1.8.0',
      description='Python based ingestor for BloodHound',
      author='Dirk-jan Mollema, Edwin van Vliet, Matthijs Gielen',
      author_email='dirkjan@dirkjanm.io, edwin.vanvliet@fox-it.com, matthijs.gielen@fox-it.com',
      maintainer='Dirk-jan Mollema',
      maintainer_email='dirkjan@dirkjanm.io',
      url='https://github.com/dirkjanm/bloodhound.py',
      packages=['bloodhound',
                'bloodhound.ad',
                'bloodhound.lib',
                'bloodhound.enumeration'],
      license='MIT',
      install_requires=['dnspython', 'impacket @ git+https://github.com/dadevel/impacket@latest', 'ldap3 @ git+https://github.com/dadevel/ldap3@latest', 'pyasn1>=0.4', 'pycryptodome'],
      classifiers=[
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
      ],
      entry_points= {
        'console_scripts': ['bloodhound-python=bloodhound:main']
      }
      )
