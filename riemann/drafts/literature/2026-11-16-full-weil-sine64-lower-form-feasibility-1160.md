# One fixed sine-complement lower-form feasibility test

TARGET: Test analytically whether Zhu's frequency-split lower form admits positive complete-complement and coupling bounds for b=log(101)/2 and the unchanged first64 Dirichlet sine modes, stopping before head-matrix assembly if its fixed norm budget fails.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse completed review1160 in 2026-11-16-full-weil-direct-spectral-enclosure-nomination-1159.md: exact sine/logarithmic spectral searches, October30 lower-reduction coverage, parity792 and complement561/619/620 comparisons, and signed-localization583/584 stop. No matching sine64 error constant was found; no novelty claim.
SOURCE_EVIDENCE: Direct primary URLs https://arxiv.org/html/2608.24827v2 ; https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf ; https://arxiv.org/html/2606.09096v3 . Zhu2608.24827v2 Theorem1.1/(4), Lemmas3.1/3.2, full Section4/(12)-(13), Lemma6.1/proof and Section11.1/(16); Teschl GSM99 version12February2009 Section6.3 pp139-141, (6.8)-(6.18),(6.21), Lemmas6.9/6.10 and proofs; reuse Suzuki2606.09096v3 Theorem1.1/Corollary1.2 and the domain inspections in791/1140. Direct URLs and precise limitations are in review1160.
COMPARISON: The known frequency split and bounded-kernel squared-tail estimates permit a fixed analytic feasibility test. The difference is complete sine-coordinate tail/coupling control, not another generic spectral theorem. Legendre decay, Laplacian modal constants, neutral-coordinate estimates and paper162 numerical margins do not transfer.
GAP: Justify the reduced full-complex form and its kernel; derive rigorous complete projected-kernel norm bounds at the fixed parameters and test their resource inequalities. No complement floor, coupling bound, head entry or sign is asserted.
REASON: One source-supported mathematical specialization can decide admission before costly head assembly. A failed sufficient norm budget retires this prescribed certificate, not positivity of the original form. Separate source-gate review1161 verified the direct primary URLs and retained SPECIALIZE for the unchanged target; no mathematics was derived in1160 or1161.
SCOPE: b=log(101)/2,N=64, the original normalized Dirichlet sines, full complex zero-extension log domain, both pole moments and all prime powers n<101. Fix the source cutoff below once. No head-matrix run, parameter sweep, increasing64, replacement basis, source numerical-certificate import, RH or Xi transfer.

## Exact proposed calculation and purpose

The main gap is L030-L032/C032a actual-Xi positivity in every degree.
A positive complete fixed-window enclosure could inform later support
work. The present intermediate target is only its analytic feasibility;
all-support signs, a successful head certificate and actual-Xi assembly
remain independent. This is standard-method specialization/REPRODUCTION,
not a creative sign mechanism or a novelty claim.

Use the form normalized in L744(6), C750f and paper162/v1(2), now on
(-b,b), retaining the complete pole product. The proposed cutoff is

    A_b=sum_(2<=n<101) 2 Lambda(n)/sqrt(n),
    T=2*pi*exp(A_b+2),
    beta=log(T/(2*pi))-1/T-A_b.

These are fixed proposed parameters, not evaluated numbers or proved
bounds in this assessment. First verify all source envelope hypotheses,
including T>=15/4 and beta>0, and the exact101 zero-overlap endpoint.
No substitution of a per-prime lower comb bound for A_b is permitted.
No large integral over this T should be attempted by naive quadrature;
start with analytic bounds and stop as soon as the budget is decided.

Use precisely Zhu's frequency-split lower form (4), with Lemma6.1's
negative odd pole and arbitrary complex coefficients. Justify its
application on the original closed logarithmic domain from the smooth
core; no smooth minimizer, H1 regularity of the whole domain, or finite
Fourier support follows from selecting sines. Import the known reduction
by citation, giving only this applicability argument. Its generic lower
form is the object to test, not the original unbounded operator treated
as a Hilbert-Schmidt kernel.

