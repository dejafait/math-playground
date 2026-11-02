# Small-cutoff multiple-zero stability: completed source comparison

TARGET: Assess the proposed shifted-Xi first-variation test for small reciprocal cutoffs near a multiple real zero, including existing perturbation and heat-flow preservation results.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact reciprocal-cutoff/first-variation/multiple-zero searches and stronger universal-factor/analytic-perturbation searches were completed; scoped theta/cutoff/heat records found the existing preservation-versus-sign warning, not a completed reciprocal-weight local test. Queries and source-access limits below; no novelty inference.
SOURCE_EVIDENCE: Read L016/L018/L019/L020/L610; reused the theta-heat and signed-cancellation assessments. Inspected de Bruijn 1950 Theorems 10-12, pp.203-205; Newman 1976 Theorem 1, p.246; Parusinski--Rainer author manuscript dated 2024-10-07, Theorem 2.2 and Puiseux argument, p.7; Schnell Fall 2024 Class 2 Theorem 2.8 and proof, pp.2-4; Csordas arXiv:1309.0055v2 (4.9)-(4.10), Proposition 4.9, pp.12-13. Original collision-proof scans were not readable and are not imported.
COMPARISON: The sources supply generic analytic preparation and preservation for specified multipliers, not preservation for L610's reciprocal weight. Rellich assumes hyperbolicity throughout a parameter interval. A bounded double-zero first-sign calculation is a routine specialization; its cutoff derivative and shifted-value sign are still unproved locally.
GAP: No unconditional small-cutoff sign or splitting conclusion is available. Establish the exact parameter expansion and identify the independent shifted-Xi sign input before proposing preservation; higher multiplicities, vanishing coefficient, moving frequency, simple/off-line configurations and higher signs remain separate.
REASON: Complete the missing comparison and nominate only a local double-zero discriminator, avoiding an unsupported heat-flow transfer or all-cutoff positivity claim. The new ready calculation assessment requires separate approval next turn.
SCOPE: This assessment completes only the saved source review. No new parameter identity, root-splitting criterion, sign lemma, mathematical script or source reproof was produced. Exact next-calculation scope is recorded separately below.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changed from importing a full-cutoff witness to local stability at a hypothetical multiple zero; its essential analytic-perturbation and multiplier hypotheses had not been assessed. Ready heat/Stein comparisons were reused.

## Gap and bounded decision

Main gap: actual-Xi all-degree signs at unbounded heights. The intermediate
target is a local first-sign discriminator for L610's exact reciprocal
weight at a hypothetical multiple real zero. Its possible downstream use
is to identify a necessary sign input, or an obstruction, for a proposed
small-cutoff positivity argument. It cannot resolve RH or all-frequency
positivity, even if that local calculation succeeds.

L020 is the canonical entire cosine representation with exactly the K
and frequency convention of L019/L610. Thus the identification of the
zero-cutoff transform is already covered, not a new lemma. L016/L018/L019,
L020 and L610 were read in full. L610 is only an all-cutoff contrast;
its numerical run/backend assumptions are not inputs to the proposed
local expansion. No actual multiple zero is asserted to exist.

Continue with one bounded calculation only: specialize at an assumed
double real zero, justify a parameter expansion with a uniform remainder,
and express its leading first-sign coefficient through independently
defined Xi data. A strict coefficient sign would be a discriminating
input rather than an all-cutoff numerical sweep. Its value/sign must
remain conditional unless independently established. Stop after this
calculation if it yields only an uncontrolled shifted-value sign; do not
launch a sequence of higher-order expansions in the vanishing case.
This nominates a test, not its identity, coefficient or sign conclusion.

## Inspected theorem hypotheses and comparison

