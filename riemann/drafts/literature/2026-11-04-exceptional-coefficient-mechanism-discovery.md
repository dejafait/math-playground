# Exceptional coefficient gap — completed bounded source comparison

TARGET: Perform a bounded source comparison of contiguous-minor condensation and real-root-preserving coefficient multipliers for actual-Xi exceptional minors k=r-1; identify one explicit additional hypothesis that could be tested independently of RH, or reject both routes using the recorded smoothing and compensation stops.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step407 inspected primary condensation, Pólya–Schur and nonlinear Turán-preserver statements; searched exact mechanism terms and local failures; followed the relevant sharp ratio-bound counterexample and a new actual-Xi infinite-log-concavity lead. Queries, read limits and version qualifications appear below; no novelty inference.
SOURCE_EVIDENCE: Dodgson (1866), condensation rules and adjugate proof; Borcea–Brändén math/0606360v6 Theorem1.7 pp.4–5; Brändén 0909.1927v3 Theorem5.7 pp.9–10; Katkova–Vishnyakova math/0504183v1 Theorems1/4 pp.2–3 and Section3 Toeplitz proof p.12; McNamara–Sagan 0808.1065v2 Lemma2.1 pp.3–4. Liu–Mao 2610.04972v1 Theorem1.1 and Section5 are an inspected but unaudited source lead.
COMPARISON: Condensation supplies a difference of products with no missing sign margin; multiplier preservation needs an independent real-rooted input and a certified multiplier. Sharp finite Toeplitz counterexamples exist below the order-dependent ratio threshold. No inspected theorem transfers L771 to k=r-1. Iterated Turán signs are a different observable; a concrete source-supported countermodel specialization is prepared separately.
GAP: Actual-Xi exceptional signs remain open. The new preprint's full proof and any actual-Xi-specific bridge from iterated Turán signs to contiguous minors are unverified. The proposed global positive entire countermodel has not been constructed.
REASON: Reject identity-only condensation and an uninstantiated multiplier as sign mechanisms at this scope. Before spending a creative attempt on a Turán-to-minor bridge, test its generic implication using known sharpness examples and a source-certified all-iterate condition.
LITERATURE_REASON: This invocation completed the essential missing primary hypotheses for the nominated mechanisms; the sharpness theorem and actual-coefficient Turán lead were new relevant findings within that comparison, not repeat browsing of L771.
SCOPE: Literature-only comparison; no lemma, new coefficient identity, new sign result, mathematical script or numerical scan was written. The following original nomination is retained as pre-step407 history; the completed decision is above and the source comparison is below.

## Evidence already available

The completed audit is canonical in L771. Its only direct notebook
input is L019; it assumes no exceptional coefficient sign. For a
future source comparison, recover the exact Xi coefficient/minor
conventions from L021 and the recorded step391 source normalization
before comparing any factorials or indices. L766 remains unaudited
and is not an accepted premise.

Reuse the inspected cases in
2026-11-04-actual-theta-signed-compensation-review.md and
2026-11-04-nuttall-cumulant-induction-transfer-review.md.
The former already separates derivative transfer, restricted
weighted-moment inequalities and iterated-tail cumulants. Their
cofactor, origin-boundary and exceptional-index limitations remain
in force. A smaller smoothing onset alone cannot remove the stated
positive smoothing cost at k=r-1. A historical stop is not a global
ban, but reopening it needs a specific new input and test.

## Bounded comparison requested, not yet carried out

First inspect primary hypotheses for contiguous-minor condensation
and determine what actual coefficient boundary data would be needed
to propagate signs to the exceptional edge. Do not treat a
determinantal identity as positivity propagation. Independently,
inspect the relevant coefficient multiplier preservation criteria
and determine whether their hypotheses can be certified for the
actual sequence without assuming its desired real-root property.
These are two source leads, not claims that either can work.

Compare against the notebook's recorded failures in targeted paths;
do not repeat broad source searches already covering identical
hypotheses. Select at most one concrete, bounded intermediate test
if a primary theorem and an independent extra hypothesis justify
it. Otherwise record the specific obstruction and choose a genuinely
different lead. No new ready continuation is created here: a
separate source review must decide IMPORT, SPECIALIZE or EXPLORE
before a mathematical attempt. Mathlib coverage is not checked.

## Completed comparison — step407

The main gap remains actual-Xi all-degree mixed positivity and its
exceptional coefficient signs. The reviewed intermediate target was
an independent hypothesis allowing condensation or a coefficient
multiplier to reach k=r-1. Downstream use would be an edge-sign input,
with other indices and the passage to all-degree signs still separate.
Continue only with a hypothesis certifiable without the desired signs;
otherwise park the proposed transfer. No actual-Xi sign was proved.

