# Lemma 950: the fixed negative-row Chernoff outer allowance is too large

## Hypotheses

Use L019's exact positive theta kernel and L938's exact continuous
density v=sum_alpha c_alpha h_alpha, with precisely its34 rows,
twelve labelled factors, factorials and retained M_0^12 normalization.
Write A_k(lambda)=integral_0^infinity u^(2k)exp(lambda u²)K(u)du/(2k)!,
0<=k<=6. Keep tilt1/10, Chernoff increment1 and energy boundary8.
Use L949's compact certificate and L947's positive margin
m=8.935649629627030e-35. Its exact compact allowance is B, with
0<B<m; the exact available budget is m-B, not a rounded display.

The numerical enclosures use L037's directed Decimal arithmetic,
correctly rounded nearest exponential widened to adjacent values,
precision200 in all three contexts, rejected exceptional arithmetic,
and exact Python integers/Fractions. Their implementations are contracts,
not independently formally verified. L949's original theta inclusion,
integer-polynomial, derivative-prefix and arithmetic contracts remain
inherited for the interpretation of m-B. No RH, density sign,
effective eventual-sign onset, contact or global crossing premise is used.

## Conclusion

Define the exact fixed Chernoff cost

    T=exp(-8) sum_(c_alpha<0) |c_alpha|
                         product_(k=0)^6 A_k(11/10)^alpha_k.       (1)

Under the numerical contracts,

    9.712929659838274e-28 <= T <= 1.270291157126160e-27,
    10869864.04170784 <= T/(m-B) <= 14215991.11176411.             (2)

The imported positive-measure bound gives

    integral_8^infinity exp(E/10)max(-v(E),0)dE <= T.             (3)

Thus this fixed upper-allowance method stops: even its exact cost
exceeds m-B by more than ten million. This is an informative limitation
of the prescribed certificate. It supplies no lower bound on the actual
negative mass. In particular it neither refutes B_4<m nor resolves
global variation, parameter signs, contacts, other degrees,
initialization, realization or actual-Xi all-degree mixed positivity.
This is a reproduction/specialization of known methods, not progress
beyond those methods or a new general probability theorem.

## Proof

### Imported Chernoff bound and exact positive-row specialization

Import Boyd and Vandenberghe, *Convex Optimization*, Cambridge2004,
corrected seventh printing2009,
[author-hosted book](https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf),
Sections7.4.1,pp374-375 and7.4.2,pp379-380, especially(7.20), with
the nonnegative exponential parameter and indicator-majorant cases
inspected in assessments85/94. This bound is imported, not reproved.

For each row, exp(E/10)h_alpha(E)dE is a finite nonzero positive
measure: L019 gives positivity and L938(6)-(10) give finiteness,
nonzero factor masses and the convolution transform. Normalize by
its mass Z_alpha=product A_k(1/10)^alpha_k. Apply the cited bound
to the energy random variable, threshold8, parameter1. Its exponential
expectation is product A_k(11/10)^alpha_k/Z_alpha. Multiplying back
by Z_alpha leaves exactly the corresponding row of(1). All moments
are finite by L058/L938, so normalization and the expectation are
legitimate. There is no multinomial factor and no removal of A_0 powers.

Pointwise max(-v,0)<=sum_(c_alpha<0)|c_alpha|h_alpha, since every
h_alpha is nonnegative. Integrating this finite inequality and summing
the row bounds proves(3). Signed v is never a probability measure.
The continuous densities have no atoms; including the endpoint8
does not affect the integral. The compact component remains separately
paid by B in L949. An oversized T cannot decide the actual integral.

### Fixed finite interval integration

