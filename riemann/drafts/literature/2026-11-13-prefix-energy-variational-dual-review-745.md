# Finite dual energy certificates: source comparison746

TARGET: Assess a finite variational-dual lower certificate for the same 256 exponential energies in C998x's fixed Gram, using smooth test functions paired with the full Dh instead of sampling its density, while retaining exact d0 C(0), <Tg,h> and both projection corrections.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Comparison746 searched exponential-kernel H1 dual norms, finite signed-measure RKHS energy and variational lower bounds; inspected the primary statements and proof cases below. Scoped C998/remote-image/prefix duplicate checks found the existing derivative-measure identity and spectral-rule duals, not this physical test-space certificate. No novelty inference.
SOURCE_EVIDENCE: Sriperumbudur--Fukumizu--Lanckriet,JMLR12(2011),Lemma7/full proof p2407 and Proposition4 proof p2402; Novak--Ullrich--Wozniakowski--Zhang,arXiv1709.02568v1,(1) p2,K1,1 p3,Theorem1 p4 and finite-s proof pp6-11; Bauschke--Goebel--Lucet--Wang,SIAM J.Optim.19(2008),Section2(1)-(2) p767 and Proposition3.3(i) p769. Links and exact applicability below; C998u/audit726 and C998x retained.
COMPARISON: Primary RKHS embedding covers arbitrary finite signed Borel measures, including atoms, and identifies kernel energy with squared representer norm. The full-line H1 kernel and Hilbert quadratic conjugacy cover the general lower direction. They supply no fixed-h trial quality, signed Schur margin, numerical accuracy or affordable implementation.
GAP: Later specialize the kernel amplitude/rate normalization, finite test-space lower certificate and compact-source test pairing; then pay all full-h pairings,C(0),<Tg,h>,both projections,full K14/K7,numerical errors,precision,storage and work. No local dual formula or numerical value is derived in this literature turn.
REASON: Essential signed-measure and whole-line source coverage is now adequate for ONE standard-method preflight after separate approval. Citation alone cannot supply the actual finite comparison or ledger; direct-density stop745 remains intact.
LITERATURE_REASON: The technique changes from source-density quadrature and exponential sweeps to a finite variational lower certificate. The required norm/Green identity for signed finite measures with endpoint atoms is outside719/723/744's inspected statements.
SCOPE: Unchanged C998r real pair and C998s h=P0Uf, all512 modes,334 shifts,identity2187,full K14,exact P0 and exactly j=0,...,255. Only a sufficient-positive fixed complex-scalar Gram is proposed; no all-vector S3 conclusion or actual-negative inference.

## Completed source review746 — 13 November2026

This is literature-only local progress: the essential source blocker is
removed. It establishes no new lemma, trial estimate or positivity beyond
the sources checked. No lemmas/ or mathematical scripts/ are changed.

### Inspected primary statements and essential cases

