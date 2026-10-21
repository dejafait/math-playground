# Minimal factor existence — critical-audit source coverage

TARGET: Critically audit L053's locally free factor existence at the exact real h, checking Yoshioka generality, nonprimitive defect strata and endpoint stability.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the factor-existence assessment and searched the specific arbitrary-vector simple-sheaf dimension input exposed by L053; inspected Yoshioka Sections 1.1–1.3 and checked Mukai source access.
SOURCE_EVIDENCE: Yoshioka math/9907001v2 Section 1.1 (p. 4), Lemma 1.5 and proof (p. 5), Lemma 1.7 and proof (p. 6); reused previously inspected Theorem 0.1, Corollary 0.3, rank-one proof case, Ellingsrud–Lehn Theorem 1 and O'Grady Section 3. Mukai's original publisher page supplies bibliographic data only.
COMPARISON: Existing primary coverage supports an audit of general integral polarizations, arbitrary-vector stable loci, quotient-stack dimensions, every finite-length defect and rational chamber transfer; no source directly states L053's exact irrational-endpoint conclusion.
GAP: Audit the specialization rather than assume its correctness: generality of the chosen integral ray, purity and scalar accounting in the nonprimitive defect argument, and strict stability at h remain to be checked mathematically.
REASON: The missing comparison is now supplied by the already relevant arbitrary-vector stack statements; source access failure for Mukai does not block an audit using these and the written trace-free deformation argument.
SCOPE: Critical audit only of L053 for c_2=5,6, using L044 and L052; no new existence mechanism, global product construction or transport.
LITERATURE_REASON: The new audit exposes arbitrary-vector stable-moduli dimension and scalar-stabilizer scope, which the old existence assessment did not compare explicitly with L053's written proof.

## Reused coverage and focused primary reading

Reuse [the factor-existence assessment](2026-10-05-minimal-survivor-stable-factor-existence.md) for its inspected existence, rank-one filtration exception, Quot and wall inputs. No general existence search was repeated. L052 is a necessary filter, L050 supplies topological existence only, and L051's boundary exclusion concerns another pair; none duplicates the audited factor conclusion. Earlier presentation and fixed-class failures and the parked Nakashima source remain intact.

[Yoshioka, math/9907001v2, 7 February 2000](https://arxiv.org/pdf/math/9907001v2), Section 1.1, states the bounded semistable stack is a quotient of an open Quot subscheme by a general linear group. Lemma 1.5 is explicitly for arbitrary positive rank, under the standing general-polarization condition and its square/divisibility bound; its proof refers the rank-one filtration case elsewhere. Lemma 1.7 explicitly omits primitivity, assumes positive square, and gives semistable-stack dimension v²+1 as well as stable nonemptiness. Read its induction and extension-count proof. These statements support dimension auditing without treating the primitive introductory moduli discussion as an arbitrary-vector theorem. The quoted total dimension alone does not establish purity of every stable component; audit the written simple-sheaf deformation argument for that claim.

[Mukai, Inventiones mathematicae 77 (1984), 101–116, DOI 10.1007/BF01389137](https://link.springer.com/article/10.1007/BF01389137) was accessible only as a subscription preview and bibliography. The author-hosted Sugaku translation (1988, originally Japanese 1987) opened its introductory pages, but relevant text requests timed out; screenshot calls supplied no readable theorem content here. The author-hosted Tata PDF returned no extracted text. Local curl failed DNS. None is counted as inspected theorem evidence, and no purchase or authentication was attempted. Mukai's named simple-sheaf smoothness theorem remains L053's citation; this review adds no theorem number inferred from secondary snippets. The available Yoshioka stack statements and L053's explicit trace-free argument suffice to make the critical audit independently testable.

## Approved audit and discriminating test

Read L053 in full and the necessary L044 metric and L052 lattice passages. Check the common integral ray against the actual generality definitions, keeping persistent nonprimitive equal Hilbert polynomials separate from walls. Check both Chern values and every possible defect length, hull stability and boundedness, relative Quot coverage, scalar automorphisms and the use of pure dimensions. In the endpoint passage distinguish the larger 24-wall set from actual equality-slope classes, and check that continuity is applied to each fixed subsheaf.

Continue using L053 as a factor input only if all three passages survive. If any fails, preserve it, identify the unsupported implication and route a precisely scoped repair; failure of this proof would not establish nonexistence. No reproof of Yoshioka, Quot irreducibility or chamber stability is authorized. Checking the local applicability arguments is necessary because no inspected theorem states this exact h conclusion.

The plausible downstream use is factor availability for the minimum pair (-9,-10), not restrictions of an already constructed product bundle. Essential input IDs are L053, L044 and L052. Compatible global mixed-tensor realization, product stability, transverse transport and universal primitive-Hodge algebraicity remain independent unresolved assumptions. Span 21 and three attained RM directions are unchanged. This approval is source coverage, not the completed mathematical audit.

## Mathlib

Full matching stable-bundle existence, stack dimensions, Quot and real endpoint coverage: **not checked**. No absence or matching declaration is asserted.
