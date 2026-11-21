# Nominated target: resolvent-to-polynomial ratio on the fixed bump

TARGET: Determine whether L714's ratio Q_n(v)=[sum_(j=0)^(n-1) b_(n,j)*exp(-u*j*v/A)/(d+c_0+u*j/n)]/H_n(exp(-u*v/A)) has a nonzero uniform limit on [omega-delta,omega+delta] along n=12q+3.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 180 searched complex resolvent coefficient multipliers, real-root polynomial ratios, Euler inverses and uniform complex Laplace asymptotics; checked the exact local inputs and three relevant failure records. Primary theorem hypotheses and the distant-tail proof case below were inspected. No exact quotient theorem was found; the bounded search does not establish novelty.
SOURCE_EVIDENCE: Reuse audited L715 and its JKM arXiv:2504.11593v1 Theorem 2.2 assessment; inspected NIST DLMF 2.3(ii), 2.4(i),(iii), equations 2.3.7--8 and 2.4.1,10--13; Temme arXiv:1308.1547v1 Section 2.1 pp.5--7; Nemes arXiv:1802.03962v2 Conditions 1.1/Theorem 1.1 pp.3--4 and Section 2 pp.8--9 (equations 29--30 and the subsequent full-tail bound). Exact scope and links below.
COMPARISON: JKM/L715 supplies the polynomial logarithm only. The inspected endpoint theorems give expansions for fixed analytic phase/amplitude under global separation and convergence hypotheses, not automatically for this n-dependent normalized polynomial array. Their angular uniformity is not uniformity in the full bump parameter. A local Taylor expansion or nonzero H_n cannot supply a relative full-integral estimate.
GAP: For the exact finite ratio, justify any integral representation, then prove a uniform local limit and control its whole tail or an admissible deformation for every v in the original closed bump interval; verify nonvanishing of the limiting ratio independently. Global separation, uniform integrability and any leading factor remain unproved.
REASON: Essential general-tool comparison and duplicate/failure review are complete for one bounded attempt on the unchanged target. The missing triangular-array domination/cancellation estimate is the mathematical test, not an inaccessible essential source. EXPLORE authorizes no asymptotic or nonvanishing conclusion and must receive the separate continuation approval before research use.
LITERATURE_REASON: This target adds the complex resolvent and full integration tail to the previously audited open-disk logarithm; those essential hypotheses lay outside the earlier assessment. This literature-only step completes their source comparison without deriving a quotient formula or result.

SCOPE: Exactly TARGET, with L714 coefficients and the original fixed closed bump interval; use audited L715 only on its proved open-disk domain. Finite algebraic quotient analysis is independent of any unaudited inverse-density use. No new contour, boundary law or signed rate is imported.

## Fixed scope and potential use

Keep L714's coefficients and exact constants U=121/64, N=n-1,
A=27/10, d=5/4, c_0=1/8 and u=(3+4i)/10. Keep the actual fixed
L703/L714 bump chi and its original omega, delta and width; any needed
parameter values must be read narrowly from their canonical definitions.
The original family, unit masses, anchor, inverse denominator angle,
j=0 factor, both endpoints and all moments are unchanged.

The essential inputs are L714's coefficient definition and L715's
audited complex-log limit F, including its root location and exact
normalization. Q_n is a standalone finite algebraic expression here.
L714's inverse-density formula (2) is a possible downstream use and
remains unaudited; this nomination does not assume its correctness
or certify any other part of that reduction.

A nonzero uniform limit would isolate the effect of the resolvent on
the polynomial scale before confronting integration against the fixed
bump. Step 175 exposed this unresolved convolution; the audited F is
material new input since that attempt. This is not a restart of the
absolute horizontal-contour certificate or the positive blend stopped
in the earlier records. The final signed integral can still cancel.

## Original nomination and continuation test

The nomination below is preserved. Its requirement for source comparison
is discharged by step 180; the new EXPLORE decision awaits separate
continuation approval. The mathematical test remains unchanged.

First reuse the prior JKM and signed-remainder assessments for precisely
what they cover. Search the exact weighted-sum/resolvent terminology and
stronger uniform complex Laplace results; inspect primary hypotheses
and the essential tail/cancellation cases, not just real-variable or
fixed-degree analogues. Do not reprove the audited polynomial limit.
No matching Mathlib theorem for this new ratio has been checked.

