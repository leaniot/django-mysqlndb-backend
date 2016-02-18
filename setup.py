try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


setup(
    name='django-mysqlndb-backend',
    version='1.0.11',
    author_email='programmers@theatlantic.com',
    packages=['mysqlndb'],
    url='https://github.com/theatlantic/django-mysqlndb-backend',
    description='Provides a django database backend that works with MySQL Cluster\'s NDB storage engine.',
    install_requires=[
        "Django >= 1.4",
        "MySQL-python >= 1.2.2",
        'django-transaction-hooks >= 0.2',
    ],
)
