# Fixed-coefficient density propagation with the actual kernel bound

TARGET: Recompute L944's value and derivative error allowances using L945 and the unchanged L938 degree256 coefficients, and test whether the endpoint E=4 remains obstructed.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step72 reused step68's direct-density discovery and primary-source comparison and step49's analytic/beta/integer audit coverage; searched the specific L938 direct/ratio/Schur stop records and L944/L945 histories. Supplementary queries were difference-of-products telescoping error bound and Conrad differentiation under the integral sign Theorem12.3; no inspected theorem supplies the actual density signs.
SOURCE_EVIDENCE: Read full L944/L945, L938(6)-(9),(15)-(18) and complete step50 audit account; read the entire step69 endpoint producer without executing it. Reuse inspected DLMF18.9.21,18.14.4,5.12.1 and step68's versioned FLINT v3.3.1 inclusion contract. Additionally inspected Keith Conrad, Differentiating under the Integral Sign, author PDF https://kconrad.math.uconn.edu/blurbs/analysis/diffunderint.pdf, Theorem12.3 and warning example12.2, printed pp14-16, retrieved 2026-11-09; its one-dimensional continuity hypotheses do not directly cover singular simplex faces.
COMPARISON: Existing finite-product telescoping, analytic Chebyshev derivative control, integrable beta weights and exact finite-polynomial evaluation cover the methods. L945 bounds k, not the saved p; a common factor bound must separately pay the full epsilon. L944's coarse stop explicitly permits sharper majorants and therefore does not preclude this fixed-data test. No stronger actual-sign result was found in the inspected sources; no novelty claim follows.
GAP: Application proof and exact endpoint comparisons remain undone. Establish a common bound for both k and p, retain L944's independently obtained derivative allowance and all coefficient errors, then recompute product radii and compare with the unchanged exact endpoint centers. The actual crossing signs, compact coverage and independent endpoint/contact conditions remain open.
REASON: Changed-hypothesis comparison is complete for one bounded REPRODUCTION calculation; it needs specialization of already covered methods, not another general theorem search or a kernel reproof. This approves method scope, not L944's correctness or a successful sharper certificate.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED because the kernel-only assessment excluded propagation; this turn resolves that specific scope gap without repeating its theta literature search.
SCOPE: Exactly TARGET; retain degree256, 257 nodes, theta cutoff8, precision200, coefficient grid10^-120, all 34 rows, twelve factors, factorials and M_0^12. One E=4 endpoint test only; no cell subdivision, new polynomial, degree/precision/cutoff sweep or independent parameter-sign inference. Use a common majorant that pays polynomial error, for example the conservative candidate 2+epsilon after its application justification, rather than silently replacing every 8 by 2. Full/supporting Mathlib coverage remains unchecked.

## Step72 completed comparison

This is literature-only source/hypothesis comparison. No sharper
allowance, ratio, derivative sign or crossing result is derived here.
The paragraphs below headed original nomination preserve the earlier
uncovered status as history, rather than current instructions.

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target is the fixed-data endpoint preflight in TARGET.
Its plausible use is to decide whether reducing the common factor bound
can make simultaneous v/v' enclosures useful for a later compact upward
crossing test. No complete route through the independent gaps is asserted.

### Coverage and applicability obligations

1. Reuse the primary-source coverage in
   [step68 source notes](2026-11-09-l938-direct-density-source-notes-68.md)
   and [step49 assessment](2026-11-09-l938-energy-certificate-audit-48.md).
   DLMF18.9.21 and18.14.4 support L944's derivative-series method on
   the real interval, with the affine scale and root-grid aliases
   retained. L945 changes neither analytic ellipse nor coefficients.
   Recomputing derivative tails or differentiating (15)'s real error
   inequality is unnecessary and is not authorized as a replacement.
2. The common-bound hypothesis in L944's product proof concerns every
   factor of both products. L945 supplies only the actual-kernel side.
   The later calculation must justify its chosen common majorant from
   L938(15), including all eta_l; positivity or the upper bound for the
   actual kernel must not be asserted for p without that argument.
   Finite-product telescoping and the product rule are elementary
   standard identities already explicit in L944, not new theorems to
   reprove. Only their changed-hypothesis constants require work.
