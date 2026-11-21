# Continuous pair adjoint with weighted derivatives — nomination1045 / review1046

TARGET: Test whether the actual positive-h pair admits a bounded continuous adjoint with the fixed bump trace and absolutely integrable weighted derivatives through t=h=0.
CHECKED: 2026-11-16
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1046 searched continuous degenerate/characteristic transport, vanishing-density transport, weighted traces, divergence-measure product rules and Calogero adjoints; compared scoped November15–16 reverse records, review1042, review1022 and stop1043/audit1045. No inspected theorem supplies this exact continuous test or incompatibility; bounded searches do not establish novelty.
SOURCE_EVIDENCE: Reuse review1042's transport/network comparisons and C467m's Stokes/DCT imports. Fresh primary reads: Boyer, author manuscript of D.I.E.18(8)(2005),891–934, §2.3, Thms3.1/4.1 and indicated proof cases; Chen–Comi–Torres arXiv:1809.01248v3, Prop3.1, Thm3.2, Thm8.4/Cor8.1 and proofs; Arlotti–Banasiak–Lods arXiv:math/0610808v5, §1.1, Thm3.6's setup and Thm4.2/proof. Precise URLs, pages and applicability limits below.
COMPARISON: C467n's joint smooth jet is removed; C467m's fixed-test coefficient bounds do not control unknown singular derivatives. The new sources require normalized-velocity regularity, an invariant Lipschitz flow, unweighted Sobolev/BV control or specified trace approximation hypotheses not established here. Neither existence nor nonexistence in the nominated class follows.
GAP: Construct the exact bounded continuous actual-data pair test, prove all four complex-coefficient derivative products integrable and the complete arbitrary-rate cutoff identity, or prove incompatibility in precisely this class. These remain mathematical obligations, not an inaccessible-source blocker.
REASON: Separate literature-only review1046 completes the existing nomination's changed-regularity comparison with TARGET and proposed test unchanged. EXPLORE permits one bounded mathematical attempt; no new lemma, specialization, obstruction or cutoff-limit result is proved in this review.
SCOPE: Only the actual n=3 positive-h original pair with b=1/4096, X=1/256, H_*=1/128, raw time, B/beta/H/H0/F and common minus sign, under C467e/i/j/l/m qualifications. No modification of flow, connector, weight or time; no full chamber–pair–triangle family is assumed.

## Proposed bounded target, not a mathematical result

Let f be any fixed smooth real bump with 0<=f<=1, f=1 on [-b,b]
and support in (-2b,2b), as in C467n. Seek one common tau>0 and
a real phi with 0<=phi<=1 continuous on
[0,tau] x [-X,X] x [-1,1] x [0,H_*]. Require phi to be smooth
locally in the physical variables wherever t>0,h>0, including
neighborhood extensions in x,s at their fixed endpoints. Its
initial value is phi(0,x,s,h)=f(x)^2 f(x+h). Do not require a
time derivative at t=h=0, fixed-h smoothness down to t=0, or a
smooth extension after replacing t by sqrt(t).

On the positive-time positive-h interior impose the original undivided
equation dphi wedge Re(-Psi)=0. With C467m(4)'s unmodified complex
coefficients A,B_c,U,V in (t,x,s,h), require

    integral (|A phi_t| + |U phi_x| + |B_c phi_s| + |V phi_h|) < infinity

over that finite parameter box. Absolute values here control the
complex coefficient products; the adjoint equation uses their real
parts. At s=0 keep the original zero coefficients, without dividing.

The complete C467m(18) cutoff identity with this phi must have a
limit for arbitrary relative rates epsilon,eta down to zero, with
the actual one-sided inner trace at h=0 and no extra distribution
at t=h=0. Every other face is retained. No exterior zero-neighborhood
condition or chamber/triangle match is imposed in this pair-only
target; those remain additional obligations if a test exists.
Requiring the identity is part of the proposed test, not a theorem
derived from continuity or integrability in this nomination.

Continue only with an actual test meeting these conditions and a
complete limit proof, or a proved incompatibility in exactly this
weaker class. Failure of a characteristic estimate, a smoothness
ansatz or a sufficient integrability bound is inconclusive. Do not
infer existence from the failure of C467n's smooth-jet argument to
apply. This is materially different from retrying the stopped smooth
construction: it allows the joint derivatives used there to fail,
while posing a concrete integrability and trace test on one piece.

