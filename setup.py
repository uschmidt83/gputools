
from setuptools import setup, find_packages

setup(name='gputools',
    version='0.1.3',
    description='OpenCL accelerated volume processing',
    url='',
    author='Martin Weigert',
    author_email='mweigert@mpi-cbg.de',
    license='MIT',
    packages=find_packages(),

    install_requires=["numpy>=1.11.0",
                      "pyopencl>=2016.1",
                      "configparser",
                      "reikna>=0.6.7"],

    package_data={"gputools":
                  ['core/kernels/*.cl',
                   'convolve/kernels/*.cl',
                   'denoise/kernels/*.cl',
                   'deconv/kernels/*.cl',
                   'noise/kernels/*.cl',
                   'transforms/kernels/*.cl',
                  ],
    },

    entry_points = {}
)