3. DLMF5.12.1 applies to positive beta parameters. L938(9) records
   k_i+1/2>0, a fixed simplex and integrable row weights. L944 supplies
   bounded k,k',p,p' and uniform row domination on the compact domain.
   Reuse that dominated-differentiation argument (Lebesgue dominated
   convergence and the mean value theorem); retain the E^17 prefactor
   derivative and sum t_i=1 accounting. Smaller upper bounds do not
   change the domain, weight exponents or needed differentiability.
   Conrad's Theorem12.3 confirms the need for parameter-independent
   integrable majorants, but its displayed one-dimensional theorem
   is supporting comparison only, not a direct simplex citation.
   Its example12.2 explicitly warns against an unjustified interchange.
4. The endpoint centers are finite rational polynomial sums, L944(4)
   from L938(18). They can be reused with unchanged inputs and exact
   arithmetic; no new quadrature, pi approximation or theta evaluation
   is needed. The read step69 producer checks all257 coefficient radii,
   all34 absolute beta weights, fixed budgets, all5101 prior audit
   flags, input hashes and the prior exact coefficient-identity residual.
   A later calculation must retain these checks and inspect complete
   load-bearing evidence; this turn did not load or verify the large
   certificate values and did not run any mathematical script.
   The L037 Decimal/exponential and integer-execution trust remains.

The reused primary source identifiers are DLMF equations cited above,
the versioned FLINT v3.3.1 arb_calc.rst root-finding contract and complete
isolate_roots.c implementation cited in step68. Their interval methods
require genuine enclosures and preserve unknown regions; they supply
no sign margin. No extra source is essential for this fixed-data change.
The web telescoping query returned a generic exposition that was not
imported; Conrad was actually read at the author URL. No inaccessible
lead is being treated as evidence or a blocker.

### Duplicate/failure comparison and bounded decision

Read the step69 coarse-endpoint stop and its history, L944's explicit
qualification about sharper bounds, and step71's L945 assembly history.
The ratio-order and Schur-concavity stop records for L938 concern other
mechanisms. Step68 already compares the signed cell masses with
pointwise/derivative coverage. No recorded result in these specific
paths tests the present smaller common factor bound. This is local
duplicate screening, not certification of originality or a global search.

Continue this implementation only if exact symmetric endpoint inclusion
excludes zero for v, or has a strictly positive lower bound for v'. If
both tests fail, preserve a stop for these allowances with the actual
versus required margins; subdivision with the same global radii cannot
repair the endpoint. Negative derivative-center sign alone does not
refute upward crossing when v is nonzero there. Passing only this
preflight authorizes no compact-cover claim. No new subdivision or
parameter sweep belongs to this target.

The finite-density crossing mechanism remains conditional on full
compact coverage, other energies, contacts and parameter endpoint signs;
all-degree Xi positivity, realization and continuation remain independent.
No cross-notebook theorem is used. The kernel/propagation work does not
supply a justified new creative central mechanism; an invented creative
label would not resolve these gaps. Next is the exact saved calculation,
subject to the supervisor's separate next-invocation gate, not more
unchanged literature browsing.

## Original step71 nomination (historical)

Main gap remains L030-L032/C032a actual-Xi all-degree mixed positivity.
Inputs are L938's unchanged polynomial, complete coefficient errors and
directed arithmetic contracts, L944's derivative inclusion and exact
endpoint sums, and L945. No new degree, cutoff or precision is proposed.
Retain L944's coarse obstruction as historical evidence. A discriminating
test is whether the sharper symmetric value interval at E=4 excludes
zero or the derivative interval has the needed positive sign. A failure
parks this specific allowance, not the density mechanism or RH.
Passing an endpoint test alone supplies neither compact coverage nor
contacts, other energies or independent parameter endpoint signs.

Review must check local duplicates and recorded failures for this exact
changed bound and decide whether the existing methods suffice. No new
error formula, rational comparison or crossing assertion is derived here.
Mathlib coverage is unchecked. No cross-notebook theorem is requested.