Let P be the L2 projection onto phi_1,...,phi_64 specified1159 and
Q=I-P. In the bounded reduced form write K=R-beta*I, once its actual
kernel representation is justified. Seek explicit upper bounds delta
for ||QKQ|| and epsilon for ||PKQ||, using complete squared-kernel or
basis-tail sums with every remainder paid. The aim is to test the known
Section4/(13) criterion's complementary resource beta-delta-epsilon>0.
This is a proposed sufficient-budget test, not a bound established here.
If it passes, the required later head floor is strictly above epsilon;
no such floor or head certificate is provided or authorized now.

Teschl's Hilbert-Schmidt norm identities permit complete squared tails
and bound operator norms. When used between different spaces, justify
the maps or their direct-sum encoding. Identify the full kernel, pole
projections, normalization and all complex conjugations before applying
those identities. Use the exact sine transforms from Zhu(16) with the
Fourier-sign convention matched and apparent poles filled by limits.
Do not copy Legendre factorial decay or assume absolute sine row sums
converge. Retain all active arithmetic terms jointly, unless a justified
absolute estimate is explicitly identified as the tested sufficient loss.
Every new local inequality belongs in a canonical proof if established;
no reproof of the cited general block or Hilbert-Schmidt theorems is needed.

Continue only upon proved finite delta,epsilon with
beta-delta-epsilon>0, saving the actual bounds and a full later head
requirement. If the prescribed complete norm estimates cannot leave
that resource positive, record their actual/required values and retire
this certificate without a larger cutoff, altered T or matrix run.
A failed bound or inconclusive interval proves neither a negative
Weil direction nor impossibility of other lower-enclosure methods.
One analytic certificate/obstruction is the whole authorized attempt.

Essential inputs are L030-L032/C032a for relevance, L744(6) and C750f
for normalization/domain qualifications, and review1160's precise known
inputs. C750i/k/l provide no full-form lower bound. C750f's paper162
certificate remains externally qualified and is not needed as a positive
premise. The original complete form's sign, tail effectiveness, all
head margins and Xi transfer remain unresolved. Full matching Mathlib
coverage is unchecked. No cross-notebook input. Further literature
requires a changed hypothesis, essential unread theorem or specific lead,
recorded as LITERATURE_REASON; do not refresh the same sources for balance.

## Separate source-gate review1161 — 2026-11-16

The recovery issue was a missing direct URL in this assessment, not a
missing mathematical estimate. The three URLs in SOURCE_EVIDENCE were
opened successfully. Reused review1160's duplicate/failure comparison;
no new search for a different target and no theorem specialization.

Rechecked [Zhu v2](https://arxiv.org/html/2608.24827v2),
Theorem1.1/(2)-(4), Lemma3.1 and its envelope proof, Section4/(12)-(13)
and its block proof, Lemma6.1 including its proof and following odd-sector
qualification, and Section11.1/(16). The reduction is initially even-real;
the cited parity discussion is essential. Source Legendre localization
is not a sine64 estimate. No claimed source numerical floor is imported.
The full-complex pole normalization, source-to-local comparison and
closed-domain extension remain explicit obligations of the saved test.

Rechecked [Teschl, February12,2009 author version](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
Section6.3 printed pp139-141 (PDF pages150-152), (6.8)-(6.18),(6.21),
including the proofs of Lemmas6.9/6.10 and Corollary6.11. These cover
squared-kernel norms and bounded compressions after the relevant kernel
has been justified; they supply no effective projected sine tail.

Opened [Suzuki v3, September23,2026](https://arxiv.org/html/2606.09096v3)
and checked its localized-form setup (1.1); retain the more detailed
Theorem1.1/Corollary1.2 and core coverage already inspected in791/1140.
No new assertion of a full-domain positive floor follows from that setup.

Decision: SPECIALIZE, unchanged exact TARGET/SCOPE. This separate approval
repairs source traceability and admits the single prescribed mathematical
attempt next turn. Outcome STALLED: no new bound, obstruction or mathematical
advance. No lemmas/scripts/PROOF/DAG changes. Mathlib matching coverage
remains unchecked. The initial notebook-scoped git status was oversized;
no mathematical conclusion relies on its truncated output, and existing
work was preserved.
