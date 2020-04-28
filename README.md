fsbl
====

Falkner-Skan boundary layer solvers in multiple programming languages.


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

To calculate the separating profile (`beta = -0.1988377350467045`), run the
program written for just this purpose:

    $ python3 separation.py

This program assumes that `h0 = 0.0` and uses a similar bisection search
algorithm to determine the correct value of `beta`.


## TODO list

- Code ported to several languages, including C, C++, Fortran, Java, Julia, ...

- Detailed documentation on the mathematics behind the Falkner-Skan profiles
  and the program's implementation of the shooting method using bisection
  search.

- Verification and validation and uncertainty quantification.

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
