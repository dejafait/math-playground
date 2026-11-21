# Proposed signed contour-head comparison

TARGET: Review source coverage for a census-free contour certificate of the signed H2 head on |Re z|<100, |Im z|<1/2 over 0<=lambda<=1/20, including horizontal-boundary and radial-shell accounting.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2155 compared the exact inverse-power contour proposal with primary residue/Laurent statements, contour-Hankel hypotheses/proofs and rigorous integration contracts; reused the step200/206/2150 coverage and searched the specifically relevant local H2 stops. Queries and inspected cases follow; no novelty or exhaustive-search claim.
SOURCE_EVIDENCE: NIST DLMF 1.10(iii)-(iv), (1.10.6)-(1.10.9), https://dlmf.nist.gov/1.10 ; Deng-Yang-Lu arXiv:2608.11520v1 Sections2.1-2.2, Definition2.4, Theorem3.4/proof, Proposition4.1/Theorem4.2 and Section6 (86)-(89)/first quadrature tests, https://arxiv.org/html/2608.11520v1 ; Johansson arXiv:1802.07942v1 Sections2/2.1, https://arxiv.org/html/1802.07942v1 ; Polymath arXiv:1904.12438v2 Theorem3.2, https://arxiv.org/html/1904.12438v2#S3 ; accepted local inputs L018,L019,L058,L874,L919,C919a,C919b.
COMPARISON: Known residue methods cover a census-free finite weighted zero sum only with all weight poles included. The closest contour-Hankel theorem assumes a holomorphic coordinate on the closed interior, which the proposed inverse coordinate violates at zero; its flow concerns fixed Xi, not heat time. C919a already covers the qualitative horizontal strip, but neither it nor C919b supplies the complete numerical F_z/F quadrature certificate.
GAP: No numerical head certificate or feasible rigorous quadrature budget is approved. First audit the exact origin residue and rectangular complement to decide whether the five outer-contour observables add independent head information; a punctured contour or independently evaluated origin term would be a separate target. Head margin, quantitative horizontal bounds and complete enclosing integration remain unpaid.
REASON: Primary hypotheses rule out direct import of the proposed head formula and redirect the route to one bounded analytic obstruction audit before any numerical head search. This is a source-scope result, not a proof that every contour method fails or any H2 sign is false.
LITERATURE_REASON: The saved changed observable had REVIEW_REQUIRED coverage: meromorphic weights, the origin term, complete-contour integration and radial/rectangular comparison were not covered by the ready vertical-boundary assessment.
SCOPE: Completed source review of TARGET. Only the separately nominated five-functional analytic audit has ready specialization coverage; no numerical head implementation, new residue identity, shell inequality, lemma or mathematical script was produced in this literature turn.

## Original nomination (preserved; completed comparison below)

The main gap is still L030-L032/C032a actual-Xi all-degree mixed
positivity. The proposed intermediate use is a finite signed 3-by-3
head matrix enclosure compared against C919a's 1/2000000000 tolerance.
It would leave higher degrees and global continuation open, even if
successful. Individual zero reality, simplicity and an exhaustive
list must not be assumed. The residue multiplicities and algebraic
transpose must survive conjugation correctly.

Essential local inputs for comparison are L019,L058,L919,C919a,C919b;
L018's strip and L037's arithmetic may support particular prerequisites
only after their applicability is checked. Use C919b's accepted fixed
boundary exactly. Its reflection does not itself pay horizontal
boundaries or the change from |zeta|<=100 to a rectangle. Assess the
origin contribution for inverse-power weights explicitly; omitting it
could turn a purported head calculation into a circular use of the
unknown moments. Complex F'/F enclosures and complete quadrature errors
are not certified by the existing finite-sum script.

