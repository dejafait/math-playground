# Terminal shear working record1588

Approved target: assessment1587's one specified terminal shear, with no
additional coordinates or shears. Inputs: C028h's actual companion block,
positive a=binom(d,2)S_2, b=2binom(d,3)S_3, and its exact block minimum.

For S=I+t E_(d,d-1), the matrix unit squares to zero, so S^-1=I-t E.
The terminal block after shearing is
[0,tb,-b; 1,-ta,a; t,1-at^2,ta]. Positive diagonal ratios x,y give
skew cost squared
(x-bt/x)^2+(b/(xy)+txy)^2+(a/y-y+at^2*y)^2.
The cross terms -2bt and +2bt cancel exactly. Thus the first two
squares equal (1+t^2*y^2)(x^2+b^2/(x^2*y^2)).

Let k=sqrt(1+t^2*y^2)>=1 and r=y/k>0. Minimizing only in x gives
cost squared >=2b*k/r+k^2*(a/r-r)^2
>=2b/r+(a/r-r)^2. This is the existing unsheared minimum-in-x
function. Its global minimum and uniform c*d floor are C028h.
Equality in the global minimum is achievable at t=0 and C028h's
optimizing x,y; nonzero t gives a strict comparison since b>0.

Remaining checks before final record: full-size compression commutation,
signs and 1/(2i) factor, d=3, and no reversal of the height upper bound.
No numerical evidence or full-cost upper bound is used. Canonical proof
will replace this working record as the mathematical reference, while
this unfinished reasoning is preserved.