Main gap: L030–L032/C032a actual-Xi all-degree positivity. A positive
pair-only result could provide an admissible test class for later
matched transport; a negative one could stop that weaker local route.
Neither gives exterior flux payment, full assembly, realization,
other degrees or Xi signs.

Essential inputs to check in the source comparison and any later
attempt: C467e/audit1017, C467i/audit1025, C467j/audit1029,
C467l/audit1037, C467m/audit1041 and C467n/audit1045, carrying
C466z/audit988,C466/audit993,C466a qualifications. C467k is not a
direct input to this pair-only target; its triangle matches remain
unresolved future work. Preserve stops1000/1009/1023/1043 in their
own scopes. Full matching Mathlib coverage is unchecked.

At nomination1045 the next-turn task was literature_comparison,
standard/high, and the smooth-test gate did not approve this changed
class. The separate review1046 below supplies the source comparison;
the nomination itself performed no construction or source approval.

## Separate source comparison1046 — 16 November 2026

LITERATURE_REASON: The changed regularity class removes the time-zero
joint jet used by C467n. Review1042 explicitly excluded weaker tests;
weighted derivatives and arbitrary-rate traces were essential uncovered
hypotheses. This is their first source comparison, not another review
of an already-ready target. No mathematics is attempted here.

### Search and local overlap

Queries issued included `Boyer trace theorems well posedness initial
boundary value problem transport equation 2005 pdf`; `Chen Frid
divergence measure fields 1999 product rule continuous W1 1 Gauss Green
pdf`; `degenerate transport equation continuous solution vanishing
coefficient initial characteristic Cauchy data`; `"Trace theorems and
spatial continuity" pdf Boyer`; `"degenerate transport" "continuous"
"Cauchy" vanishing`; `"transport equation" "vanishing density"
continuous solution trace`; `"characteristic Cauchy problem" "first
order" "continuous" transport`; and `"Calogero" "adjoint" transport
collision`. Search results were leads, not theorem evidence.

Reused review1042's already-inspected Ambrosio–Crippa, Roggensack,
Egger–Philippi and Camilli–DeMaio–Tosin comparisons without repeating
those searches or calling them coverage of the present class. Read
C467m's actual hypotheses, (4)–(5), full mixed-minor formulas (11)–(16),
and tested identity (18)–(19); C467n's hypotheses and real ratios
(19)–(26); C467j/l's original connector/domain conventions; and
stop1043/audit1045. The local comparisons retain the original raw time,
orientation, coefficient zeros and common minus sign. C467n(25) is an
existing asymptotic statement, not a new calculation here; it does not
by itself decide the integral assumptions of a weak-transport theorem.

A targeted search of November15–16 reverse literature, attempts and
histories found review1022's weak-pullback and Phuc–Torres removability
comparisons, read only in their relevant paragraphs. They concern
extension of prescribed forms/fields, not construction of this unknown
adjoint. Neither that record nor review1042 nor the audited smooth stop
contains a solution of the present test. This is a bounded duplicate
comparison, not an assertion that none exists elsewhere. Prior
stops1000/1009/1023/1043 retain their original scopes.

### Primary statements and proof cases inspected

