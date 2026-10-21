# L062 — Conditional finite-depth localization exponent test

## Hypotheses

Retain every hypothesis and convention of L061, hence every L026 premise:
E/Q is non-CM, p>=5 is good ordinary, E[p] is surjective, p divides
neither #E(F_p), the Manin constant nor any Tamagawa factor,
E(Q_p)[p]=0, and a residual Kurihara number in Sakamoto's N_(1,0) is
nonzero with compatible Neron plus-period and discrete-log conventions.
Assume L(E,1)=0, w(E)=+1 and an independently certified nonzero quadratic
coefficient of the fixed primitive ordinary cyclotomic series.

Use D=Sel(Q,E[p^infinity]), its maximal divisible subgroup D_div,
the classical discrete localization f:D -> L_p and the whole-Kato-system
first index k from L061. Supply integers e>=0 and n>e satisfying
p^e(D/D_div)=0. Supply a classical class c in Sel_(p^n)(E/Q).
Write loc_p(c) in E(Q_p)/p^n E(Q_p) via its finite Kummer image.
The exponent and class are additional certified inputs, not consequences
of the hypotheses above. The prior approved scope is the COVERED_TARGET
in [the finite-depth assessment](../drafts/literature/2026-10-14-finite-depth-localization-witness.md).

## Conclusion

At the same coefficient depth n,
\[
p^e\operatorname{loc}_p(c)\ne0\quad\Longrightarrow\quad k=1.
\]
Consequently L061's rationalized localization has rank one and its strict
Selmer kernel has dimension one. This selects a branch conditionally;
it supplies neither the exponent nor a class satisfying the test.
A zero test for the supplied class is inconclusive. No fixed-depth
converse, rational Kummer membership, rational-rank-two conclusion,
finite Sha or complex-order comparison is asserted. The separate critical
audit below passes under the unchanged supplied-input hypotheses.

## Proof

**Imported arithmetic input.** Use audited L061, including its
coefficient identifications (4)--(5), their naturality and its exhaustive
alternatives k in {1,2}. Its primary input is Chan-Ho Kim, *The structure
of Selmer groups and the Iwasawa main conjecture for elliptic curves*,
author text dated 2025-05-12: [Definition 2.12 and Theorem 2.13(5),
printed pp. 14--15](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=15),
[Proposition 3.13, p. 20](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=21),
and [(5.1) and the complete positive-corank cases, pp. 26--28](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=27).
Every premise is retained above, so this is an application of the existing
source specialization, not a reproof of Kim's theorems.

