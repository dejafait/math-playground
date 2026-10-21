# Forgetting the distinguished root — source comparison

TARGET: Determine the normalization genus and fixed-minus-three lifting condition of the quotient that forgets the distinguished root.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L106/L107, their ready genus/quotient assessments, the saved duplicate search and ATTEMPTS/045–046/048; searched exact polynomial variants, Putz with (3,5,11) and quadratic factors, Belyi passport (5,5,1), unordered-pair covers and divided-difference twists; read the primary constructions below, with no inspected exact-instance genus or fixed-field classification found.
SOURCE_EVIDENCE: Dèbes–Fried, Pacific J. Math. 190 (1999), Sections 1.4–1.6 pp.51–52, especially (1.11); Putz thesis (2024), Section 4.3.2 pp.134–135, (4.3)–(4.5) and Proposition 4.18 with proof; Stacks 39.23.9 (03BM), 53.2.6 (0BY1), 59.28.1 (03PK), 15.116.2 (09EV); reuse ready L106/L107 Milne, finite-cover, Riemann–Hurwitz, genus and torsor coverage.
COMPARISON: Unordered-pair covers and symmetric-coordinate quotients are established methods. The inspected numerical genus and elliptic models concern different maps; they do not compute this quotient or its minus-three twist. The general method is covered, while the exact model, components, ramification and lifting specialization remain to be proved.
GAP: Identify the rational pair-only model and its fixed-minus-three marked companion, prove their relation to L106/L107 and their proper normalizations, and determine complete branch action, genus and normalized lifting criteria; no such calculation is established by this review.
REASON: Essential method coverage is available for the unchanged bounded target; specialize the cited general theorems in a later research turn without re-proving them or importing another map's genus.
SCOPE: Exactly TARGET for phi(T)=(3T²+T+1)^5(1−5T), including the distinct-root open and normalized boundary lifting; no rational-point classification, remaining-root lifting criterion, other quadratic field or L095 integer elimination.
LITERATURE_REASON: The saved REVIEW_REQUIRED target forgets r itself, outside the ready involution quotient scope; this review supplies the essential unordered-pair comparison and checks reuse of the covering and Kummer inputs.

## Gap, use and continuation test

The main gap remains open rational-point control and exclusion of both
L095 integer systems, within the larger unresolved Beal problem. The
intermediate target retains the unordered quadratic factor and forgets
the distinguished rational root. A simpler necessary rational-point image
of the existing genus-38 curve could support a later point calculation.
It need not settle the separate rational-root, power, gcd or positivity tests.

Essential inputs for the next attempt are audited L106's polynomial,
actual monodromy and branch data, and audited L107's invariant coordinates
and fixed-minus-three marking. Audited L108 is available only for later
boundary-image comparison; its boundary classification is not an assumption
about a different curve's rational points. Its unfinished nonrational
boundary-field decomposition remains preserved.

Continue this simplification if an exact rational model, all geometric
components, proper forgetful maps, complete normalization ramification and
reversible fixed-field lifting can be verified, and the unmarked genus is
strictly below 38. A hidden component, incorrect constant twist, or genus
at least 38 fails the proposed lower-genus diagnostic. Even a favorable
genus does not promise a feasible point method. Retain the existing
1000-label arithmetic cap; no class-group backend is needed for this test.

## Primary constructions compared

