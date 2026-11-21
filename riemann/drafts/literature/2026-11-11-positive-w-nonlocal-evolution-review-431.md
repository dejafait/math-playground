# Positive-w completed evolution: source scope and paid subtractions

TARGET: Assess whether Lagarias–Rains Theorem7.4 and Section7.2 yield a convergent nonlocal w-evolution law for G(w,t)=xi_Q(w,w/2+i*t) on [1,3/2] x [40,45], with the completion factor and crossed-pole terms explicit, and whether its integral is sign-controlled at G=G_t=0 without assuming a global sign of G.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step432 searched exact Lagarias/Rains/nonlocal/evolution/generator terms, inspected the primary statements and relevant proof cases below, and compared the named reviews421/425 and stops427/429/430. No inspected theorem supplies the positive-w completed evolution or its eventwise sign; failed searches establish no novelty.
SOURCE_EVIDENCE: Lagarias–Rains math/0104176v5 Theorem2.1/(2.9), Theorem2.2 caseIII/(2.12),(2.15) and proof(2.17)-(2.22)/pole remark, Lemma4.8 with proof, Proposition7.2/(7.12), Theorem7.4 with proof and Section7.2/Lemma7.5 with proof; https://arxiv.org/pdf/math/0104176v5 ; published Sections7.1-7.2 pp48-51 compared. Schilling arXiv1603.00251v2 Theorem6.8/(6.8)-(6.11), proof steps1-5 and its near/far bounds, Theorem5.9(d)/Remark5.10 first implication inspected; https://arxiv.org/pdf/1603.00251v2 . C999g's audited normalized completed representation reused.
COMPARISON: Lemma7.5's holomorphy is in s within u>0, |v|<u, not continuation of its convolution law to w>0. Theorem2.2 caseIII does cover the proposed centered rectangle, with both pole subtractions retained, and Lemma4.8 permits polynomial completion. These supply starting transforms, not a parameter-evolution identity. The standard nonlocal generator and global maximum principle give no automatic sign from the local equations G=G_t=0.
GAP: Still to derive: the positive-w completion-conjugated operator, compensation/remainder and its convergence, with normalization and moving center retained. No inspected source independently controls its eventwise signed residual. Event existence, curvature, nondegeneracy, multiplicities and global transport remain open.
REASON: Park citation-only positive-w sign transfer; replace the vague continuation-domain question by a bounded attempt starting from the source's already convergent caseIII transform, keeping every subtraction and completion derivative. Approve no sign or new identity in this literature turn; a separately nominated assessment needs later approval.
LITERATURE_REASON: The hypotheses change from the inspected negative-w semigroup and w=0 generator to a positive-w completed operator on the finite rectangle; the old generator-to-Li comparison does not assess this operator or its pole terms.
SCOPE: Completed literature-only comparison. SPECIALIZE records coverage of the starting transforms and the exact remaining derivation; it establishes no evolution identity, event sign or new lemma. The distinct bounded derivation is nominated in review432 for separate next-turn approval. No lemma or mathematical script was changed.

Main gap: L030–L032/C032a actual-Xi positivity. L966/L968 forcing,
L984(H) and C997s's capped E_n bridge are separate unresolved routes.
The intermediate target is source coverage for an actual positive-w
completed evolution law, with a test of what an event condition could
eliminate. If such a law exists with a controlled sign mechanism, it
could support a future local fold-orientation argument. Neither the
law nor the sign mechanism is asserted here.

Essential local inputs for the continuation are C999g and L018/L019,
with review421's exact-source notes and reviews425/429's scoped stops
as comparison evidence. C999f is not a premise. Read only the needed
source cases. No cross-notebook theorem is proposed. Full matching
Mathlib coverage remains unknown.

Discriminating test: locate an applicable convergent identity, or
identify the exact additional term/domain hypothesis a derivation
would have to pay. Inspect both the completion and the continuation
across the source's parameter domain; merely continuing the name of
an operator or a formal Fourier multiplier fails. For the sign question,
reject any argument replacing G=G_t=0 by global nonnegativity or a
global minimum. If no independently testable completion/pole budget
emerges, park this proposal; do not repeat negative-w positivity as
an answer to the positive-w event problem.

