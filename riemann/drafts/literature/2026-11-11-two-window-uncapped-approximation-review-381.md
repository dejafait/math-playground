# Two-window uncapped spectral approximation — completed source comparison

TARGET: Assess two-window polynomial approximation on the fixed gamma grid for an O(exp(-n/64)) upper bound on complete-kernel action of every exact band-null unit-TV measure, without a coefficient cap.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step382 searched Laguerre kernel/fixed-frequency exact-null approximation, two-arc varying-exponential polynomial approximation, complex powers, Faber-Walsh and Hermite contour remainders; reused reviews312/344/369 and read the relevant C997c/r/s/t/u contracts. Primary contracts and queries are recorded below; no exact matching rate or novelty was established.
SOURCE_EVIDENCE: Inspected DLMF3.3.3-6/37 https://dlmf.nist.gov/3.3 and Calvi, Lectures on Multivariate Polynomial Interpolation (Hanoi2005), Theorems1.9/1.17/1.18 and their proofs, pp14,20-21, https://www.math.univ-toulouse.fr/~calvi/res_fichiers/MPI.pdf ; Sete-Liesen arXiv1502.07633v2 Theorems2.1/2.3 pp3-5; reused review344's Charpentier-Levenberg-Wielonsky2401.11955v1 Theorem2.4, checking its fixed-target forward proof. Further comparisons and access limits below.
COMPARISON: Hermite's exact finite-degree contour remainder allows n-dependent analytic functions and repeated nodes, but supplies no favorable rate for free. Fixed-function Faber-Walsh asymptotics and weighted approximation-pair theory do not directly pay the two-window complete residual; fixed-weight circular-arc residual asymptotics solve another objective. C997r/t/u retain their stated scopes.
GAP: A polynomial/contour choice and its fully charged growing-n remainder on BOTH windows remain unpaid, including the complete kernel's upper-window growth. No O(exp(-n/64)) bound, arbitrary exact-null obstruction or coefficient-cap estimate is established.
REASON: Essential finite-degree tool coverage is sufficient for one bounded Hermite-interpolation attempt; use the exact remainder rather than a fixed-function limiting rate. No essential source blocker remains for that attempt. The separate ready continuation382 requires later approval before research.
SCOPE: Integer n>=2, I=[7/4,9/4], z_star=1+i/8, gamma_j=15/8+j/(4n), 0<=j<=n; complete C997s kernel, both beta terms/windows, K's -1 and every zero. Coefficients in the proposed comparison are unrestricted; the original capped E_n remains a different quantity.
LITERATURE_REASON: Changed target from one prescribed determinant density to uncapped two-window primal approximation; the required multipoint/weighted approximation hypotheses and growing-degree rate have not been assessed. Reuse existing determinant, cutoff and weak-certificate coverage without retrieving it again.

## Original step381 nomination (preserved; completed comparison below)

### Gap, intermediate target and use

The main gaps remain L030–L032/C032a actual-Xi positivity, L966/L968
signed forcing and unpaid L984(H). C997u's actual-normalized determinant
test did not resolve its rate. Instead of repeating that construction,
review the possibility of a uniform complete-residual approximation by
the same n+1 band columns when the coefficient cap is removed.

The proposed mathematical target after source approval is existence of
coefficients A_(j,n), with NO l1 restriction, and fixed C,n_0 such that

    sup_(c in I) |k_n(c,z_star)-sum_(j=0)^n A_(j,n) k_n(c,gamma_j)|
                         <= C exp(-n/64), n>=n_0.

Its intended use would be to bound every unit-TV measure whose pairings
with all these band columns vanish exactly. Such a bound would direct
future obstruction work toward paid leakage and the original coefficient
cap. It would not give an upper bound on C997s's capped E_n and would
not close any actual-Xi transfer gap. The assertion is a target, not a
claim proved or approved in step381.

One concrete source question is approximation by polynomials of degree
at most n in the variable exp(it/(4n)), multiplied by exp(15it/8).
The complete kernel uses t in [n,n+2] and
[7n/4,9(n+2)/4]. Both compact arcs must be accounted for, including
their overlap at small n if relevant; no lower-window deletion or
division by g_n is allowed. A two-center or multipoint construction is
a possible later recipe, not a constructed polynomial. The source
review must identify the absolute error after integration against the
full n-dependent weight, not just an unweighted asymptotic on one arc.

## Prior failures and source boundaries

C997r allows all truncation orders for one Taylor center at t=2n, but
tests a simultaneous subexponential coefficient norm and sufficient
weighted-defect condition. Its stop is not a complete-residual lower
bound for arbitrary grid coefficients. C997q excludes exact endpoint
homogeneity for finite band measures; the proposed target is approximate.
C997t's quadratic mandatory roots come from a constant-coefficient ODE;
C997u proves only fixed-n admissibility for a variable determinant.
C997s's finite atomic failures do not bound the optimal residual.
All these earlier scopes and evidence must be preserved.