The proposed mathematical test, only after coverage is approved, asks
for one identified continuous limiting ratio with uniform convergence
on the entire stated compact interval and a strictly positive minimum
modulus. A formal local expansion, numerical ratios, an absolute upper
bound or merely pointwise convergence is insufficient. A proved zero,
nonconvergent subsequence, or competing tail contribution would instead
be informative negative evidence. If an essential source is inaccessible,
park this dependent target and nominate an independent one rather than
repeat source attempts indefinitely.

No boundary limit, endpoint law, saddle dominance, relative asymptotic,
p_n/R_n nonvanishing or signed rate is presumed. Retain log(0)=-infinity.
The fixed bump integration, other frequencies/comb/tails/moments, angular
persistence, complementary spatial Jensen defect, amplitude/full charge,
H/support and actual-Xi realization remain unresolved. The original nomination approved no mathematics. Step 180 below records
source coverage for the same target, without resolving it.

## Completed source comparison — step 180, 3 November 2026

### Exact scope, duplicates and failures

Read L714's Hypotheses, coefficients, (1)--(5), and proof Sections 1--3;
read the needed L715 statement and proof Sections 1--3, reusing its
step-179 audit and the ready polynomial source assessment. L714 (2)
and its general inverse-density reduction remain unaudited. The
standalone quotient needs only its finite coefficient definition and
L715's audited root/log input, not the correctness of that application.
No polynomial limit was reproved or extended.

For the interval, read L703's original parameter/cutoff hypotheses,
L708's fixed-profile hypotheses and L713's defining first section:

    omega=A*[log(9/5)-4/5+(121/100)*log(201/121)],
    delta=2*pi*w, 0<delta<1/3000,
    v in [omega-delta,omega+delta].

These are existing definitions; no numerical width or endpoint law is
selected here. The original eta, w and unit-mass family are retained.
The relevant local search covered the two earlier signed-bump source
assessments, step-175 working record, step-179 history and polynomial
audit assessment. The current quotient was nominated in step 179;
no prior solution of it was located in these records.

Read the specific failure records
`ATTEMPTS/2026-11-03-signed-bump-rate-inconclusive.md`,
`ATTEMPTS/2026-11-03-spatial-boundary-absolute-contour-stop.md`, and
`ATTEMPTS/2026-11-02-positive-blend-signed-saddle-stop.md`.
They respectively leave convolution/outer cancellation unpaid, stop an
absolute horizontal-contour certificate, and stop different blended
weights. None proves convergence or failure of the present quotient.
L715 is the new input since step 175; its use does not reopen the
absolute-contour or blended-weight certificate.

### Queries and primary evidence

Queries included:

- `polynomial coefficient multiplier 1/(a+k/n) asymptotics real negative zeros Stieltjes transform ratio`;
- `uniform complex Laplace method Watson lemma endpoint parameter analytic tail asymptotic theorem`;
- `polynomial resolvent coefficient Laplace asymptotic ratio zeros`;
- `polynomial Euler operator inverse asymptotics zeros`;
- `polynomials complex coefficient multipliers asymptotic integral`;
- `polynomials resolvent exponential profiles`;
- `polynomials 1/(a+k) zeros`.

Search snippets supplied leads only. No exact ratio result was found.

