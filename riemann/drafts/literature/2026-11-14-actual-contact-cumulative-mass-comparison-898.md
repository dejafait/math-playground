# Actual contact forcing: cumulative signed-mass comparison nomination

TARGET: Assess whether C466b's actual-H first-contact forcing admits a signed cumulative-mass comparison using W(u)=integral_0^u H(t)V(t)dt and r(t)=-H'(t)/H(t), under the cited reciprocal-Xi structure and without global PF or complete monotonicity.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Step899 searched continuous signed stochastic order, cumulative comparison, Steffensen--Popoviciu and actual reciprocal-Xi logarithmic-slope terminology; inspected the primary statements below and the recorded886/889/891/898 stops. No applicable actual-contact cumulative estimate was found; no novelty inference.
SOURCE_EVIDENCE: Elgert2019 TU Wien thesis, DefinitionA.1.11/RemarkA.1.13 and LemmasA.1.15/A.1.18, printed pp190-193, including the continuous proof; Niculescu--Stanescu JMI11(2017)469-483, Definition1/Lemma1/Corollary2/Theorem1 and Abel-summation discussion pp469-472; Sra arXiv2611.02944v1, Lemmas2.1/2.2 and proofs pp3-5, compared with Hexagon2610.00584v1 and inherited assessment883. Exact links and qualifications below.
COMPARISON: Signed stochastic order requires the unproved cumulative dominance and a bounded monotone test; it does not supply either for actual V and r. The inspected Steffensen--Popoviciu statements require positive total mass, whereas C466b(4) has zero mass. Sra supplies interior derivative convergence, but no actual W estimate, r monotonicity, singular-endpoint comparison or strict forcing in the inspected cases.
GAP: Actual-specific location and integrated-mass control remain missing. No application yielding x_*D_m'(x_*)>0, no full Stieltjes endpoint justification, and no simultaneous-contact or propagation argument is established.
REASON: The inspected theorem hypotheses close automatic cumulative-order import under the current premises. Park this inference, retain W as optional bookkeeping, and nominate a separately reviewable integer-pole structural diagnostic; no new contact identity or estimate is derived.
SCOPE: Only the hypothetical actual-density rank-(m-1) contact in C466b, with D_j(x_*)>0 for j<m, D_m(x_*)=0 and D_m positive immediately to its left; arbitrary finite m, including beyond the reported finite-PF range. No replacement density or new finite-order certification.
LITERATURE_REASON: Cumulative signed-mass comparison and its actual-Xi structural hypotheses are not covered by ready assessment892 or the parked sign-variation assessment888; essential primary theorem comparison is missing.

The main gap remains actual-Xi all-degree algebraic-square positivity,
L030-L032/C032a. Essential inputs for the review are C466b's exact V and
contact identities, C466a's qualified actual-density imports, and
L018/L024 only as needed for normalization. C466d is an exclusion test
for generic scalar arguments, not an actual-density input. Review its
audit898 status before using that exclusion. No cross-notebook input is
proposed.

