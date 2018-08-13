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
if __name__ == "__main__":
    sk = 14882071797825200960306924264818229255658412868262546790940224952926711938513
    out = publickey(sk)
    #Bx = 15112221349535400772501151409588531511454012693041857206046113283949847762202 #4 * inv(5)
    #By = 46316835694926478169428394003475163141307993866256225615783033603165251855960 #xrecover(By)
 
    Bx = 17777552123799933955779906779655732241715742912184938656739573121738514868268 #4 * inv(5)
    By = 2626589144620713026669568689430873010625803728049924121243784502389097019475 #xrecover(By)

    base = Point(Fq(Bx), Fq(By))


    
    sk = "123"
    m = "asdf1asdfaflkjasdlkfjalksjfklasjflkadsjflksdjlkfjdklj"
    pk = publickey(sk)


    #assert(ed25519.isoncurve(A))
    R,S = signature(m,sk,pk)
    print( "R  ", R, " S " ,  S , " m " ,  m , "pk  ",  pk)
    h = Hint(encodepoint(R) + encodepoint(pk) + m)
    print( " h " , h ) 
    checkvalid(R,S,m,pk)
    point1 = Point(Fq(R[0]), Fq(R[1]))

    S_bin = [ int(x) for x in bin(S)[2:] ]
    h_bin = [ int(x) for x in bin(h)[2:] ] 
    S_bin = [0] * (253 - len(S_bin)) + S_bin
    h_bin = [0] * (253 - len(h_bin)) + h_bin
    print(S_bin)
    print (h_bin)







