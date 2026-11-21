# Lemma 952: the fixed pointwise signed-response norm test is inconclusive

## Hypotheses

Use L938's actual continuous density v, its complete34-row polynomial,
twelve labelled factors and normalization M_0^12. Retain its unchanged
degree256 kernel polynomial p,257 nodes,theta cutoff8,precision200,
grid10^-120 and complete uniform residual epsilon from(15).
Use L948's exact response J_p[k-p] and full second-order remainder.
Use C948a's audited signed-prefix maxima M_k in common degree2816,
J=1411, and its full positive derivative majorants V_k at rho=1/32.
L949's full degree3089 endpoint enclosure is a consistency check.

Numerical conclusions are conditional on the inherited theta inclusion,
signed derivative-prefix multiplication, full polynomial multiplication
and Python exact-integer/Fraction/directed-Decimal execution contracts.
Those original producers are not independently audited here. All new
scalar normalizations and the full endpoint contraction are replayed
below. No sign or independence of residual values, actual density sign,
RH premise, interval sign or tail onset is assumed.

## Conclusion

There is a complete symmetric enclosure for the actual v(8), with
outward rational bounds

    -8.166988064413890e-50 <= v(8) <= 8.166988064438508e-50.      (1)

It contains zero. The fixed allowance U and positive polynomial endpoint
v_p(8) satisfy

    8.166988064426198e-50 <= U <= 8.166988064426199e-50,
    1.230901990512815e-61 <= v_p(8) <= 1.230901990512816e-61.   (2)

For the exact lower enclosure v_(p,-), the computed ratio obeys

    663496210695.3523 <= U/v_(p,-) <= 663496210695.3524.        (3)

Thus this prescribed sufficient positive-sign test U<v_(p,-) fails.
This is a failure of an upper-allowance certificate, not an error lower
bound, a negative sign, an actual counterexample or an obstruction to
every possible endpoint method. Stop this fixed test without refinement.
No interval positivity, integrated outer-tail budget, global crossing,
all-degree sign transfer or RH conclusion follows. This is reproduction
of the assessed Taylor/beta/Bernstein method, not a new general theorem.

## Proof

### Pointwise prefix and complete complement

Retain L948's Q(E,y), w(y)=y^(21/2)(1-y)^(-1/2) and f_(k,l).
C948a(4)-(5) express the signed prefix exactly as

    Q_<=J(8,y)=sum_(k=0)^6 y^(6-k)(1-y)^k F_k(y).

