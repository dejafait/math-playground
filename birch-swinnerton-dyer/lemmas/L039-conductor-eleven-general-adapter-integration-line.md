# L039 — Conductor-eleven arithmetic and full-relative integration line

## Hypotheses

Let E/Q be the curve with Weierstrass coefficients
[a_1,a_2,a_3,a_4,a_6]=[0,-1,1,-10,-20], namely
y^2+y=x^3-x^2-10x-20. Work at weight two and trivial character on
Gamma_0(11), on the entire relative symbol module modulo all torsion.
Paths are oriented {alpha,beta} from alpha to beta. Matrices act on
coordinate columns, and J denotes geometric reflection
{alpha,beta}->{-alpha,-beta}, rather than Stein's negative star.

The exact evidence lives in `scripts/conductor-eleven/`. The structural
construction and relative identification are those of L038. The dual
program/interface is the audited parameterized supplement of L030; no
conductor-389 numerical data is imported. L029 supplies the real-line
sufficiency statement. These results and their precise named source
inputs are imported, not reproved. Reproduce from the notebook root:

```bash
python3 scripts/conductor-eleven/certify_arithmetic.py
python3 scripts/general-relative/build_certificate.py --level 11 --primes 2 --out scripts/conductor-eleven/structural-certificate.json
python3 scripts/dual-kernel/build_certificate.py --structural scripts/conductor-eleven/structural-certificate.json --arithmetic scripts/conductor-eleven/arithmetic-input.json --adapter L038-relative-v1 --out scripts/conductor-eleven/dual-certificate.json
python3 scripts/dual-kernel/verify_certificate.py scripts/conductor-eleven/dual-certificate.json --structural scripts/conductor-eleven/structural-certificate.json --arithmetic scripts/conductor-eleven/arithmetic-input.json --out scripts/conductor-eleven/dual-verification.json
```

## Conclusion

The displayed equation is globally minimal, its exact conductor is 11,
it is non-CM, and a_2(E)=-2. In the certified integral quotient basis of
the full relative space V (dimension three), the matrices are

\[
J=\begin{pmatrix}-1&0&0\\1&1&0\\0&0&1\end{pmatrix},\qquad
H_2=\begin{pmatrix}-2&0&0\\0&-2&-1\\0&0&3\end{pmatrix}.
\]

The full relative dual kernel of (J^t-Id; H_2^t+2Id) has dimension one,
spanned by v=(5/2,5,1)^t. For phi(x)=v^t[x] and the normalized newform
f of E, the real-integration functional
I({alpha,beta})=Re(2 pi i integral_alpha^beta f(z) dz) satisfies
I=beta phi on all V tensor R for a nonzero real beta.

This is one finite reproduction of known algorithms and L029's theorem.
The complete replay and separate critical audit of this arithmetic/instance
assembly pass. Generic software arithmetic status remains
SUPPLIED_CONDITIONAL; the local arithmetic proof below supplies this
instance's assumptions separately. There is no universal software theorem,
period normalization, independent q, normalized denominator, coefficient,
point certificate, complex-order comparison, or new BSD case here.

## Proof

