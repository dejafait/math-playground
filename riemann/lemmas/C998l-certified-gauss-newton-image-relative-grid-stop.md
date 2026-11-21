# C998l: Image-relative Newton conversion exhausts a fixed Gauss grid

## Hypotheses

Consider precisely the prescription saved before execution in
`drafts/2026-11-13-certified-gauss-newton-working-690.md` and implemented
by `scripts/separation-seven/certified-gauss-newton-690.py`. Its target
is all nodes AND weights of the degrees63,81,117 Gauss-Legendre rules,
separate interval radii<=2^-512 and complete setup work<=5000000 in
the scalar convention of C998g. This convention and the possible use
in a shared endpoint-bank square service are context, not positivity
or operator inputs to the stop below. No coefficient archive is used.

Use P_0=1,P_1=x with Bonnet's recurrence and D=2^640. The initial
positive mesh is x_j=1-j^2/16384, j=0,...,127, in descending order.
Require exactly(N-1)/2 sign-change brackets, then perform16 sign
bisections per bracket and at most12 Newton updates. Every polynomial
point evaluation is an exact rational calculation. The zero root and
reflection are specified separately. The prescription stops immediately
on a failed safeguard, rather than continuing other roots or degrees.

For X=[l,u] contained in(0,1), put m=(l+u)/2,r=(u-l)/2 and

    M=min{(N-1)N(N+1)(N+2)/8, 4N^2/(1-u^2)^2},
    d=P'_N(m), [d_-,d_+]=[d-Mr,d+Mr].                  (1)

Require0 notin[d_-,d_+]. Form the full interval-Newton image
I=m-P_N(m)/[d_-,d_+], and J=I intersect X, requiring positive width.
To convert J to grid endpoints, binary-search its center c within X:
halve a current dyadic cell[A,B] containing c while B-A>width(J).
On termination expand to[A-h,B+h], h=B-A, and intersect with X.
Require strict contraction. Every halving must remain exactly on
the D grid. There is no alternative stopping condition based on
the requested output tolerance, and no precision increase.

Once a converted node interval has width<=2^-550, recompute(1) on
that interval and enclose its weight by the derivative formula below.
Both radii are checked independently. Outputs are exact rational
intervals; a floating or fixed-point weight conversion is not assumed.

