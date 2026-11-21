# Energy-image complement: nomination611 and source comparison612

TARGET: Certify ||A0^-1/2(I-P_W)||<=1 for W_512=A0^(1/2)H_512 by a complete inverse Galerkin remainder comparison using C999k's fixed reference order.
CHECKED: 2026-11-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step612 searched inverse Galerkin error operators, Ritz energy projections and shorted-operator terminology; read the primary passages below, reused552/607/609, and compared C999k/l/s and stops537/598/600/603. No exact numerical bound was located; this is not a novelty claim.
SOURCE_EVIDENCE: Teschl GSM99 version12February2009, Theorem1.7/proof p43, Theorem2.13/proof pp71-72, Theorems3.1/3.2 pp90-92 and (3.25)-(3.27); Behrndt et al.1403.5704v1 Proposition2.1 p4, Theorem3.4/nonnegative sufficient proof p11, Corollary3.5 p12; Schoberl iFEM Section10.1 Galerkin orthogonality, Cea proof and symmetric case. Direct links and limited Grubisic comparison below; reuse607 for spectral-support coverage.
COMPARISON: Standard projection/closed-form calculus and relation inverse order cover the mechanism, not the effective constant. C999s611 supplies J*J=A on exactly W_512; C999k supplies the qualified full reference order. The remaining work is their operator-norm specialization, preserving the finite-rank subtraction and all blocks. C999r's raw projection and Grubisic's relative Ritz measure do not supply this bound.
GAP: Establish the proposed bounded-operator identity with domains justified, then certify the complete fixed-reference inverse-error upper comparison at threshold1, or expose its precise unpaid term. No identity, new bound or numerical comparison is proved by this literature turn.
REASON: Separate literature-only step612 completes the changed-target comparison. SPECIALIZE approves only the unchanged TARGET under the existing contracts; qualitative approximation and inverse order alone do not certify its constant. The completed611 finite-margin audit remains valid independently.
LITERATURE_REASON: The proposed inverse Galerkin remainder on W_512-perp is outside the ready finite-margin and raw-projection cutoff scopes; exact operator-error coverage and its hypothesis comparison have not been read.
SCOPE: Fixed N512, ell=log(3)/2, exact Z and A=Z*LZ from C999l, actual restricted A0 and E=A0^-1/2, P_W the L2 projection onto W_512; C999k's unchanged R<=L, head H and complementary QDQ/2. No parameter tuning, new scalar floor, finite inverse square root or C999r tail transfer.

Main gap: L030-L032/C032a actual-Xi positivity. The proposed intermediate
target is a bound on the inverse square root restricted to the changed
complement. An explicit bound <=1 would remove the enormous global
c_*^-1/2 loss from this particular factor. Even success would leave the
signed separation7/14 couplings and the remaining norm factors unpaid;
it would not certify the complete S3 sign or the mixed-block comparison.

The suggested mechanism is to investigate the candidate identity

    E(I-P_W)E = A0^-1-Z A^-1 Z*,

as a whole positive Galerkin error operator and compare it with the
fixed reference inverse, preserving the subtracted finite-rank term.
This is a source-review question, not a proved identity or an approved
calculation. In particular the restriction of R^-1 to H0 must be handled
as a form comparison with the correct projections, not identified with
A0^-1. Taking independent norms of both terms might destroy the desired
cancellation; sources must be checked for exact hypotheses and effective
operator bounds, beyond qualitative convergence or pointwise residuals.

Essential local inputs: C744z Sections1-3 for the actual restricted
operator; C999l(1)-(3), Sections1-2/6-7 and audit561 for exact Z,A;
C999s Sections1/5 for the energy-image geometry and audited finite margin;
C999k Sections1-2/6 for the qualified full reference order and inverse
comparison. C999r is a contrast, not a bound for this projection.
Keep all inherited analytic/arithmetic/core and unreplayed c_* assumptions.
No cross-notebook input; full matching Mathlib coverage is unchecked.