**Arithmetic imports and applicability.** Import John Cremona,
*Algorithms for Modular Elliptic Curves*, corrected second edition (1997),
[Sections 3.1--3.2, pp.62--67](https://johncremona.github.io/book/fulltext/chapter3.pdf),
for the integral Weierstrass invariants, discriminant transformation and
the good/multiplicative exits of Tate's algorithm (lines 1--22, specifically
19--22 for multiplicative reduction). Import the same book's Section 3.9,
p.103, rational CM j-list, all of whose entries are integral. Import
Breuil--Conrad--Diamond--Taylor, *On the modularity of elliptic curves over
Q: wild 3-adic exercises*, JAMS 14 (2001), 843--939,
[Theorem A and Introduction conditions (1)--(2)](https://virtualmath1.stanford.edu/~conrad/papers/tswfinal.pdf).
For every elliptic curve over Q this gives its normalized rational
weight-two newform at the exact conductor, with good-prime coefficient
p+1-#E(F_p). No rank or ordinary-prime hypothesis is needed.
The independent calculations below are required to apply these results to
this exact equation; no database conductor or newform label is a premise.

Using b_2=a_1^2+4a_2, b_4=a_1a_3+2a_4,
b_6=a_3^2+4a_6 and
b_8=a_1^2a_6+4a_2a_6-a_1a_3a_4+a_2a_3^2-a_4^2 gives

\[
(b_2,b_4,b_6,b_8)=(-4,-20,-79,-21),\quad
c_4=b_2^2-24b_4=496,\quad
c_6=-b_2^3+36b_2b_4-216b_6=20008,
\]
\[
\Delta=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6
=-161051=-11^5.
\]

Also c_4^3-c_6^2=1728 Delta. The trial divisors 2,3, all integers
through floor(sqrt(11)), have remainders 1,2; hence 11 is prime.
The nonzero discriminant establishes nonsingularity. Every local
discriminant valuation of this integral equation is zero or five. A
decrease under a rational change to another integral local equation is
a positive multiple of 12 by the cited transformation formula; an
integral equation has nonnegative discriminant valuation. Since five
is below 12, no such decrease is possible, at any prime. Thus the
displayed equation is globally minimal.

At the only bad prime 11, c_4=496 is congruent to one. Tate's
multiplicative exit therefore gives type I_5 and conductor exponent one.
Every other prime has unit discriminant and good reduction, with
conductor exponent zero. Consequently N=11. Moreover
j=c_4^3/Delta=-122023936/161051 has reduced denominator 11^5>1,
since 11 does not divide c_4. It is outside the complete rational CM
list in the cited Section 3.9, so E is non-CM.

Reduction modulo two has y^2+y=x^3+x^2. For x=0 and x=1 the
right side is zero, and for y=0 and y=1 the left side is zero.
Thus all four possible affine pairs are points and exhaust F_2^2.
There is precisely one point at infinity, [0:1:0], so #E(F_2)=5.
The discriminant is odd, hence this is good elliptic reduction. Explicitly,
the affine y derivative is one modulo two and the homogeneous derivative
F_Z is one at infinity. Therefore a_2=2+1-5=-2. BCDT now supplies
exactly the newform required by L029 at the independently determined
conductor. `arithmetic-certificate.json` retains every invariant, prime
trial, local valuation/unit test, all four affine pairs, infinity, exact j,
the twelve arithmetic checks and their empty failure list. The proof
above supplies the implications from those computations to arithmetic.
`arithmetic-input.json` binds the same model, N, P and trace while retaining
the generic adapter's conditional provenance marker.

**Entire lattice and operators.** Import L038's full integral relative
construction: its Stein Theorem 3.13 identification includes all Manin
relations and removal of all torsion; its coprime lifts, path witnesses
and saturation are used here without an absolute-cycle restriction.
The complete `structural-certificate.json` has s=12 cosets, 24 relation
rows, relation rank r=9 and quotient dimension d=3. It includes all 120
primitive-pair orbit assignments, all 36 relation lookups, unimodular
transforms and inverses, and every generator coordinate. All nine diagonal
pivots are one, so the removed torsion order is one; saturation is still
verified, not inferred from the rational dimension.

The separate dual checker invokes the entire general structural checker
before any linear claim. The fresh subordinate report is
`dual-verification-structure/general-verification.json`; it binds the
structural bytes and has no failures. It completely replays 43 row and
13 column operations and their 43 and 13 inverses, both inverse products,
UAW=D, all diagonal/zero-tail entries, PiQ=Id, PiK=0, PiA^t=0 and the
integral splitting identity. It checks all twelve generator coordinates.
There are sixty complete paths: twelve original-generator reductions,
twelve reflected paths, and thirty-six T_2 paths (all three terms for
each generator). All 218 saved segments have their complete oriented
endpoint chains and Gamma_0(11) witnesses checked. The expected coset,
relation, path and operation counts match the full domain, not a sample.

For both J and T_2, the checker reconstructs the raw Z and coordinate
Y=Pi Z, then checks every source-relation and saturated-kernel image,
B_O=YQ, and B_O Pi=Y on every generator. Across the two operators
these are 48 source-relation images, 18 saturated images and 24 generator
reconstruction identities. These full path and descent checks identify
the displayed column matrices on the whole relative lattice. J is the
geometric reflection with unchanged endpoint direction. The supplementary
J^2=Id and commutation checks are not substituted for path identification.
The subordinate report records 15,944 successful checks and the full
actual/required domain counts; their number alone is not the evidence.

**Full rank witness and functional.** The outer independent checker
reconstructs every entry of the following 6-by-3 matrix from those certified
column matrices and the independently proved a_2:

\[
B=\begin{pmatrix}
-2&1&0\\0&0&0\\0&0&0\\0&0&0\\0&0&0\\0&-1&5
\end{pmatrix}.
\]

The four saved reversible rational operations scale row 0 by -1/2,
swap rows 1 and 5, scale row 1 by -1, then add half of row 1 to row 0.
Their full replay yields leading rows (1,0,-5/2) and (0,1,-5), with all
remaining rows zero. Thus the kernel is precisely Q(5/2,5,1)^t.
Independently, rows 0,5 and columns 0,1 of the original B give
the minor ((-2,1),(0,-1)), whose determinant is two. The checker uses
denominator clearing and fraction-free Bareiss elimination with all exact
divisions checked, rather than the producer's rational determinant routine.
All six entries of Bv are zero and v is nonzero. The minor proves rank
at least two and v proves rank at most two. Thus actual rank equals the
required d-1=2 and actual nullity equals the required one.

In generator order, the complete functional values are
(-1,1,0,5,5/2,-5/2,-5,-5,-5/2,5/2,5,0).
They are computed from every integral coordinate, not from a selected
generator or a rational-lattice guess. The checker verifies all twelve
values, all 24 source-relation values and all nine saturated-relation
values vanish as appropriate. Model/arithmetic and structural byte
bindings, adapter version, complete shapes and fresh subordinate report
hashes are retained in `dual-certificate.json` and `dual-verification.json`.
The outer replay has no failures. A bounded JSON display was used only
to inspect selected complete matrices/vectors; all structural and linear
evidence was checked by the full replay, not established by a preview.

All hypotheses of L029 now hold for this exact curve and full relative
module. Its integration membership and nonvanishing theorem gives
I=beta phi with beta nonzero. No period or twist value enters that
application. In particular these unnormalized half-integral values are
not a denominator bound for Neron-normalized symbols. Independent q and
the remaining L028/L036 assumptions are still necessary for calibration.
The reproduction produces a relevant finite line input beyond the prior
local executed instances, but no progress beyond the imported mathematics
and no solution to the arbitrary-curve BSD gap.

**Separate critical audit (2026-10-10).** The complete arithmetic proof,
L029's full-relative contract, and both current checker programs were
independently reviewed under the saved SPECIALIZE scope. No arithmetic,
operator, lattice, rank or assembly correction was needed. Reproduce:

```bash
python3 scripts/conductor-eleven/audit_certificate.py
```

The full audit is `scripts/conductor-eleven/critical-audit/manifest.json`;
the fresh outer and subordinate reports are `verification.json` and
`verification-structure/general-verification.json` in that directory.
All twelve input/program/report files, including this new audit program,
were hashed and copied before replay under `originals/`, with their full
paths preserved; `pre-replay-manifest.json` records the hashes. Every
original input and program remains unchanged. Producer hashes bind their
current bytes; mathematical acceptance comes from the independent checker
contract and complete replay, not a producer-success flag.

For arithmetic, the audit recomputes every b and c invariant and computes
Delta independently as (c4^3-c6^2)/1728, comparing with the original
discriminant formula. Trial division covers every possible divisor through
sqrt(11); the equality Delta=-11^5 is its complete factorization. At each
prime a rational local change has integral valuation of its scale, so a
strict decrease of the discriminant valuation is at least twelve. The
integral model's valuations zero and five therefore prove local minimality
everywhere. The cited good and multiplicative cases apply respectively
away from 11 and at 11, since c4 mod 11=1. No additive Tate branch is used.
The reduced j denominator remains 11^5, excluding every rational CM entry.
The independent audit also enumerates all seven nonzero projective triples
over F2: exactly (0,0,1),(0,1,0),(0,1,1),(1,0,1),(1,1,1) satisfy the
homogeneous equation. Over F2 these are already distinct projective
classes. Thus infinity is unique, the point count is five and a2=-2;
the smoothness checks and modularity applicability above are unchanged.
The generic SUPPLIED_CONDITIONAL marker is retained intentionally.

For the full relative module, the structural checker independently
partitions all 120 primitive pairs by all ten units and checks the twelve
SL2 lifts. All 24 relations are reconstructed from all 36 right-action
lookups, including repeated indices. Each integral operation is reversible;
complete forward and inverse logs identify U,W and both inverses, UAW=D,
all nine positive pivots and the zero tail. Consequently the rows of A
have saturated transpose lattice K=W^(-t)E_head, and Pi=E_tail^t W^t
has exactly that kernel. The integral section Q and splitting identity
verify the quotient lattice and every coordinate, not just rational rank.

Every segment has checked SL2 determinant, both oriented endpoints and
the exact Gamma0 matrix h g_i^(-1); adjacency and the final endpoint
make the entire chains telescope. Subtracting the start chain from the
end chain fixes the path orientation. Reflection uses diag(-1,1) without
endpoint exchange; T2 uses all three prescribed good-prime maps. Thus all
sixty paths and 218 segments establish the intended raw Z and Y=Pi Z.
Both complete source-relation and saturated-kernel images vanish; YQ and
BPi=Y identify both operators on all twelve generators. All actual/required
counts above match. The full fresh subordinate report, including all
15,944 check labels, equals the original report. The original count of
218 segments is rechecked in full, not inferred from the path count.

The dual checker reconstructs all six rows from these column matrices.
Each of the four rational operations is invertible, the two leading
pivots are unit columns, and all four tail rows are zero. The free third
coordinate and its determined first two entries give precisely the
recorded vector. Independently of either determinant routine, the audit
computes the displayed two-by-two determinant as (-2)(-1)-(1)(0)=2
and checks every Bv entry. This proves both rank bounds, hence exactly
rank two and nullity one in dimension three. All twelve generator values,
24 source relations and nine saturated relations pass; the entire fresh
linear check list and summary equal the originals. Current structural,
arithmetic and dual byte bindings, both checker hashes and the subordinate
report hash match the actual files.

The prior persistence failure was tested specifically on this general
adapter. A separate copy increments the first original-path segment's
claimed Gamma0 matrix entry, updating the dual structural hash so that
rejection must reach geometric replay. A valid success report is first
seeded at the new subordinate output path. Both fresh reports then reject
at `original generator paths: h times inverse lift in Gamma0`; the
subordinate report replaces the stale success, binds the corrupted bytes,
records its failure and has no summary. Full corrupted inputs and reports
are retained in the audit directory. This is an expected rejection, not
a failure of the unmodified certificate or a universal soundness test.
All 31 audit comparisons pass with no unexpected failures.

Finally L029 applies to the independently established minimal non-CM
curve and its conductor-level normalized nonzero newform, the complete
relative module, good prime 2, certified trace/operators and exact
one-dimensional dual kernel. Its real-period nonvanishing gives beta!=0;
no central-value nonvanishing is substituted. The audit validates this
fixed known-algorithm input only. It supplies neither an independent q nor
a Neron-normalized denominator, and none of the original BSD gaps is
removed. Mathlib coverage remains as qualified below.

## Mathlib

Full matching conductor-eleven arithmetic/full-relative line certificate:
not checked. Supporting Weierstrass invariant, local minimality/conductor,
CM classification, modularity, integral relative-symbol and exact matrix
coverage: not checked. Unknown availability is not absence. The named
inputs are cited above and in the imported canonical L029/L030/L038;
no Mathlib theorem is assumed to certify these new executable artifacts.
