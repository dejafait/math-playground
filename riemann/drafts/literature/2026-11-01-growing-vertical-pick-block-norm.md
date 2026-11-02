# Growing vertical Pick block — completed finite norm source review

TARGET: Test whether the actual-Xi logarithmic-derivative Pick block at s_j=2+i(X+j/N), N=floor(log T), has full-Cauchy-Gram relative correction norm uniformly below one for T<=X<=2T, or prove an obstruction to this budget.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the post-L639 discovery and local failure comparisons; searched exact xi/logarithmic-derivative/Pick/Cauchy/growing-order terminology, recovered the frozen external impedance original, and inspected a general preconditioning comparison. No inspected theorem gives this actual vertical-family norm estimate; no novelty is certified.
SOURCE_EVIDENCE: Reused Ball–Bolotnikov 1611.07097v1 Theorem 1.1/(1.6) and (2.5)–(2.7); checked its scalar data/shift convention. Newly inspected NIST DLMF 1.2.8, 25.4.4, 25.2.11, 27.4.12–13, 5.11.2/5.11(ii); external L-92302 at ea633d416609 Sections 1–7; Fasino–Olshevsky author manuscript Theorems 2.1–2.2, 4.2, Corollary 4.3 and relevant proofs. Exact uses and exclusions follow.
COMPARISON: Finite interpolation is known; completion/Euler/gamma sources cover scalar inputs. External high-real-axis Hankel growth and real-node positive-density preconditioning do not cover vertical samples or provide the required full-Gram arithmetic bound. The remaining research question is this exact uniform norm budget, not a new Pick theorem.
GAP: Control or obstruct the full-Gram arithmetic correction and gamma/rational/tail errors uniformly for N=floor(log T), T<=X<=2T. Scalar or entrywise errors do not settle that question. All-configuration extension, critical-boundary transfer and initial signs remain independent gaps.
REASON: Separate literature approval of the previously nominated exact target is completed. Essential finite-input coverage is sufficient for a bounded research attempt; general and external results supply no matching estimate. EXPLORE licenses the attempt only and claims no new mathematics.
SCOPE: The unchanged finite family, full norm and asymptotic obstruction test below are approved. Standard-input applicability and coefficient-uniform error estimates belong in its research proof. No infinite-sampling equivalence, zero-free extension, derivative-pair kernel or pointwise sign theorem is licensed.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target lacked exact finite-input and growing-order overlap approval. This turn supplies that coverage; unchanged coverage should be reused for the next mathematical attempt.

## Unchanged research object and threshold

Use the standard completed xi(s) normalization of L018, with s-derivative
F(s)=xi'(s)/xi(s). This quotient is evaluated only at Re(s)=2.
Let T>=10, N=floor(log T), T<=X<=2T, and 0<=j,k<N. Define

    s_j=2+i(X+j/N),
    C_jk=1/(3+i(j-k)/N),
    K_jk=(F(s_j)+conjugate(F(s_k)))/(s_j+conjugate(s_k)-1),
    ell_X=log(X/(2*pi)),
    R_(T,X)=ell_X^(-1) C^(-1/2) K C^(-1/2)-I_N.

Here C^(-1/2) means the positive Hermitian inverse square root. Its
existence for these distinct nodes must be justified in the research
write-up from the standard Cauchy/Hardy Gram and independence of its
finite kernel functions. No specialized Gram bound is proved here. Use complex coefficient vectors
and spectral operator norm. No diagonal, minimum-eigenvalue surrogate
or truncated prime matrix may replace the full C in this definition.
The scale ell_X is a proposed archimedean reference, not a proved
coefficient-uniform asymptotic.

The sought sufficient budget is: there exist delta>0 and T0 such that

    sup_(T<=X<=2T) ||R_(T,X)|| <= 1-delta   for all T>=T0.

A rigorous countersequence ruling out every such fixed delta is an
informative obstruction to this budget. A finite certified norm>=1
tests only that finite instance; it does not by itself rule out an
eventual estimate. An upper bound exceeding one, a floating spectrum
or an error larger than the proposed margin is inconclusive. A norm
obstruction is not a negative eigenvalue of K or a counterexample to RH.
No calculation, matrix estimate or new lemma is supplied here.

