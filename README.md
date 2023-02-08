# IntegralALL
##  A fortran legacy package to easy integrate numerically

RESUME : Integrate using different methods and spline1 interpolation  scheme. Original routine dates back to 2003-2004.

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
src
├── python
│   ├── __init__.py
│   └── PyIntegralALL.py
└── fortran
    ├── IntegralALL.compile
    ├── IntegralALL.f90
    ├── IntegralALL.cpython-39-x86_64-linux-gnu.so
    ├── DataTypes.f90
    ├── GaussLegendreQuadrature.cpython-39-x86_64-linux-gnu.so
    ├── GaussLegendreQuadrature.f90
    ├── LINinterpol.f90
    └── GaussLegendreQuadrature.compile
</code>
</pre>

PyIntegralALL.py is a python wrapper to the library in fortran. 
