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


#include <cassert>
#include <memory>

#include <libsnark/gadgetlib1/gadget.hpp>

#ifndef BABY_JUBJUB_CPP
#define BABY_JUBJUB_CPP
#endif

#include <sha256/sha256_ethereum.cpp>


namespace libsnark {

template<typename FieldT, typename HashT>
class eddsa : public gadget<FieldT> {

private:
    /* no internal variables */
public:

    pb_variable<FieldT> a;
    pb_variable<FieldT> d;


    //input variables 
    pb_variable_array<FieldT> pk_x;
    pb_variable_array<FieldT> pk_y;
    pb_variable_array<FieldT> A;
    pb_variable<FieldT> b_x;
    pb_variable<FieldT> b_y;
    pb_variable_array<FieldT> message;
    pb_variable_array<FieldT> S;
    pb_variable_array<FieldT> r_x;
    pb_variable_array<FieldT> r_y;
    pb_variable<FieldT> s_x;
    pb_variable<FieldT> s_y;

    //intermeidate variables 

    pb_variable_array<FieldT> lhs_x;

    pb_variable_array<FieldT> lhs_y;
    pb_variable_array<FieldT> rhs_mul_x;
    pb_variable_array<FieldT> rhs_mul_y;

    pb_variable<FieldT> rhs_x;
    pb_variable<FieldT> rhs_y;

    std::shared_ptr <block_variable<FieldT>> encode_point_r_input;
    std::shared_ptr <block_variable<FieldT>> encode_point_pk_input;
    std::shared_ptr <block_variable<FieldT>> encode_points_input;
    std::shared_ptr <block_variable<FieldT>> hint_input;


    std::shared_ptr<digest_variable<FieldT>> encoded_r;
    std::shared_ptr<digest_variable<FieldT>> encoded_pk;
    std::shared_ptr<digest_variable<FieldT>> encoded_points;
    std::shared_ptr<digest_variable<FieldT>> h;
    // gadgets 
    std::shared_ptr<isOnCurve<FieldT>> jubjub_isOnCurve1;
    std::shared_ptr<isOnCurve<FieldT>> jubjub_isOnCurve2;

    std::shared_ptr<pointAddition<FieldT>> jubjub_pointAddition;
    std::shared_ptr<pointMultiplication<FieldT>> jubjub_pointMultiplication_lhs;
    std::shared_ptr<pointMultiplication<FieldT>> jubjub_pointMultiplication_rhs;

    std::shared_ptr<HashT> encode_point_r;
    std::shared_ptr<HashT> encode_point_pk;
    std::shared_ptr<HashT> encode_points;
    std::shared_ptr<HashT> hint;

    std::shared_ptr<digest_variable<FieldT>> lhs_leaf;

    std::shared_ptr<multipacking_gadget<FieldT>> unpacker_h;
    std::shared_ptr<multipacking_gadget<FieldT>> unpacker_pk_x;
    std::shared_ptr<multipacking_gadget<FieldT>> unpacker_pk_y;
    std::shared_ptr<multipacking_gadget<FieldT>> unpacker_r_x;
    std::shared_ptr<multipacking_gadget<FieldT>> unpacker_r_y;


    pb_variable_array<FieldT> h_packed;
    pb_variable_array<FieldT> h_bits;
    pb_variable_array<FieldT> pk_x_packed;
    pb_variable_array<FieldT> pk_y_packed;
    pb_variable_array<FieldT> r_x_packed;
    pb_variable_array<FieldT> r_y_packed;


    eddsa(protoboard<FieldT> &pb,
                   //const pb_linear_combination_array<FieldT> &bits,
                   const pb_variable<FieldT> &a, const pb_variable<FieldT> &d,
                   const pb_variable_array<FieldT> &pk_x, const pb_variable_array<FieldT> &pk_y,
                   const pb_variable<FieldT> &b_x, const pb_variable<FieldT> &b_y,
                   const pb_variable_array<FieldT> &r_x, const pb_variable_array<FieldT> &r_y,
                   const pb_variable_array<FieldT> &message, const pb_variable_array<FieldT> &S
                   );

    void generate_r1cs_constraints();
    void generate_r1cs_witness();
};

}
#include <eddsa.cpp>

