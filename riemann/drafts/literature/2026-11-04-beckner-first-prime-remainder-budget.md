# First-prime budget from an exact uncertainty remainder — assessed scope

TARGET: Test whether Q_2(f)<=R_B(f)/2 for every complex globally neutral f in C_c^infinity(0,4log3), with R_B the centered one-dimensional Beckner logarithmic-uncertainty remainder.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step298 separately searched logarithmic uncertainty remainder/translation, weighted Hardy remainder/translation, Pitt finite-interval remainder and logarithmic-Hardy spectral bounds; exact queries and inspected versus unread leads are recorded below. No inspected theorem establishes the proposed arithmetic comparison; no novelty claim follows.
SOURCE_EVIDENCE: Beckner math/0701939v6 (31 July2009), Thm4/(12) printed p.5, Fourier convention p.2, Appendix (43)/(44) pp.20-22; Liao--Wang--Yang 2609.23593v1 (20 September2026), operator (1.1), Prop1.1, Thms1.2/1.3 pp.1-4 and endpoint construction p.7; local L743 (1) and L744 (6). Essential resource hypotheses and coefficient are accessible; no source theorem pays the signed delay.
COMPARISON: Beckner's unrestricted Schwartz identity covers the literal centered resource, including n=1 and complex tests, but gives no translation bound or half allocation. The recent logarithmic-Hardy spectral theorem assumes mu>-1 and cannot be used at its critical endpoint; its printed endpoint proof also has a suspect cutoff. L743's unweighted supremum and L745's carrier restriction do not decide this weighted question.
GAP: Prove or refute Q_2<=R_B/2 on precisely the globally neutral smooth class below. The arithmetic-to-resource estimate, full-energy spatial/digamma corrections, other prime powers, complementary signs and support propagation remain unresolved.
REASON: The separate bounded source comparison is complete enough for one mathematical test of the unchanged target. EXPLORE authorizes investigation of the uncovered difference, not a claim of originality or an import of the proposed inequality. No essential source blocker remains for the literal quadratic forms.
SCOPE: One bounded proof/counterexample attempt for the exact TARGET, with K=8, L=4log3, both global moments, complex tests, centered whole-line resource and coefficient 1/2 retained. Source identities may be cited; any new Fourier conversion, approximation or strict witness must be justified in that research step. No full-energy positivity or compact spectral certificate is preapproved.
LITERATURE_REASON: Step298 closes the separate gate required by step297's new arithmetic-versus-remainder observable. This is its first exact comparison, not repeat literature on a ready target; the following turn should use mathematics.

## Exact unproved question

Fix K=8, ell=log(3)/2, L=K ell=4log3, and a=log2.
Let f range over complex C_c^infinity(0,L), extended by zero to R,
with the two exact global constraints

    integral_0^L exp(x/2) f(x) dx = 0,
    integral_0^L exp(-x/2) f(x) dx = 0.

There are no cellwise constraints, carrier restriction, sign, parity,
nullvector, positivity or RH assumptions. Define the actual p=2
contribution in L743's Hermitian arithmetic normalization by

    Q_2(f) = (2log2/sqrt2) Re integral_a^L
                               f(x-a) conjugate(f(x)) dx.

Use centered coordinates h(y)=f(y+L/2), with the same zero extension,
and g(y)=sqrt(|y|) h(y). Specify the proposed positive resource by

    R_B(f) = (1/4) integral_(R x R)
             |g(y)-g(z)|^2 / (|y-z| sqrt(|y z|)) dy dz.

This is the one-dimensional right-hand resource of the cited Beckner
identity, not a new representation theorem. The null sets at y=0,
z=0 and y=z are interpreted through its nonnegative Lebesgue integral;
no individual singular value is assigned there. Step298 checked
applicability and the normalization of this literal expression,
including n=1 and complex functions, as recorded below. Reproof of the cited identity is
unnecessary unless a concrete suspect claim or changed hypothesis is
identified. No physical-frequency conversion or full-energy decomposition
is derived in this nomination.

The question is precisely

    Q_2(f) <= (1/2) R_B(f)                   for all such f.   (P)

The coefficient 1/2 is a proposed allocation: use at most half this
positive resource for the first prime, retaining the rest for other
terms. It is not asserted to be sharp, source-proved or sufficient
for full positivity. The norm and both sides are homogeneous of degree
two, so a later test may impose ||f||_2=1 without changing the question.
No inequality has been established or numerically tested this turn.

