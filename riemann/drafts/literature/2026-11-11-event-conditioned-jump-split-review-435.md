# Event-conditioned jump split: completed source comparison

TARGET: Assess an event-conditioned curvature subtraction in C999h with fixed jump cutoff |y|=1 on [1,3/2] x [40,45], seeking a signed bound for the combined far-jump and pole correction that can determine G_w*G_tt without global positivity; compare the required fourth-order remainder and curvature control with stops427/429/430 before approving one bounded proof test.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step436 searched exact family/curvature/double-zero/jump/pole terms and standard Taylor/central-difference remainder terminology; inspected the primary statements and cases below. Reused reviews421/425/431/432 and checked C999g/C999h and stops427/429/430 narrowly. No matching inspected signed comparison; no novelty inference.
SOURCE_EVIDENCE: Lagarias–Rains math/0104176v5 Theorem5.1 and proof pp24–27, Lemma5.2/(5.2)–(5.6), Theorem7.4/(7.15)–(7.16) and proof pp38–39, Theorem7.9/(7.31) and full proof p43, https://arxiv.org/pdf/math/0104176v5 ; Folland Advanced Calculus 2nd ed author PDF Theorem2.55/(2.56) and proof pp85–86, Theorem2.58/(2.59) pp86–87, https://sites.math.washington.edu/~folland/AdvCalc24.pdf . Reuse review431's Schilling comparison; DLMF3.4(i) is a checked general-method lead, not an actual-family sign theorem.
COMPARISON: The standard remainder is absolute and derivative-dependent; exact canonical mass is not a cutoff mass or a signed convolution estimate. None of the inspected results pays the complete far-jump/pole residual relative to event curvature. Theorem5.1's logarithmic-theta Mellin transform does supply a narrower independently evaluable correction target; matching it to Q remains mathematical work.
GAP: No strict signed margin or relative fourth-order bound was obtained. The fixed-cutoff collision-sign proof test is not approved. Exact reduction of the complete Q is a source-covered intermediate specialization; the actual-family far-jump sign and eventwise curvature control remain independent gaps.
REASON: Finish this source-only review without converting convergence, nondegeneracy or Taylor regularity into positivity. Narrow the continuation to the full correction before considering a new signed mechanism; preserve the original split nomination and all stop evidence.
LITERATURE_REASON: Changed target from identity/convergence to event-conditioned sign: the essential uncovered input is a relative curvature/remainder comparison and a signed far-jump plus pole budget for the actual theta family.
SCOPE: Completed literature-only review of this single mechanism. EXPLORE records incomplete mathematical signing after a completed bounded source search; it does not approve the original sign attempt. No new identity, inequality, event search, lemma or mathematical script. The separate correction-only continuation requires next-turn approval.

## Original nomination retained

The main gap remains L030-L032/C032a actual-Xi positivity, with the
L966/L968 forcing and L984(H) gaps separate. A favorable local
collision sign would be a possible later transport input; it would
not establish initialization, other heights or global transport.

Essential inputs are C999h, its audited C999g normalization, inherited
L018/L019, and review425's fold convention. At a prospective event
require G=G_t=0, and for orientation also G_tt!=0 and G_w!=0.
No such event is asserted to exist. C999f is not a premise, and no
cross-notebook input is proposed.

The candidate is to split the exact (3) at |y|=1, keeping the complete
Q alongside the far-jump term, and test a curvature subtraction of
the near-jump integrand. In this notation the prospective Taylor
subtraction from U(t+y)+U(t-y) is y^2*U_tt(t). The research question
is whether the actual theta family supplies a signed remaining
comparison, after paying a fourth-order remainder, strong enough to
determine the favorable product G_w*G_tt>0. No split identity,
fourth-order estimate, signed inequality or favorable direction for
an individual term is being established in this nomination.

Check exact statements under standard small-jump Taylor/Peano remainder
and nonlocal comparison terminology, then the primary hypotheses and
essential proof cases of any relevant actual-family estimate. Reuse
review431's compensation and global-maximum coverage. Do not infer a
global minimum from the two event equations. Compare narrowly with
stops427/429 (unsigned core remainders) and stop430 (missing positive
mixed-product weight). Retain the signed cancellation between the
far-jump contribution and Q; separate absolute estimates are acceptable
only if they meet a stated strict margin. No novelty follows from an
unsuccessful search.

Continuation test: identify a source-covered, independently estimable
signed component and a quantitative strict threshold that includes
the entire near-jump remainder and pole correction. Any use of relative
curvature must supply its lower bound, or avoid division by curvature.
Nondegeneracy, a formal Taylor expansion, or a renamed form of the
desired product is insufficient. Abandon this nomination if the
comparison needs the desired sign as an assumption, unproved global
positivity, or an uncontrolled relative fourth derivative. Preserve
the audited identity even if this mechanism fails.

