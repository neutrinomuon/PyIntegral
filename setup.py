''' This setup.py file is for installing the script of pyintegral. \
It conforms with PEP 8 guide for python'''
# --------------------------------------------------------------------
# Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
from numpy.distutils.core import Extension
from numpy.distutils.core import setup

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

with open("version.txt","r",encoding="utf-8") as vh:
    version_description = vh.read()

#ext1 = Extension(  name='PyIntegral.flib',
#                   sources=['src/fortran/DataTypes.f90',
#                            'src/fortran/LINinterpol.f90',
#                            'src/fortran/GaussLegendreQuadrature.f90',
#                            'src/fortran/IntegralALL.f90'],
#                  )

# In agreement with PEP 8 definitions
ext2 = Extension(  name='pyintegral.flib',
                   sources=['src/fortran/DataTypes.f90',
                            'src/fortran/LINinterpol.f90',
                            'src/fortran/GaussLegendreQuadrature.f90',
                            'src/fortran/IntegralALL.f90'],
                 )

setup( name='pyintegral',
       version=version_description,
       ext_modules=[ ext2 ],
       extra_compile_args=['-O3'],
       description='Integrate arrays, functions numerically using'
                    'different methods in Python. Original Fortran'
                    '2003+ legacy routines date back to 2003-2004.'
                    'Read the LICENSE.txt file. In agreement with '
                    'PEP 8 standard guide',
        long_description=long_description, # Long description read from the the readme file
        long_description_content_type="text/markdown",
        author='Jean Gomes',
        author_email='antineutrinomuon@gmail.com',
        url='https://github.com/neutrinomuon/PyIntegral',
        install_requires=[ 'numpy','matplotlib' ],
        classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Fortran",
            "Operating System :: OS Independent",
                    ],
        package_dir={"pyintegral": "src/python"},#, "PyIntegral": "src/python"},
        packages=['pyintegral'],#,'PyIntegral'],
        data_files=[('', ['version.txt','LICENSE.txt'])],
       )
