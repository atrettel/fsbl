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

ALPHA = 1.0
G0 = 0.0
GINF = 1.0
GINF_TOL = 1.0e-15
N_ITER_MAX = 256

def first_order_system( f, g, h, beta ):
    fp = g
    gp = h
    hp = -ALPHA * f * h + beta * ( g * g - 1.0 )
    return fp, gp, hp

def solve_rk4( f0, h0, beta, eta ):
    n = len(eta)

    f = [f0] * n
    g = [G0] * n
    h = [h0] * n

    for i in range(n-1):
        deta = eta[i+1] - eta[i]

        fp1, gp1, hp1 = first_order_system(
            f[i],
            g[i],
            h[i],
            beta,
        )

        df1 = deta * fp1
        dg1 = deta * gp1
        dh1 = deta * hp1

        fp2, gp2, hp2 = first_order_system(
            f[i] + 0.5 * df1,
            g[i] + 0.5 * dg1,
            h[i] + 0.5 * dh1,
            beta,
        )

        df2 = deta * fp2
        dg2 = deta * gp2
        dh2 = deta * hp2

        fp3, gp3, hp3 = first_order_system(
            f[i] + 0.5 * df2,
            g[i] + 0.5 * dg2,
            h[i] + 0.5 * dh2,
            beta,
        )

        df3 = deta * fp3
        dg3 = deta * gp3
        dh3 = deta * hp3

        fp4, gp4, hp4 = first_order_system(
            f[i] + df3,
            g[i] + dg3,
            h[i] + dh3,
            beta,
        )

        df4 = deta * fp4
        dg4 = deta * gp4
        dh4 = deta * hp4

        f[i+1] = f[i] + ( df1 + 2.0 * df2 + 2.0 * df3 + df4 ) / 6.0
        g[i+1] = g[i] + ( dg1 + 2.0 * dg2 + 2.0 * dg3 + dg4 ) / 6.0
        h[i+1] = h[i] + ( dh1 + 2.0 * dh2 + 2.0 * dh3 + dh4 ) / 6.0

    return f, g, h

def bisection_search( beta, f0, n, eta_max, h0_min, h0_max ):
    deta = eta_max / float(n-1)
    eta = [0.0] * n
    for i in range(n-1):
        eta[i+1] = eta[i] + deta

    h0_l = h0_min
    f_l, g_l, h_l = solve_rk4( f0, h0_l, beta, eta )
    sign_l = ( g_l[n-1] > GINF )

    h0_r = h0_max
    f_r, g_r, h_l = solve_rk4( f0, h0_r, beta, eta )
    sign_r = ( g_r[n-1] > GINF )

    assert( h0_r > h0_l )

    print( "[{:f}, {:f}]".format( h0_l, h0_r ) )

    n_iter = 0
    while ( n_iter < N_ITER_MAX ):
        h0_c = 0.5 * ( h0_l + h0_r )
        f_c, g_c, h_c = solve_rk4( f0, h0_c, beta, eta )
        sign_c = ( g_c[n-1] > GINF )

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
    n = 2**14
    eta_max = 10.0
    h0_min = 0.0
    h0_max = 1.0

    if ( argc > 1 ):
        beta = float( argv[1] )

    if ( argc > 2 ):
        f0 = float( argv[2] )

    if ( argc > 3 ):
        n = int( argv[3] )

    if ( argc > 4 ):
        eta_max = float( argv[4] )

    if ( argc > 5 ):
        h0_min = float( argv[5] )

    if ( argc > 6 ):
        h0_max = float( argv[6] )

    print( "beta    = {:f}".format( beta    ) )
    print( "f0      = {:f}".format( f0      ) )
    print( "n       = {:d}".format( n       ) )
    print( "eta_max = {:f}".format( eta_max ) )
    print( "h0_min  = {:f}".format( h0_min  ) )
    print( "h0_min  = {:f}".format( h0_max  ) )

    eta, f, g, h = bisection_search( beta, f0, n, eta_max, h0_min, h0_max )

    print( h[0] )
    print( g[n-1] )

if __name__ == "__main__":
    main( len(sys.argv), sys.argv )
