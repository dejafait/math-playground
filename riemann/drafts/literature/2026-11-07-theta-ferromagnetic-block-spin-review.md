# Actual-theta ferromagnetic block-spin representation — completed source review

TARGET: Assess whether Griffiths-Simon ferromagnetic block-spin approximation supplies a noncircular construction of the even actual-theta law K(|u|)/(2M_0), requiring an explicit finite-spin construction and compact-complex Laplace convergence criterion before nominating any mathematical test.
CHECKED: 2026-11-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Step97 checked exact author/class names and local ferromagnetic/GHS/partition stops, searched Griffiths-Simon theta realization and finite-quartic marginal tails, and compared three mechanisms below. No adequate actual-theta construction was found; this bounded search establishes no novelty or nonexistence.
SOURCE_EVIDENCE: Newly inspected Simon-Griffiths CMP33(1973),145-164, Section2 definitions, Theorem1 with Lemmas1-3/full proof pp147-151, Theorem3/full proof and Lemma4 pp151-152, Theorem4/full proof pp152-153; readable primary PDF and images. Aizenman arXiv:2112.04248v3 Section9.1 Definition9.1/(9.1)-(9.7) and ensuing construction discussion inspected. Reused Newman1975 Theorem1 coverage from the November5 post-Favard assessment; no new Newman proof claim.
COMPARISON: The explicit quartic construction is independent of a single-site zero assumption, but no inspected result constructs the actual theta law. Strong approximation includes uniform tail control; the weak-limit GS definition is not itself an approximation algorithm or compact-complex convergence proof. Three scopes are distinguished below.
GAP: Actual-theta representation and approximation-level complex-transform control remain unproved. No sufficient density-only criterion matching K was found. The finite-quartic marginal tail discriminator nominated separately is unproved and does not cover dimension-growing limits.
REASON: Finish the one construction comparison and park unparameterized GS realization. Select an independently testable finite-dimensional quartic marginal tail question, rather than another model-fitting, L876 or four-copy access campaign. No new mathematical result or impossibility theorem is claimed.
SCOPE: Completed literature-only assessment. No spin fitting, moment calculation, new lemma, mathematical script or derivation. The new continuation assessment needs separate approval next turn.
LITERATURE_REASON: At invocation the proposed measure-construction mechanism lay outside ready operator and partition/GHS coverage; essential primary hypotheses were unread. This turn completes that specific source comparison.

## Completed comparison — 7 November 2026, step97

Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
Intermediate source target: an explicit ferromagnetic approximation of
the even density K(|u|)/(2M_0), independently of its zeros. Downstream:
an applicable Lee-Yang limit could supply zero location. Continue only
with an actual construction and sufficient transform control. That test
was not met. Outcome EXPLORATION: source scope is clarified, but no
construction or new obstruction is proved. STATUS remains IN_PROGRESS.

### Primary evidence and exact scope

