# Response discriminant mean — conjugate coverage and contour comparison

TARGET: Determine the leading dyadic mean of L367's normalized discriminant B²−4ℓ_F0 C, including its sign and a vanishing relative error.
CHECKED: 2026-10-06
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Third bounded review checked the exact title/DOI, author research links, publisher article/abstract/PDF endpoints and the related arXiv:2104.10243v3; the complete JNT theorem remains inaccessible through the checked routes.
SOURCE_EVIDENCE: Reused ready conjugate/scalar coverage; inspected Das–Pujahari arXiv:2104.10243v3 (22 May 2024), §1.2 Theorem 3 and §2 Lemma 5, (15)–(16), which explicitly quotes JNT Proposition 2; inspected the author research-page links. Full JNT definitions (3)/(8)/(9), Theorems 1/3 and proof endpoint cases remain unread.
COMPARISON: The accessible Hardy statement is mollifier-specific and excludes direct a=1 in its stated interval range; the companion zeta theorem is also mollifier-specific. Neither is arbitrary right-line/gamma-weight coverage for the sharp discriminant mean.
GAP: Full JNT hypotheses and endpoint cases remain unavailable; generic same-sign moving-weight products and sharp signed endpoint control are still uncovered. Park the dependent mean instead of repeating access searches.
REASON: New primary theorem-scope evidence rules out the accessible companion statement as a direct substitute; repeated unsuccessful full-source access now warrants parking this source-dependent target and reviewing an independent pointwise algebraic test.
LITERATURE_REASON: The saved target required extracting the essential unread Das–Pujahari sharp-moment lead; this review inspected its accessible primary restatement rather than repeating ready conjugate coverage.

## Inspected primary statements and their restrictions

