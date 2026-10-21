# Fixed scalar-action maps — construction coverage

TARGET: Construct and independently verify the six nonzero scalar-action maps on L067's full 7-torsion algebra for y^2+y=x^3+x^2-2x.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused approved full-torsion and full-descent assessments; searched local lemmas, torsion evidence and relevant histories for scalar-map duplicates; queried exact conductor-389 seven-torsion, division-polynomial multiplication and Schaefer--Stoll scalar automorphisms. Primary sources below were inspected; no completed matching local map certificate was located, and no novelty is asserted.
SOURCE_EVIDENCE: Sutherland, MIT 18.783 Fall 2023 Lecture 5 (2023-09-26), Sections 5.5--5.6, Lemma 5.20, Theorem 5.21 and Lemma 5.24, printed pp. 10--14; Schaefer--Stoll, author long version dated 2001-06-13, Section 5 equation (5.1), Lemma 7.2 and Corollary 7.3 with following convention, Corollary 7.9 and Proposition 7.10, printed pp. 9,13--14,18--19; exact statements and essential proof cases inspected online 2026-10-15, reusing prior descent proof coverage.
COMPARISON: Known multiplication coordinates and the explicit source pullback convention cover the target; remaining work is fixed-model arithmetic certification and full independent replay, not new multiplication or descent theory.
GAP: No scalar coordinate maps, exact denominator inverses or composition certificate have been computed. Incidence data, functions, complete units/classes, local bounds and other descent premises remain absent.
REASON: This separate literature turn resolves the full-domain and convention coverage left pending by step 241; the unchanged target is ready for known-algorithm reproduction.
SCOPE: Six geometric scalar pullbacks on the full degree-48 algebra, both model coordinates, exact denominator-unit witnesses, inverse/composition identities, complete independent replay and bounded altered-evidence rejections; excludes incidence construction, descent functions, units/classes, local conditions, residual surjectivity and Selmer conclusions.

## Inspected primary inputs

[Sutherland, Lecture 5](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf),
pp. 10--14, supplies recursive coordinates phi_n/psi_n^2 and
omega_n/psi_n^3 on a nonsingular short Weierstrass curve. Characteristic
two/three requires modified formulas; Q meets the restrictions. Lemma
5.20 handles parity and polynomial divisions. Theorem 5.21 identifies
multiplication, including negative indices. Its proof treats odd addition
and even doubling but leaves numerator verifications analogous, referring
to Washington, second edition, Theorem 9.33; that book proof was not
separately read. Lemma 5.24's adjacent-multiple contradiction excludes
cancellation; the kernel description on p. 1 identifies affine poles.
Import these named results rather than reprove the recurrences.