The complete audited Bernstein coefficients of F_k in degree2816
belong to[-M_k,M_k]. Import the normalized Bernstein nonnegativity
and partition of unity on the closed interval from Javier Sanchez-Reyes,
*Algebraic manipulation in the Bernstein form made simple via
convolutions*, Computer-Aided Design35(2003),959-967,
DOI10.1016/S0010-4485(03)00021-6,
[primary paper](https://www.cise.ufl.edu/research/SurfLab/seminar/algebraicmanipulation.pdf),
Sections1.1-1.2,2.1-2.4,2.6, pp959-962, and R. T. Farouki,
*The Bernstein polynomial basis: a centennial retrospective*,
[47-page author deck](https://faculty.engineering.ucdavis.edu/farouki/wp-content/uploads/sites/51/2021/07/Bernstein-polynomial-basis.pdf),
PDF pp12,24-25. These were inspected in assessment102; its unchanged
coverage is reused. In this normalization |F_k(y)|<=M_k everywhere,
including endpoints. These are the exact saved rational maxima, not
their rounded decimal displays.

Import Euler's beta integral, [DLMF5.12.1](https://dlmf.nist.gov/5.12#E1),
with positive arguments35/2-k,k+1/2, and the gamma recurrence and
duplication formulas [DLMF5.5.1,5](https://dlmf.nist.gov/5.5#E5).
They give precisely C948a's

    beta_k=B(35/2-k,k+1/2)/pi
          =(34-2k)!(2k)!/[4^17(17-k)!k!17!],
    P_8=8^17 sum_k M_k beta_k,
    8^17 integral_0^1 w(y)|Q_<=J(8,y)|dy <= pi P_8.            (4)

For each remaining degree l=1412,...,2816, the same beta evaluation
before energy integration gives

    |f_(k,l)| B(l+35/2-k,k+1/2)/pi
       =|d_(k,l)|/[2 C^11 4^k k!(l+17)!].                    (5)

Both beta arguments are strictly positive for every retained k,l.
The singular face is integrable; no endpoint neighborhood is removed.
C948a(10) bounds |d_(k,l)|/C^11 by V_k rho^(-l) for every degree,
using all coefficients of the unchanged kernel and all34 rows.
The signed prefix cancellations are already performed before its
maxima are taken. Absolute rows are used only for the complement.

Set L=1412 and

    q=256/(L+18)=256/1430=128/715<1,
    T_8=8^17 256^L/[(L+17)!(1-q)]
                      *sum_(k=0)^6 V_k/[2*4^k k!].          (6)

Successive terms 256^l/(l+17)! have ratio256/(l+18)<=q for l>=L.
The triangle inequality, (5), the coefficient majorant and a positive
geometric-series extension therefore give

    8^17 integral_0^1 w(y)|Q_>J(8,y)|dy <= pi T_8.             (7)

This pays every degree through2816 and enlarges that finite sum by
positive terms beyond it. There is no series interchange for Q.
The denominator here is(l+17)!, not C948a's integrated(l+18)!;
its ratio256/1431 and integrated bound B are not inputs to this bound.

### Full replacement payment and endpoint in identical units

L948(5), |k-p|<=epsilon and (4),(7) imply

    |J_p(k-p;8)| <= U_1=epsilon*pi_+^6(P_8+T_8).

L948(1) is the complete first-order Taylor remainder, obtained from
[DLMF1.4.35-37](https://dlmf.nist.gov/1.4#E35) applied to the finite
interpolating product in its parameter, with twelve labelled factors
bounded by8 on the whole parameter interval. It pays every term with
at least two residual factors, not only quadratic monomials. Its
integrable simplex domination includes every singular face. Thus

    U_2=66 epsilon^2 8^10*pi_+^6*Z*8^17,
    Z=(293/540)/(2^36*17!),
    |v(8)-v_p(8)| <= U:=U_1+U_2.                            (8)

No exp(4/5), energy-cell mass or integrated allowance enters(8).
The inherited pi_+ encloses pi from above and is positive. Complete
rational calculation gives outward displays

    1.274779338895856e-17 <= P_8 <=1.274779338895857e-17,
    2.189957128649659e-80 <= T_8 <=2.189957128649660e-80,
    1.512354696858995e-67 <= U_2 <=1.512354696858996e-67.       (9)

All3073 coefficients R_l of L938(18) contribute to the exact rational

    c=v_p(8)/pi^6
      =sum_(l=0)^3072 R_l 8^(17+l)/[C^12(17+l)!].            (10)

No high-degree remainder is discarded. The script uses the common
denominator C^12*3089! and checks every factorial division. It finds
c>0 and verifies that it lies in L949's complete last global Bernstein
coefficient interval, since evaluation at the included endpoint1 is
exactly that coefficient. Define v_(p,-)=pi_-^6*c and
v_(p,+)=pi_+^6*c, using the inherited positive pi enclosure.
Then [v_(p,-)-U,v_(p,+)+U] encloses v(8). Exact comparisons give
(1)-(3). This complete interval contains zero. U being too large
does not imply that the actual error is large.

### Execution and independent replay

Reproduce with

    python3 scripts/heat/l938-pointwise-signed-response-104.py
    python3 scripts/heat/check-l938-pointwise-signed-response-104.py

Full exact new constants, endpoint and comparisons are in
`scripts/heat/l938-pointwise-signed-response-104.json`;
the independent report is
`scripts/heat/l938-pointwise-signed-response-check-104.json`.
All3113 producer checks and31 independent replay checks pass, with no
arithmetic failures. The mathematical test is explicitly INCONCLUSIVE.

The replay reconstructs beta masses by odd products, checks uncancelled
beta/gamma factorial cancellation at the first omitted degree for all
seven k, reconstructs the complement factorial by a product and checks
the exact ratio. It recombines the complete pointwise scalar allowance.
It checks(10) by a separate backward integer Horner recurrence: start
u=R_3072,d=1; for l=3071,...,0 put d<-(l+18)d and
u<-8u+R_l d with the new d, then c=u8^17/(d17!C^12).
The nested weights reproduce(10), so this independently checks every
term without the producer's forward factorial-dot-product contraction.
It checks all reported outward displays and both complete endpoints.

Inputs are hash-checked against the inherited audits. Those checks
establish identity and reuse, not a fresh proof of theta production,
prefix multiplication, or the original full polynomial multiplication.
Every new rational comparison is consumed in full by the replay;
bounded JSON previews are not treated as proof. No precision, kernel,
cutoff, nodes, grid, residual sign or mesh is changed.

## Mathlib

Full or supporting Mathlib coverage of this specialized endpoint test
is not checked; unknown coverage is not evidence of absence. Standard
inputs are the precisely cited Taylor, positive beta/gamma and finite
Bernstein identities. The new work is their fixed finite specialization
and arithmetic obstruction, with the qualifications above.
