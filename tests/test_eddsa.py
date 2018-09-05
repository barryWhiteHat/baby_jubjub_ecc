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
import hashlib

from ed25519 import *

import pdb

def toBin(x):
    out = [ int(x) for x in bin(int(x, 16))[2:] ]
    out = [0] * (256 - len(out)) + out
    return(out) 


if __name__ == "__main__":


    #Bx = 15112221349535400772501151409588531511454012693041857206046113283949847762202 #4 * inv(5)
    #By = 46316835694926478169428394003475163141307993866256225615783033603165251855960 #xrecover(By)
 
    Bx = 17777552123799933955779906779655732241715742912184938656739573121738514868268 #4 * inv(5)
    By = 2626589144620713026669568689430873010625803728049924121243784502389097019475 #xrecover(By)

    base = Point(Fq(Bx), Fq(By))
        
    sk = "123123"
    m = "4147a3c1586a12cd3ebbc0ad31d6161e10a57894fe2d114d98b509a812918ad0"
       #"3384407148f0a084436f6bb1ca2ad6dc2eb1d30570d6b8917d431c8622313ca0"
    pk = publickey(sk)

    #assert(ed25519.isoncurve(A))
    R,S = signature(m,sk,pk)
    print( "R  ", R, " S " ,  S , " m " ,  m , "pk  ",  pk)

    #h = Hint(encodepoint(R) + encodepoint(pk) + m)

    checkvalid(R,S,m,pk)

    R[0] = hex(int(''.join(str(e) for e in hexToBinary(hex(R[0]))[::-1]),2))
    R[1] = hex(int(''.join(str(e) for e in hexToBinary(hex(R[1]))[::-1]),2))

    pk[0] = hex(int(''.join(str(e) for e in hexToBinary(hex(pk[0]))[::-1]),2))
    pk[1] = hex(int(''.join(str(e) for e in hexToBinary(hex(pk[1]))[::-1]),2))


    message = hex(int(''.join(str(e) for e in hexToBinary(m)),2))
    #print( " h " , h ) 
    S_bin = toBin(hex(S))

    message_bin = toBin(message)
    pk_x_bin = toBin(pk[0])
    pk_y_bin = toBin(pk[1])

    r_x_bin = toBin(R[0])
    r_y_bin = toBin(R[1])

    #print(S_bin)
    #print (h_bin)

  
    print( "    S.fill_with_bits(pb,  {" , S_bin , "});")


    print( "    message.fill_with_bits(pb,  {" , message_bin , "});")

    print( "    pk_x_bin.fill_with_bits(pb,  {" , pk_x_bin , "});")
    print( "    pk_y_bin.fill_with_bits(pb,  {" , pk_y_bin , "});")

    
    print( "    r_x_bin.fill_with_bits(pb,  {" , r_x_bin , "});")
    print( "    r_y_bin.fill_with_bits(pb,  {" , r_y_bin , "});")


    '''
    pb.val(r_y) = FieldT("309603861070827434771553290186311069341018266983092380603809384193577137789");

    S.fill_with_bits(pb,  {0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0});

    H.fill_with_bits(pb, {0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0});

    '''





