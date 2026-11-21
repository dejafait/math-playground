# C029p — Full tilted T_6 has derivative-Bezoutian inertia (5,1,0)

## Hypotheses

Use precisely C029n's full Kuznetsov T_6, including all odd coefficients,
normalization S=sin(pi/8)/sqrt(2)>0, and U=T_6/S. Its exact coefficient
formula, Bernoulli convention, recurrence and actual degree six are those
stated and audited in C029n. The primary input is Alexey Kuznetsov,
*Expansion of the Riemann Xi Function in Meixner-Pollaczek Polynomials*,
Canad. Math. Bull. 51(4) (2008), 561–569,
[DOI](https://doi.org/10.4153/CMB-2008-055-0), recurrence (2), coefficients
(4)/(13), pp563/566, and weighted truncation pp568–569. No numerical root
observation or weighted infinite-series convergence claim is imported.

Use the exact real symmetric matrix B of C029o, with no bulk support
restriction, defined by

    Phi(x)^t B Phi(y)=(U(x)U'(y)-U(y)U'(x))/(x-y),
    Phi=(p_5,p_4,p_3,p_2,p_1,p_0)^t,
    (k+1)p_(k+1)=t p_k-(k+1/2)p_(k-1), p_0=1, p_(-1)=0.

The evaluation comrade C, scaled matrix A=D^(-1)CD and positive D are
those of C029n/C029o. In particular

    D^2=diag(693/256,315/128,35/16,15/8,3/2,1), G=DBD.

For the finite calculation use exactly C029n's audited closed rational
pi and sqrt(2) enclosures of width 10^(-60), with its Machin/isqrt
containment proof. No precision refinement, simplicity, nonzero minor
or negative-index assumption is made.

## Conclusion

The six leading principal minors Delta_j of B have signs

    (+,+,+,+,+,-).

Consequently B and G have inertia (positive,negative,zero)=(5,1,0).
They are nonsingular and G satisfies A^t G=GA. In the standard
derivative-Bezoutian interpretation, U has four distinct real roots and
one nonreal conjugate pair, all six roots simple. Positive scaling by S
gives the same roots for T_6.

This is one finite, known-method reproduction. It retains negative
index<=1 only at N=6. It establishes no eventual bound, no weighted
compact convergence, no actual-Xi positivity and no RH implication.
Independent audit2019 checks the source applicability, complete finite
construction and every stored arithmetic endpoint. This validates the
existing finite reproduction, without claiming a new theorem or an
eventual-family estimate.

## Proof

### Exact matrix and unchanged inputs

C029n proves that U has actual degree six and that both rational input
intervals contain their intended constants. C029o constructs B exactly
over (Q[s]/(s^2-2))[X], specialized at s=sqrt(2), X=pi, and proves its
symmetry, defining kernel and C^t B=BC orientation. Its descending basis
has nonzero rational leading coefficients 1/k!, so no basis singularity
is assumed away. This imports the construction rather than asserting a
new general symmetrizer theorem.

For this calculation every stored entry was reconstructed using
C029o's division-free monomial kernel formula, followed by the rational
conversion t^i=sum_k R_ik p_k and reversal to Phi. All 36 exact entries
agree with the original certificate; all 49 coefficients of the kernel
identity and all 36 entries of symmetry were checked. With alpha=A_6
(the coefficient of p_6 in U), the reconstructed cleared evaluation
comrade alpha*C agrees with C029o, and all 36 coefficients of
(alpha*C)^t B=B(alpha*C) agree. Here alpha<0 by C029n; clearing it
does not assert a possibly invalid division. The positive squared D
entries satisfy the five adjacent symmetrizing relations from C029n.
Thus the stored matrix and its orientation have not been changed to
obtain favorable signs. The construction check reuses the existing
exact polynomial helpers and is not an independent audit of C029o.

Pinned SHA256 values of the two input certificates are

    tilted-boundary-metric-2010.json:
    361e31b72ad348b17f6c2ac785c20f5ab73e27796025bd724af208543e0feaf7
    tilted-bezoutian-n6-2014.json:
    6870f303d2fa8bd6ec5bd9fcde2a197d6c9987f98b6bccf048a378f3ccdedd47

The new certificate additionally pins both imported helper scripts.
The previous expanded-determinant Horner failure is preserved in C029o;
it concerned a different enclosing expression, not the exact minors.

### Entry intervals and the complete finite determinant expressions

Import the interval inclusion rules of S. M. Rump, *Verification methods:
Rigorous results using floating-point arithmetic*, Acta Numerica 19
(2010), 287–449, [corrected author PDF](https://www.tuhh.de/ti3/paper/rump/Ru10.pdf),
Sections5–5.2, (5.1)/(5.4)–(5.9), Section5.5, (5.16)–(5.17) and its
successive-application justification; Section6, (6.1)–(6.2), explains
dependency overestimation. These are finite closed real intervals and
enclosing additions/multiplications. Exact Fraction endpoints suffice;
there is no interval division, overflow or rounding premise to pay.
Repeated use of the same pi/sqrt(2) parameters may enlarge the enclosure
but does not require statistical or algebraic independence.

For every one of the 36 entries, enclose a coefficient a+b*sqrt(2) with
the correct sign of rational b, then evaluate its X-polynomial by
interval Horner at the fixed pi interval. Denote the resulting closed
interval by I_ij, so B_ij belongs to I_ij. These entry intervals are
formed before any determinant arithmetic. For j=1,...,6 evaluate exactly

    J_j=sum_(sigma in S_j) sgn(sigma) product_(i=0)^(j-1) I_(i,sigma(i)),

using enclosing interval products and sums, with sign obtained by
inversion parity. The finite Leibniz definition and the cited inclusion
rules give Delta_j in J_j. All j! permutations are retained, including
their unsigned and signed exact product intervals, without term dropping
or symbolic determinant expansion. The total is 873 terms. No pivot,
zero-minor rule, approximate root or limiting interchange is used.

The following are rational outer bounds for the computed J_j. Each
decimal denotes the exact terminating rational shown, and the last
column multiplies both endpoints. Complete unrounded J_j endpoints,
not these outer bounds, were used by the script for sign decisions.

| j | Lower | Upper | Multiplier |
| --- | ---: | ---: | ---: |
| 1 | 1.332652 | 1.332653 | 10^(-7) |
| 2 | 1.024767 | 1.024768 | 10^(-12) |
| 3 | 2.168268 | 2.168269 | 10^(-16) |
| 4 | 1.704970 | 1.704971 | 10^(-19) |
| 5 | 2.250491 | 2.250492 | 10^(-22) |
| 6 | -3.178327 | -3.178326 | 10^(-24) |

Every displayed outer interval excludes zero. The first five exact
lower endpoints are positive and the last exact upper endpoint is
negative; hence all six minors are nonzero with the asserted signs.

The full calculation is reproducible from this notebook by

    python3 scripts/pollaczek/tilted_bezoutian_entrywise_2017.py
    python3 scripts/pollaczek/tilted_bezoutian_entrywise_check_2017.py

The first writes `scripts/pollaczek/tilted-bezoutian-entrywise-2017.json`,
containing the full matrix coefficients, 36 exact entry intervals,
every signed permutation product, six exact endpoints, signs, input
hashes and all 34 construction/reporting checks. All pass without
failures. The second reads this complete certificate and uses a separate
Fraction implementation to recompute all 36 entry intervals, every
permutation's parity and product, the six complete sums, and their exact
outer-bound comparisons. All 873 terms and all 79 checks pass. Its full
check record, input-certificate hash and exact rational outer bounds are
in `scripts/pollaczek/tilted-bezoutian-entrywise-check-2017.json`.
The six load-bearing outer bounds and complete check fields were
inspected with the shared JSON inspector. No truncated raw-endpoint
preview or pass banner is used as mathematical evidence: the checker
compares every raw endpoint exactly, and the small rational outer bounds
give the strict inequalities used here. This is arithmetic consistency
checking, not formal verification or an independent source audit.

### Inertia, root interpretation and scope

Apply Jacobi's theorem in Michel Coste, *An Introduction to Semialgebraic
Geometry* (October2002), Section1.4.2 p19,
[primary notes](https://perso.univ-rennes1.fr/michel.coste/polyens/SAG.pdf).
Its hypotheses are a real symmetric matrix and every leading principal
minor nonzero. B is real symmetric by construction and the six bounds
pay the nonvanishing hypotheses. There is precisely one sign change in
(1,Delta_1,...,Delta_6), and Delta_6!=0. Thus B has one negative, five
positive and zero null eigenvalues. Since D is real invertible,
Sylvester's law of inertia gives the same inertia for G=DBD, and the
already paid orientation yields

    A^t G-GA=D(C^t B-BC)D=0.

For the optional root interpretation import G. Heinig and K. Rost,
*Bezoutians*, Chemnitz2008-09,
[primary preprint](https://www.tu-chemnitz.de/mathematik/preprint/2008/PREPRINT_09.pdf),
Example7.2 p40, Proposition7.15/(7.11) p45 and Theorem10.4 with the
repeated-root discussion pp59–60. The square congruence (7.11) applies
to degree-six U and degree-five U'; its order is (U,U'), agreeing with
the kernel above. Changing the order would negate the form. The
invertible degree-graded basis conversion is also a congruence. These
results identify inertia with the Newton-sum Hermite form, without
assuming simplicity: for r distinct real roots and c distinct nonreal
conjugate pairs it is (r+c,c,6-r-2c), as also covered by Coste
Theorem1.14 pp17–18 and its proof. Therefore c=1, r=4 and nullity zero
certifies six distinct roots, hence simplicity at degree six. The
singular-case distinction between distinct pairs and algebraic
multiplicity is not suppressed; nonsingularity was proved first.

The root count agrees with the source's numerical N=6 observation but
provides a local finite certificate by a known method. It is not new
theory beyond the sources checked. The eventual uniform index premise
in C029m, the qualified upstream[9]/weighted compact convergence and
the actual-Xi all-degree mixed positivity gap L030–L032/C032a remain
unproved. Neither the boundary-metric stop nor the expanded-Horner stop
is reversed: this unrestricted-bulk matrix and enclosing expression are
different. There is no automatic degree or precision escalation and no
RH candidate.


### Independent application audit2019

The approved scope is exactly assessment2017, separately approved in
step2018: N=6, every odd coefficient, and the unchanged input intervals.
Reuse the complete primary extraction in review2001 and the theorem/proof
comparisons2013/2015, with the Heinig–Rost proof cases rechecked in
approval2018. No fresh source-access claim is made. Comparing those
recorded formulas with the Hypotheses above finds no changed phase,
basis parameter, Jensen weight or coefficient normalization. In
particular u_n/S has phase factors 1,1+sqrt(2),-1,-1-sqrt(2), in that
order; beta_6 uses u_4,u_6,u_8 with coefficients 120,367,255. The n=0,1
negative-index terms are omitted. U'=sum_(i=0)^5 (i+1)b_(i+1)t^i has
actual degree five because b_6=A_6/720!=0.

A separate implementation imports only Python standard-library modules,
not the earlier mathematical helpers. It reconstructs every u_n,
beta_n, Jensen coefficient and basis polynomial in sparse
Q[X,s]/(s^2-2). Rather than reconstructing B by the original kernel and
basis-inversion routines, it expands the **stored** B in Phi(x),Phi(y)
and checks all 49 coefficients of

    (x-y)Phi(x)^t B Phi(y)=U(x)U'(y)-U(y)U'(x).

It also checks all 36 monomial/basis inverse relations, all 42 cleared
evaluation-comrade coefficients and all 36 entries of the cleared left
metric identity. This establishes that the unchanged certificate is for
the specified polynomial and kernel, rather than just a matrix with the
desired signature. Uniqueness follows from the invertible degree-graded
basis, as in C029o. All stored polynomial coefficients are compared
exactly, not by evaluating selected sample points.

The sign convention can also be checked directly in the defining
identity: the coefficient of x^6 on its right is b_6 U'(y), so the
coefficient of x^5 in the quotient is b_6 U'(y). Since p_5 has leading
coefficient 1/120, this gives e_1^t B Phi=(A_6/6)U'. The audit checks all
six coefficients of this row identity. Substitution in the two cleared
comrade identities cancels the kernel numerator with this same sign,
yielding C^t B=BC; it does not yield the reversed right-metric identity.
The five positive adjacent squared-D ratios reconstruct precisely the
stated D^2, so G=DBD, not D^(-1)BD^(-1), is the left metric for A.
This is the finite orientation applicability check, not a reproof of the
cited general-basis theorem.

The independent implementation checks the complete 48-term arctangent
sums/remainder bounds, their Machin interval, the exact input containment
and strict squared sqrt(2) inequalities. C029n's analytic Machin branch
argument is retained: the angle has tangent 1 and lies in (0,pi/2),
using the stated integral inequalities, not just a tangent equality.
It reconstructs all 36 entry intervals. For each j it checks that the
stored permutations are exactly S_j without duplicates, recomputes
every inversion parity and each unsigned/signed product interval, and
compares every complete raw sum endpoint. Thus all 873 terms are read
and checked. Exact rational comparisons put all six raw intervals
inside the displayed outer bounds above, with the five strictly
positive lower bounds and strictly negative last upper bound. The
original expressions and 60-decimal inputs are unchanged.

Reproduce from the notebook with

    python3 scripts/pollaczek/tilted_bezoutian_independent_audit_2019.py

All 82 checks pass with no failures. Complete raw endpoints, every
permutation-term comparison, six outer-bound comparisons and SHA256
values of the three input certificates are saved in
`scripts/pollaczek/tilted-bezoutian-independent-audit-2019.json`.
The original coefficients/certificates and failed expanded-Horner
calculation are preserved. This is an independently implemented exact
arithmetic audit, not a formal proof-assistant verification.

Finally, Jacobi applies to the actual real symmetric B because all six
leading minors are nonzero; their sequence, preceded by 1, has exactly
one sign change. There is no singular-minor convention in use. In the
Heinig–Rost square congruence (7.11), take denominator U of degree six
and numerator U' of degree five, with ratio U'/U at infinity. The
matrix B(U,1) is invertible for the proved nonzero leading coefficient;
there is no assumption that U and U' are coprime at this stage. The
basis change is invertible as already checked. Consequently B has the
same inertia as the six-dimensional Newton-sum Hermite form by the
cited congruence, including repeated-root cases. The imported
rank/signature theorem gives rank=r+2c and signature=r, with r distinct
real roots and c distinct conjugate pairs. Here rank=6 and signature=4,
so r=4,c=1. Six distinct complex roots exhaust the degree, proving
simplicity only after nonsingularity, as required. Scaling by S>0
changes no root. The nonreal pair is a root pair of an approximant,
not an off-line zeta zero.

No mathematical correction to C029p was required. This completed audit
adds reliability to the finite input, not progress beyond the source
root-count theory. C029m's eventual index premise and qualified weighted
compact convergence, including upstream[9], remain unproved. The main
actual-Xi all-degree gap is unchanged. No degree/precision escalation,
new lemma, new source theorem or RH candidate results from this audit.

## Mathlib

Full matching finite certificate, polynomial construction, Jacobi and
derivative-Bezoutian/Hermite coverage were not checked in Mathlib. No
absence or formalization claim is made. The named source theorems are
imported; the finite exact application is the reproduced work here.
