# Conditional nullvector modulation — completed source comparison

TARGET: Assess source coverage for a support-preserving modulation test using cos(xi x)v and sin(xi x)v in L523's conditional model, to determine whether their combined complete-form energies can control S(v)<=P(v)-H(v).
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Compared the completed bounded-multiplier assessment, L517's two-packet modulation obstruction, L523's value/slope stop, L524's transport sign test and L529's killed/periodic distinction; searched unitary trace identities, logarithmic-form multipliers, signed cosine reconstruction and Weil modulation. Retrieved the primary statements and proof cases below. No matching signed-slope theorem was found in the sources inspected; no novelty or exhaustive-search claim.
SOURCE_EVIDENCE: Harrell--Stubbe arXiv:0903.0563v1 (3 March 2009), Theorems 2.1/2.2, Corollary 2.3, Theorem 2.4 with proofs, Section 3 (3.1)--(3.8) and Section 6 (6.1)--(6.4), printed pp.3--9,19--20; FOT second edition (2011), Theorem 1.4.2(ii) and product-domination proof, p.28. Reused the completed IMS/ground-state and L522 BV comparisons, plus L514's local finite-energy/core identification; no source manuscript is independently audited.
COMPARISON: Each fixed smooth modulation falls within the already screened bounded-multiplier subject. The new unitary source adds general conjugation identities with explicit operator-domain premises; its constant double commutator is specific to a Laplacian with a local potential. Neither this specialization nor the inspected IMS/BV results imports a signed displacement-slope upper bound for the full convolution model.
GAP: S<=P-H remains unproved. No inspected theorem provides the proposed frequency-family-to-slope bridge, controlled signed inversion, operator-domain invariance for the full family, or a uniform O(lambda) version. Reference form-domain coverage is distinct from these missing claims.
REASON: The saved continuation test fails: usable source conclusions stop at localization/conjugation identities and generic spectral inequalities. Park this modulation implementation before a calculation; the full null equation and other arithmetic mechanisms are not disproved. EXPLORE records the bounded search decision and does not approve a renamed multiplier calculation or a new lemma.
LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED for the frequency-family/signed-slope connection. This completes that changed-scope comparison, reusing ready domain/BV/IMS coverage rather than repeating L523's audit or browsing to satisfy a quota.
SCOPE: Retain L523's fixed conditional model, 0<a<A, ell=2a>log(2), full nu_rho, signed pole, both prime shifts and cutoff-equality atoms, semidefiniteness only on Q_(I_a), real normalized operator-domain nullvector, nonzero left trace and log(2)!=ell-d_n for every retained positive-weight atom. Source identification, BV and trace qualifications remain unchanged. The two proposed tests are real; no complex positivity assumption is introduced.

The original nomination below is retained as the question screened;
the completed source cases and decision follow it. No new mathematical
identity, inequality, lemma or mathematical script is derived here.

The main gap remains actual-Xi all-degree positivity. The proposed
intermediate target is to decide whether the family of complete-form
energies of cos(xi x)v and sin(xi x)v, as real xi varies, can yield
the missing upper bound S<=P-H. Its possible downstream use is
zero-flux exclusion at a conditional first nullvector. A bound for
positive-eigenvalue families, existence and Xi transfer would still
be missing even if that intermediate bound were obtained.

Essential local inputs would be L515's reference form domain,
L516's complete form and flux identity, L522's signed BV slope
formula, and L523's semidefinite nullvector setup. No cross-notebook
input is proposed. The completed L523 audit is canonical there;
this nomination contains no second dependency index.

The question differs from the stopped single nodal compression
because it proposes a parameterized family of support-preserving
tests. It also differs from the outward dilation, endpoint-fixed
transport and periodic-generator implementations. That difference
alone is not evidence that it escapes their mathematical obstructions.
The source review must compare L517's generic oscillatory-test stop
and L524's coefficient-sign failure explicitly before recommending
any calculation. Generic finite-rank identities are not a fallback:
the pole-resolvent stop already leaves the arithmetic numerator open.

Primary-source leads to inspect, not imported results: modulation
variational identities for translation-invariant forms with signed
bounded perturbations; finite-difference or double-commutator sum
rules on the actual logarithmic form domain; and any valid mechanism
recovering signed displacement slopes from the resulting parameter
family. The current FOT/BV coverage by itself supplies none of the
last implication. Do not silently assume operator-domain membership
of the proposed tests, H1 regularity, complete-form contraction,
a positive nullvector or a sign-definite transformed kernel.

Continuation test: approve a mathematical test only after identifying
its precise admissibility input and an explicit, falsifiable proposed
bridge to S<=P-H, with every signed term retained. If the sources
and comparison supply only overlap-value identities, generic
nonnegative energies or an uncontrolled signed inversion, record
that limitation and abandon this implementation before a calculation.
No derivative or sign conclusion has been derived in this nomination.
No existing exploration budget is reset by changing the test family.

