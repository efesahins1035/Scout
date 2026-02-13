from setuptools import setup, find_packages

setup(
    name="scout",
    version="1.0.0",
    description="Modüler Ağ Güvenlik Aracı",
    author="Efe Şahin",
    packages=find_packages(),
    install_requires=[
        "rich",
        "scapy",
        "requests"
    ],
    entry_points={
        'console_scripts': [
            'scout=scout_v2.main:main',
        ],
    },
)
