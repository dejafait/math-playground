# Reverse-gradient actual-h full pullback phase — nomination1011

TARGET: Assess source coverage for a uniform full-pullback phase cone for the reverse-gradient actual-h three-particle flow on the existing chart and first lifetime.
CHECKED: 2026-11-15
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1012 searched reverse/negative antiholomorphic gradient flow, logarithmic repulsion, Vandermonde phase and Jacobian phase bounds; reused review989/990's exact/stronger discovery and failure comparison, and scoped C466/C467 actual-h searches. No matching uniform reverse cone or refutation was located; queries and inspected cases are below. No novelty inference.
SOURCE_EVIDENCE: Freshly inspected TNV arXiv1706.03822v2 Sections2.1-2.2 and AppendixB(B.1)-(B.5), https://arxiv.org/html/1706.03822v2 ; LY arXiv2101.05755v5 IV.1-IV.2 selected residual-phase/iteration/singular-limit passages, https://arxiv.org/html/2101.05755v5 , with published IV.A-IV.C coverage reused from ready989/approval990; FM arXiv2012.08468v1 (1.6)-(1.12), (3.16)/footnote12, https://arxiv.org/html/2012.08468v1 . Reuse ready992's Teschl and actual-B coverage; precise locators and limits are below.
COMPARISON: Local smooth-flow and real-parameter variational tools are available before the reversed lifetime; action phase, Gram identities and modified perfect-manifold constructions do not give the requested full-K_- cone. C466/audit993's inward barriers and C467d/audit1011's forward exclusion are direction-specific.
GAP: Establish or rigorously refute a uniform nonvanishing phase cone for the prescribed reversed full pullback, including arbitrarily small and unequal initial gaps. No reverse cone, lifetime bound, current extension or Xi transfer was established in this review.
REASON: Separate literature-only review1012 completes the changed-field source comparison without an essential access blocker. A bounded creative proof-or-refutation target is saved in ready1012 for separate next-turn approval; neither alternative is proved here.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED concerns reversal of the singular field; forward assessments do not cover its phase barriers. Reuse unchanged analytic and ODE coverage.

## Exact proposed target and its limits

Keep C466's actual normalized B, x=B'(1), real H_0,
H(z)=sum_j[B(1+z_j)-x(1+z_j)], g(z)=B'(1+z)-x,
F=Delta^2 exp(-H), n=3, R=1/4, a=1/16 and T_0=1/1920.
For distinct real u in I=(-a,a)^3, define a different raw field by

\[
 \dot Y_j=+2\sum_{\ell\ne j}
             \frac{Y_j-Y_\ell}{|Y_j-Y_\ell|^2}
             -\overline{g(Y_j)},\qquad Y(0,u)=iu.
\]

Its lifetime tau_-(u) is the first maximal lifetime in the original
open box minus the collision divisor. There is no restart or assigned
flow on an initial diagonal. For t<min(T_0,tau_-(u)) put

\[
 K_-(t,u)=-\frac{e^{H_0}}{\Delta(u)^2}F(Y(t,u))
             \det_{\mathbb C}[(1/i)\partial_{u_k}Y_j(t,u)].
\]

The proposed mathematical test is whether there is a uniform
alpha<pi/2 such that K_- is nonzero and admits |arg K_-|<=alpha
throughout this survivor domain, for arbitrary relative spacings.
These are definitions and an unproved target, not a sign claim.
The reverse lifetime, secant and matrix bounds are not identified
with their forward counterparts. In particular do not substitute
-t into C466's forward barrier without checking every hypothesis.

The source review should check standard reverse-gradient/Lefschetz
deformation results and known singular tangent/phase obstructions,
starting with primary hypotheses and the essential collision or
small-gap cases. Reuse ready external smooth-ODE and full-Jacobian
coverage where it actually applies. An unread lead is not coverage,
and neither a real-axis scalar model nor a modulus-square estimate
settles this complex determinant target. The existing density
qualifications remain in force; no RH assumption is permitted.

