# Untilting before approximation — completed source comparison2064

TARGET: Review primary Meixner–Pollaczek angle/connection and exponential-multiplication formulas for constructing untilted-Xi approximants, and decide whether they provide a root-defect estimate independent of the failed scalar-node condition.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded angle/connection/exponential search2064; primary match1405.1918v2 inspected. Scoped Romik/Pollaczek assessments expose prior direct-untilted coverage and the actual-measure qualification in L530. Queries and read boundaries below; no novelty or exhaustive-search claim.
SOURCE_EVIDENCE: Baeder–Cohl–Volkmer, https://arxiv.org/pdf/1405.1918v2, Section5 pp14–16, Lemma5.1 and Theorems5.3–5.4 with proofs; DLMF18.19.8/18.23.7; Romik1902.06330v3 Theorem3.1/Section3.2, reusing October30 coverage of Section3.4.
COMPARISON: Angle connection preserves the fixed polynomial. The exponential generating identity concerns its generating variable, not multiplication of Xi by exp(pi*t/4). A direct untilted compact expansion is already known and locally assessed; none of these inputs pays its root-defect estimate.
GAP: No source-defined transformed Jensen coefficient rule with a uniform root bound is supplied. The actual theta coefficient restriction, initial signs, all-degree control and Xi transfer remain unpaid. This source-scope stop neither refutes the known untilted expansion nor transfers L530's endpoint-atom witness to its actual measure.
REASON: The primary hypotheses are accessible and the nomination fails its stated discriminator: construction/convergence overlap is known, while independent zero control is absent from the inspected transformations. Park this nomination; no new lemma, calculation, repeated source fetch or generic moment-flow retest is approved.
LITERATURE_REASON: The saved REVIEW_REQUIRED question required previously unread general-angle and exponential generating identities; existing convergence and finite-obstruction assessments are reused without redoing their mathematics.
SCOPE: Completed literature-only comparison, including essential proof cases and explicit scope limits. EXPLORE describes search coverage, not authorization for an unspecified mathematical continuation. The original nomination below is preserved as historical scope.

## Completed primary comparison — 21 November 2026

The main gap and downstream use remain those in the nomination below.
This step supplied source-scope evidence only. No coefficient map,
approximation theorem or root estimate was derived.

### Exact angle and exponential statements

