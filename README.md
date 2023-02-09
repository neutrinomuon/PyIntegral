# IntegralALL
##  A fortran legacy package to easy integrate numerically
email: antineutrinomuon@gmail.com, jean@astro.up.pt

© Copyright ®

J.G. - Jean Gomes

<link rel="stylesheet" href="devicon.min.css">

<!--  for devicon plain version -->
<i class="devicon-devicon-plain"></i>

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

.devicon-devicon-plain {
  max-width: 2em;
}

/* if you want to change the original color */
.devicon-devicon-plain path {
  fill: #4691f6;
}
