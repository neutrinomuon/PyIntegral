# IntegralALL
##  A fortran legacy package to easy integrate numerically

RESUME : Integrate using different methods and spline1 interpolation  scheme. Original routine dates back to 2003-2004.

The methods are given by Int_Type and may be summarized bellow:


<table>
<tr><td>Int_Type</td><td>Description</td></tr>
<tr><td>0<td>R -> Right rectangle Integral  </td></tr>
<tr><td>1<td>L -> Left rectangle Integral   </td></tr>
<tr><td>2<td>T -> Trapezoidal rule          </td></tr>
<tr><td>3<td>S -> Simple Integral           </td></tr>
<tr><td>4<td>M -> Median rectangle Integral </td></tr>
<tr><td>5<td>I -> Simpsonregel's rule       </td></tr>
<tr><td>6<td>G -> Gauss-Legendre Quadrature </td></tr>
</table>

The main structure of the directories and files are:

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
