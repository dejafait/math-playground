# Source comparison: complete-response cancellation at the sampled support edge

TARGET: Assess source coverage for transferring L721's support-edge singularity to the complete response G_n(u_*,-1), including the exact cancellation mechanisms in L713's comb, remote-frequency, physical-tail and finite-moment terms.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 200 searched exact full-response/support-edge terminology, Poisson summation for moving rational products, Cauchy-transform jump cancellation and analytic support/FIO exclusion of remote contributions; read the primary Plemelj and Poisson statements/proof cases below and reused the recorded analytic-support and generating-function assessments. Scoped local comparison found no established joint germ for this complete response; no novelty inference follows.
SOURCE_EVIDENCE: S. Tanveer, Week 8 lectures, Definition 1.3/(1.5), Theorem 1.1, Lemmas 1.5–1.6, proof and Remark 1.9, pp.2–5; S. D. Miller, Some notes on distributions (15 January 2006), Theorem 4.1/proof p.7 and Section 6/(6.1)–(6.2) p.9; reused Hitrik–Sjostrand v1 Theorems 2.2.3/2.7.1, Deleporte v1 Propositions 4.23–4.24, Mazzucchelli–Salo–Tzou author-version Theorems 1.2–1.3/5.1/6.1 and the size-generating-function assessment's exact reading limits. Links, hypotheses and limits below.
COMPARISON: The known results identify jumps or preserve singularities for an already identified operator/germ with the stated localization hypotheses; they do not construct or separate this complete discrete response. L721 handles K_n only. L713 retains every correction but does not give their size-generating germs. A correction on the same local arc can defeat inheritance; an interior jump alone does not prove an endpoint singularity of the germ from zero.
GAP: Verify L713's full identity at the specified center, construct compatible germs or a joint representation for all retained terms, justify exchanges and continuation from zero, and decide whether their total local contribution cancels the L721 edge. No full-response convergence radius, correction analyticity or noncancellation is established.
REASON: Essential generic source coverage is available and the bounded comparison found no matching full-response theorem. EXPLORE covers one joint-cancellation attempt, not another single-bump support proof or a repetition of stopped remainder subordination. The newly covered continuation requires the supervisor's separate approval before research use.
SCOPE: Original L666/L703/L708 family only; fixed chi, 0<delta<1/3000, actual b=sup supp chi, n=12q+3, u_*=(3+4i)/10 and spatial argument -1. Retain comb, negative/high frequencies, both physical tails and every M=n/3 moment. No n-dependent profile, endpoint law, assumed noncancellation, noninteger-size interpolation or unverified full identity is granted.
COVERED_TARGET: Test whether the complete sampled germ of n^(-1/2)G_n(u_*,-1) retains L721's support-edge singularity at z_*=exp(-12*S(b)) by identifying the joint local contribution of L713's comb, remote-frequency, physical-tail and finite-moment terms.
LITERATURE_REASON: The full finite response is a changed observable after L722's audited stop; earlier ready coverage concerns the isolated bump, not its joint cancellation with all other terms.

## Preserved step-199 nomination

The following nomination is retained as the starting question. Its missing
source review is completed in the step-200 section below; its mathematical
obligations remain open.

The main gap remains actual-Xi all-degree mixed positivity. The intermediate
question is whether the accepted singularity of the positive-bump sampled
germ can be detected in the full finite response. A successful joint-germ
test could supply a genuine complete-response lower-growth input toward
the spatial Jensen-defect route. A pointwise lower rate would still leave
angular persistence, logarithmic-mean payment, amplitude/full charge,
H/support and Xi realization unresolved.

Keep the original L703 bump and b=sup supp chi, not omega+delta. Use the
L721 phase S and candidate edge point z_*=exp(-12*S(b)), with
R_*=|z_*|=exp(-12*Re S(b)). The natural sampled normalization is
n^(-1/2) at n=12q+3, exactly as in L721; no full root limit is assumed.
Do not assume the full-response generating series initially reaches
z_*: its convergence domain is itself part of the comparison.

L713 (4) proposes the exact decomposition

    G_n(u_*,-1)=P_n-R_n+[8+B_n+V_n-L_n^- -L_n^+ -T_n].

