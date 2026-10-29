# Complete low heat response: critical-audit coverage

TARGET: Critically audit L301's complete low one-heat-line o(1) bound at r_N, including relative-grid trace control, mixed-source allocations and every low-contour residue.
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 549 reused the moving-cluster and first-source audit assessments, read L301 in full and L297 section 4, and checked ATTEMPTS/047--050; added bounded discrete-trace, signed-energy-form and row-sum searches recorded below. No inspected theorem supplies the complete relative Wilson bound; no novelty inference.
SOURCE_EVIDENCE: Reopened Texier Propositions 1.1/2.1 and proof, pp. 250,252--253, https://ems.press/content/serial-article-files/44369?nt=1 ; Schweitzer 2203.03930v1 section 2.1 Lemma 1/Theorem 2 and proofs, PDF pp. 2--3, https://arxiv.org/pdf/2203.03930v1 ; BBS 1907.05474v2 Propositions 2.1.6/2.1.9 and Corollary 2.1.11, printed pp. 31--33, https://arxiv.org/pdf/1907.05474v2 ; Watrous 2018 draft section 1.1, pp. 32--33, (1.165)--(1.175), https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf . Additional trace comparison below is not an imported input.
COMPARISON: Standard sources cover finite Gaussian contractions, total projectors, ordered resolvent derivatives and Schatten duality. They do not prove L301's staggered extension, signed full-H form bound or mixed-source localization; these are explicit local audit obligations. No additional essential general theorem is required by the written direct argument.
GAP: Audit the complete proof under the exact cube and source hypotheses, especially staggered extension energies, weighted traces on all strata, anchor translations, both mixed inverse orders and all source allocations, external curls and weighted trace pairing.
REASON: Separate literature-only proof-to-source comparison is complete; coverage permits exactly the saved conceptual audit, without accepting L301's estimates or deriving any mathematics this turn.
LITERATURE_REASON: The new audit target adds full-H relative-grid trace and mixed-source estimates beyond the prior moving-cluster assessment; check their source scope once, then return to mathematics.
SCOPE: L301 with direct inputs L003 L282 L287 L297 L298 L300 and their upstream premises, including L279 L280 L283 L289 L299; exact SU(2), even N, a=8/N, counting measure, fixed unweighted H and Q, both exact reflected 12-bumps, ambient own-slice jets, full density, boundary-fixed gauges and every variable normal endpoint.

The canonical result is
[L301](../../lemmas/L301-complete-low-heat-response-energy-form-bound.md).
The completed research assessment remains unchanged at
[moving-low-cluster-response-test.md](2026-10-29-moving-low-cluster-response-test.md).
At creation this file was REVIEW_REQUIRED and authorized no dependent
mathematics. The separate step-549 comparison below now approves the
saved audit target for a later research turn.

The requested review concerns the full four-term scalar, not only a
fixed-ground compression. Its claimed upper bound is
O_f(N^-1/2 log(eN)^(5/2)). The new mechanism is a small form norm on
all of fixed H; it avoids asserting a source-uniform moving-projector
bound. Check L301's exact finite-grid reflection and slice-trace
calculation, the use of complete signed direction rows, the mixed
kernel convolutions and every labeled tensor placement. The existing
low-contour estimates must still retain their off-ground residues,
source signs and external color factor three.

The standard tool hypotheses and source qualifications from the prior
review persist: Texier treats total projectors including splitting;
Schweitzer's resolvent lemma is applicable, while the full-spectrum
theorem is not itself a low-contour theorem. No unproved complex-source
compression, changed slice, differentiated nonconstant-rho identity,
or scalar replacement for the transverse covariance may be inserted.
Full matching Mathlib coverage remains not checked.

Accept only if all estimates and their endpoint/source accounting
justify the displayed rate under the stated inputs. A local repair
must retain the full scalar and its o(1) threshold; otherwise preserve
the exact failed bound as unfinished or negative evidence. Acceptance
would remove only this low-response bottleneck. High contour, full
tail, uncut estimates, uniform higher remainder and the interacting
continuum/mass construction remain separate gaps.

After separate coverage approval, this is a conceptual proof audit,
appropriately deep_research/xhigh. It is not a complete-solution
candidate audit and is not a routine arithmetic replay.

## Separate coverage approval: step 549, 2026-10-29

