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

import sys

# Global parameters
ALPHA = 1.0
G0 = 0.0
GINF = 1.0
GINF_TOL = 1.0e-15
N_ITER_MAX = 128

def first_derivatives( f, g, h, beta ):
    fp = g
    gp = h
    hp = -ALPHA * f * h + beta * ( g**2.0 - 1.0 )
    return fp, gp, hp

def explicit_first_order_solver( f0, g0, h0, beta, eta ):
    n = len(eta)

    f = [f0] * n
    g = [g0] * n
    h = [h0] * n

    for i in range(n-1):
        deta = eta[i+1] - eta[i]

        fp, gp, hp = first_derivatives( f[i], g[i], h[i], beta )

        f[i+1] = f[i] + deta * fp
        g[i+1] = g[i] + deta * gp
        h[i+1] = h[i] + deta * hp

    return f, g, h

def bisection_search( beta, f0, n, eta_max ):
    deta = eta_max / float(n-1)
    eta = [0.0] * n
    for i in range(n-1):
        eta[i+1] = eta[i] + deta

    h0_l = 0.0
    f_l, g_l, h_l = explicit_first_order_solver( f0, G0, h0_l, beta, eta )
    sign_l = ( ( g_l[n-1] - GINF ) > 0.0 )

    h0_r = 1.0
    f_r, g_r, h_l = explicit_first_order_solver( f0, G0, h0_r, beta, eta )
    sign_r = ( ( g_r[n-1] - GINF ) > 0.0 )

    n_iter = 0
    while ( n_iter < N_ITER_MAX ):
        h0_c = 0.5 * ( h0_l + h0_r )
        f_c, g_c, h_c = explicit_first_order_solver( f0, G0, h0_c, beta, eta )
        sign_c = ( ( g_c[n-1] - GINF ) > 0.0 )

        if ( ( h0_r - h0_l ) <= 0.0 ):
            print( "Interval has zero length." )
            break
        elif ( ( g_c[n-1] - GINF)**2.0 < GINF_TOL**2.0 ):
            print( "Solution within tolerance." )
            break

        if ( sign_c == sign_l ):
            h0_l = h0_c
            f_l = f_c
            g_l = g_c
            h_l = h_c
        else:
            h0_r = h0_c
            f_r = f_c
            g_r = g_c
            h_r = h_c

        n_iter += 1

    if ( n_iter == N_ITER_MAX ):
        print( "Maximum number of iterations." )

    return eta, f_c, g_c, h_c

def main( argc, argv ):
    beta = 0.0
    f0 = 0.0
    n = 2**16
    eta_max = 100.0

    if ( argc > 1 ):
        beta = float( argv[1] )

    if ( argc > 2 ):
        f0 = float( argv[2] )

    if ( argc > 3 ):
        n = int( argv[3] )

    if ( argc > 4 ):
        eta_max = float( argv[4] )

    print( beta )
    print( f0 )
    print( n )
    print( eta_max )

    eta, f, g, h = bisection_search( beta, f0, n, eta_max )

    print( h[0] )
    print( g[n-1] )

if __name__ == "__main__":
    main( len(sys.argv), sys.argv )
