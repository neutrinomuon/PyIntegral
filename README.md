# IntegralALL
##  A fortran legacy package to easy integrate numerically
email: antineutrinomuon@gmail.com, jean@astro.up.pt

© Copyright ®

J.G. - Jean Gomes

RESUME : Integrate arrays, functions numerically using different methods and
spline1 interpolation scheme. Original routines date back to 2003-2004. Read
the LICENSE.txt file.

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
├── src
│   ├── python
│   └── fortran
├── build
│   ├── lib.linux-x86_64-3.9
│   ├── src.linux-x86_64-3.9
│   ├── bdist.linux-x86_64
│   └── temp.linux-x86_64-3.9
└── .git
    ├── branches
    ├── logs
    ├── info
    ├── index
    ├── description
    ├── HEAD
    ├── objects
    ├── packed-refs
    ├── hooks
    ├── COMMIT_EDITMSG
    ├── refs
    └── config

17 directories, 15 files
</code>
</pre>

<mark>PyIntegralALL.py</mark> is a python wrapper to the library in fortran
called <mark>pyintegralall.flib</mark>. The fortran directory can be compiled
separately for each individual subroutine.

