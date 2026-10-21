# Quantitative pinned trace — critical-audit coverage

TARGET: Critically audit L221's O(N^(-1/2)) finite-diagnostic comparison, including killed-Green boundary control, monopole energy cutoff and complete heat summation.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the quantitative assessment and its parent review's exact-statement/stronger-result searches; narrowly searched the first-pair assessments and history/277–278 for duplicate audits, and read ATTEMPTS/022–025. Inspected L221 sections 1–7 for source requirements, L079 section 1 and L045 section 1 for imported hypotheses. No completed L221 audit was located in this scope.
SOURCE_EVIDENCE: Lawler–Limic, Random Walk: A Modern Introduction (Cambridge, 2010), author-hosted PDF accessed 2026-10-17: section 1.1 printed pp. 9–11, Theorem 4.3.1 pp. 81–84 including the simple-walk and bipartite passages and transient proof, and Proposition 4.6.2(a) p. 97 including its transient proof; reused the previous quantitative assessment's inspection.
COMPARISON: The scalar sources cover the asymptotic and killed-domain identity; L045 supplies the energy-projection framework and L079 supplies the exact trace and mode hypotheses. They do not certify L221's quantitative specialization. The separate audit may check that specialization without reproving the cited scalar theorems or claiming a known full matching trace theorem.
GAP: Verify all uniform constants, source cancellation, zero-extension errors, coefficient freezing, tensor normalization and complete heat summation in L221; no audit verdict or new mathematical estimate is established in this literature turn.
REASON: Essential source coverage for this exact audit is now complete. The remaining work is a bounded proof audit, with no blocked primary premise; readiness is distinct from correctness of L221.
LITERATURE_REASON: The new independent audit target required separate approval and source-hypothesis comparison after L221 was written; this is not repeated browsing of the already approved rate-calculation target.
SCOPE: Audit only L221 for SU(2), the relative pinned cube, straight lower-rooted direction-1 forest, a=8/N, tau=1/16 and actual probes i=3,6, with the finite diagnostic unchanged. No component-rate search or full-coefficient audit is covered.

## Inspected primary source and precise import boundary

Primary text: [Lawler–Limic, Random Walk: A Modern Introduction](https://www.math.uchicago.edu/~lawler/srwbook.pdf).
Theorem 4.3.1 assumes symmetric finite-range irreducible increments
in dimension at least three. It gives a leading inverse-power Green
term with O(|x|^-d) remainder, explicitly specializes to simple walk,
and handles bipartite walks on p. 82 via (4.4)–(4.5). The proof uses
local-limit estimates; its sharp error uses vanishing third moments.
Section 1.1 includes simple walk and gives its isotropic covariance.
Proposition 4.6.2(a) applies to any lattice subset in transient
dimension and subtracts the exit Green expectation. Its transient
proof splits visits before and after exit. These passages were read,
not inferred from search snippets. The recurrent case is unnecessary.

L221 uses the three-dimensional scalar Delta=6(I-P), after L078's
exact cancellation, rather than applying a scalar theorem to the
four-dimensional relative edge inverse. The factor 1/6 must remain
in both finite and infinite scalar kernels. This normalization and
the bounded-offset use of the asymptotic are explicit audit items,
not newly proved conclusions here. No reproof of the named inputs is
needed. No broader external source or unread lead is essential.

## What the local source comparison leaves to audit

Essential input IDs: L045 L070 L076 L078 L079 L221.
L045(5)–(6) identify energy projection with pinned end-edge energy;
their qualitative convergence contains no quantitative rate.
L079(4)–(6) state the polynomial mode bounds, exact diagonal pairing
and finite differentiated source. Those identities are the appropriate
starting point; this review does not re-audit upstream proofs.

The next audit must check all of the following in L221's actual order:

- Sections 1–2: fixed-radius signed source, exact zero mass, compact physical source set K, exit positions and all zero-extended output rows. Check bounded-offset subtraction without differentiating an uncontrolled asymptotic remainder.
- Section 3: the monopole lives in energy, the sampled cutoff is supported inside the pinned cube, and its projection error includes every normal end edge. Only the finite monopole receives an l2 norm.
- Sections 4–5: actual coefficient C1 bounds are uniform in axial level; freezing stays inside the source divergence; boundary coefficient extensions and transpose identities are justified. No rough prefix or Green column receives smoothness by assumption.
- Section 6: the L070 tensor orientations and diagnostic vertex average match L079; both signs, all mesh factors and polynomial mode dependence are checked before summing the full heat spectrum. Retain L078's separate O(N^2) error.

These are proof obligations, not conclusions of this source review.
The comparison found no known theorem making them automatic; the
existing bounded literature search does not certify originality.
Mathlib coverage of the full rate and supporting results remains
not checked, without an absence claim.

## Relevance, recorded failures and decision test

The main gap remains an ultraviolet-uniform interacting construction,
matched reflected error <=c_box/2, continuum axioms and finite positive
infrared mass. The intermediate audit tests the claimed quantitative
input |a^3 J_(i,N)-2 gamma D_(i,a)|<=C_i N^(-1/2).
If sound, it can support a later quantitative mixed-component estimate.
It leaves L080's diagnostic rate, L101's O(N^(27/10)) replacement and
other component rates independent and unresolved; no coupling-uniform
expansion or complete quantitative remainder is assumed.

ATTEMPTS/022–023 stop automatic parity and generic centering shortcuts;
ATTEMPTS/024–025 stop bulk axial-profile deletion and absolute-norm
power-gain shortcuts. This audit retains the finite diagnostic and
actual coefficient order, so those historical stops do not forbid it.
No new source blocker or duplicated completed audit was identified.

Continue to use L221 only if every claimed bound is uniform under its
actual hypotheses and the complete heat-summed rate survives. Otherwise
record the exact failed implication and a bounded repair or a reason to
park this rate. A failed upper-bound argument does not prove signed
response growth. This literature turn approves coverage only; the
independent mathematical audit remains the single next action.
