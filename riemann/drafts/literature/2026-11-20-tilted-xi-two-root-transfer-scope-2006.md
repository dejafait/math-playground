# Tilted-Xi transfer: source coverage completed2007

TARGET: Assess primary coverage for specializing C029l's two-distinct-nonreal-zero conclusion to the tilted Xi limit, including symmetry and imaginary-axis zeros.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused convergence-source-review2004 and Hermite assessment2005; searched exact Kuznetsov/two-complex-zero and Xi/real-axis/at-most-two statements; narrowly checked November20 Pollaczek assessments, attempts and histories. Queries and inspected ranges below; no novelty inference.
SOURCE_EVIDENCE: Kuznetsov2008 DOI10.4153/CMB-2008-055-0 pp561-563 and exact weighted statement pp568-569; Titchmarsh1986 second edition Sections2.1/2.2/2.12, equations(2.1.12)-(2.1.15),(2.2.1),(2.12.4), Theorem2.12 and subsequent zero-location argument pp29-31; https://dlmf.nist.gov/25.4 and https://dlmf.nist.gov/25.10 for normalization/symmetry cross-checks. Direct primary PDF links below.
COMPARISON: Known compact convergence, classical Xi properties and C029l cover the inputs to a conditional specialization; no inspected source proves the actual-family eventual index bound. Weighted convergence is explicitly stated on p568, not inferred from fixed-column weight limits.
GAP: A later applicability audit must check real coefficients, eventual nonconstancy with actual degrees, nonzero limit, removal of the exponential factor, symmetry in the correct variable and all axis cases. The eventual uniform negative index<=1 remains an explicit unproved premise.
REASON: New essential Xi-specific primary coverage completes the scope excluded by assessment2005. This is useful local source import, with no mathematical result beyond checked sources and no new derivation in this literature turn.
SCOPE: Exact Kuznetsov family, full complex-plane compact convergence, singular Newton-sum Hermite forms of actual degrees, eventual negative index<=1, and a conditional RH implication only. Arbitrary zero multiplicities allowed; no index estimate, effective onset, finite-degree inference or reciprocal-series continuation.

## Reviewed primary inputs

Alexey Kuznetsov, *Expansion of the Riemann Xi Function in
Meixner-Pollaczek Polynomials*, Canad. Math. Bull.51(4)(2008),561-569,
[DOI](https://doi.org/10.4153/CMB-2008-055-0),
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FD79D70DF68748CCEC70097E3FB9F2FA/S0008439500012492a.pdf/expansion-of-the-riemann-3-function-in-meixner-pollaczek-polynomials.pdf).
Reaccessed p561 normalization/properties, pp562-563 basis/(2)-(5),
and pp568-569 complete weighted passage. Source-review2004's full
Theorem2.1 proof inspection is reused, including its upstream[9]
qualification. The standalone theorem is imported, not reproved.

The source uses Xi(t)=xi(1/2+it) and the usual completed xi.
Its basis is p_k(t)=P_k^(3/4)(t/2;pi/2); beta_k denotes its real b_k
from Theorem2.1(3)-(4), retaining odd terms. Page568 states compact
convergence on C of

    T_N(t)=sum_(k=0)^N [N!/((N-k)!N^k)] beta_k p_k(t)

for N>=1 to F(t)=exp(-pi*t/4)Xi(t). This weighted assertion is
unnumbered; no separate proof is displayed there. Theorem2.1 supplies
ordinary convergence; summability review2004 remains parked, not
silently completed. Page569 reports numerical root behavior only
through degree20, then poses further questions; it supplies no uniform
index theorem. Reality of coefficients and actual degree remain local
applicability checks, rather than inferred from numerical degree labels.

