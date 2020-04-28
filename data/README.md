Data for validation and benchmarking
====================================


## Benchmarks

These benchmarks are previous high-quality calculations of the Falkner-Skan or
Blasius boundary layers.  Benchmarking is not strictly speaking the same thing
as either verification or validation, since it neither establishes the the
implementation's correctness nor compares the program's results to the real
world.  Nonetheless, benchmarking does compare the program's results to some
previous standard, and that provides some information about how well the
program meets expectations.

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

    - Notes

        - This benchmark uses different boundary conditions than the code, so
          the results must be re-scaled for a proper comparison.

            - `eta = eta_Emmons * sqrt(2.0)`

            - `f = f_Emmons / sqrt(2.0)`

            - `f' = g = f'_Emmons / 2.0`

            - `f'' = h = 0.5 * f''_Emmons / sqrt(2.0)`

    - CSV files

        - `EmmonsHW_1954_table2.csv`

            - This table lists `h0` as a function of `f0` for a constant `beta
              = 0.0`.

- Inglis, J. A. 1962.  "A digital computer solution of the Falkner and Skan
  boundary layer equation."  Naval Postgraduate School master's thesis.

    - Falkner-Skan boundary layers without suction and blowing.

    - <https://apps.dtic.mil/sti/citations/AD0481404>

    - CSV files

        - `InglisJA_1962_beta_h0.csv`

            - This table lists `h0` as a function of `beta` for a
              constant `f0 = 0.0`.


## Experimental studies

- To be compiled.


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