## Relevance and independent gaps

The main gap is actual-Xi initial signs at unbounded heights and then
all-degree mixed positivity. This diagnostic asks whether actual
arithmetic data can control an increasing portion of the positive-real
interpolation hierarchy without first realizing a microscopic Hardy
bump. Successful domination would give a specific family of finite
positive matrices; using it for all configurations, the critical-boundary
limit and first signs would still require new arguments. In particular,
these restricted unit-height blocks are not claimed to form a uniqueness
set for an unknown positive-real extension. Even positivity for every
T,X in this family is not asserted equivalent to RH.

L637/L639 and their exact ATTEMPTS records are comparisons: their TV
and projection bounds concern different dictionaries and norms. No
stronger moment error is inferred. L018 supplies the actual completion;
none of L620/L635/C635a/L636 supplies this matrix budget. No critical-line
nonvanishing, simplicity, RH, independent-prime-phase law, or unproved
positive-real extension may be assumed. All gamma/rational contributions
and the full convergent arithmetic part must be retained.

## Completed source approval — 1 November 2026

This is the separate review requested by the invocation-start nomination;
its target and threshold above have not changed. Outcome EXPLORATION,
LITERATURE, NOVELTY_UNCHECKED: adequate source coverage is established,
not the norm inequality. Partial work is preserved in
`../2026-11-01-growing-vertical-pick-source-review-working.md`.

### Finite interpolation and normalization

