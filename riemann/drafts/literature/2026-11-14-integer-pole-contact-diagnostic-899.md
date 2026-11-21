# Integer pole structure: fixed-law source assessment

TARGET: Assess the fixed reciprocal-product law h_0(s)=(1+s)((s+3)^2+1)/10 times product_(n>=1)(1+s/2^n) as a diagnostic for whether integer pole multiplicities permit a smooth flat positive density with positive decreasing H, positive D1/D2 and a first simple downward D3 contact.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completion900 searched the exact finite product and reciprocal-entire, complex-pole matrix-exponential, self-decomposable Wronskian and finite-PF terminology; inspected the primary cases below and L560's full proof/audit assessment. No inspected theorem supplies the joint fixed-law first contact; no novelty inference.
SOURCE_EVIDENCE: Sra https://arxiv.org/pdf/2611.02944v1 LemmaC.17 proof (C.49), pp38-39, supplies a general finite-factor positive inverse; TheoremC.14 pp34-35 and LemmaC.16 pp37-38 give qualified obstruction/window comparisons. Kwasnicki https://arxiv.org/pdf/1710.11023v3 Section6.1 p20 supplies the geometric smoother. Reuse assessment892's Steutel--van Harn V.2.11/V.2.16 (2.23); DLMF https://dlmf.nist.gov/1.14#iii supplies transform conventions and hypotheses. Exact reading/scope below.
COMPARISON: Integer-pole examples and finite-window/global-PF separation already occur in Sra C.17. Its positive-inverse proof covers a useful finite-factor family, while its window signs require sufficiently small b and do not certify b=1. L560 is a different bilateral C2/PF2-to-polynomial test. C466d remains the audited scalar obstruction; none of these establishes the present joint conditions.
GAP: Apply the cited finite inversion and smoothing inputs with their hypotheses; verify the canonical H and -H' globally, strict lower signs on the needed prefix, the endpoint join and a first simple downward D3 contact. No fixed-law property or new lemma was derived in this literature turn.
REASON: Coverage now supports one bounded specialization attempt on the unchanged law, importing known inversion/smoothing rather than claiming a new construction. The joint determinant/contact obligations remain model-specific and unresolved; automatic PF nonmembership-to-simple-contact inference is excluded.
LITERATURE_REASON: Completion of the supplied REVIEW_REQUIRED target: its integer-product/conjugate-pole hypotheses exceed assessment892, and the previously uninspected Sra C.17 proof is an essential relevant overlap.
SCOPE: One fixed product only, with the geometric rates exactly 2^n and one conjugate rate pair 3+i,3-i. The density, if it exists, has proposed Laplace transform 1/h_0. No actual-Xi claim, strip/counting-law match, PF-order extension, or counterexample to RH is proposed.

## Historical nomination899

The paragraphs below preserve the pre-review nomination. Their statements
about missing source inspection are superseded by completion900 below;
their unverified mathematical obligations remain in force.

Main gap: L030-L032/C032a actual-Xi all-degree algebraic-square
positivity. The intermediate diagnostic isolates an extra structural
restriction of reciprocal-Xi laws absent from C466d's gamma factor.
Potential use: success would show that an automatic contact barrier
still needs information beyond that restriction; failure would identify
a precise additional condition worth testing, without proving a barrier.

Essential local inputs for comparison are C466a/b's actual-product
scope, C466d's audited model and assessment892's source toolkit.
Before further work, compare the exact L560 statement and its assessment
2026-10-31-l560-independent-countermodel-audit.md for duplication;
its bilateral curvature/PF example is not silently a one-sided
Volterra/contact result. No proof from that lemma was loaded this turn.
Sra's finite actual-PF conclusion does not certify this artificial law.

Continuation/abandonment test: approve a mathematical diagnostic only
after source coverage identifies how to verify every stated premise
and a bounded contact test. Abandon this fixed law if a required
positivity, flatness, lower sign or first-contact condition fails;
retain that evidence without tuning parameters or inferring actual-Xi
failure. Non-PF3 alone and finite plots are insufficient. No proof,
asymptotic sign, convolution positivity or numerical evidence for this
law was derived in step899.

No creative actual-Xi mechanism is ready. A later source review may
prepare a structural obstruction test, but should not label routine
inverse-Laplace specialization creative. Actual cumulative-mass control,
strict forcing, simultaneous contacts, barriers, propagation and final
assembly all remain unresolved. Full matching Mathlib coverage unchecked.

## Completed source comparison900 — 14 November 2026

### Primary sources and their limits

