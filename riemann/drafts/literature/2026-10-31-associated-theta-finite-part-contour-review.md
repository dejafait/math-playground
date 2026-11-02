# Finite-part contour source assessment — extension parked

TARGET: Assess primary finite-part boundary-contour criteria for nonnegativity of the Fourier transform of L596's exact A, requiring compatibility with its radial growth and an explicit sign hypothesis; park this extension if no applicable criterion is found.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded finite-part/Fourier-sign, higher-order Plemelj and distributional-Cauchy searches listed below; reused the exact-theta and Tuck comparisons, read Galapon v3 and Norvidas 2015 primary theorem statements and essential proof cases. No inspected theorem supplies the requested sign-controlled boundary formula for this A; no novelty or nonexistence conclusion follows.
SOURCE_EVIDENCE: Galapon, arXiv:1512.01323v3, Sections 2–4, Definition 1, Lemma 1, Proposition 2 and Theorem 1, https://arxiv.org/html/1512.01323v3 ; Norvidas, Nonlinear Anal. Model. Control 20(2) (2015), 210–225, Theorems 1–2, Lemmas 3–4 and Theorem 2 necessity/sufficiency, https://doi.org/10.15388/NA.2015.2.4 ; reuse Tuck (2006), pp.135–137 (5)–(13), DOI 10.1017/S0004972700047511, from the completed exact-theta assessment.
COMPARISON: Finite-part contour averaging handles a prescribed isolated integer-order pole with analytic numerator; it gives no Fourier sign. Distributional Cauchy criteria require explicit complete monotonicity of auxiliary transforms, not merely boundary existence or radial growth. Neither identifies A at the boundary or proves its sign-bearing hypothesis.
GAP: Exact boundary distribution, subtraction data, all other singularities, large-real-part bounds and a separately verifiable sign condition remain missing. L596 gives only radial lower growth. No applicable finite-part positivity theorem was found in this bounded review; mathematical impossibility is not asserted.
REASON: The source comparison changes the route: park the finite-part extension instead of inferring positivity from regularization. Retain the independently defined real-axis Cauchy-transform lead only as a separate finite-derivative source-review nomination, not a theorem application or another boundary-size audit.
LITERATURE_REASON: Changed hypothesis: replace the rejected ordinary low-order radial model by a finite-part or explicitly subtracted boundary-contour formula compatible with the lower bound C delta^(-9/2); essential theorem and sign-condition coverage is missing.
SCOPE: Completed literature comparison for the exact A only. EXPLORE records the bounded search, not permission to derive a boundary theorem. No lemma, mathematical script, subtraction formula, new sign or RH claim was produced.

## Invocation-start comparison scope (preserved)

Use A(z)=integral_R s^2 k(s+z)k(s-z) ds on |Im z|<pi/4,
with exactly the L019/L239 theta normalization audited in L596. Do not
replace it by the auxiliary theta function also named A in those inputs.
Use L233 only to check the downstream first-level Fourier normalization;
it is not a premise establishing a contour theorem or a sign.

Search for primary finite-part/Hadamard-subtraction contour positivity
criteria, including stronger-singularity extensions of the Tuck setting.
Inspect theorem hypotheses and relevant proof cases before broader
extracts. Distinguish a boundary-value representation from a positivity
criterion. Record subtraction contributions, frequency range, growth
upper bounds, other singularities and all sign assumptions explicitly.
L596 provides only a radial lower bound, not any needed upper bound or
boundary regularity. Do not infer a pole order or a finite subtraction
order from its exponent.

Continue only if an inspected theorem or precisely specified mechanism
produces an explicit sign condition that can be tested independently of
the desired Fourier nonnegativity and is compatible with L596. Nominate
that condition for separate coverage/approval before mathematics.
Otherwise park this extension with the exact scope obstruction; do not
repeat the ordinary simple-pole search or extend the old stop globally.
No first-level or higher-degree Xi sign has been proved. A creative
central-gap attempt is not yet justified because its boundary object
and sign-bearing condition have not been identified. Full matching
Mathlib coverage is not checked.

## Completed review — 31 October 2026

The main gap is actual-Xi all-degree positivity at unbounded heights.
The intermediate target was a sign-controlled finite-part boundary
formula for A. Its plausible use was the first-level identity in L233,
Ahat(2x)=Xi'(x)^2-Xi(x)Xi''(x); higher degrees remain separate.
The continuation test required an explicit independent sign condition
compatible with L596. No inspected theorem passes that application test.
This is source-scope evidence against the proposed application, not a
proof that every finite-part approach fails.

### Exact input and duplicate screen

Read the full canonical L596 including its audit and L233's complete
Fourier proof. Reused the two supplied predecessor assessments and the
low-order radial-model stop. L596 identifies A on the open strip and
proves only A(i(pi/4-delta))>=C delta^(-9/2). It does not establish a
pole, an upper bound or a horizontal trace. L233 fixes the full-line
normalization; no new Fourier calculation is made here.

