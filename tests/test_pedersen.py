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
import pdb



def hashtopoint(y):
    # brute force this, Should use 
    # https://github.com/daira/zcash-test-vectors/blob/master/sapling_jubjub.py#L69
    x = 0
    while x < q_j:
        p = Point(Fq(x), Fq(y))
        if p.is_on_curve():
            return(x)
        x = (x + 1) %q_j
    return(False)


# hash to point is currently broken. 
# It will take infinite time to find the hash of
# any point other than y = 1
# include here as the zksnark is working correctly. 
# just need to improve this algorithm. 

H = Point(Fq(16540640123574156134436876038791482806971768689494387082833631921987005038935),Fq(20819045374670962167435360035096875258406992893633759881276124905556507972311)) #hashtopoint(h)
base = Point(Fq(17777552123799933955779906779655732241715742912184938656739573121738514868268), Fq(2626589144620713026669568689430873010625803728049924121243784502389097019475))
# we use a naive point which means that this is borken as the discreate logitihim 
# between the  and the base is known. But it works for the test. 

# commitment 
m = Fq(123123123123312321321) # message
r = Fq(123123123123123123123123) #random number
print("commitiment" , base * m + H*r," r ", r)
print("message ", m)


r_bin = [ int(x) for x in bin(int(r))[2:] ]
m_bin = [ int(x) for x in bin(int(m))[2:] ]

r_bin = [0] * (253 - len(r_bin)) + r_bin
m_bin = [0] * (253 - len(m_bin)) + m_bin
print(r_bin)
print (m_bin)