Michael A. Baeder, Howard S. Cohl and Hans Volkmer,
*Generalizations of generating functions for higher continuous
hypergeometric orthogonal polynomials in the Askey scheme*,
[v2, 23 October 2014](https://arxiv.org/pdf/1405.1918v2), pp14–16:
Lemma5.1, (5.2), for lambda>0 and phi,psi in (0,pi), states

    P_n^(lambda)(x;phi) = sin(psi)^(-n) sum_(k=0)^n
      (2lambda+k)_(n-k)/(n-k)! * sin(phi)^k
      * sin(psi-phi)^(n-k) P_k^(lambda)(x;psi).

Its proof takes a finite continuous-dual-Hahn connection limit.
Theorem5.3 requires real x and
|rho|(sin(phi)+|sin(psi-phi)|)<sin(psi). Its transformed series uses
rho_tilde=rho*sin(phi)/(sin(psi)-rho*sin(psi-phi)). The proof bounds
the absolute double series by a polynomial times a geometric series.
Theorem5.4 assumes lambda>0, both angles in (0,pi), rho complex;
it inserts exp(rho*exp(-i*phi)*sin(psi-phi)/sin(psi)) into a confluent
hypergeometric generating identity. Its proof uses factorial summability.
Neither theorem bounds zeros of partial sums.

Use PDF numbering: the HTML misnumbers theorems as zero and shifts
equation labels. The inspected proofs import upstream connection/limit
identities; no independent audit of those inputs is claimed.

The [NIST author slides](https://math.nist.gov/~HCohl/ucoim2014.pdf),
9 July2014, slides43–44, were a discovery lead; the paper supersedes
them as the theorem/proof citation. One PDF screenshot request timed
out; complete relevant parsed PDF text and HTML were accessible.
This is not an essential source blocker.

### Applicability limits

[DLMF18.19.8](https://dlmf.nist.gov/18.19.E8) gives
w(x)=|Gamma(lambda+i*x)|^2 exp((2phi-pi)*x),
lambda>0, 0<phi<pi. [DLMF18.23.7](https://dlmf.nist.gov/18.23.E7)
gives its generating product for |z|<1; the logarithms are the branches
analytic at z=0. Served version1.2.8, release15September2026.
The exponential here is part of the orthogonality weight. It is not
a zero-control theorem for arbitrary linear combinations.

Applicability judgment: lambda=3/4 and source angle pi/2 satisfy the
parameter hypotheses. Applying the finite connection identity to
C029m's already fixed T_N reexpresses that same polynomial. Applying
an infinite identity before truncation would instead require the
actual transformed coefficients and justified summation/remainder
control. Neither the geometric nor factorial coefficient hypotheses
identify C029m's arbitrary beta_k as the generating coefficients.
No analytic extension to complex x or endpoint rho is assumed here.
In particular, rho is not the Xi variable t; the source exponential
does not supply an exp(pi*t/4) multiplication operator on T_N.
This is a theorem-applicability comparison, not an impossibility
theorem for alternative constructions.

### Known untilted construction and duplicate boundary

Romik, [arXiv:1902.06330v3](https://arxiv.org/html/1902.06330v3),
5May2019, (3.1)–(3.5), Theorem3.1 and Section3.2, already expands
untilted Xi in sum_j (-1)^j c_(2j) P_(2j)^(3/4)(t/2;pi/2),
uniformly on every complex compact. The coefficients are the positive
theta integrals (3.3). Rechecked the convergence proof: compact basis
bounds, reflection and exponential integral-tail estimates justify
the interchange and summable remainder. No root bound follows there.
Reuse the October30 assessment for Theorems3.6–3.8/Proposition3.9;
the latter's reported example is not imported as a certified obstruction.

The exact actual-measure comparison is already recorded in
[assessment October30](2026-10-30-theta-pollaczek-weighted-discriminator.md).
L530's fully read canonical counterexample has endpoint atoms 0 and1;
it is not the actual theta measure. Thus smooth/open-support/theta
restrictions are not refuted by it. Conversely, merely recalling that
positive moment formula repeats existing coverage and supplies no new
root-control premise. C029m's full tilted beta_k and these even c_(2j)
must not be identified. C029n/q coefficient conventions and
C029x/y finite stops remain unchanged and concern their stated families.

### Search boundary and decision

Queries: `Meixner Pollaczek polynomials connection formula different
angle zeros exponential multiplication Kuznetsov Riemann xi`;
`Meixner-Pollaczek connection phi polynomials angle formula`;
`Meixner-Pollaczek multiplication exponential Romik zeros`;
`Cohl Costas-Santos Wakhare Meixner Pollaczek connection relations
generating functions 2014 angle`; exact generating-function title;
`Meixner-Pollaczek exponential multiplication polynomials connection`.
Search-only leads on plane waves, associated polynomials, Christoffel
modifications and stochastic martingales were not imported. The
Meixner/Krawtchouk paper1509.01027 is not the selected continuous-angle
theorem. No additional root theorem was established by these searches.

The bounded test required both an actual changed approximation mechanism
and an independently supported root-defect claim. The former has known
overlap; the latter is unpaid. Outcome NEGATIVE closes this nomination
on that precise source evidence, with no progress beyond the sources.
No mathematical script, lemma or proof/DAG change is warranted.
Mathlib full transformation/root-bound coverage is unchecked.
No cross-notebook input was used.

## Original nomination2063 (preserved)

## Three-mechanism comparison and bounded test

1. More computation of the prescribed scalar Q_6 cannot meet its four-node
   premise: C029y, now independently audited2063, gives exactly two.
   Preserve stop2061; neither higher-degree sampling nor a repeated audit
   is the selected continuation.
2. The existing finite-matrix propagation shortcuts have actual-input
   obstructions: C029n's boundary-supported metric is inconsistent and
   C029x's specified difference has rank at least three. Merely enlarging
   the same ansatz without a new controlling theorem supplies no justified
   uniform estimate. Their stops remain local, not global bans.
3. Select source discovery for an untilted family before truncation. The
   concrete question is whether a primary transformation theorem gives an
   exact actual-coefficient construction together with usable zero control.
   A connection identity alone, positivity of a weight alone, or numerical
   evidence does not meet that test.

Inspect primary Meixner–Pollaczek general-angle connection/generating
identities and any cited exponential-multiplication or zero-preservation
theorem. Identify the actual transformed function, parameters, signs,
domains, summability, and whether the result acts on a fixed polynomial or
changes the approximating sequence. These sources have not been read for
this target. Reuse C029m's family conventions and previously assessed
Kuznetsov passages; additional reading needs a specific missing hypothesis.

Continue toward a separately gated mathematical target only if exact
source hypotheses support a genuinely changed approximation mechanism and
an independently testable root-defect claim. If the sources merely change
coordinates, multiply by a nonpolynomial, require already-real zeros, or
leave all root control unpaid, record that obstruction and stop this
nomination after the bounded review. Do not replace it with a theorem
equivalent to RH and label that progress.

Plausible downstream use is a uniform finite nonreal-zero bound for
approximants to the even untilted Xi, to be combined with an independently
justified compact-limit/symmetry argument. It is not asserted that the
sources supply such a bound. Essential current inputs: C029m's exact full
family/tilt, C029n and C029q coefficient conventions, audited C029y and
C029x as contrasts only. Uniform index/root control, convergence of any new
family, actual degrees, multiplicities, initialization and Xi transfer
remain open. No cross-notebook input. Mathlib coverage of the proposed
transformation and bound is unchecked.