M. P. Young, *A short proof of Levinson's theorem*, Archiv der Mathematik
95 (2010), 539–548, DOI 10.1007/s00013-010-0199-9:
[primary published PDF, Lemmas 4–5, pp. 542–543](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf#page=4).
Lemma 5 assumes positive integers h,k with hk≤T^(2θ), fixed θ<1/2,
complex α,β=O(1/log T), and a weight satisfying (2.1)–(2.3):
0≤w≤1, support in [T/4,2T], and w^(j)=O_j((T/log T)^(-j)).
It evaluates

\[
\int_{\mathbb R}w(t)(h/k)^{-it}
 \zeta(1/2+\alpha+it)\zeta(1/2+\beta-it)\,dt
\]

by the two hm=kn sums in (4.5), with the respective kernels
V_(α,β) and X_(α,β,t)V_(-β,-α), and error O_(A,θ)(T^(-A)).
Kernel and gamma-ratio definitions are (4.1)–(4.3), not constants to
be suppressed. Read the full proof: Lemma 4 supplies both functional-equation
terms; integration by parts uses product-kernel decay and the lower
bound |log(hm/kn)|≥1/(2√(hkmn)) off the diagonal. There is no RH premise.
The Cauchy argument on p. 541 explains differentiating a **uniform
holomorphic** shifted error. It does not permit differentiating an
undifferentiated real-variable error. Lemma 3's mollifier-specific
conclusion is not an arbitrary-right-line-weight theorem.

The text extraction renders (4.4)'s decay ratio in reverse, whereas the
following proof explicitly uses (1+mn/T)^(-A). A page-image fetch timed
out. Do not import the extracted (4.4) as an independent bound without
checking the displayed version; the complete Lemma 5 statement and its
proof's actual product bound were inspected. This isolated display issue
does not supply full discriminant coverage or constitute a persistent
source-access blocker.

S. Bettin, V. Chandee and M. Radziwiłł, *The mean square of the product
of the Riemann zeta function with Dirichlet polynomials*,
[author PDF dated January 15, 2015, (1.1), Theorem 1, pp. 1–2](https://www.math.mcgill.ca/radziwill/BCR.pdf#page=1),
published J. Reine Angew. Math. 729 (2017), 51–79.
The theorem concerns |ζ(1/2+it)A(1/2+it)|² with smooth φ(t/T)
supported in [1,2], A(s)=Σ_(n≤N)a_n n^(-s), a_n≪_η n^η,
N=T^θ, θ<17/33. Its main term is the gcd/lcm sum in Theorem 1
and its error is O(T^(3/20+η)N^(33/20)+T^(1/3+η)).
This version has no shifted statement. Its θ>1/2 off-diagonal analysis
is unnecessary for a sufficiently short truncation here. The full proof
was not inspected or imported; no derivative or same-sign conclusion
is credited to it.

K. Pratt, N. Robles, A. Zaharescu and D. Zeindler, *More than five-twelfths
of the zeros of ζ are on the critical line*, Research in the Mathematical
Sciences 6, 2 (2019),
[§4, Theorem 4.1](https://link.springer.com/article/10.1007/s40687-019-0199-8#Sec4).
The published statement has two polynomials with a_n,b_n≪_η n^η,
N=T^θ, smooth Φ supported in [1,2] with Φ^(j)≪_j log^j T,
and α,β≪1/log T. Its first, generic-coefficient error is
T^(3/20)N^(33/20)+N^(1/2)T^(1/2+η); it states the two polar
ζ(1±α±β) contributions together. Read all three error cases and
the proof's opening reference to [58, §3.2.5]. The special Möbius
coefficient improvements do not apply merely because our coefficients
are arithmetic. The inherited general shifted proof and its shift-uniform
constants were not fully inspected here. This is supporting comparison,
not a second independent proof or coverage for arbitrary gamma weights.

## Applicability, required specialization and uncovered cases

Reuse drafts/literature/2026-10-05-gaussian-linear-response-sign.md and
the separate mean-audit assessment for Arias de Reyna's scalar Theorem 6,
Cauchy jets, the exact reflection, and absolute right-line convergence.
Reuse drafts/literature/2026-10-05-gaussian-response-quadratic-sign.md
for the qualified DLMF gamma/polygamma and Euler-product inputs. These
sources and assumptions have not changed. Inspected L367 (1)–(15),
L369 (4)–(14), and L368's carrier and full-curvature treatment.

The right-line jets have absolutely convergent logarithm-weighted series.
After **proving** a finite truncation error, they can furnish short rational
twists; their decay fits the generic coefficient restriction. Young's
shift radius fits critical-line jets through order two, subject to retaining
frequency-versus-complex derivative factors and uniform Cauchy contours.
These are applicability observations, not a proved truncation, differentiated
moment, or discriminant identity. The two functional-equation contributions
must be combined analytically before taking the zero-shift limit; individual
polar terms cannot be evaluated there separately.

In particular the reviewed hypotheses require a slowly varying real
weight. A gamma-phase multiplier with phase derivative of size log T
does not satisfy those derivative hypotheses. Products arising from real
projections may have both conjugate and same-sign critical factors;
L369's reflection identity must be used exactly, and it has not been
shown in this review to remove every remaining oscillatory multiplier.
A theorem for a modulus square cannot silently replace a real square.
Nor do fixed smooth-weight estimates automatically give the original
unsmoothed [H,2H] integral at whatever smaller scale survives cancellation.
Endpoint envelopes, right-line tails and carrier-weight variation still
need a stated source comparison. No complete reduction was derived here.

Consequently essential coverage remains incomplete. A further bounded
source review should check a primary same-sign jet-product/contour input
and the sharp-interval hypotheses, reusing the conjugate coverage above.
If it establishes a different bounded specialization of named inputs,
record exactly that difference before approving research; a direct theorem
for the full discriminant is not required. Do not repeat the BCR discovery
search or its unshifted statement as if it closed these gaps.

## Search, duplicates and failures

Queries submitted included `twisted second moment zeta derivatives small
shifts Bettin Chandee Radziwill theorem 2015`, `zeta derivatives second
moment Hardy Z derivatives twisted second moment polynomial`,
`Bettin Chandee Radziwill mean square product zeta Dirichlet polynomial
arxiv Theorem shifted`, `"twisted second moment" "alpha" "beta" zeta
theorem uniform`, `"twisted second moment" "shifts" "Young"`,
`Matthew Young "twisted second moment" "Theorem 1.2"`,
`"A short proof of Levinson" shifts second moment Young`,
`"twisted second moment" "alpha" "beta" "uniformly" "a_n"`,
and `"shifted" "second moment" "Theorem 1" "Radziwill" "Pratt"`.
Additional bounded terminology searches used zeta with `same sign`,
`non-conjugate`, `nonconjugate`, `non-conjugated`, `complex second moment`,
`mean value zeta squared critical line`, `first moment zeta(s)^2`,
`Gonek lemma chi`, and `polarized Laguerre`, plus
`"Laguerre" "discriminant" "bilinear"` and
`"Laguerre inequality" "pencil" discriminant`. Some returned unrelated
uses of zeta or Laguerre; none establishes absence or novelty.

The Roy–Robles–Zaharescu PDF returned as a lead was checked only to
identify the mollifier-restricted Theorem 1.1; its later technical inputs
and proofs remain unread and are not coverage. Results on signs of
Hardy derivatives, extrema, random matrices, conditional shifted moments
and the Gonek–Ki paper likewise remain unused leads; neither snippets
nor their titles approve the needed moments. The precise primary contour
input for the remaining same-sign case has not yet been isolated.

Narrow searches of drafts/literature/2026-10-05-gaussian-*,
history/2026-10-05-gaussian-*, the relevant L367–L369 files, and
ATTEMPTS/2026-10-04-gaussian-common-first-sign-threshold.md found only
the proposed discriminant placeholder. L369 is an established linear
obstruction, not the new quadratic mean. The global-regulator stop in
L365 remains valid; this is a changed independent target, not a reopening.
The long-height-versus-coupled-height and absolute-budget failures recorded
in the supplied overview are warnings against changing sampling or hiding
an unsigned remainder; no such historical failure prohibits this mean test.

Full matching Mathlib coverage is **not checked**. No library theorem
for the discriminant mean or its weighted jet moments is claimed.

Use exactly L367's real quantities B=mathcal B, C=mathcal C and
ℓ_F0=(F_0′²−F_0 F_0″)/(A²L²). The proposed mean is
H^(-1) integral from H to 2H of (B²−4ℓ_F0 C), at actual real
frequencies and with the original positive normalization. No regulator
curve, arbitrary prime phases, zero premise or division by F_0/G is allowed.
Essential local inputs are L018, L358, L366, L367, L368 and audited L369.

The main gap remains global actual-theta mixed positivity. L368 supplies
a positive eventual quadratic coefficient, whereas L369 rules out an
eventually nonnegative linear coefficient. The discriminant tests a
possible sufficient comparison involving the constant term as well.
A positive leading mean would obstruct eventual nonpositive discriminant;
a negative mean would provide only averaged evidence, requiring a separate
pointwise argument before any total-sign conclusion. Neither outcome
would by itself prove the first theta sign or the higher mixed conditions.

The eventual mathematical test is a controlled nonzero leading mean with
an error little-o of its magnitude, or a precise failure of that certificate.
Do not assert its scale or sign in advance. If the main terms cancel or
available estimates cannot separate the sign, record that failure instead
of escalating automatically to more moments. First compare exact known
mixed-moment theorems and recorded local failures; if an inspected theorem
already covers the target, import it rather than reprove it.

The total theta margin, higher low-index signs, heights above forty and
endpoint arithmetic margin remain unresolved. L365's stopped common
global-regulator certificate stays stopped; this proposed moment is not
a reopening of that target. Mathlib coverage of the full proposed mean
is not checked. No new mathematics has been attempted or approved here.

## Second bounded review: contour and sharp endpoint comparison

Completed 2026-10-05; literature only. The first review above is retained,
including its successful conjugate coverage and display qualification.
The second review inspected L367 (1)–(3), L368 (1)–(7), L369 (4)–(14),
the saved linear-mean audit coverage and the existing discriminant draft.
No local duplicate theorem was found in these specific inputs. The earlier
failure screen is reused; no sibling notebook or new mathematical script
was read or written. No discriminant reduction was derived.

### Gonek: precise narrower input, not blanket oscillatory coverage

S. M. Gonek, *Mean values of the Riemann zeta-function and its derivatives*,
Invent. Math. **75** (1984), 123–141, DOI 10.1007/BF01403094,
[author PDF, Lemmas 2–5, pp. 130–132](https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=8).
The extracted Lemma 5 (26) assumes a fixed a>1, a nonnegative integer
logarithmic weight order and complex coefficients b_n bounded by n^eta
for every eta>0. It evaluates a chi(1-a-it)-weighted absolutely convergent
Dirichlet series on [1,T], with error of order T^(a−1/2)(log T)^m.
Its proof treats [T/2,T], then sums dyadically; Lemmas 2–4 retain endpoint
stationary-transition errors and distinguish near and far endpoint indices.

The original PDF text garbles several displayed exponents and symbols.
Screenshot calls returned text placeholders without accessible images;
local retrieval failed DNS resolution. Thus no display-dependent formula
is imported. The extracted proof was read through its final dyadic sum,
but that is not verification of the missing displays. The lemma does not
state uniformity for a growing rational twist, H-dependent coefficient
families or arbitrary moving gamma weights. Such use needs a separate
justification; neither a fixed-twist restatement nor a title provides it.
No RH-dependent zero-sum corollary of this paper is used.

This comparison changes the source route: a generic appeal to Gonek does
not complete the assessment. A source directly treating sharp derivative
moments is a better next extraction target. This is a theorem-scope finding,
not a proof that the discriminant attempt fails or that contour methods
cannot work.

### Supporting strip input and the signed endpoint issue

E. C. Titchmarsh, *The Theory of the Riemann Zeta-function*, second edition
revised by D. R. Heath-Brown (1986),
[§5.1, (5.1.1)–(5.1.8), pp. 95–96](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=52),
gives polynomial growth on fixed strips and the unconditional convexity
exponent (1−sigma)/2 on 0<sigma<1, with an arbitrary positive exponent
loss. Read the finite-order, functional-equation and convexity discussion;
uniform complex neighborhoods and derivative losses must still be justified
by Cauchy estimates in a later specialization.
[§7.2(A), p. 141](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=75)
states a uniform second-moment upper bound on 1/2≤sigma≤2 of order
T min(log T,1/(sigma−1/2)), with log T at the endpoint. Its proof splits
the coefficient ranges and real-part ranges. These are supporting bounds,
not sharp local derivative moments or a full discriminant theorem.

Young's [§2, pp. 540–541](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf#page=2)
removes smoothing for his nonnegative squared integrand by smooth upper
and lower bounds to the characteristic function, with transition width
T/log T. A signed discriminant cannot use that inequality directly.
It requires an absolute endpoint envelope, derived from applicable positive
jet moments, and comparison against the actual surviving main term.
The supplied review has not established that comparison. No smaller
transition width or uniform short-interval theorem is inferred.

### New primary lead: sharp Hardy derivative products

M. K. Das and S. Pujahari, *Mean of the product of derivatives of Hardy's
Z-function with Dirichlet polynomial*, J. Number Theory **258** (2024),
334–367, DOI 10.1016/j.jnt.2023.11.001,
[publisher article](https://www.sciencedirect.com/science/article/pii/S0022314X23002366).
Read the available introduction, Theorems 1–3 labels/text, Remark 1 and
section descriptions. Theorem 3 concerns two finite-order Hardy derivatives
times a Dirichlet-polynomial modulus square in a sharp short interval.
The available text omits essential equations (3), (8), (9), parameter
ranges, constants and errors; no applicability or parity formula is imported.
Theorems 1/3, Propositions 1/2 and their relevant proof cases remain
uninspected in complete form. The authors' research page links only this
publisher page for the paper. No openly accessible preprint was located
by this bounded search; this is not evidence that none exists.

This is a specific new relevant lead, not an essential source already
credited as read. Its modulus-square restriction may still leave same-sign
right-factor products outside its scope. The next comparison must retain
that restriction and the actual gamma phase, and either document a bounded
specialization of named tools or leave the dependent calculation parked.

Additional queries were `Gonek lemma chi Dirichlet integral`, `zeta
non-conjugate second moment`, `zeta twisted second moment sharp interval`,
`mean zeta(s)^2 integral non conjugate`, `Gonek Mean values Riemann zeta
1984 pdf`, `Riemann zeta convexity bound sigma 0 1 Titchmarsh theorem`,
and the exact Hardy derivative-paper title with `pdf`, `authors`, and
`Das Pujahari arxiv`. Thesis restatements were leads only; none is used
as a substitute for primary hypotheses. No matching Mathlib coverage
was checked and no absence is claimed.

The main gap, intermediate discriminant target and downstream use remain
as stated above. Continue only after essential coverage is ready, and then
test a nonzero leading sharp mean with error little-o of its magnitude.
If cancellation leaves a scale unsupported by the endpoint/truncation
estimates, stop this certificate rather than assume sign or undertake an
unreviewed lower-order calculation. The independent theta margin and
higher-sign gaps remain open. Completed outcome: EXPLORATION,
LITERATURE, NOVELTY_UNCHECKED; this is new source-scope evidence and a
concrete extraction lead, not mathematical progress beyond the sources.

## Third bounded review: accessible restatement and parking decision

Completed 2026-10-06, literature only. Existing unfinished derivations,
identifiers and stop evidence are preserved. The target was not calculated.

The JNT article page, abstract endpoint and PDF endpoint returned internal
errors on direct opens. Indexed publisher text still omits essential
formulas. The [author research page](https://sites.google.com/view/mithundas/research),
item 8, links only to the publisher for this article. Searches used the
exact title with `pdf`, the DOI, and `Pujahari Dirichlet polynomial Hardy
preprint`. No accessible full JNT copy was located in this bounded review;
this makes no claim about copies elsewhere. No paid access, API key or
message to an author was used. Together with the preceding review, this
is a repeated access obstacle; another unchanged access search is not the
continuation.

An accessible primary comparison is Das–Pujahari,
*Zeros of higher derivatives of Riemann zeta function*,
[arXiv:2104.10243v3, 22 May 2024, §2 Lemma 5](https://arxiv.org/html/2104.10243v3#S2).
It explicitly restates part of JNT Proposition 2. It uses
G_k=Z^(k)/(log sqrt(t/(2π)))^k and the squared modulus of the mollifier
Σ_(n≤T^θ) μ(n)n^(−1/2−it)(1−log n/(θ log T)). With
κ=min(k₁,k₂), it requires 0<θ<(2κ+1)/(4(κ+1)) and H=T^a,
1/2+θ<a<(4κ+3)/(4(κ+1)). Equations (15)–(16) give parity-dependent
main terms and relative-size error O((log log T)^3/log T), including
separate zero-order cases. The upper range excludes a=1; no endpoint
extension is imported. Its §1.2 Theorem 3 allows a≤1 but retains the
specified Möbius mollifier and conjugate zeta jets. Neither statement
covers arbitrary right-line factors or moving gamma weights. The quoted
Hardy proof remains in the inaccessible JNT source; these statements are
scope comparisons, not imports or substitutes for that proof.

This is new evidence against the direct companion-theorem substitution,
not a failure theorem for the discriminant or for contour methods. The
full JNT theorem may have broader scope; its unseen formulas cannot be
credited. Known conjugate coverage remains ready and need not be refreshed.
Mathlib matching coverage remains not checked.

The main gap remains global actual-theta mixed positivity. The reviewed
intermediate target was the original sharp discriminant mean; a positive
nonzero leading mean with relative o(1) would obstruct eventual nonpositive
discriminant, while a negative mean alone would not sign theta. Its scale,
sign, same-sign moments and endpoint error remain unresolved. The
continuation test remains nonzero leading mean with relative o(1); failure
of coverage now parks this dependent certificate without asserting that
its mathematical conclusion is false.

For recovery, propose a different independently testable intermediate:
a zero-safe pointwise Wronskian decomposition of this discriminant, retaining
the full common-envelope curvature. This finite algebraic test needs no
sharp moment theorem. An exact decomposition could isolate a square and
identify the remaining signed term before any averaging. It may also show
that this route provides no useful pointwise comparison. No identity is
derived or approved here. Its separate REVIEW_REQUIRED assessment is
`drafts/literature/2026-10-06-discriminant-pointwise-decomposition.md`.
The next turn must assess that exact target before any calculation. The
total theta margin, higher signs, exterior heights and endpoint arithmetic
margin remain independent gaps; L365's fixed-regulator stop is preserved.

Completed outcome: NEGATIVE, LITERATURE, NOVELTY_UNCHECKED. The advance is
in route selection through new primary scope evidence, not new mathematics.
