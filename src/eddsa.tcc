/*    
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
*/


using namespace libff;
typedef bigint<alt_bn128_r_limbs> bigint_r;

namespace libsnark {


template<typename FieldT>
eddsa<FieldT>::eddsa(protoboard<FieldT> &pb,
                   //const pb_linear_combination_array<FieldT> &bits,
                   const pb_variable<FieldT> &a, const pb_variable<FieldT> &d,
                   const pb_variable<FieldT> &pk_x, const pb_variable<FieldT> &pk_y,
                   const pb_variable<FieldT> &b_x, const pb_variable<FieldT> &b_y,
                   const pb_variable<FieldT> &r_x, const pb_variable<FieldT> &r_y,
                   const pb_variable_array<FieldT> &H, const pb_variable_array<FieldT> &S
                   ):
        gadget<FieldT>(pb, "eddsa") , a(a), d(d), pk_x(pk_x), pk_y(pk_y), b_x(b_x), b_y(b_y), r_x(r_x), r_y(r_y) , H(H), S(S) 
{


    lhs_x.allocate(pb, 253,  FMT("lhs x", "eddsa"));
    lhs_y.allocate(pb, 253, FMT("lhs y", "eddsa"));
    rhs_mul_x.allocate(pb,253, FMT( "rhs mul x" , "eddsa" ));
    rhs_mul_y.allocate(pb,253, FMT( "rhs mul y ", "eddsa"));

    rhs_x.allocate(pb, FMT("rhs x", "eddsa"));
    rhs_y.allocate(pb, FMT( "rhs y","eddsa"));

    jubjub_isOnCurve1.reset( new isOnCurve <FieldT> (pb, pk_x, pk_y, a, d, "Confirm x, y is on the twiseted edwards curve"));
    jubjub_isOnCurve2.reset( new isOnCurve <FieldT> (pb, r_x, r_y, a, d, "Confirm x, y is on the twiseted edwards curve"));


    jubjub_pointMultiplication_lhs.reset( new pointMultiplication <FieldT> (pb, a, d, b_x, b_y, S, lhs_x, lhs_y, " lhs check "));
    jubjub_pointMultiplication_rhs.reset( new pointMultiplication <FieldT> (pb, a, d, pk_x, pk_y, H, rhs_mul_x, rhs_mul_y, "rhs mul "));
    jubjub_pointAddition.reset( new pointAddition <FieldT> (pb, a, d, rhs_mul_x[252], rhs_mul_y[252] , r_x , r_y, rhs_x, rhs_y , "rhs addition"));



}



template<typename FieldT>
void eddsa<FieldT>::generate_r1cs_constraints()
{
    // not sure if we need to check pub key and r 
    // are on the curve. But doing it here for defense
    // in depth
    jubjub_isOnCurve1->generate_r1cs_constraints();
    jubjub_isOnCurve2->generate_r1cs_constraints();

    jubjub_pointMultiplication_lhs->generate_r1cs_constraints();
    jubjub_pointMultiplication_rhs->generate_r1cs_constraints();
    jubjub_pointAddition->generate_r1cs_constraints();

    this->pb.add_r1cs_constraint(r1cs_constraint<FieldT>({lhs_x[252]} , {1}, {rhs_x}),
                           FMT("find y1*x2 == y1x2", "eddsa"));
    this->pb.add_r1cs_constraint(r1cs_constraint<FieldT>({lhs_y[252]} , {1}, {rhs_y}),
                           FMT("find y1*x2 == y1x2", "eddsa"));
}


template<typename FieldT>
void eddsa<FieldT>::generate_r1cs_witness()
{
    jubjub_isOnCurve1->generate_r1cs_witness();
    jubjub_isOnCurve2->generate_r1cs_witness();
    jubjub_pointMultiplication_lhs->generate_r1cs_witness();
    jubjub_pointMultiplication_rhs->generate_r1cs_witness();
    jubjub_pointAddition->generate_r1cs_witness();


    //debug
    /*
    std::cout <<  this->pb.lc_val(lhs_x[252]) << " " <<  this->pb.lc_val(rhs_x) << " "<< std::endl; // <<  this->pb.lc_val(S) << " " <<  this->pb.lc_val(H) ;
    for (uint i = 0 ; i < 253; i++) { 
        std::cout << i << " i  " << this->pb.lc_val(S[i]) << std::endl;
    }*/
}

}
