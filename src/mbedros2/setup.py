import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'mbedros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        (os.path.join('share', package_name, 'launch'), 
         glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Faizan Hossain',
    maintainer_email='mmfaizanhossain@users.noreply.github.com',
    description='Serial bridge from ROS 2 to the STM32 motor controller.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 'mbed_motor_ctrl = mbedros2.camfollow_mtr:main',
            # 'one_node = mbedros2.one_node:main',
            'sendcommandkey = mbedros2.sendcommandkey:main',
        ],
    },
)
