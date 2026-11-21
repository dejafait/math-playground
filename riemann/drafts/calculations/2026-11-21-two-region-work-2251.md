# Fixed two-region attempt2251

Prior gate: SPECIALIZE in assessment2249, separately retained by2250.
Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
Target: exactly the fixed J and I boxes in2249; no retuning after a sign
failure. Possible use: one-removal decrease, hence a shape input for
another sine operator. Iteration and the all-degree bridge stay open.
Inputs: L019/L058, C919f methods/contracts, C919m/n/o interfaces.
Generic-model and approval-loop stops2238/2241/2243/2246/2248 remain.

## Fixed plan saved before calculation

Use U=4, n<=4, Simpson M=16384, precision80; exact dyadic nodes.
Bound finite kernel derivatives on [0,5] by1280 closed cells of width1/256.
Use x Taylor degree8 at57/4, radius1/4, and32 closed x cells.
Integrate both sine/cosine coefficient families at u=0 and
u=(2i+1)/32 for i=1,...,15. Use u Taylor degree16, with centers as above;
near zero divide the polynomial difference symbolically, never divide
independent errors by u. For I use32 equal closed subcells in each
u interval[i/16,(i+1)/16], i=1,...,15. For J use32 closed subcells
covering[0,1/16]. Required rational lower bounds: J>1/100, I>1e-12.
Failure of an enclosure is inconclusive; a certified nonpositive point
rejects only the stronger fixed-box test. No parameter/cutoff/order
retuning in this step. Save all preflight bounds before the node pass.

## Analytic derivation to implement and check

Write K_n(s)=exp(s/2-v) P_0(v), v=pi*n^2*exp(2s), P_0=8v^2-12v.
Then P_(m+1)=(1/2-2v)P_m+2v P_m'. Exact rational polynomial recurrence
supplies all derivatives through17 (coefficients, not sampled derivatives).
Let A_m=sum_k |p_mk|*(4k)^k with the k=0 factor1. For v>=0,
v^k*exp(-v/4)<=(4k)^k, by maximizing the elementary function.
Thus for n>=5, n^2>=25+10(n-5), exp(2s)>=1+2s, pi>3,

 sum_(n>=5)|K_n^(m)(s)| <= 2 A_m exp(-225/4) exp(-112s), s>=0.

The geometric ratio exp(-45/2)<1/2 follows from exp(1)>2.
Consequently omitted-index t^j integrals at any u>=0 are bounded by
2 A_m exp(-225/4) j!/112^(j+1). For all indices and s>=4,
n^2>=1+3(n-1), the geometric bound gives
sum_n |K_n^(m)(s)| <=2 A_m exp(s/2-(9/4)exp(2s)).
Since s/2 <= exp(2s)/4 and exp(2s)>=256(1+2(s-4)), this is
<=2 A_m exp(-512) exp(-1024(s-4)). Integrate each t^j by the
finite binomial expansion at4; translation only decreases this envelope.
Pointwise omitted-index bounds also apply at every Taylor center.

Whole compact derivative bounds use exp(r/2-v_lo)*sum|p_mk|v_hi^k,
summed over n<=4 on every closed spatial cell. Together with the two
tails this bounds integral_0^infinity |K^(17)(s)|ds =: M17,
and integral t^9 K(t)dt =: M9. Translated M9 is bounded by M9 using
the imported K decrease. These pay all Taylor and derivative tails.

I'= -K(u)+x S_x(u), S_x(u)=integral K(u+t)sin(xt)dt,
I''+x^2 I=-K'(u). Justify by differentiation and integration by parts,
using the complete bounds. At each u center integrate x Taylor coefficients
of I and S, with full ninth-moment remainder. For normalized u coefficients,
a0=I, a1=-K+xS, a_(k+2)=(-K^(k+1)/k! - x^2*a_k)/((k+1)(k+2)).
Finite kernel jets include pointwise omitted-index errors. The u Taylor
remainder is M17*|u-center|^17/17!. At zero,
J=sum_(k=1)^16 a_k*u^(k-1) + remainder bounded by M17*u^16/17!,
including u=0 by continuity. This cancels the constant before bounding.

FTC gives the quotient integrand =integral_0^1 K'(t+su)ds. Rapid
derivative decay uniformly for u in[0,1] supplies signed Fubini and
dominated convergence at zero. The same complete derivative bounds
justify parameter derivatives. At an actual root, I_x(0)=Xi(x)=0,
so I_x(u)=u J_x(u), G_x'=-x^2 I_x. Both closed signs pay the split;
C919o pays u>=1 including1. G_x'(0)=0 remains the root boundary.
Multiplicity is unrestricted. This is a finite specialization, not RH.

## State before node pass

Unfinished: implement and check every bound, run the one fixed setup,
inspect complete relevant records, and write canonical result or failure.
No signed margin has been computed. Full matching Mathlib coverage is
unchecked. Reuse cited Simpson/Taylor/FTC/dominated-integration inputs
from2249 without reproof; all specializations above still require review.

## Completed fixed pass

The unchanged setup passed: J lower bound0.23259130360944 and I lower
bound9.824596137136e-9, exceeding1/100 and1e-12. Complete proofs, arithmetic
qualifications and root conversion are canonical in C919r. Full evidence:
scripts/real-zero-origin/two_region_preflight_2251.json, two_region_2251.json
and two_region_inspection_2251.json. Internal inspection passed97255 checks,
zero failures. No setting changed after the sign pass. A separate conceptual
audit remains required. No iteration or all-degree claim follows.