The source review should compare precise residue/enclosing-integration
results, stronger directly applicable conclusions, local duplicates
and recorded failures. Relevant preserved failures are the step206
endpoint Rayleigh stop in
`../../ATTEMPTS/2026-11-09-h2-endpoint-rayleigh-inconclusive-206.md`
and the moment-box stops identified in the existing low-time H2 review.
The candidate changes the joint observable, not the old precision or
direction; whether it actually retains useful correlations is unknown.

Continuation test: approve at most one fully specified fixed contour
certificate budget only if complete source coverage and noncircular
head/shell accounting make the comparison testable. Otherwise record
the precise overlap or missing premise and park it. No sweep, census
search, contour implementation, new lemma or calculation is authorized
by this nomination. Full Mathlib matching coverage is unchecked.

No justified central creative mechanism follows from a finite boundary
certificate. This source comparison is not labeled creative; it must
first determine whether the contour observable pays a new prerequisite
or merely restates the stopped moment calculation. A later genuinely
new all-degree mechanism would require its own exact target and gate.

## Step2155 completed source comparison

The main gap remains L030-L032/C032a actual-Xi all-degree algebraic
mixed positivity. The reviewed intermediate target is a signed finite
H2 head on this fixed rectangle and closed heat band. Its possible use
is a head lower bound exceeding C919a's 1/2000000000 budget, with
cutoff transfer justified. No source inspected proves that margin.

### Primary statements and limitations

