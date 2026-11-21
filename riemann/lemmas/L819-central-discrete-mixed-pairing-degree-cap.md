# Lemma 819: central discrete/mixed matching has degree at most 151

## Hypotheses

Use L791's exact shift-zero ratios q_k=R_(k+1)^2/(R_k R_(k+2)), k=0,1,2,
with gamma(j)=8*4^j*j!*a_j and R_j=gamma(j)/gamma(0). Retain its
L018/L021/L776/L778 completion, normalization, analytic-error, data,
evaluator and software contracts. Use its audited outward enclosures,
written with closed endpoints to enlarge the input:

    q_0 in [1.07484394250019421126346157158,1.07484394250019421126346157162],
    q_1 in [1.06274366627144916855311401273,1.06274366627144916855311401285],
    q_2 in [1.05430333113463476927545484495,1.05430333113463476927545484516].

Let d>=2 be an integer and A,B,C,D>0 satisfy

    q_k=(A+k)(B+k+1)(C+k)(D+k+1)
        /[(A+k+1)(B+k)(C+k+1)(D+k)], k=0,1,2.

For either pairing (A,B),(C,D) or (C,B),(A,D), suppose each numerator
minus its paired denominator lies in {1,...,d-1} union (d-2,infinity),
and at least one lies in the integer set. Parameters may depend on d;
D is free and L791's particular solution box is not imposed.

## Conclusion

Necessarily d<=151. In fact no positive solution of these equations
has both paired gaps positive integers, for either pairing. In a solution
in the stated regime with d>=5, one designated gap is 1 or 2; the other
lies respectively in (40.17,40.20) or (149.38,149.40).

These are necessary bounds, not feasibility assertions, optimal bounds,
or classifications outside the stated regime. The obstruction holds on
the entire displayed enclosure product, including the correlated actual
ratios. This is a local algebraic specialization whose originality is
not established. Its separate critical audit passed in step604 under
the inherited input and software contracts, as detailed below. No actual-Xi
sign, off-line zero or RH result follows; separation, signed residual
payment and mixed assembly remain open.

## Proof