## Relevance, inputs and limits

The main gap is unconditional actual-Xi mixed positivity. L743 fixes
the signed arithmetic coefficient and L744 (6) fixes complete smooth
energy, including the pole and digamma multiplier. These are essential
input IDs. L745 is only comparison evidence: its restricted positive
span supplies no premise here. No conclusion of L742 is used.

If (P) held, it would pay one genuine negative arithmetic contribution
using a known positive resource, rather than the entire prime absolute
norm. This is useful only after translating the source identity into
L744's complete normalization with all spatial-logarithm and actual
symbol terms retained. It supplies no sign for those remaining terms,
other prime powers, complementary modes or growing supports. It does
not supply arbitrary-support induction or resolve RH. Fixed support
length L exceeds 4, the length corresponding to the parked paper60
radius-two claim, but that numerical claim is not an input or a
benchmark purportedly improved by a theorem here.

The new feature is a fixed explicit weighted quadratic resource; no
spatial localization multiplier is applied to an unknown nullvector,
and no favorable derivative of a signed kernel is assumed. Compare
`ATTEMPTS/2026-11-04-neutral-prime-only-rayleigh-saving-stop.md`,
`ATTEMPTS/2026-11-04-carrier-span-general-sign-scope-limit.md`, and the
October30 localization/Sonin comparisons without reopening them by name.
The old stops are scope evidence, not counterexamples to (P).

## Continuation or abandonment test

The completed bounded comparison used the terminology logarithmic
uncertainty remainder, weighted Hardy remainder, arithmetic translation
quadratic form, and finite-interval translation estimates. Reuse the
source statement already read; inspect further source proof cases only
where they settle n=1, complex applicability or a specific suspect step.
A known matching result should be imported with its precise constants;
otherwise record the uncovered difference before approving mathematics.
Search silence is not a novelty claim.

After separate source approval, one bounded mathematical test should
seek either a rigorous proof of (P) or a concrete exact-neutral smooth
family yielding Q_2(f)>R_B(f)/2. Numerical optimization is merely a lead
until the moments, integrals and strict inequality are certified.
A counterexample abandons this half-budget at this window, not every
remainder budget or RH. A generic L2 estimate, an uncontrolled center
cutoff, a trial-space-only bound or dropping the other energy terms
cannot count as proving the intended downstream sign. Preserve partial
reasoning; repeating an inconclusive test needs a refined mechanism.

A source-approved investigation of the remainder-to-shift comparison justifies
the next proof_attempt/creative: the obstruction is a discrete signed
arithmetic delay with no paid energy comparison on arbitrary neutral
tests; the decisive bounded test is (P) at this fixed window. The current
next action remains the exact TARGET, now source-ready under EXPLORE.
Matching Mathlib coverage is unchecked. No cross-notebook
input, derived theorem or complete candidate is proposed.

## Separate source comparison — step298, 4 November 2026

### Accessible known resource and applicability

