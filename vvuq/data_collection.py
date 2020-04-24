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

import subprocess

for eta_max in [ 5.0, 10.0, 20.0 ]:
    for n in [ 2**5, 2**6, 2**7, 2**8, 2**9, 2**10, 2**11, 2**12, 2**13,
        2**14 ]:
        for beta in [ -0.18, 0.0, 0.3, 1.0 ]:
            completed_process = subprocess.run( [
                "python3",
                "../python/fsbl.py",
                str(beta),
                "0.0",
                str(n),
                str(eta_max),
            ] )

            print( "Return code: {:d}\n".format( completed_process.returncode ) )

exit(0)
