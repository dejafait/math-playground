# Heat-kernel Laplace transfer — nomination1107

TARGET: Assess whether two-stage Laplace composition of the actual heat-trace kernel yields L030's finite inverse-power Hankel matrices, with exact factorial normalization, endpoint convergence and finite-order sign hypotheses.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1108 reused comparison1107 and assessment883, searched heat-trace/inverse-power Hankel and two-stage Laplace composition terminology, and checked the exact mixed-minor duplicates L033/L038/L041. No inspected source states the complete nominated double-integral bridge. This is a bounded coverage decision, not a novelty claim.
SOURCE_EVIDENCE: Polson1708.02653v24 Definition5.1/Lemma5.2 and Section6.4 give trace conventions, endpoint control and factorial heat moments; Theorem7.4/Corollary7.5 and the complete Lemmas7.6-7.9 proof cases were read. Sra's hexagon2610.00584v1 LemmaC.1/PropositionC.2 give strict finite-order transfer; reuse Ruzza Lemma3.1.1. DLMF5.12.1 and5.9.1 give the beta/gamma normalization tools. Exact citations and reading limits below.
COMPARISON: The sources cover the conditional finite-order toolkit and supply a separate source-stated finite signed-block theorem. They do not explicitly identify the nominated matrix with L030's H_d. Actual-node matching, double-integral normalization and strict improper-composition applicability remain a bounded specialization, rather than a new sign theorem or a fan transfer.
GAP: Prove the nominated entry identity and finite-order implication using only strict finite differential-block positivity at every positive time; keep this premise explicit unless separately importing the finite-block theorem with its verification-height hypotheses. No local entry identity or new matrix sign is established by this literature turn.
REASON: Finite-order source coverage is now sufficient for a mathematical specialization. Neither scalar trace positivity nor both all-size one-time blocks should replace the exact finite premise. The all-degree sign gap remains; the ready continuation is recorded separately for the supervisor's approval.
LITERATURE_REASON: New target replaces the unsupported direct fan-to-Q import with a specific two-stage heat-kernel transform; exact normalization and conditional finite-order scope lie outside review1107's completed source-import decision.
SCOPE: One bounded source comparison; no new lemma, integral evaluation, counterexample, numerical test, mathematical script or all-degree sign construction. A future mathematical attempt must be gated separately.

## Proposed object, not an established identity

Use the actual paired nodes of L018/L024-L026. To distinguish the
source heat trace from C468h's holomorphic H, call it mathcal H(t).
Match its multiplicities and squared-zero convention to the source's
H(t) and Polson's W(t) before use. A candidate finite matrix to assess is

    M_ij = integral_(x>0) integral_(y>0)
               (x^i/i!)(y^j/j!) mathcal H(x+y) dx dy,
    0 <= i,j <= d.

The proposed target is comparison with L030's S_(i+j+2), not an assertion
that they agree. No change of variables, integral evaluation or sign
consequence is proved here. In particular, do not replace a coefficient
factorial by a row factor without verification.

For degree one, the decisive observable test retains c0^2 S2,
2 c0 c1 S3 and c1^2 S4 simultaneously. For general finite d, identify
the necessary order in the source kernel/differential-matrix theorem
and the maximum moment needed; do not infer all d from fixed order.
An adequate source assessment must inspect complete relevant proof
cases for determinant composition, truncation, strict/non-strict
positivity, and the origin/infinity limits. State whether only ordered
minors or full positive semidefiniteness is obtained, and how symmetry
and finite rank enter. Do not treat scalar mathcal H>0 as a signed
kernel theorem.

## Purpose and discriminating decision

The main gap remains actual-Xi all-degree Q>=0. A correct finite-order
bridge would attach known or independently testable heat-trace matrix
premises to this exact mixed observable, bypassing the unfinished
local fan assembly. It can be useful without resolving all orders.
Continue toward a mathematical specialization only if the entry
normalization and a noncircular conditional finite-order theorem are
covered, or one explicit unmatched hypothesis yields a bounded test.
If the result is already fully known, IMPORT and cite it; do not reprove
it. If only the RH-equivalent all-order premise survives, record that
limitation and choose a materially different signed mechanism.

