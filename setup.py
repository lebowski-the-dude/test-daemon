from setuptools import setup
setup(
    name = 'my-daemon',
    version = '0.0.0',
    # packages = ['main'],
    entry_points = {
        'console_scripts': [
            'my-daemon = main.__main__:main'
        ]
})
