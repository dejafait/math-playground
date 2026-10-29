# Fixed-pair branch annihilator test: source coverage ready

TARGET: Decide by three certified global square-class comparisons whether L147's fixed Selmer pair spans the rational branch Kummer class, and record only the resulting forced-zero obstruction or its absence.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Checked L138/L147, L139's interface, ATTEMPTS/065 and histories 528/529/531 plus the membership draft for duplicates/failures; searched exact number-field square testing, Stoll odd-model representation and Trager factorization. Found complete standard algorithms, not an inspected computation for this fixed pair. No inference of novelty from search results.
SOURCE_EVIDENCE: Reused the inspected Fisher–Yan radical/alternation assessment; newly read Stoll (2001), Section 4 pp.249–251, Lemmas 4.1/4.3 and Proposition 4.2; Trager (1976), pp.219–221, Theorems 2.1–2.3, Lemma 2.4, Corollary 2.5 and both factoring algorithms, including their proofs; SymPy 1.14.0 official factorization interfaces; PARI official nffactor/nfroots hypotheses and conditional-order caveat; AFP Kronecker_Factorization definitions and soundness/completeness statements.
COMPARISON: Published odd-model descent identifies the exact equality group; published number-field factorization supplies a complete square decision. Only the three instance comparisons and their certified pairing consequence remain. No full global basis, sextic transport or standard covering model is required for this test.
GAP: None in essential source coverage for this bounded calculation. All three actual comparisons, exact certificates and a later critical review remain undone; no membership, nonmembership or pairing value is established.
REASON: Import the general theorems and algorithm rather than reprove them; specialize only to the authenticated pair and branch representative. This source advance readies a later calculation and is not new mathematics beyond the sources checked.
LITERATURE_REASON: The changed global-equality target required an essential unread complete square-test method; reuse of the ready pairing assessment avoided refreshing that theory.
SCOPE: Exactly TARGET on L138's actual odd model and L147's masks 165 and 132102; three comparisons, exact certificates and their conditional pairing consequence. No new witness search, covering box, backend probe, full global basis or point classification.

## Proposed calculation, relevance and decision test

The main gap is still exclusion of residual primitive Beal solutions.
L147 now supplies the accepted upper bound rank<=2+c<=4 and two
independent Selmer classes, but no nonzero pairing. The intermediate
target is to establish or exclude one specific forced-zero obstruction
for that pair before any further investment in standard covering models.
This could eliminate an unsuitable pair or justify continuing a different
pairing construction; it would not itself resolve point control.

Essential inputs: L138's actual Q-times-K model and maximal-order basis,
L139's rational two-torsion dimension, and L147's exact representatives,
complete local images and rational branch evaluation
(H(9075),9075−eta). The saved selected masks are 165 and 132102.
The proposed finite domain consists of their three nonzero combinations,
each compared with that branch class in the full odd-model square-class
group. No scalar quotient or sextic transport is part of this test.

The completed review below preserves that calculation. No actual comparison
or new lemma is contained in this file. A certified
branch-span membership would require recording its precise pairing
consequence and retiring this pair if forced zero. Certified nonmembership
would remove only this obstruction, not show a nonzero pairing or certify
any covering. If a complete test cannot be justified, record that exact
blocker rather than enlarge a search box.

ATTEMPTS/065 failed at raw-form isotropic-vector search and remains parked.
The present test concerns the selected cohomology classes before covering
construction, so it neither repeats that box nor substitutes a backend.
The known source material about radical containment is explicitly reused.
No novelty claim or creative-route designation is justified for this
standard specialization. A central creative pairing mechanism remains
premature until this fixed pair is separated from the rational radical.

## Primary inputs and exact interface