Read all seven proof sections of L301 to distinguish cited tools from
claims requiring audit. Reused the completed moving-cluster review and
the first-source compression critical-audit assessment. L297 section 4
already contains the weighted low residues and product rule; L301's
new claim is their pairing with a small form bound on all fixed H.
Neither the old fixed-ground compression nor projector regularity is
a duplicate proof of that claim. Histories 548 and ATTEMPTS/047--050
retain the unfinished work and distinct stopped mechanisms. In
particular the bare all-heat obstruction is not a counterexample to
this complementary one-heat low scalar.

Reopened the primary sources listed in SOURCE_EVIDENCE. Texier's
Proposition 2.1 and its proof include changing numbers of distinct
eigenvalues and nilpotent terms. Its isolating-curve hypothesis fits
the fixed finite H and affine matrix family, conditional on L297's
stated isolation. No N-uniform estimate follows from that proposition;
Corollary 2.2's constant-multiplicity restriction is not imposed on
individual branches here. Schweitzer's Lemma 1 supplies every ordered
resolvent product for points off the spectrum. Its Theorem 2 requires
the full spectrum inside the contour and cannot directly supply a
low-only estimate. The previously recorded sign typo in intermediate
equation (4) persists; retain the stated lemma and L297's source
convention. The local contour and quantitative weighted residues
remain local inputs to be checked, not consequences of this citation.

Bauerschmidt--Brydges--Slade's polynomial Gaussian formula, Laplace
transform characterization and independent-sum corollary cover finite
positive semidefinite covariances, including restriction to their
support. This fits the fixed transverse Gaussian. Signed derivative
slots must be multilinear contractions, not asserted positive Gaussian
laws. Their use supplies no Wilson-specific bound. Watrous's Schatten
duality (1.173)--(1.174) and ideal property (1.175) apply to arbitrary
finite complex operators; positivity and commutation are unnecessary.
The later audit must check the actual half-power placement and weights.
These standard inputs should be cited, not reproved.

New bounded queries were `"discrete" "trace inequality" lattice
boundary energy reflection`, `"Wilson" "signed" "energy form"
"heat" covariance`, and `"lattice" "row sums" "quadratic form"
boundary Green function`. No matching complete Wilson theorem was
identified. A relevant primary comparison was inspected at its
publisher: Badia--Droniou--Tushar, *A Discrete Trace Theory for
Non-Conforming Polytopal Hybrid Discretisation Methods*, Foundations
of Computational Mathematics 26 (2026), 2667--2716, published online
3 December 2025, [DOI 10.1007/s10208-025-09734-6](https://link.springer.com/article/10.1007/s10208-025-09734-6),
section 2, Assumption 2.1, definitions (2.1)--(2.3), Theorems 2.2/2.3
and Remark 2.4. These concern cell/face polynomial hybrid spaces on
regular quasi-uniform polytopal meshes, with a boundary H^(1/2)
seminorm and a lifting. They are not the counting-measure staggered
edge extension or weighted slice estimate in L301(9)--(12). No
identification of spaces or energies is supplied or assumed. This
comparison is not an imported theorem; its full proof was not read
and is not needed for the direct audit. Other search hits about
finite-element polynomial inverse traces were left as unread leads.

The direct finite-grid calculation is justified as a specialization
fixing the exact midpoint/vertex conventions and both normal endpoints,
not as a reproof of a general trace theory. Its correctness is still
pending. Likewise the signed-row conversion, logarithmic convolutions,
disjoint-support gain and labeled Wilson allocations require direct
checking. Do not import a continuum trace inequality, periodic gradient
covariance theorem, scalar covariance, or nonconstant-rho cancellation
to bypass those obligations. No new lemma, rate or repair was derived.

Coverage is adequate for the exact TARGET with DECISION EXPLORE.
Accept the later audit only if all four complete terms reach the
claimed O_f(N^-1/2 log(eN)^(5/2)) rate under the stated inputs; otherwise
preserve the precise invalid estimate or uncontrolled residual. A bad
absolute bound alone is not a counterexample. Acceptance would remove
only the low-response bottleneck. High-contour/full-tail control,
uncut estimates, higher remainder and interacting continuum/positive
mass construction remain unresolved. Full matching Mathlib coverage
remains not checked. This is source-scope progress only, not mathematical
validation or evidence of originality.