The invocation-start SPECIALIZE assessment687 and source-notes688
cover these techniques. Import Johansson--Mezzarobba, *Fast and rigorous
arbitrary-precision computation of Gauss-Legendre quadrature nodes and
weights*, arXiv:1802.03948v1,12February2018, Section1(1),(3),
Section2(5), Proposition3(7), printed pp1,4-5,
[primary PDF](https://arxiv.org/pdf/1802.03948v1).
The simple-root count is also the standard orthogonal-polynomial
theorem in [DLMF18.2(vi)](https://dlmf.nist.gov/18.2#vi), with its
positive unit weight on(-1,1). Import root preservation under scalar
interval Newton from Alefeld--Claudio, *The basic properties of interval
arithmetic, its software realizations and some applications*,
Computers & Structures67(1998),3-8, Section5 Theorem2 and scalar case,p6,
[primary PDF](https://na.math.kit.edu/alefeld/download/1998_The-basic_properties_of_interval_arithmetic_its_software_realization_and_some_applications.pdf).
No asymptotic seed, unconditional convergence schedule, finite source
work bound, or reproof of those general theorems is used.

## Conclusion

This exact prescription stops on the sixth Newton update of the second
positive root in descending order for N=63. Its incoming node interval
has dyadic depth534 and width in(2^-523,2^-522], so the separate
width<=2^-550 output gate has not yet been met. The intersected Newton
image has positive width in(2^-1034,2^-1033]. After106 conversion
halvings the depth is640, the cell width is

    3645*2^-640 in(2^-629,2^-628],                       (2)

and another halving is demanded. Its midpoint is not on the D grid.
Thus the specified safeguard fails before all-node completion.

Before that stop the first positive root and its reflected root have
node radii<=2^-579 and weight radii<=2^-575, separately. These two
completed nodes do not establish the requested261-node/weight setup.
The exact zero-node weight is not reached, nor either other degree.
The ledger counter at the stopped prefix is183800<5000000; this is
not a complete setup-work bound or an independently audited cost claim.
No budget excess, universal Newton obstruction, bank feasibility,
complete square-service error, signed S3 comparison or RH claim follows.

## Proof

All relevant arithmetic is rational. To evaluate points a/D, the
construction uses the scaled source recurrence

    Q_k=k!D^k P_k(a/D), Q_0=1,Q_1=a,
    Q_(k+1)=(2k+1)a Q_k-k^2 D^2 Q_(k-1).              (3)

Substitution into Bonnet's recurrence gives(3) exactly. This scaling
is an implementation specialization, not a new Legendre theorem.
An unscaled exact-rational Bonnet recurrence separately checks every
recorded mesh value, bisection value, accepted Newton point, final
weight evaluation and failing Newton point. It checks complete exact
values, not approximate signs or a preview of the certificate.

For N=63 all128 positive mesh values are nonzero, and the complete
mesh gives31 disjoint sign-change brackets. Continuity gives one root
in each. Parity gives a reflected negative root for each and the zero
root. The imported degree63 simple-root theorem then accounts for all
63 roots, so each positive bracket contains precisely one root.
The16 checked bisections retain opposite signs in each bracket started.
No claim that the mesh works for81 or117 is made: those degrees are
not reached. Completeness at63 is enough to identify this failure.

The point derivative is evaluated exactly by source equation(5),

    P'_N(m)=N[P_(N-1)(m)-mP_N(m)]/(1-m^2).

Its denominator is positive on every used interval. Proposition3(7)
bounds |P''_N| by the first entry of(1), including endpoints, and
by 2^(5/2)N^(3/2)/[sqrt(pi)(1-x^2)^(5/4)] in the interior.
For0<=x<=u<1 the latter is at most4N^2/(1-u^2)^2:
2^(5/2)/sqrt(pi)<4, N^(3/2)<=N^2, and0<1-u^2<=1.
Thus(1) bounds the derivative throughout X by the mean-value theorem.
The replay checks exclusion of zero for every division. Polynomial
smoothness and the existing bracket supply the other scalar Newton
hypotheses. Root preservation therefore applies at each accepted update
and to the exact image of the failed update; existence is not inferred
from an unchecked contraction or a floating approximation.

The conversion search retains c in[A,B]. If it terminates, its last
cell width h satisfies width(J)/2<h<=width(J), so J, whose radius
is width(J)/2, lies in[A-h,B+h]. Intersecting with X preserves its
root. All10 accepted conversions before failure are checked exactly,
including strict contraction, endpoint continuity and grid depth.
The first root's final derivative interval is also recomputed on its
final node interval. For X=[l,u] positive and its derivative interval
[d_-,d_+] excluding zero, its weight is enclosed by

    [2/((1-l^2)max(d_-^2,d_+^2)),
     2/((1-u^2)min(d_-^2,d_+^2))].                    (4)

This is the imported weight formula with positive denominator and
monotone interval bounds. The complete endpoints, both separate radii
and the reflected outputs are checked. The dyadic bounds on those
radii in the Conclusion are exact inequalities, not decimal estimates.

For the second root, five updates are accepted after its16 bisections.
On update6, the replay reconstructs(3), (1), both endpoints of I and
the intersection J. It verifies the image-width and incoming-width
inequalities in the Conclusion by exact integer comparisons. Replaying
all106 required conversion halvings gives the failed cell(2). Its
lower grid index is even and its upper index odd; their difference
is the odd integer3645. The exact midpoint consequently has a
half-integral grid index. The positive image width is still less than
the cell width, so the prescribed loop requests this unavailable
midpoint. The depth guard refuses it. This proves the stated stop,
independently of whether an alternative enclosure at coarser accuracy
would already suffice for the intended output. Changing that rule is
a different prescription, which has not been tested here.

Full construction evidence is
`scripts/separation-seven/certified-gauss-newton-690.json`; the unchanged
first run is retained in `scripts/separation-seven/certified-gauss-newton-first-run-690.json`.
The diagnostic rerun adds failure serialization only; the full prior
rows, guard counts and ledger are exactly equal. The complete relevant
unscaled replay is `scripts/separation-seven/certified-gauss-newton-replay-690.json`,
with3051 exact checks and no failed check. It does not certify the
completeness of the scalar ledger or any unexecuted computation.

Reproduction from this notebook:

    python3 scripts/separation-seven/certified-gauss-newton-690.py
    python3 scripts/separation-seven/certified-gauss-newton-replay-690.py

The decision is to abandon this uncapped image-relative conversion on
a fixed640-bit grid. A future output-tolerance cap is an unproved
continuation within the assessed finite-inclusion technique, not a
retroactive repair or a general convergence claim. C998k's distinct
fixed-bisection stop and all earlier service stops are preserved.
Independent inverse debt, signed S3, higher/mixed signs, C744q/H2,
non-neutral and source-to-Xi assembly gaps remain open.

## Mathlib

Full matching coverage for this finite prescription, its trace and
conversion stop has not been checked. Supporting rational arithmetic,
Legendre polynomials or interval facts would not alone certify this
service. Unknown coverage is not evidence of absence. The source
theorems above are imported with their stated qualifications.