Review344's inspected Charpentier–Levenberg–Wielonsky theorem concerns
weighted holomorphic best polynomial approximation under a regular
compact-set, connected-complement and approximation-pair hypothesis.
It does not by itself verify the present n-dependent target or numerical
rate. Reuse its exact source notes before deciding whether the primary
theorem has a legitimate specialization. General polynomial-density or
fixed-function convergence statements would not pay the required rate.
Review369's discrete complex theorem additionally has Haar and finite-
node hypotheses, and is not imported to this continuum question.

At nomination step381 no primary two-window specialization was inspected
or proved. Step382 below completes tool coverage without proving the
desired specialization or rate. No originality claim or new mathematical
lemma is made. Mathlib matching coverage is not checked.

## Bounded continuation and abandonment test

The next turn compares primary theorem hypotheses, relevant proof cases
and exact existing stops for this one target. Approve a later bounded
research test only with adequate coverage for degree growth, both windows
and the target-dependent weights. A matching quantitative theorem may
be imported with its specialization. If only qualitative approximation
or unpaid n-dependent constants are available, record that distinction;
do not label the desired exponential rate as covered.

For any later mathematical attempt the decisive evidence is a uniform
complete-residual upper bound with rate at least 1/64, or an informative
obstruction to the stated approximation mechanism. Finite fits and
single-window estimates are insufficient. Do not resume C997u's recipe
merely because the new source question is difficult.

Essential inputs: C997c(1),(4)–(6), C997s(2)/step373. C997q/r/t/u are
scope comparisons, not assumptions paying the new approximation.
Unknowns include that approximation itself, any coefficient cap if one
is later reintroduced, C997a(8), selected/both-sign transfer,
assay/reconstruction, complements/regulators, L993, L984(H), L966/L968
forcing and actual-Xi signs. No cross-notebook input is proposed.

## Completed literature-only comparison — step382

11 November 2026. This completes the source question, not the desired
estimate. The original nomination and stopping evidence above are retained.

### Exact finite-degree input