A targeted Cauchy/complete-monotonicity search found the September 23
normalized-theta and scalar-bridge stops. Those concern L232's
x-normalization and L247's squared-axis logarithmic derivative, not a
Cauchy transform of the associated A. L253's first-sign masking stop
also warns that a first-level sign would leave the all-degree gap.
These distinctions are comparisons, not proofs of a new implication.
A possible return to C464c was rejected as a duplicate after reading
its dated 26 October audit history; no audit is repeated or changed.

### Primary finite-part theorem: representation, without a sign

E. A. Galapon, *The Cauchy Principal Value and the Hadamard finite part
integral as values of absolutely convergent integrals*,
[arXiv:1512.01323v3](https://arxiv.org/html/1512.01323v3),
1 May 2016, Sections 2–4: Definition 1, Lemma 1 (8)–(10),
Proposition 2 (18)–(22), Theorem 1, and (25)–(28) were read.

Hypotheses: finite a<x0<b, integer n>=0, analytic numerator f on a
neighborhood of [a,b], and detours excluding other singularities in the
chosen deformation region. The prescribed singularity is
f(z)/(z-x0)^(n+1). The finite part equals the two-detour average;
one detour instead retains the signed correction
+-i*pi*f^(n)(x0)/n!. For n>=1, (18) subtracts Taylor terms of orders
k<n with coefficients
f^(k)(x0)(1-(-1)^(n-k))/(k!(n-k)*epsilon^(n-k)).
The proof expands through n and bounds the remaining small arc by
O(epsilon); its residue correction is retained before cancellation.
No Fourier-frequency range or positivity conclusion is asserted.

For A, no such isolated-pole factorization, Taylor jet, deformation
region or infinite-endpoint control is supplied. Inserting a Fourier
exponential would require these data and all resulting corrections
at each frequency. A radial lower exponent cannot choose n.
No specialization or reproof of this theorem is attempted.

### Primary distributional sign criterion: an extra hierarchy

S. Norvidas, *Distributional boundary values of analytic functions and
positive definite distributions*, Nonlinear Anal. Model. Control
20(2) (2015), 210–225,
[DOI 10.15388/NA.2015.2.4](https://doi.org/10.15388/NA.2015.2.4),
Theorems 1–2, definitions (5)–(14), Lemmas 3–4, and both directions
of Theorem 2 (pp.219–224) were read.

Theorem 2 assumes f in D'_L2 and finitely many regular cones whose
duals cover R^n exactly (overlaps have measure zero). It characterizes
positive definiteness by complete monotonicity of every corresponding
Cauchy transform K_Gamma(f)(iy), in all cone directions and orders.
In dimension one both half-lines are required, with their prescribed
orientations; (5), (12)–(13) fix the normalization. Necessity pairs
positive-definite derivative kernels with positive-definite f.
Sufficiency uses the complete-monotonicity measure representation,
analytic continuation, and reconstruction from all cones. Thus neither
proof supplies the signs for an arbitrary f. Theorem 1 similarly needs
all derivative signs for two distinct exponential tilts and a transform
order exceeding the tempered distribution's order.

These are auxiliary Cauchy transforms of f, not f's own boundary
continuation. Taking f to be a proposed boundary value of A would first
require identifying that value and its distribution class; taking
f=A on R changes the operation. Neither choice makes the derivative
hierarchy follow from L596. No application is asserted.

### Search record, decision and limits

Fresh queries included:

- `"Fourier transform" positivity "finite part" contour`
- `"Tuck" "positivity" "higher order" Fourier`
- `"Hadamard finite part" Fourier transform positivity theorem`
- `"Hadamard" "finite part" "Plemelj" Sidi`
- `"Fourier" "positive definite" "boundary values" strip distribution theorem`
- `Galapon "Cauchy principal value" "absolutely convergent" arxiv`
- `"Tuck" "positivity" "finite-part"`
- `"associated kernel" "Cauchy" "theta" Fourier positivity`

The primary Galapon and Norvidas passages above, rather than search
snippets, support the comparison. Tuck's simple-pole limitation is
reused from the ready predecessor; the ordinary detour search was not
reopened as mathematics. Numerical finite-part quadrature papers,
Estrada–Kanwal regularization and higher-dimensional Plemelj hits
remain unread leads, not theorem evidence. No inaccessible essential
source is being assumed; the result is a bounded search failure to
find an applicable sign criterion, not SOURCE_BLOCKED or a global ban.

Decision: park this boundary extension. Reopening needs an identified
boundary object/subtraction formula with full correction signs and
an independently testable sufficient condition; boundary existence
alone will not qualify. No first-level or higher-degree sign is proved.

The separate proposed continuation asks for source coverage of one
finite necessary sign of the Cauchy transform built from real-axis A,
not A's boundary trace. Its exact nomination is in
`2026-10-31-associated-theta-cauchy-second-derivative-review.md`.
That assessment remains REVIEW_REQUIRED; no derivative formula,
positivity, new lemma or mathematical script was derived here.
This is a materially different operation, independent of the unresolved
boundary regularization. It is not yet a justified creative central-gap
attempt: no mechanism controlling the full sign hierarchy is known.
Full matching Mathlib coverage is not checked; no absence is asserted.