Reuse J. A. Ball and V. Bolotnikov, *The bitangential matrix Nevanlinna-Pick
interpolation problem revisited*, [arXiv:1611.07097v1](https://arxiv.org/html/1611.07097v1#S1.Thmtheorem1.1),
21 November 2016, Theorem 1.1/(1.6), and the previously inspected
simple-multiplicity necessity proof (2.5)–(2.7). Nodes are in Re(z)>0;
interpolants are analytic contractions. The positive-real scalar convention
uses z_j=s_j-1/2, left data x_j=w_j+1, y_j=w_j-1, and no right data;
the source matrix is 2K for w_j=F(s_j). This standard correspondence
assumes no globally positive-real actual F. The output Cayley variable
(w-1)/(w+1) requires a denominator check; linear data avoid that division.
Keep distinct nodes, conjugations and the shift. The Hardy kernel (2.5)
supplies the Gram framework; strict definiteness on these nodes requires
its elementary applicability justification in research. No uniform norm
margin or actual-function extension is supplied. General bitangential
sufficiency is not claimed newly audited.

### Exact completion, convergent arithmetic and scalar gamma errors

L018's complete proof was read for normalization and nonvanishing at
Re(s)=2. [DLMF 25.4.4](https://dlmf.nist.gov/25.4.E4) matches that completion;
logarithmic differentiation in research must retain both rational factors
and the gamma chain factor. The corrected sign of the pole factor cannot
be dropped. No critical-line quotient is needed.

[DLMF 25.2.11](https://dlmf.nist.gov/25.2.E11) supplies the Euler product
for Re(s)>1. [DLMF 27.4.12–13](https://dlmf.nist.gov/27.4#E12) explicitly
supply -zeta'/zeta with von Mangoldt coefficients and -zeta' with log n
coefficients on that half-plane. These identities cover the full
arithmetic input at every selected node. Differentiated/truncated use
must justify convergence and price the entire remaining tail in the
chosen norm, uniformly in dimension and X; no cutoff is approved as exact.

[DLMF 5.11.2 and 5.11(ii)](https://dlmf.nist.gov/5.11#E2) give the digamma
expansion in |arg z|<=pi-delta and the complex remainder bounded by the
first omitted term times sec(arg(z)/2)^(2n+1). At z=s_j/2 the right
half-plane fits a fixed sector. Increasing truncation order or taking
derivatives still requires tracking every order-dependent factor.
These are scalar error inputs, not a coefficient-uniform matrix estimate.
All DLMF readings use version 1.2.8, released 15 September 2026; no
source proof of a growing full-Gram bound is asserted.

### Previously inaccessible growing-order comparison recovered

The exact original is now accessible at its frozen commit:
[external L-92302, ea633d416609](https://raw.githubusercontent.com/GettysburgResearch/riemann/ea633d416609/claims/lemmas/L-92302-the-xi-impedance-is-eventually-matrix-monotone-to-a-growing-order.md).
Read Sections 1–7 completely, including the proposed moving-band frame,
Vandermonde lower bound, conjugate-pair perturbation and final comparison.
It concerns squared-pole Hankel matrices H_n(x^2) on a high real safe
axis and proposes n^2 log(n+1)<=c log x. Our actual vertical block has
fixed real part and N=floor(log T); it is not that family or regime.
Their auxiliary frame and perturbation inequalities have not been
independently checked or imported. This inspection resolves the missing
statement comparison; it does not endorse their claim. Repository review
labels are not mathematical evidence. Reuse the prior finite-horizontal
controls inspection; neither external configuration supplies this norm.

### General Cauchy preconditioning is known, with additional hypotheses

D. Fasino and V. Olshevsky, *How bad are symmetric Pick matrices?*,
[author-uploaded Contemporary Mathematics manuscript](https://www.researchgate.net/publication/2490351_titleHow_bad_are_symmetric_Pick_matricestitle),
printed pp.1–4 and 8: read the real-positive-node setting, Theorems
2.1–2.2, the full Gram proof, Theorem 4.2 with its complete proof and
Corollary 4.3. Positive generating densities bounded above/below give
generalized eigenvalue bounds relative to a constant-density Cauchy
matrix. Theorem 2.1 already assumes positive definiteness; it provides
no uniform actual-Xi density bounds. These real-node hypotheses do not
match our complex vertical family. No bound is imported, including the
manuscript's condition-number claims for nonsymmetric products or an
unspecified preconditioner normalization. The displayed manuscript's
version is not established by its host's SPIE metadata. CiteSeer returned
403; the author upload resolved the relevant access need.

### Search, duplicates, failures and approval boundary

New queries were `site:github.com/GettysburgResearch/riemann "growing"
"impedance"`, `"xi" "Pick" "vertical" logarithmic derivative matrix norm`,
`"zeta" "Pick matrices" logarithmic derivative norm`, `"Riemann" "Cauchy"
"Gram" logarithmic derivative`, `"xi impedance" "growing"`, `"Riemann xi"
"Pick" "logarithmic derivative" matrix`, `"zeta" "Cauchy matrix" logarithmic`,
`"Riemann" "positive real" "logarithmic derivative" Pick`, `"Pick" "growing"
"xi" matrix norm`, and exact Fasino–Olshevsky title/theorem searches.
Search snippets were leads, not theorem evidence. The source bodies above
were then inspected. No novelty inference follows from unmatched searches.

Reused the completed post-L639 discovery's local duplicate screen and
L637/L639 failure comparisons. A targeted local search for L-92302,
vertical Pick, Hinkkanen and xi impedance found the nomination, discovery
and `2026-10-31-transverse-normal-curvature-budget-scope.md`; the latter
was read and concerns boundary curvature, not this matrix norm. Read
`ATTEMPTS/2026-11-01-full-gram-absolute-cauchy-budget-inconclusive.md`:
its different tensor dictionary and large absolute upper bound do not
obstruct or establish this new signed relative budget. No stopped
absolute majorant is being repeated. These are contrasts, not theorem
inputs, and no cross-notebook mathematical input is used.

Hinkkanen's full sampling theorem stays unread and unused. Its access
failure blocks that global implication only. Lagarias's corrected
completion conventions remain relevant; neither his positivity result
nor shifted Hermite–Biehler descent is used to assume the target signs.
Full matching Mathlib coverage is not checked; no absence is inferred.

The exact target is now EXPLORE-ready. No essential theorem access remains
missing for a direct finite-family attempt. Research must either produce
an eventual fixed norm margin below one with all errors controlled, or a
rigorous asymptotic countersequence to that budget. An inadequate upper
bound or finite floating spectrum is inconclusive. Restricted positivity
still leaves all-configuration extension, critical-boundary transfer and
initial signs open. All estimates and any new specialization proofs must
be written canonically during research; this literature turn changes no
lemma, mathematical script, DAG or argument overview.