This is a candidate for a later creative proof attempt only if that
source review yields an independently testable signed mechanism. Such
a later nomination must name its exact obstruction, bounded test and
decisive evidence; it is not authorized now. No justified creative
target is ready merely because the source count or schedule favors one.
Event existence, curvature, nondegeneracy, multiplicities, initialization,
other heights and transport remain open. Full matching Mathlib coverage
is unknown. STATUS remains IN_PROGRESS, without an RH candidate.

## Completed comparison — step436

The main gap, downstream use and event convention above are unchanged.
Read the entire C999h proof, C999g's relevant normalized representation,
the three named stops, and review425's event scope. Review421's
Theorem5.1 assessment was reused and its Mellin proof case checked
directly for the changed observable. There is no cross-notebook input.

### What the new source check actually covers

G. B. Folland, *Advanced Calculus*, second edition, author-hosted
[2024 PDF](https://sites.math.washington.edu/~folland/AdvCalc24.pdf),
Theorem2.55/(2.56), pp85–86, assumes f in C^(k+1) on a real interval
and gives the degree-k Taylor remainder as

    R_(a,k)(h)=h^(k+1)/k! integral_0^1 (1-v)^k f^(k+1)(a+v*h)dv.

Its proof checks the fundamental-theorem case and repeated integration
by parts, including signed h. Taking k=3 needs C4 control on the
whole segment; it supplies neither a sign for f'''' nor a comparison
with f''(a). Theorem2.58/(2.59), pp86–87, instead controls a remainder
through variation of the highest retained derivative. It supplies no
numerical modulus of that variation for the theta family. Neither
theorem turns pointwise nonzero curvature into an effective lower
bound. These are imported calculus facts; no application producing a
new jump-split identity or estimate is made here.

NIST [DLMF3.4(i)](https://dlmf.nist.gov/3.4.i), version1.2.8,
equations3.4.1–3.4.3 and the paragraph referring second-derivative
formulas to Collatz, was inspected. It gives no actual-family signed
comparison. Collatz's tables and the small-jump approximation leads
were not read or used as theorem evidence. Folland supplies the
needed precise remainder theorem, so those leads are not essential
source blockers.

Lagarias–Rains [math/0104176v5](https://arxiv.org/pdf/math/0104176v5),
7 July2002, Theorem7.4/proof, pp38–39, gives the positive canonical
density and its normalization; Theorem7.9/(7.31), p43, gives

    integral_R M(y)dy=pi^2*theta(1)^8/8-1/2.

The latter proof uses polynomial Fourier inversion in negative w
and entire continuation of the convergent integral. This is total
canonical mass, not mass below the cutoff or a mixed signed integral.
Theorem5.1/proof, pp24–27, also gives

    xi_Q(0,s)=(s^2/2) integral_0^infinity log(theta(r^2))*r^s dr/r,
    Re(s)>0.

Its series evaluation requires Re(s)>2; its resulting zeta-product
identity continues to all s. The proposed evaluation s=w/2+i*t
lies in the Mellin domain, outside that series domain. Matching the
full transform to Q, including the rational term, is not done here.
The formula offers an independent correction input, not an event sign.

### Search, comparison and decision

Queries included `"Lagarias" "Rains" "theta" "curvature"`,
`"two-variable zeta" "zeros" "derivative"`,
`"two-variable zeta" "double zero" curvature`,
`"Lagarias" "Rains" "small" "jumps"`,
`"Lévy" "small jumps" "Taylor" "fourth" remainder`,
`"zeta" "pole" "small jumps"`, and standard central-difference and
integral-remainder searches. No inspected source provides the required
combined signed budget. Search hits, numerical departure discussions
and unread references are not proofs of such a bound or of novelty.

Stops427/429 discard cancellation in different uniform-factor
enclosures. A near-jump Taylor bound would still discard cancellation
in its remainder; its acceptability must be tested against a proved
strict margin. Stop430 cannot supply that margin through a square
replacement. Review431 already excludes a local-event maximum-principle
import. None is a global prohibition of the new split.

No signed margin, curvature lower bound or fourth-derivative comparison
was established. Thus the original sign nomination has not passed
its continuation test. Park it pending a specific independently
controlled signed component; do not repeat the same source search or
approve a formal Taylor split as a creative advance. Exact treatment
of Q is a narrower useful input because its pole cancellation must
be preserved in any future far-jump budget.

Outcome EXPLORATION / LITERATURE / NOVELTY_UNCHECKED: new bounded source
comparison and a narrower source-covered continuation, with no signed
mathematical result. No calculation budget is spent or reset. The
[correction-only assessment](2026-11-11-complete-pole-correction-mellin-review-436.md)
nominates one specialization for separate approval. Original central
positivity, far-jump, curvature and transport gaps remain open.