[Sra, arXiv2611.02944v1, 2 November 2026](https://arxiv.org/pdf/2611.02944v1),
53 pages: read Lemma2.1/proof p4; LemmaC.17/proof pp38-39;
TheoremC.14/proof pp34-35; and LemmaC.16/proof pp37-38.
C.17's finite factors have ordered real rates q_j<A<r_j and pair A+-ib.
Its proof explicitly inverts the first real factor and that pair,
and proves positivity using the bracket's successive minima, for any b>0.
Prospective finite-factor substitution: q_1=1, A=3, b=1.
The theorem's finite-window signs instead use compact continuity as b->0;
there is no stated threshold covering b=1 or first/simple contact.
C.14 requires a finite exponential-polynomial expansion, nonzero leading
coefficients and an exponentially smaller remainder beyond the first
nonreal decay group. Its PF obstruction uses finite translates, not a
confluent contact. C.16 assumes all lower differential signs throughout
the claimed interval; it does not supply them. Lemma2.1 concerns actual
Xi's product and zero inputs, not arbitrary products. No conclusion for
the proposed infinite law is imported without its applicability check.

[Kwasnicki, arXiv1710.11023v3, 27 November 2018](https://arxiv.org/pdf/1710.11023v3),
Section6.1 p20: read the complete geometric-smoothing paragraph, including
its final qualification. Its g_m has rates m2^n, is smooth and supported
on the positive half-line, and g_m(x)=m g_1(mx). This supplies the
component at the fixed m=1. Preservation of the source example's excess
second-derivative sign changes requires sufficiently large m; that
conclusion is not available here. Also inspected Definition4.1 and
Theorem4.3/proof p10: real-rate exponential products and variation
diminution are not a general complex-rate determinant-sign theorem.
No bell-shape conclusion is used as a D3 contact certificate.

Reuse the previously inspected scalar-law inputs in assessment892 and
C466b: Steutel--van Harn (2004), Chapter V Theorems2.11/2.16,
equation(2.23), with Chapter III Theorem10.4 for a singular canonical
kernel. [Direct book text](https://www.nzdr.ru/data/media/biblio/kolxoz/M/MV/Steutel%20F.%2C%20van%20Harn%20K.%20Infinite%20divisibility%20of%20probability%20distributions%20on%20real%20line%20%28Dekker%2C%202004%29%28ISBN%200824707249%29%28546s%29_MV_.pdf).
The book was not retrieved again. Applicability still requires the same
law, no drift, left endpoint zero, and its verified positive decreasing
canonical kernel. Integer multiplicities alone do not check these.

[NIST DLMF1.14(iii)](https://dlmf.nist.gov/1.14#iii), live HTML read today:
equations1.14.17-20, 23, 30-31. The one-sided transform uses exp(-st).
Piecewise continuity and exponential growth control establish the domain;
the convolution rule multiplies transforms there. Inversion requires
its stated regularity or decay conditions. Use direct finite integration
or the cited finite inverse when possible; justify absolute convergence
and differentiation separately. These rules do not prove positivity.

### Search and duplicate/failure comparison

Queries included `"(1+s)((s+3)^2+1)"`,
`"matrix-exponential" "complex poles" density positivity`,
`"Pólya frequency" "Wronskian" finite order density`,
`"self-decomposable" "Wronskian" contact`,
`"Laplace transform" "conjugate" "log-concave"`,
and geometric exponential-convolution terminology. Exact-product and
joint-contact searches returned no adequate matching theorem. The useful
stronger overlap was Sra C.17, not a claim of novelty from search failure.

The matrix-exponential searches returned characterization leads that
presuppose a positive density. They were not inspected as primary
theorems or imported. A separated-real-rate lead appeared at
[Evidence Press, version0.2.0-candidate](https://evidencepress.org/releases/separated-rates-exact-polya-order/):
the inspected release states a positive mixture of faster real exponential
rates and real slow factors. Its linked manuscript retrieval was blocked
by a restricted GitHub release URL. The manuscript is unread and no
theorem from it is imported; this is nonessential to the present toolkit,
and no positive real-mixture representation is asserted for this law.
Sra PDF screenshots timed out on two pages, but the full relevant proofs
were accessible in its versioned PDF text; this is not a source blocker.

Read the full L560 proof and its assessment
`2026-10-31-l560-independent-countermodel-audit.md`: its even bilateral
C2 density, open transform strip and negative reciprocal-polynomial jet
do not assert the present one-sided smooth flat joint first contact.
Reuse assessment892's gamma/geometric comparison; C466d's source toolkit
and admissibility range were checked, without reopening its full audit.
Keep the generic scalar stop in
`ATTEMPTS/2026-11-14-generic-scalar-first-contact-barrier-stop-898.md`.
Success here could strengthen that structural diagnostic only. Actual-Xi
cumulative control, strict forcing, simultaneous contacts, barriers,
propagation and L030-L032/C032a assembly remain unresolved.

### Approved bounded mathematical attempt, not an established result

The exact TARGET is unchanged. SPECIALIZE covers the source applications
and only the following model-specific difference: test the full joint
conditions for these fixed factors. Import the finite positive inverse
from C.17's proof and the geometric smoother rather than reprove general
inversion or smoothing theorems. Any additional finite integrations,
series bounds or sign enclosures must be justified as checks of this law.
Derive its canonical kernel from its own transform and verify every
scalar-law premise before invoking the contact identity.

Use a bounded search window 0<x<=16 for a contact witness. A success needs
smooth flat positive p, integrable C1 kernel H with H>0 and H'<0 globally,
the scalar equation for this same p, and x_*,eta>0 with x_*+eta<=16,
D1,D2>0 on (0,x_*+eta), D3>0 on (0,x_*), D3(x_*)=0 and
D3'(x_*)<0. Prove the entire endpoint neighborhood and join it to any
compact certificate; finite sampling or non-PF3 is insufficient.
Bounds need derivatives through order5 for the contact derivative and
complete error control. Do not borrow C466d's gamma-specific sign bounds.

A certified failure of admissibility or any required lower sign before
the proposed contact abandons this fixed law without changing its rates.
No witness within the window, an unresolved enclosure, or inability to
pay the endpoint join is inconclusive: save the precise missing bound
and stop this bounded attempt. A multiple contact does not certify the
target. Do not tune parameters, enlarge the search automatically, or
deduce actual-Xi failure. No missing essential primary theorem prevents
this attempt; unknown model-specific inequalities are its test, not
assumed inputs. Full matching Mathlib coverage remains unchecked.

Outcome: new documented overlap directs the route toward a sourced
specialization, avoiding repetition of known finite inversion, with unresolved contact
conditions (NEGATIVE source comparison). No lemma, script, numerical
test, new mathematical result or RH advance was produced. Next routing
is proof_attempt/development, deep_research/xhigh, because global kernel
admissibility and a complete endpoint/contact join are analytic obligations.
No justified creative actual-Xi target is ready: signed actual-weight
control remains missing, and this structural specialization does not
provide it.
