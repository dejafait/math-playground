# Quartic residual-insertion cubic scale — completed source assessment

TARGET: Determine whether the complete quartic residual-insertion response kappa_0(f_(i,0),r_2) in L011(6) has a vanishing a^3-scaled limit for both actual L010 probes in the straight lower-rooted forest.
CHECKED: 2026-10-12
DECISION: EXPLORE
SEARCH_EVIDENCE: On 2026-10-12 searched exact quartic-residual terminology, lattice translation-breaking insertions, flowed Ward identities, tree/axial-gauge quartic responses and one-loop power counting; followed the relevant Ward and Symanzik leads below and checked local duplicates and ATTEMPTS/009 and /011. No exact theorem match was established; no novelty is inferred.
SOURCE_EVIDENCE: Rechecked Del Debbio–Patella–Rago 1306.1173v1 sec. 6 (6.1)–(6.16), printed pp. 13–16; Lüscher–Weisz 1101.0963v2 secs. 7.2–7.4, 8.2 and 8.4, printed pp. 21–25; read Capponi et al. 1512.04374v1 secs. 1, 3–5, pp. 2–4, (3.1), (4.1)–(4.5); Ramos–Sint 1508.05552v1 secs. 3.1, 3.5–3.6 and 4.4, pp. 7–8, 15–17, 24–26. Reused the three earlier assessments named below.
COMPARISON: The strongest inspected statements concern complete renormalized flowed correlations, a finite matched translation generator, or the Symanzik expansion with its retained zero-flow-time insertions; none bounds the single bare fixed-mesh quartic jet covariance in the pinned forest. The displayed full-response O(a^2) Ward remainder does not transfer to this one summand.
GAP: Contract the complete r_2 polynomial with both actual quadratic probes under Sigma_F, retaining nonlinear coordinate-generator terms, all colors, connected subtractions, pinned prefix rows and the undamped internal pair; establish o(a^-3), or an informative alternative, without assuming full-response finiteness termwise.
REASON: This separate literature-only approval completes the changed insertion's source comparison. The explicit Gaussian test can proceed from existing local inputs; the inspected general theorems need no reproof and no essential source is blocked. Only the exact TARGET is approved, with no new asymptotic claimed here.
SCOPE: SU(2), a=8/N through admitted even meshes, all-face relative box, straight direction-1 lower-rooted forest, L008 displacement, L010 probes at tau=1/16, fixed-mesh bare small-coupling expansion before mesh refinement; one complete kappa_0(f_(i,0),r_2) only. Full-response cancellation, forest-independent meaning and interacting bounds are excluded.

The proposal was REVIEW_REQUIRED at invocation start. This separate
source-review step approves one subsequent mathematical attempt under
EXPLORE for the unchanged TARGET. It derives no result and adds no lemma
or mathematical script. Source comparison is completed below; a failed
exact search is not evidence of originality.

Use SU(2), a=8/N through admitted even meshes, the all-face relative box,
L008's displacement, and L010's probes with tau=1/16. The bare small-
coupling coefficient is taken at fixed mesh before refinement. In
L011(13), retain all of
r_2=(D s_2 v_3+D s_3 v_2+D s_4 v_1-j_(3,4)-j_(6,4)) composed with I.
The target is the single complete covariance with f_(i,0), including
all colors and connected subtractions; it is not any one summand of
that quartic polynomial. No higher jet is transferred to the Hodge law
without a justified lift. All pinned rows and undamped internal lines
remain.

Essential starting inputs are L011 for the exact jet and coefficient,
L010 for the actual nonlinear generator/probes, L017 and L018 for
quadratic quotient conventions, and L026 for the growing forest
covariance. L019 constrains nonlinear forest compensation. L147 and
L148 motivate the same-forest cubic comparison but supply no estimate
for this new term. Preserve ATTEMPTS/009 and ATTEMPTS/011; no isolated
forest invariance, bounded raw link covariance or internal heat damping
may be assumed.

A justified o(a^-3) bound would remove another compensation source;
a finite nonzero cubic coefficient or a precise obstruction would also
inform the route. An O(a^-3) upper bound alone does not prove the zero
threshold. Abandon a mechanism that merely repeats the failed raw-link
bound. The other jets, full cubic compensation, finer powers/logarithm,
finite matching, reflected error <=c_box/2 and all continuum/infrared
construction requirements remain unresolved. No candidate exists.