Essential inputs: L018/L024-L026/L030-L032/C032a; review1107's primary
identity inventory; source product/low-zero/counting qualifications.
No physical graph, reflected background, free boundary datum, arbitrary
all-order positive kernel, or actual source certificate is assumed.
C468f/h and their qualifications stay intact as contrasts, not inputs
to this proposed integral matrix. Mathlib matching coverage is unchecked.
No cross-notebook input is proposed.

This is a possible standard composition/specialization, not a justified
creative proof mechanism. The missing independently signed all-order
premise blocks that label. If a new central sign mechanism emerges,
record its precise obstruction and bounded decisive test in a later
nomination. Do not manufacture it from the scheduling preference.

## Completed source comparison1108 — 16 November 2026

The preceding proposed-object section is preserved as the nomination,
not as a completed proof. This review imports source statements and
approves a separate conditional specialization; it does not evaluate M.

### Precise primary inputs and reading scope

Nicholas G. Polson, *On Hilbert's 8th Problem*, September2026,
[arXiv1708.02653v24](https://arxiv.org/pdf/1708.02653v24):
Definition5.1, Lemma5.2/full proof, pp7-8, count one squared exponent
per reflection pair, with multiplicity. The trace is real and smooth;
its origin bound is O(t^(-1/2)log(1/t)), and its infinity decay is
exponential, using the verified first pair and gap. Section6.4, p14,
states integral t^n W(t)dt=n! sigma_n. Theorem7.4 and Corollary7.5,
pp18-21, assert strict positivity of both N-by-N derivative blocks
at every t>0 under verification through T_N=20000N sqrt(1+log N);
N=3 instead permits height10000. The cited published verification
gives N<=30000000. Read the complete near-zero, interpolation-tail
and joining cases, Lemmas7.6-7.9 and equations(21)-(28).
This is a precise source import, not an independent arithmetic audit.
Underlying explicit-formula/counting estimates and published zero
verification were not revalidated. No large finite matrix was computed.

Suvrit Sra, *On some positivity properties of the Riemann Xi function*,
[hexagon2610.00584v1](https://hexagonmath.org/pdf/2610.00584v1),
LemmaC.1/full proof pp18-19 and PropositionC.2/full proof p19:
real smooth f on (0,infinity), and

    B_k(t)=[(-1)^(i+j) f^(i+j)(t)]_(0<=i,j<k) positive definite
    for every t>0

imply strict total positivity of f(x+y), x,y>0, through order k.
The proof uses initial Wronskians twice; the induction divides by a
strictly positive first function and integrates evaluation determinants
over intervals between distinct ordered points. It supplies ordered
minors, not directly an improper polynomial quadratic-form identity.
No non-strict analogue is imported: replacing positive definite by
positive semidefinite would need a separate argument. AppendixA's
all-order equivalences are not positivity premises here. This exact
PDF differs from the earlier Hub and author-v3 versions. The arXiv
identifier2610.00584 belongs to an unrelated Banach-space paper; use
the linked Hexagon source, not an arXiv substitution.

Giulio Ruzza, *Introduction to Random Matrix Theory, Riemann-Hilbert
problems, and Universality*,
[4May2022 notes](https://webpages.ciencias.ulisboa.pt/~gruzza/introRMT.pdf),
Lemma3.1.1, (3.1.2)-(3.1.9), pp27-28: reuse comparison1107's complete
proof inspection. Measurable complex functions are allowed, with every
entry product in L1. The bilinear identity has its factorial and no
complex conjugation. Peter J. Forrester,
[*Meet Andreief, Bordeaux1886, and Andreev, Kharkov1882-83*](https://arxiv.org/pdf/1806.10411v1),
(1.7), p2, Section2.2, p4, gives the same permutation proof; (2.4), p5,
was also inspected. Do not mistake that two-by-two identity for the
unwritten general two-stage application. Both composition stages need
their own L1 verification. Reproof of the identity is unnecessary.

[NIST DLMF5.12.1](https://dlmf.nist.gov/5.12.E1) gives Euler's beta
integral for Re(a),Re(b)>0;
[DLMF5.9.1](https://dlmf.nist.gov/5.9.E1) gives the gamma Laplace
integral for Re(nu)>0, mu>0, Re(z)>0, with principal powers.
These are normalization inputs, not an evaluated instance of M.

### Applicability obligations retained for the mathematical turn

1. Match squared exponents to L018/L024's alpha_j^2, including
   reflection pairs, off-line quadruples and multiplicities. Establish
   the positive-real-part bound and summable majorant from the actual
   local strip/rectangle and summability inputs; one must not posit
   real exponents. Source low-zero data are separate qualifications.
2. Check the entry integral on the whole positive quadrant. Use the
   cited beta/gamma formulas or the already stated heat moments to
   verify the index shift and every factorial. Keep M_ij=S_(i+j+2)
   as the proposed identity until proved; no coefficient-factorial
   deletion or row congruence has been justified by this review.
3. For each fixed d use k=d+1, with derivatives through 2d in B_k,
   and moments through S_(2d+2) in H_d. Apply only the strict source
   theorem at every positive time. A one-time finite block, scalar
   f>0, individual derivative signs, or PF of the density Theta is
   a different hypothesis. The shifted block of the all-order
   Stieltjes criterion is not a substitute for this conditional test.
4. For leading minors of every size up to k, apply Andreief twice
   on compact domains, keep orientations and normalization, and
   verify the ordinary Vandermonde signs of the monomial evaluation
   matrices. State whether working on full Cartesian powers or ordered
   chambers before fixing factorials. Prove convergence of the complete
   determinant integrands; entrywise convergence alone does not prove
   strict positivity in a limit. Retain a compact positive contribution
   if using strictness. Use symmetry and Sylvester's criterion only
   after all leading minors have been established. Finite spectral
   rank can defeat strictness and may not be ignored.

These are specified proof obligations, not new derivations. A correct
bridge could then be combined with the separately cited finite-block
input, with qualifications visible. It still cannot take d to infinity
from a fixed verification height. No source certificate is needed for
the first, conditional bridge; no unconditional actual H_d extension
is claimed now.

### Duplicates, failures and decision

L033/L038 already supply the actual first mixed determinant and its
positive certificate; L041 already certifies H_2. Degree one here is
a coefficient-matching discriminator, not a new finite-sign target.
No certificate replay or replacement lemma is warranted. The useful
uncompleted item is the general fixed-finite-order transfer, rather
than another finite theta quadrature. The bounded exact-phrase local
screen located no existing double-integral bridge; absence of a match
does not establish originality.

Reused assessment883's distinction between scalar trace signs and
signed composition minors. Its higher PF results concern reciprocal
densities, not this heat kernel. The connected-partition stop and
review1107's direct fan stop stay intact; a historical stop is not a
ban on this different conditional transform. No upper fan boundary,
global payment, independent all-degree sign or Xi realization has
thereby been supplied.

Queries included `heat trace inverse power Hankel Riemann`,
`Hankel two Laplace composition total positivity`,
`Sra Hankel Xi moments`, and `Hankel factorial total positivity
composition moments`. Searches returned unrelated Hankel-transform
and moment-lifting leads; none was used as theorem evidence. All
load-bearing passages above were inspected in primary sources or
reused with their already recorded proof scope. Shell downloads had
DNS failures; web retrieval supplied the relevant text, so no essential
source blocker remains. PDF screenshot calls returned no visible
images and are not counted as proof inspection; the full extracted
text passages supplied the cases described above.

**Decision.** SPECIALIZE a conditional finite-order bridge. This is
progress in source coverage, not a new positivity theorem, a complete
solution candidate, or progress beyond the checked sources. The
continuation test is exact entries plus strict leading-minor transfer
under the stated finite premise. Abandon that claimed specialization
if normalization fails or only an all-order RH-equivalent premise
justifies its sign; preserve any narrower true identity. The source
proof does supply a finite premise to assess, so a creative label is
unjustified. Mathlib matching coverage is not checked; the above
citations are mathematical references, not Lean coverage claims.

The ready mathematical target and its scope are in
[assessment1108](2026-11-16-finite-heat-laplace-specialization-1108.md).
It is newly written and awaits the supervisor's separate approval.