Source comparison is the exact next task. If it identifies a justified
new arithmetic bridge, a later creative proof attempt should name
that bridge and its bounded falsification test in NEXT_ESCALATION;
the present nomination does not preapprove such an attempt. Full
matching Mathlib coverage is unchecked. There is no manuscript audit,
numerical evidence or candidate solution here.

## Inspected source cases and applicability

[Harrell--Stubbe, *Trace identities for commutators, with applications
to the distribution of eigenvalues*, arXiv:0903.0563v1](https://arxiv.org/pdf/0903.0563v1),
Theorems 2.1/2.2, require both G and G* to preserve Dom(H).
The first also assumes discrete spectrum. Theorem 2.2's proof splits
by a spectral projector and uses trace cyclicity; trace existence
must still be justified in an application. Theorem 2.4 uses a
separated spectral projector for its inequality. Section 6 rewrites
these identities for unitary conjugation. Section 3's phase multiplier
is applied to -Delta+V with local V and compatible boundary conditions;
(3.3)--(3.8) use its differential commutator. This source does not
establish the required slope comparison for signed convolution.
The v2 HTML guess returned 404; the available PDF identifies v1, so
there is no persistent source-access blocker.

[Fukushima--Oshima--Takeda, second revised edition, Theorem 1.4.2(ii),
p.28](https://api.pageplace.de/preview/DT0400.9783110218091_A15362972/preview-9783110218091_A15362972.pdf)
gives product closure for bounded Dirichlet-form domain members.
Its proof bounds differences using (1.4.8). Apply only to the
reference form. For a fixed frequency, use a smooth whole-line
cutoff equal to one on [-a,a] times the real sine/cosine, and the
bounded zero-extended v. L514's bounded-interval finite-energy/core
identification is the existing input relating that product to Q_(I_a).
The raw sine/cosine need not itself be in the killed part domain.
This is the standard applicability route, not a new multiplier proof
or a bound uniform in frequency. FOT grants no operator-domain
invariance or contraction for the signed perturbation.

Reuse [the bounded-multiplier comparison](2026-10-30-weil-nullvector-weighted-localization-coverage.md):
Frank--Lieb--Seiringer v2 Lemmas 3.1/3.5 give fractional IMS weighted
overlaps, while Frank--Seiringer v2 Assumption 2.1 and Propositions
2.2--2.3 retain a positive reference and nonnegative kernel. These
are not a full signed logarithmic-form slope theorem. Their exact
proof-case assessment need not be repeated. Likewise the ready
Galerne comparison in the L523 audit supplies signed BV convergence,
not an upper sign. No operator products or complex positivity are
assumed merely because the unitary source uses complex notation.

## Duplicate and threshold comparison

L517 explicitly uses cosine-modulated two-packet smooth tests and
obtains both signs for the first-prime slope, including arbitrarily
small form-norm perturbations of a positive-energy seed. Those are
not nullvectors. It blocks a universal form-energy or coefficient-sign
closure; it does not reject a genuinely eigen-equation-specific bound.
L523 separates static overlap values from the required signed slopes.
L524 supplies stationarity with a different displacement field and
no favorable coefficient sign. L529 concerns an unbounded periodic
derivative generator, whereas phase multiplication is a different
test. Do not infer that its obstruction bans phase multiplication,
or that support preservation proves every operator-domain premise.
The generic pole-resolvent stop independently leaves its arithmetic
numerator open.

The proposed new use of *all* frequencies is not imported by any
of these results. The inspected unitary statements contain no
reconstruction of L522's slope observable and no error measured
against P-H. A signed inversion, if available, would require its
own justified inequality; nonnegative test energies by themselves
are not that missing justification. No claim of logical independence,
counterexample to the nullvector bound, or new no-go theorem is made.

## Search record and route decision

Queries included `Harrell Stubbe trace identities unitary operators
commutators eigenvalue inequalities modulation nonlocal`,
`logarithmic Laplacian form domain multiplication Lipschitz function`,
`signed measure 1-cos nonnegative negative definite`,
`Weil positivity modulation trace formula`, and `nonlocal modulation
virial signed kernel eigenfunctions`. The exact primary passages
used are identified above. General logarithmic-Laplacian spectral
papers, Fourier positive-definiteness leads, nonlinear virial papers
and web claims about Weil modulation were not read at theorem level
and establish no exclusion or imported theorem here.

The continuation test therefore directs abandoning this implementation
before its algebra: there is admissibility coverage for weak fixed-
frequency tests, but no falsifiable, source-supported signed-slope
bridge. Reopening needs a specific new arithmetic comparison, not a
generic finite-conjugation identity. Mathematical exploration usage
is unchanged by this literature turn; no earlier stop is erased.
Full matching Mathlib coverage is unchecked. No canonical proof,
DAG edge, positivity range or RH status changes.
