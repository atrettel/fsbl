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
GINF_TOL = 0.0
N_ITER_MAX = 128

def first_derivatives( f, g, h, alpha, beta ):
    fp = g
    gp = h
    hp = -alpha * f * h + beta * ( g**2.0 - 1.0 )
    return fp, gp, hp

def explicit_first_order_solver( f0, g0, h0, alpha, beta, eta ):
    n = len(eta)

    f = [f0] * n
    g = [g0] * n
    h = [h0] * n

    for i in range(n-1):
        deta = eta[i+1] - eta[i]

        fp, gp, hp = first_derivatives( f[i], g[i], h[i], alpha, beta )

        f[i+1] = f[i] + deta * fp
        g[i+1] = g[i] + deta * gp
        h[i+1] = h[i] + deta * hp

    return f, g, h

def similarity_coordinate( n, eta_max ):
    deta = eta_max / float( n - 1 )
    eta = [0.0] * n
    for i in range(n-1):
        eta[i+1] = eta[i] + deta
    return eta

def main( argc, argv ):
    beta = 0.0
    f0 = 0.0
    n = 128
    eta_max = 5.0

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

    eta = similarity_coordinate( n, eta_max )

    h0 = 0.4696

    f, g, h = explicit_first_order_solver( f0, G0, h0, ALPHA, beta, eta )

    print( g[-1] )

if __name__ == "__main__":
    main( len(sys.argv), sys.argv )
