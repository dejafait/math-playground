# Source-scope nomination: fixed-arc spatial defect audit

TARGET: Audit L706's fixed-arc spatial Jensen-defect bound, including common-factor removal, interior numerator zeros, both signed endpoint sums and the full-circle qualification.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step 154's exact fixed-profile defect comparison in 2026-11-03-fixed-profile-spatial-jensen-defect.md and its inspected local contrasts L669/L683/L698/L705 and clearing/block stops; no new external search or novelty claim. Step 156 separately checked the direct primary URLs and hypotheses; no new novelty search was needed for this unchanged audit target.
SOURCE_EVIDENCE: Reopened Brunault--Zudilin Propositions 1.4-1.5/Lemma 1.6 pp.6-8 https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf ; Issa--Lalin arXiv:1203.5379v1 Remark 3.8/Theorem 4.1 and proof p.7 https://arxiv.org/pdf/1203.5379v1 ; Ash--Novinger (2004) Theorem 4.8.3/Lemma 4.8.4 pp.33-36 and Corollary 4.7.4 p.27 https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesWithHyperlinks.pdf . Reuse complete prior proof readings; precise interfaces below.
COMPARISON: These inputs cover actual-degree Mahler accounting, finite product-log integrability and boundary Poisson evaluation. They do not certify L706's new uniform neighborhood, regularized product upper bound or signed two-endpoint limit; those are the precise local arguments to audit. The old isolated-angle result is not the positive-measure arc conclusion.
GAP: Independently verify L706 (1)-(3) for the same actual fixed L703 profile and all sufficiently large n=12q+3, including every spatial moment, angular numerator zero and common pole; reject any inference of the unproved complementary o(n) bound or full amplitude/charge estimate.
REASON: Separate step-156 source approval completes the unchanged audit scope under SPECIALIZE; direct primary URLs and essential hypotheses are verified. The next turn may audit the quantitative specialization. This approval does not accept L706 mathematically.
SCOPE: Exactly TARGET; fixed profile selected before n, |u|=1/2, original L666 G_n and L657 K,Q, existential fixed positive arc and onset, no reflection or effective constants. Permitted work is verification or repair of the stated arc result and its limited implications, not a full-circle endpoint expansion or Xi bridge.

LITERATURE_REASON: Supervisor recovery requires direct source URLs in this ready assessment; this turn repairs that evidence and separately approves the saved scope without extending its target.

## Relation to the completed step

Step 155 was a RESEARCH proof attempt under the unchanged prior EXPLORE
assessment, not this audit. It produced a paid intermediate arc bound;
J_sp(n)=o(n) remains unresolved. L706 is explicitly unaudited. This
source scope received separate source approval in step 156 before its audit
is invoked; this does not approve the mathematics.

The exact local target has changed from a defect proof attempt to
critical verification of its new arc argument. Reuse the parent
assessment's actual source readings and comparison; no additional
browsing is needed absent a specific missing hypothesis or new lead.

## Inputs and load-bearing checks

Read L706 in full and only the needed L705 endpoint inequalities.
L666 supplies the original family and exact rational continuation;
L703 supplies one fixed profile with |e_m|<=1/8 and e_m->0 at both
ends. L657 supplies K,Q and the prior finite-polynomial interface,
but its unit-angular-circle nonvanishing statement is not itself
a theorem at radius 1/2. L706 must justify that specialization.

The general source hypotheses are unchanged from the parent assessment:
nonzero complex polynomials of their actual finite degree for the
Mahler formula; a nonzero rescaled polynomial for product logarithmic
integrability; and a polynomial analytic through the closed spatial
disk with a nonzero interior evaluation for Poisson--Jensen. Boundary
zeros are allowed. No source gives growing-degree uniform log control.

The conceptual audit should check:

- The exact common factor retains j=0 and the inverse angle. Its
  moving poles cannot be uniformly bounded in a neighborhood; only
  the pole-free normalized factor is estimated there. Radius 1/2
  itself must avoid every actual denominator pole for all allowed n.
- Vandermonde nonvanishing uses the fixed anchor even when individual
  nonanchor weights vanish. The angularly rescaled K is nonzero and
  finite-n logarithmic Fubini is justified.