L714 gives R_n=P_n+K_n, so the nominated comparison must retain the
whole square bracket against the positive-bump term. This citation
specifies the future object only; step 199 neither accepts the unaudited
L713 full identity nor derives a new complete-response consequence.
In particular B_n here is the comb sum in L713, distinct from the bump
Laplace integral with the same letter in L714. The negative and high
frequencies in V_n, both endpoint tails and every finite moment remain.

Essential local inputs to check are L666/L703/L708 for the actual family,
L713's exact identity, L714's signed reduction and L721/L722 for the
accepted single-bump facts. The next literature step should search the
exact statement, standard terminology, stronger results and the specific
recorded complete-response stops before selecting a bounded proof target.
It must distinguish ordinary exponential subordination from a genuinely
different joint singular-support mechanism. Do not relabel the stopped
R_n/P_n comparison or the already accepted support-transfer completion
as a new creative mechanism.

Continuation test: approve mathematics only if the reviewed representation
makes a concrete joint-germ cancellation test possible with all corrections
retained. For example, a justified larger disk for a complete correction,
or separately identifiable singular pieces at z_*, would give an explicit
test; neither is assumed. A matching singularity capable of cancelling the
single-bump germ defeats naive inheritance and must be recorded. Persistent
source failure or an exhausted duplicate requires a different independently
testable target. The next review may reject this nomination without changing
the completed L722 audit. Full matching Mathlib coverage is not checked.

## Completed source comparison — 3 November 2026, step 200

### Local scope and duplicate/failure comparison

Read the hypotheses and relevant definitions of L666/L703/L708; L708
Sections 2–5 on the real-frequency prescription, complex-measure
representation and regularized Poisson passage; L713 through its full
identity (4); L714's exact finite reduction; and L721's hypotheses,
conclusion and Sections 4–5 on the sampled germ and its endpoint.
The step-199 L722 outcome is reused as supplied, not audited again.
This review compares claimed interfaces; it does not newly certify
L713's full identity or extend L708's estimates to u_*.

The observable is precisely the full finite polynomial of L708's
hypotheses, evaluated at u_* and -1, with all M=n/3 moments. The
profile e is fixed before n, real, summable with the stated Gevrey
weight, and |e_m|<=1/8. The low real-frequency identity is available
only for |v|<3*pi/4. It is not a complex-frequency continuation or
an identity on the whole real axis. In this review b always denotes
sup supp chi, not Im(u_*)=2/5. Also distinguish L713's comb B_n
from the unrelated entire bump integral B_n(a) of L714.

Keep the proposed L713 (4) exactly as written above. The comb includes
every integer sample; V_n includes v<0 and v>=9/4; the low-frequency
identity accounts for the remaining positive bump. The physical sums
have indices m<=-2q-1 and m>=2q. The finite-moment correction T_n
includes the anchor and every original atom. L713's fixed-n absolute
convergence and first-moment justifications do not provide uniform
summability in q for any generating series. Verifying its signs,
normalizations, endpoint indices and geometric-series correction is
an essential preliminary mathematical obligation of the covered test.

The scoped search/read also compared these preserved failures:

* `ATTEMPTS/2026-11-03-spatial-boundary-absolute-contour-stop.md`:
  L713's horizontal absolute envelope exceeds the small residue.
  This does not measure any signed correction germ.
* `ATTEMPTS/2026-11-03-signed-bump-common-phase-stop.md`:
  L717's unaudited phase-winding obstruction defeats a single rotation
  of the kernel; it neither proves nor excludes joint cancellation.
* `ATTEMPTS/2026-11-03-signed-bump-gamma-rice-size-stop.md`:
  L718's interpolation poles violate that Rice domain, and its
  removable size-interpolation pole is not a generating-variable pole.
* `ATTEMPTS/2026-11-03-actual-signed-remainder-subordination-stop.md`:
  audited L722 stops R_n/P_n subordination at unchanged data. Changing
  the horizontal contour height cannot change that signed observable.

L708 already proves complete-response cancellation near the different
center u=1/2, including both endpoints and all moments. Its proof's
positive-majorant concentration and small complex neighborhood are
part of its hypotheses/estimates; its conclusion cannot be moved to
u_* by citation. This is relevant positive evidence that retaining a
single term's size does not settle the complete response. The
step-161 cancellation-budget review concerns an angular absolute
envelope, not the present sampled joint germ. The step-187 size-series
and step-193 support reviews concern K_n. No checked local statement
already supplies the proposed full-response conclusion.

