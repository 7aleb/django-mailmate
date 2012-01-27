from setuptools import setup, find_packages
# Execute emailtools/version.py to add __version__ to setup.py namespace.
# This way, we avoid the django imports that are triggered by importing
# any members of the emailtools module.
execfile('emailtools/version.py')

setup(
    name='Email Tools',
    version='.'.join(map(str, __version__)),
    author='Chris McKenzie',
    author_email='chrismc@hzdg.com',
    packages=find_packages(),
    include_package_data=False,
    description='Django email tools.',
    license='LICENSE.txt',
    url='http://gitorious.hzdesign.com/django-emailtools/django-emailtools',
    long_description=open('README').read(),
    zip_safe = False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)