The proposed variables W and r only specify the source-search target.
Inherited primary locators include [Sra Hub v1](https://hub.valency.io/works/W_pr5z5huy_v1)
and [Sra author v3](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf);
neither was reopened during this nomination.
Do not claim that an integration-by-parts identity involving r is
already justified: C466b explicitly imports only H in C1 on the open
half-line, with a possible singularity at zero. Additional regularity,
endpoint terms and integrability required by any proposed comparison
must be identified in primary sources and checked against actual H.

Plausible downstream use: an applicable noncircular cumulative-mass
estimate might pay the signed forcing in C466b(5)/(7), whose desired
strict threshold is x_*D_m'(x_*)>0. It would still leave simultaneous
contacts, barriers, propagation and final L030 assembly unresolved.
This nomination supplies neither that estimate nor a forcing sign.

Bounded continuation test: search signed-measure comparison, cumulative
orders and logarithmic-slope criteria, then read primary hypotheses and
essential proof cases for the closest theorem. Approve a mathematical
target only if it isolates an independently checkable actual-Xi input
that distinguishes C466d and genuinely improves the unpaid force.
Stop this proposal if it merely rewrites C466b's identity, requires
global PF/complete monotonicity or another target-equivalent sign, or
uses only premises already satisfied by C466d. An unanswered search
does not establish impossibility or novelty.

Reuse the retained-zero stop886, bell-shape/variation stop889 and
finite-root stop891. They constrain their respective inferences, not
all future research. The narrow local duplicate check here does not
replace primary-source discovery or inspect other notebooks. Suggested
immediate routing is literature_comparison, standard/high. No justified
creative mathematical target is ready yet: an actual-specific estimate
and its essential source coverage are both missing. If this comparison
exposes one, the following turn may nominate proof_attempt/creative
with its precise bounded test and escalation justification.

Full matching Mathlib coverage has not been checked. No new lemma,
comparison theorem, source approval or mathematical script for this
nomination was written in audit898.

## Completed source comparison899, 14 November 2026

The preceding nomination is preserved as provenance. Its statements that
no primary comparison has been inspected are superseded here. This turn
reviews precisely the startup TARGET; no new mathematical result is
proved. The main gap and desired strict threshold are unchanged.

### Primary statements and relevant proof cases

Christiane Elgert, *Theory of Distribution-Constrained Optimization
Problems*, TU Wien dissertation, 2019,
[institutional primary PDF](https://repositum.tuwien.at/bitstream/20.500.12708/5381/2/Elgert%20Christiane%20-%202019%20-%20Theory%20of%20distribution-constrained%20optimization...pdf),
Appendix A.1, Definition A.1.11, Remark A.1.13, Lemma A.1.18,
printed pp190-193 (PDF pp200-203): equal-mass finite-total-variation
signed measures on a continuous interval are ordered by every upper
tail exactly when their integrals are ordered for all bounded measurable
increasing functions. Read both directions: indicator tests give the
necessary tails; the converse adds Jordan negative parts and normalizes
to probability measures. Lemma A.1.15 is the countable version, not the
continuous statement to substitute silently. The continuous proof retains
some discrete notation and a stray restricted-domain subtraction; no
displayed shorthand from that proof is imported as a new formula.
The comparison itself is a weak inequality with a bounded-test premise.

Constantin P. Niculescu and Marius M. Stanescu, *The
Steffensen--Popoviciu measures in the context of quasiconvex functions*,
J. Math. Inequal.11(2)(2017),469-483,
[publisher primary PDF](https://files.ele-math.com/articles/jmi-11-39.pdf),
doi:10.7153/jmi-11-39, Definition1, Lemma1, Corollary2 and Theorem1,
pp469-472: the measure has strictly positive total mass. Lemma1 tests
both endpoint hinge integrals; Corollary2 assumes an integrable signed
density whose cumulative integrals lie between zero and its positive
total mass. Theorem1 is Jensen's inequality for that class and divides
by the total mass. Read the discrete Abel-summation implication and
the stated absolutely-continuous counterpart; Lemma1/Theorem1 refer to
Niculescu--Persson for full proofs, which were not reopened. The
positive-mass hypotheses alone exclude direct application to C466b(4).

Suvrit Sra, *On some positivity properties of the Riemann Xi function*,
[arXiv:2611.02944v1](https://arxiv.org/pdf/2611.02944v1), 53-page
primary version, Section2.1 Lemma2.1 and Section2.2 Lemma2.2, pp3-5,
and [Hexagon2610.00584v1](https://hexagonmath.org/pdf/2610.00584v1),
25-page version, same lemmas pp3-5: read the product/convergence proof
and retained-zero proof, including the small-phase nonnegative case
and the delayed-negative-tail estimate. The former states local
absolute convergence of H and all its derivative series in Re(t)>0.
The latter gives positivity of H and -H', with a retained-zero bound
for 100<=U<=the version's verified height. Neither inspected statement
asserts monotonicity of -H'/H or a contact-specific cumulative inequality.
These are matching supporting inputs, not a new PF theorem or source audit.

### Applicability and the decisive difference

C466b(4) is already a zero-total-mass statement for the signed density
H(t)V(t), and its proof supplies absolute integrability. This meets
the mass/finiteness portion of the signed-order theorem. Its remaining
dominance hypothesis is a condition on all partial masses, exactly
the information not supplied by (4). Total cancellation is not that
condition. Neither C466a's boundary initialization nor C466b's finite
cofactor premises establish it. The signed-order theorem supplies no
actual-Xi estimate of these partial masses.

Moreover, C466b imports only interior C1 for H; the inspected Sra
derivative convergence provides a legitimate source for later interior
higher-regularity work. This does not settle boundedness/monotonicity
of r at the singular endpoint, variation there, any boundary product
involving W, or absolute integrability against a putative dr. No
integration-by-parts identity for r and W is asserted or approved here.
Working on [eta,x_*] would still require retaining its boundary terms,
its generally nonzero truncated mass, and a justified eta->0 limit.
The existing C466b endpoint argument controls its own H,V pairing;
it must not be relabeled as a proof for a differentiated quotient.

Even after a weak comparison were applicable, its weak conclusion
would not by itself give the strict inward forcing needed to contradict
a first contact. A separate strictness condition or local barrier
would remain. For the positive-mass Jensen alternative, normalizing
the zero-mass contact measure is unavailable. Adding an atom or
discarding one Jordan part would be a different measure with extra
terms to pay; no such modification is justified here.

The finite source PF conclusion and complete-monotonicity equivalence
remain as qualified in assessment883/C466a. Neither is an arbitrary-order
repair. C466d continues to rule out universal forcing from its scalar
premises. No theorem found here uses an independently verified actual
structural input to distinguish that model and improve the force.
This fails the startup continuation test for automatic cumulative
comparison; it does not prove that every future cumulative estimate
is impossible or that actual W has either sign.

### Search, duplicates, source limits and outcome

Queries included `signed measures cumulative integral order decreasing
function integration by parts stochastic dominance theorem`,
`signed measures first order increasing stochastic dominance theorem
integral`, `Steffensen signed measure monotonic function`,
`Levin--Stechkin theorem`, `self decomposable density canonical function
logarithmic derivative completely monotone Riemann xi`, `Sra Xi
cumulative density`, and `Volterra cumulative Polya density determinant`.
Search snippets are discovery only; the primary PDFs above were read.

Marshall--Olkin--Arnold, Chapter17 A.2, p639, is an unread continuous
comparison lead: its PDF repeatedly timed out, so its search excerpt
is not counted as inspected theorem coverage. Levin--Stechkin's original
paper was not inspected or imported. The Elgert and publisher sources
make these access failures nonessential to this comparison.
Hub v1 timed out; the author-v3 PDF failed to open. The author homepage
identified the correct arXiv locator, which supplied the full primary
text. A discovery service's suggested arXiv2611.00809 instead resolved
to an unrelated interpolation paper and is explicitly excluded.
No silently changed source version is used for the inherited C466a/b
imports, and no new finite-PF audit is claimed.

Local reuse: C466a/b statements and relevant proofs, C466d's audited
statement, assessments883/888, stop records886/889/891/898, and the
distinct Li-cumulative assessment200/201 were inspected. Narrow
November14 contact searches found no matching actual-W estimate.
No cross-notebook input. Full matching Mathlib coverage is unchecked;
ordinary integration support would not establish the missing sign.

Outcome: NEGATIVE source-applicability result, literature-only and
NOVELTY_UNCHECKED. The evidence is the continuous theorem's unpaid
dominance/bounded-test premises and the positive-mass mismatch of the
Jensen alternative. This changes the route: park automatic cumulative
import rather than spend a mathematical turn deriving another identity.
No lemma, script, new inequality or RH progress beyond the cited sources
is asserted. PROOF.md and DAG.md need no change.

The next nomination in assessment899 isolates integer pole multiplicity,
which C466d's noninteger gamma factor does not test. It is an independent
fixed-law diagnostic, not an actual-Xi substitute or an approved new
mathematical attempt. Its essential literature gate remains open.
