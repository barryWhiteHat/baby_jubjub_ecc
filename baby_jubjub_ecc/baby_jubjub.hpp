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

namespace libsnark {

template<typename FieldT>
class isOnCurve : public gadget<FieldT> {
//greater than gadget
private:
    /* no internal variables */
public:

    pb_variable<FieldT> x;
    pb_variable<FieldT> y;
    pb_variable<FieldT> a;
    pb_variable<FieldT> d;
    //intermeditate variables 
    pb_variable<FieldT> xx;   
    pb_variable<FieldT> axx;
    pb_variable<FieldT> dxx;
    pb_variable<FieldT> yy;
    pb_variable<FieldT> dxxyy;
    pb_variable<FieldT> lhs;
    pb_variable<FieldT> rhs;


    std::string annotation_prefix = "isonCurve";

    isOnCurve(protoboard<FieldT> &pb,
                   /*const pb_linear_combination_array<FieldT> &bits,*/
                   const pb_variable<FieldT> &x, const pb_variable<FieldT> &y, 
                   const pb_variable<FieldT> &a, const pb_variable<FieldT> &d,
                   const std::string &annotation_prefix);

    void generate_r1cs_constraints();
    void generate_r1cs_witness();

};

template<typename FieldT>
class pointAddition : public gadget<FieldT> {
//greater than gadget
private:
    /* no internal variables */
public:
    pb_variable<FieldT> a;
    pb_variable<FieldT> d;

    std::shared_ptr<isOnCurve<FieldT>> jubjub_isOnCurve;
    //intermeditate variables 
    pb_variable<FieldT> x1;
    pb_variable<FieldT> x2;
    pb_variable<FieldT> x3;
    pb_variable<FieldT> x1x2;
    pb_variable<FieldT> y1;
    pb_variable<FieldT> y2;
    pb_variable<FieldT> y3;
    pb_variable<FieldT> x1y2;
    pb_variable<FieldT> y1y2;
    pb_variable<FieldT> y1x2;
    pb_variable<FieldT> x1x2y1y2;
    pb_variable<FieldT> dx1x2y1y2;
    pb_variable<FieldT> ax1x2;

    std::string annotation_prefix = "point Addition ";


    pointAddition(protoboard<FieldT> &pb,
                   /*const pb_linear_combination_array<FieldT> &bits,*/
                   const pb_variable<FieldT> &a, const pb_variable<FieldT> &d,

                   const pb_variable<FieldT> &x1, const pb_variable<FieldT> &y1,
                   const pb_variable<FieldT> &x2, const pb_variable<FieldT> &y2,
                   const pb_variable<FieldT> &x3, const pb_variable<FieldT> &y3,

                   const std::string &annotation_prefix);

    void generate_r1cs_constraints();
    void generate_r1cs_witness();
};


template<typename FieldT>
class conditionalPointAddition : public gadget<FieldT> {
//greater than gadget
private:
    /* no internal variables */
public:
    pb_variable<FieldT> a;
    pb_variable<FieldT> d;


    //input variables 
    pb_variable<FieldT> x1;
    pb_variable<FieldT> y1;
    pb_variable<FieldT> x2;
    pb_variable<FieldT> y2;
    pb_variable<FieldT> x3;
    pb_variable<FieldT> y3;
    pb_variable<FieldT> canAdd;

    //intermediate variables
    pb_variable<FieldT> x_toAdd;
    pb_variable<FieldT> y_toAdd;
    pb_variable<FieldT> y_intermediate_toAdd1;
    pb_variable<FieldT> y_intermediate_toAdd2;
    pb_variable<FieldT> not_canAdd;


    std::string annotation_prefix = "conditioanl adiditon";

    std::shared_ptr<pointAddition<FieldT>> jubjub_pointAddition;


    conditionalPointAddition(protoboard<FieldT> &pb,
                   /*const pb_linear_combination_array<FieldT> &bits,*/
                   const pb_variable<FieldT> &a, const pb_variable<FieldT> &d,
                   const pb_variable<FieldT> &x1, const pb_variable<FieldT> &y1,
                   const pb_variable<FieldT> &x2, const pb_variable<FieldT> &y2,
                   const pb_variable<FieldT> &x3, const pb_variable<FieldT> &y3,
                   const pb_variable<FieldT> &canAdd, const std::string &_annotation_prefix);

    void generate_r1cs_constraints();
    void generate_r1cs_witness();
};

template<typename FieldT>
class pointMultiplication : public gadget<FieldT> {
//greater than gadget
private:
    /* no internal variables */
public:
    int coef_size; //coeffient size
    pb_variable<FieldT> a;
    pb_variable<FieldT> d;

    std::shared_ptr<isOnCurve<FieldT>> jubjub_isOnCurve;
    //intermeditate variables 
    pb_variable<FieldT> x;
    pb_variable<FieldT> y;
    pb_variable<FieldT> x_zero;
    pb_variable<FieldT> y_zero;

    pb_variable_array<FieldT> x_ret;
    pb_variable_array<FieldT> y_ret;


    // store the result of the current iteration
    pb_variable_array<FieldT> x_intermediary;
    pb_variable_array<FieldT> y_intermediary;

    pb_variable_array<FieldT> coef;

    std::vector<std::shared_ptr<pointAddition<FieldT> > > doub; //double
    std::vector<std::shared_ptr<conditionalPointAddition<FieldT> > > add; //double

    pointMultiplication(protoboard<FieldT> &pb,
                   /*const pb_linear_combination_array<FieldT> &bits,*/
                   const pb_variable<FieldT> &a, const pb_variable<FieldT> &d,
                   const pb_variable<FieldT> &x_base, const pb_variable<FieldT> &y_base,
                   const pb_variable_array<FieldT> &coef, const pb_variable_array<FieldT> x_ret,
                   const pb_variable_array<FieldT> y_ret, const std::string &annotation_prefix, 
                   int coef_size);

    void generate_r1cs_constraints();
    void generate_r1cs_witness();
};

} // libsnark
#include <baby_jubjub.cpp>
