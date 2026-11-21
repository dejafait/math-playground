# Shared-scalar theta/Laguerre averaging — completed source comparison

TARGET: Assess the shared-scalar theta/Laguerre-mixture route for central Jensen hyperbolicity against mixed-characteristic-polynomial and common-interlacing theorems, retaining dependence and unbounded theta support.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step499 read primary DLMF and MSS statements/proof cases and screened a correlated-averaging extension; exact queries, inspected passages and duplicate comparisons are below. No adequate automatic theta-average theorem was identified; no novelty inference.
SOURCE_EVIDENCE: DLMF1.2.8 (2026-09-15), 18.5.12, 13.2.2, 5.5.5, Table18.3.1 and 18.2(vi); MSS, Annals182 (2015), Definitions3.1/3.3, Lemma3.5, Theorem4.1/Lemma4.2, Corollary4.4, Theorem4.5 and relevant complete proofs, pp.331–338; Ravichandran1704.06195v1, definition p.3 and Theorem21 p.12 (statement only, no import).
COMPARISON: Known reference formulas and a precise averaging criterion are available, but neither independence nor common interlacing nor a stable correlated realization is supplied for the proposed theta law. Existing finite-free/LP and universal-preserver stops are reused, not reopened.
GAP: Verify the local normalization/finite moment averaging identity and test the common-interlacing premise on two actual support scales. Actual-weighted compensation and degree-uniform signs remain outside the sources' supplied conclusions.
REASON: Reject an automatic MSS import for its unmet hypotheses; nominate one separate elementary support/normalization specialization before investing in a theta-specific coupling. This is source-scope evidence, not a theorem that the theta average fails.
SCOPE: Completed literature-only comparison; no new mathematical result, lemma, script, root computation or degree sweep. The separate next assessment needs supervisor approval before research.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED; earlier LP, universal-preserver and fixed pointwise-kernel assessments did not cover correlated scalar averaging.

## Original nomination and unproved interface — preserved

The main gap is actual-Xi all-degree mixed positivity. The candidate
interface is the unshifted coefficient family, using the same moments
and factorial convention as L794:

    P_d(x)=sum_(j=0)^d (-1)^j binom(d,j)
           [j! m_j/((2j)! m_0)] x^j,
    m_j=integral_0^infinity u^(2j)K(u)du.

The source review should first locate the exact primary finite Laguerre
coefficient formula and determine whether a shared scalar drawn from
the normalized theta law gives the proposed reference-polynomial average.
This identity is a proposed target, not a result derived in step498.
Then read only the essential real-rooted-average theorem statements and
proof cases, including any independence/rank-one or common-interlacing
hypotheses. Marcus–Spielman–Srivastava's mixed-characteristic/interlacing
work and the DLMF Laguerre formulas are unread primary leads; no theorem
number or applicability is asserted from memory.

Decisive comparison: common scalar randomness is correlated, theta
support is unbounded, and the reference zeros must not be replaced by
the unknown actual zeros. Continue toward a later mathematical test only
if a theorem supplies applicable sufficient conditions or the review
specifies an explicit theta-dependent condition and a bounded test that
does not assume the desired signs. Reject an automatic independence,
interlacing or real-rooted-average import with its exact missing
hypothesis; do not merely cite real-rooted reference polynomials.
No implication from an arbitrary mixture to actual-theta failure is
permitted. Compare any discovered criterion with the existing
universal-preserver and finite-free/LP stops before approving it.

Plausible downstream use is a coefficient-level real-rootedness mechanism
without pointwise positivity of the nonlinear Newton kernel. It remains
conditional on an actual, independently controlled coupling or averaging
property, with degree-uniform control and the main signs unresolved.
The only analytic inputs proposed are L018/L019/L021/L776; L794 is a
contrast, not a positivity premise. No cross-notebook input is required.
Full matching Mathlib coverage is unchecked. A creative nomination is
premature until the representation, source hypotheses and a decisive
theta-specific test have been identified.

## Completed comparison — step499, 5 November 2026

Main gap: actual-Xi all-degree mixed positivity. The intermediate target
was an applicable averaging theorem or a concrete independently testable
theta condition. Its possible use is coefficient-level hyperbolicity
without L794's pointwise Newton-kernel sign. This review supplies source
coverage and a bounded applicability test, not positivity or a new
mathematical obstruction.

### Primary formulas and exact theorem scope