[Schaefer--Stoll, long version](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
numbering above, explicitly states on p. 14
(sigma_g phi)(P)=phi(gP). Lemma 7.2 assumes point stabilizers meet the
scalar center trivially; its proof uses free scalar orbits, character
decomposition and additivity of H^1. Corollary 7.3 gives the necessary
kernel g-sigma_g in additive power-class notation. Corollary 7.9 also
requires the incidence kernel; Proposition 7.10 obtains its map by
pullback and fiber norm. Equation (5.1) retains the full cohomology image
and classical local conditions. These full-set statements do not assume
residual surjectivity. Prior essential descent proof coverage is reused.

Keep this forward scalar pullback distinct from an inverse-permutation
convention. Field automorphisms without geometric scalar identification
fail the target; scalar constraints alone do not certify cohomology.

## Applicability and later finite verification

Essential inputs are audited L067's complete R and both coordinate maps,
L030's nonsingularity and L066's source conventions. L067 already supplies
the origin-preserving change X=36x+12, Y=216y+108 to
Y^2=X^3-3024X+46224 and its inverse. Retain the entire E[7] minus O,
not its sign quotient. The indices 1,...,6 are prime to seven; the source
applicability requirement is avoidance of their multiplication kernels
on this entire set. Exact inverse witnesses must still certify every
actual evaluated denominator. This is a verification specification for
later research, not a newly computed denominator or map theorem.

The approved bounded construction must meet these obligations:

1. Fix all six indices. Record and replay every base case and recurrence
   used for both coordinates, including any further recurrence inputs
   needed for omega_n. Check polynomial divisions before evaluation and
   supply an exact inverse in R for each evaluated denominator. Account
   for intermediate coordinate divisions and nonzero rational constants.
2. Produce both short coordinates of [a]P, both transported original
   coordinates and sigma_a on t=Y. Retain complete representatives and
   full basis action. Verify defining relations, transports and geometric
   multiplication on every nonzero torsion point using the imported
   theorem with its domain conditions. Checking h(sigma_a(t))=0 alone
   supplies no geometric identification.
3. Check identity, every scalar composition with indices reduced modulo
   seven, and every inverse on the full algebra, retaining both
   coordinates. If a primitive residue g is selected for later scalar
   constraints, certify its order and use the source convention. No
   global power-class basis or constraint matrix is part of this target.
4. Independently reconstruct all arithmetic without producer imports and
   replay every map, denominator inverse, basis identity and composition.
   Save full certificates/reports under scripts/seven-torsion/, printing
   concise actual/required dimensions, failures and paths. Include bounded
   corrupt-coordinate, incorrect inverse/action and missing-denominator
   rejection cases with original upstream bytes preserved. A preview or
   an unverified generator image is insufficient.

These instance witnesses are needed because the named theorems do not
supply their coefficients. No general multiplication reproof is proposed.
An eventual canonical lemma must retain hypotheses, specialization,
complete evidence, qualifications and Mathlib coverage; none is written
this turn.

## Duplicates, failures and search record

Scoped local searches covered lemmas/, drafts/literature/,
scripts/seven-torsion/ and relevant recent histories, with scalar-action,
pullback and multiplication-map terms. L067 excludes these maps;
L065/L066 supply conditional interfaces only. Reuse the approved
full-torsion construction assessment for its unchanged algebra scope.

Queries included `Schaefer Stoll p descent scalar action sigma nu alpha
equation 5.1`, `Sutherland 18.783 2023 Lecture 5 division polynomials
Theorem 5.21`, an exact `389` / `7-torsion` / `scalar` query,
`Schaefer Stoll automorphism primitive root p-descent`, and `elliptic
curve division polynomials multiplication nonzero p torsion algebra
scalar automorphism`. The inspected matches are standard multiplication
and the explicit descent convention. Positive-characteristic torsion,
finite-local-ring and software-documentation search leads were not
inspected as theorem evidence for this target. Neither an unsuccessful
instance query nor local nonduplication establishes originality.

ATTEMPTS/021 retains the finite-Selmer defect; 032 retains the capped
zero Kurihara residue; 033 retains the absent ordinary evaluation; 034
stops repeating conditional interfaces. None supplies these scalar maps
or prohibits this independently checkable finite target. Do not enlarge
the Kurihara cap or repeat the interface audit. Preserve the degree-47
draft and initial audit-harness expectation failure.

## Relevance and decision test

The main gap remains arbitrary-curve rank equality at analytic order at
least two. The intermediate target is exactly the six certified scalar
pullbacks. They can supply the scalar part of L066's optional necessary
cohomology-image constraints once complete global power classes are
independently available. They supply neither that basis nor incidence.

Continue only if every map is geometrically identified on all 48 points,
every actual denominator has an exact inverse, and full inverse,
composition and independent replay checks pass with intended rejections.
Otherwise isolate and preserve the failed map/evidence and stop the
bounded attempt without a full-descent inference. Implementation failure
is not an impossibility theorem about these known maps.

No cross-notebook input or L026 premise is needed for map production.
Descent functions, incidence data, embeddings/local identifications,
complete units/classes and local-image upper bounds remain unprovided.
L026 residual nonvanishing, successful localization, rational membership,
divisible Sha and arbitrary complex-order comparison stay independent.
Successful maps alone do not activate L066 or establish D=D_div.

Mathlib: full matching scalar-map and descent-certificate coverage was
not checked; no absence claim. The ready continuation is REPRODUCTION
under SPECIALIZE, with no progress beyond known algorithms asserted.
No maps, lemmas or mathematical scripts were produced this turn; no
mathematical exploration budget was spent.