NIST DLMF, live section retrieved 11 November2026 (release identifier
not independently checked), [3.3.3-6 and3.3.37](https://dlmf.nist.gov/3.3#E6):
for analytic f on a simply connected domain D, distinct interpolation
nodes a_0,...,a_n, and a positively oriented simple closed contour C in D
enclosing the nodes and evaluation point y, the degree-at-most-n
interpolant p has the exact remainder

    f(y)-p(y)=(1/(2pi i))*integral_C
        [omega(y)/omega(zeta)]*f(zeta)/(zeta-y) dzeta,
    omega(y)=product_(j=0)^n(y-a_j).

This is not the real mean-value remainder3.3.5, whose real-function/node
hypotheses are inappropriate here. Formula3.3.37 gives the corresponding
complex divided-difference contour integral. The analyticity, enclosure,
contour separation and all n-dependent factors must be checked in use.

For repeated nodes, J.-P. Calvi,
[*Lectures on Multivariate Polynomial Interpolation*, Hanoi, summer2005](https://www.math.univ-toulouse.fr/~calvi/res_fichiers/MPI.pdf),
Chapter1, Theorem1.9 p14, section4.1 p20, Theorems1.17-1.18 p21,
(1.36)-(1.39), gives this same remainder for Lagrange-Hermite
interpolation, counting multiplicities in omega. The domain is simply
connected, f holomorphic, and the piecewise C1 contour has index one
about every node and y. Read the complete1.17 induction: Cauchy's formula
handles degree zero, its derivative formula handles coincident nodes,
and the divided-difference recurrence handles the other case.
Theorem1.18 combines that identity with1.9's Newton remainder; both proofs
were read. Import these named formulas; no reproof is needed.

Applicability to the proposed test is conditional on a chosen log branch
and admissible contour. The spectral coordinate is y=exp(it/(4n)); a
degree-at-most-n polynomial times exp(15it/8) is precisely the allowed
grid-sum form. The target in this coordinate is an n-dependent complex
power, as in C997r's centered binomial identity, not a fixed analytic f.
Hermite's identity is pointwise in degree and therefore permits this
input without asserting a uniform constant. The future attempt must
retain f_n on the entire contour and charge both finite-measure windows
using C997c(4)-(6). No branch-domain or remainder-rate proof is supplied
in this literature step.

### Stronger approximation theorems and their limits

O. Sete and J. Liesen,
[*Properties and examples of Faber-Walsh polynomials*, arXiv1502.07633v2](https://arxiv.org/pdf/1502.07633v2),
retrieved PDF bearing manuscript date12 May2022, Theorems2.1/2.3,
printed pp3-5: E is a union of mutually exterior simply connected
nonpoint compact sets. Its lemniscatic map defines the polynomials.
For a FIXED f analytic on E, with maximal single-valued extension to a
Green-level interior of radius rho>1, its Faber-Walsh series has maximal
root convergence factor1/rho. Read the coefficient contour formula(2.6)
and Theorem2.3(2), including the fixed-f limit and nearby bounds(2.7).
This is not a uniform statement for coupled degree/function/arc limits.
Review312's v1 extremal normalized-polynomial comparison remains valid
on its scope; v2 has different title/numbering. Neither supplies the
present absolute1/64 rate or a complete-kernel representation. No map,
coefficient estimate or fixed-set replacement is assumed here.

Reuse review344's full statement/proof assessment of S. Charpentier,
N. Levenberg and F. Wielonsky,
[*Weighted holomorphic polynomial approximation*, arXiv2401.11955v1](https://arxiv.org/html/2401.11955v1#S2),
Theorem2.4 pp6-7. Rechecked the section2 regularity convention, entire
weight assumption and forward proof. Regular K with connected
complement, an approximation pair(G,W), entire W nonvanishing on G,
and fixed continuous f are essential. The weighted Fekete/Hermite
construction approximates f/W^n before multiplying by W^n; its rate
uses the weighted equilibrium potential. We have established neither
such an approximation pair and its numerical potential nor an identity
between that weighted error and our complete residual. The fixed-target
and entire-weight hypotheses cannot be silently replaced by a local
complex-power branch. Its forward proof reinforces the usefulness of
an explicit Hermite remainder, not the desired estimate by citation.

J. S. Christiansen, B. Eichinger, O. Rubin and M. Zinchenko,
[*Weighted residual polynomials on a circular arc*, arXiv2602.05428v1](https://arxiv.org/html/2602.05428v1),
5 February2026, introduction(1.1)-(1.10) and section4.1 Theorem4.1,
(4.7)-(4.10), were read. The theorem uses a fixed arc and a fixed
weight w=w_0 product|u-u_j|^s_j, with w_0 Riemann integrable and
bounded above and away from zero, fixed points/exponents. It controls
the weighted residual polynomial normalized at an exterior point,
not approximation of our n-dependent complex power. No uniformity
over growing weights or two moving arcs is asserted. No theorem from
this paper is imported and its proof is not needed for that mismatch.
The HTML introduction's link called4.10 points to Theorem4.1 and its
equation4.10; the citation here uses the displayed theorem number.

### Search, duplicates and access qualifications

Queries included `polynomial approximation two arcs varying exponential
analytic function Bernstein Walsh Faber quantitative`, `complex polynomial
interpolation Hermite integral formula analytic contour remainder omega n
theorem lecture notes`, `Faber Walsh polynomials polynomial approximation
two disjoint intervals Sete Liesen 2015 theorem3.3`, `Laguerre kernel
exponential frequency grid exact null measure polynomial approximation
two windows`, and `polynomial approximation varying complex powers
circular arc weighted exponential n`. These bounded searches did not
identify the exact full-kernel conclusion; this is not a novelty claim.

Pritsker-Varga, *Weighted polynomial approximation in the complex plane*,
Kent-hosted `paper_220.pdf`, was a real-power-weight lead. The web PDF
exposed no readable lines; screenshot calls returned only metadata, and
local retrieval failed DNS resolution. Its search excerpt is NOT primary
theorem evidence, so no theorem or disk criterion is imported. This is
nonessential to the accessible exact Hermite formula; no retry is needed
before the proposed test. Austin's2016 thesis Hermite Theorem1.11 was
located, but its surrounding proof was not assessed or used. The2025
incomplete-polynomial paper and Fourier-extension hits remain unused
leads; no conclusion depends on them.

The targeted local search found review312's earlier Faber-Walsh coverage;
reuse it rather than reprove its extremal statement. Read C997c through
(6), C997r's hypotheses/conclusions and(5), C997s(2) and step373's
pairing/kernel audit, and C997t/u's hypotheses/conclusions. C997r's
coefficient-norm dichotomy does not exclude an uncapped interpolant;
its defect lower bound is not a residual lower bound. C997t is limited
to common constant-coefficient differential densities; C997u is parked
with its normalized determinant rate unresolved. C997s's finite lower
certificates do not decide an asymptotic upper bound. Preserve all stops.

### Decision and bounded continuation

EXPLORE approves tool coverage only. Nominate one prospective two-center
Hermite test, with interpolation multiplicities adding to n+1, split as
equally as possible at the spectral images of t=n+1 and t=2(n+1).
These are candidate interpolation nodes, not new band frequencies.
The precise construction, branch verification, estimates and conversion
to complete kernel coefficients remain future mathematical work.
Record that exact target in continuation382 for separate later approval.

Success means a uniform complete-residual bound C exp(-n/64) for all
sufficiently large integers n, with both windows, every zero, both beta
terms, K's subtraction and endpoint values retained. A fully charged
contour estimate with insufficient rate is only failure of that estimate;
a rigorous lower obstruction would stop the stated interpolant. Failure
to obtain either is inconclusive and parks this recipe. No finite fit,
fixed-function root rate, or large coefficient bound decides the target.

There is no source import resolving the target, mathematical advance
beyond the checked literature, lemma/script change, RH candidate or
change to PROOF/DAG. Full matching Mathlib coverage remains unchecked;
none is an input. Essential local inputs and independent unresolved
assumptions remain exactly those recorded above.
