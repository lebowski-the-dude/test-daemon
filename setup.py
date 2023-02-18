from setuptools import setup
setup(
    name = 'my-daemon',
    version = '0.0.0',
    packages = ['daemon'],
    entry_points = {
        'console_scripts': [
            'my-daemon = daemon.daemon:main'
        ]
})
