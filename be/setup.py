import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='be',
    version='0.0.1a1',
    packages=find_packages(),
    include_package_data=True,
    license='be License',
    description='An About Africa Tours and Travel CMS',
    long_description=README,
    url='https://github.com/kalume-wa-kitsao/abound-africa-tours-and-travel',
    author='Kalume Kitsao',
    author_email='kalumewakitsao@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIKAKI License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'dj-database-url',
        'Django>=3.2.4',
        'ipython',
        'djangorestframework',
        'django-extensions',
        'django-filter',
        'psycopg2-binary',

        # celery
        'Celery',
        # celery results
        'django-celery-results',

        # gunicorn
        'gunicorn>=20.1.0'
    ],
    python_requires='>=3.7',
)
