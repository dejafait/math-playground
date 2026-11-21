# Direct archimedean payment — completed source comparison

TARGET: Assess whether known results cover A(f)>=W_b(h)/2 for every complex globally neutral f in C_c^infinity(0,4log3), with A the full archimedean digamma form and W_b as in L748.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step310 searched the literal digamma/logarithmic-resource comparison and finite-support neutral Weil forms; reused the compensated and modulation assessments and checked the R-only, carrier and generic-energy failures. Queries and inspected/unread distinctions are recorded below; no adequate matching theorem was located and no novelty is inferred.
SOURCE_EVIDENCE: Reuse Beckner math/0701939v6 Thm4/(12) and Laptev--Weth 2009.03395v2 Thm4.1/(4.1) under step308's inspected hypotheses; L748 (1)-(5), L744 (6) and L743 (1). Directly read Connes--Consani author version 4 July2021 Thm1 p.2 and Thm6.11/proof pp.44-45; Zhu 2608.24827v2 Lem2.5/proof and Lem3.1/proof, Sections2.1/3; NIST DLMF5.9.16 and 5.11(ii)'s complex remainder paragraph.
COMPARISON: The uncertainty sources control W_b but do not compare it with A. The Sonin theorem has a smaller support window and a different resource; the high-frequency estimate does not settle the bounded frequencies. Exact smooth-form identities are available for a bounded witness test, but no inspected theorem proves or refutes the literal universal inequality.
GAP: The sign of A(f)-W_b(h)/2 on the exact-neutral smooth class remains unproved. A finite trial-space failure would refute only this payment inequality; trial-space positivity would not prove it. Other prime powers and support propagation remain independent gaps.
REASON: Essential source coverage is now sufficient for one bounded counterexample screen without reproof of the uncertainty imports. Approve only the covered continuation below for separate next-turn execution; this literature turn derives no new inequality, witness or lemma.
LITERATURE_REASON: First source comparison of the changed digamma-versus-resource inequality nominated at step309; reuse ready uncertainty coverage rather than repeat its discovery. No further unchanged-scope literature turn is needed before the bounded test.
SCOPE: Exact target below, b=2log3, complex C_c^infinity(0,4log3), zero extensions, both exact global moments, full W_b. One real smooth trial-space counterexample screen is covered because a witness in that subclass suffices to refute the universal assertion. No arbitrary-support positivity, finite-dimensional positivity inference, new source-certificate replay or RH claim is approved.
COVERED_TARGET: Test the direct payment inequality A(f)>=W_b(h)/2 on the six-mode smooth trial space specified in the assessment, imposing both global exponential moments exactly and seeking a rigorous negative defect certificate.

The nomination text below is retained as historical gate language.
Step310's completed comparison and bounded continuation supersede its
pending-review instructions; the mathematical question is unchanged.

## Exact target for the next source review

Keep L748's b=2log3, L=2b=4log3, h(y)=f(y+b), whole-line
zero extensions and both exact global exponential moments. No parity,
cellwise constraints or carrier restriction is added. Define

    F_f(t)=integral_R exp(-itx)f(x)dx,
    A(f)=integral_R [Re psi(1/4+it/2)-log pi]
                         |F_f(t)|^2dt/(2pi).

This is precisely the archimedean part in L744 (6); its pole term
vanishes on the stated exact-neutral class. W_b is the full resource
of L748 (1), including all exterior pairs of its Beckner term and its
added finite spatial integral. The proposed comparison is

    A(f)>=W_b(h)/2                       for all stated f.

This is an unproved question, not an imported theorem or a conclusion
of step309. Essential input IDs for the continuation are L744 (6)
and L748 (1)-(3); L743 fixes the arithmetic coefficient. No other
claim of L744 is needed. Review its exact source normalization and
the existing compensated assessments before seeking new coverage.

## Use and discriminating test

If established, this would pay the already bounded first-prime term
from the actual archimedean resource on this one window. It would not
pay the other primes or give full Weil positivity, growing support or
RH. If false, a later rigorous smooth exact-neutral witness would
stop this direct payment inequality while preserving L748. A generic
unweighted bound, a restricted positive trial family or a numerical
preview cannot establish the universal statement.