Full matching Mathlib coverage: not checked. Unknown is not absence.

## Relevance, reuse and duplicate screening

The main gap remains the ultraviolet-uniform interacting reflected
comparison with error <=c_box/2, followed by the continuum field/axiom
construction and infrared finite positive mass. This intermediate test
addresses only one potential compensation source for L147's nonzero
two-group cubic coefficient. L148 removes the density group at that
scale; neither result bounds this different insertion.

The supplied full overview and local DAG were used before detailed
proofs. Inspected L011's full statement and proof, L010's hypotheses and
probe definitions (1)–(4), L017(1)–(2), L018(1)–(3), L026(1)–(5), and
L019(1)–(5). L011 already defines r_2 and proves its fixed-mesh occurrence;
rederiving the general coefficient expansion would duplicate it. L019
retains residual jets in the nonlinear change-of-forest cancellation and
does not make their separate cumulants invariant. The targeted draft and
history search found no completed estimate of this exact covariance.

Reuse [the combined-response assessment](2026-09-26-current-target.md),
[the finite forest assessment](2026-10-04-forest-compensated-ward-identity.md),
and [the fixed-box locality assessment](2026-09-27-fixed-box-one-loop-locality.md).
The latter already checks Adams–Lee's momentum-integral hypotheses,
slab effective-action results and physical corner scope; none has a
verified finite-box comparison for this forest insertion. The matching
and tree theorems remain supporting context, not an isolated-jet bound.
The same-day official-target version check in
[the density assessment](2026-10-12-coordinate-haar-cubic-scale.md) is
reused: Jaffe–Witten's linked 14-page description, sec. 4, p. 6,
with its finite-mass qualification. No target or regulator is changed.

## Search record and inspected primary cases

Queries on 2026-10-12 included:

- `"quartic residual" "Yang-Mills"`
- `"residual insertion" "gradient flow"`
- `"translation Ward" "axial gauge" lattice quartic`
- `"lattice" "translation" "Ward identities" "irrelevant" "gradient flow" residual`
- `"gradient flow" "tree gauge" quartic Ward`
- `"lattice gauge" "axial gauge" "quartic" "Ward identity"`
- `"gradient flow" "translation Ward identities" lattice renormalization residual Del Debbio`
- `"lattice" "quartic" "translation" "gradient flow" insertion`
- `"lattice gauge" "one-loop" "power counting" "axial gauge"`

Searches located the following primary comparisons, rather than a match
for the saved statement. Abelian gauge-dependent correlators, 2D tree
gauge/topology papers, chiral axial-current identities and recent claimed
mass-gap constructions were not used as theorem evidence.

