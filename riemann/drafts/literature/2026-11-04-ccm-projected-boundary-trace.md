# CCM projected boundary trace — source comparison, step374

TARGET: Assess source coverage for periodic Fourier endpoint averaging and explicit jump subtraction to bound b(P_N k) for the exact CCM trial at fixed lambda=sqrt(13) as N tends to infinity.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched periodic endpoint averaging, Dirichlet-Jordan convergence, piecewise-smooth jump subtraction, Bernoulli Fourier coefficients and coefficient bounds; inspected Lebl's original textbook, Batenkov's published papers and exact CCM/domain passages. Local comparison covered L759/L760/L761/C761a, the finite-trial/observable assessments and recorded fixed-cell failure; details below.
SOURCE_EVIDENCE: Lebl section4.3.2/Theorem4.3.1; Batenkov, Math.Comp.84(2015),2329–2350, Definitions1/3, Proposition2, section2/(2.1), Proposition6/(2.2); Batenkov–Yomdin, Math.Comp.81(2012),277–318, Lemma2.1 and complete proof pp280–281, with degree/termination wording qualified below; DLMF1.2.8 section24.8(i)/(24.8.2)–(24.8.3); CCM2511.22755v1 Lemma5.5/Corollary5.6; Osipov–Rokhlin1301.1707v1 Theorem1/(27), Theorem3/Remark6.
COMPARISON: Known Fourier analysis covers periodic one-sided averaging and an explicit jump model including the seam. CCM's direct boundary theorem assumes the periodic differentiation domain, which L761's L2 transport does not supply. Remaining work is the exact trial specialization and effective constant, not a new general convergence theorem.
GAP: No exact trial jump inventory, endpoint-limit evaluation, effective N-tail constant or denominator lower bound is established here. Source O-estimates do not supply certified trial constants. Ground/trial comparison, ground convergence, family hypotheses, lambda limit and Xi signs remain separate.
REASON: Essential coverage now supports a bounded known-method specialization. No local tail theorem is derived in this literature-only turn. A separate ready continuation is nominated in 2026-11-04-ccm-boundary-trace-specialization.md for next-turn approval.
SCOPE: Fixed lambda=sqrt(13), exact compact angular trial and translated basis of L761/L759, variable N; only b(P_N k). No imposed inversion parity, fitted trial, ground family or RH conclusion.
LITERATURE_REASON: C761a's finite miss led to previously unassessed endpoint/support-jump hypotheses; ready fixed-cell coverage did not cover variable N.

## Primary theorem and proof coverage