The next turn must compare precise known logarithmic/digamma form
estimates and finite-codimension neutral constraints with this exact
statement, including stronger conclusions and known obstructions.
Reuse the ready uncertainty-source assessments; retrieve a new source
only for an essential changed hypothesis or relevant new lead. A
matching theorem should be imported with its constants. Otherwise
record the uncovered difference and a bounded subsequent proof or
counterexample test. No mathematical attempt is authorized by this
nomination itself. Mathlib matching coverage remains unchecked.

No justified creative all-window mechanism follows from the passing
audit: an independent payment/complement estimate is missing. This
screen makes one such missing premise explicit; it is not labeled
creative merely to meet a scheduling preference.

## Completed review — step310, 4 November 2026

### Relevance, duplicates and retained failures

Main gap: unconditional actual-Xi mixed positivity. This target is only
one sufficient payment on one window. A proof could combine with L748's
accepted allocation to pay the first-prime term; it would leave the
remaining prime powers, signed complements and support propagation open.
A counterexample would stop this direct inequality and preserve L748.

Read L748's hypotheses, conclusions and resource conversion (4)-(7),
L744 through the exact smooth identity (6), and L743's hypotheses/(1).
In particular the already established identity, quoted without a new
conversion, is L748 (5):

    W_b(h)=q(h)+(log b-psi(1/4)-log2)||h||_2^2,
    q(h)=integral log|t| |F_h(t)|^2 dt/(2pi).

Reuse the [compensated assessment](2026-11-04-spatially-compensated-first-prime-budget.md)
and [its source-scope audit assessment](2026-11-04-compensated-first-prime-allocation-audit.md).
The named [R-only failure](../../ATTEMPTS/2026-11-04-first-prime-half-beckner-budget-stop.md)
concerns a different resource. The
[carrier scope limit](../../ATTEMPTS/2026-11-04-carrier-span-general-sign-scope-limit.md)
and [generic-energy source stop](../../ATTEMPTS/2026-11-04-joint-energy-generic-source-scope-stop.md)
exclude unjustified whole-space/complement imports, not this payment
question. Narrow searches of the compensated assessment, L748 and
step309 history found the unpaid-cost qualification, not a duplicate
payment theorem or counterexample. No stopped route is reopened here.

### Primary source comparison

