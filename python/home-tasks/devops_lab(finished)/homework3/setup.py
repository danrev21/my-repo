from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = snapshot.snapshot:main",
        ],
    },
    install_requires=[
        'psutil==5.9.0'
    ],
    version="1.0",
    author="Danil Tyuev",
    author_email="Danil_Tyuev@epam.com",
    description="snapshot app",
    license="MIT")
