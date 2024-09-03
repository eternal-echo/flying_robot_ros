from setuptools import find_packages, setup

package_name = 'test_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='flying',
    maintainer_email='yu.yuan@sjtu.edu.cn',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'flying_hardware_node = test_py.flying_hardware_node:main',
            "IMU_subscriber = test_py.test_subscribe_node:main",
        ],
    },
)
