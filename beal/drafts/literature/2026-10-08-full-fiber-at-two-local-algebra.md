# Complete fiber at two — local-algebra comparison coverage

TARGET: Certify whether L035's whole fiber B_2 is isomorphic to A over Q5, using complete local factor data and accounting for every factor.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the distinctive constant 24729001 with modular-curve/local-five terms, X0(11) with j=2, FNS with 54a1/local-five, and defining-polynomial coefficient terms; searched the relevant local lemmas, ATTEMPTS/008–011 and history/097; no completed B_2 comparison or inspected exact-pair theorem was identified.
SOURCE_EVIDENCE: Reused the primary statements and full relevant proof cases inspected in drafts/literature/2026-10-08-full-fiber-at-one-local-algebra.md: Milne ANT v3.08 Theorem 7.33, Corollary 7.42, Proposition 7.50 and Proposition 7.60; Clark ANT II Theorems 1.79, 2.38 and 2.41; FNS final author manuscript June 10, 2019, Section 7.2, Table 5, equation (7.4) and Lemma 7.6.
COMPARISON: Known local-field results cover complete coprime factor lifting, unramified classification and certified Hensel–Krasner field identification; the changed scalar requires its own coordinate and factor certificates, which neither the sources nor L038 supply.
GAP: B_2's coordinate reconstruction, complete factor data and algebra comparison remain uncertified; matching ramified degrees or stabilized finite-precision output would not establish an isomorphism.
REASON: L038 exhausts j=1 only; j=2 is an independently testable scalar already included in L036, with a complete pairing potentially supplying compatible-image nonemptiness.
SCOPE: Exactly the fixed j=2 whole-fiber comparison with L033's entire A, L034's map and L035's interpretation; certify all coordinate exceptions and all factors. No varying-scalar image decision, global Selmer computation, GRH, rank, Sha, global basis or arbitrary precision cutoff.

## Main gap, input scope and recorded failures

The main gap remains global emptiness for residual signatures; even ordered
(3,4,11) has five surviving twists. This intermediate test addresses the
missing concrete realization in the local-five whole-fiber-compatible
image, not global emptiness. Inputs are L033 (entire degree-twelve A),
L034 (complete map and elimination identity), L035 (images), L036 (scalar
domain), L037 (faithful comparison interpretation), and L038 (fixed-one
stop). No cross-notebook input is used.

Read L033's hypotheses and field definition, L034's complete-map and
regular-fiber arguments, L035's image definitions, L036's exact domain,
and L038's complete-algebra conclusion. L036 already lists 2+5 Z5; no
new scalar-domain lemma is required. L038 supplies A's unramified factor
identification, but its B_1 computation must not be relabeled as B_2.
ATTEMPTS/008–010 retain the missing global arithmetic, constant-norm and
unrestricted-baseline obstructions. ATTEMPTS/011 and history/097 stop
j=1, not other scalar fibers. No duplicate B_2 certificate was found in
these targeted records.

## Reused primary coverage and search limits

The preceding [fixed-one assessment](2026-10-08-full-fiber-at-one-local-algebra.md)
contains the inspected hypotheses, proof cases, version information and
qualifications. Those general theorems are unchanged by the scalar:

- J. S. Milne, [Algebraic Number Theory v3.08, July 19, 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Theorem 7.33 and Remark 7.36, pp.121–123: monic factors over a complete DVR lift uniquely when their reductions are pairwise coprime. Corollary 7.42 and Remark 7.43, p.124: finite local degree equals ef. Proposition 7.50, pp.127–128: unramified extensions are classified by residue extensions under its perfect-field hypotheses. Proposition 7.60, pp.131–132: Krasner inclusion requires separability and strict separation from distinct conjugates.
- Pete L. Clark, [Algebraic Number Theory II](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf), 161-page version retrieved 2026-10-08, revision date unidentified: Theorem 1.79, p.58, requires integral polynomial and approximate root over a complete valued field with |f(r)|<|f'(r)|^2; Theorem 2.38, p.80, requires Henselianity, separability and strict conjugate separation; Theorem 2.41, pp.81–82, preserves the entire separable quotient algebra for sufficiently close coefficients, with every factor retained. Its existential tolerance supplies no automatic numerical cutoff.
- Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents 2, 3, n*, Compositio Math. 156 (2020), 77–113, [final author manuscript June 10, 2019](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf), Section 7.2, pp.24–28: Table 5 supplies the field; equation (7.4) supplies the degree-twelve polynomial. Lemma 7.6's specified Q2 domains exclude 54a1 from its statement; its proof does not decide this Q5 pair. GRH-dependent Selmer dimensions are not inputs.

These primary passages were reused from the recorded inspection, not
retrieved or claimed newly read this turn. Fresh searches returned FNS,
other X0(11) discussions and unrelated coefficient matches; none supplied
an inspected theorem deciding B_2. Search snippets are not imported
results. No inference of novelty follows from failed searches. The prior
PARI factorpadic assessment remains an implementation lead only, not a
certificate. Mathlib coverage of the complete comparison or supporting
criteria remains not checked.

## Approved bounded calculation and discrimination test

Use the existing map identity to propose the specialization
F(x,2)=h^3+2J-4d; this notation is not certification that its quotient is
the whole fiber. Before using that presentation, certify reconstruction
of y=(2d-a)/b and account for any roots where b or d vanish. The known
map degree is twelve and its branch values are 0,1728,infinity, but a
regular fiber can still have an exceptional affine coordinate. If the
single-coordinate presentation fails, use the full curve/fiber algebra
rather than discarding points. No B_2 resultant or discriminant was
computed in this literature turn.

Reuse L038's A identification. Compute exact residue factors of the
certified B_2 presentation; apply the cited results only after verifying
integrality, monicity and coprimality. If repeated residue blocks occur,
record the unresolved block and use certified translations, scalings or
extension models; a degree-dropping reduction alone is incomplete.
For ramified identifications verify the strict Hensel/Krasner bounds or
an exact isomorphism with a full-rank generation certificate. No general
local-field theorem needs a reproof; only this explicit specialization's
missing arithmetic and completeness checks are authorized.

Continue on a complete pairing of every field factor, including repeated
isomorphic occurrences, with both dimension totals twelve. Together with
L036 and L035 this would supply nonemptiness of I_pow and I_fiber.
Abandon this scalar on an intrinsic complete-algebra invariant mismatch;
this rejects only j=2. Matching e,f for ramified fields, an order
polynomial's discriminant, guessed roots or unfinished lifting decides
neither case. Record actual versus required bounds if lifting stalls.
Image strictness, global intersections, all five twist emptiness claims
and infinitely many signatures remain independent unresolved gaps.