- L705's strict endpoint derivatives persist on one fixed compact
  neighborhood. The regularized interior logarithm yields a uniform
  upper Riemann estimate despite possible sampled numerator zeros;
  it cannot be replaced by an unjustified uniform log derivative.
- Both actual endpoint indexings, e_m->0, geometric tails and the
  exponentially bounded interior are kept. Every M=n/3 spatial term
  survives through its exact geometric remainder. No conjugacy of
  the finite displaced family is assumed.
- The two distinct spatial resolvents prevent simultaneous cancellation
  at 0 and 1/2 after normalization by the larger endpoint. The Poisson
  kernel's minimum is used with the correct inequality direction and
  boundary upper bound, including spatial boundary zeros.
- The global bound still has a positive coefficient of n. Paying a
  fixed arc does not establish pointwise control almost everywhere,
  complementary o(n), an angular amplitude bound, full charge, H/support
  or Xi realization. Those limitations must survive any repair.

All full proofs and precise citations belong in L706; the above is
audit scope, not a second proof. Full matching Mathlib coverage remains
unchecked; the supporting polynomial/Mahler theorem names are already
recorded in L706 and the parent assessment.

Routing after step-156 source approval: proof_audit/conceptual_audit,
deep_research/xhigh. Uniform asymptotics through angular numerator
zeros, signed growing sums and boundary logarithms require conceptual
scrutiny. This is neither routine arithmetic nor a complete-RH candidate
audit. No new calculation or lemma is requested by this scope.

## Separate source approval — 3 November 2026, step 156

All three primary URLs in SOURCE_EVIDENCE opened successfully. SPECIALIZE
is ready for the unchanged conceptual audit. This literature-only repair
supplies no new mathematical evidence and is classified STALLED.

Brunault--Zudilin, *Many Variations of Mahler Measures*, ISBN 9781108794459:
reopened Propositions 1.4-1.5 and Lemma 1.6, printed pp.6-8, including
the complex-analytic boundary-arc case and coefficient proof. The root
formula retains actual degree, nonzero leading coefficient, multiplicities
and circle roots. Lemma 1.6 is the binomial coefficient bound, not a
sublinear defect theorem. Use the boundary-arc proof rather than an
equally spaced logarithmic sum through a sampled zero.

Issa--Lalin, *A generalization of a theorem of Boyd and Lawton*,
arXiv:1203.5379v1, 24 March 2012: reopened Remark 3.8, Theorem 4.1 and
its full proof, printed p.7. Inputs are finitely many nonzero complex
multivariate polynomials. For s=1 the small-value/complement split
justifies logarithmic integrability at torus zeros; reuse the earlier
complete supporting readings. The rescaled numerator must be nonzero.
Fixed-polynomial integrability supplies no uniform growing-family bound.

Ash--Novinger, *Complex Variables*, copyright 2004 hyperlinked text:
reopened Theorem 4.8.3, the boundary-factor reduction and Lemma 4.8.4's
statement/exterior-root limiting argument, printed pp.33-35; reuse the
previously inspected remainder through p.36. Located and checked
Corollary 4.7.4's mass-one statement, p.27. Require analytic extension
through the closed disk, a function not identically zero, and evaluation
away from its zeros. Boundary zeros are permitted. Polynomial spatial
slices satisfy the extension hypothesis; paid interior values and uniform
boundary upper control remain local audit obligations. No n-uniform
bound follows merely from this citation.

Reuse the parent assessment's duplicate/failure comparisons: isolated-angle
L705, changing-profile L669, generic linear root cost L683 and
different-radius amplitude L698 do not settle the positive-measure arc.
No new query or source result changes those comparisons. Full matching
Mathlib coverage remains unchecked; recorded supporting references do
not formalize L706. No general theorem needs a reproof for this audit.

The continuation test remains the load-bearing checks above. Accept,
repair or withdraw the arc result only after conceptual audit. Source
approval leaves complementary o(n), amplitude control, compensation and
Xi realization unresolved. No lemma or mathematical script changed.