1. Sriperumbudur, Fukumizu and Lanckriet, *Universality, Characteristic
   Kernels and RKHS Embedding of Measures*, JMLR12(2011),2389-2410,
   [published primary PDF](https://jmlr.org/papers/volume12/sriperumbudur11a/sriperumbudur11a.pdf).
   AppendixB Lemma7, p2407, assumes a measurable bounded reproducing
   kernel and a finite signed Borel measure. It represents integration
   as the RKHS inner product with the integrated kernel. Its complete
   proof bounds the integration functional by total variation and the
   bounded diagonal, then uses Riesz representation and kernel sections.
   Proposition4's proof, p2402, explicitly equates the double kernel
   integral with the squared RKHS norm. The relevant identities do not
   require the universality or strict-positivity conclusion of that
   proposition. This is the published Lemma7, not Lemma26 in the longer
   arXiv version. Probability-only mean-embedding claims are unnecessary.

2. Novak, Ullrich, Wozniakowski and Zhang, *Reproducing Kernels of Sobolev
   Spaces on R^d and Applications to Embedding Constants and Tractability*,
   [arXiv1709.02568v1](https://arxiv.org/pdf/1709.02568v1),
   submitted8September2017, title date11September2017. Equation(1), p2,
   fixes the full-line derivative L2 inner product; p3 gives
   K_(1,1)(x,t)=exp(-|x-t|)/2 for that norm. Theorem1, p4, treats
   s>d/2. Section2's finite-s proof, pp6-9, uses Fourier isometry and
   reproducing evaluation; the univariate evaluation, pp10-11, includes
   s=1. These were read, not inferred from the abstract. A later use
   must check dilation and kernel-amplitude scaling for each positive
   rate a_j. No bounded-interval or periodic norm may be substituted.

3. Bauschke, Goebel, Lucet and Wang, *The Proximal Average: Basic Theory*,
   SIAM J.Optim.19(2)(2008),766-785,
   [author primary PDF](https://webpages.math.luc.edu/~rgoebel1/publications/journals/BauschkeGoebelLucetWang08SIOPT.pdf).
   Section2(1)-(2), p767, sets a real Hilbert space and q=||.||^2/2.
   Proposition3.3(i), p769, states q*=q; its proof cites Rockafellar--Wets,
   *Variational Analysis*, Example11.11. This is quadratic Hilbert norm
   duality, not an elliptic theorem restricted to L2 forcing. The
   supremum convention for conjugacy gives the lower direction for
   individual trials or a restricted trial space. Lemma7 above also
   displays the operator-norm supremum directly. The local normalized
   finite expression and matrix optimization are deferred to research;
   none is proved here.

Supporting comparison only: Fasshauer--Ye,
*Reproducing Kernels of Generalized Sobolev Spaces via a Green Function
Approach with Distributional Operators*,
[arXiv1204.6448v3,4March2013](https://arxiv.org/pdf/1204.6448v3),
Definition4.4 pp11-12, Theorem4.2/full proof pp12-13,
Theorem4.6 p15 and Example5.7 p19 were inspected. The general theorem
has symbol, growth, continuity, evenness and L2-inclusion hypotheses;
it is not an unrestricted Green-function slogan. Its scaled Sobolev
example corroborates the route. The simpler explicit one-dimensional
source above suffices, so no new application of this general theorem
or special-function normalization is needed.

### Applicability comparison and boundary obligations

C998u(5)-(6)/audit726 already supplies a real finite signed Borel
measure on R, supported on [0,ell], with TV<B=2^23. It contains the
full density, all interior jumps and both outer traces. Thus the
measure class in Lemma7 matches: no density in L2, positive measure,
non-atomicity or nonzero total mass is required. Exponential kernels
are bounded and continuous; the explicit Sobolev kernel supplies the
RKHS input. This is a source-hypothesis comparison, not a new proof
of C998u or a local energy formula.

The H1 requirement belongs to the TEST function/representer, not to
the discontinuous h. Use continuous representatives so each atom is
paired at a definite value. The whole-line norm includes the exterior
of [0,ell]; imposing zero trace at its endpoints or discarding exterior
test-function norm changes the certificate. Both support endpoints
are interior points of R. No new boundary condition there is needed.

A later pairing through the definition of Dh must retain all of h.
C998u/audit726's test identity is stated for compact smooth tests;
using a whole-line smooth trial requires explicitly inserting a smooth
cutoff equal to1 near the compact support before applying that identity.
This does not permit dropping h's outer traces, either projection
moment or K14. The dual restriction supplies a LOWER comparison only.
Its variational deficit is separate from arithmetic/quadrature error;
there is no asserted1e-6 two-sided approximation to Q_a or the full E.

### Searches, duplicates, failures and access

External queries included `exponential kernel signed measure energy
variational H1 dual norm Green function`, `reproducing kernel Hilbert
space finite signed measures energy variational supremum Sobolev
exponential kernel`, `exponential kernel Sobolev norm RKHS R`,
`Fenchel Hilbert norm conjugate`, `kernel energy signed measures
variational lower bound Sobolev`, and `exponential kernel dual norm
Sobolev measure`. Exact statement and stronger-result searches led to
the signed-measure theorem rather than a probability-only result.
There is no claim that this standard method is original.

Local comparison reused744's block/energy coverage,719's analytic panel
coverage and723's derivative/sweep comparison. Targeted searches read
C998s(1)-(2), C998u(5)-(6) and audit726, C998x(1)-(3), the722 comparison
and ATTEMPTS745. The only further physical-route `dual` hit,
C998w Section8's retained cardinal/polynomial certificates, concerns
spectral support weights, not physical H1 trials. Stops from coarse
BV truncation, the full original-measure ledger and direct density
remain prescription-specific evidence; they do not cover this new
finite trial representation. No sibling notebook was read.

Vovk's working paper17 was inspected only at its Sobolev-space/Pettis
passages; it is not used for exact exponential constants. Feydy's
*Geometric Data Analysis* draft was an optional direct H^(-1) lead;
retrieval failed because the PDF exceeded the web size limit. It is
UNREAD and nonessential given the three inspected inputs. General
Riesz-energy and bounded-domain PDE search hits are uninspected leads,
not source coverage. No persistent essential-source blocker remains.
Full matching Mathlib coverage is unchecked.

### Bounded continuation, nominated but not performed

Nominate just the real span of

    phi_k(x)=exp(-(32x/ell-k)^2),  k=0,...,32,  x in R,

for all256 rates, with no order, width, center, witness or prefix sweep.
This is a proposed33-function smooth trial family, not a computed
certificate or a claim about its adequacy. A later preflight must
specialize the cited norm/duality, certify membership and full-line
normalization, and specify complete full-h pairing/error/work treatment
before evaluating any Gram entries. It may reuse rate-independent
pairing data only after proving that reuse valid. No Gaussian trial
integrals, coefficients, lower bound or affordability are derived here.

Continue only with a complete<=1e8 operation ledger, precision and bytes,
and<=1e-6 numerical error for every evaluated comparison entry, retaining
d0 C(0), q=C(0), the signed t=<Tg,h>, the leading block and C998x's
strict outward positive Schur-margin threshold. An unpaid essential
term or cost failure parks the prescription. A nonpositive certified
lower margin only rejects this sufficient test, not the actual Gram.

The exact next target and source scope are recorded in
`drafts/literature/2026-11-13-prefix-energy-gaussian-preflight-review-746.md`.
That new ready continuation needs a separate approval next turn. This
standard specialization is not a new creative central mechanism:
uniform signed domination against BOTH defects, full S3, C744q/H2 and
Xi/global assembly remain missing. No discovery quota claim is made.

## Original nomination745 body — preserved historical scope

The following paragraphs describe the uncovered state BEFORE comparison746;
their missing-source statements are superseded by the review above.

This file is an uncovered continuation nomination. It does not derive or
approve a new mathematical statement. The next step must compare the
precise proposed dual direction with primary sources and local duplicates,
reusing the existing energy and block assessments. In particular an
ordinary L2-source theorem cannot silently cover Dh's atoms. Account for
whole-line support, outer endpoint terms, both projection corrections,
full K14 and the signed cross entries; do not replace h by its head.

Essential inputs: C744z(1)-(5), C998r/audit709, C998s(1)-(2),
C998u(5)-(9)/audit726, C998x. C999l's exact completion is retained
through C998r. The witness hash remains
99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a.
The analytic-response, neutral-core, IEEE754/Decimal and unreplayed c_*
qualifications persist. No cross-notebook theorem is nominated.

Source-level continuation test: identify a precisely cited theorem that
supports a finite computable lower certificate for the actual signed
measure, with all hypotheses and constants applicable. Otherwise park
this dependent target. If source coverage is adequate, nominate ONE
fixed trial family and a later bounded error/work preflight, retaining
the1e-6 per-entry and1e8 total-operation gates and C998x's strict outward
positive Schur-margin requirement. Do not derive or test that family in
the literature turn. A negative lower margin cannot refute the actual
Gram. No old prescription is reopened by this question.

The route remains an intermediate finite-span tool. A new creative
central mechanism is not justified by step745: uniform signed control
of V14+R^2 against BOTH defects is still missing, and success on this
one Gram would not supply it. No creative-routing quota claim is made.
Full S3, localization, other entries/endpoints, C744q/H2 and actual-Xi
assembly remain unresolved. Full matching Mathlib coverage is unchecked.