[Jiří Lebl, Notes on Diffy Qs, section4.3.2, Theorem4.3.1](https://www.jirka.org/diffyqs/html/moreonfourier_section.html)
was inspected with its preceding definition and both convergence cases.
A finite partition must give finite one-sided function values and a
piecewise-continuous first derivative. At a discontinuity the periodic
Fourier series converges to the mean of the two one-sided limits.
Isolated assigned values do not determine that mean. The text explicitly
supplies no convergence rate. This piecewise-smooth version suffices;
the more general BV theorem is unnecessary here.

[Batenkov, Complete algebraic reconstruction of piecewise-smooth functions
from Fourier data, Math.Comp.84(2015),2329–2350](https://dimabatenkov.info/pdf/batenkov_complete.pdf),
pp2329–2331, Definitions1/3, Proposition2 and section2/Proposition6 were
read. His smoothness class requires continuity through derivative order d,
with the next derivative piecewise continuous and piecewise differentiable;
Proposition2 also requires periodic matching through order d. It yields
coefficient decay O(|n|^(-d-2)) and uniform truncation error O(N^(-d-1)).
Section2 allows periodic-endpoint jumps. Given jumps a_(ell,j) at xi_j,
the periodic Bernoulli polynomial model Phi satisfies

    c_n(Phi)=(1/(2pi)) sum_j exp(-i n xi_j)
                         sum_(ell=0)^d a_(ell,j)/(i n)^(ell+1), n!=0.

Subtracting Phi is the source's existing mechanism. Its abstract
O-constants are not effective trial constants. Nonlinear jump-location
recovery is unnecessary when locations come from the exact definition.

[Batenkov–Yomdin, Algebraic Fourier reconstruction of piecewise smooth
functions, Math.Comp.81(2012),277–318](https://dimabatenkov.info/pdf/batyom_alg_fourier.pdf),
section2, Lemma2.1/(2.1)–(2.2), pp280–281, gives that construction
and its integration-by-parts proof. The coefficient identity is for
nonzero n; the mean must be retained independently. There is a wording
qualification: the displayed V_d contains B_(d+1), despite the surrounding
degree-d description. The proof's literal vanishing-derivative statement
must not be imported for that model. Its relevant final nonzero Fourier
coefficient vanishes for a constant derivative. Use the explicit Bernoulli
formula, not that degree/termination wording. No exact nonpolynomial
coefficient identity without a remainder is imported.

[DLMF section24.8(i), (24.8.2)–(24.8.3)](https://dlmf.nist.gov/24.8),
version1.2.8, released2026-09-15, was inspected to resolve this
normalization/degree issue independently. Its B1 sine and complex series
hold for 0<x<1; the endpoint allowance is only for higher degrees.
Thus endpoint B1 values cannot be substituted into the Fourier series.
The periodic midpoint convention must be supplied by the convergence
theorem. This primary formula suffices for the value-jump model; a new
general reconstruction theorem is unnecessary.

[CCM, Zeta Spectral Triples, arXiv:2511.22755v1, section5.3](https://arxiv.org/html/2511.22755v1#S5.SS3),
Lemma5.5 and its complete Parseval/Cauchy–Schwarz proof, then Corollary5.6,
were read. Their boundary evaluation assumes the periodic self-adjoint
differentiation domain. L2 membership alone does not supply it; jumps
cannot be dropped. Normalization is L^(-1/2) times the basis coefficient
sum, as in L760. Sections5.5/7 distinguish finite eigenvector normalization
from proposed limits. The direct literal-boundary theorem cannot simply
be applied to L761's trial.

[Connes, arXiv:2602.04022v1, sections6.3–6.4](https://arxiv.org/html/2602.04022v1#S6.SS3),
the compact-extension sentence, (20) and footnote20 were checked against
ready definitions: modes are zero outside [-lambda,lambda], and the
trial uses the zero-integral combination and a finite arithmetic sum on
the selected interval. No endpoint vanishing, periodic matching or
ground convergence theorem was extracted.

[Osipov–Rokhlin, arXiv:1301.1707v1, section3.1](https://arxiv.org/html/1301.1707v1#S3.SS1),
Theorem1/(27), Theorem3 and Remark6 were inspected. For c>0 the finite-
Fourier eigenvalues are nonzero; (27) represents the unit-L2 angular
modes and Remark6 gives their entire continuation. This covers angular
piece regularity, not smoothness of the zero extension. The integral
identity offers a route to derivative constants; none is derived here.

## Applicability and bounded continuation

The later specialization must use log(lambda*u) with period L=log(13),
pay the basis normalization, identify every support cutoff and the
periodic seam, and use inward limits rather than assigned endpoint
values. The endpoint-only r=13 term recorded in L761 must be distinguished
from an inward contribution. No jump value or cancellation is assumed.

The concrete mechanism to attempt is value-jump Bernoulli subtraction
(d=0), retaining the jump model's exact finite Fourier sum, then a paid
piecewise integration-by-parts remainder. Its effective constant must
retain first-derivative jumps and absolute second-derivative integrals.
Jump-model tails require geometric-sum/Abel bounds away from their own
jumps; at a jump use symmetric partial sums and the midpoint convention.
These are next-turn tasks, not established trial estimates. A uniform
absolute 1/n tail estimate is inadequate.

Continue if this produces the periodic midpoint and an explicit finite
N-tail constant for N>=1 (or a stated effective onset). Abandon this
implementation if it requires unavailable trace/derivative control or
omitted jump data. An oversized bound may still clarify the trace but
cannot certify a normalized comparison. No denominator nonvanishing,
ground identification or repair of C761a's 1/10 miss is approved.

## Local failures, access and qualifications

The narrow local search used CCM assessments/history and
ATTEMPTS/2026-11-04-ccm-fixed-boundary-observable-miss.md. L761 controls
fixed-projection coefficients and C761a proves the N=120 miss; neither
contains this all-N bound. The older finite-trial comparison already
warned that lowest-energy convergence supplies no trace. These stops
remain intact. No novelty is inferred from the search.

Queries included “Dirichlet Jordan theorem Fourier series endpoint average
bounded variation lecture notes pdf”, “Fourier coefficients piecewise
smooth jumps exact formula Bernoulli polynomials remainder bound Eckhoff
Batenkov”, and “Fourier coefficient bounded variation bound”. Copenhagen
BV notes timed out twice and were not used. An arXiv:1005.1884 HTML
follow-up timed out; the author's published 2012 PDF supplied the full
needed proof. Poonen's 18.03 (2025) Definition26.21/Theorem26.22 and a
Boyd coefficient-bound lead were inspected but are not essential inputs;
Lebl's explicit piecewise-smooth hypotheses and Batenkov's jump formulas
control this assessment. No essential source blocker remains.

Mathlib matching endpoint/jump coverage is unchecked. No lemma,
mathematical script, DAG edge or assembly argument is added. This is
source progress only; the strongest local result remains C761a's miss.