Reuse `drafts/literature/2026-10-28-pair-cassels-tate-test.md` without
another Fisher–Yan read: *Computing the Cassels–Tate pairing on the
2-Selmer group of a genus 2 Jacobian*, author manuscript dated
14 September 2023, [pp.2,10,18–19](https://www.dpmms.cam.ac.uk/~taf1000/papers/genus2ctp.pdf),
equations (1)–(2),(40), Lemmas 2.4 and 3.1. Its pairing factors through
Sha, so rational Kummer classes are radical. The rational Weierstrass
point makes the canonical cocycle zero and supplies alternation.
L138 authenticates that point and the genus-two model over Q; L147
authenticates both Selmer inputs. No finiteness of Sha or full rational
two-torsion is needed. The later calculation must spell out the elementary
bilinear consequence for a two-dimensional span containing a nonzero
radical element; it must not infer a nonzero value from nonmembership.

Newly checked Michael Stoll, *Implementing 2-descent for Jacobians of
hyperelliptic curves*, Acta Arith. 98 (2001), 245–277,
[Section 4, pp.249–251, Lemmas 4.1/4.3, Proposition 4.2](https://www.impan.pl/shop/en/publication/transaction/download/product/83397),
DOI 10.4064/aa98-3-4. The hypotheses are a monic integral squarefree
odd-degree model over Q, with its rational infinity. The representation
is the norm kernel inside L*/L*², with no scalar quotient; Lemma 4.3
includes branch divisors. These are exactly L138's certified hypotheses
and L147's branch evaluation, not the unaudited sextic transport.
Consequently the comparison uses both components of Q×K. L147 already
records a nonzero branch localization at 3; do not assume every rational
two-torsion point has nonzero image modulo twice the rational group.

## Complete square decision and certificate requirements

Barry M. Trager, *Algebraic Factoring and Rational Function Integration*,
SYMSAC '76, pp.219–226, [primary scanned paper, pp.219–221](https://www.cecm.sfu.ca/~mmonagan/teaching/TopicsinCA11/TragerFactor.pdf):
Theorem 2.2 recovers complete factors by gcds from a squarefree norm's
complete base-field factorization. Theorem 2.3, Lemma 2.4 and Corollary
2.5 justify terminating integer shifts; p.221 gives `sqFr_norm` and
`alg_factor`. Characteristic zero, an irreducible field polynomial,
squarefree input and complete rational factorization are essential.
For each nonzero quartic ratio b, apply this existing algorithm to
U²−b over L138's K. Save the shift, resultant, squarefree gcd identity,
complete rational factorization with irreducibility evidence, recovered
gcds and inverse shift. These certify completeness; a product identity
alone does not certify irreducibility. Positive outcomes instead admit
direct verification of a displayed square root in Q[alpha]/A.
This imports the algorithm, not a new square-testing lemma.

The rational component is tested separately by exact integer square
tests on its reduced numerator and positive denominator, including its
sign. A single certified nonsquare component suffices. The three ratios
are branch divided by epsilon, eta_class and their product, respectively;
do not change any representative by a nonsquare rational scalar.
Do not compare the masks as global class coordinates: they only name
products in the fixed witness list. No ratio is evaluated this turn.

An explicit complete rational-factor certification fallback is the
standard Kronecker algorithm. The primary formal development
[AFP, Kronecker_Factorization](https://isa-afp.org/browser_info/current/AFP/Polynomial_Factorization/Kronecker_Factorization.html),
accessed 2026-10-28, supplies `kronecker_factorization_main_complete`
and `kronecker_factorization_rat`, with full divisor-function hypotheses
and degree bounds. A reproduced exhaustive certificate must retain all
divisor choices, interpolation/divisibility checks and domain bounds;
an interrupted enumeration is unresolved. No claim of practical runtime
for this fallback or of a local Isabelle installation is made.

[SymPy 1.14.0 official internals](https://docs.sympy.org/latest/modules/polys/internals.html#sympy.polys.factortools.dup_ext_factor),
`dup_ext_factor`, `dup_sqf_norm`, `dup_zz_factor`, explicitly document
Trager and complete integer factorization. These are implementation
leads, not certificates for these inputs. The official
[PARI nffactor/nfroots documentation](https://pari.math.u-bordeaux.fr/dochtml/html/General_number_fields.html#nffactor)
also provides complete exact interfaces and warns against a conditional
nonmaximal `nf` structure; pass the defining polynomial or certify it.
Neither source requires a unit/class basis for this fixed square test.
No backend was probed or installed. Sage's square-test documentation
was an inspected search lead, not an essential mathematical import.

## Gate decision and limits

SPECIALIZE permits the next bounded calculation using the saved exact
representatives and the imported algorithm, with an independent exact
replay. Local nonsquare certificates may end a comparison early; absence
of local obstruction cannot establish equality. If complete evidence is
unavailable within a declared work bound, save the unfinished comparison
and report it unresolved, without calling it a negative result.
The failed PDF screenshot fetch did not block the theorem review: the
primary paper's complete relevant text, proofs and algorithms were
accessible; no uninspected diagram is load-bearing.

This source gate makes no rank improvement. The accepted bound remains
rank J(Q)<=2+c<=4. Global generation, pairing/covering construction,
point control, marked/integer recovery and the residual exponent family
are separate gaps. Full matching Mathlib coverage was not checked;
neither the AFP theorem nor software documentation is a Mathlib theorem.
