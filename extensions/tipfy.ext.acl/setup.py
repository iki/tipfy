"""
tipfy.ext.acl
=============

This extension provides an Access Control implementation for tipfy, the
almighty little framework for Google App Engine.

Links
-----
* `Tipfy <http://www.tipfy.org/>`_
* `API Documentation <http://www.tipfy.org/docs/>`_
* `Wiki <http://www.tipfy.org/wiki/>`_
* `Discussion Group <http://groups.google.com/group/tipfy>`_
* `Issue Tracker <http://code.google.com/p/tipfy/issues/list>`_
* `Source Code Repository <http://code.google.com/p/tipfy/>`_
"""
from setuptools import setup

setup(
    name = 'tipfy.ext.acl',
    version = '0.5.5',
    license = 'BSD',
    url = 'http://www.tipfy.org/',
    description = 'Access Control extension for tipfy',
    long_description = __doc__,
    author = 'Rodrigo Moraes',
    author_email = 'rodrigo.moraes@gmail.com',
    zip_safe = False,
    platforms='any',
    packages = [
        'tipfy',
        'tipfy.ext',
    ],
    namespace_packages = [
        'tipfy',
        'tipfy.ext',
    ],
    include_package_data = True,
    install_requires = [
        'tipfy',
        'tipfy.ext.db',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