**Boyer.** Franck Boyer, *Trace theorems and spatial continuity properties
for the solutions of the transport equation*, Differential and Integral
Equations18(8)(2005),891–934, DOI10.57262/die/1356060150;
[author manuscript, §2.3, Thms3.1/4.1, manuscript pp5–14](https://www.math.univ-toulouse.fr/~fboyer/lib/exe/fetch.php?media=publications%3Afboyer_die.pdf).
The domain is bounded C2. For bounded data, (2.5) requires
v in L1_t W1,1_x, div v=0 and v·nu in Lalpha on the boundary,
alpha>1. Theorem4.1 gives a unique bounded renormalized solution
with prescribed bounded inflow data and source in L1_t Linfinity_x;
continuity is into finite Lq spaces, not joint pointwise continuity.
Theorem3.1 supplies flux-weighted traces. Read the shifted mollification
and commutator step pp6–7, boundary Cauchy argument pp9–10, and
parabolic maximum-principle/weak-limit and renormalized uniqueness cases
pp11–14. No normalized velocity satisfying these hypotheses, inflow
assignment, joint continuity, or four separate complex weighted
derivative bounds has been established for the nominated pair.

**Chen–Comi–Torres.** Gui-Qiang G. Chen, Giovanni E. Comi and Monica
Torres, *Cauchy Fluxes and Gauss-Green Formulas for Divergence-Measure
Fields over General Open Sets*,
[arXiv:1809.01248v3, 18January2019, §3 Prop3.1/Thm3.2; §8 Thm8.4/Cor8.1](https://arxiv.org/html/1809.01248v3).
DMp means an Lp field with Radon-measure divergence. Proposition3.1
assumes bounded continuous phi with distributional gradient in Lp',
p'=p/(p−1); p=infinity requires unweighted W1,1. Its proof mollifies
phi for p>1 and the field for p=1. Theorem3.2 requires bounded BV g
and a measure limit of mollified-field pairings with Dg; read both
proof steps. Theorem8.4 treats U compactly contained in the field
domain, with Lipschitz boundary, continuous phi and gradient in Lp';
its deformation sequences avoid a null exceptional set. Read its
area-formula proof and Cor8.1's continuous-field refinement/proof,
which retains the Sobolev assumption. These results neither construct
an adjoint nor establish the nomination's unweighted regularity,
ambient extension, or arbitrary independent rectangular-cutoff limit.
No BV or Sobolev upgrade from weighted integrability is claimed.

**Arlotti–Banasiak–Lods.** Luisa Arlotti, Jacek Banasiak and Bertrand
Lods, *A new approach to transport equations associated to a regular
field: trace results and well-posedness*,
[arXiv:math/0610808v5, 24January2009, §1.1, Thms3.6/4.2](https://arxiv.org/html/math/0610808v5).
The field is autonomous globally Lipschitz on RN and its flow preserves
the positive Radon measure mu. Theorem3.6 characterizes the maximal
L1 transport domain through almost-everywhere absolutely continuous
characteristic representatives. Read its mollification setup and
Lemma3.7's invariant-measure integrability proof. Theorem4.2 assumes
lambda>0 and L1 inflow/source data, gives the characteristic resolvent
with L1 outgoing trace, and is proved by separate source and boundary
parts, integration along paths and the zero-inflow resolvent uniqueness
argument; those cases were read. This does not provide pointwise joint
continuity or separate weighted coordinate derivatives. No invariant
Lipschitz-flow model meeting the original pair requirements is verified;
changing to such a model is not an authorized specialization.

Access: the initially guessed Boyer PDF URL failed; the exact author
PDF above resolved access and was read. The arXiv primary texts were
accessible. No persistent essential source blocker remains. Additional
search hits on degenerate scattering, generalized-function transport,
characteristic wave equations and quantum Calogero systems were not
read as theorem evidence and do not approve or refute this target.

### Decision, admissible use and bounded test

The strongest inspected conclusions are conditional characteristic
representations, renormalized weak solutions and product/normal-trace
identities under the hypotheses just recorded. There is no identified
matching theorem to import for this exact original pair. That comparison
supports EXPLORE, not a claim of originality or a prediction of success.
No standard theorem is reproved, and no result is imported with
unverified hypotheses. Existing C467m smooth Stokes and DCT citations
remain supporting tools on their stated domains only.

The next mathematical turn may attempt exactly the proposed test above:
one common positive tau, the unchanged bounded continuous trace,
positive-time/positive-h smoothness, original undivided real equation,
all four absolutely integrable complex weighted derivatives, and every
term of the complete one-sided cutoff identity for arbitrary relative
rates. Source-theorem trace conclusions do not replace its explicit
corner and face checks. No division at s=0 or the joint corner is
authorized; an interior division must be justified on its own domain.

Continue with a complete construction or a proved incompatibility in
this exact class. A failed sufficient bound or characteristic ansatz is
inconclusive; preserve that residual and require a materially different
input or refined test before repeating an unsuccessful mechanism.
The smooth stop cannot be extended merely by asserting hidden jet
regularity. A positive result supplies only a possible pair component;
triangle matches, exterior payment, full assembly, realization, all
degrees and Xi transfer remain independent gaps. Mathlib coverage of
the full continuous-adjoint or weighted-corner statement was not checked;
previous Stokes/DCT supporting coverage is not a matching theorem.

Review1046 approves the unchanged nomination for one proof attempt;
it derives no mathematical result and changes no canonical lemma or
script. Any later change to the target or its regularity/flow hypotheses
requires its own source comparison. PROOF.md and DAG.md are unchanged.
