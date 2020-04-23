#!/bin/bash

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

attached_command="python3 ../python/fsbl.py"
separated_command="python3 ../python/separation.py"

for eta_max in 5.0 10.0 20.0
do
    for n in 32 64 128 256 512 1024 2048 4096 8192 16384
    do
        for beta in -0.18 0.0 0.3 1.0
        do
            echo
            $attached_command "$beta" 0.0 "$n" "$eta_max"
        done

        echo
        $separated_command 0.0 "$n" "$eta_max"
    done
done
