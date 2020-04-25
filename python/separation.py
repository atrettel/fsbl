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

DEFAULT_BETA_MIN = -0.20
DEFAULT_BETA_MAX = -0.19

H0 = 0.0

def bisection_search( f0, n, eta_max, beta_min, beta_max ):
    eta = fsbl.create_similarity_coordinate( n, eta_max )

    beta_l = beta_min
    beta_r = beta_max

    assert( beta_r > beta_l )

    print( "beta_l   = {:f}".format( beta_l ) )
    print( "beta_r   = {:f}".format( beta_r ) )

    f_l, g_l, h_l = fsbl.solve_rk4( f0, H0, beta_l, eta )
    sign_l = ( g_l[-1] > fsbl.GINF )

    f_r, g_r, h_r = fsbl.solve_rk4( f0, H0, beta_r, eta )
    sign_r = ( g_r[-1] > fsbl.GINF )

    assert( sign_l != sign_r )

    n_iter = 0
    while ( n_iter < fsbl.N_ITER_MAX ):
        beta_c = 0.5 * ( beta_l + beta_r )
        f_c, g_c, h_c = fsbl.solve_rk4( f0, H0, beta_c, eta )
        sign_c = ( g_c[-1] > fsbl.GINF )

        if ( ( beta_r - beta_l ) <= 0.0 ):
            print( "Interval has zero length." )
            break
        elif ( ( g_c[-1] - fsbl.GINF )**2.0 < fsbl.GINF_TOL**2.0 ):
            print( "Solution within tolerance (GINF_TOL = {:e}).".format(
                fsbl.GINF_TOL
            ) )
            break

        if ( sign_c == sign_l ):
            beta_l = beta_c
            f_l = f_c
            g_l = g_c
            h_l = h_c
        else:
            beta_r = beta_c
            f_r = f_c
            g_r = g_c
            h_r = h_c

        n_iter += 1

    if ( n_iter == fsbl.N_ITER_MAX ):
        print( "Maximum number of iterations (N_ITER_MAX = {:d}).".format(
            fsbl.N_ITER_MAX
        ) )

    return beta_c, eta, f_c, g_c, h_c

def main( argc, argv ):
    f0 = fsbl.DEFAULT_F0
    n = fsbl.DEFAULT_N
    eta_max = fsbl.DEFAULT_ETA_MAX
    beta_min = DEFAULT_BETA_MIN
    beta_max = DEFAULT_BETA_MAX

    if ( argc > 1 ):
        f0 = float( argv[1] )

    if ( argc > 2 ):
        n = int( argv[2] )

    if ( argc > 3 ):
        eta_max = float( argv[3] )

    if ( argc > 4 ):
        beta_min = float( argv[4] )

    if ( argc > 5 ):
        beta_max = float( argv[5] )

    print( "f0       = {:f}".format( f0       ) )
    print( "n        = {:d}".format( n        ) )
    print( "eta_max  = {:f}".format( eta_max  ) )
    print( "beta_min = {:f}".format( beta_min ) )
    print( "beta_max = {:f}".format( beta_max ) )

    beta, eta, f, g, h = bisection_search( f0, n, eta_max, beta_min, beta_max )

    print( "h0   = {:+20.16f}".format( h[0]  ) )
    print( "ginf = {:+20.16f}".format( g[-1] ) )

    print( "beta = {:+20.16f}".format( beta ) )

    if ( ( g[-1] - fsbl.GINF )**2.0 < fsbl.GINF_TOL**2.0 ):
        fsbl.save_profiles( eta, f, g, h, beta )
        exit(0)
    else:
        exit(1)

if __name__ == "__main__":
    main( len(sys.argv), sys.argv )