The prior stops are preserved: step422 concerns logarithmic Li-cost
transfer; steps427/429 leave the uniform G_w factor unpaid; step430
parks citation-only determinant signing. None is a global prohibition,
but none supplies the missing operator hypothesis. A successful source
comparison can nominate a separate bounded proof attempt. Creative
routing is not yet justified: the analytic operator domain and a
specific eventwise sign mechanism remain uncovered. Even a successful
local test would leave event existence, nondegeneracy, curvature,
multiplicities, initialization, all heights and global transport open.

## Completed source comparison — step432

Primary statements inspected: Lagarias–Rains v5 Proposition7.2/(7.12),
Theorem7.4/(7.15)-(7.16) with its proof, Section7.2/Lemma7.5 with
its proof, and Section7.3 Question4. Lemma7.5 explicitly assumes
u>0 and |v|<u, hence concerns w=-u<0. Its final explanation of
“holomorphic” concerns s within that cone; it is not a theorem of
operator continuation to positive w. Published Section7.2, pp50-51,
retains that domain. No positive-w generator law has been derived.

Theorem2.2 caseIII/(2.15), its proof (2.17)-(2.22), and the following
pole remark were read for the changed domain. They explicitly retain
both subtractions, theta(t^2)^w-1-t^(-w), when 0<Re(s)<Re(w).
The positive-w centered rectangle lies in that case. Lemma4.8's
polynomial Fourier inversion retains both subtractions as well.
These source facts identify a possible analytic continuation input;
they do not provide its parameter-evolution integral or its sign.

### Exact normalization and the remaining specialization

