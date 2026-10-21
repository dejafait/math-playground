# Mod-7 image after global torsion adjunction — source comparison

TARGET: Determine whether L046's curve has mod-7 image containing SL_2(F_7) over F=Q(zeta_60,E_0[30]) from L045.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Targeted mod-7/adjunction assessments, histories 143,146,150 and ATTEMPTS/022,025,026,027 supply no duplicate restriction result; searches for SL2 normal subgroups and elliptic mod-l restriction identified Conrad and Milne, inspected below.
SOURCE_EVIDENCE: Inspected Milne Fields and Galois Theory v5.10 (September 2022), Theorem 3.17 and Propositions 3.19,3.21, printed pp.39–42; Conrad Simplicity of PSLn(F), author-hosted 9-page version retrieved 2026-10-11, Theorem 3.3 and its complete proof, p.4; reuse L045/L046's audited full-coordinate representation inputs.
COMPARISON: Known compositum restriction and elementary-unipotent generation cover the required mechanism; only their application to the same L046 curve and L045 field remains, without a new subgroup-classification theorem or disjointness assumption.
GAP: Next verify the actual restricted image is normal of index prime to 7 and apply the cited generation result through the finite quotient; this source review does not establish the containment.
REASON: Essential coverage is now inspected; approve one known-method specialization of the unchanged target, deferring its mathematical derivation to the next turn.
SCOPE: Exactly TARGET, using the same reselected E_0 and full coordinate fields, with no assumption of linear disjointness or full GL_2 image over F.

## Original proposal and relevance (preserved)

The original gap is finite B>=A. The intermediate question could
join L046's global image over Q to L045's global rational 30-torsion
and retained H,N completions, as one more initial-data prerequisite.
It does not address the numerical comparison or provide sufficient
initial data. Essential local inputs for a later attempt are L046
and L045, with audited L044 and its retained L042 packet. L045 is
to be applied to the reselected L046 curve, not to an independently
chosen approximation. Check its exact hypotheses before doing so.

The initial REVIEW_REQUIRED proposal requested that the comparison retrieve a primary theorem governing
images on restriction to finite Galois extensions, or the precise
finite-group facts needed for this GL_2(F_7) case, and compare all
hypotheses with L045's stated degree divisibility. It must distinguish
mere prime-to-7 extension degree from stronger image hypotheses and
must not assume disjoint division fields. Approve only the precise
covered specialization; if the stated inputs are insufficient, record
the missing condition or an independently testable obstruction.
No group-theoretic implication is proved or approved in this proposal.

Global surjectivity after restriction, effective coefficients,
geometric-parameter/full initial data, native/input/action, pilot
transport, essentiality and original finite B>=A are not assumed.
ATTEMPTS/022,025,026,027 remain intact. No cross-notebook input is
needed. Full matching Mathlib coverage for this target is unchecked.


## Inspected primary coverage and qualifications

J.S. Milne, *Fields and Galois Theory*, v5.10, September 2022,
[author PDF](https://www.jmilne.org/math/CourseNotes/FT.pdf),
Theorem 3.17(b),(d), printed pp.39–40, provides subgroup index/degree
and normality/quotient correspondence. Proposition 3.19, pp.40–41,
identifies restriction from a Galois compositum over the second field
with the Galois group over the intersection. Its proof checks both
injectivity and surjectivity by the fixed field of the image.
Proposition 3.21, pp.41–42, says the intersection and compositum of
two Galois extensions are Galois; the proof checks normality and
separability by roots of minimal polynomials. All statements and
these proof cases were read. The next specialization uses the full
7-coordinate field and F inside the same Q-bar, both finite Galois
over Q. Tower degree divisibility, rather than disjointness or an
upper bound on degree, is the relevant test. Reuse L045's inspected
full-coordinate kernel coverage; no new absolute-Galois theorem is
needed beyond finite Galois restriction and extension of embeddings.

Keith Conrad, *Simplicity of PSLn(F)*,
[author PDF](https://kconrad.math.uconn.edu/blurbs/grouptheory/PSLnsimple.pdf),
9-page version retrieved 2026-10-11 (no version date printed),
Theorem 3.3, p.4, states generation of SL_2 over any field by upper
unipotents and their conjugates, with at most four upper/lower
unipotent factors. Read the full proof and inspected the rendered
page: it handles separately nonzero upper off-diagonal entry,
nonzero lower off-diagonal entry, and diagonal matrices, and displays
the conjugation exchanging upper and lower subgroups. No restriction
on field size is required for this theorem. Theorems 3.4–3.5, p.5,
about perfectness and simplicity were also inspected but are
unnecessary for the selected mechanism. Import generation without
reproving the factorization. The later application must check orders
of the elementary matrices and use Lagrange's theorem in the finite
quotient; those specific checks are deferred, not derived here.

## Local applicability, duplicates and stopping evidence

Read the full relevant L045 statement and degree proof and L046's
hypotheses/conclusion and imported-input passage. L045 allows any
qualifying L044 E_0, so the same reselected L046 E_0 is permitted.
L046 retains that curve's full local 210-torsion module. L045 states
F/Q Galois and degree dividing 2^14*3^3*5, and does not assert a
restricted mod-7 image. No effective coefficients, extra curve
selection or new local realization is required for this target.

Specific local searches for restricted image, SL_2 and prime-to-7
conditions found only the pending proposal and the earlier Q-image
and torsion-adjunction coverage. No duplicate proof was found in
these checked paths; this is not a novelty claim. The packet stops
ATTEMPTS/022,025,026 and exact-curve stop ATTEMPTS/027 concern other
realizations and stay intact. The new target changes none of them.

Searches on 2026-10-11: “SL2 finite field perfect PSL2 simple theorem
normal subgroup prime to p index” and “elliptic curve mod l image
finite Galois extension degree prime to l SL2 restriction”. Search
snippets and a secondary reference request were discovery leads only.
No subgroup-classification citation from those leads is imported.
Conrad's direct generation theorem is sufficient source coverage;
the finite Galois comparison reuses and rechecks Milne.

## Approved continuation and discriminating test

The exact TARGET is now SPECIALIZE. Next write only its cited
application, with essential inputs L046 and L045 applied to the
same E_0, retaining audited L044/L042 and Omega,H,N. Verify the
finite restriction identification, normality and index divisibility,
then check that the elementary generators satisfy the required
finite-quotient test. Success closes this large-image prerequisite
only. Failure of any of those obligations stops this mechanism and
must identify the missing condition; prime-to-7 degree alone is not
to replace the Galois hypothesis. Do not assert full GL_2 image over
F, disjoint division fields, geometric-parameter/full initial data,
actual/native input/action, marked pilot transport, essentiality or
finite B>=A. Those independent gaps remain open.

This literature-only turn proves no new lemma and changes no
mathematical script, DAG edge or argument overview. No reproof of a
known theorem is authorized or needed. Full matching Mathlib coverage
and supporting theorem names were not checked; no absence is claimed.
