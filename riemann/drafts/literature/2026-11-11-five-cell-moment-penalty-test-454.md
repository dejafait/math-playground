# Five-cell physical moment penalty: bounded attempt assessment

TARGET: Test a rank-ten cell-moment penalty for the complete L744 energy at K=5 using Li's positive-response/Parseval reduction, with penalty 256, 128 retained responses, 4096 modes per parity and covariance prefix 16384; certify a positive fully paid Schur margin or identify the precise failure of this fixed test.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step454 searched exact Weil/cellwise/neutral/penalty and constrained-Schur terminology externally and in the local joint-energy/neutral assessments and attempts; no inspected matching exact-cell-penalty certificate was located. The stronger paper60 theorem claim overlaps the desired sign and remains source-blocked; no originality claim follows.
SOURCE_EVIDENCE: Li paper45 displayed v2, November9, (2.1), Lemma3.1 with complete arbitrary-a Green-kernel proof, Sections4-5 including full covariance (5.3), weighted-tail (5.4)-(5.5) and closed-form comparison (4.7)-(4.9); Zhu arXiv:2608.24827v2 Section4/Lemma6.1 for complete-block obligations and parity. Detailed inspected cases and exact primary links are in 2026-11-11-five-cell-paid-band-certificate-review-453.md.
COMPARISON: Positive responses, finite-rank terms, Parseval covariance and Schur reduction are known. The proposed fixed physical penalty and its complete constrained margin are not supplied by L743/L744/C744a or the inspected analytic formulas. Paper60 claims a stronger unrestricted sign, but the notebook has not admitted its inaccessible numerical input. This is an independent verification mechanism, not a proposed new support record.
GAP: Establish or fail the quantitative whole-form certificate at the fixed parameters, retaining penalty-tail cross terms, signed poles, every prime power and the entire weighted complement. No positive finite-block margin, tail floor, constraint-preservation argument or effective constant for this test is assumed.
REASON: Use directly accessible analytic source formulas and local supported-delay bounds to test a physical constraint mechanism instead of revisiting blocked artifacts, prime-only neutrality, half-allocation, localization or return-frequency signing. No mathematics was derived in the source turn; this newly ready scope requires separate approval.
SCOPE: Fixed K=5, ell=log(3)/2, L=5ell, complex smooth interval tests and L743 U_5. One penalty value and one response/mode/prefix specification only; no support iteration, growing K, H2 cap, source-file reconstruction or assumed full-form positivity.
LITERATURE_REASON: The saved five-cell source review explicitly requests selecting a numerical or analytic test. Its changed constraint mechanism needed exact-statement searches and accessible complete-covariance source cases, now recorded; further literature needs a changed essential hypothesis or lead.

## Proposed object and relevance

The main gap is L030-L032/C032a actual-Xi positivity. The intermediate
target is a complete-form sign on U_5, with both complex exponential
moments zero on each of its five cells. It could supply a paid joint
arithmetic/archimedean block at one window. All-window positivity,
moment complements and transfer to the main mixed-sign gap remain
independent unresolved obligations.

For the proposed test define the ten-component physical moment map
on the original L2 interval by

    (C u)_(j,sigma) = integral_0^ell
        exp(sigma*(s-ell/2)/2) u(s+j*ell) ds,
    j=0,...,4, sigma=+1,-1.

Use the ordinary sum of the ten squared absolute values, without
normalizing the representers. Investigate the candidate lower bound

    E_L(u) + 256*||C u||^2 >= delta*||u||^2,  delta>0.

This is a proposed inequality, not a proved input. A future attempt
must justify its relationship with L743's moments, interval centering,
reflection/parity and complex coefficients. It must not assume that
an ordinary frequency or coefficient projection preserves C u=0.
The local-centered weights specify the candidate penalty exactly;
altering their normalization alters the fixed test.

## Known inputs to import and specialization to attempt

Use L744 (6) for the complete smooth energy and L743 for U_5 and
the full arithmetic operator. C744a (4) is an available bound for
the original supported prime-delay form; it supplies no pointwise
Fourier-symbol bound. L740/L741 are inherited normalization inputs,
not new positivity assumptions. Do not use L742's conditional result.

Primary analytic input:
[Hongmin Li, paper45, displayed v2](https://rstation.ai/problems/riemann_hypothesis/papers/45),
9 November 2026, Lemma3.1 and Sections4-5. Import the arbitrary-a
Green-response identity with its signed odd pole, then specialize
its lower-form and full-Parseval-covariance method. The numerical
endpoint and supplementary certificate are not inputs. The bounded
physical moment term has to be included in the actual cross covariance;
its positive sign does not authorize deleting mixed terms.

Keep responses with indices j=0,...,127. The specified spatial bases
are the source's cosine and half-integer sine parity bases, rescaled
to a=L/2. Retain q=0,...,4095 in each parity. The weighted covariance
prefix is 4096<=q<16384; every q>=16384 still needs an analytic bound.
These integers specify a test only. Source constants at log(11)/2
or radius2 must not be reused as constants at this a.

The remaining work is quantitative, not a reproof of Schur algebra:
establish a positive lower diagonal on the full complement, enclose
the actual retained matrix and prefix, bound the rest using complete
Parseval covariance and valid increasing weights, then compare the
paid Schur lower matrix with zero. Trace or pivot values must not
be presented as full-operator eigenvalue bounds. Where the lower
comparison needs a form-domain justification, import the source
argument and verify its bounded-term/core hypotheses at this a.

## Bounded continuation and abandonment test

Attempt only this specified penalty/response/mode/prefix combination.
Save unfinished derivations before any lengthy enclosure work. An
analytic estimate may settle the test before matrix assembly. If
computation is used, its complete certificate must state actual and
required bounds, all errors and failures; a float screen is not a sign
certificate. No large matrix or log should be dumped to the chat.

Continue only if a rigorously positive complement floor and paid
finite Schur margin can be obtained. A certified negative direction
of the proposed lower comparison, or a proved incompatible bound,
is an informative failure of this fixed certificate. Merely failing
to certify a pivot or obtaining a nonpositive *lower bound* is
inconclusive: record the exact unpaid quantity, classify honestly,
and do not infer negative actual Weil energy. Do not retune parameters
silently or repeat an unchanged failure; a later retry needs a
materially improved bound or different signed mechanism and coverage.

This is a new proposed quantitative mechanism relative to
the inspected local attempts; its generic finite-rank algebra is
standard. The decisive question is whether the ten exact moments
lift the low signed deficit enough to pay the entire cross covariance,
despite L743's unchanged arithmetic Rayleigh supremum. A success is
independent verification of a sign already claimed by paper60, not
certified originality or a complete RH candidate. Full matching
Mathlib coverage is unchecked. No cross-notebook input is proposed.