**The finite-image alternative.** Suppose k=2. L061 gives a finite image
I=f(D), possibly nonzero. The image f(D_div) is divisible: for y=f(x)
with x in D_div and any integer a>0, divisibility supplies z in D_div
with az=x, whence a f(z)=y. A finite divisible group is zero. Indeed,
if its order is b>0, multiplication by b is both zero (Lagrange's theorem)
and surjective (divisibility), which forces the group to be zero.
Thus f kills D_div; it is not claimed to kill all of D.

The supplied quotient bound means that p^e x lies in D_div for every
x in D. Therefore
\[
p^e f(x)=f(p^e x)=0\qquad(x\in D)
\]
in this branch. This controls the entire finite image even when it is
nonzero. No divisible-subgroup splitting or inverse-limit surjectivity
is needed. The Stacks injectivity theorem assessed for possible splitting
is consequently unnecessary; we do not reprove or invoke it.

**Same-depth coefficient transfer.** Let alpha_n:Sel_(p^n) -> D[p^n]
and beta_n:E(Q_p)/p^n E(Q_p) -> L_p[p^n] be the natural isomorphisms
proved and audited in L061. Put x=alpha_n(c). The localization square
commutes, so
\[
\beta_n(\operatorname{loc}_p(c))=f(x).
\]
Both maps are homomorphisms at the fixed depth n. Consequently
\[
\beta_n(p^e\operatorname{loc}_p(c))=p^e f(x)=0.
\]
Injectivity of beta_n gives p^e loc_p(c)=0, contradicting the test.
Here multiplication by p^e stays in E(Q_p)/p^n E(Q_p); it is not a
downward coefficient transition or a replacement by a smaller point
quotient. The global residual hypothesis and local p-torsion premise
are exactly the coefficient-injectivity hypotheses checked in L061;
no local torsion vanishing elsewhere is added.

Hence k cannot be two, and the exhaustive alternatives imply k=1.
Its rank-one localization and strict-line conclusions follow directly
from L061. The assumed n>e excludes a vacuous test: if n<=e then the
point quotient itself is killed by p^e. The proof uses no bound on an
integral Tate-module cokernel and no presupposed rationalized nonzero
localization. For e=0 it states precisely that a nonzero finite
localization suffices when D=D_div; it does not assume that equality
in the general case. Choosing c=0 always makes the test zero, even
if k=1, so failure for a supplied class cannot select k=2.

**Relevance and limitations.** This is a local advance by known-source
specialization, classified REPRODUCTION, not progress beyond the checked
source package. It could certify the localization prerequisite without
first providing a rational-point basis. Independent exponent and class
production remain missing. Even with a successful witness, the strict
line need not lie in rational Kummer space; auxiliary availability,
uniform coefficient production and arbitrary complex-order/rank equality
remain unresolved. ATTEMPTS/031's direct-semisimplicity stop is preserved.

**Separate critical audit (2026-10-14).** The complete implication passes;
no additional hypothesis, repaired implication or stronger conclusion is
needed. This verifies the existing conditional specialization, not a new
arithmetic production result. The prior approved scope is
[the audit assessment](../drafts/literature/2026-10-14-finite-depth-localization-critical-audit.md).

First, all L026 premises listed in the hypotheses remain in force. L061
therefore supplies corank D=2, L_p isomorphic to Q_p/Z_p, and the
exhaustive alternatives k=1,2 with finite image in the second case.
The image is finite as an actual group, not merely zero after tensoring.
For J=f(D_div), divisibility is checked within J: a preimage of x under
multiplication by a is chosen in D_div itself, so its image is an
a-division of f(x) in J. Since J is a subgroup of the finite image I,
multiplication by |I| kills J, while divisibility makes that same map
surjective. Thus J=0, including when I is the trivial group. The bound
p^e(D/D_div)=0 says exactly that p^e x belongs to D_div for every x;
it gives p^e I=0 without assuming I=0, bounding only a proper quotient,
or invoking a splitting. This is the entire finite-image argument.

For an independent check of the coefficient step, write i_n:E[p^n] -> A
for inclusion. The long exact sequence for
0 -> E[p^n] -> A -> A -> 0, with last map multiplication by p^n,
gives an isomorphism H^1(K,E[p^n]) -> H^1(K,A)[p^n] when H^0(K,A)=0.
Residual surjectivity gives this vanishing for K=Q; the retained
E(Q_p)[p]=0 gives it for K=Q_p. Indeed an invariant of order p^a would
yield an invariant of order p after multiplication by p^(a-1).
The maps to H^1(K,E) commute with i_n. Their kernels are respectively
the finite and infinite Kummer images, so the preimage of the infinite
Kummer condition is the finite one. This last statement holds at every
place even without local coefficient injectivity. It therefore preserves
all classical conditions away from p and gives alpha_n globally. At p
the coefficient map is injective as well, giving beta_n and the
zero-condition matching. These are precisely the coefficient
identifications imported from audited L061, with no extra torsion
restriction at bad primes.

In detail, represent the local finite Kummer class of [P] by the cocycle
sigma -> sigma(Q)-Q, where p^n Q=P. Its image under i_n is the same
cocycle with values in A. Multiplication by p^e at this fixed n is the
cocycle of p^e Q, a p^n-division point of p^e P. Thus the commuting
localization square carries p^e[P] to p^e f(alpha_n(c)), with n unchanged.
No downward transition to depth n-e is involved. Since beta_n is
injective, p^e I=0 in the k=2 branch forces the proposed finite test to
be zero. A nonzero test excludes exactly that branch; L061 then gives
rank one and the strict Selmer line. No Tate-module surjectivity is
needed anywhere in this finite-depth contradiction.

The boundary cases do not strengthen the conclusion. For e=0 the
quotient condition is D=D_div, so a finite localization image must be
zero; n>0 and a nonzero test still exclude k=2. For n<=e the point
quotient is killed by p^e, so the strict depth inequality only prevents
a vacuous test. Even at n>e, c=0 makes the test vanish regardless of
the branch. A zero result therefore gives no converse or stopping
criterion. A finite nonzero image when e>0 remains allowed and is
annihilated by the supplied exponent. Neither a witness, an effective
bound for that exponent, nor membership of the strict line in rational
Kummer space has been established by this audit. The precise Kim
citations and their unchanged applicability are imported through L061;
no fresh theorem discovery, source reproof or mathematical script is
needed for these checks.

## Mathlib

Full matching theorem and supporting divisible-group, finite-group,
coefficient-map and imported arithmetic coverage: not checked. No absence
is claimed. The elementary group argument and same-depth specialization
are proved here; Kim's arithmetic inputs remain precise named imports.
