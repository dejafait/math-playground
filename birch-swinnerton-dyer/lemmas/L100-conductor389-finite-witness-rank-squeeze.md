# L100 — Fixed rank squeeze with finite-witness independence

## Hypotheses

Let E/Q be y²+y=x³+x²−2x, with coefficients [0,1,1,-2,0],
P=(0,0), Q=(1,0), and p=7. Use L030's minimal non-CM model,
audited L099's independent images of P,Q in E(Q) tensor_Z Q,
and audited L033's good ordinary prime and quadratic coefficient.
Use L004's classical cyclotomic Selmer dual X, Lambda=Z_7[[T]],
A=Lambda_(T), M=X tensor_Lambda A, and characteristic generator f_X.
The primitive ordinary series L_7(E,T)=sum a_j T^j is exactly L033's:
trivial Teichmuller branch, total minimal real period, kappa(gamma)=8,
and T=gamma−1 in the Iwasawa algebra. Its analytic coordinate is
T=8^(s−1)−1. No Euler factor is removed or divided out.

No published rank, basis, saturation or Sha assertion is a hypothesis.
The normalization retains L031's published optimality, rational torsion-order
and Manin-constant inputs through L032 and L033; their qualifications are
specified below. The published torsion order is not used in L099's
independent-point argument.
The approved assessment is
`drafts/literature/2026-10-20-finite-witness-rank-squeeze.md`.

## Conclusion

For this exact curve and classical dual,

\[
\operatorname{rank}E(\mathbf Q)
=\operatorname{ord}_T f_X
=\operatorname{ord}_T L_7(E,T)=2,
\qquad \Sha(E/\mathbf Q)[7^\infty]\text{ is finite}.
\]

In particular the divisible-Sha and augmentation defects of L004
vanish. Also a_0=a_1=0 exactly and v_7(a_2)=0.

This is REPRODUCTION of a known fixed result and method. L034 already
has these conclusions from a published basis; the change here is the
finite-witness provenance of the lower bound. The separate critical audit below passes. It asserts no basis or saturation, vanishing
or order of primary Sha, full Sha finiteness, complex analytic order,
refined formula or uniform certificate production. It is not a BSD
candidate.

## Proof

**Known inputs and the reason for specialization.** Apply L004 rather
than reprove its general arithmetic inputs. In particular its upper
bound is Kato's divisibility, in Stein–Wuthrich, *Algorithms for the
arithmetic of elliptic curves using Iwasawa theory*, Math. Comp. 82
(2013), 1757–1792, Proposition 7.2 and Theorems 7.3–7.4, p.1778
([published offprint](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=22)),
with the classical dual of Section 6, p.1775. The original theorem is
Kato, *p-adic Hodge theory and values of zeta functions of modular
forms*, Asterisque 295 (2004), Theorem 17.4; the checked elliptic-curve
translation and representation cases are retained in
[foundations/05](../foundations/05-kato-divisibility.md).
Only divisibility after inverting seven is used. The same paper's
Theorem 6.1, p.1776, gives the characteristic-order equality criterion
([statement](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=20));
L004 already assembles it with control and the Kummer sequence.
Section 7.1, p.1779, already illustrates the point/coefficient method.
The sole specialization needed here replaces the published independence
premise of L034 by L099. Neither L034 nor L082 is a mathematical input.

**Match the lower bound.** L099's completed separate audit establishes
independence of these exact P,Q in E(Q) tensor_Z Q. It uses the finite
local and global tests on the same R=Q−4P and justifies removal of
rational torsion. It does not use the global rank/Sha assembly of
L083: only the local quotient argument appearing in L096 is retained.
Thus L004's k=2 premise is met without importing any published rank,
saturation or Sha computation. Membership is also immediate by
substitution into this equation. No independence criterion is reproved
here, and individually nonzero or distinct points are not substituted
for L099's stronger conclusion.

**Match the upper bound.** L030 gives minimal discriminant 389 and
non-CM. L033 gives #E(F_7)=13 and a_7(E)=−5, so 7>=5 is good
ordinary on this very model. The same audited L033 supplies

\[
v_7(a_2-13/256)\ge1>v_7(13/256)=0.
\]

