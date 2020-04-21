fsbl
====

Falkner-Skan boundary layer solvers in multiple programming languages.

I want to use this project to write the same program in multiple languages.
The point is so that I can evaluate how the different languages represent the
program, especially in regards to how they handle different numerical issues
like arrays and floating point numbers.


## Usage

The Python version is the prototype (reference implementation) for the other
versions of the program.

    $ python3 fsbl.py [beta] [f0] [n] [eta_max] [h0_min] [h0_max]

All command line arguments are OPTIONAL.  The default values are

- `beta = 0.0` (Falkner-Skan pressure gradient parameter)

- `f0 = 0.0` (boundary condition on `f`)

- `n = 16384` (number of grid points)

- `eta_max = 10.0` (maximum coordinate value)

- `h0_min = 0.0` (minimum `h0` value for bisection search)

- `h0_max = 0.0` (maximum `h0` value for bisection search)

When `h0_min == h0_max`, the program uses an algorithm to find the bisection
search interval.  This algorithm works well for `-0.198837 < beta < +1.25`.
Outside of this range all command line arguments must be specified to get a
meaningful solution.  For example, for the case of `beta = 2.0`, the following
parameters work:

    $ python3 fsbl.py 2.0 0.0 16384 10.0 1.67 1.69

Note that the program has difficulty calculating the profile as it approaches
separation at `beta = -0.19884`.  It can get rather close (`beta = -0.198837`)
but not all the way there as it is written right now.  It should be possible to
correct this issue but I at least wanted to note it for the time being.


## TODO list

- Code ported to several languages, including C, C++, Fortran, Java, Julia, ...

- Detailed documentation on the mathematics behind the Falkner-Skan profiles.

- Verification and validation and uncertainty quantification.


## Tabulated verification and validation sources

- Hartree, D. R. 1937.  "On an Equation Occurring in Falkner and Skan's
  Approximate Treatment of the Equations of the Boundary Layer".  Mathematical
  Proceedings of the Cambridge Philosophical Society 33 (2), pp. 223-239.

    - Falkner-Skan boundary layers without suction and blowing.

    - <https://doi.org/10.1017/S0305004100019575>

- Howarth, L. 1938.  "On the solution of the laminar boundary layer equations".
  Proceedings of the Royal Society A: Mathematical, Physical and Engineering
  Sciences 164, pp. 547-579.

    - Blasius boundary layer without suction or blowing.

    - <https://doi.org/10.1098/rspa.1938.0037>

- Emmons, H. W. and Leigh, D. C. 1954.  "Tabulation of the Blasius Function
  with Blowing and Suction".  Aeronautical Research Council Current Paper 157.
  ARC-CP-157.

    - Blasius boundary layers with suction and blowing.

- Inglis, J. A. 1962.  "A digital computer solution of the Falkner and Skan
  boundary layer equation."  Naval Postgraduate School master's thesis.

    - Falkner-Skan boundary layers without suction and blowing.

    - <https://apps.dtic.mil/sti/citations/AD0481404>

-------------------------------------------------------------------------------

Copyright © 2020 Andrew Trettel

FSBL is free software: you can redistribute it and/or modify it under the terms
of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.

FSBL is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
FSBL.  If not, see <https://www.gnu.org/licenses/>.
