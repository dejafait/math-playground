# Lemma 818: a finite cap for central matching in the strict Jacobi regime

## Hypotheses

Use L791's exact central ratios q_k=R_(k+1)^2/(R_k R_(k+2)),
k=0,1,2, with its normalization gamma(j)=8*4^j*j!*a_j and shift zero.
Retain its actual-completion, analytic-error, certified-data and trusted
software contracts inherited from L018/L021/L776/L778. This argument
uses L791's separately audited ratio enclosures; it does not independently
rebuild the evaluator or attest its software.

Let d>=1 be an integer. Suppose A,B,C,D>0 satisfy

    q_k=(A+k)(B+k+1)(C+k)(D+k+1)
        /[(A+k+1)(B+k)(C+k+1)(D+k)], k=0,1,2.

Suppose either A>B+d-1 and C>D+d-1, or C>B+d-1 and A>D+d-1.
All four parameters may vary with d, and D is free.

## Conclusion

Necessarily d<=319. Thus no arbitrarily large degree family satisfies
these equations in this strict sufficient Jacobi regime, for either
numerator pairing. This is a conservative cap, not an optimal cap or
an existence statement for any d<=319.

Only this specified regime is stopped. No general nonexistence of
degree-dependent positive-rooted hypergeometric models, nonreal root
of an actual Jensen polynomial, off-line zeta zero or RH conclusion
follows. L791's directly certified degree-five roots and L817's
different fixed-tuple conclusion remain intact. Quantitative separation,
signed residual payment and all-degree mixed assembly remain open.

## Proof

