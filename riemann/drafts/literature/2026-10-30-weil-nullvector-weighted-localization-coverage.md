# Nullvector-weighted localization: completed source comparison

TARGET: Assess whether nullvector-weighted localization with bounded spatial multipliers can compare L522's prime slopes for L516's full signed kernel, without a sign assumption or division by the nullvector.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the narrow nodal/transport assessments and their recorded stops; searched nonlocal IMS localization, signed kernels, ground-state representation, sign-changing Picone identities and Weil nullvector multipliers. Read the primary statements/proof cases listed below. No inspected source supplies the signed BV-slope comparison; this is a bounded scope exclusion, not a novelty or impossibility claim.
SOURCE_EVIDENCE: Fukushima--Oshima--Takeda second edition Theorem 1.4.2(ii), statement and proof p.28; Frank--Lieb--Seiringer arXiv:math/0610593v2 Lemmas 3.1/3.5, pp.8-9/12; Frank--Seiringer arXiv:0803.0503v2 Section 2.1, Assumption 2.1, Propositions 2.2-2.3, Remark 2.4 and relevant Section 2.4 proof, pp.5-6/10-11. Reused L522's already assessed two-sign BV theorem and the prior nodal assessment's qualified source comparisons.
COMPARISON: Bounded part-domain multipliers have standard domain coverage. Fractional IMS permits sign-changing inputs but gives static weighted overlaps and a bounded error, not the signed translation slopes in L522. The positive-reference/nonnegative-kernel ground-state theorem does not cover the stipulated full model. No source grants a full-form contraction, favorable sign, or singular-multiplier limit.
GAP: The requested nullvector-specific upper comparison S<=P-H remains unproved, as do any full-kernel slope-sensitive localization estimate and its admissible limiting family. Ordinary fixed-multiplier identities do not close this source gap. No full-form identity or mathematical no-go theorem is derived here.
REASON: The new primary comparison fails this nomination's continuation test: usable conclusions stop at domain closure/static localization or require an unavailable positive reference and nonnegative kernel. Park this implementation rather than schedule another generic transform calculation. EXPLORE records the completed bounded search; it does not approve a new inequality or a renamed L523/L524 test.
LITERATURE_REASON: At invocation the exact bounded-multiplier/BV-slope target was REVIEW_REQUIRED. This turn inspects its missing theorem/proof scope once; it does not refresh already adequate nodal or BV coverage for quota reasons.
SCOPE: Retain L515's actual killed smooth-core domain, L516's full signed model, L521/L522's continuous BV nullvector and prime limits, and L524's audited obstruction. Keep c=log(2pi), nu_rho, the signed pole, both prime shifts, all equality atoms, 0<a<A, ell>log(2), real normalization, nonzero left trace, excluded reflected-image collision and b>=0 only on the fixed interval. No H1, positivity of v, simplicity, larger-interval positivity or ell>log(6) is granted.

The original question and test below are preserved as the nomination.
The completed comparison and route decision follow it. No lemma or
mathematical script was written in this literature-only step.

The main gap remains actual-Xi all-degree positivity. The intermediate
question is whether the exact null equation can supply a useful
localization inequality involving the signed displacement slopes in
L522, beyond the two already recorded value/stationarity constraints.
Its plausible downstream use would be a nullvector-specific upper
comparison S<=P-H, and only subsequently a uniform O(lambda) version.
Those goals, trace vanishing, existence, full-Weil identification,
collars and Xi transfer are all unresolved.

The later literature-only step should search standard nonlocal
ground-state representation, localization and Picone terminology,
then inspect the relevant theorem hypotheses and proof cases. Reuse
[the nodal source comparison](2026-10-30-weil-nodal-nullvector-compression-coverage.md)
and its warning about pole-free transforms. An identity obtained by
dividing by a positive reference eigenfunction does not apply to an
unknown sign-changing v with possible zeros. Domain closure for the
reference form does not grant full-form contraction or a favorable
sign after the signed pole and atomic terms are restored.

The proposed distinction to assess is the use of bounded spatial
multipliers on the actual v together with the signed BV translation
observable, rather than a universal sign on arbitrary smooth packets
or a static two-nodal-part compression. This is a question for the
source review, not a claim that such a comparison exists. No formula
or limit is derived in this nomination. No cited source is being
independently reproved.

Continuation test: approve a later mathematical target only if the
review isolates a precise admissible test and a slope-sensitive
estimate whose sign or threshold can be checked with the full signed
kernel. If all applicable conclusions merely reproduce an overlap
identity, require a sign of v, drop the pole, assume the desired
trace bound or give a generic absolute estimate, park this proposed
implementation. Do not repeat L523/L524 with renamed variables.
The historical stops are not a global ban on arithmetic localization.

The listed input IDs are for the proposed scope, not a new DAG node.
L523 is comparison evidence only, not an audited input to a new
result. Mathlib matching for the proposed specialization is unchecked.
No cross-notebook theorem, new mathematical script or approval of
previously uncovered mathematics is included in this nomination.

## Inspected primary statements and essential proof cases

