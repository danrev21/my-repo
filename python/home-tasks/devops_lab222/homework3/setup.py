from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot= snapshot.snapshot:main",
        ],
    },
    install_requires=[
        'psutil==5.5.1'
    ],
    version="0.1",
    author="Dzmitry Barouka1",
    author_email="dzmitry_barouka1@epam.com",
    description="Utility for system usage monitoring",
    license="MIT",
)
