# L081 — Exhaustive nonintegral dyadic points via a parameter at infinity

## Hypotheses

Use L033's E0: y²+y=x³−x²−10x−20, L069's coordinates
X=4x, Y=8y+4, and L078's entire fields and fixed generator:

    H=Q2(pi), pi^11=2,
    J=H[rho], rho³−3pi⁴rho²+2pi⁸rho−pi=0,
    theta=−16+12pi⁷rho−2pi³rho².

Use the maximal rings, exact arithmetic and unit-square labels proved
in L078. Thus v_H(2)=11, v_J(pi)=3, v_J(theta)=44, and the strict
unit-square threshold in J is 66. L079 supplies the existing realized
2048-label list and its abstract full-image equality. The independent critical audit below checks these inputs in the needed scope. No global unit basis,
class-kernel value, independence, rank bound or integer solution is assumed.

## Conclusion

All nonintegral-x points of E0(H), together with O, have an exhaustive
terminal-disk certificate in the parameter t=-x/y at infinity. All
16384 disks in pi O_H modulo pi^15 are realized. Every disk has a
constant fixed-theta Kummer class on this parameter branch. The classes
give exactly the same 2048 labels as L079, with every collision and
affine representative comparison retained. The complete records are in
`scripts/ramified-dyadic-image/parameter-disks.json`; the summary and
full replay are `parameter-certificate.json` and `parameter-verification.json`
in that directory.

In particular this covers the formerly missing original-x annuli
−22<=v_H(x)<0: even negative valuations correspond to 1<=v_H(t)<=11,
and odd negative valuations admit no point. The 16376 parameter disks
in this range are all realized. The other eight disks cover the tail
v_H(t)>=12, including O. Combined with L079's integral-x disks, this
is exhaustive pointwise disk evidence for the full local image. L080's
standard reciprocal evidence is preserved as an overlapping chart.

This uses an implicit parameter chart and the assessed square-neighborhood
method; it is not a literal execution trace of Bruin–Stoll's cubic-X
disk partition. No global direction is shown independent of L077, no
supported dimension below fourteen is obtained, and no class or integer
emptiness conclusion follows. The independent critical review below confirms this local certificate.

## Proof

### Exact parameter branch and exhaustive realization

Write t=-x/y and u=1/x. Direct substitution in the original equation
gives

    u-t²+t²u+(10t²-t)u²+20t²u³=0.

Putting u=t²v yields

    F_t(v)=v-1+t²v+(10t⁴-t³)v²+20t⁶v³=0.          (1)

For every actual t in pi O_H, F_t(V) reduces to V-1 modulo pi and
F'_t(V) is a unit for every integral V. The simple-root Hensel theorem
therefore gives exactly one integral root v(t), a unit reducing to one.
Uniqueness also follows directly: F_t(v)-F_t(w) is (v-w) times a unit
for integral v,w. We use the standard Hensel theorem already underlying
the inspected Bruin–Stoll SquareClasses proof, not a new local theory.

For t!=0 define

    x=1/(t²v(t)),       y=-1/(t³v(t)).             (2)

Reversing the substitution verifies the exact curve equation and
t=-x/y. With k=v_H(t)>=1, these points have v_H(x)=-2k and
v_H(y)=-3k. Their existence follows for every t, not from a sampled
or truncated square root. In projective Weierstrass coordinates they
are [t:-1:t³v(t)], which at t=0 is [0:-1:0]=O. Equation (1) verifies
this projective extension directly.

Conversely let a point have n=v_H(x)<0. On the right side of the
original equation, x³ has uniquely smallest valuation 3n. If y were
integral the left side would be integral, impossible; hence y is
nonintegral and y² has uniquely smallest valuation there. Thus

    2v_H(y)=3n.

It follows that n=-2k, v_H(y)=-3k for an integer k>=1, and
t=-x/y has valuation k. Its v=1/(xt²) is a unit satisfying (1),
so it is exactly the unique root v(t) above. This exhausts every
nonintegral-x point and rejects all odd negative x-valuations.
Only this branch of the parameter is used; an integral point having
the same numerical t need not be the integral-root branch (1).

### Fixed Kummer evaluation and even normalization

