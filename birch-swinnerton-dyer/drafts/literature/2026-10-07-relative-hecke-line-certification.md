# Full-relative integration line from finite Hecke data — source comparison

TARGET: Assess whether certified Hecke and real-involution matrices on the full relative weight-two symbol module, together with an exact one-dimensional simultaneous dual kernel for E's eigenvalues, certify L028's real-integration line without a twist value or an assumed relative-line identification.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Checked L028, ATTEMPTS/022--023 and targeted normalization/audit histories for duplicates and failures; searched relative modular-symbol Hecke duality, real involution, eigenspaces and msfromell; inspected the primary Stein and Cremona passages identified below.
SOURCE_EVIDENCE: Stein online General Modular Symbols, Hecke Operators, Proposition 1.38, Theorems 1.39 and 1.42 with its full change-of-variables proof, Remark 1.41, equations (11)--(12) and Remark 1.43; Cremona corrected second edition Section 2.1.2--2.1.3, equations (2.1.3)--(2.1.4), pp. 10--12, Section 2.4 pp. 18--19 and Section 2.7 pp. 25--26.
COMPARISON: Known results provide full-relative integration and Hecke compatibility plus nondegenerate real-period duality on absolute cycles; Cremona already computes dual eigenvectors on absolute plus homology. The proposed full-relative finite-kernel certificate needs only an explicit specialization and rational linear algebra, not a new multiplicity or twist-nonvanishing theorem.
GAP: No source states this complete finite certificate verbatim; the mathematical turn must justify the Gamma_0(N) good-prime specialization, relative involution convention, nonzero real functional and scalar extension of the exact dual kernel. Actual matrices, kernel rank evidence, period scale, q and termination remain unproduced.
REASON: Essential source coverage is now adequate for this conditional sufficiency attempt; keep full-space kernel dimension as a certified premise and use real-period duality rather than a nonzero central or twist value. No new result is derived in this literature turn.
LITERATURE_REASON: Changed hypothesis: L028's granted full-relative integration-line identification is to be replaced by certified finite operator and kernel data; the ready audit assessment explicitly excluded production of that premise.
SCOPE: Non-CM minimal E/Q and its normalized weight-two newform at conductor N; L028's complete torsion-free relative presentation is still granted, and L(E,1)=0 is allowed. No independent twist q, Manin constant one, BSD or finite Sha is assumed for this line-identification target.
COVERED_TARGET: Prove a conditional full-relative real-integration-line certificate for L028 from certified good-prime Hecke and geometric real-involution matrices and an exact one-dimensional simultaneous dual kernel.

## Exact test and source boundaries

Main gap remains rank E(Q)=m(E) for m(E)>=2. This review targets only
the production of L028 hypothesis 2. Its plausible downstream use is
exact symbol normalization after independent q becomes available, then
L027 and conditionally L026. Essential local input is L028; L027, L026
and L004 are downstream only. Their independent arithmetic assumptions,
q-production, finite quotient F, divisible Sha, rational membership and
complex-order comparison remain unresolved.

Find and inspect primary hypotheses for the action and integration on
the whole relative module, the geometric involution r -> -r with the
orientation relevant to real integration, and integration nonvanishing
for the normalized newform even when its central L-value is zero.
Compare the finite-kernel certificate to stronger standard algorithms;
import an exact match rather than reprove it. A claimed one-dimensional
kernel must be an exact rank computation in the entire relative dual,
with certified operators, not a list of eigenvalue checks on a vector.
No sufficiency theorem, termination guarantee or finite eigenvalue bound
is asserted in this pending assessment.

Continue only if primary sources cover membership and nonvanishing on
that exact relative space and specify checkable hypotheses for the
finite certificate. If they cover absolute cycles only, leave the
boundary extension unresolved; do not assume it. Stop or narrow the
proposal if it needs the same granted line, unknown period scale or
unproved multiplicity assertion it seeks to replace. Any automatic
production/termination claim requires separate explicit coverage.

The initial pending review named Stein's operator/pairing sections and
Cremona Sections 2.6--2.7 as unread leads. This turn inspected the relevant
passages below. Earlier presentation and normalization coverage is reused;
it is not mistaken for evidence of the newly reviewed operator hypotheses.

## Primary statements actually inspected