Reuse step297's source assessment rather than reprove the uncertainty
identity. The targeted reread was for the nominated expression's exact
dimension, complex scope, singular weight and coefficient:
[Beckner, *Pitt's inequality and the fractional Laplacian: sharp error
estimates*, arXiv:math/0701939v6, Theorem4, (12), printed p.5](https://arxiv.org/pdf/math/0701939v6#page=5).
Its hypothesis is f in S(R^n); no real-valued, radial, parity,
mean-zero or vanishing-at-origin restriction is stated. The theorem
uses g=|x|^(n/2)f and coefficient Gamma(n/2)/(4 pi^(n/2)).
For n=1 this is exactly the nominated 1/4, since Gamma(1/2)=sqrt(pi).
The centered zero extension h of a compactly supported smooth f is
Schwartz. The theorem requires smoothness of h, not of sqrt(|y|)h(y)
at the origin. Thus no center cutoff is an extra premise of this import.
Both global moments merely restrict this source class.

The source Fourier convention is exp(+2 pi i x xi), printed p.2.
The left side of (12) is the sum of spatial and Fourier logarithmic
quadratic integrals minus D times the squared norm, with
D=psi(n/4)-log(pi). Its right side is the whole-space weighted
modulus-square integral. Keep that entire integral, including pairs
outside the support of h. A truncated square in the support is a
different quantity. This identity may supply an alternative evaluation
in a later attempt; the conversion to L744's exp(-i xi x) convention
and actual digamma symbol has not been carried out here.

The relevant proof check is Appendix (43), printed p.20, which states
the weighted formula for Schwartz functions and
0<alpha<min(2,n), 0<lambda<n-alpha, with modulus squares in its
symmetrization. These are compatible with complex functions; no
positivity of the function itself is used. Lemma15/(44) has a first
proof restricted to n>=3 and a second proof on pp.21-22 for the full
stated range. Its final Fourier interchange is explicitly
distributional. We import Theorem4 as stated, including its
alpha-to-zero argument, rather than treating these manipulations as
an independently audited proof. No new endpoint differentiation or
identity is proved in this literature turn.

### Stronger-looking spectral lead and its limits

The search found a genuinely relevant primary lead:
[Liao, Wang and Yang, *Dirichlet Eigenvalues for the Logarithmic-Hardy
operator*, arXiv:2609.23593v1, 20 September2026](https://arxiv.org/pdf/2609.23593v1).
Read the operator definition on p.1, Proposition1.1 and Theorems1.2/1.3
on pp.2-4, energy (1.6), and the endpoint construction on p.7.
Their operator has Fourier symbol 2log|xi| plus
2mu log(1/|x|). Theorem1.3 assumes a bounded Lipschitz domain
containing 0, N>=1 and mu>-1. Theorem1.2 states compact embedding
only for mu>-1 and claims noncompactness at mu=-1.
The sign of the spatial logarithm in Beckner's remainder corresponds
to that endpoint, not the open parameter range of the spectral theorem.
This is a source-scope comparison, not a derived spectral result for
the notebook's constrained form. No source theorem here includes
the actual translation at log2, its coefficient, or these two moments.

Do not import the endpoint claim as a verified obstruction either.
As printed on p.7, the proof chooses supp(eta) contained in B_1 and
defines psi_n(x)=eta(nx)(log(1/|x|))^(1/2) 1_{|x|>1/n};
the stated cutoff and indicator have disjoint nonzero regions, yet
the proof subsequently normalizes its mollification. This suspect
source construction prevents using that displayed sequence as a
certificate. Resolving that paper is unnecessary for the current
literal-form test; none of its spectral or endpoint conclusions is
an input. Its compactness statements supply neither (P) nor a
counterexample to (P). No repair or reproof is attempted.

### Bounded search, duplicates and disposition

Queries in this separate turn included:

- `Beckner logarithmic uncertainty remainder translation inequality ground state representation`
- `"logarithmic uncertainty" "remainder" "Hardy" Beckner`
- `"Beckner" "logarithmic" "translation" remainder`
- `"logarithmic uncertainty" "remainder" "shift"`
- `"Hardy remainder" "translation" logarithmic`
- `"logarithmic uncertainty" "translation" Beckner inequality finite interval`
- `"Beckner" "remainder" "shift" Pitt`
- `"logarithmic Laplacian" "Hardy" remainder eigenvalue interval`
- `"logarithmic uncertainty" "translation operator"`
- `"logarithmic uncertainty" "log 2" remainder`
- `"Pitt" "remainder" "finite interval" Beckner`
- `"Dirichlet Eigenvalues for the Logarithmic-Hardy operator"`

Search results also led to Frank--Seiringer's nonlinear ground-state
representation, Laptev--Weth's unperturbed logarithmic-Laplacian
spectrum, transformed uncertainty inequalities and a 2026
Faber--Krahn preprint with mu>-1. These were not read at theorem
level and are not imported or represented as disproving the target.
The two inspected primary comparisons above are sufficient for a
bounded EXPLORE decision, not an exhaustive literature or novelty claim.

Local reads checked L743's Hermitian coefficient and scope, L744's
complete smooth energy (6), step297's Beckner assessment, and the two
named ATTEMPTS records. Those stops concern an unweighted norm and a
restricted carrier span respectively. They do not address this fixed
weighted resource. No known local duplicate proves (P), and no archive
certificate is assumed. A generic translation L2 norm bound alone
would still require a quantitative lower comparison with this resource.

Decision: EXPLORE the unchanged (P) in one subsequent mathematical
attempt. The success/failure threshold and downstream limits above
remain exact. Any witness must retain both moments and certify the
strict inequality on an actual smooth function, with singular and
exterior contributions controlled. An unsuccessful search, finite
matrix preview or trial-space bound is inconclusive. No inequality,
new lemma, numerical experiment or mathematical script was produced
in step298. Outcome EXPLORATION; no mathematical-budget reset.