**Source scope and reason for the specialization.** The prior SPECIALIZE
assessment is `drafts/literature/2026-11-05-degree-dependent-central-jacobi-test.md`.
Its completed comparison is
`drafts/literature/2026-11-05-degree-dependent-central-jacobi-feasibility.md`.
Jonathan Holland, [arXiv:2608.08682v1](https://arxiv.org/html/2608.08682v1),
equations (49),(52),(66)–(74), Lemma6.2 and its proof, supplies conditional
matching, not central unbounded feasibility. The Jacobi identity and
the classical parameter conditions are given by
[DLMF18.5.7](https://dlmf.nist.gov/18.5.E7),
[Table18.3.1](https://dlmf.nist.gov/18.3#T1) and
[18.2(vi)](https://dlmf.nist.gov/18.2#vi).
No matching, orthogonality or root theorem is reproved or needed in the
inequality below. The difference to be checked is the compatibility of
the exact central equations with the stated growing-degree inequalities.
This is a conventional algebraic specialization; no originality claim
is made. The broader regimes in Martinez-Finkelshtein–Morales–Perales,
[arXiv:2309.10970v3](https://arxiv.org/pdf/2309.10970v3), Proposition4.15(ii)
and (R2), are outside this conclusion.

**A necessary inequality from two equations.** For t>0 set
h_0(t)=(t+1)/t and h_1(t)=(t+2)/(t+1). Let

    U=h_0(B)h_0(D),  V=h_1(B)h_1(D),
    x=1/(B+1),       y=1/(D+1).

Then 0<x,y<1, U=1/[(1-x)(1-y)] and V=(1+x)(1+y).
Consequently the exact identity

    V-(2-1/U)=2xy>0

holds. The matching equations at k=0,1 give

    U=q_0 h_0(A)h_0(C),  V=q_1 h_1(A)h_1(C).

All factors are positive and h_0(A)h_0(C)>1. Therefore

    q_1 h_1(A)h_1(C)>2-1/[q_0 h_0(A)h_0(C)]>2-1/q_0.

For either pairing the assumed strict inequalities imply A,C>d-1,
since B,D>0. Thus h_1(A),h_1(C)<1+1/d. In particular every admissible
solution must satisfy

    q_1(1+1/d)^2>2-1/q_0.                         (1)

This argument uses no pairing-specific ordering beyond A,C>d-1;
exchanging the numerator parameters leaves it unchanged. It permits
arbitrary dependence of B,D and the other parameters on d.

**Exact rational comparison.** L791's full conservative enclosures imply

    q_0>1.0748=2687/2500,  0<q_1<1.0628=2657/2500.

These outward weakenings preserve the entire original enclosures and
therefore the correlated actual values. If d>=320, monotonicity of
1+1/d and of 2-1/q on q>0 gives

    q_1(1+1/d)^2 < (2657/2500)(321/320)^2
                        < 2874/2687 < 2-1/q_0.

The middle comparison is purely rational: after multiplication by
2500*320^2*2687>0 its right side minus left side is

    2874*2500*102400 - 2657*103041*2687
      =735744000000 - 735646690719
      =97309281>0.

This contradicts (1). Hence d<320, and integrality gives d<=319.
The unused equation at k=2 can only restrict solutions further; a
necessary obstruction to the first two equations excludes every full
three-equation solution. No independently selected interval data,
finite scan, approximate solver, degree sweep or mathematical script
is used. The proof is an exact rational inequality conditional on the
inherited audited actual-data input.

### Separate exact-arithmetic and hypothesis audit, 5 November 2026 — step600

Reused the pre-existing SPECIALIZE assessment
`drafts/literature/2026-11-05-central-strict-jacobi-cap-audit.md`.
The stated conservative cap passes this independent audit. It is not a
sharp feasibility boundary, a discovery beyond the sources checked, or
an audit of their manuscripts. No mathematical correction is required.

**Input and contract boundary.** Read L791's full input and separate
step478 audit, and the relevant normalization and analytic/software
passages of L018/L021/L776/L778. Substitution into the even moment series
gives a_j=M_(2j)/[8*4^j*(2j)!], so gamma(j)=j! M_(2j)/(2j)! is positive;
R_0=1 and the displayed q ratios use this same normalization at shift
zero. No zero-free-annulus or Fredholm-norm hypothesis from L776 is
used. L778's complex uniform |G-P_0| bound, including the boundary
|w|=1600, permits the Cauchy coefficient error E_G/1600^j; the retained
cell-integration widths must also be included, as L791 does. We import
L791's already audited resulting enclosures, not merely its decimal
centers. Its directed Decimal and exp/sqrt contracts (including allcr=1),
quadrature and tail bounds, data and evaluator assumptions remain in
force. This audit does not rerun that evaluator, attest its binary or
remove those qualifications.

**Identity, signs and scope.** For 0<x,y<1, expand
1/U=1-x-y+xy and V=1+x+y+xy. Hence V-(2-1/U)=2xy>0.
All matching denominators are positive, and
q_0 h_0(A)h_0(C)>q_0>0. Taking reciprocals reverses this strict
inequality; subtracting from 2 gives precisely the second strict
inequality in the proof. For either nominated pairing, positivity of
B,D gives A,C>d-1. Thus A+1,C+1>d>0 and
h_1(A)=1+1/(A+1)<1+1/d, likewise for C. Multiplication by positive q_1
preserves strictness and proves (1), including d=1. This reasoning is
pointwise for every admissible tuple and places no uniformity, fixed-D,
fixed-box or degree-independence assumption on the parameters. The
third matching equation is an additional constraint, so omitting it
cannot invalidate a necessary obstruction to all three equations.

**Whole-enclosure arithmetic and unbounded degrees.** Run
`python3 scripts/central-jacobi/audit_600.py`. It uses exact integer and
Fraction arithmetic on all six printed L791 endpoints and verifies
that the entire q_0 and q_1 enclosures imply the outward weakenings.
The full integer products are independently reproduced as
735744000000 and 735646690719, with difference 97309281>0.
The exact positive rational margin is 97309281/687872000000.
The report `scripts/central-jacobi/audit-600/report.json` records PASS,
17 checks, no failures, complete rational values and the canonical
input hash. This finite arithmetic replay is not a degree sweep:
for every integer d>=320, 1/d<=1/320, while q maps to 2-1/q
increasingly on q>0. The proof therefore excludes all such d at once.
The arithmetic margin is sufficient for the contradiction and is not
a root-separation or actual-Xi sign margin.

Only the stated strict sufficient regime is stopped. The broader
continuous/discrete source regimes, L791's direct degree-five root
certificate and L817's fixed-tuple classification have different
hypotheses. This audit supplies neither existence for d<=319 nor a
global model-nonexistence statement. Separation, signed residual
control and all-degree mixed positivity remain unresolved. The only
direct mathematical input remains L791; no DAG edge changes.

## Mathlib

Full matching coverage of this specialization is unchecked. Its new
step uses elementary ordered-field identities and rational comparisons;
no absence claim or formal verification is made. The analytic/data and
software qualifications of L791 remain hypotheses.
