'''   
    copyright 2018 to the baby_jubjub_ecc Authors

    This file is part of baby_jubjub_ecc.

    baby_jubjub_ecc is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    baby_jubjub_ecc is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with baby_jubjub_ecc.  If not, see <https://www.gnu.org/licenses/>.
'''

from sapling_jubjub import *

Point.ZERO = Point(Fq.ZERO, Fq.ONE)
#print(Point.ZERO, Point.ZERO + Point.ZERO )
assert Point.ZERO + Point.ZERO == Point.ZERO



x0 = Fq(17777552123799933955779906779655732241715742912184938656739573121738514868268)
y0 = Fq(2626589144620713026669568689430873010625803728049924121243784502389097019475)


base = Point(x0, y0)


binary = '1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001'

l = Fq(int(binary, 2))
l = Fq(2**253 + 1)
print(l)
out = base * l 
print( out, "outut")

