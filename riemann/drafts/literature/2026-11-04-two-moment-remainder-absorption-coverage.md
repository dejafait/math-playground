# Two-moment remainder absorption: completed source comparison

TARGET: Assess a two-moment weighted Hardy-Poincare certificate for L751 at L=9log3 that bounds its negative residual by the complete transformed remainder, with no assumed positive complement or spectral gap.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step323 searched exact Weil/ground-state/Poincare and two-moment terms, nonlocal weighted Hardy-Poincare and linear-constraint inequalities; inspected the primary passages below and reused the four named local stops. No inspected source gives the required coefficient; search silence establishes no novelty.
SOURCE_EVIDENCE: Chen-Wang 1207.7140v1 Section3, Proposition3.2 and proof, Lemma3.4 and proof, Theorem3.6 and proof, printed pp17-22; Alessandrini-Morassi-Rosset math/0601667v2 Lemma2.1/Remark2.2 and proof pp2-3; teal-sea b09fa4dd RESULTS Section6. Reuse Frank-Seiringer 0803.0503v2 through the saved assessment and audited L751, not a fresh identity proof.
COMPARISON: General drift or projection theorems leave independently evaluated constants and hypotheses unpaid; the inspected Weil gap comparison is unresolved and its reported shortfalls are numerical. None supplies this sine's signed-potential absorption. An already proved compact neutral trial family permits a distinct one-sided obstruction test without assuming a positive complement.
GAP: The full-class absorption coefficient <=1 remains unproved. Only a finite-family obstruction screen is covered next; a nonnegative trial block cannot establish the full inequality or RH.
REASON: Essential source comparison is complete for the bounded obstruction test specified below, not for a claimed quantitative import. Reuse L750's existing admissible family unchanged, rather than inventing a reference, asserting endpoint control, or repeating the ground-state identity.
SCOPE: Fixed L=9log3 and h of L751; unchanged four-dimensional exact-neutral cutoff-sine kernel of L750 at T=8log3, embedded by its existing zero extension in (0,L). Every term of L751(3)-(4) remains. No unrestricted-support, positive-complement, spectral-gap or closure premise.
LITERATURE_REASON: Invocation-start coverage was REVIEW_REQUIRED for this changed quantitative absorption question; this is its first essential comparison, not extra browsing on a ready research target.
COVERED_TARGET: Rigorously test L751's remainder-absorption inequality at L=9log3 on L750's unchanged four-dimensional exact-neutral cutoff-sine space at T=8log3, using the full continuous remainder and every prime-power edge.

## Completed comparison, step323

This turn is literature-only: no inequality, matrix entry, sign or new
lemma is proved. The nomination below is preserved as its original
question, with its review status superseded only by the scope above.
The newly written covered continuation requires separate next-turn
approval; no dependent mathematical work is performed here.

### Primary sources and applicability