**Source scope.** The pre-existing SPECIALIZE gate is
`drafts/literature/2026-11-05-central-discrete-pairing-test.md`; its completed
primary-source comparison is
`drafts/literature/2026-11-05-central-discrete-pairing-feasibility.md`.
A. Martinez-Finkelshtein, R. Morales and D. Perales, *Real roots of
hypergeometric polynomials via finite free convolution*,
[arXiv:2309.10970v3](https://arxiv.org/pdf/2309.10970v3), 2 May 2024,
printed pp.33–34, Proposition4.15(ii), (R2) and its iteration sentence,
give the specified sufficient root regime, allowing repeated roots.
Jonathan Holland, [arXiv:2608.08682v1](https://arxiv.org/html/2608.08682v1),
9 August 2026, (66)–(71) and Lemma6.2, gives conditional coefficient
matching. These results motivate the target; neither establishes its
central feasibility. The obstruction below uses only the three equations
and L791's enclosures, and reproves neither source theorem. The completed
source review is reused, not independently repeated here.

**Affine elimination.** Write Q=q_0, R=q_1, Z=q_2, S=RZ, and set

    a=1/(A+1), c=1/(C+1), x=1/(B+1), y=1/(D+1),
    p=a+c, r=ac, s=x+y, t=xy.

All four reciprocals lie in (0,1). By the symmetries of the equations,
relabel so a<=c and x<=y. The equations give

    1-p+r = Q(1-s+t),
    1+s+t = R(1+p+r),
    1+2s+4t = S(1+2p+4r).                         (1)

The third identity uses q_1*q_2, with no approximation. Define

    H=3R-2S-1/Q, J=3R-4S+1/Q, K=S-3R+3-1/Q,
    p0=K/H, p1=-J/H,
    t0=((QR-1)p0-(2Q-QR-1))/(2Q),
    t1=((QR-1)p1+(QR+1))/(2Q),
    s0=Rp0+R-1-t0, s1=Rp1+R-t1.

Eliminating s and t in (1) gives Hp+Jr=K. Thus every solution has

    p=p0+p1*r, s=s0+s1*r, t=t0+t1*r.              (2)

Conversely these expressions satisfy all three linear identities (1)
for every real r. The exact rational interval calculation below gives

    .01695<H<.01696, .10944<p0<.10945,
    21.422<p1<21.423, 2.34<p0*p1<2.35,
    .003799<t0<.003800.                            (3)

All divisions in these definitions are valid. From (2),

    (p1*a-1)(p1*c-1)=1-p0*p1<0.

Our ordering implies a<1/p1<c and

    a=(c-p0)/(p1*c-1), r=c(c-p0)/(p1*c-1), c>p0.  (4)

**Interlacing and both pairings.** Let F(z)=z^2-pz+r and G(z)=z^2-sz+t.
Define polynomials in v by

    E(v)=p1*v-1,
    N_s(v)=s0*E(v)+s1*v*(v-p0),
    N_t(v)=t0*E(v)+t1*v*(v-p0),
    P_m(v)=v^2*E(v)-v*(1-mv)*N_s(v)+(1-mv)^2*N_t(v).

For v=c, (4) gives N_s(c)=sE(c), N_t(c)=tE(c). When 1-mc is nonzero,

    P_m(c)=E(c)(1-mc)^2 G(c/(1-mc)).              (5)

There is the exact polynomial identity

    P_0(v)=t0*(2v+1)*(v^2-1).                    (6)

Indeed P_0 has degree at most three and constant term -t0. Its roots
are 1,-1,-1/2: at each value E(v) is nonzero by (3); put
r=v(v-p0)/E(v) in (2). Then F(v)=0. Respectively the first, second and
third identities in (1) force G(v)=0 (using Q>0 for the first).
Thus P_0(v)=E(v)G(v)=0. The three roots and nonzero constant term
determine the cubic (6). This is an exact identity, not a fitted factor.

At the actual c in (0,1), E(c)>0 and (6) is negative, so G(c)<0.
Therefore x<c<y. Formula (4) also holds with a in place of c;
E(a)<0 while the numerator in (6) is negative, so G(a)>0.
Since a<c<y, this forces a<x. Altogether

    a<x<c<y.                                     (7)

A positive original gap requires its numerator reciprocal to be smaller
than its denominator reciprocal. The only pairing with both gaps positive
therefore pairs a with x and c with y: pairing c with x would give a
negative gap. This covers both original labelings and imposes no new
ordering hypothesis on A,B,C,D. Write the positive gaps as

    n=1/a-1/x, m_*=1/c-1/y.                       (8)

**Uniform bound on the designated gap.** Expand P_m(p0+u) in powers of u.
The complete outward coefficient bounds are below. Every displayed
decimal is an exact terminating rational; intervals are open.

| m | u^0 | u^1 | u^2 | u^3 | u^4 |
|---|---|---|---|---|---|
| 1 | (-.002811,-.002810) | (.0375,.0376) | (.723,.724) | (6.838,6.839) | (23.829,23.830) |
| 2 | (-.000923,-.000922) | (.0920,.0921) | (1.659,1.660) | (15.416,15.417) | (52.487,52.488) |
| 3 | (.001087,.001088) | (.1570,.1571) | (2.814,2.815) | (25.743,25.744) | (85.974,85.975) |

There are no higher coefficients. In particular P_3(c)>0 since c>p0.
If c>=1/3, then m_*=1/c-1/y<1/c<=3. If c<1/3, set z=c/(1-3c).
Then z>c>x and G(z)>0 by (5). Since x<c<y, this sign forces z>y.
Taking positive reciprocals gives 1/y>1/z=1/c-3. In both cases,

    0<m_*<3.                                     (9)

This holds for every positive solution, independently of d.

**The two discrete cases.** If m_* is a positive integer, (9) restricts
it to m=1 or 2. Then y=c/(1-mc), where 1-mc>0, and P_m(c)=0 by (5).
For both m the coefficient table proves strict increase of P_m(p0+u)
on u>=0, with negative value at u=0. Exact interval evaluation gives

    m=1: .14677442 < c < .14677444,
    m=2: .11802777 < c < .11802778.                (10)

At each left endpoint P_m is in (-10^(-7),0), and at each right
endpoint it is in (0,10^(-7)), uniformly over all input enclosures.
Both brackets lie above p0 by (3). Strict increase places every possible
root c>p0 in its bracket; this does not assert existence of a positive
solution to the original system. Using (4), t=t0+t1*ac, and xy=t, compute

    x=t*(1-mc)/c, n=1/a-1/x.                     (11)

Interval evaluation on the entire brackets (10), retaining all input
widths, gives

    m=1: 40.17<n<40.20,
    m=2: 149.38<n<149.40.                         (12)

All divisions are by positive quantities: in both cases c-p0 is in
(.008,.04), p1*c-1 in (1.5,2.2), 1-mc in (.7,.9), a in (.005,.02),
and x in (.03,.07). Neither interval in (12) contains an integer.
Thus both paired gaps cannot be positive integers, without assuming
any bound on their possible sizes in advance.

If d<=4 the cap is immediate. If d>=5, a continuous allowed gap must
exceed d-2>=3. Thus (9) forces m_* into the discrete set, so m_*=1 or 2
and (12) applies. The other gap n is noninteger and must satisfy d-2<n.
Since n<149.40<150, d<152; integrality gives d<=151. This covers the
one-discrete-gap and two-discrete cases. No boundedness or convergence
of a parameter family has been assumed.

**Exact arithmetic certificate and limitations.** Run
`python3 scripts/central-jacobi/discrete_pairing_602.py` from this notebook.
Every endpoint is a Python Fraction. Closed rational intervals propagate
by exact addition, subtraction, four-endpoint multiplication and division
only by intervals excluding zero. Polynomial multiplication constructs
the displayed P_m, and composition substitutes p0+u. Each bound in (3),
the coefficient table, the endpoint signs in (10), the positivity bounds
and (12) is checked against the full rational enclosure. Independent
reuse of input intervals enlarges the domain, so correlated actual data
are included. No floating-point value certifies a sign or inequality.

The full output is `scripts/central-jacobi/discrete-pairing-certificate-602.json`:
PASS, 36 checks, no failures, all rational intermediates, and input/program
SHA256 hashes. The complete `/checks` field was inspected. Midpoint
diagnostics proposed the mechanism and brackets only; their JSON files
are preserved in the same directory and supply no proof premise.
The first certificate run incorrectly requested the auxiliary bound x>.04
for m=2. Its failed report is preserved as
`scripts/central-jacobi/discrete-pairing-first-pass-602.json`. The wider
valid bound x>.03 suffices; all other checks, including (12), already
passed. No mathematical obstruction was suppressed.

The original certificate assumes correct Python integer/Fraction operations
and the displayed interval implementation. Step602 did not independently
replay it; the separate step604 audit is below. L791's evaluator has not been rerun or its
binary attested. Its inherited analytic/data/software qualifications
remain hypotheses. The separate audit checks the reduction, complete
case coverage and rational computation. L817's fixed-tuple stop and
L818's strict-gap stop are contrasts, not inputs.

### Separate conceptual audit, 5 November 2026 — step604

The unchanged SPECIALIZE assessment is
`drafts/literature/2026-11-05-central-discrete-mixed-cap-audit.md`.
Its completed primary-source comparison was reused; no root-preservation
or matching theorem was reproved. The audit found no mathematical defect
in the conditional statement. It does not upgrade any of L791's inherited
analytic, coefficient, evaluator, data or software premises, and does not
assert a feasible tuple below the cap.

**Exact elimination and domains.** Substituting the four reciprocals in
q_0 and q_1 gives the first two equations in (1). In q_1*q_2 the factors
1+a, 1+c, 1+x, 1+y cancel, giving the third equation; q_2 alone would not
give it. Those factors and all original denominators are positive.
The first two equations equivalently give

    2t=(R-1/Q)p+(R+1/Q)r+R+1/Q-2,
    s=R(1+p+r)-1-t.

Inserting these in the third yields Hp+Jr=K exactly, proving both
directions of the affine elimination for arbitrary real r when QH!=0.
Thus the uses of (2) at formal special values below need no positivity
assumption on the corresponding artificial r. The certified Q,H,p1,t0
are positive and p0*p1>1. The product identity following (3) is exact;
with a<=c it forces a<1/p1<c, so neither E(a) nor E(c) vanishes.
Equation (4), a>0 and E(c)>0 then force c>p0. No division assumes
that A,B,C,D stay bounded or that a family has a limit.

**Cubic and interlacing.** The degree of P_0 is at most three. At
v=1,-1,-1/2, E(v) is nonzero; using r=v(v-p0)/E(v) gives F(v)=0.
The three equations (1) read, respectively,

    F(1)=Q G(1), G(-1)=R F(-1), G(-1/2)=S F(-1/2).

Consequently the three distinct values are roots of P_0. Its constant
term -t0 is nonzero; this fixes exactly t0(2v+1)(v^2-1), not merely
its sign or a numerical approximation. At c, this numerator is negative
and E(c)>0, hence G(c)<0. As G=(v-x)(v-y) with x<=y real,
x<c<y, including exclusion of x=y. At a the numerator is negative
but E(a)<0, hence G(a)>0. Because a<c<y, the only possibility is a<x.
This excludes a=c as well. Independent sorting of numerator and
denominator reciprocals permutes the two possible pairings. One is
(a,x),(c,y), and both gaps are positive; the other contains (c,x),
whose original-parameter gap is negative. Thus the proof includes both
original pairings without silently imposing an extra labeling condition.

**Whole domain and discrete cases.** Positivity of all five coefficients
of P_3(p0+u) for u>=0 proves P_3(c)>0 for every allowed c, not just
for the bracketed integer cases. If c>=1/3, then m_*<1/c<=3.
If c<1/3, the denominator of z=c/(1-3c) is positive. Equation (5)
gives G(z)>0, while z>c>x rules out the left component of {G>0};
therefore z>y and m_*<3 strictly. The equality c=1/3 belongs to the
first case and requires no evaluation of the singular expression z.

If m_* is an integer it is 1 or 2, and 1-mc=c/y>0. For each of these
two m, the shifted coefficient of u is positive and every higher one
is positive, so P_m(p0+u) is strictly increasing on u>=0. Its constant
is negative. The two endpoint signs, at endpoints above p0, capture
every possible root in this domain. This is a uniqueness and location
argument for a necessary equation, not an existence proof for the full
matching system. Formula (11) follows from xy=t and the gap relation;
all its denominators stay positive on the full two brackets. The
resulting open intervals for n contain no integer. In particular both
positive gaps cannot be integers, regardless of their permitted sizes.
For d=2,3,4 the degree cap is immediate. For every integer d>=5,
m_*<3<=d-2 excludes the strict continuous alternative for m_*, so it
must be discrete. Then n is noninteger, hence must satisfy d-2<n<150,
which implies d<152 and therefore d<=151. Neither an endpoint gap equal
to d-2 nor an equality at 150 is admitted. All one- and two-discrete
possibilities in the hypotheses are covered.

**Independent arithmetic and complete saved evidence.** Run
`python3 scripts/central-jacobi/audit_604.py`. The report is
`scripts/central-jacobi/audit-604/audit-report.json`: PASS, 51 checks,
no failures, including all 36 independent proof comparisons and an
additional complete comparison of all 36 saved bounds. Full actual and
required rational endpoints, Gaussian pivots and division denominators
are saved. The full report's `/checks` field was inspected; no preview
or printed floating-point approximation is used to certify a bound.

The new checker imports no arithmetic from the original generator.
It solves the three equations for (p,s,t) by interval Gauss-Jordan
elimination with two right-hand sides (constant and r terms), using
the augmented rows

    [-1, Q, -Q | Q-1, -1],
    [-R, 1, 1 | R-1, R],
    [-2S, 2, 4 | S-1, 4S].

Every pivot excludes zero. For each exact input triple these row
operations yield the unique affine solution; interval dependency only
enlarges its enclosure. The checker expands the quartic coefficients
explicitly and uses the binomial formula for the shift by p0, instead
of polynomial multiplication and Horner composition. Endpoint signs
are computed from the factored definition of P_m. With E=p1*c-1 it
computes x={t0*E+t1*c*(c-p0)}(1-mc)/(c*E) and n=(x-a)/(a*x),
independently of the original arrangement. All 36 names and required
open intervals are matched exactly to the original specifications.

Interval endpoints use Python integers/Fraction, rounded outward after
each operation to multiples of 10^(-70). Specifically the lower endpoint
is floor(10^70*l)/10^70 and the upper is ceil(10^70*h)/10^70;
integer division implements these operations, including negative values.
Four endpoint products or quotients give exact range bounds, with zero
excluded before division. The independently computed n enclosures satisfy
the same open intervals (12); no optimized degree cap is asserted.

Before replay, both saved input/program SHA256 values were checked.
An isolated copy of the unchanged generator and L791 input produced a
byte-identical copy of the entire original certificate, including every
rational intermediate. Replay files and log remain under
`scripts/central-jacobi/audit-604/`; all originals were preserved and
their hashes rechecked afterward. Replay equality is supplemented by
the differently arranged computation above, not used as its substitute.

The first-pass failure is exactly the obsolete auxiliary lower bound
x>1/25 for m=2. Its complete q, affine, polynomial and case records are
identical to the final certificate's records. Both computations enclose
that x strictly between .03 and .04, so the old failure is confirmed,
not erased. The first-pass program hash is different; no preserved
first-pass program was available for byte-identical replay, and none is
claimed. Its unchanged mathematical records suffice to check the stated
threshold correction. Python integer/Fraction behavior, interpreter and
filesystem integrity remain software trust; this is an independently
checked informal certificate, not a formal verification or evaluator
binary attestation.

## Mathlib

Full matching coverage of this specialization is unchecked. The proof
uses ordered-field algebra, polynomial identities and rational interval
comparisons; no absent-coverage or formal-verification claim is made.