N. G. de Bruijn, *The roots of trigonometric integrals*, Duke Math. J.
17 (1950), 197-226, DOI 10.1215/S0012-7094-50-01720-0,
[repository text](https://repository.tudelft.nl/file/File_524a4d3c-0858-4c55-b425-8c8ce1fb89da).
Theorem 10 assumes integrability, conjugate reflection and decay
O(exp(-|u|^b)), b>2. Theorem 12 treats finite products of factors
xi_k exp(lambda_k u)+conj(xi_k) exp(-lambda_k u), |xi_k|=1,
lambda_k>0: the squared zero-strip width contracts by sum lambda_k^2,
down to zero. Read the Theorem 11 proof and its reduction to Theorem 8,
and the iteration immediately preceding Theorem 12, pp.203-205.
This is not a theorem about a negative exponential of an exponential or
an average of such weights. No representation of W_epsilon by admissible
factors is supplied. No reproof or specialization is claimed.

C. M. Newman, *Fourier transforms with only real zeros*, Proc. Amer.
Math. Soc. 61 (1976), 245-251, DOI 10.1090/S0002-9939-1976-0434982-5,
[primary scan](https://sites.math.northwestern.edu/~auffing/papers/Newman.pdf),
Theorem 1, p.246, states the Gaussian strip contraction: for real even
integrable f with decay O(exp(-|u|^gamma)), gamma>2, and all Fourier zeros
in |Im z|<=Delta, multiplying f by exp(delta u^2), delta>0, contracts
the width to sqrt(max(Delta^2-2delta,0)). This preserves a real-zero
input in that direction; it supplies no reciprocal-weight evolution or
sign comparison at zero cutoff. It is cited for comparison only.

Parusinski--Rainer, *Perturbation theory of polynomials and linear
operators*, [author manuscript](https://www.mat.univie.ac.at/~armin/publ/handbook_paper.pdf),
dated 7 October 2024, Theorem 2.2 and its Puiseux proof discussion,
printed p.7, assumes a monic hyperbolic polynomial with real analytic
coefficients on an open real interval around zero. It supplies analytic
root labels. Hyperbolicity is a hypothesis for every parameter, not a
consequence of one real-rooted member. The proof explicitly uses real
values of the Puiseux branches over real parameter values. This cannot
establish the desired preservation. Rellich's original paper was not
read; only this author's theorem statement/proof exposition was inspected.

Christian Schnell, *Complex Manifolds, Fall 2024*,
[Class 2, 3 September](https://www.math.stonybrook.edu/~cschnell/mat545/class2.pdf),
Definitions 2.5-2.6 and Theorem 2.8, printed pp.2-4, gives Weierstrass
preparation for a holomorphic germ whose restriction to the distinguished
variable has finite vanishing order d: a unit times a monic degree-d
polynomial with coefficients vanishing at the base parameter. Read the
contour zero-count and symmetric-coefficient proof. The theorem supplies
local multiplicity bookkeeping, not real-root preservation or a sign.
Joint parameter holomorphy of the actual integral must be justified
before applying it; a one-sided real limit alone is insufficient.

Csordas, [arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055v2),
21 February 2014, (4.9)-(4.10), Proposition 4.9, printed pp.12-13,
uses the Gaussian backward-heat family and states that a multiple real
zero at time t_0 implies t_0<=Lambda; zeros at t>Lambda are real and
simple. This does not exclude multiplicity at the transition and is not
a theorem for W_epsilon. Reuse the earlier theta-heat comparison; no
historical numerical bound or normalization of Lambda is imported.

The proposed calculation needs only L019/L020, parameter differentiation
with domination, and Taylor expansion of the first form. The generic
preparation and heat results explain the limits of potential extensions;
no root-splitting theorem is required or approved for that calculation.
In particular do not infer a zero-location conclusion from a first-sign
coefficient or silently extend a double-zero calculation to higher order.

## Searches, duplicates and source limitations

Queries actually issued included `de Bruijn roots trigonometric integrals
1950 universal factors cosh Fourier real zeros theorem`; `analytic
perturbation multiple zeros holomorphic family Puiseux real roots
hyperbolic polynomials Rellich theorem`; `"reciprocal" "cutoff" "Xi"
"multiple"`; `"Riemann" "reciprocal cutoff" "perturbation"`; `"Xi"
"first variation" "multiple zero"`; `"cosh" "Xi" "perturbation"
"zeros"`; `"Fourier transforms with only real zeros" Newman 1976 pdf`;
`"holomorphic" "multiple zero" "perturbation" "Rouche"`; and
`"Weierstrass preparation theorem" Lebl theorem holomorphic parameter`.
Exact-term results did not supply a matching reciprocal-weight theorem.
This is a bounded search, not certified originality or comprehensive
nonexistence evidence.

Reused the completed theta-heat, backward-energy, post-L607 and signed
cancellation source comparisons. Scoped exact-term searches in theta,
cutoff and heat assessments/ATTEMPTS found no completed local version of
the selected test. The generic collision-energy stop, fixed-a allocation,
first-period grouping and three-mechanism discovery stops remain in
force for their stated mechanisms. None proves a reciprocal local result.
No zero-free region or reciprocal-series continuation is proposed here.

The first Delft fetch timed out; its later primary repository text was
read. Its Theorem 13 transcription has suspect Gaussian exponents, so
those formulas are not used. The Eindhoven version-of-record scan at
https://pure.tue.nl/ws/files/1769368/597490.pdf exposes only its cover text
through this interface. The correctly parameterized Gaussian statement
above is read in Newman's Theorem 1, not repaired from OCR or derived.

Original Csordas--Smith--Varga scans at
https://www.math.kent.edu/~varga/pub/paper_206.pdf (Constr. Approx. 10,
1994, 107-129, Lemma 2.2/remarks) and paper_209.pdf (PSAM 48, 1994,
553-556, Proposition 1) returned no readable lines. Screenshot calls
yielded references without inspectable image content; shell retrieval
failed DNS. Indexed search passages identifying even/odd multiplicity
and double-zero remarks are leads, not inspected proof cases. No
conclusion is imported from those passages and their reproof is not
authorized. They are nonessential to the restricted first-sign expansion;
park any dependent all-multiplicity collision import instead of repeating
source-access attempts. Schnell's complete preparation proof and the
readable Gaussian theorem suffice for the present comparison.

No load-bearing conclusion uses an initial truncated local search.
No sibling proofs, cross-notebook input, shared infrastructure mutation,
mathematical script, lemma or DAG/PROOF change occurred. Full matching
and supporting Mathlib coverage for the proposed local calculation were
not checked; unknown availability is not absence.

## Decision and continuation

Outcome EXPLORATION: the source review narrows the mechanism to a
double-zero first-sign expansion with an explicit missing sign input.
No new local mathematical result or advance beyond the checked sources
is claimed. The unchanged full-cutoff obstruction says nothing decisive
about this local test. Literature work does not spend or renew the
mathematical exploration budget.

The exact nominated calculation is in
`drafts/literature/2026-11-01-reciprocal-cutoff-double-zero-variation.md`.
It is a routine specialization, not a creative central-gap attempt.
Independent control of the shifted-value sign remains the blocker to
such a nomination. The new assessment receives separate approval next
turn; nothing in this literature turn performs its calculation.
