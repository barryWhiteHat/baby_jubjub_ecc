# baby\_jubjub\_ecc

This repository contains zksnark constarint systems for [twisted ewards curve](https://github.com/barryWhiteHat/baby_jubjub) 
point addion, point multiplicaion, eddsa signature verificaion and pedersen commiments. As well as python scripts for
test case generation. 

This is a naive implmentaion and considerable optimizations are possible. 

## build instructions:

### build libsnark gadget and getting the proving key
get dependencies `git submodule update --init --recursive`
`mkdir build` 
`cd build`
`cmake .. && make`

### Running the tests
Start your prefered ethereum node, `cd tests` and run `python3 test*` will generate all the 
test variables that you can confirm in `src/main.cpp`

You can run the test after building by 
```
cd build
./src/main
```


## Resources 
[Lecture 16](https://www.youtube.com/watch?v=vnpZXJL6QCQ) and [Lecture 17] (https://www.youtube.com/watch?v=zTt4gvuQ6sY)
of [this](https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg) course should help you get a good understanding of 
the basics of what we are doing here. 