NIST [DLMF18.5.12](https://dlmf.nist.gov/18.5.E12) gives the finite
Laguerre expansion and its factor (alpha+1)_d/d! relative to 1F1.
[13.2.2](https://dlmf.nist.gov/13.2.E2) specifies the hypergeometric
coefficients (a)_j/((b)_j j!), with b not a nonpositive integer.
[5.5.5](https://dlmf.nist.gov/5.5.E5) gives Gamma duplication for
2z outside the nonpositive integers. Read these exact formulas, not
merely search snippets. The reference candidate uses alpha=-1/2 and
b=1/2; checking its scale and coefficient normalization is deferred.
[Table18.3.1](https://dlmf.nist.gov/18.3.T1) has the Laguerre weight
e^(-x)x^alpha on (0,infinity), alpha>-1;
[18.2(vi)](https://dlmf.nist.gov/18.2#vi) gives simple zeros in the
orthogonality interval. These are reference-polynomial facts, not a
theorem about averages over dilations. Inspected online release:
version1.2.8, 15 September 2026, accessed 5 November 2026.

Marcus, Spielman and Srivastava,
[*Interlacing families II*, Annals182 (2015), 327–350](https://www.cs.yale.edu/homes/spielman/PAPERS/Marcus_Spielman_Srivastava_IFII.pdf),
published version, pp.331–338: Definitions3.1/3.3 specify interlacers
and interlacing families. Lemma3.5: equal-degree real polynomials with
positive leading coefficients have common interlacing iff every convex
combination is real-rooted. Theorem4.1 identifies the expected
characteristic polynomial of independent finitely supported column
vectors' rank-one Hermitian outer products with the differential
mixed-characteristic polynomial of their covariance matrices.
Read Lemma4.2 (invertible determinant identity and singular continuity)
and the full induction: independence is used to integrate the last
vector with fixed covariance. Corollary4.4 gives real-rootedness for
PSD matrix inputs via determinant stability, differential operators
and real specialization. Read its complete proof. Theorem4.5's full
proof reweights one independent input and invokes Lemma3.5.
Thus the correlated scalar law is not automatically covered. A distinct
PSD realization could still suffice, but none is provided. Lemma3.5
is cited, not reproved; its earlier cited originals were not inspected.

Independence is not a universal requirement for all known averaging
theorems. Ravichandran,
[*An analytical Lieb-Sokal lemma*, arXiv:1704.06195v1](https://arxiv.org/pdf/1704.06195v1),
20 April 2017, p.3 definition and p.12 Theorem21: a strongly Rayleigh
law on subsets of a finite ground set, together with a fixed Hermitian
matrix, gives a real-rooted expected characteristic polynomial for
the sampled principal-submatrix construction. The definition requires
a real-stable multiaffine generating polynomial. Read the statement,
not its cited original proof; no import is made. A representation of
the proposed scalar-dilation average in this finite-subset framework,
including the required stable law, is unestablished. Its additional
structure cannot be replaced by mere dependence or positive weights.

### Local applicability and limits

L019/L021 were read: they give a positive kernel on u>0, all required
finite moments and the coefficient convention. The initial definition
in L776 was checked for scale compatibility; none of its conditional
Fredholm positivity is used. L018 supplies the completed-Xi context.
The proposed identity remains a specialization to verify later, not a
result established or approved by deriving it during this review.

The scalar is shared by all roots/factors. Replacing it by independent
scalars changes the proposed law and requires a coefficient identity;
conditioning on it alone does not supply the missing unconditional
theorem. No claim that *every* PSD representation is impossible is
made. Similarly, unbounded support is not by itself a mathematical
obstruction: a truncation approach would need moment convergence and
the relevant structural hypotheses uniformly through approximation.
No truncation or limit is invoked here. The endpoint u=0 also needs
care if reference degrees drop; the proposed test uses u>0 only.

There is an explicit theta-dependent sufficient condition to test:
the same-degree reference polynomials across the support should have
a common interlacer. Testing two positive support scales is a necessary
finite test for that full-support premise. The next step is to verify
the exact reference definition, then test degree two at u=1 and u=4.
The scale choices are a proposed discriminating test, not a computed
counterexample. Failure stops this sufficient full-support premise;
it cannot show that the actual fixed-weight average is nonreal-rooted.
A passing pair alone does not establish the premise on the full support.

Compared with `2026-11-04-actual-jensen-mechanism-discovery.md`, the
finite-free/Appell sources require LP or real-rooted inputs; those
conditions still cannot be assumed. Compared with
`2026-11-05-central-growing-signed-mechanism-discovery.md` and
`ATTEMPTS/2026-11-05-central-universal-residual-preserver-stop.md`,
C792a stops universal residual preservation, not scalar-average
interlacing. L794's pointwise product-kernel stop is a different
test. No fixed-grid sweep, new universal-preserver claim or
eventual-shift extrapolation is proposed.

### Searches, leads and route decision

External queries included `Marcus Spielman Srivastava Interlacing
Families II mixed characteristic polynomial common interlacing finite
support`; `site.dlmf.nist.gov 18.5.12 Laguerre`; `Laguerre scale mixtures
real rooted polynomials common interlacing theta Jensen`; `"Laguerre"
"scale mixture" "real rooted"`; `"expected characteristic polynomial"
"correlated" "strongly Rayleigh"`; `"Riemann" "Laguerre" "common
interlacing"`; `"Laguerre" "dilations" "common interlacing"`; and
the Ravichandran/Anari–Oveis Gharan titles. Specific scalar-mixture,
common-interlacing and source-ID phrases were searched in the named
recent local assessments/stops and foundations. An initially oversized
local search was narrowed; its truncated output is not evidence of
exhaustive coverage. No duplicate exact support-scale test was located;
this does not establish novelty.

Search hits for Polson's Gamma(2) location/scale mixture and parameter-
shifted Laguerre interlacing were not theorem-level inspected; no
conclusion is imported. Anari–Oveis Gharan1412.1143v3 returned404;
the primary abstract confirms v2 is current. That uninspected lead is
not an essential blocker because no dependent application is proposed.
Ravichandran's inspected statement suffices to prevent an overbroad
claim that all correlated averages are excluded. Source access is not
the bottleneck for the chosen finite test.

Outcome: NEGATIVE source-scope evidence rejects automatic import and
narrows the route to a concrete hypothesis test. The continuation is
in `2026-11-05-theta-laguerre-support-test.md`, newly written and awaiting
separate supervisor approval. Its normalization/support specialization
is conventional, not creative. A justified creative central mechanism
still lacks an independently controlled theta-weighted coupling or
signed estimate; no quota-based label is substituted. Degree-uniform
control, actual-weighted compensation and all-degree signs remain open.
No lemma or mathematical script was changed; PROOF/DAG are unchanged.
Full matching Mathlib coverage remains unchecked. No RH candidate exists.