[Chen and Wang, *Weighted Poincare Inequalities for Nonlocal Dirichlet
Forms*, arXiv:1207.7140v1, 31 July 2012](https://arxiv.org/pdf/1207.7140v1),
Section3, printed pp17-22: read Proposition3.2, Lemma3.4, Theorem3.6
and their complete proofs. The setting is a regular symmetric jump
form on a probability space with the Section2 integrability conditions.
Theorem3.6 requires a smooth drift function phi>=1 in (3.36), a
positive smooth weight w, a truncated-generator bound
Lhat phi<=-w+b*1_B, integrability of phi/w, and finite local
inverse-kernel constants kappa_r from (3.42). For real bounded smooth
tests of mean zero it gives a weighted inequality. Its proof pays
the local term and tail to obtain C=2(1+b*kappa_r1), after choosing
a tail ratio <=1/2. Proposition3.2 alone retains the local error;
Lemma3.4 retains a local mean. These are not coefficient-one imports.
The notebook has no supplied drift data or bounds for these constants.
Its finite interval, vanishing sine endpoint weights, two prescribed
moments and atomic edges require a separate comparison. No theorem is
imported or extended to this setting. Theorems1.1/4.1 were inspected as
leads only; their full-space radial hypotheses do not remove these
obligations. No endpoint or complex-domain conclusion is inferred.

[Alessandrini, Morassi and Rosset, *The linear constraints in Poincare
and Korn type inequalities*, arXiv:math/0601667v2, 26 July2006](https://arxiv.org/pdf/math/0601667v2),
Lemma2.1 and Remark2.2, printed pp2-3, with complete short proof:
for Banach spaces X,Y, bounded L:X->Y with kernel X0, a bounded
projection P onto X0 and an existing estimate
||x-Px||<=K||Lx||, any bounded T:X->X0 fixing X0 gives the estimate
with factor (1+||T||)K. Remark2.2 permits the smaller factor
1+min(||T||,||T-P||). This accommodates changed constraints only
after a base coercive estimate and the appropriate projection have
been supplied. The source does not produce a jump-energy lower bound
or the required constant. No local derivative inequality is silently
substituted for this nonlocal remainder; no projection norm or base
constant has been evaluated here.

The primary research record [teal-sea, *Weil positivity propagation*,
RESULTS Section6, compiled 2 November2026, revision b09fa4dd](https://zeta.teal-sea.com/read/hunts/weil_propagation/theory/RESULTS.html)
was inspected directly, including the stated hypotheses, comparison
and correction. It uses an unknown pole-free Perron ground state,
not the prescribed sine. Its gap reformulation remains unresolved.
The reported comparison lower bounds 0.579 and 0.443 fall short of
reported requirements 5.8497 and 8.7819 at its two tested windows;
these are the authors' measurements, not imported rigorous bounds.
The claimed near-orthogonality evidence is explicitly withdrawn as
a precision artifact. Its windows, reference and constraints differ
from ours: neither its stop nor its numerical ratios prove a failure
of the present inequality. This overlaps the generic-gap mechanism
and supplies no independent quantitative absorption theorem.

Reuse the earlier neutral-supersolution assessment for
Frank-Seiringer's exact identity. L751 and its step322 audit already
check the continuous killing, atomic identity, complex factors and
compact-support domain. Reproving them would not answer this target.
Mathlib matching coverage for the constrained estimate is unchecked;
neither availability nor absence is asserted.

### Exact searches, duplicate and failure comparison

Queries included `nonlocal weighted Poincare inequality two constraints
signed potential Hardy optimal constant ground state representation`,
`Hardy Poincare inequality nonlocal Dirichlet forms Muckenhoupt
criterion signed potential constrained`, `Poincare constraints nonlocal
weighted inequality two orthogonality`, `nonlocal Poincare linear
constraints weighted`, `Weil Poincare ground state`, and `Weil two
moment Hardy`. Exact-term results did not provide a matching theorem.
Fractional/power-kernel, local weighted, three-constraint periodic
and finite-range results appeared as leads; beyond the explicit
passages above they are unread and are not applicability evidence.
No source-access blocker remains for this bounded trial test.

The four ATTEMPTS files named in the preserved nomination were read.
They reject a pointwise sine residual, static nodal slope inference,
an unpaid generic Schur complement, and one particular corrected
localization defect, respectively. None evaluates the present
absorption functional. L750's hypotheses, conclusion and exact-kernel
proof were also read. Its cutoff-sine tests are a ready admissible
family; its localization energies do not determine absorption.
Reusing this family is not reopening its failed localization rule.
No sibling notebook or cross-notebook theorem was used.

### Bounded continuation and decision test

Use L750's definitions unchanged: T=8log3, delta=T/40,
chi and phi_k=chi*sin(k*pi*x/T), k=1,...,6, and its exact moment
kernel. Its canonical proof gives the four basis functions with
k=3,5 corrected by phi_1 and k=4,6 corrected by phi_2 using the
exact M_+ ratios. Keep that T and the existing zero extensions;
do not rescale it to L or substitute a numerical nullspace. These
functions are already compactly supported inside (0,T), hence can
be tested inside (0,9log3); the same integrals define their moments.
Only this elementary domain inclusion is used, not a new family
construction or any claim about its absorption sign.

The proposed later calculation is the Hermitian restriction of
D_h(f)-integral R_-(x)|f(x)|^2 dx to this family, where D_h means
the sum of the two remainder terms in L751(3). This is a definition
of the test, not a computed criterion proving full-class positivity.
Retain h and R_h for the larger L=9log3 throughout, every shift
2<=n<19683 (including those with zero overlap), exterior killing
in R_h, and g=f/h. Exact neutrality and compact support are inherited
from L750; no division at h's endpoint zeros is permitted.

An upper enclosure strictly below zero for one nonzero exact-neutral
vector rejects this sufficient absorption inequality. It does not
reject neutral positivity, since positive residual terms were removed
from this sufficient test. A floating eigenvalue is only a screening
lead: a witness needs full outward error bounds for the continuous
kernel, the max in R_-, all finite edges and moment ratios. Existing
L750 certificates do not contain these new values. A rigorous positive
finite block proves only the restricted test; an interval crossing
zero is inconclusive. In either case, absent a violation or a materially
new quantitative mechanism, park the full absorption certificate
rather than increase modes or repeat generic-gap literature.

This is an ordinary finite-family obstruction calculation, not a
justified creative proof mechanism. Such a mechanism remains blocked
by missing quantitative full-class control, including endpoint and
complement errors. Other windows and actual-Xi mixed signs remain
unresolved. The outcome is EXPLORATION of source scope, with no claim
of a new mathematical input or progress beyond the sources checked.

## Preserved invocation-start nomination

## Exact proposed comparison

Use L751(3)-(4) and its audited notation. Write R_-(x)=max{-R_h(x),0}.
The prospective sufficient estimate is that the integral of
R_-(x)|f(x)|^2 is bounded by the sum of the two transformed remainder
terms displayed in L751(3), for every f in C_c^infinity(0,9log3)
with both M_+(f)=M_-(f)=0. In terms of the existing g=f/h, retain
exactly the constraints integral e^(+/-x/2)h(x)g(x)dx=0. This is
the proposed target, not an estimate established in step322. A known
bound with coefficient C<=1 would suffice for this absorption test;
C>1 or an unspecified positive gap would not.

The plausible downstream use is a fixed-window neutral certificate
which allows a signed residual. Other windows, unrestricted support,
the nonneutral complement and actual-Xi mixed positivity remain open.
Do not claim that the fixed-window target alone is an RH resolution.

Read exact primary hypotheses for weighted nonlocal Hardy-Poincare
inequalities with constraints and signed potentials. Compare stronger
results and known obstructions before any local derivation. Essential
issues are the exact two moments (not an interchangeable mean-zero
condition), endpoint behavior of h and R_-, k(u) near zero and at
infinity, the finite atomic shifts and complex tests. A theorem that
assumes the desired constrained positivity or an unknown positive
complement does not pay this estimate. A general characterization of
the optimal constant is not a quantitative bound.

Continuation test: approve a later bounded mathematical test only if
the comparison identifies an independently applicable quantitative
bound, a computable criterion with all complement errors paid, or a
specific admissible obstruction family for this absorption inequality.
If only a variational restatement of the missing sign is available,
park this certificate and nominate a different independently testable
target. Do not spend another turn reproducing the ground-state formula.
An obstruction to this sufficient estimate would not refute neutral
positivity. No such obstruction is asserted or tested here.

Reuse the comparison in
`2026-11-04-neutral-supersolution-certificate-coverage.md` for the
identity, including its documented overlap with teal-sea's unpriced
ground-state gap. Relevant stops are
`ATTEMPTS/2026-11-04-fixed-sine-pointwise-supersolution-stop.md`,
`ATTEMPTS/2026-10-30-weil-nodal-compression-slope-gap.md`,
`ATTEMPTS/2026-11-04-joint-energy-generic-source-scope-stop.md` and
`ATTEMPTS/2026-11-04-fixed-corrected-ims-propagation-stop.md`.
They stop particular inferences, not this untested constrained bound.
No cross-notebook input is needed. Mathlib matching coverage is unchecked.

There is not yet a justified creative proof invocation: the numerical
or analytic absorption mechanism and endpoint control are unspecified.
The source review must expose a genuine quantitative mechanism before
any such routing, rather than treating the new name as new evidence.