[Stein, *Modular Forms, a Computational Approach*, online chapter
General Modular Symbols, v0.1](https://www.wstein.org/books/modform/modform/modular_symbols.html),
retrieved 2026-10-07. The Hecke Operators section treats level-N groups
containing Gamma_1(N), hence includes Gamma_0(N), on the entire symbol
module. Its prime action is the sum of transformed cusp paths; the
bad-prime formula omits one matrix. The proposed continuation is restricted
to good-prime operators, so no bad-prime normalization is needed.
Proposition 1.38 defines well-defined integration on the relative module,
not just its boundary kernel. Theorem 1.42 explicitly takes x in the
entire relative module and gives adjointness with the form operator.
Its statement is for Gamma_1(N); Remark 1.41 covers general compatible
double cosets. Read the proof from the coset sum through all determinant,
Jacobian and polynomial cancellations to its final equality. It applies
to arbitrary cusp endpoints; no cycle assumption enters that calculation.
For the continuation, match the Gamma_0(N) prime action directly to that
proof or Cremona's Gamma_0(N) formula, rather than silently substituting
a group in the narrower printed statement.

Theorem 1.39 is nondegeneracy only on the cuspidal symbol subspace.
Equations (11)--(12) define Stein's involution on the relative module;
Remark 1.43 explicitly distinguishes its sign from Cremona's convention.
Theorem 1.44 is likewise a cuspidal pairing statement, not a full-relative
uniqueness theorem. These domain distinctions are essential to the review.
The continuation must not infer a boundary extension from an absolute
eigenvector alone.

[Cremona, *Algorithms for Modular Elliptic Curves*, corrected online
second edition (1997), Chapter 2](https://johncremona.github.io/book/fulltext/chapter2.pdf),
retrieved 2026-10-07. Section 2.1.2, equation (2.1.3), printed p. 10,
states exact period duality with real absolute homology. Section 2.1.3,
equation (2.1.4), printed pp. 11--12 (PDF pages 5--6), restricts this to
the real Fourier-coefficient forms and geometric plus homology.
This is the nonvanishing input: it concerns a nonzero form, without a
condition on L(f,1). Use the stated duality, not the preceding shorthand
claim that a single form detects whether every individual cycle is plus;
that stronger reading is unnecessary. The PDF extraction loses conjugation
bars in the geometric reflection formulas, so interpret the operation as
z mapped to -conjugate(z), as in the real-structure discussion, not -z
on the upper half-plane.

Section 2.4, printed pp. 18--19, gives the Gamma_0(N) good-prime operator
and proves the integration identity by substitution on a path {alpha,beta}.
Read the displayed determinant derivative and integral equality before
the Hecke sum. Although Cremona's ambient homology formalism is absolute,
this path identity and Stein's full-relative theorem are the covered
inputs for the proposed relative specialization; neither is an assertion
that an absolute computational presentation is the relative one.

Section 2.7, printed pp. 25--26, describes columns for cycles, matrices
acting on the left, and simultaneous left eigenvectors in the dual
(equivalently eigenvectors of transposes). It determines these up to scale
on H^+(N). This is a stronger standard algorithmic precedent than simply
checking a proposed vector's eigenvalues, but it does not certify our
relative extension. No unconditional finite Hecke cutoff or termination
claim is imported from that algorithm.

## Comparison and authorization boundary

The exact covered continuation is stated in COVERED_TARGET above. It may
specialize the imported path identities and real duality, then justify
the finite rational-kernel sufficiency argument. This source review does
not perform that proof. No reproof of Manin generation, period duality,
Hecke adjointness, multiplicity one or twist nonvanishing is needed.
The only work beyond the named inputs is the explicit convention and
finite-certificate applicability argument. Classify that attempt as
REPRODUCTION, not as a discovery beyond the sources checked.

Required evidence for that attempt is an independently certified complete
relative rational presentation, good-prime matrices matching the imported
operators, geometric reflection on every generator, the matching exact
integer eigenvalues a_ell(E), and exact rank witnesses for the simultaneous
dual kernel in the entire relative dual. The desired threshold is kernel
dimension exactly one; a larger kernel leaves this certificate inconclusive.
No requirement that the chosen finite operators generate the entire Hecke
algebra is authorized or needed as an added premise of this sufficiency
target. Availability of such a finite list is a separate unreviewed target.
Check the sign with the normalized differential 2 pi i f(z) dz, not the
word “plus” in software. Stein's star has the extra minus sign. Rational
row-versus-column and full-space dimension evidence must be explicit.

Local failures ATTEMPTS/022--023 stop repeated conditional enclosure and
calibration audits. They do not obstruct this distinct missing-input test.
L028 currently grants the real line; it contains no proof from operator
data, so this attempt is not a duplicate. Even a successful conditional
certificate would produce neither matrices for a chosen curve nor a
normalized period scale, q, C, b or a nonzero quadratic coefficient.

## Search record and limits

Queries: `Stein modular symbols pairing relative homology star involution
Hecke nondegenerate`; `Cremona Algorithms modular elliptic curves 2.6 2.7
eigenspaces relative homology periods`; `"modular symbols" "relative"
"eigenspace" "dual" integration`; `"modular symbols" "mseigen"
"msfromell"`. The searches found the primary textbook passages above
and broader Eisenstein/completed-cohomology leads. Those latter papers
were not inspected and are not imported. A PARI modular-symbol handbook
lead was returned, but opening its page yielded an internal retrieval
error; it is optional software evidence and not an essential source
blocker. No novelty or source absence is inferred from the search.

Mathlib: the full certificate and supporting modular-symbol integration,
Hecke, real-duality and rational-kernel results are not checked. Unknown
coverage is not absence. The mathematical continuation must place any
completed result, full proof and precise citations in its canonical lemma
file; this literature-only turn does not modify lemmas or scripts.