Import direct real interval-box inclusion from Fredrik Johansson,
*Numerical integration in arbitrary-precision ball arithmetic*,
[arXiv:1802.07942v1](https://arxiv.org/pdf/1802.07942v1),
22February2018, Sections2,2.1,3.2,printed pp2-4,6, as inspected
in assessment94. No complex ellipse or Gaussian quadrature is used.
Requested tolerance is not evidence; every finite box and omitted
contribution is included below. Use L037's existing interval operations.

Partition[0,4] into4096 boxes J_j=[j/1024,(j+1)/1024]. On each
box evaluate, by enclosing interval arithmetic,

    x=exp(2u), v_n=pi n² x,
    K_8(u)=sum_(n=1)^8 4v_n(2v_n-3)exp(u/2)exp(-v_n),
    g_k(u)=u^(2k)exp(11u²/10)K_8(u)/(2k)!.

L019 gives this positive factorization, with v_n>=pi>3. Each
computed lower summand endpoint is positive. Multiply the enclosing
range of g_k by the exact width1/1024 and sum all4096 contributions.
The functions are continuous on these boxes, including u=0,k=0;
there is no energy-coordinate singularity in this integration.
The actual kernel has additional positive theta terms, so the finite
integrals give lower moment bounds. Their upper bounds must be
augmented by both following tails.

### Complete omitted-theta and infinite-u contributions

For n=9+j, j>=0, induction using ((n+1)/n)^4<= (10/9)^4<2
gives n^4<=9^4 2^j. Also n²>=81+19j. Drop the negative part of
each L019 summand. On0<=u<=4, exp(2u)>=1 and exp(9u/2)<=exp(18),
so the entire omitted kernel is at most

    D=8pi² exp(18)9^4 exp(-81pi)/(1-2exp(-19pi)).             (4)

The geometric ratio lies strictly between0 and1. Since u^(2k)<=4^(2k)
and exp(11u²/10)<=exp(88/5), the omitted finite-interval moment is
at most

    d_k=4 D 4^(2k)exp(88/5)/(2k)!.                           (5)

For the infinite u-tail use L058's explicit domination, with
L=11/10,R=0,p=2k and

    q=exp(-pi),
    C=8pi²(1+11q+11q²+q³)/(1-q)^5.

The cutoff4 satisfies4>=max(1,3*(33/5)/(2pi)). L058 therefore
bounds the full weighted kernel u^(2k)exp(11u²/10)K(u) by
C(2k)!exp(-(pi/2)exp(2u)) on u>=4. Dividing by the moment
factorial cancels (2k)!; this applies to every0<=k<=6, including0.
Convexity gives exp(2u)>=exp(8)(1+2(u-4)) for u>=4. Integrating
the resulting decreasing exponential bounds the full moment tail by

    d_infinity=C exp(-(pi/2)exp(8))/(pi exp(8)).              (6)

This specializes L058's explicit majorant, not L035's inapplicable
unheated five-moment tail. Formula(4) treats only0<=u<=4; formula(6)
uses the full infinite theta series on the remaining half-line, so
no contribution is omitted or counted as a favorable negative error.
Certified upper endpoints give d_k<2e-88 for every k and
d_infinity<4.193e-2036. Their complete positive enclosures are saved.

### Moment enclosures and restored cost

Combining every finite box with[0,d_k]+[0,d_infinity] gives these
outward enclosures for the actual factorial-normalized A_k(11/10):

| k | lower | upper |
|---:|---:|---:|
|0|0.5203999178740316|0.5282800948641874|
|1|0.01314702001689725|0.01348790669483165|
|2|0.0001531221594145505|0.0001579641092372177|
|3|0.000001109872989078539|0.000001150485775504816|
|4|5.687564582450766e-9|5.921537557286264e-9|
|5|2.213791685139544e-11|2.314283716385676e-11|
|6|6.855159935113471e-14|7.194053365842368e-14|

The computation uses the complete200-digit endpoints, not this display.
All positive powers, all twelve factors and all18 negative rows enter
(1). The exact L938 table is checked against all34 source rows, with
sum alpha_k=12 and sum k alpha_k=12 for every row. The positive rows
are omitted only in the upper bound(3). Exact rational products of
the endpoint values independently check each directed row evaluation,
and their complete rational sums check the final enclosing Decimal
evaluation of T. Applying the interval for exp(-8) yields(2).
The lower endpoint concerns T itself, not the left side of(3).
Thus tighter moment quadrature alone cannot make this fixed cost fit.

The exact rational budget is loaded from
`scripts/heat/l938-compact-negative-mass-94.json`,
`/exact/unused_margin`, in full. The script checks m against L947's
exact decimal, B against C948a's audited complete bound and its
producer, L949's zero compact polynomial allowance, and the identity
unused_margin=m-B. It also checks kernel/producer identity hashes.
Hashes provide input consistency, not an independent audit of the
inherited compact computations. The strict comparison uses exact
Fractions before any outward display.

### Reproduction and verification scope

Run `python3 scripts/heat/l938-fixed-outer-tail-96.py`.
Full certificate: `scripts/heat/l938-fixed-outer-tail-96.json`.
Every finite kernel enclosure and all28672 moment contributions are
in `scripts/heat/l938-fixed-outer-tail-boxes-96.json`.
All61529 checks pass, with no failures. They include all32768 positive
theta summands, all finite contributions, complete rational resumming
of the stored boxes for every moment, all18 exact endpoint products,
the full cost and exact margin comparison. Both omitted-tail formulas
are justified above; the complete moment/tail enclosures were inspected.
The implementation inherits the documented arithmetic contracts and
does not claim an independent conceptual audit or formal verification.

No exponent, split, kernel, compact certificate or moment-grid campaign
was performed. C947b's earlier unsigned compact-error stop is preserved
at its original scope. L939's audited eventual positivity still has
no effective onset at8. A different cancellation-preserving mechanism
needs its own coverage before further mathematics.

## Mathlib

Full and supporting Mathlib coverage of this particular heated-moment
and outer-tail certificate is not checked; unknown coverage is not
evidence of absence. The general probability and validated-integration
methods are imported by the precise citations above; the local content
is their qualified numerical specialization and its negative outcome.