The previously assessed monic-cubic Kummer map evaluates [4x-theta]
without a scalar quotient; see Denis Simon, *Computing the rank of
elliptic curves over number fields*, LMS J. Comput. Math. **5** (2002),
7–17, [DOI](https://doi.org/10.1112/S1461157000000668), Section 1.1,
Propositions 1.1–1.2, p.8; and Bruin–Stoll, *Two-cover descent on
hyperelliptic curves*, Math. Comp. **78** (2009), 2347–2370,
[DOI](https://doi.org/10.1090/S0025-5718-09-02255-8),
[14 March 2008 author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Remark 2.1 and Section 4, pp.3,6–10. The general map and algorithm
are imported; only this curve's coordinate and disk estimates are derived.

Multiplication of 4/(t²v)-theta by the square (tv/2)² gives exactly

    q(t)=v(t)-(theta/4)t²v(t)².                   (3)

The two summands have J-valuations 0 and 6k-22. These are never equal
for integer k. Consequently

    v_J(q(t))=m(k)=min(0,6k-22).

This is -16,-10,-4 for k=1,2,3 and zero for k>=4. Every m(k) is
even, so q(t)/rho^m(k) has the same square class and is a unit.
The negative exponents here mean multiplication by rho^16, rho^10
or rho^4, respectively. No odd valuation direction is suppressed.
At O the Kummer class is identity. No finite Weierstrass exception
exists because the entire cubic algebra is a degree-three field (L078).

### Uniform terminal-disk bounds

Take N=15. For t,t' in one nonzero disk modulo pi^N, let their
common valuation be k, 1<=k<N, and put

    beta=min(N+11+k,2N),     d=min(beta,N+2k).

Writing t'=t+epsilon with v_H(epsilon)>=N proves
v_H(t'²-t²)>=beta. Factoring differences of powers also gives
v_H(t'³-t³)>=N+2k and v_H(t'⁴-t⁴)>=N+3k.
The sixth-power difference has valuation at least N+5k. Thus the
coefficients of F_t-F_t' all have valuation at least d.

Evaluate this difference at the integral root v'=v(t'). Since
F_t(v)-F_t(v') is (v-v') times a unit, as proved above, one obtains

    v_H(v-v')>=d.

For k=1,...,14 the minimum possible d is 17, greater than 11.
Since v+v'=2v+(v'-v), it follows that v_H(v+v')=11 and hence
v_H(v²-v'²)>=d+11. Therefore

    v_H(t²v²-t'²v'²)>=min(beta,2k+d+11)=beta;

the last equality follows from the displayed definitions for these
fourteen k (also recorded in the full bound table). Applying (3) gives

    v_J(q(t)-q(t'))>=min(3d,3beta-22).

After division by q(t') the bound is

    min(3d,3beta-22)-m(k) = 67  for k=1,2,3,
                           68  for k=4,...,14.      (4)

Every value strictly exceeds 2v_J(2)=66. By the strict Hensel
square-neighborhood fact in Bruin–Stoll, Section 4, Lemma 4.4 and
its proof, pp.7–8, the ratio q(t)/q(t') is square. This is the
already inspected and imported general square test used in L078;
ramification and the factor 4 are explicitly retained in (4).

For the zero disk, k>=15. Equation (1) gives
v_H(v(t)-1)>=2k, and (3) gives

    v_J(q(t)-1)>=min(6k,6k-22)>=68>66.

Thus its entire nonzero branch has identity class, matching O.
This completes class constancy on all parameter disks, including the
one whose center is the exceptional point.

### Complete exact certificates and their replay

The centers t0=sum_(i=1)^14 b_i*pi^i give precisely 2^14=16384
disjoint disks covering pi O_H modulo pi^15. Every nonzero center
itself is realized by (1)–(2). In the zero disk choose the nonzero
representative t=pi^15, as well as treating O explicitly. Thus no
parameter disk is rejected; the empty odd-x annuli were accounted
for separately by the exact valuation argument above.

The implementation uses O_H/64O_H in the eleven-element basis
1,pi,...,pi^10, reducing by pi^11=2. Its H-precision is 66.
Starting from v=1, the residual of (1) has valuation at least 2k.
Six unit-derivative Newton steps therefore suffice modulo pi^66.
Each derivative inverse uses seven Newton inverse steps, squaring
an error initially of valuation at least one to at least 128>66.
The final residual and unit derivative are verified in every record.
Hensel consequently places the unique exact root within pi^66 of
the stored approximation; the approximation is never treated as
an actual curve coordinate.

Equation (3) is then evaluated in the exact rational coefficient
algebra before any reduction in J. Changing the root lift by
H-valuation 66 changes the first term by J-valuation at least 198;
for the second term the denominator 4 costs at most 66, while all
other factors are integral. The conservative resulting error is
at least 132. Normalization by rho^(-m(k)) does not lower it.
Every normalized coefficient is checked integral, and only then
reduced modulo eight. Thus the computed units have precision 99,
above the strict square threshold 66. There is no premature division
of low-precision data.

Run

    python3 scripts/ramified-dyadic-image/check_parameter_disks.py
    python3 scripts/ramified-dyadic-image/verify_parameter_certificate.py

The construction saves every parameter center, realized t, approximate
implicit root, zero polynomial residual, unit derivative, even
normalization, full L078 normal form, affine representative match,
and complete collision histogram. Its 13/13 checks pass with no
failures. It has 16384/16384 disks, including 16376 with k<=11,
and exactly 2048 distinct labels, all in L079's list. Equality of
the two lists follows because the latter also has cardinality 2048;
it does not assume cardinality in place of point realization.

The replay reads every full disk record, substitutes each root into
(1) by Horner evaluation, checks every derivative, recomputes every
exact normalization, and reconstructs each class from the fixed
generators, its square factor and strict-square residual. It verifies
every mask exactly once, all affine matches, the entire collision and
valuation histograms, all fourteen bounds (4), and the zero disk.
All 12/12 replay checks pass with no failures. The complete relevant
bound table, coverage fields and check objects were inspected; this
is full evidence replay, not a bounded-preview correctness claim.
The replay shares the certified ring operations and is not an
independent critical audit of L078's mathematics or of this proof.

The present parameter chart and L079 now cover every E0(H) point.
The literal source algorithm's cubic-X disk tree was not executed;
the parameter specialization supplies exhaustive realizations and
square-class constancy instead. Historical L080 correctly describes
the gap at its own stage. No enumeration there or in L079 was rerun.
This is local reproduction of assessed methods, with no novelty or
additional independent global restriction claimed.

### Independent critical audit — 2026-10-16

The audit confirms the implicit equation, its exact parameter branch and
exhaustiveness. Direct projective substitution of [t:−1:t³v] into
Y²Z+YZ²=X³−X²Z−10XZ²−20Z³ gives t³ times (1), including the extension
at t=0. For each t in pi O_H, all nonlinear coefficients in (1) vanish
modulo pi and the linear coefficient is a unit. The difference quotient
in v is a unit on all integral inputs, proving uniqueness, as well as
the simple-root Hensel existence. Conversely the unique smallest terms
for negative v_H(x) force 2v_H(y)=3v_H(x); hence every such point is
on precisely this branch. No negative odd x-valuation or extra root
branch is silently omitted.

The Kummer normalization is an exact field identity: multiplying
4/(t²v)−theta by (tv/2)² gives (3). Its two terms have distinct valuations
0 and 6k−22 for every integer k, so the stated m(k) is exact and even.
For a depth-fifteen nonzero disk, the audited coefficient difference
bound is d=min(26+k,30,15+2k)>11. Thus v_H(v+v')=11 and the improved
square difference bound is valid; using only v_H(v−v') here would lose
needed precision. All fourteen resulting relative bounds are 67 or 68,
strictly above 66. On the zero disk v_H(v−1)>=2k gives bound 68 and
agrees with infinity. These are uniform bounds, not center tests.

The independent verifier in L078 checks every one of the 16384 full
records. Each saved root has polynomial residual zero modulo 64 O_H
and unit derivative, hence the exact Hensel root differs by H-valuation
at least 66. Root lifting error after the denominator 4 is at least
132 in J, before reduction to precision 99. Independently of the
constructor's fractional arithmetic, the verifier forms

    (4v−theta*t²v²)*rho^(−m) modulo 32 O_J,

checks coefficient divisibility by four, and divides to obtain the
normalized unit modulo eight. This retains precision 165−66=99; no
low-precision division is used. Polynomial convolution operates in the
maximal ring proved in L078. Every fixed class representative, square
factor, residual and affine representative match is then reconstructed.
All masks, all collision multiplicities and the full valuation histogram
are compared, not just a preview or a list of counts.

Actual/required disks are 16384/16384, including 16376 over the middle
annuli, and their label set equals the 2048-class affine set. The minimum
stored residual bound is 67>66. The separate complete audit certificate
has 23/23 aggregate checks and no failures. Together with L079 and the
explicit O treatment this certifies exhaustive pointwise local coverage.
The literal cubic-X source algorithm was not executed. No correction
of L081's conclusions was required; the audit establishes a reliable
local input, not a new global direction, class value, rank bound or
primitive integer exclusion. The general results cited above are reused;
Mathlib coverage remains not checked.

## Mathlib

Full matching implicit-parameter disk certificate, exact local list
and implemented comparisons: **not checked**. Supporting Hensel,
complete local fields, Kummer maps and square-neighborhood results:
**not checked**. Unknown coverage is not evidence of absence.
