# C029r — Two positive residues at the fixed p_5 reference poles

## Hypotheses

Use exactly C029n's full finite Kuznetsov family, including every odd
coefficient and the constant normalization

    S=sin(pi/8)/sqrt(2)>0, U=U_6=T_6/S,
    U(t)=sum_(k=0)^6 A_k p_k(t),
    A_k=6!/((6-k)!6^k) beta_k/S,
    (k+1)p_(k+1)=t p_k-(k+1/2)p_(k-1), p_(-1)=0, p_0=1.

The beta_k and finite u_0,...,u_8 formula are those stated and audited
in C029n, from A. Kuznetsov, *Expansion of the Riemann Xi Function in
Meixner–Pollaczek Polynomials*, Canadian Mathematical Bulletin 51(4)
(2008), 561–569, recurrence (2), coefficients (4)/(13), printed
pp563/566 and Jensen weights p568,
[primary source](https://doi.org/10.4153/CMB-2008-055-0).
Import C029n's exact coefficient formulas, degree six and negative
leading coefficient l=[t^6]U. Use only its proved rational enclosures
of pi and sqrt(2), each of width 10^(-60); no precision increase.

Set Q=U/l, P=120p_5, and f=Q/P. For each zero lambda_j of P, ordered
increasingly, define r_j=Q(lambda_j)/P'(lambda_j), after verifying the
five simple real zeros below. The denominator is fixed independently
of U's roots. No root-count or simplicity assumption on U is made.

## Conclusion

P is monic of degree five with five distinct real zeros. All five
residues are nonzero, with signs (-,+,-,+,-). In particular the proposed
condition of at most one positive residue fails: the actual count is
two. The divided-difference kernel of f has exactly two negative squares,
so the approved N_0/N_1 zero theorem cannot be applied to this f.

This rejects the fixed N=6 reference-residue baseline only. It supplies
no lower bound on U's nonreal-zero count and does not refute C029m's
eventual uniform index premise or RH. C029p's audited one-pair numerator
is consistent with this stronger sufficient condition failing. No
isolated-degree or input-precision campaign follows from this result.

## Proof

### Exact reference poles and finite enclosures

The recurrence, retaining all its rational factors, gives

    P(t)=t^5-35t^3+(531/4)t,
    P'(t)=5t^4-105t^2+531/4.

Both Q and P are monic, of degrees six and five respectively; for Q
this uses C029n's l<0 rather than an assumption of full degree.
On the prescribed grid j/16, -256<=j<=256, exact evaluations give
sign-changing brackets

    [-89/16,-11/2], [-17/8,-33/16],
    [33/16,17/8], [11/2,89/16],

and the singleton root 0. All endpoints other than 0 have nonzero
values. The four brackets and singleton are disjoint. The intermediate
value theorem gives five distinct real roots; degree five proves that
these exhaust all roots and each is simple, without assuming simplicity.
Exactly 30 rational bisections in each nonsingleton bracket give the
following complete final brackets; the four nonsingleton brackets
each have width 1/17179869184.

| j | Lower endpoint | Upper endpoint |
| --- | ---: | ---: |
| 1 | -95145986785/17179869184 | -2973312087/536870912 |
| 2 | -17870491601/8589934592 | -35740983201/17179869184 |
| 3 | 0 | 0 |
| 4 | 35740983201/17179869184 | 17870491601/8589934592 |
| 5 | 2973312087/536870912 | 95145986785/17179869184 |

Interval Horner evaluation of P' on these full brackets has signs
(+,-,+,-,+), with no zero-containing denominator. Evaluate every exact
coefficient b_i=[t^i]U in Q(sqrt(2))[pi] using C029n's unchanged rational
input bounds. Enclose [t^i]Q by b_i/l for i<6, and set [t^6]Q=1 exactly.
Horner evaluation over each complete bracket encloses Q(lambda_j).
Multiplication by the reciprocal interval of P' gives the residue.
Every reciprocal is taken only after checking separation from zero;
for [a,b] not containing zero its reciprocal is [1/b,1/a].

The resulting full rational intervals are contained in these outward
rounded enclosures. Every terminating decimal here is an exact rational.

| j | Lower residue bound | Upper residue bound | Sign |
| --- | ---: | ---: | --- |
| 1 | -24371.533 | -24371.532 | negative |
| 2 | 31647.087 | 31647.088 | positive |
| 3 | -11173.747 | -11173.746 | negative |
| 4 | 366.125 | 366.126 | positive |
| 5 | -90.969 | -90.968 | negative |

The interval operations are C029n's exact rational inclusion rules:
endpoint addition, the extrema of all four products, reciprocal on
zero-free intervals, and successive Horner evaluation. Dependencies
between coefficient enclosures can enlarge the result but do not
invalidate inclusion. Evaluating U first and then dividing by l gives
overlapping Q enclosures as a consistency check, not an independent
proof. The full Q-coefficient evaluation is the sign certificate.

Reproduce from this notebook with

    python3 scripts/pollaczek/fixed_pollaczek_residues_2028.py

The complete certificate is `scripts/pollaczek/fixed-pollaczek-residues-2028.json`.
It contains pinned source-input/helper hashes, every finite coefficient,
all 513 grid values, all bisection midpoint values, final endpoint values,
full derivative/Q/residue intervals, outer bounds, signs and failures.
All 44 checks pass, five of five poles and signs are resolved, and the
positive count is 2 against the required maximum 1. All ten full residue
endpoints and all ten derivative endpoints were inspected, not just a
preview. The first development run had a type error before pole work
(it passed exact coefficient polynomials instead of their interval
values to interval multiplication); this was corrected and recorded
in the certificate. No bound failed and no precision changed.

### Kernel orientation and applicability of the inspected theory

Ordinary partial fractions give, with c real,

    f(z)=z+c+sum_(j=1)^5 r_j/(z-lambda_j).

The linear coefficient is +1 because both polynomials are monic with
degree difference one. Subtracting these principal parts leaves a
polynomial; matching infinity gives the displayed linear part, including
its real constant. In particular no polynomial contribution is omitted.
For nonreal z,w, away from the poles,

    K_f(z,w)=(f(z)-conj(f(w)))/(z-conj(w))
      =1-sum_(j=1)^5 r_j/((z-lambda_j)(conj(w)-lambda_j)).

The expression extends at a removable diagonal argument. Indeed
(1/(z-lambda)-1/(conj(w)-lambda))/(z-conj(w))
=-1/((z-lambda)(conj(w)-lambda)); this fixes the residue sign.
Thus every finite kernel matrix is V D V*, with evaluation columns
1 and 1/(z-lambda_j), and

    D=diag(1,-r_1,-r_2,-r_3,-r_4,-r_5).

D has four positive and two negative entries, none zero. Consequently
every such matrix has at most two negative eigenvalues: a subspace
on which its form is negative definite maps injectively under V* to
a negative subspace for D. Attainment also holds. At the six distinct
upper-half-plane points i,2i,...,6i, V is invertible. A vanishing linear
combination of its columns, multiplied by P, would be a polynomial of
degree at most five with six distinct zeros. It is identically zero.
Evaluating that identity at each lambda_j forces its pole coefficient
to vanish since P'(lambda_j)!=0; the constant coefficient then vanishes.
Congruence by this invertible V gives exactly two negative eigenvalues.
This verifies both parts of the negative-square definition, not merely
an upper bound.

The cited convention and definition are H. Langer, A. Luger and
V. Matsaev, *Convergence of generalized Nevanlinna functions*, Acta
Sci. Math. (Szeged) 77 (2011), 425–437, Definition 1.1, pp426–427,
[primary text](https://acta.hu/download.phtml?id=3148).
Here f is rational, meromorphic off R and satisfies real symmetry.
The finite calculation therefore places it in N_2, rather than N_0 or
N_1. This is a routine application of the definition; no general
zero theory is reproved.

For the proposed threshold, the same finite kernel computation would
instead give N_0 if there were no positive residues, or N_1 if exactly
one were positive; zero residues would be omitted as cancelled real
poles. In the former case K_f(z,z)>=1, so Im(f(z))=Im(z)K_f(z,z)>0
in the upper half-plane, excluding zeros there. In the latter case the
known one-negative-square theorem gives at most one upper-half-plane
zero, which is simple: H. de Snoo, H. Winkler and M. Wojtylak,
*Zeros of nonpositive type of generalized Nevanlinna functions with one
negative square*, arXiv:1011.2081v1 (9 November 2010), introduction,
(1.1)–(1.4), Theorem 2.2 and Corollary 2.3, manuscript pp1–5,
[primary text](https://arxiv.org/pdf/1011.2081v1).
Import that theorem as stated, without reproof or claiming an audit
of its upstream references [3–5]. Numerator simplicity is not an input.
P has only real zeros, so division by P cannot cancel any nonreal zero
of Q. This explains the plausible one-pair use of the screen, but its
sign hypothesis fails here and that theorem is not applied to f.

No all-degree sign law, actual-degree control for varying N,
initialization, or qualified weighted compact-convergence/upstream[9]
claim in C029m is resolved. The identity-bulk obstruction C029n and
affine-quotient obstruction C029q are contrasts, not residue premises.
The result is a local informative negative under known theory, not a
discovery beyond the sources checked or an RH candidate.

## Mathlib

Full matching Pollaczek/coefficient, residue and negative-square theorem
coverage was not checked. No absence claim is made. The finite rational
certificate and the explicit applicability argument above provide the
local specialization; the general zero theorem is imported by citation.