P. Dèbes and M. D. Fried, *Integral specialization of families of rational
functions*, Pacific J. Math. **190** (1999), no.1, 45–85,
[publisher PDF](https://msp.org/pjm/1999/190-1/pjm-v190-n1-p04-s.pdf),
**Sections 1.4–1.6, pp.51–52**, retrieved 2026-10-20.
The construction removes the diagonal of a twofold fiber product, takes
the swap quotient and normalizes; symmetric functions give the function
field. Section 1.5 applies the induced unordered-pair permutation action
and Riemann–Hurwitz, equation (1.11). Its example uses degree five,
geometric group S5 and four specified branch cycles. Its genus-zero
conclusion and Section 1.6's conic alternatives therefore do not apply
to L106's map. Theorem 1.2 concerns infinitely many reducible values in
a fixed fractional ideal, not this fixed-field incidence problem, and is
not imported. This is a primary precedent for the method; general
validity here rests on the cover and quotient theorems below. The
references [DF90a] and [Fri86] were not separately read this turn and
are not additional premises.

P. H. C. Putz, *Enumeration of local and global étale algebras applied to
generalized Fermat equations*, VU thesis (2024), version of record,
[DOI](https://doi.org/10.5463/thesis.832),
[primary PDF](https://research.vu.nl/ws/portalfiles/portal/367784086/Thesis_CasperPutz.pdf),
**Section 4.3.2, pp.134–135**, equations (4.3)–(4.5), Proposition 4.18
and its proof, retrieved 2026-10-20.
This is a related swap quotient using sum/product coordinates and an
elliptic model for the different degree-eight map in the (5,2,7) chapter.
Proposition 4.18 requires a number field not containing Q(sqrt(−91)),
distinct coordinates and a common rational image different from one.
Its proof checks exceptional birational charts and uses a computed
rational-point list. Neither that elliptic model nor its point conclusion
is imported. The ready L106 assessment already compares Putz's actual
Chapter 5 map and special-coefficient eliminations; those eliminations
remain outside coefficient one. No repeat of their computations is needed.

## General inputs and applicability obligations

Reuse the source versions and theorem-level readings in
`drafts/literature/2026-10-20-global-rational-quadratic-fiber-genus.md`
and `drafts/literature/2026-10-20-minus-three-unmarked-quotient.md`.
The target changes the root-label action, not those general theorems'
characteristic-zero hypotheses. The following Stacks statements and
indicated proof cases were also rechecked in current primary HTML on
2026-10-20.

1. [Stacks Proposition 39.23.9, tag 03BM](https://stacks.math.columbia.edu/tag/03BM):
   affine groupoid, finite locally free source/target and an equivalence
   relation give the invariant-ring fppf quotient. The inspected proof
   uses flat base change of invariants and faithful flatness. Verify the
   free swap action on the actual distinct-pair open and identify its
   invariant ring. This does not assert freeness at a closure's boundary.
   Forgetting r is an incidence-cover map; it must not be presented as a
   new finite-group action on L107 without proof.

2. [Stacks Theorem 53.2.6, tag 0BY1](https://stacks.math.columbia.edu/tag/0BY1):
   transcendence-degree-one function fields correspond to nonsingular
   projective curves and nonconstant morphisms. The proof extends maps
   from nonempty opens uniquely. Establish the relevant function-field
   inclusions, geometric integrality and full constants before applying
   it to the pair curves and forgetful maps. In characteristic zero the
   nonsingular models are smooth. Normalize the closure of the specified
   open, not every component of unsaturated equations.

3. Reuse Milne, *Lectures on Étale Cohomology*, v2.21 (22 March 2013),
   **Theorems 3.1 and 21.3, pp.27,130–131**,
   [author PDF](https://www.jmilne.org/math/CourseNotes/LECc.pdf), and
   [Stacks Theorem 58.6.2, tag 0BND](https://stacks.math.columbia.edu/tag/0BND).
   Over the connected branch-complement open, finite étale covers and
   their morphisms correspond to finite fundamental-group sets. Apply
   this to the actual pair-label action and its incidence with L107,
   using L106's established monodromy. Verify transitivity and rational
   descent of the marked twist; geometric labels alone do not fix its
   Q-form. No new monodromy theorem is needed.

4. Reuse [Stacks Lemmas 53.12.2 and 53.12.4, tag 0C1B](https://stacks.math.columbia.edu/tag/0C1B),
   [53.8.2, tag 0BY6](https://stacks.math.columbia.edu/tag/0BY6), and
   [53.18.2, tag 0CE0](https://stacks.math.columbia.edu/tag/0CE0).
   Riemann–Hurwitz requires smooth proper curves and a generically étale
   map with the indicated full constants; tame ramification contributes
   e−1. Compute every induced cycle over all branch values, including
   infinity. Verify all components before reporting a genus. Normalization
   genus, arithmetic genus of an equation and the old marked genus are
   different data. The complex punctured-disk comparison is already
   assessed in L106's source notes; import it with its applicability
   explanation rather than re-proving Riemann existence.

5. [Stacks Lemma 59.28.1 and its cohomology sequence, tag 03PK](https://stacks.math.columbia.edu/tag/03PK)
   require the root degree invertible; the proof adjoins a root of a unit
   by a finite free étale algebra. Reuse torsor triviality/section
   equivalence from **21.4.2–3**, [tag 03AG](https://stacks.math.columbia.edu/tag/03AG).
   Apply at degree two only after identifying the actual marked function
   field and its constant twist from Q(sqrt(−3)). Reuse L107's
   discriminant convention; verify its counterpart on the new curve in
   both directions. An arbitrary rational quadratic factor does not
   establish the prescribed field or restore a rational root.

6. [Stacks Lemma 15.116.2, tag 09EV](https://stacks.math.columbia.edu/tag/09EV),
   parts (1)–(5) and the DVR proof, treats a root of a uniformizer and its
   integral closure/ramification. Together with 03PK's unit-root case it
   supports boundary charts after separating valuations and units.
   These are valuations of a curve over Q, with characteristic-zero
   residue fields. Verify the new double cover's boundary ramification
   rather than importing L107's freeness. At rational boundary points
   the lifting condition must use the normalized local unit and handle
   any ramified case found. Direct substitution into a zero or pole of
   an affine discriminant is insufficient.

These are imported general results. The necessary additional work is
instance-specific invariant algebra, rational twist identification,
complete finite permutation arithmetic and local normalization charts.
No reproof of the source theorems is justified. Mathlib coverage is not
checked; no full matching theorem or absence from Mathlib is claimed.

## Searches, duplicates and preserved stops

External queries included `Putz (3,5,11) quadratic curve`, exact polynomial
variants `(3t^2+t+1)^5(1-5t)` and `3*T^2+T+1` with `1-5*T`,
`Belyi 11 5,5,1 genus`, `polynomial unordered pairs genus monodromy curve`,
and `fiber product quadratic twist divided difference curve`.
The pair-cover search led to the Dèbes–Fried primary text. Exact-instance
queries supplied no matching inspected result; unrelated hits and
snippets are not theorem evidence. A Neftin-hosted dissertation and
papers on general reducibility/genus appeared as leads but were not
read or used. No originality is inferred from this bounded search.

The saved local discovery already searched October 18–20 route assessments,
October 20 attempt notes, histories 360–369, L103–L108 and ATTEMPTS/04*
for forgetting r and pair-only covers without finding a completed match.
This turn checked the relevant L106/L107 proof ranges and ready source
notes and read ATTEMPTS/045, the minus-three ATTEMPTS/046, ATTEMPTS/048
and history/372. L107 retains r and does not calculate this target.
The L101 direct-scaling stop, L097 octic irreducibility stop, class-backend
park and exact seven-adic joint-factor witness remain unchanged. This
pair-incidence target tests a different mechanism; no old route is
reopened by renaming it. No sibling notebook was read.

The former REVIEW_REQUIRED proposal is preserved in substance by the
unchanged TARGET, downstream use, inputs and strict genus threshold.
This assessment supplies method readiness only: no quotient equation,
genus, twist formula, boundary classification, new lemma or mathematical
script was produced. The ready specialization is for a later invocation
after the supervisor's separate approval. Both L095 systems, remaining
global factors, minus-eleven and the main Beal gap remain open.