B. Simon and R. B. Griffiths, *The (phi^4)_2 Field Theory as a Classical
Ising Model*, Commun. Math. Phys.33(1973),145-164,
[author PDF](https://math.caltech.edu/SimonPapers/47.pdf), Section2:
pp147-148 define pair-spin laws (nonnegative couplings), mesh densities,
and strong limits: mesh tends to zero, pointwise convergence, and for
each k>0 a uniform bound D_k exp(-k x^2). Theorem1 constructs
exp(-a x^4-b x^2), a>0, b real. Its proof, pp149-151, uses Stirling,
binomial entropy/quadratic cancellation, mesh N^(-3/4), and a global
quartic envelope. For a=1/12 the Hamiltonian is
(b N^(-3/2)-1/(2N))(sum sigma_i)^2, ferromagnetic eventually.
Theorem3, pp151-152, uses finitely many such site limits, positive
continuous pair couplings (source wording), zero field, and fields
h_i=0 or Re(h_i)>0. Dominated
compact-complex convergence and Lemma4's zero-free limit principle
(on the nonvanishing domain, normalization excluding zero) transfer
Lee-Yang nonvanishing. Theorem4, pp152-153, disproves general even
sextic-potential extension via a three-atom limiting law; four-body
interactions do not repair the general Lee-Yang conclusion.
All relevant proof cases were read; this is comparison, not reproof.

M. Aizenman, *A geometric perspective on the scaling limits of critical
Ising and phi^4_d models*,
[arXiv:2112.04248v3](https://arxiv.org/html/2112.04248v3), revised
3October2022, Section9.1, Definition9.1/(9.1)-(9.7): records the GS
class through finite weighted-spin representations or weak limits with
an exp(|phi|^alpha) moment for some alpha>2. Subsequent paragraphs
describe quartic block construction and finite decorated graphs. This
is a representation hypothesis, not a density criterion for an arbitrary
rapidly decreasing even law. The HTML's b_j/alpha_j notation mismatch
is not used to extend the class; no conclusion rests on unspecified
weight signs. A tail property of the limit alone is not taken as uniform
integrability of approximants. The original strong theorem above is
the inspected source for compact-complex convergence.

### Three mechanisms compared; one different bounded target

1. One critical mean-field block: Theorem1 specifies quartic densities.
   No equality to the actual K law is supplied. Arbitrary potential
   approximation with ferromagnetic pair couplings is not justified.
   Park the automatic import.
2. General independent Lee-Yang sites: reuse
   `2026-11-05-post-favard-theta-mechanism-discovery.md`, Newman CMP41
   (1975),1-9, (1.1)/Theorem1. Evenness, all quadratic exponential moments
   and independently imaginary-zero single-site Laplace transforms are
   essential. Choosing the theta law as that site assumes the missing
   property. The November6 GHS source stop concerns a different observable
   and remains parked without retrieval retry.
3. A finite graph of quartic sites with a nonnegative linear observable:
   this gives a specified sufficient model class but no theta identity.
   Before hidden-site fitting, test whether its interval tails can even
   match L019. This is the selected new target, uncalculated this turn.

The proposed discriminator asks for a quartic-exponential lower bound
on P(X in [t,t+1]) for each fixed model, to compare with L019's full-theta
tail estimate. A proof could exclude exact finite-quartic representations;
a failure must identify the precise failed hypothesis or bound. Neither
outcome would exclude arbitrary GS weak limits: constants and dimension
need not stay controlled. No lower bound or mismatch is established here.

The new target has a separate assessment,
`2026-11-07-finite-quartic-marginal-tail-test.md`, written this turn.
It needs separate approval before mathematical invocation. This is an
elementary class discriminator, not a central creative attempt. The
blocker to such an attempt remains a specified actual-theta representation
or sufficient density criterion. Do not manufacture one or repeat
model-free discovery under another name.

### Searches, duplicates, access and limitations

Local exact-name and representation searches covered only this notebook's
assessments, ATTEMPTS and relevant lemma filenames/statements. Reused the
November5 post-Favard and November6 independent-arithmetic/GHS comparisons.
Read L019-L021 for K, M_0 and the complex transform; L025 and L030-L032
retain their supplied downstream roles, not newly proved premises.
L876 is a contrast and was not reaudited. No matching finite-quartic
marginal-tail test was found in the scoped searches.

External queries included `Griffiths Simon 1973 phi4 Ising approximation
theorem Lee Yang measures block spins`, `Griffiths-Simon tails measures`,
`Griffiths-Simon Riemann theta measure`, `ferromagnetic quartic marginal
tails`, `linear polynomial potential tails Gibbs measure marginal`, and
`theta quartic ferromagnetic representation`. Primary hypotheses and
proof cases, not snippets, support this comparison. A computing_rh/GitHub
summary was discovery only; its book and claimed theta/Polya results
were not read or imported. No novelty claim.

Euclid's attempted article URL was inaccessible; IntlPress returned403;
Springer exposed a subscription preview; shell retrieval failed DNS.
The author's original PDF was readable. Initial screenshot wrappers
returned references without image data; the connected search tool then
supplied readable images for printed pp148-153, including previously
timed-out p149. No essential display blocker remains for this scope.
No paid access, API key or four-copy retrieval retry occurred.

Full matching Mathlib coverage is unchecked, not claimed absent. No new
canonical theorem import is made in this literature-only turn. PROOF
and DAG stay unchanged because the mathematical argument does. The
original nomination below is retained as historical scope.

## Original nomination — preserved

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. L019/L021 specify the full kernel and its normalization;
L020 identifies the cosine transform, and L025 specifies the local
logarithmic coefficients. These are the essential input IDs for a
future applicability comparison, not new dependencies or a new graph.
L876 is a contrasting excluded fixed operator, not an input to any
prospective measure construction. No cross-notebook input is proposed.

The intermediate source target is an explicit route from this particular
even density to limits of ferromagnetic finite-spin laws. Its plausible
downstream use would be a zero-location theorem with an independently
verified arithmetic premise. Both the construction and its convergence
remain unproved, as does any all-degree conclusion for Xi.

Start by locating the exact Griffiths-Simon approximation definitions
and the applicable Lee-Yang preservation/limit theorem in primary
sources. Check whether their hypotheses can be verified from the actual
theta density rather than from its unknown zero location. Search the
notebook for the exact primary author/theorem names before retrieving
larger passages. Reuse any adequate coverage discovered there.

Continuation test: sources must expose a specified construction or a
sufficient condition directly on the density with a bounded, independent
verification step, including the convergence needed for complex fields.
Only then nominate that concrete mathematical subtarget for a later
turn. A finite moment fit, weak convergence without the required transform
control, or an assumed Lee-Yang single-site property is insufficient.
If the sources only rename the missing zero property, recover the old
scalar-GHS gap, or offer no independently checkable construction, park
this lead after this one source comparison. Do not retry the unread
four-copy displays as a substitute or claim that their access stop is a
global ban on ferromagnetic constructions.

This is not yet an approved creative attempt. If a new central mechanism
survives, its later proof_attempt/creative nomination must name the exact
theta premise, one bounded falsifier and the main-gap implication. If
none survives, record that result without manufacturing a lemma or
repeating L876. Mathlib coverage is unchecked, with no absence claim.
