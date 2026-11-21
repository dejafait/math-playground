# Actual quotient loss working record1963

Approved target: assessment1962's fixed-positive-interval actual q=1/2
Jensen-loss test. Initial reasoning preserved below. The complete argument
is now canonical in C029f, pending separate audit; this is not a second
proof or an independently approved result.

Inputs C028d/e/f/g. Put t=f_d/(2d), m=E_nu t, v=t-m.
C028d/e/g give m=O_A(1/d). Positivity gives, uniformly for 1<=x<=2,
0<=d^(-1)log(P_d(x)/x^d)<=K d^(-1/4), by F(d/x).
Thus t(x+b_1)->(1/2)log(x/(x+b_1))<0 uniformly.
With lambda=(1/2)log(1+b_1/2)>0, eventually v<=-lambda/2
on that length-one interval. Let r=exp(-lambda/2)-1+lambda/2>0.
The nonnegative remainder exp(v)-1-v gives E exp(v)>=1+r/(2Ad).
Hence D=4Ad log E exp(v)>=4Ad log(1+r/(2Ad)), whose degree limit
is 2r, independently of fixed A. Need full integrability cases and
the C028d/e payment implication checked in canonical proof.

At zero a numerator zero of multiplicity k gives moment exponent
(k-d)/(2d)>=-1/2; other real zeros are harmless positive exponents.
The payment expression 4Ad log Z=D+(1/d)integral f_d has liminf
at least 2r-8M/A, since H_d>=0. This would stop only this fixed-q
upper-payment normalization, not RH or other signed estimates.
