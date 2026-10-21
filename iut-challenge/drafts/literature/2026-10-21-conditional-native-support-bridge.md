# Conditional same-member native reduction/support bridge

TARGET: Test whether, for every L089-L090 survivor and ordering and any prime ell>=7 with v_ell(j(E))>=0, S={p:v_p(j(E))<0} is the unique nonempty rational-prime support U avoiding 2 and ell such that E_o/C_o has multiplicative reduction at every place above U and good reduction at every place outside U away from 2ell.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step389's native-selected-support comparison searched exact IV good-reduction/2ell and selected-support terminology; reused steps368/382/385 and scoped L089/L090/L096/L097. No matching all-survivor conditional support theorem was identified; no novelty is asserted.
SOURCE_EVIDENCE: IUT I May 2020 reproduction https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf Definition 3.1(b),(c),(e) pp.61-63; IV April 2020 reproduction https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf Theorem 1.10 p.22 and Proposition 1.8(v) statement p.19/full proof p.20, inspected at step389; Silverman AEC second edition (2009) https://studylib.net/doc/28155304/the-arithmetic-of-elliptic-curves VII.5.5 pp.197-199 including characteristic two, reused from inspected step368/382 assessments. Reproduction/current-byte authentication remains unresolved.
COMPARISON: Known prime-to-residue full-torsion semistability and integral-j potential-good criteria cover the reduction methods. The difference is their application to the unchanged literal E_o at every actual C_o-place, then the selected-support predicate under the explicit extra ell-integrality assumption.
GAP: The conditional reduction classification and support uniqueness are unproved here; no actual height-selected ell-integrality, q-order coprimality, remaining initial data or exact-generation repair is supplied.
REASON: The source review isolated the ell exception; this bounded mathematical test can establish a usable conditional support bridge without assuming native initial data or repeating the weighted audit.
SCOPE: Exactly TARGET. The reduction clauses are only the selected multiplicative and complementary good-reduction predicates, with residue exclusions; they do not include all I Definition 3.1 clauses. Separate next-turn supervisor approval precedes mathematics.

## Inputs and justification for specialization

Retain audited L089 and L090: one arbitrary survivor E/Q, its fixed
c,h,d_*,e_*, both domains and fixed closure; all six full-coordinate
E_o, T=Q(E[2])=Q(t_o), G_o=T(iota,E_o[15]), C_o=G_o^nor over Q.
Every division field retains both coordinates of every geometric
torsion point. Use every actual finite C_o-place. L089's domain
gives integral j at two and its retained same-member local data give
v_3(j(E))=-30. L090 gives the same rational j for all E_o and native
F_mod=Q. No conclusion from an older curve or its selected singleton
is a premise.

The additional assumption is a prime ell>=7 with
v_ell(j(E))>=0. It is not claimed for the corollary's eventual
height-selected prime, and the retained full mod-seven image does
not select ell. Treat ell-integrality as a named conditional premise,
not an inferred consequence of the source. If no such premise is
available in a later native application, this result would remain
conditional rather than solving that application.

Import IV Proposition 1.8(v) as assessed in the completed comparison:
over each complete DVR field, full rational torsion at a prime level
>=3 invertible in its residue field gives semistability. Use level
three at residue characteristic five and level five elsewhere.
Verify rationality of the entire torsion module after each completion
before applying this theorem. Import Silverman VII.5.5 in its complete
perfect-residue-field scope, including characteristic two, for the
potential-good/integral-j test. Distinguish semistable good reduction
from semistable multiplicative reduction when applying the criterion;
no arbitrary potentially-good twist inference is allowed.

These general results have already been inspected, so repeating their
proofs or starting a broad literature search is unnecessary. The local
specialization still requires a rigorous proof in a canonical lemma
file if it succeeds. Neither a selected support nor the conclusion
of TARGET has been proved or imported by this assessment.

## Use and stop test

The main gap is original finite B>=A. The proposed intermediate result
would decide the reduction/support bridge under a transparent extra
assumption, allowing a later identification of L097's reduced divisor
with a native-style selected divisor. L097's inequality itself needs
no new audit here. A passing support test supplies no native
exact-generation equality or complete repair.

Continue only if every actual place is classified, S is nonempty and
meets the two residue exclusions, and both directions of support
uniqueness are proved using the exact good-reduction exceptions.
An unsupported reduction or a counterexample stops the claimed
bridge; save it without enlarging the assumptions silently. Do not
replace the ell assumption by ell=7 or claim q-order coprimality.

Independent gaps remain L092's factor-four relative excess, exact
generation/repairs, April reproduction authentication/current-version
and def= boundary, actual height-selected prime, stable pointed and
other independent initial data, native input/action/factorization/
pilot and essentiality. ATTEMPTS/035 stays parked. Full/supporting
Mathlib coverage is unchecked; no complete-solution candidate or
new mathematical result is asserted by this source assessment.

## Step390 — direct-source repair and separate scope approval

The URLs in SOURCE_EVIDENCE are copied from the inspected step389
comparison, whose source ledger and reduction-method comparison were read
for this repair. No fresh retrieval, new theorem inspection or current-byte
authentication is claimed. The first two links identify reproductions of
the primary IUT texts; the third identifies the inspected reproduction of
Silverman's book. The precise theorem/proof ranges and source qualifications
are unchanged. This supplies direct retrieval locations in this assessment
instead of requiring another assessment to resolve them.

The unchanged SPECIALIZE decision covers exactly TARGET, with the explicit
ell-integrality premise. It approves the separate mathematical attempt's
source scope, not its unproved reduction classification or uniqueness
conclusion. Known torsion semistability and the integral-j criterion are
to be cited, not reproved. The actual-place applicability argument is still
required. No additional literature search or derivation is needed for this
metadata repair; there is no new mathematical or source evidence.
The recorded use/stop test, downstream use, independent gaps and unchecked
Mathlib coverage above remain in force.
