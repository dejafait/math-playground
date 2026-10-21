# Depth-two eligibility after the finite residual defect

TARGET: Assess whether Sakamoto's all-depth primitive rank-zero systems guarantee a residual nonzero two-prime index supported in P_(2,0), assuming Selmer corank two and zero finite Selmer quotient.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the local construction and finite-defect assessments; searched Mazur Rubin Kolyvagin systems Corollary 4.1.9 pdf and Sakamoto "Pm,n" "Kolyvagin" restriction; inspected the published Sakamoto statements and the cited Mazur--Rubin core-vertex and Chebotarev cases.
SOURCE_EVIDENCE: Sakamoto, Doc. Math. 27 (2022), DOI 10.4171/DM/X21, Section 2.3 (p. 1902), Theorem 2.20/Remark 2.21/Corollary 2.22 (p. 1904), Proposition 3.19 and proof (pp. 1915--1916), Lemma 4.2 (p. 1917), Proposition 4.7/Theorem 4.8 (p. 1919); Mazur--Rubin, Kolyvagin Systems, Mem. AMS 168 (799) (2004), Section 3.5, Proposition 3.6.1 and its p>4 proof case (pp. 27--31), Corollary 4.1.9 (p. 38).
COMPARISON: Theorem 2.20 and the proof of Corollary 2.22 detect a unit on N_(m,n) for a basis, using Remark 2.21; Proposition 3.19 supplies compatible bases at all depths from residual nonvanishing. Theorem 4.8 counts a divisor-minimal residual witness without replacing its prime factors. These cover the stronger eligibility mechanism; its exact coefficient specialization is reserved for research.
GAP: Write the depth-two application and scalar reduction with compatible normalizations, then apply residual divisor minimization and L021 with zero finite quotient; no new existence theorem or arithmetic realization is needed for this conditional test.
REASON: Approve a bounded specialization of the inspected detection, compatibility and residual-count theorems; do not reprove their Chebotarev or system-rigidity machinery, and do not remove the granted finite-quotient condition.
LITERATURE_REASON: Changed essential prime-set hypothesis from P_(1,0) to P_(2,0) requires a separate source comparison before any dependent mathematical attempt.
SCOPE: Retain L021's ordinary, non-anomalous, residual, local-torsion, Manin and Tamagawa hypotheses and residual-family nonvanishing; additionally grant S/S_div = 0. Do not assume finite Sha, rational rank two, complex-to-corank equality or a P_(2,0) witness.

COVERED_TARGET: Specialize Sakamoto's unit detection and compatible reduction to produce a divisor-minimal residual two-prime index in P_(2,0), retaining L021's hypotheses and zero finite Selmer quotient.

## Main gap, intermediate target and test

The main gap remains rank E(Q) = m(E) for arbitrary analytic order at
least two. The intermediate target is conditional production of the
eligible two-prime index, for the fixed-prime application in L015 and the
lifting route in L018. It supplies neither analytic-to-corank comparison
nor rational membership. L021 remains the input for residual dimension
two after granting zero finite quotient. Its finite-defect obstruction in
ATTEMPTS/021 remains valid; this target does not reopen that inference.
The existing construction assessment covered fixed eligible primes but
not their production. No duplicate production lemma was located in the
specific assessments, L015/L021 and history/038 inspected here.

Continue with the bounded cited specialization if the actual common-index
scalar reduction preserves units and divisor minimization keeps support
in P_(2,0). Stop that application if either map has a nonunit factor or an
essential hypothesis cannot be retained. Neither arbitrary prescribed
primes nor a fixed depth-two unit scalar is asserted by primitivity.

## Primary source ledger