[Fukushima, Oshima and Takeda, *Dirichlet Forms and Symmetric Markov
Processes*, second revised edition, 2011, Theorem 1.4.2(ii), p.28](https://api.pageplace.de/preview/DT0400.9783110218091_A15362972/preview-9783110218091_A15362972.pdf)
states that bounded members of a Dirichlet-form domain have a product
in the domain, with the square-root energy bound in terms of their
supremum norms. Its proof uses (1.4.8) and domination of differences.
This extends the previously inspected lattice case to products.
Apply only to L515's stipulated reference part Dirichlet form: its
bounded vector and a compact smooth spatial multiplier meet the
stated hypotheses, as does the square of that multiplier. This is a
direct applicability check of a cited domain theorem, not a new
multiplier proof. L516 retains the same domain under the bounded
signed perturbation. The theorem gives no contraction or sign for
that perturbed energy, no operator-domain claim, and no estimate
uniform in multipliers with diverging gradients. Arbitrary bounded
measurable multipliers are outside this justified test class.

[Frank, Lieb and Seiringer, *Hardy--Lieb--Thirring inequalities for
fractional Schroedinger operators*, arXiv:math/0610593v2,
27 October 2006, Lemmas 3.1 and 3.5, pp.8-9 and 12](https://arxiv.org/pdf/math/0610593v2)
give the difference-kernel representation and the nonlocal IMS
formula. Lemma 3.5 assumes 0<s<min(1,d/2), Lipschitz functions whose
squares sum to one, and a compact smooth input. Its error operator
has kernel a_(s,d)|x-y|^(-d-2s) times the sum of squared multiplier
differences. No sign of the input is required. Read the full
statement and its stated reduction to Lemma 3.1; also read that
lemma's Plancherel and constant-evaluation proof. The error is a
bilinear overlap, not a nonnegative quadratic form merely because
its kernel is pointwise nonnegative. The source is fractional, not
the present logarithmic signed atomic form. It supplies neither a
literal full-form import nor a derivative-measure inequality.
Changing kernels, adding the pole/atoms, and passing to a moving
singular test would require a separate argument. Reproving the
fractional identity here would not address the missing estimate.

[Frank and Seiringer, *Non-linear ground state representations and
sharp Hardy inequalities*, arXiv:0803.0503v2, 14 November 2008,
Section 2, pp.5-6 and 10-11](https://arxiv.org/pdf/0803.0503v2)
assumes a symmetric nonnegative measurable kernel and a positive
measurable reference omega. Assumption 2.1 also requires symmetric
dominated regularizations and locally weak-L1 convergence of their
potentials. Proposition 2.3 requires p>=2 and finiteness of the
three indicated energies/potential integrals for compactly supported
u=omega times v; at p=2 it is an equality. The domain/graph extension
in Remark 2.4 keeps these hypotheses. Read Proposition 2.2's complete
symmetrization and limit proof: its scalar comparison uses the ratio
omega(y)/omega(x) in [0,1], and its integral step uses nonnegative
regularized kernels. The proof of Proposition 2.3 is explicitly
abbreviated by the authors, referring to the stronger scalar bound;
no independent proof audit is claimed. Unknown-sign nullvectors and
the full signed pole/atomic model do not meet this reference/kernel
scope. Positive off-diagonal prime coefficients do not repair the
retained signed continuous term. No division by the actual vector
or extension across its zeros is justified by this citation.

## Search record, slope comparison and decision

Queries used on 2026-10-30:

- `nonlocal IMS localization formula signed kernel eigenfunction ground state representation multiplier`
- `nonlocal Picone identity sign changing ground state representation eigenfunction bounded multiplier`
- `Frank Lieb Seiringer fractional IMS localization formula Lemma 3.1 kernel`
- `Frank Seiringer non linear ground state representations Proposition 2.3 positive kernel 2008`
- `"signed" "kernel" "localization" "IMS" nonlocal`
- `"Picone" "sign-changing" "nonlocal" identity`
- `"Weil" "nullvector" localization multiplier`

Search leads about nonlinear critical Hardy problems, graph
ground-state representations, and antisymmetric Picone identities
were not inspected at theorem level and are not imported or used
as evidence excluding those broader subjects. The primary cases
above suffice to evaluate the proposed standard IMS/positive-ground-
state implementation. No exhaustive literature or novelty claim is made.

The BV convergence already used in L522 permits continuous tests
against a finite signed derivative measure and both signs of the
translation increment. It supplies convergence and an absolute
variation bound, not a favorable signed correlation. Reuse that
assessment unchanged. No newly found source controls the specific
sum of d_n w_n times the two-shift signed derivative pairing in
L522 (1)/(4). In particular the inspected fixed-multiplier source
contains no bound at the required threshold S<=P-H, nor any error
proportional to lambda. Neither an unspecified bounded multiplier
nor an unproved shrinking family is an admissible remedy.

Thus the source-supported continuation test fails for this
implementation. Park ordinary nullvector-weighted spatial
localization as a sign mechanism. This does not show that all
arithmetic localization is impossible, that a special nullvector
cannot satisfy the desired estimate, or that the full signed
operator lacks another useful representation. L523's static stop,
L524's smooth-packet obstruction and the earlier pole-free transform
scope remain distinct evidence; none is promoted to an RH obstruction.

For a materially different continuation, only nominate a local
Green-potential correction of L518's first interior prime cusp.
Its existing raw-adjoint assessment explicitly excludes corrected
weights. The needed singular-source and boundary-pairing coverage
is therefore REVIEW_REQUIRED, not inherited from this IMS review.
No correction, cancellation, residual expansion or new inequality
has been derived. Existing renewal and raw-residual inputs may be
reused once the new scope is reviewed. Full matching Mathlib
coverage is unchecked, and no cross-notebook input is used.
