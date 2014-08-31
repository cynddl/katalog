from setuptools import setup, find_packages

setup(
        name='katalog',
        version='0.1',
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
                    'Click',
                    'ZODB'
                ],
        entry_points='''
            [console_scripts]
            katalog=katalog.cli:cli
        ''',
)