## Relevance, bounded test and possible routing

The main gap is L030–L032/C032a actual-Xi all-degree positivity.
A signed reverse deformation would test a local direction not covered
by C467d's audited forward capacity exclusion. Its first necessary
test is the full pullback phase above. A positive result would only
justify considering reverse complete-current and mass-balance coverage
later; none of those statements follows from a phase cone alone.

After adequate coverage, one bounded attempt would seek the uniform
cone on this fixed chart and horizon, or a rigorous sign loss/phase
escape in an explicit family of distinct initial triples. A failure
of a particular barrier is only a failure of that barrier. Retain
partial reasoning and do not repeat an unsuccessful attempt without
a changed mechanism or discriminating new input. Numerical trajectories
would be diagnostic only. This nomination proves neither alternative.

The immediate route is literature_comparison, standard/high. If the
comparison leaves this as a genuinely unresolved deformation mechanism,
the prospective mathematical route is proof_attempt/creative,
deep_research/max: the precise obstruction is possible singular
amplification of the full tangent phase under the reversed field,
which could defeat a direction intended to escape forward mass loss.
The fixed-domain uniform cone versus a rigorous sign-loss family is
the bounded test. If sources instead cover the sign or reduce it to
routine specialization, classify and route it accordingly. Current
source readiness does not authorize that mathematical turn.

No reverse-flow estimate, lemma, certificate or current theorem was
derived in step1011. Full matching Mathlib coverage has not been
checked. Stops961/968/979/1000/1009 and C467c's fixed-bump payment
are preserved. This target needs a separate source-review invocation.

## Completed source comparison1012 — 15 November 2026

The nomination above records the earlier uncovered status. This separate
review changes source readiness, without deriving reversed dynamics or
evaluating K_-. The main gap and exact proposed field remain unchanged.

### Discovery and primary cases

Fresh queries:

- reverse antiholomorphic gradient flow logarithmic singularity Jacobian residual phase Lefschetz thimble;
- Lefschetz thimble flow Jacobian phase singular fermion determinant gradient flow Tanizaki Nishimura Verbaarschot;
- repulsive complex logarithmic particle flow Jacobian phase Vandermonde;
- "holomorphic gradient flow" "reverse" "phase";
- "Lefschetz" "negative flow" "Jacobian";
- "Vandermonde" "gradient flow" "phase";
- "antiholomorphic gradient flow" "Lagrangian" Jacobian invertible;
- "reverse gradient" "Lefschetz" phase singularity;
- "logarithmic" "repulsive" "holomorphic gradient flow";
- "Lefschetz" "Jacobian phase" bound theorem.

Several narrow searches produced unrelated results or no adequate match.
Snippets are discovery only. This bounded search does not establish
novelty or absence from the literature. Reuse ready989/approval990 and
nomination988's completed general phase-cone/perfect-manifold discovery.
The changed direction is checked here.