### Primary results, hypotheses and reading limits

**Cauchy jumps.** S. Tanveer, *Week 8 lectures*, undated author-hosted
[PDF](https://people.math.osu.edu/tanveer.1/m7651/week8.pdf), retrieved
2026-11-03: read Definition 1.3 and (1.5), Theorem 1.1, Lemmas
1.5–1.6, their proofs, and Remark 1.9, printed pp.2–5. For a
Holder-continuous density on a simple smooth compact oriented curve,
the Cauchy integral has the stated two boundary values at interior
points, with difference equal to the density. The proof subtracts
the local density value, uses Holder domination, and computes the
two constant-kernel limits. Endpoints are excluded. This supplies
an interior jump test once a representation is justified; it does
not identify our correction density or prove endpoint inheritance.
The endpoint still needs the same germ from zero and the slit-domain
identification, as in L721 Section 4. No reproof of Plemelj is needed.

**Comb and duality.** S. D. Miller, *Some notes on distributions*,
15 January 2006, [author-hosted PDF](https://sites.math.rutgers.edu/~sdmiller/musagei/distributions.pdf):
read Theorem 4.1 with its periodization/Fourier-series proof, p.7,
and Section 6, (6.1)–(6.2), p.9. Poisson is stated for Schwartz
functions; tempered duality makes the integer Dirac comb self-dual
in the 2*pi Fourier convention. The source does not directly give
an n-uniform theorem for our rational kernels. L708 Section 5
records a Gaussian regularization and fixed-n dominated passage.
A use at the changed center must check the new density estimates
and all normalizations, then separately pay any q-summation exchange.
These known tools do not erase the unshifted comb or its aliases.

**Analytic support tools, reused without new browsing.** Reuse the
precise statements, proofs/cases and applicability comparison in
`drafts/literature/2026-11-03-signed-bump-support-edge-transfer.md`,
Sections “Primary statements and proof cases actually read” and
“Applicability obligations, all still unpaid”:

* Hitrik–Sjostrand, *Two Minicourses on Analytic Microlocal Analysis*,
  [arXiv:1508.00649v1](https://arxiv.org/pdf/1508.00649v1), Theorems
  2.2.3 and 2.7.1, pp.35–36,54–55: inversion needs a classical
  analytic elliptic symbol with its factorial bounds and an actual
  operator realization. It is not a theorem for arbitrary samples.
* Deleporte, *The Szego kernel in analytic regularity and analytic
  Fourier Integral Operators*,
  [arXiv:2306.15382v1](https://arxiv.org/pdf/2306.15382v1),
  Propositions 4.23–4.24, pp.40–41: the elliptic inverse supplies
  reverse analytic regularity in the specified operator calculus;
  the general FIO statement is only a forward inclusion. Nonzero
  amplitude for one summand says nothing about the sum's symbol.
* Mazzucchelli–Salo–Tzou, *A general support theorem for analytic
  double fibration transforms*,
  [author-hosted 46-page version](https://users.jyu.fi/~salomi/pub/MazzucchelliSaloTzou2023.pdf),
  Theorems 1.2–1.3, pp.4–5; Theorem 5.1/proof, pp.27–28; Theorem
  6.1, p.42. Analytic geometry, nonzero weight, the stated dimensions,
  Bolker uniqueness/injectivity and one-sided support are essential.
  The localized proof excludes the remote term using uniqueness.
  No comparable exclusion has been proved for our full response.

The same assessment's Arendt–Batty–Hieber–Neubrander Theorem 2.8.3
comparison remains valid: its fixed real-coordinate Laplace transform
and Muentz samples do not cover n-dependent amplitudes on a complex
phase curve. Its unread Baeumer original remains an attributed lead,
not an imported premise. No access blocker to the present comparison
is inferred from that original.

Reuse also
`drafts/literature/2026-11-03-signed-bump-size-generating-function.md`,
Section “Boundary and transfer theorems”: Flajolet–Sedgewick's 2004
Theorem IV.3 and Flajolet–Odlyzko (1990), Theorem 1 and Corollaries
1–3, with the exact versions/pages and proof cases recorded there.
They require the radius or an appropriate continued germ and local
expansion; they do not locate a singularity of the unknown full
response. Positive chi is not positivity of its complex coefficients.
No asymptotic expansion or root limit is required merely to test a
nonremovable singularity. None of these known theorems is reproved.

### Bounded search record and limits

Web queries included:

* `"analytic wavefront" "cancellation" "Fourier integral operators" elliptic`
* `"generating function" "Poisson summation" "singularities" finite sums`
* `"Cauchy transform" "jump" "analytic" density cancellation singular support`
* `Tanveer Plemelj formula Holder arc proof math osu notes`
* `"Poisson summation" "finite measures" "Kallsen" Kruehner`
* `"generating function" "singularities" "finite lattice" "Poisson"`
* `"analytic wavefront" "sum" "cancellation" elliptic`
* `"Plemelj" "generating functions" singularity cancellation`
* `"generating function" "compactly supported" "Cauchy transform" cancellation`
* `"Poisson summation" "rational products" asymptotic`
* `"Fourier integral" "support theorem" "cancellation" Bolker`
* `"G_n" "finite-moment" "support-edge"`

The exact search did not locate this notebook's statement. The
general searches led to Cauchy/moment reconstruction, integral-geometry
and unrelated lattice examples. Search snippets and secondary pages
are discovery leads only. No theorem is imported from them. The
author-hosted Plemelj and Poisson texts above were actually read;
the analytic-operator/support sources reuse the ready assessments.
This is a bounded comparison, not a claim of exhaustive search or
originality. Full matching Mathlib coverage is not checked.

### Covered mathematical test, threshold and stopping condition

The covered continuation is one attempt on the exact original data.
Its proposed object is the germ formed directly from

    sum_(q>=1) (12q+3)^(-1/2)*G_(12q+3)(u_*,-1)*z^q.

This formula specifies a target, not an established analytic domain.
Keep L713's signed identity and all its terms as a single cancellation
problem. First verify that identity against the finite definition;
if it fails, preserve the discrepancy and do not use it as an input.
Then seek a common convergent germ or controlled analytic continuation
of the exact samples and determine the corrections' total local
contribution near z_*=exp(-12*S(b)). A representation assembled only
from formal size asymptotics is insufficient. Every interchange of
q, frequency integration and lattice/physical-tail summation needs
domination on the claimed common domain. Nearer singularities must
be addressed before asserting access to z_*; continuing unrelated
branches to its two sides does not identify the germ from zero.

The discriminating comparison is with L721's accepted endpoint germ,
not with the much smaller residue. A holomorphic correction through
the entire local slit neighborhood, justified for the germ from zero,
would make inheritance testable. If a correction has the same local
singular arc, retain its signed density/operator contribution and
test the total near the actual support edge. A single interior jump,
a leading coefficient at b (where a smooth bump may vanish), or a
vanishing first symbol coefficient does not decide this endpoint.
Any analytic-elliptic argument must concern the combined operator;
all later orders and exact exponential errors must be controlled.

Continue if an exact common representation with a noncancelling
terminal support contribution, or a justified holomorphic correction,
is obtained. A genuine inherited singularity would support the useful
threshold limsup log|G_n(u_*,-1)|/n>=Re S(b), subject to the actual
domain/branch argument; it would not assert a full rate limit or signs.
If a matching correcting singularity remains unresolved, abandon
naive inheritance and record precisely which term carries it. If
the entire edge cancels, stop this particular edge-transfer test.
If only old absolute envelopes, finite-order formal expansions or a
new noncancellation assumption are obtained, save the partial reasoning
and report the failure; do not repeat unchanged subordination.

This is a materially different joint-cancellation question, not a
new version of the already completed single-bump support theorem.
Even success would provide only pointwise subsequential growth.
Angular persistence and logarithmic-mean payment, the complementary
spatial Jensen defect, amplitude/full charge, H/support, Xi realization
and actual-Xi all-degree positivity remain independent open steps.
No new lemma, calculation, corrected identity or full-response result
is established by this literature-only review. The newly covered
creative attempt awaits the separate continuation approval.
