# Auxiliary quadratic modification — source scope approved

TARGET: Determine whether, for a cross-residue difference D=r_j-r_i from L076 and s in H with s^2=D, the embedded field F'=F_aux(s) gives L074's corresponding ordered-root Legendre model full rational 15-torsion while F'_u=H and F'(E_aux[7])_w=N.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step300 compared the local ordered-root and global torsion-adjunction assessments, L073/L074/L076, history/296/299 and ATTEMPTS/027,028,031,032,033; searched Milne completion finite extension compositum Kw Lw and Milne elliptic curves Legendre roots square isomorphism 2.4 on 2026-10-18. The needed standard completion statement was located; no novelty inference or new classification search is needed.
SOURCE_EVIDENCE: Reopened Milne, Algebraic Number Theory v3.08 (19 July 2020), section 8 introductory completion argument p.135 and Propositions 8.1–8.2 with both place/factor directions and the canonical tensor-map proof p.136. Reuse the inspected Milne, Elliptic Curves second edition (2021), II Theorem 2.4(b) pp.52–53 and full-coordinate torsion coverage from the 2026-10-17 ordered-root and 2026-10-11 torsion-adjunction assessments.
COMPARISON: Known finite-separable completion and pointed-coordinate theorems cover the general mechanisms; the new task is their application to one embedded quadratic adjunction and its corresponding ordered-root model. No general compositum theorem, new twist classification or reproof is required.
GAP: Coverage is ready; the combined torsion and two embedded completion assertions remain to be proved in a separate research turn. Exact native generation and all independent IUT prerequisites remain outside scope.
REASON: The missing changed-field source coverage is now supplied and compared with reusable coordinate coverage. Proceed to one mathematical specialization of the unchanged target; this literature turn establishes no changed-field verdict.
SCOPE: Exactly TARGET, for the same L073 auxiliary witness, a chosen L076 cross-residue difference and its square root in the fixed H embedding, with both coordinates of full torsion and induced places; no native generation, global Galoisness or retained-witness conclusion.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED because a global field adjunction and its induced completions were excluded from the ready local-square assessment; this turn fills that essential scope gap.

This is a ready source assessment, not a mathematical attempt or a
proved field construction. Inputs are L073's same E_aux, F_aux, H and N, L074's ordered
roots and monic Legendre equations, and L076's cross-residue square
root in the fixed embedding. The selected root s must be considered
inside that embedding, rather than by an abstract extension-degree
comparison. Both coordinates of all division points remain part of
the field convention. The place symbols refer to the places induced
by this embedding on the proposed fields.

The positive test requires all three assertions in TARGET for one
and the same D, s and auxiliary curve; a failure of embedded completion
equality or of the pointed coordinate transfer stops that construction.
An insufficient theorem is a coverage gap, not evidence of failure.
Potential downstream use is a field on which a literal Legendre model
and the preserved local packet can be examined together. No exact
native generation statement is included: F'=T(i,E_L[15]), identification
of native T/model, independent initial data, actual input/action,
marked factorization, pilot transport, essentiality and finite B>=A
would still need independent work.

Preserve ATTEMPTS/027,028,031,032,033. This does not globalize the exact
curve with q=3^30, reopen the marked-coordinate or tensor objections,
or undo L075's exclusion for the unchanged F_aux. Retained E_0,F,
K_glob,Omega,embedding,u,w,H,N,q_0 are not reselected; the proposed
extension concerns only the auxiliary witness. Neither q_aux=q_0 nor
q_aux=3^30 is assumed. Mathlib coverage for the proposed combined
target has not been checked.

## Primary completion theorem and applicability boundary

[Milne, Algebraic Number Theory v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
section 8 pp.135–136, treats a finite separable extension L=K[alpha]
and an archimedean or discrete nonarchimedean absolute value on K.
At a chosen extension, its completion is K-hat[alpha]. The argument
uses completeness of finite extensions; its converse constructs the
place from an irreducible factor over K-hat. Proposition 8.2 gives
the product of all completions and its canonical tensor map. Neither
Galoisness nor linear disjointness is assumed. Both directions and
the full tensor-map proof were read on 2026-10-18, PDF pp.136–137
(printed pp.135–136). Import these statements, without reproof.

This is the same general input inspected in
`drafts/literature/2026-10-11-global-torsion-adjunction-preserving-completion.md`.
The new comparison is at an induced place, not an arbitrary factor
of the tensor product. The later application must use finite extensions
inside the fixed Omega throughout, identifying the chosen image of the
adjoined root and checking the completions for the base field and for
the full seven-division field separately. Separability is automatic in
characteristic zero. A global extension degree need not equal a local
extension degree; no degree comparison can replace this check.

## Coordinate coverage reused and remaining specialization

Reuse the ready source comparison in
`drafts/literature/2026-10-17-auxiliary-ordered-legendre-obstruction.md`:
[Milne, Elliptic Curves (2021), II.2.4(b)](https://www.jmilne.org/math/Books/EC2.pdf)
covers the invertible pointed Weierstrass changes and extension at
infinity. L074 already writes both directions for each root ordering.
Its general coordinate theorem does not require a nonsquare scale;
it is applicable over characteristic-zero extensions too. Rational
pointed group isomorphisms transport the complete torsion group,
not just x-coordinates. Reuse the full-coordinate convention and
rational group law coverage of the earlier torsion-adjunction review.
No new quadratic-twist representation proof is needed here.

The research step must select the row matching D, verify that the
actual map and inverse are defined over the proposed F', and transport
all geometric 15-torsion from the same E_aux. It must then express
the proposed seven-division extension using the original curve's full
coordinate field and the same adjoined root, applying the cited
completion theorem at its induced place. This is a checklist of
unproved specialization obligations, not a derivation of their answer.
L073 supplies the original rational torsion and H,N; L074 supplies
the row and maps; audited L076 supplies the root in H. No assertion
about the third local difference or native T is needed for this test.

## Duplicate/failure comparison and decision

L075's obstruction fixes F_aux; the proposed changed field falls
outside its conclusion. The searched local records propose modifications
but do not prove this combined target. The earlier global adjunction
assessment supplies a reusable mechanism, not the present conclusion.
ATTEMPTS/027 concerns the exact transcendental-j Tate curve;
ATTEMPTS/028 concerns a different universal-model predicate;
ATTEMPTS/031 and /032 retain independent marking/enclosure stops;
ATTEMPTS/033 parks redundant classification retrieval. None is reopened.
A narrow search also used a nonexistent literature filename glob;
that diagnostic supplied no evidence and is not counted as coverage.

Continue to mathematics with SPECIALIZE / REPRODUCTION. A positive
result would remove this particular local-packet obstruction to working
with a literal Legendre model over a larger auxiliary field. It would
not establish F'=T(i,E_L[15]), native admissibility, or an IUT flaw.
Stop this construction if any of TARGET's three requirements fails;
insufficient proof remains unresolved rather than a negative verdict.
Full matching Mathlib coverage was not checked; source theorem coverage
is sufficient for this informal specialization and claims no absence.