J. C. Lagarias and E. Rains, *On a Two-Variable Zeta Function for
Number Fields*, arXiv:math/0104176v5 (7 July 2002), is the primary
formula source linked above. Theorem7.4 is on PDF pp38-39;
Section7.2/Lemma7.5 and proof are on PDF pp39-40. The published
version, *Ann. Inst. Fourier*53(2003),1-68,
[Sections7.1-7.2, pp48-51](https://www.numdam.org/item/10.5802/aif.1939.pdf),
retains the strict cone. Published text extraction loses formulas;
the legible v5 statements fix those formulas. Screenshot retrieval
did not supply inspectable images; no conclusion relies on a preview.

Theorem7.4's characteristic function is

    f(r)=theta(1)*exp(-r/2)/theta(exp(2r)),
    M(x)=xi_Q(0,i*x)/pi
        =x^2*|1-2^(1+i*x/2)|^2*|zeta_hat(i*x/2)|^2/(8*pi),
    zeta_hat(s)=pi^(-s/2)*Gamma(s/2)*zeta(s).

At x=0 the displayed product uses its continuous removable value.
Here M is the finite Feller canonical density in Proposition7.2,
not the jump density with compensation omitted. The proof uses the
unshifted Theorem4.4, Theorem5.1 and the known zero-free line Re(s)=1;
it neither uses RH nor signs xi_Q at positive w. The w=0 statement
has already been assessed in review421; it is reused, not rederived.
The sine compensation and Fourier convention in (7.12) must be
matched before applying a modern generator theorem. In particular,
finite total mass of M is not a license to discard its x^(-2) factor.

The normalized semigroup density in (7.5) is

    P_u(t)=theta(1)^u*Z_Q(-u,-u/2+i*t)/(2*pi),  u>0.

Its positivity concerns Z_Q and negative w. G is the entire
completion xi_Q with its factor s(s-w)/(2w). The parameter derivative
of this factor and the moving evaluation s=w/2+i*t must both be
retained in any proposed evolution. Theorem2.1/(2.9) explicitly
contains -1/s+1/(s-w). Theorem2.2's proof turns these into the two
Heaviside subtractions; the following pole remark identifies them
as crossed-pole contributions. CaseIII applies since
0<Re(s)=w/2<w throughout the proposed rectangle. This is a direct
hypothesis check, not a newly derived evolution identity.

Lemma4.8 covers polynomial Fourier multipliers with the same
subtractions, sigma outside {0,Re(w)}, and |Im(z)|<pi/4. Its proof
uses Schwartz Fourier inversion and differentiation, not a
non-polynomial logarithmic multiplier. Consequently it does not
already justify the proposed nonlocal parameter operator. The
necessary extra work is now specified: differentiate the full
pole-compensated transform, match the generator conventions, and
prove the resulting operator and all extra terms converge. Entire
continuation of xi_Q alone cannot replace this argument. Section7.3
Question4 (PDF p44) leaves a zero-control question open; it supplies
no eventwise sign theorem.

### What the standard nonlocal theorem does and does not say

R. L. Schilling, *An Introduction to Lévy and Feller Processes*,
[arXiv:1603.00251v2,17 October2016](https://arxiv.org/pdf/1603.00251v2),
Theorem6.8/(6.8)-(6.10), printed pp39-41, states the generator
formula for a Lévy process on C_c^infinity(R^d). Its triplet has
real drift, positive semidefinite Gaussian matrix, and a nonnegative
jump measure satisfying integral min(1,|y|^2)nu(dy)<infinity. The
nonlocal integrand retains f(x+y)-f(x)-grad f(x).y*1_(|y|<1).
Proof steps1-5 establish the test-function domain, off-origin measure,
large-jump finiteness and the second-order small-jump bound. Both
near and far cases were inspected; the off-origin part explicitly
uses values away from x. This is a precise standard theorem input,
not a proof that G or its completion quotient lies in its domain.

Theorem5.9(d), printed pp33-34, states a GLOBAL maximum condition
for functions in the generator domain. Remark5.10's first implication
proves it using positivity and contraction of the whole semigroup.
Neither statement replaces the global comparison by f'(x)=0, or
by f(x)=f'(x)=0. Thus these sources do not sign the proposed
nonlocal expression merely from G=G_t=0. We do not assert an
actual-family counterexample, prove a new abstract obstruction, or
assume a global sign of G. Completion-conjugation, the sign of the
evolution parameter and extra pole terms would require their own
check even if a global comparison were available.

Theorem6.8 supplies the required standard generator terminology.
No further Feller reference is essential to nominate the bounded
identity attempt. Its source-domain matching and absolute convergence
are the attempt's conclusions to prove, not assumptions to import.
Full matching Mathlib coverage has not been checked and is unknown.

### Search evidence, outcome and continuation

Queries included `Lagarias Rains two-variable zeta theta infinitely
divisible Theorem 7.4 positive w convolution generator`,
`"Lagarias" "Rains" "generator" "convolution" theta positive`,
`"two-variable zeta" "evolution" nonlocal`,
`"Lagarias" "Rains" "nonlocal" zeta`, and
`"two-variable zeta" "generator" positive w`; standard-term search
located Schilling's primary notes. Nonmatching snippets and secondary
hits are not theorem evidence. No novelty is inferred.

Reused review421's generator-to-Li stop and review425's exact
collision-sign comparison. Read C999g and the scoped stops429/430;
stop429 records both uniform-factor attempts427/429. Narrow searches
of the named theta/generator reviews and event/theta failure records
found no completed matching operator. No other notebook was read.

Outcome NEGATIVE / LITERATURE / NOVELTY_UNCHECKED: the exact cone,
caseIII pole prescription and global-maximum hypothesis now close
the source-scope question and rule out the proposed automatic import.
They supply a bounded analytic test, not a sign estimate. This changes
the continuation from unspecific analytic continuation to the explicit
caseIII completion problem; it is not progress beyond known sources.
No mathematical exploration turn is spent or reset.

The new [review432](2026-11-11-pole-compensated-nonlocal-identity-review-432.md)
nominates one bounded derivation, requiring separate approval before
research. Continue only with an absolutely convergent identity whose
extra term is fully displayed; stop if a divergent/formal multiplier
or a global-sign premise is needed. Signing any residual remains a
later target. No justified creative sign mechanism has emerged: an
operator identity alone would be difficult specialization/development,
not a creative solution of the central positivity gap. C999g and
stops427/429/430 are preserved. PROOF and DAG remain unchanged.