These are the coefficient and coordinate stipulated in the hypotheses,
not the coefficient of a changed or imprimitive series. The strict
inequality gives a_2!=0 and v_7(a_2)=0 by L004's finite-precision
test. Its error threshold is one; unit-root precision three is not
substituted for that error threshold. The all-level denominator C=0
comes from L032's entire normalized relative module via L033.

L031's calibration imports the exact model's optimality from Cremona's
appendix to Agashe–Ribet–Stein, *The Manin constant*, Theorem 5.2
([statement](https://wstein.org/papers/ars-manin/html/node13.html)),
and the semistable Manin result of Cesnavicius, arXiv:1703.02951,
Theorem 2.13, p.9 ([primary text](https://arxiv.org/pdf/1703.02951)).
Its model/optimal-label lookup excludes the rank column but retains the
last-column rational torsion order one for L031's unitary-cusp denominator
bound (Wuthrich, arXiv:1608.06423v2, Proposition 1, pp.3–4). Those published
normalization inputs and the audited independent twist calibration
remain part of the provenance; this replacement does not assert that
every upstream arithmetic input is independent of published computation.
None is a published rank, saturation or Sha premise. Existing finite
replays and audits are reused without rerunning arithmetic.

**Apply the matching threshold.** Write r=rank E(Q),
h=ord_T f_X, ell=ord_T L_7(E,T),
s=corank_Z_7 Sha(E/Q)[7^infinity], and delta=length_A(TM).
The checked inputs satisfy L004 with k=n=2, hence

\[
2\le r\le r+s+\delta=h\le\ell\le2.
\]

Every term is two. Since s,delta are nonnegative, both are zero.
L004's matching-case conclusion gives finite 7-primary Sha, rather
than merely stating zero corank for an arbitrary torsion group: its
dual is finitely generated over Z_7 and rank zero, hence finite.
No finiteness premise has been inserted. The equality ell=2 then
forces a_0=a_1=0 by the definition of order, independently of any
finite approximate zeros. The valuation of a_2 was established above.

The required and achieved thresholds coincide: two independent rational
directions and a nonzero quadratic primitive coefficient. The result
supplies a fixed certificate assembly with the approved replacement
provenance. Producing such inputs uniformly from complex analytic
order >=2 and identifying that order with r remain unresolved.
Finiteness of one primary subgroup does not prove its vanishing or
finiteness of the whole Sha. No leading-coefficient valuation or
complex-order comparison is extracted from this T-order squeeze.
ATTEMPTS/043 and the step-371 stop in ATTEMPTS/045 are unaffected.

**Separate critical audit, 2026-10-21 (step 391).** The prior SPECIALIZE
assessment `drafts/literature/2026-10-21-finite-witness-rank-squeeze-audit.md`
covers this exact verification. The written assembly passes. The following
checks reuse the completed finite arithmetic audits; they do not assert
a fresh replay or a new theorem beyond the inspected sources.

The equation and points agree across all four direct inputs. Substitution
at (0,0) and (1,0) gives zero on both sides. L030's invariant calculation
has c_4=112, c_6=-856 and Delta=389; the integral model's discriminant
valuations are at most one, so its minimality argument applies. Its
nonintegral rational j=112^3/389 excludes CM. Since 389 is not divisible
by seven, the model has good reduction there. L033's complete seven-point
x-table gives twelve affine points and O, hence trace -5, prime to seven.
Thus the non-CM, p>=5 and good ordinary conditions of L004 all hold.
No residual-surjectivity assertion is needed: foundations/05 retains
both representation cases of the cited Stein–Wuthrich statements, with
powers of seven allowed in the nonsurjective case.

The lower bound is rational independence, not independence of arbitrary
Selmer classes. Audited L099 uses the actual R=Q-4P: L081 makes [P]
nonzero locally modulo seven, L096 makes [R] zero locally, and L097
makes [R] nonzero globally. Its test excludes both nonzero coefficients
in any global relation modulo seven. Its local order-thirteen reduction
and strict formal logarithm exclude rational seven-primary torsion;
Mordell–Weil makes the remaining torsion finite and seven-divisible.
The resulting torsion-free quotient therefore retains the two independent
classes, to which the corrected Datta–Smith Lemma 5.5 applies. These
are the precise pointwise hypotheses needed for rank at least two.
Only the local part associated with L083 occurs in that argument;
its published-rank/Sha conclusions are not imported through L096.

For the upper bound the normalized symbol is exactly
S(r)=F({infinity,r}), with F=-phi on L032's entire relative module.
Its common denominator two is a unit at seven and gives all-level C=0.
The independent twist-five ratio and both total minimal real periods
are retained; a sampled denominator or an absolute-cycle scale cannot
replace them. L031's published optimality, Manin constant and rational
torsion order one remain normalization inputs, including the last one
in its denominator bound. This audit makes that provenance explicit;
it does not remove it or use it to replace L099's local torsion proof.
No published rational rank, saturation or Sha assertion enters.

L033 uses the trivial Teichmuller branch and gamma with kappa(gamma)=8.
The finite polynomials in powers of (1+T) and the limiting series use
this same T; no inversion, shift, Euler-factor removal or division by
T occurs. Its u=16 satisfies u^2+5u+7=343 and has unit derivative 37.
The input root precision M=3 and n=2 give the limiting error
min(n-1-C,M-C)=1. The exact b=13/256 is a seven-adic unit.
Thus v_7(a_2-b)>=1>v_7(b)=0, so a_2 is nonzero. Finite vanishing
of lower coefficients in the approximant plays no role. L030's modular
form coefficient a_2(E)=-2 is a different quantity from this quadratic
coefficient of L_7; no use of the former supplies the latter.

For completeness, every inequality in the assembly has a separate
justification. Independence gives 2<=r. L002's control/Kummer identity
gives h=r+s+delta with s>=0 and delta>=0, hence r<=h. Cotorsion
makes f_X nonzero. Kato gives L_7=f_X g in Lambda[1/7]; the nonzero
a_2 makes g nonzero. Its embedding in Q_7[[T]] has no negative
T-powers, so ord_T g>=0 and h<=ell. The nonzero quadratic coefficient
gives ell<=2, without assuming lower vanishing. Hence r=h=ell=2
and s=delta=0. The powers of seven in divisibility have T-order zero;
this argument uses no reverse divisibility or integral valuation bound.

The finiteness conclusion uses the actual arithmetic module, not an
unspecified zero-corank group. Finite generation of X over Lambda
makes X/TX finitely generated over Lambda/(T)=Z_7. Mazur's base-layer
control, dualized as in L002, gives X/TX -> S_0^vee with finite kernel
and cokernel. Its image is finitely generated and its finite cokernel
has finitely many generators, so S_0^vee is finitely generated over Z_7.
The classical all-place Kummer sequence dualizes to an injection
D^vee -> S_0^vee for D=Sha(E/Q)[7^infinity]. Since Z_7 is Noetherian,
D^vee is finitely generated. The equality s=0 makes it torsion; a
finitely generated torsion Z_7-module is a finite sum of Z_7/(7^e),
and is finite. Pontryagin biduality makes D finite as claimed. No
primary-Sha finiteness or vanishing was assumed in control or Kummer.
This explicitly verifies the finite-generation step already used by
L003/L004, rather than introducing an additional arithmetic theorem.

The equality ell=2 forces a_0=a_1=0 exactly. Delta=0 means TM=0;
neither conclusion was a premise for obtaining the squeeze. Finiteness
of D does not specify its order, and v_7(a_2)=0 supplies no such order
from divisibility after inverting seven. L034 is overlap only; L082,
L035's complex order and L083's global assembly supply no premise.
The existing DAG row is unchanged: all direct inputs remain L004,
L030, L033 and L099. The audit clarifies normalization provenance and
expands the finiteness justification without changing the argument or
its conclusion. The fixed certificate now has a checked assembly;
uniform production, the arbitrary complex-order comparison, full Sha
finiteness and the refined formula remain unresolved.

## Mathlib

Full matching theorem for this fixed finite-witness application,
including its arithmetic inputs: not checked. Supporting valuation,
power-series order and finite-generation results: not checked.
No library absence or formal verification is claimed. The named
theorems are imported through the precise references above and L004;
this file proves only their fixed applicability and resulting squeeze.