The later bounded test would certify the stated <=1 threshold on the
entire complement or identify the exact insufficient inequality or
allowance, without varying N, the basis, reference or allocation. Failure
of a sufficient upper estimate would not prove that the actual norm
exceeds1. A successful bound could feed a separately assessed signed
endpoint/complement comparison; C744q, H2, non-neutral directions and
global assembly would remain independent gaps.

Preserve the uniform-tail537, enlarged-family598/600 and fixed-trial603
stops. This proposal changes the operator being estimated and retains a
finite-rank inverse cancellation; it does not retry those enclosures.
No external coverage, novelty or mathematical success is asserted.
The likely method is established-route development, not a justified
creative central-sign mechanism. A future creative nomination needs a
specific paid signed-coupling idea beyond this standard Galerkin question.

## Separate source comparison612 — 12 November2026

The paragraphs above preserve nomination611, including its then-pending
coverage. This separate review supersedes that pending status, without
establishing its candidate identity or its threshold. Main gap, target,
downstream use and independent unresolved assumptions remain as stated.

### Primary coverage actually inspected

[Teschl, *Mathematical Methods in Quantum Mechanics*, GSM99, author
version12February2009](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
Theorem1.7 and proof p43: orthogonal decomposition for a closed subspace
of a complex Hilbert space, followed by the closest-vector statement.
Theorem2.13/proof pp71-72 treats densely defined closed semibounded
Hermitian forms. Theorems3.1/3.2 pp90-92 and (3.25)-(3.27) specify
spectral calculus, integrability domains and truncation limits. Reuse607
for Theorems2.18/3.7 and spectral support. These support the restricted
square-root coordinates; they do not permit commuting a projection
through A0 or inserting a finite inverse square root. No reproof needed.

[J. Schoberl, *An Interactive Introduction to the Finite Element Method*,
Section10.1, Approximation of coercive variational problems](https://jschoeberl.github.io/iFEM/abstracttheory/Coercive.html#approximation-of-coercive-variational-problems),
accessed12November2026, copyright2024: read the closed trial-space setup,
Galerkin orthogonality, complete Cea proof and symmetric-case energy
projection passage. The page uses real bilinear forms. It supplies the
standard method, not a theorem about this notebook's complex restricted
operator or a uniform L2 inverse-error constant. For the Hermitian
specialization use Teschl's complex projection theorem; the later attempt
must justify completeness and the coordinate maps, rather than silently
applying the real display as a complex operator identity.

[Behrndt–Hassi–de Snoo–Wietsma, *Antitonicity of the inverse for selfadjoint
matrices, operators, and relations*, arXiv1403.5704v1,
22March2014](https://arxiv.org/pdf/1403.5704v1): inspected Proposition2.1
p4, Theorem3.4 and its sufficient proof p11, and Corollary3.5 p12;
reuse552 for Sections2.1-2.3 and the supporting inverse-order proof cases.
Proposition2.1 uses inclusion of shifted square-root domains and their
norm inequality. Corollary3.5 reverses order for nonnegative selfadjoint
relations on a separable Hilbert space, including non-dense domains.
The proof explicitly includes zero negative index, positive shifts and
successive strong-resolvent limits. Its conclusion controls the inverse
of C999k's relation; it does not identify it with an unrestricted inverse
compression or certify a norm after finite-rank subtraction.

For comparison only, inspected the setup pp1-2 and formula(1.7) p3 of
[L. Grubisic, *On eigenvalue and eigenvector estimates for nonnegative
definite operators*, arXiv:math/0503328v1](https://arxiv.org/pdf/math/0503328v1).
It compares energy-scaled Ritz residuals through a relative inverse
difference on the trial space. This is not the absolute operator norm
on the entire changed complement asked for here. Its later theorems and
their proofs were not inspected or imported; no new angle hypothesis,
spectral gap, or numerical estimate is assumed from that lead.

Queries included `Galerkin inverse error operator energy orthogonal
projection positive self adjoint operator norm variational approximation
inverse`, `"Galerkin" "inverse" "error operator" positive definite`,
`"Ritz" "inverse" "energy projection" operator`,
`"shorted operator" "Galerkin"`, and
`Grubisic Ritz approximation inverse operator energy norm error positive
definite`. Other search hits, including finite-matrix coarse-grid and
shorted-operator leads, were not inspected as theorem inputs. No novelty
is inferred from this bounded search. Full matching Mathlib coverage is
unchecked; generic projection/spectral results would not pay the local
effective constant.

### Applicability and remaining specialization

Read C744z Section1, C999k Sections1-2 and the domain/order portion of
audit557, C999l(1)-(4)/Section1, and C999s Section1. Reuse audits561/611
and assessments552/607/609 for their unchanged scopes. These local
inputs already supply, conditionally, the actual closed restriction,
finite strong-domain vectors, exact neutral coordinates and full
reference order. They do not supply the proposed inverse-error bound.

The next mathematical attempt has the following obligations within the
unchanged TARGET and SCOPE:

- Use C999s's exact J=A0^(1/2)Z and J*J=A to identify P_W. Establish
  the nominated identity on all H0, with every square-root composition
  and adjoint justified. Do not infer invariance of H_512 or interchange
  the two noncommuting projections. This is a finite-coordinate
  specialization of the cited projection/calculus results, not a reproof
  of them; the identity remains unproved in this review.
- Relate the requested norm to the positive inverse Galerkin error
  with the correct square and adjoint orientation. Apply C999k's
  restricted-relation inverse order, keeping both surrounding neutral
  projections when viewing its full-space reference as an H0 operator.
  Retain the exact subtracted Galerkin term. The proposed complete
  reference upper comparison must be justified before evaluating it.
- Bound that entire comparison using the unchanged rational head H,
  QDQ/2 and exact Z,A. Include head, complement and mixed terms,
  exact-neutral conversion, every used entry/arithmetic allowance and
  the infinite diagonal tail. Existing fixed546 residual numbers and
  the .00014 finite S3 margin are not inverse-error bounds.
- Compare the resulting uniform operator upper bound with exactly1.
  A qualitative convergence theorem, finitely many residual checks,
  or separate large norms of the two inverse terms do not complete
  this test. No parameter search, new floor, reference change or finite
  inverse-square-root replacement is covered.

If the fixed comparison cannot reach1, save the exact insufficient
inequality or allowance and stop this attempt without tuning. Failure
of a sufficient upper estimate does not prove an actual norm lower
bound. If it succeeds, record only the qualified complement factor;
the signed separation7/14 coupling, other norm factors, full reference
inputs, original core/c_* validation, C744q, H2, non-neutral coverage
and global assembly remain open. A later use needs its own assessment.

### Duplicate/failure check and decision

Read the four exact ATTEMPTS records ending537/598/600/603. Their stops
concern a scalar uniform-tail charge, enlarged-family isotropic losses,
entry-radius losses and a fixed-trial head-action allowance respectively.
This fixed energy-image inverse-error question has different input and
output spaces and keeps a finite-rank cancellation. It does not undo
those stops or authorize their repetition. C999r's audited raw neutral
L2 projection is likewise a contrast, not a transfer theorem for P_W.

DECISION SPECIALIZE: coverage is ready for the exact saved target in a
separate mathematical turn. The citation-only imports do not settle
the notebook-specific identity or effective bound; no lemma or
mathematical script was changed. Outcome EXPLORATION / REPRODUCTION:
this is source-scope progress, with no mathematical advance or progress
beyond the inspected methods. Established Galerkin development is the
appropriate route. No justified creative central-sign mechanism is
ready: a new paid signed remote/complement coupling is still missing.