The published Sakamoto PDF is the received 2022-05-13, revised
2022-07-20 text at
[EMS](https://ems.press/content/serial-article-files/29299?nt=1).
Section 1.1 retains p>3, good ordinary reduction, surjective E[p] and
p prime to #E(F_p) and the Tamagawa product. The local target also retains
its Manin and local-torsion assumptions. Section 2 uses
R = (Z/p^m)[Gal(Q_n/Q)] and T = Ind(E[p^m]); at n=0 these are the
requested coefficient ring and elliptic representation. Section 2.3,
p. 1902, defines P_(m,n) by cyclic E(F_ell)[p^m] of order p^m and
ell congruent to 1 modulo p^max(m,n+1). This is the precise stronger
prime set, rather than all residual Kolyvagin primes.

[Theorem 2.20(2), Remark 2.21 and Corollary 2.22, p. 1904](https://ems.press/content/serial-article-files/29299?nt=1#page=14)
are the essential detection coverage. For a basis, the scalar ideal at d
is the initial Fitting ideal of the dual modified Selmer module. Remark
2.21 gives residual-zero modified Selmer indices in N_(m,n) for a
nonnegative-core-rank structure; the proof of Corollary 2.22 expressly
uses one such index and obtains a unit scalar there. The classical
structure is self-dual and Cartesian (Corollary 2.15), so this is the
source's arithmetic application, not a new assertion about an arbitrary
restricted set. Injectivity alone over Z/p^2 would not establish unit
detection; the actual proof supplies the stronger statement needed.

[Proposition 3.19 and proof, pp. 1915--1916](https://ems.press/content/serial-article-files/29299?nt=1#page=25)
equates residual scalar nonvanishing somewhere with basis status at
every (m,n). Its proof defines the inverse-limit system module, records
surjective canonical finite-level projections, and explicitly places the
constructed family in that inverse limit. This supplies coefficient
compatibility on common indices; it does not assert a unit at every
index. Theorem 3.17 identifies its scalars with the rank-zero derivative
of the normalized modular-symbol family. Lemma 4.2, p. 1917, identifies
residual scalar nonvanishing with the Kurihara number. The later application
must retain the same generators of G_ell and rank-one quotient bases;
G_d is unchanged on a common index, not replaced by a tensor containing
an extra p factor.

[Proposition 4.7 and Theorem 4.8 with proof, p. 1919](https://ems.press/content/serial-article-files/29299?nt=1#page=29)
are applicable to a residual index in the larger N_(1,0). Their proof
selects divisors, not new primes. This is the exact support-preservation
case needed after restricted detection. Self-duality is essential in
Lemma 4.6 and is emphasized in Remark 4.9; analogues for ideal class
groups cannot be imported. Combining these sources with L021 is the
approved future mathematical work, not a result derived in this review.

## Essential existence machinery checked

Mazur--Rubin, *Kolyvagin Systems*, Mem. AMS 168 (799) (2004),
[primary text mirrored at IMJ](https://webusers.imj-prg.fr/~christophe.cornut/ES/Ref/KolySys.pdf),
Section 3.5, pp. 27--28, requires a free finite-rank representation,
absolute residual irreducibility, a cyclotomic-trivial tau with free
rank-one Frobenius quotient, two Galois cohomology vanishings, either
residual non-self-duality or p>4, a prime set containing a sufficiently
deep Kolyvagin set and contained in the residual set, and Cartesian
local conditions. Sakamoto, p. 1896, records (H.0)--(H.3) for its induced
module; p>=5 supplies (H.4b), and its Section 2.3 and Corollary 2.15
provide the arithmetic prime set and Cartesian application. We rely on
his explicit Remark 2.21 at arbitrary (m,n), rather than claiming that
an arbitrary thin subset satisfies Mazur--Rubin's prime-set hypothesis.

Inspected Proposition 3.6.1, pp. 30--31, and the relevant p>4 proof
case: nonzero cocycles remain detected after restriction and projection
by (H.1)--(H.3); each forbidden coset has measure at most 1/p. Four such
cosets do not cover the group for p>=5. Chebotarev then produces
positive-density detecting primes at the chosen coefficient depth.
This case does not require the non-self-dual (H.4a) alternative.
Corollary 4.1.9, p. 38, with Chapter 4's (H.0)--(H.6) hypotheses,
produces core vertices in arbitrarily deep allowed sets; its proof uses
this detection and Lemma 4.1.7(iv). These are named theorem imports,
not grounds for reproving Chebotarev or the connectivity theorem.

The AMS and UCI PDF endpoints failed in the browser; the complete
needed statements and relevant proof case were accessible in the
primary-text mirror, so there is no essential source blocker. The exact
search did not supply a stronger unconditional BSD conclusion; this is
not evidence of novelty. The previously inspected Kim decomposition is
reused through L021, with no changed hypotheses. Mathlib coverage of
these system theorems was not checked; no formal matching theorem is
claimed.

## Authorization and limits

DECISION SPECIALIZE covers the original TARGET and the exact
COVERED_TARGET above. No lemma, mathematical script or new implication
was written this turn. A later research turn must write the complete
conditional application in its canonical lemma, including the scalar
map and support checks. No reproof of the standard source results is
justified. No choice of numerical primes is required for this existence
test. Production of corank two and zero finite quotient from complex
order two, rational membership and higher ranks remain independent gaps.