**L. Del Debbio, A. Patella and A. Rago, *Space-time symmetries and the
Yang–Mills gradient flow*, JHEP 11 (2013) 212,
[1306.1173v1](https://arxiv.org/pdf/1306.1173v1), 5 June 2013.**
Rechecked sec. 6, printed pp. 13–16, (6.1)–(6.16). Their chosen clover
translation preserves Haar measure. Their residual vanishes on smooth
configurations, but the discussion following (6.3) explicitly warns
that divergent contractions prevent neglecting it in correlators.
Equation (6.4) retains its mixing with tensor divergences. Equations
(6.11)–(6.13) express the flowed-probe translation response as a local
flow-time-zero multiplier insertion with finite generator normalization.
The extra translation-restoration assumption precedes (6.14)–(6.15).
These statements apply to the matched full insertion. L010 has a
different endpoint-averaged generator with nonzero Haar divergence,
and L011's r_2 is only one bare Taylor coefficient on a nonlinear
forest slice. Neither the conditional residual limit nor the generator
normalization asserts a bound on that coefficient. This is a scope
comparison, not a refutation of the source's result.

**M. Lüscher and P. Weisz, *Perturbative analysis of the gradient flow
in non-abelian gauge theories*, JHEP 02 (2011) 051,
[1101.0963v2](https://arxiv.org/pdf/1101.0963v2), 10 February 2011.**
Rechecked secs. 7.2–7.4, printed pp. 21–23, (7.6)–(7.8), and 8.2,
8.4, pp. 24–25. In their renormalized continuum SU(N) theory, directed
flow trees exclude bulk counterterms; power counting leaves two
zero-flow-time counterterms, and the BRS identity sets both coefficients
to zero. Gauge-invariant positive-flow-time composites need no further
renormalization. Their lattice discussion states an expectation based
on the remaining exact symmetries. The proof concerns full renormalized
correlations after ordinary four-dimensional renormalization, and its
boundary is t=0 in the flow direction. It does not provide a physical
cube-face estimate or assign final-time damping to the internal pair of
an unflowed r_2 insertion. No reproof is needed or licensed here.

**F. Capponi, L. Del Debbio, A. Patella and A. Rago, *Renormalization
constants of the lattice energy momentum tensor using the gradient
flow*, PoS LATTICE2015 (2016) 302,
[1512.04374v1](https://arxiv.org/pdf/1512.04374v1), 14 December 2015.**
Read secs. 1, 3–5, printed pp. 2–4, (3.1), (4.1)–(4.5) and the setup
paragraph in sec. 5. Equation (3.1) displays an O(a^2) remainder for
the full Ward identity using the renormalized tensor and normalized
translation; sec. 1 states the continuum translation-restoration
assumption. Their numerical SU(3) study uses clover representatives,
open-SF temporal and periodic spatial boundaries. Section 4 qualifies
the chosen three-vector-probe system as underdetermined in the continuum.
That warning is about their probes, not a contradiction to L008's
different two quadratic forms. The paper delegates derivation to
1306.1173 and reports preliminary numerical results; (3.1) is not an
independent uniform bound on a fixed-mesh quartic jet. Its representatives,
geometry and matched full response differ from the TARGET.

**A. Ramos and S. Sint, *Symanzik improvement of the gradient flow
in lattice gauge theories*, Eur. Phys. J. C 76 (2016) 15,
[1508.05552v1](https://arxiv.org/pdf/1508.05552v1), 23 August 2015.**
Read sec. 3.1, printed pp. 7–8, (3.1)–(3.6); 3.5–3.6, pp. 15–17,
(3.46)–(3.58); 4.4, pp. 24–26, (4.38)–(4.47). Their Symanzik expansion
retains connected insertions from the flow bulk and zero-flow-time
boundary. Their on-shell basis reduction uses field equations modulo
contact terms; they distinguish strictly positive-flow-time observables
from the more general zero-time case. Improved Zeuthen flow and improved
observables remove the flow/observable O(a^2) effects, leaving quantum
effects at t=0. The two-point check has both insertions flowed, twisted
periodic geometry and leading order in the coupling. This does not
control Wilson flow with a bare unflowed quartic residual on an all-face
pinned forest, or justify applying a smooth-field expansion to its rough
internal loop. The v2 PDF endpoint returned an internal error; v1 was
read successfully and is the precise assessed version. No blocker is
assigned to an unneeded later-version text.

## Decision and continuation obligations

No essential unread theorem premise remains for one explicit Gaussian
attempt. The older Caracciolo–Menotti–Pelissetto paper remains a
metadata-only lead as recorded in the combined-response assessment;
it is not needed here, and its unread general-discretization formulas
are not imported. The general flow, matching and forest results should
be cited within their already-recorded scopes instead of reproved.
EXPLORE means that the bounded comparison found no adequate theorem
for this asymptotic, not that the asymptotic is original.

Use L011 L010 L017 L018 L026 as essential inputs; L019 is the nonlinear
compensation constraint, and L147 L148 motivate the same-forest scale
test. Begin the later attempt with the complete local quartic jet and
its connected Wick contraction. Verify the exponential-coordinate
generator, all three chain-rule terms and both insertion subtractions
before any estimate. A proposed tensor cancellation must hold for the
complete insertion; a selected monomial does not answer the TARGET.
Keep the exact Sigma_F and all pinned rows, including the upper jump.
No higher-jet Hodge transfer, isolated forest invariance, bounded raw
covariance or internal heat damping is an available hypothesis.

Continue if a justified o(a^-3) bound removes the term, or if a finite
nonzero cubic limit or a discriminating obstruction changes the next
mathematical decision. An O(a^-3) upper bound alone leaves the zero
threshold open. Abandon any mechanism relying only on ATTEMPTS/011's
disproved O(1) raw-loop bound or on smooth-field vanishing from (6.3).
Preserve ATTEMPTS/009's forest-interpretation warning. Even success leaves
all independent response jets, the full compensation, finer powers and
logarithm, finite matching, interacting error <=c_box/2, reflection
positivity, continuum axioms, infrared control and finite mass unresolved.
This review establishes no mathematical bound and no candidate solution.