E. C. Titchmarsh, *The Theory of the Riemann Zeta-function*, second
edition revised by D. R. Heath-Brown, Oxford1986,
[Sections2.1-2.2, printed p16 (PDF page13)](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=13),
[Section2.12, printed pp29-31 (PDF pages19-20)](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=19).
Read equations(2.1.12)-(2.1.15), (2.2.1) and its Re(s)>0
convergence statement, Theorem2.12 and the full relevant zero-location
paragraphs through symmetry, before the factorization application.
The book gives entireness, the same xi/Xi normalization and evenness;
its zero-location argument cancels the trivial zeta zeros against gamma
poles, confines xi zeros to the closed strip, and identifies them with
zeta zeros. Equation(2.12.4) uses the positive alternating series for
real 0<s<1 to exclude real zeros there. Endpoint values xi(0)=xi(1)=1/2
are recorded; exterior real points and trivial-zero cancellations are
covered in the preceding paragraph. The following paragraph gives
conjugate and functional-equation symmetries. No simplicity is required.
These are inspected source inputs, not a proof of the proposed
conditional implication. Their different variable conventions must
still be applied explicitly next turn.

[NIST DLMF25.4.3-4](https://dlmf.nist.gov/25.4) confirms the functional
equation and normalization; [25.10(i)](https://dlmf.nist.gov/25.10)
confirms the standard zero symmetries. DLMF is a cross-check; the
real-axis exclusion is taken from the inspected Titchmarsh passage,
not inferred from a statement of strip symmetry. The named elementary
complex exponential identity exp(z)exp(-z)=1 suffices for the tilt factor;
no logarithm branch or zero-divisor assertion is assumed for Xi.

Access: indexed primary PDF text was legible for the needed formulas
and proof paragraphs. Screenshot requests again returned references
without image payloads; no visual inspection is claimed. No essential
source blocker remains for the conditional specialization. Upstream
Kuznetsov[9] remains unaudited as recorded2004; the named source results
are imported with that qualification, not asserted as independently
verified proofs.

## Applicability scope and deferred test

The later audit should keep s and t distinct throughout. It must check
imaginary t against real s, including t=0 and s=0,1, and inspect all
possible coincidences in the zero-symmetry orbit rather than presume
a generic four-point orbit. It must transfer zero locations through the
nonvanishing tilt without claiming F itself is even. The conclusion of
C029l counts distinct zeros only, which must stay explicit; multiplicity
bounds and simplicity are unnecessary proposed inputs, not established
outputs. Eventual nonconstant degree must be justified or stated as an
additional premise; no degree-N assertion is preapproved.

Continue only if these applicability checks hold under the eventual
index premise; otherwise name the failed premise and retain the
conditional distinct-root result. No orbit-count argument, new lemma,
weight identity or numerical test is performed in this source review.
A later canonical proof must cite C029l and the precise external inputs.

## Prior evidence and search limits

Reused source-review2001 (exact finite family and singular Hermite
qualifications), source-review2004 (weighted limit), assessment2005,
C029l and audit2006. Scoped November20 Pollaczek records reveal no
completed Xi-specific transfer. Stops2002/2003 concern Arb runtime;
park2005 concerns immediate recovery routing for summability. Neither
is a mathematical counterexample to this separate target. Nothing is
reset, discarded or reopened. L530/L955's older countermodels give no
actual-family index bound, as already assessed2001.

Queries: `Riemann xi function positive real axis no real zeros Titchmarsh
2.12`; `Kuznetsov Meixner Pollaczek Jensen weighted one pair complex
zeros`; `"Kuznetsov" "two" "complex zeros" Xi`;
`"Riemann" "at most two" "nonreal zeros" symmetry`.
Strongest used coverage is the source convergence plus classical
zero-location facts, not any claimed uniform inertia estimate. Other
search hits were not inspected or imported; no originality follows
from this bounded search. The future scope is a standard conditional
specialization, not a creative central-gap mechanism.

Mathlib: full matching specialization, supporting Xi identities and
axis exclusions not checked; unknown coverage is not absence. No
lemmas/ or scripts/ changes, and no PROOF/DAG update: the argument has
not changed. Main gap L030-L032/C032a and actual-index bottleneck remain.
