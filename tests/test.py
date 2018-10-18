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

x1 = Fq(16540640123574156134436876038791482806971768689494387082833631921987005038935)
y1 = Fq(20819045374670962167435360035096875258406992893633759881276124905556507972311)

base = Point(x0, y0)
#x = Fq(0)
#y = Fq(1)
#print ("lhs , rhs    : ", x*x, JUBJUB_A*(x*x) + (y*y) , Fq(1) + (JUBJUB_D * (x*x) * (y*y)))

x2 = x1
y2 = y1

x1 = x0 
y1 = y0

x3 =  (x1*y2 + y1*x2) / (Fq.ONE + JUBJUB_D*x1*x2*y1*y2) 
assert( x3 == (x1*y2 + y1*x2) * (Fq(1) + JUBJUB_D*x1*x2*y1*y2).inv() )

y3 = (y1*y2 - JUBJUB_A*x1*x2) / (Fq.ONE - JUBJUB_D*x1*x2*y1*y2)
assert( y3 == (y1*y2 - JUBJUB_A*x1*x2) * (Fq.ONE - JUBJUB_D*x1*x2*y1*y2).inv() )
print("out " , x3, y3)


p3 = Point(x3, y3)
assert(p3.is_on_curve())
print(base + Point(Fq(0),Fq(1)))

# point multiplicaion test inpouts
print(base *  Fq(1))
print(base *  Fq(2))
print(base *  Fq(7))
print(base *  Fq(15))
print(base *  Fq(31))

# test point for tests.cpp
binary = "1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"
# 7237005577332262213973186563042994240829374041602535252466099000494570602497
l = Fq(int(binary, 2))
print(base * l , "outut")


print ( test + test, "double test") 

'''
gen = Point(x1, y1)
for i in range(2,10):
    res = base * Fq(i)
    print (res)
    assert(res.is_on_curve())
    assert(res != base)

res = base * Fq(8)
print ( res )
assert(res == gen) 



res = base * Fq(r_j + 1)
assert(res == base)

print (res)
'''
