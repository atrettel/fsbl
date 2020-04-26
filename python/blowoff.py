#!/usr/bin/env python3

# Copyright (C) 2020 Andrew Trettel
# 
# FSBL is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
# 
# FSBL is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with
# FSBL.  If not, see <https://www.gnu.org/licenses/>.

import fsbl
import sys

DEFAULT_F0_1 = -0.80
DEFAULT_F0_2 = -0.85

BLOWOFF_ETA_MAX = 40.0
BLOWOFF_N = 65536
H0_TOL = 1.0e-12

def secant_method( beta, n, eta_max, f0_1, f0_2 ):
    assert( f0_1 > f0_2 )

    f0_array = [ 0.0 ] * fsbl.N_ITER_MAX
    h0_array = [ 0.0 ] * fsbl.N_ITER_MAX

    eta, f_1, g_1, h_1 = fsbl.bisection_search( beta, f0_1, n, eta_max,
        fsbl.H0_SEPARATION, fsbl.DEFAULT_H0_MAX )
    eta, f_2, g_2, h_2 = fsbl.bisection_search( beta, f0_2, n, eta_max,
        fsbl.H0_SEPARATION, fsbl.DEFAULT_H0_MAX )

    f0_array[0] = f_1[0]
    h0_array[0] = h_1[0]

    f0_array[1] = f_2[0]
    h0_array[1] = h_2[0]

    i_iter = 1
    while ( h0_array[i_iter]**2.0 > H0_TOL**2.0 ):
        i_iter += 1

        if ( i_iter == fsbl.N_ITER_MAX ):
            print( "Maximum number of iterations (N_ITER_MAX = {:d}).".format(
                fsbl.N_ITER_MAX
            ) )
            break

        f0_array[i_iter] = f0_array[i_iter-1] - h0_array[i_iter-1] * (
            f0_array[i_iter-1] - f0_array[i_iter-2]
        ) / (
            h0_array[i_iter-1] - h0_array[i_iter-2]
        )

        eta, f, g, h = fsbl.bisection_search( beta, f0_array[i_iter], n,
            eta_max, fsbl.H0_SEPARATION, h0_array[i_iter-1] )

        h0_array[i_iter] = h[i_iter]

    return eta, f, g, h

def main( argc, argv ):
    beta = fsbl.DEFAULT_BETA
    n = BLOWOFF_N
    eta_max = BLOWOFF_ETA_MAX
    f0_1 = DEFAULT_F0_1
    f0_2 = DEFAULT_F0_2

    if ( argc > 1 ):
        beta = float( argv[1] )

    if ( argc > 2 ):
        n = int( argv[2] )

    if ( argc > 3 ):
        eta_max = float( argv[3] )

    if ( argc > 4 ):
        f0_1 = float( argv[4] )

    if ( argc > 5 ):
        f0_2 = float( argv[5] )

    print( "beta    = {:f}".format( beta    ) )
    print( "n       = {:d}".format( n       ) )
    print( "eta_max = {:f}".format( eta_max ) )
    print( "f0_1    = {:f}".format( f0_1    ) )
    print( "f0_2    = {:f}".format( f0_2    ) )

    eta, f, g, h = secant_method( beta, n, eta_max, f0_1, f0_2 )

    print( "h0   = {:+20.16f}".format( h[0]  ) )
    print( "ginf = {:+20.16f}".format( g[-1] ) )

    print( "f0   = {:+20.16f}".format( f[0] ) )

    if ( h[0]**2.0 < H0_TOL**2.0 ):
        fsbl.save_profiles( eta, f, g, h, beta )
        exit(0)
    else:
        exit(1)

if __name__ == "__main__":
    main( len(sys.argv), sys.argv )