1. **Reused polynomial theorem.** J. Jalowy, Z. Kabluchko and
   A. Marynych, [arXiv:2504.11593v1](https://arxiv.org/pdf/2504.11593v1),
   Definition 1.2 and Theorem 2.2(a),(b),(e), pp.3,5--6.
   Reuse the already inspected profile/zero theorem and its audited
   specialization L715. Its object is the zero measure/Cauchy transform,
   rather than the present weighted finite sum divided by H_n. No
   additional general theorem from this paper is needed or claimed.

2. **Classical endpoint hypotheses.**
   [DLMF 2.3(ii)](https://dlmf.nist.gov/2.3.ii), (2.3.7)--(2.3.8), and
   [2.4(i),(iii)](https://dlmf.nist.gov/2.4), (2.4.1),(2.4.10)--(2.4.13),
   online text retrieved 3 November 2026. Watson requires an endpoint
   expansion and convergent Laplace transform; complex sectors require
   appropriate growth for rotation. The contour version assumes analytic
   phase/amplitude, convergent endpoint series with Re(lambda)>0,
   mu>0, p_0!=0, sector width below pi, absolute uniform convergence at
   the far end, and positive rotated real phase difference away from
   the initial endpoint, uniformly separated at the far end. It yields
   the displayed endpoint expansion with consistent branches. These
   conditions do not certify themselves for our varying polynomial
   integrand. Uniformity in the large parameter's angle does not assert
   uniformity in this v interval. This is tool coverage, not an import
   of the quotient limit.

3. **Uniform complex extension and full-tail case.** G. Nemes,
   *An extension of Laplace's method*,
   [arXiv:1802.03962v2](https://arxiv.org/pdf/1802.03962v2),
   28 June 2018, Conditions 1.1 and Theorem 1.1, pp.3--4;
   Section 2, pp.8--9, equations (29)--(30) and the following tail bound.
   Read all six conditions: analytic p,q,r and contour independent of z;
   finite initial endpoint; convergent local power series with p_0!=0,
   mu>nu>=0 and Re(lambda)>0, fixed branches; closed z-sector of width
   below pi and uniform absolute convergence at a base radius; strict
   angular phase separation with a uniform far-end gap; and r bounded
   by the phase difference there. The theorem gives a sector-uniform
   expansion for exp(-zp+z^(nu/mu)r)q. Remark (3) permits positive real
   phase difference plus corresponding real-part control of r; r=0
   recovers Olver. The distant-tail proof uses the global positive gap,
   a fixed convergent majorant and nu/mu<1. It cannot replace these with
   a local expansion. No supplied fixed-phase reduction or uniform
   majorant for our triangular array meets these hypotheses yet.

4. **Independent Watson comparison.** N. M. Temme,
   *Uniform Asymptotic Methods for Integrals*,
   [arXiv:1308.1547v1](https://arxiv.org/pdf/1308.1547v1),
   7 August 2013, Section 2.1, pp.5--7, (2.1)--(2.3),
   and the bounded-parameter warning following (2.7).
   The stated amplitude is analytic near zero and in a sector, with
   exponential growth control at infinity. Finite Taylor remainders
   underlie the Watson expansion; rotation also needs decay on the
   rotated ray. The following Bessel example warns that increasing
   the extra parameter can destroy the expansion. It supplies no
   automatic growing-array or full-v uniformity theorem.

Additional leads left **unread and unused**: Van Assche
arXiv:2609.12717 (coefficient/zero-distribution comparison), and
arXiv:2610.12498 (search abstract describes integration of a fixed
polynomial). Neither snippet establishes the needed growing complex
quotient theorem. Their unread status is not a source-blocking claim:
the inspected endpoint tools suffice to formulate a bounded direct
attempt, and no theorem from either lead is an essential premise.
No matching Mathlib theorem was checked; no absence claim is made.

### Coverage decision and next mathematical test

DECISION is EXPLORE rather than IMPORT or SPECIALIZE: no inspected
result covers the requested relative quotient, and no asserted
specialization has yet verified the missing global estimates. This
is a completed bounded source comparison, not certified novelty or
negative evidence about convergence. No source access blocker remains
for a direct test on the same target. Reproving JKM or a general Watson
theorem is unnecessary; any necessary triangular-array estimate must
be isolated and proved for the exact finite data in a later turn.

After separate approval of this assessment, one coherent attempt may
use L715's zero representation and logarithmic limit to test local
resolvent behavior together with a uniform bound on the entire
convolution tail. First justify the chosen exact representation from
the finite expression. Keep the original v interval and complex u;
check every interchange and make all constants uniform in v. Analytic
rotation is an option only with a paid deformation and its far edges;
Gevrey bump analyticity is never available as a premise.

Success is one identified continuous limiting ratio, uniform on the
whole original closed interval, with strictly positive minimum modulus.
An actual zero, nonconvergent subsequence or competing tail is an
informative obstruction. Failure to dominate a guessed tail merely
stops that certificate; a finite numerical sample does not settle
convergence. An inconclusive attempt must preserve the unpaid estimate
and use a materially new input before repeating it.

The downstream application remains L714 (2), conditional on its separate
audit, followed by the still unpaid fixed signed bump integration.
Other frequencies, finite-family tails and moments, angular persistence,
complementary spatial Jensen defect, amplitude/full charge, H/support,
actual-Xi realization and all-degree positivity remain unresolved.
No lemma, mathematical script, ratio formula or new bound is produced
in this literature-only step; PROOF.md and DAG.md need no change.
