# IntegralALL
##  A fortran legacy package to easy integrate numerically
email: antineutrinomuon@gmail.com, jean@astro.up.pt

© Copyright ®

J.G. - Jean Gomes

<!--  for devicon plain version -->
<svg id="Devicon" class='devicon-devicon-plain' xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128"><path id="plain" fill="#60be86" d="M64,7.83H4.77L14.95,95.13l49,25,.06,0,49.07-25L123.23,7.83Zm42.77,54.86c0,.88,0,1.67-.77,2L73.25,80.44l-2.42,1.13-.27-3.15V72.23l.24-1.57,1.09-.47L95.07,59.81l-21.54-9.6L64.35,68.34,58.9,78.87l-1.22,2.27-2.05-.9L22,64.71a2.42,2.42,0,0,1-1.45-2V56.91a2.39,2.39,0,0,1,1.42-2l34-15.73,3.21-1.44v9.66l.24,1.34-1.56.7L34.45,59.79,56.3,69.42l8.05-16,6.21-12.65,1.13-2.28,1.81.91L106,54.89c.73.35.76,1.14.76,2Z"/></svg>

RESUME : Integrate arrays, functions numerically using different
methods. Original Fortran 2003+ routines date back to 2003-2004. Read the
LICENSE.txt file.

The methods are given by Int_Type and may be summarized bellow:


<table>
<tr><td>Int_Type</td><td>Type</td><td>Description</td></tr>
<tr><td>0<td>R</td><td>Right rectangle Integral  </td></tr>
<tr><td>1<td>L</td><td>Left rectangle Integral   </td></tr>
<tr><td>2<td>T</td><td>Trapezoidal rule          </td></tr>
<tr><td>3<td>S</td><td>Simple Integral           </td></tr>
<tr><td>4<td>M</td><td>Median rectangle Integral </td></tr>
<tr><td>5<td>I</td><td>Simpsonregel's rule       </td></tr>
<tr><td>6<td>G</td><td>Gauss-Legendre Quadrature </td></tr>
</table>

The main structure of the directories and files are:

<pre>
<code>
IntegralALL
├── dist
│   └── pyintegralall-0.0.1.tar.gz
├── README.md
├── pyintegralall.egg-info
│   ├── PKG-INFO
│   ├── dependency_links.txt
│   ├── SOURCES.txt
│   ├── top_level.txt
│   └── requires.txt
├── LICENSE.txt
├── setup.py
├── tutorials
│   ├── Example1 - IntegralALL.ipynb
│   └── .ipynb_checkpoints
│       └── Example1 - IntegralALL-checkpoint.ipynb
├── src
│   ├── python
│   │   ├── __init__.py
│   │   └── PyIntegralALL.py
│   └── fortran
│       ├── IntegralALL.compile
│       ├── IntegralALL.f90
│       ├── IntegralALL.cpython-39-x86_64-linux-gnu.so
│       ├── DataTypes.f90
│       ├── GaussLegendreQuadrature.cpython-39-x86_64-linux-gnu.so
│       ├── LINinterpol.compile
│       ├── GaussLegendreQuadrature.f90
│       ├── LINinterpol.cpython-39-x86_64-linux-gnu.so
│       ├── LINinterpol.f90
│       └── GaussLegendreQuadrature.compile
├── version.txt
└── build
    ├── lib.linux-x86_64-3.9
    │   └── pyintegralall
    ├── src.linux-x86_64-3.9
    │   ├── pyintegralall
    │   ├── build
    │   └── numpy
    ├── bdist.linux-x86_64
    └── temp.linux-x86_64-3.9
        ├── pyintegralall
        ├── __pycache__
        ├── ccompiler_opt_cache_ext.py
        ├── src
        ├── .libs
        └── build

21 directories, 25 files
</code>
</pre>

<mark>PyIntegralALL.py</mark> is a python wrapper to the library in fortran
called <mark>pyintegralall.flib</mark>. The fortran directory can be compiled
separately for each individual subroutine.