Tanizaki, Nishimura and Verbaarschot, *Gradient flows without blow-up for
Lefschetz thimbles*, JHEP10(2017)100,
[arXiv:1706.03822v2, 27 September 2017](https://arxiv.org/html/1706.03822v2):
read Sections2.1-2.2, especially (4)-(7), (14), (21)-(23) and the
weight/Jacobian qualification, and AppendixB (B.1)-(B.5), printed p22
(HTML69-73). The real scalar collision example omits regular terms;
it gives no uniform complex three-particle estimate. The variational
tool requires a smooth nonsingular trajectory and real parameter
variations. Modified-metric completeness changes the field. Reuse
review989/990's fuller qualifications; neither completeness nor a
phase cone is imported.

Lawrence and Yamauchi, *Normalizing flows and the real-time sign
problem*, [Phys. Rev. D103(2021)114509, IV.A-IV.C, pp4-7](https://scoap3-prod-backend.s3.cern.ch/media/files/62831/10.1103/PhysRevD.103.114509.pdf):
reuse review989/990's published-version assessment. Freshly read
[arXiv:2101.05755v5, 24 May 2022, selected IV.1-IV.2 passages](https://arxiv.org/html/2101.05755v5),
including residual phase, effective-action iteration and the singular-limit caveat.
The stronger construction permits reparametrization and changes
effective action; global conclusions are conditional. It does not
settle the fixed raw reverse flow. Version labels are retained.

Fukuma and Matsumoto, *Worldvolume approach to the tempered Lefschetz
thimble method*,
[arXiv:2012.08468v1, 15 December 2020](https://arxiv.org/html/2012.08468v1):
read (1.6)-(1.12), the variational proof in footnote3, and (3.16)
with its complete footnote12 argument. Gram-matrix reality is a
supporting tangent-space identity; (1.11) retains a separate determinant
phase. Neither supplies an angular bound. This is the inspected
preprint version, not an identification of its equation numbers with
the later journal version.

### Applicability and nonimports

Reuse Teschl's author-hosted April2012 preliminary *Ordinary Differential
Equations and Dynamical Systems*, Lemma2.14/Corollary2.15, pp52-53,
Theorem3.9 p81 and Theorem6.1/proof pp189-190, as inspected in
[ready992](2026-11-14-actual-h-full-pullback-cone-audit-ready-992.md),
[primary book](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
These supply local existence, smooth dependence and continuation on
compact subsets of a smooth vector-field domain. Reversal does not
remove the divisor from that domain. No common lifetime or uniform
distance from the divisor follows.

For local flow tools, the negative of a holomorphic action is still
holomorphic on each nonsingular branch chart. Thus the cited differential
tools apply to the nominated reversed field on compact intervals
strictly before its own lifetime, with its imaginary initial plane
and real parameters. This is an applicability check, not a derived
reverse variational or phase formula. The source's identity initial
Jacobian must not replace the nominated initial derivative.
The weight in K_- stays F: interpreting the field using the negative
action does not authorize replacing F by its reciprocal or importing
a global integral identity for that negative action.

The mathematical attempt must check its complete fixed-time variational
system and signs. It may use C466/audit993 and C466z/audit988's
unchanged actual-B analytic bounds on the same disk; those bounds
assert nothing about the reversed trajectory. C466's secant cone,
Riccati barrier, projection invertibility and forward buffer do not
transfer. A geometric tangent-space identity also needs its initial-plane
and sign specialization. No general theorem above gives the full
target; none needs reproof. Full matching Mathlib coverage remains
not checked, not absent.

### Duplicates, failures and bounded decision

Scoped actual-h assessment/attempt searches found no existing reverse
cone. Read C466's hypotheses and direction-sensitive secant/matrix
ranges (9)-(20), and stop1009's audit1011 update. Reuse the explicit
duplicate comparison in nomination988/review989 for
stops927/932/941/947/948 and C466j/t; reread stop948's qualification.
Product contours, iid factorization, an unflowed marginal, free germs
and unproved smooth collision extension are different targets.
C467d excludes only its prescribed forward flow/cap/initial family.
None establishes a reverse cone or its failure.

EXPLORE permits one bounded creative attempt at the unchanged proposed
phase mechanism, with no essential source-access blocker. Its exact
mathematical target is in
[ready1012](2026-11-15-actual-h-reverse-flow-phase-ready-1012.md).
That newly written continuation needs separate approval next turn.
This is a source-scope decision, not mathematical progress beyond
the inspected literature.

Continue on a proof of the uniform cone or a rigorous actual
full-coefficient refutation; a failed barrier alone is inconclusive.
If inconclusive, preserve the obstruction and require a refined mechanism
or material new input before repetition. Current extension, initial
trace, mass payment, interfaces, all degrees and Xi transfer remain
independent. No lemma, mathematical script, certificate replay or
original mathematical derivation was made.