### Exact conventions and retained stops

L021 gives M_(2n)=integral u^(2n)K(u)du and the denominator (2n)!.
For comparison use a_n=M_(2n)/(8*4^n*(2n)!) and
D_(r,k)=det[a_(k+j-i)] for i,j=0,...,r-1. These are the
definitions in L766, whose proof remains unaudited and is not used.
At k=r-1 the coefficients range from index 0 through 2r-2.
L771 is an accepted smoothing input, not a coefficient-transfer theorem.

Reuse the inspected step391/392 assessments linked in the nomination.
Their Nuttall coefficient range k>=r-1+ceil(m/2), origin/cofactor
compensation limitations and different-kernel transfer stop are unchanged.
The primary det3CAEXP_2.pdf exceptional-case discussion was also
retrieved: Section4.6 explicitly leaves infinitely many exceptions.
No zero-free-region proposal or parked arithmetic estimate is made.

### Condensation: what the source actually supplies

C. L. Dodgson, *Condensation of Determinants, being a new and brief
Method for computing their arithmetical values*, Proc. Royal Soc.
London 15 (1866), 150–155, rules(1)–(4), zero-divisor discussion,
and the adjugate proof, read in the
[public-domain transcription](https://schnark.github.io/lewis-carroll/html/magazines/condensation-of-determinants.html)
and [Gutenberg reprint](https://www.gutenberg.org/files/37354/37354-pdf.pdf),
reprint pp.2–6. The proof's 3-by-3 and 4-by-4 cases were inspected.
The underlying Desnanot–Jacobi identity is polynomial; division in
condensation requires a nonzero interior minor. Row rearrangements
in the algorithm are not a positivity-preserving Toeplitz argument.

In the present notation the standard contiguous Toeplitz specialization
is D_(r,k)D_(r-2,k)=D_(r-1,k)^2-
D_(r-1,k-1)D_(r-1,k+1), with D_(0,k)=1.
This is an applicability/index comparison of the named identity,
not a new local lemma or a sign proof. To use its quotient with a
positive denominator, one needs the difference on the right
nonnegative, including a strict margin if strictness is sought.
Signs of its factors alone do not provide that comparison. A zero
interior minor must be retained in the undivided identity. L771 does
not supply this coefficient boundary data. Assuming that inequality
as the new hypothesis would merely repackage the missing determinant
sign, so identity-only propagation is rejected.

### Multipliers: input and symbol hypotheses persist

Julius Borcea and Petter Brändén,
[*Multivariate Pólya–Schur Classification Problems in the Weyl Algebra*](https://arxiv.org/pdf/math/0606360v6),
v6, 6 November2009, Theorem1.7, printed pp.4–5, gives the classical
Pólya–Schur equivalences. For a real diagonal sequence mu_n,
the symbol is sum mu_n z^n/n!; it must have the stated same-sign
real-zero approximation/product, equivalently the binomial test
polynomials have same-sign real zeros. The definition acts on
real-rooted polynomials. The entire product requires a>=0,
alpha_j>=0 and sum alpha_j<infinity, up to reflection and the
allowed real constant and initial monomial. These hypotheses were read.

L021 concerns ordinary coefficients a_n, not an exponential
generating sequence. Using an actual coefficient sequence as a
multiplier requires the factorial conversion; using mu_n=n!a_n
makes the symbol precisely the actual generating function. Its
required zero property is the desired property, not an independent
certificate. Alternatively a fixed known multiplier needs an
independently real-rooted input and an exact coefficient relation.
Neither has been supplied from the smoothed derivative determinants.
Preservation supplies no inverse conclusion from a transformed
function's signs. No multiplier is proposed or tested here.

Petter Brändén,
[*Iterated sequences and the geometry of zeros*](https://arxiv.org/pdf/0909.1927v3),
v3, 30 August2010, Theorem5.7 pp.9–10 and its complete proof were read.
It covers nonlinear U_alpha on polynomials with nonpositive real
zeros and on LP-positive entire functions. The proof reduces to
Hermite–Biehler and the previously stated preserver criterion.
It does not infer the input zero property from nonnegative iterates.
The definitions, Theorem6.1 and the S_1 case of Proposition6.2 were
also read. No full independent proof audit is claimed.

### A discriminating additional hypothesis and its known limit

Olga M. Katkova and Anna M. Vishnyakova,
[*On sufficient conditions for the total positivity and for the
multiple positivity of matrices*](https://arxiv.org/pdf/math/0504183v1),
v1, 9 April2005, Theorem1 p.2 and Theorem4(i) p.3, state both
the determinant criterion for positive matrices with adjacent ratio
at least c_k=4cos^2(pi/(k+1)) and sharpness even for Toeplitz
matrices. Strict adjacent inequalities yield a positive determinant.
Section3 p.12's full Toeplitz proof was read: a tridiagonal
sine-determinant model is perturbed by successively small positive
Toeplitz diagonals while retaining the ratio inequalities and
negative determinant. The Hankel case is unnecessary here.

This provides a concrete finite ratio hypothesis rather than a
determinant-sign identity. It is not certified for actual a_n.
For an order-five discriminator the source threshold is c_5=3;
a bound 11/4 is below that threshold. The source's finite sharpness
example is ready to specialize; no global coefficient counterexample
is claimed in this turn.

Peter R. W. McNamara and Bruce E. Sagan,
[*Infinite log-concavity: developments and conjectures*](https://arxiv.org/pdf/0808.1065v2),
v2, 24 March2009, Section2 pp.3–4, Lemma2.1 and its full preceding
proof, give preservation of r_0-factor log-concavity,
r_0=(3+sqrt(5))/2. Sequences are extended by zero at negative
indices. This supplies an all-iterate certificate if a positive
global sequence meets that inequality; finitely many numerical
iterates would not suffice. Since 11/4>r_0, it is a usable
source-supported certificate for the proposed independent test.
No new extension or combination proof was performed.

The separate continuation assessment records exactly what remains:
an explicit positive prefix, its negative 5-by-5 determinant,
a compatible positive tail, entire convergence and all-index bounds.
This is reproduction/specialization of known obstructions, not a
creative actual-Xi mechanism or certified originality. Success would
reject a generic infinite-log-concavity-to-edge-sign inference;
it would not decide the actual-Xi minors.

### New actual-Xi lead, deliberately not imported

Yanxin Liu and Jianxi Mao,
[*Infinite log-concavity of the Taylor coefficients of the Riemann
xi-function*](https://arxiv.org/html/2610.04972v1),
v1, 4 October2026, (1.1), definition of L, Theorem1.1 p.3,
and Section5 pp.54–55 were read, including the complete Lemma5.1
proof and the two-case assembly. Their lambda_n is
xi^(2n)(1/2)/(2n)!, whereas a_n=lambda_n/(8*4^n).
Their claimed conclusion is positivity of all L-iterates, not a
contiguous-minor theorem. The proof invokes analytic Proposition3.5
and computer-assisted Proposition4.5 with different index ranges.
Those essential estimates and the numerical certificate were not
audited; no actual-Xi theorem is imported. The read closure argument
alone cannot validate Theorem1.1. This source is motivation for
testing a generic transfer, not a premise of the next test.

### Search record, qualifications and route

Web queries included exact terms for Desnanot–Jacobi/contiguous
Toeplitz condensation; Pólya–Schur multiplier sequences, Jensen
polynomials and factorials; infinite log-concavity versus total
positivity/real-rootedness; the new preprint identifier with
correction; and Katkova–Vishnyakova's sharp cosine threshold.
Primary statements above, not search snippets, support the comparison.
The retrieved preprint claiming a de Bruijn–Newman resolution was
not inspected or used. Unread related leads are not evidence.

Local searches were confined to literature, ATTEMPTS, relevant
same-day history and the indicated source/lemma files. Exact
condensation/multiplier terms and the new preprint ID/title/authors
found no prior matching assessment in these searches. Narrow
theta/coefficient/Toeplitz searches found no prior matching
sharp-ratio countermodel. This is not exhaustive duplicate exclusion.
The old Hermite/pencil preserver assessments concern different
hypotheses and were not relabeled as coverage here.

HTML/PDF renderings of older arXiv sources disagree in regenerated
display dates and some equation numbers. Citations bind to the
arXiv version, theorem and proof section; no recent revision is
inferred from a regenerated date. The KV Toeplitz construction was
read in both renderings. No persistent access blocker remains.

Full matching Mathlib coverage is not checked; no availability or
absence claim is made. No lemma, script, DAG or PROOF argument was
changed. The bounded comparison is complete. Park direct condensation
and uninstantiated multipliers. Prepare the known-obstruction
specialization for separate next-turn approval. A creative central
attempt remains blocked by the absence of an independent actual-Xi
bridge; this finite discriminator should be resolved first.