NIST, [DLMF 1.10(iii)-(iv)](https://dlmf.nist.gov/1.10), read
(1.10.6)-(1.10.9) and surrounding hypotheses. Laurent coefficients
use a circle in the annulus of analyticity, traversed once positively.
The finite residue theorem allows finitely many interior singularities
but none on the contour; every interior singularity contributes.
The argument principle counts multiplicities. Thus inverse-power
weights require the origin contribution even though F(lambda,0)>0.
This is standard theorem coverage, not a head formula proved here.

Z. Deng, X. Yang and H. Lu,
[arXiv:2608.11520v1, 12 August 2026](https://arxiv.org/html/2608.11520v1),
Section2.1, Lemma2.3/(8)-(10) and full proof require nonvanishing
on a piecewise smooth Jordan boundary and a coordinate holomorphic
near the closed interior. The inverse coordinate fails the latter
hypothesis. Definition2.4 uses algebraic transpose. Theorem3.4's
full proof requires conjugation-compatible nodes/equal conjugate
weights and matrix order at least the distinct-node count; it does
not give unconditional low-order positivity. Section6 (86)-(89)
and its first tests use numerical trapezoidal comparisons, not a
validated heat-band enclosure. Proposition4.1/Theorem4.2 were also
rechecked against the existing step194/step200 comparison: coordinate
motion of fixed Xi zeros is not heat-time evolution. No automatic
head or heat-positivity theorem is imported from this preprint.

F. Johansson,
[arXiv:1802.07942v1, 22 February 2018](https://arxiv.org/html/1802.07942v1),
Sections2/2.1: read the complete adaptive algorithm and its termination,
tolerance and evaluation-limit cases. The caller must enclose the
integrand and certify analyticity on each quadrature ellipse; bounds
for its complex magnitude pay the Gaussian remainder. A pole or an
interval denominator containing zero prevents that finite bound.
Requested tolerances are not guaranteed: actual returned radii must
be checked, also when work limits are hit. The paper supplies a
rigorous method, not a certified F_z/F evaluator, time-box enclosure
or feasible budget for the proposed rectangle. C919b's normalized
nonvanishing bound is insufficient to differentiate its error formula
or enclose the logarithmic derivative on those ellipses.

Polymath, [arXiv:1904.12438v2, 4 August 2019](https://arxiv.org/html/1904.12438v2#S3),
Theorem3.2 and its cited de Bruijn Theorem13 were inspected at the
statement/citation level; the original de Bruijn proof was not newly
read or reproved. Reuse the already audited C919a normalization and
strip application, including L018's open strip at zero time. These
are ready qualitative horizontal-boundary inputs. They do not provide
a quantitative lower bound for enclosing quadrature over horizontal
parameter boxes. Reuse the step2150/2153 finite-sum assessment solely
within C919b's accepted vertical-boundary scope.

### Local overlap, origin and cutoff obligations

Read L019/L058, L919 including its accepted product/coefficient and
complete-tail proof, C919a's strip and opposing-component estimate,
C919b's hypotheses and boundary conclusion, L018, and L874's logarithm
germ/derivative convention. L874 already expresses the germ derivative
through the S_k. Therefore an origin Laurent coefficient cannot be
set to zero merely because the origin is not a zero of F. Whether
the corrected outer contour leaves independent head information is
the nominated audit, not a result derived in this source turn.

The sharp radial head in L919 and the open rectangular head are
different. A contour count cannot identify them without a shell
argument. C919a bounds the negative quadratic part of a full radial
tail; it is neither an absolute norm bound nor permission to subtract
an arbitrary signed shell. Its per-class proof is the appropriate
covered input for a future conjugation-invariant-subset comparison.
No new subset bound or rectangular matrix identity is asserted here.

Preserved failures: L917/step195 independent moment boxes, L920's
step206 fixed Rayleigh enclosure and L922/step213 shared-parameter
Taylor determinant enclosure. The latter still straddles zero even
with a common parameter. A new contour representation alone neither
invalidates those results nor proves improved correlations. The
step194/step200 fixed-Xi flow mismatch remains in force; the present
review tests static inverse-power observables instead of reusing
that stopped heat-flow inference. This distinction is not a global
endorsement of the contour route.

### Search record and decision

Queries included `validated contour integration power sums zeros
argument principle Johansson Arb rigorous complex integration`,
`Delves Lyness 1967 numerical method locating zeros analytic function
power sums contour integrals`, `site.fredrikj.net rigorous numerical
integration Johansson Petras complex Arb 2018`, and `site.arxiv.org
"Hankel" "contour" "de Bruijn"`. Local searches were limited to
the named H2 assessments/stops, the reciprocal-Hankel assessment and
the specific result files above. The Delves-Lyness 1967 paper,
DOI10.1090/S0025-5718-1967-0228165-4, remains an unread optional lead:
the publisher PDF returned403 and a second publisher URL failed.
Its snippet was not treated as theorem evidence. Accessible DLMF,
Johansson and the inspected contour-moment proof cover the essential
general method, so this is not an essential source-access blocker.
No broader source-access campaign is justified.

The useful negative finding is a precise direct-import obstruction:
the closest contour-head theorem excludes the proposed weight pole,
and its numerical section cannot certify the changed heat-band test.
Park the numerical head proposal; there is no approved precision,
mesh, cutoff or quadrature sweep. The bounded next question is the
five-functional analytic audit specified in
`2026-11-21-h2-outer-contour-origin-audit-2155.md`. It can discriminate
an outer-tail reformulation from independent head information without
building the missing evaluator. Its ready assessment is new and needs
the supervisor's separate approval before mathematical work.

Continuation/abandonment test: retain all origin/multiplicity terms
and compare the actual rectangular complement. If the five outer
functionals give only exterior data unless the unpaid S_2,...,S_6
are supplied, stop this outer-only head mechanism. If independent
head information survives, specify its still-unpaid enclosing
integration prerequisites before implementation. A punctured contour
or separate origin evaluation would need a new mechanism-specific
test, not a silent omission of the origin. This review proves neither
alternative and does not ban such later proposals.

Full matching Mathlib coverage of the heat-band signed-head certificate
and these effective errors is unchecked. No new lemma, mathematical
script, mathematical certificate, DAG edge or proof assembly was
written. This is local source-scope progress, not progress beyond the
checked methods, a new positivity result or an RH candidate. No
justified central creative mechanism follows from this finite contour
comparison; an independent all-degree sign input is still missing.