**Uncertainty inputs, reused.** Beckner, *Pitt's inequality and the
fractional Laplacian: sharp error estimates*,
[math/0701939v6, Thm4/(12), p.5](https://arxiv.org/pdf/math/0701939v6#page=5),
and Laptev--Weth, *Spectral properties of the logarithmic Laplacian*,
[2009.03395v2, Thm4.1/(4.1), p.7](https://arxiv.org/pdf/2009.03395v2#page=7),
have already inspected complex-Schwartz and zero-extension form scope.
Step308 includes the relevant proof cases and dimension-one check;
no source sharpness proof is repeated. The latter PDF's form/domain
(1.1)-(1.3) was retrieved again. These results control the logarithmic
resource. Neither states the proposed digamma comparison.

**Sonin comparison.** Connes--Consani, *Weil positivity and Trace formula,
the archimedean place*,
[author version 4 July2021](https://alainconnes.org/wp-content/uploads/Selecta.pdf),
Thm1 p.2 requires multiplicative support [2^(-1/2),2^(1/2)] and
transform zeros at i/2 and 0. Its lower bound uses a Sonin trace.
Thm6.11 pp.44-45 uses a zero at -i/2 and retains a correction at 0.
Read its support-preserving primitive and trace/error-form proof.
Neither theorem covers our additive interval of length 4log3 or the
resource W_b/2. Global exp(+-x/2) moments do not supply the stated
additional zero at frequency 0 as a cited premise. No dilation or
changed-inner-product transfer is imported.

**Digamma evaluation and tails.**
[NIST DLMF5.9.16](https://dlmf.nist.gov/5.9.E16) gives the Gauss integral
for psi(z)+gamma on Re z>0; this includes z=1/4+it/2.
Reuse the [modulation-audit assessment](2026-11-04-uniform-neutral-modulation-energy-audit.md)
for [DLMF5.11.2](https://dlmf.nist.gov/5.11.E2) and
[5.11(ii)](https://dlmf.nist.gov/5.11.ii), whose complex remainder
paragraph was directly read again. It bounds truncation error by the
first omitted term times the stated sector factor. These are scalar
evaluation/tail tools, not an all-frequency neutral payment theorem.
No new integration estimate is derived here.

**A possible evaluation aid, not a positivity import.** Zhu,
[2608.24827v2, Section2.1 Lem2.5 and Section3 Lem3.1](https://arxiv.org/html/2608.24827v2#S2.SS1),
was read through both proofs. Lem2.5 assumes real even continuous g
supported in [-2L_source,2L_source], an existing one-sided slope at 0,
and integrability of |F_g(t)|log(2+|t|). It gives the archimedean
integral including its tail constant; its proof checks absolute Fubini
and the origin limit. A later real smooth autocorrelation application
must verify those hypotheses and 2L_source=4log3. Lem3.1 gives a
one-sided high-frequency bound for t>=15/4, not the required universal
comparison. No numerical source certificate or wider positivity claim
is imported. Smooth cutoffs do not inherit the paper's polynomial
example's analyticity or its geometric quadrature-error assertion.

Mathlib: full matching coverage remains unchecked. Standard Plancherel,
Fourier inversion and finite-dimensional linear algebra are supporting
named inputs, not a matching theorem for the payment inequality.

### Search record and scope of the conclusion

External queries actually submitted:

- `archimedean Weil quadratic form digamma positivity compact support Connes Consani`
- `"digamma" "logarithmic Laplacian" inequality`
- `Weil archimedean logarithmic uncertainty neutral exponential moments lower bound`
- `"Re" "psi" "1/4" "log" "inequality" Weil archimedean`
- `"archimedean" "Beckner" Weil positivity`
- `"digamma" "quadratic form" "neutral"`
- `"digamma" "logarithmic uncertainty" inequality`
- `"archimedean" "spatial" "Beckner"`
- `"Weil" "exponential moments" "digamma"`

Only the primary passages identified above support this decision.
Search hits for logarithmic-Laplacian Dirichlet problems, metaplectic
uncertainty and finite Weil matrices were not inspected as matching
payment theorems. Secondary courses, mirrors, GitHub claims and snippets
were not treated as proof. The parked paper60 certificate is not retried.
These are unread/nonessential leads, not inaccessible essential inputs.
No inspected source proves or refutes the literal inequality. This is
bounded coverage, not a claim of novelty or nonexistence of a theorem.

### Covered next test; no test performed in this turn

Use the exact COVERED_TARGET above, retaining L744 (6), L748 (1)-(5),
b=2log3, L=4log3, h(y)=f(y+b), zero extensions, both global moments
and the whole resource. L743 (1) is needed only for the downstream
arithmetic interpretation. No RH or conditional L742 input is allowed.

One prospective finite family is fixed as follows. Put delta=L/40.
Use the standard smooth step theta(s)=eta(s)/(eta(s)+eta(1-s)),
where eta(s)=exp(-1/s) for s>0 and 0 otherwise. Define

    chi(x)=theta((x-delta)/delta)*theta((L-delta-x)/delta),
    phi_k(x)=chi(x)*sin(k*pi*x/L),  k=1,...,6.

Test real linear combinations of these six functions subject to both
exact exp(+-x/2) moments. This is a proposed test definition, not a
constructed neutral witness or a new proved inequality. Verify smooth
compact support, a nonzero exact-neutral vector, and all source-form
hypotheses in the mathematical turn. An exact integral-defined nullspace
is acceptable if its rank/nonvanishing and enclosure errors are proved;
rounded approximate moments are insufficient.

The decisive threshold is a rigorous upper bound strictly below zero
for A(f)-W_b(h)/2 for one nonzero such f. Certify every omitted Fourier
tail, log singularity, quadrature error and coefficient error, or replace
numerics by a complete analytic estimate using the cited formulas.
Use L748 (5) only with its exact normalization; do not truncate its
original exterior pairs. Save complete certificates to disk and inspect
all load-bearing bounds. A floating preview is not evidence of failure.

One six-mode screen at this fixed cutoff is the bound on this attempt.
A negative certificate abandons this direct payment inequality only.
A certified nonnegative trial form closes this trial-family screen but
leaves the universal inequality open; an unresolved error enclosure is
inconclusive. Do not keep enlarging the family or call trial positivity
a universal proof without a materially new test and source gate.

The continuation is calculation/standard/high under EXPLORE, potentially
new only in the policy's limited searched-scope sense. It is not labeled
creative: a fixed-window resource screen supplies no new central
support-propagation or signed-complement mechanism. That independent
missing mechanism remains the blocker to justified creative routing.
The supervisor's separate approval next turn is respected. No lemma,
mathematical script, PROOF.md or DAG.md was modified in this literature
step; no new mathematical claim is accepted by this assessment.
