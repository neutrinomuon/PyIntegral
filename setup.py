from numpy.distutils.core import Extension
from numpy.distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

ext1 = Extension(  name='pyintegralall.flib',
                   sources=['src/fortran/DataTypes.f90','src/fortran/LINinterpol.f90','src/fortran/GaussLegendreQuadrature.f90','src/fortran/IntegralALL.f90'],
                 )
    
setup( name='pyintegralall',
       version='0.0.9',
       ext_modules=[ ext1 ],
       extra_compile_args=['-O3'],
       description='Integrate arrays, functions numerically using different methods in Python. Original Fortran 2003+ legacy routines date back to 2003-2004. Read the LICENSE.txt file.',
       long_description=long_description, # Long description read from the the readme file
       long_description_content_type="text/markdown",
       author='Jean Gomes',
       author_email='antineutrinomuon@gmail.com',
       url='https://github.com/neutrinomuon/pyintegralall',
       install_requires=[ 'numpy','matplotlib' ],
       classifiers=[
           "Programming Language :: Python :: 3",
           "Programming Language :: Fortran",
           "Operating System :: OS Independent",
                   ],
       package_dir={"pyintegralall": "src/python"},
       packages=['pyintegralall'],
       data_files=[('', ['version.txt'])],
      )
    
