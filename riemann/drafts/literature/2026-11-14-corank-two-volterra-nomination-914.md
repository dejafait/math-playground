# Corank-two actual contact: prospective source comparison

TARGET: Assess whether a second-adjugate Volterra contraction at a hypothetical corank-two actual reciprocal-density contact supplies a nonzero signed local balance, without invertible size-(m-1) minors or higher-order PF assumptions.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Step915 searched higher adjugate/determinant differential, corank-two Hankel, Volterra-Hankel and simultaneous-zero terminology; screened November14 local contact records. Inspected primary manuscript statements and essential proof cases below; no novelty inference from unmatched searches.
SOURCE_EVIDENCE: Bhatia--Jain (2009) Theorems1-4, equations(8)-(14)/(18)/(25)-(28), proofs and Remarks2-3; Rubiano-Murcia--Galvis arXiv:2303.09953v1 Theorem3.3/Corollary3.3.1 and proof; Celsus et al. Dec7 2021 arXiv:1504.07297 Lemmas2.8/2.12 and full relevant proofs; Gallier Aug24 2019 Section1 factorization p2; Vrabel arXiv:2604.04650v1 Theorems2-4/9 and proof cases.
COMPARISON: Singular polynomial determinant differentials and an invertible size-(m-2) Schur reduction are available without size-(m-1) inverses. None of the inspected results supplies a nonzero signed actual-density Volterra contraction. Spectral-pencil, oscillatory-weight and PSD conclusions have additional hypotheses not supplied here.
GAP: Nonvanishing of a specified frozen Hessian weight on the actual Hankel curve, its exact endpoint-controlled Volterra identity and any strict sign remain unproved. Nonzero ambient second differential is insufficient; finite contact order and actual contact existence are not assumed.
REASON: New source-scope negative parks automatic higher-adjugate sign import. The algebraic toolkit now supports a bounded diagnostic of one explicit frozen weight; this is a proposed next mathematical attempt, not a theorem or a creative mechanism.
SCOPE: Actual p and H of C466a/b, inherited L018 convention; finite m>=3, x_*>0, D_j(x_*)>0 for 1<=j<=m-2, D_(m-1)(x_*)=D_m(x_*)=0, rank A_m(x_*)=m-2. First-contact interpretation additionally retains both determinants positive immediately left. No such contact or extra jet nondegeneracy is asserted.
LITERATURE_REASON: The supplied target changed rank-one conditional signing to a corank-two singular determinant contraction; prior ready scalar-law/cofactor assessments did not cover the essential higher differential and singular-source hypotheses.

## Original nomination914, retained for scope

The main gap remains L030-L032/C032a actual-Xi positivity at all
degrees. A usable local balance in this conditional stratum could
clarify the simultaneous-contact part of a later preservation argument.
It would not pay the rank-one signed head, anchor, full tail, strict
forcing, global continuation or Xi transfer.

Inspect primary higher-adjugate/compound determinant differentiation
and Schur-complement statements, with singular cases and actual
Volterra compatibility, before proposing a mathematical attempt. Check
standard terminology, stronger results and obstructions. The desired
intermediate output is a precise conditional observable and a local
test that can distinguish a useful balance from an identically zero
contraction; an identity with no such test is insufficient.

Continue only if the sources support an independently checkable
nonzero higher-contact balance without dividing by D_(m-1), assuming
an unproved derivative sign or reintroducing residual PF_m. Otherwise
record the exact obstruction and choose another independent target.
Retain all rank hypotheses: adjacent zero leading determinants alone
must not silently be identified with the stated corank condition.
Do not assert finite-order contact or nonflatness of its determinant
without justification. No determinant differentiation, compound
identity or sign calculation was performed in this nomination.

Essential future mathematical inputs are C466a and C466b; C466h is
not needed unless a later target explicitly uses its factor law.
The source zero-counting, verified-height, symmetry and normalization
qualifications remain external. C466d/e are rank-one generic contrasts,
not imported corank-two witnesses. The November6 L847/G contact
assessments were screened only to distinguish their coordinate and
rank problem; no proof from that route is used. No cross-notebook
input is involved. Matching Mathlib coverage is unchecked.

No justified proof_attempt/creative target is ready. Source coverage
and a signed discriminant must come first. Any later creative
nomination must name the precise central obstruction and bounded
test, and receive separate approval; routine compound algebra alone
does not constitute a new central mechanism.

## Completed comparison915

### Primary statements and relevant proof cases

Rajendra Bhatia and Tanvi Jain, *Higher order derivatives and perturbation
bounds for determinants*, Linear Algebra Appl.431 (2009),2102-2108,
[DOI 10.1016/j.laa.2009.07.003](https://doi.org/10.1016/j.laa.2009.07.003).
Read the authors' May18 2009 manuscript isid/ms/2009/05 in its
[full manuscript rendering](https://www.academia.edu/7491948/Higher_order_derivatives_and_perturbation_bounds_for_determinants),
not merely its abstract. The institutional PDF endpoints timed out/502;
the manuscript text and theorem numbering were accessible on the mirror.
Theorems1-3 apply to arbitrary complex n-by-n matrices, singular included.
For 1<=k<=n, (9) states

    d^k det_A[X,...,X]
      =k! sum_(I,J in Q_(k,n)) (-1)^(sum I+sum J)
                         det A(I|J) det X[I|J].

Here A(I|J) deletes those rows/columns and X[I|J] selects them.
Equation(13) gives the polarized exterior-power trace version;
(25) uses mixed discriminants. Read the coefficient-of-monomial proof,
Laplace expansion and exterior-power conversion in Section2. Theorem4
(18) gives the differential norm k! times the elementary symmetric
polynomial of degree n-k in the singular values. Remarks2-3 provide
nonnegativity when A and all direction matrices are PSD; arbitrary real
symmetric directions are not covered by that sign assertion. These are
known identities, with no reproof proposed.

Jorge I. Rubiano-Murcia and Juan Galvis, *Higher order derivatives of the
adjugate matrix and the Jordan form*, [arXiv:2303.09953v1](https://arxiv.org/html/2303.09953v1),
Theorem3.3, Corollary3.3.1, equations(18)-(24), proof via Theorem3.2:
B(z)=adj(zI-A) for a fixed complex A. At a diagonalizable eigenvalue
lambda_i of multiplicity n_i, the derivatives below n_i-1 vanish and
B^(n_i-1)(lambda_i)=(n_i-1)! q_i(lambda_i)P_i, with
q_i(z)=det(zI-A)/(z-lambda_i)^n_i and P_i its spectral projector.
Read the resolvent/Cauchy proof including nilpotent terms. This controls
spectral z-variation, not x-variation of A_m(x). It does not sign a
Volterra integral or establish a nonzero derivative along that curve.

Andrew F. Celsus, Alfredo Deano, Daan Huybrechs and Arieh Iserles,
*The kissing polynomials and their Hankel determinants*, Transactions
of Mathematics and Its Applications6 (2022),1-66,
[DOI 10.1093/imatrm/tnab005](https://doi.org/10.1093/imatrm/tnab005).
Read the [December7 2021 arXiv manuscript](https://arxiv.org/pdf/1504.07297),
printed pp4-6,12-16: (1.14)-(1.19), Lemma2.8 with proof and Lemma2.12
with its complete proof. Its moments are integral_[-1,1] z^j exp(i omega z)dz,
not p^(j)(x). Lemma2.8 states h_n h_n''-(h_n')^2=-h_(n-1)h_(n+1);
the proof uses moment derivatives, orthogonal-polynomial ratios and Toda.
Lemma2.12 excludes consecutive zeros for that family. Its double-root
argument also uses (1.19), a non-identically-zero normalized determinant
polynomial, and downward propagation to the explicit base family.
The publisher's Lemma2.9 is numbered2.12 in this manuscript. Neither
that nonvanishing premise nor an applicable replacement base argument
has been verified for the actual density. Do not import the stronger
no-simultaneous-contact conclusion from a shared Hankel label, or use
the divided logarithmic version at a zero. No assertion that the
published theorem is false is made.

Jean Gallier, *The Schur Complement and Symmetric Positive Semidefinite
(and Definite) Matrices*, [August24 2019, Section1, printed p2](https://www.cis.upenn.edu/~jean/schur-comp.pdf):
read the factorization for [B C; E F] with B invertible into triangular
factors and diag(B,F-E B^(-1)C). The full matrix and its Schur complement
may be singular. The source explicitly checks the factorization directly;
no inverse of the full matrix is needed. In the prospective application,
B is the leading size-(m-2) block, whose determinant is nonzero by the
stated D_(m-2)>0 hypothesis. This permits a later two-by-two residual
calculation; it supplies neither its derivative nor a sign. Positive
signed leading Hankel determinants must not be confused with PSD of the
unsigned derivative matrix.

Robert Vrabel, *Determinant Dynamics under Low-Rank Perturbations:
A Unified Framework for Singular Systems*,
[arXiv:2604.04650v1, April6 2026](https://arxiv.org/html/2604.04650v1),
Theorems2-4 and9: read the finite rank-one telescoping proof and the
singular block proof. The additive identity allows singular matrices;
the inverse-product theorem requires nonsingular intermediate matrices.
Theorem9 instead concerns pseudodeterminants, semisimple zero and
P_0 U=0, V^T P_0=0. Its proof identifies a perturbed nonzero block's
pseudodeterminant with its determinant without explicitly requiring that
block to stay nonsingular; this passage is not certified here. Do not
import Theorem9. Even a qualified version concerns the nonzero spectral
block and imposes kernel compatibility absent from the target; it does
not supply determinant emergence or Volterra signs. No new counterexample
or corrected theorem is derived in this literature step.

### Comparison with the actual law and previous stops

C466a's hypotheses/conclusion and C466b's (1)-(14), localization,
endpoint/rank proof and audit888 were inspected, together with the
working audit888 and stop886. Reuse assessment886's completed coverage887
for the unchanged scalar law and convolution inputs; no new book/manuscript
proof audit or finite verified-zero certificate is claimed. C466b's
finite-head extensions are not inputs to this target. The source
zero-counting, verified height, symmetry and normalization qualifications
stay external exactly as recorded there.

The ordinary cofactor observable is zero at corank two: its coefficients
are size-(m-1) minors. The inspected higher-differential formulas avoid
this loss in the ambient space, but the intended directions are constrained
by the derivative Hankel curve. A nonzero multilinear form need not be
nonzero on specified directions. No source checked identifies those
compressed directions as PSD, proves their determinant nonzero, or bounds
the resulting signed weight against the actual kernel. No compound of a
convolution is silently replaced by a convolution of compounds.

The regularity question is narrower than a new source-access blocker:
any specified frozen linear functional of A_m(x_*-t) is smooth on the
closed interval by C466a, while C466b's improper integration-by-parts
argument requires vanishing at t=0 and an O(t) bound there. These
properties and the exact differentiated balance must be verified for
the proposed functional; neither follows here from a chosen notation.
Higher derivatives on H at zero are not among the ready inputs.

Stop886/audit888 concerns scalar domination of a rank-one signed weight;
review914's conditional-cone stop concerns finite-factor test signs.
Neither proves that this distinct corank-two diagnostic fails. Conversely,
compound algebra does not reopen either unpaid signed estimate.
The November6 G-contact route supplies no mathematical input here.
No cross-notebook input, zero-free-region improvement or arithmetic
estimate is involved. No new result is derived in this comparison.

Queries included `higher adjugates corank second derivative determinant
rank n-2 compound matrix theorem`, `Bhatia Jain higher derivatives
determinant compound matrix pdf`, `Hankel Wronskian consecutive determinants
zero multiplicity Toda singular contact`, `Hankel second derivative corank
determinant`, `Volterra adjugate Hankel determinant`, and `Hankel second
adjugate`. Scoped local searches covered November14 contact assessments,
attempts and histories; no duplicate frozen-Hessian test was located.
Unmatched searches do not establish originality. Other recent Hankel
singularity/pseudodeterminant search hits were not read and are not inputs.
One unrelated arXiv identifier was opened in error and discarded as
irrelevant; no claim relies on it.

### Bounded continuation, not yet performed

Propose the scalar function

    W(t)=d^2 det_(A_*)[A_*', A_m(x_*-t)],
    A_*=A_m(x_*), A_*'=dA_m/dx at x_*.

The differential is precisely Bhatia--Jain's symmetric bilinear second
Frechet differential. This defines a test target, not an established
nonzero observable, balance identity or signed derivative. Freeze both
A_* and A_*'; do not differentiate either when differentiating in t.
A later attempt may use only the cited polynomial identities, the
size-(m-2) Schur block and C466b's localized scalar recurrences. It must
retain all parity factors before interpreting a D_m sign.

Continue this diagnostic only if it produces a nonzero W with a rigorous
endpoint-controlled balance and an independently checkable signed
quantity. A precise extra finite-jet condition may be informative, but
must be marked unproved for actual p. If the weight vanishes under the
Hankel/rank relations, or the needed nondegeneracy/sign is simply an
additional unpaid premise, record that result and stop this frozen-weight
choice. Do not escalate automatically through higher derivatives, assume
finite contact order, or report a generic jet model as an actual contact.
A passing diagnostic would address only this simultaneous-contact stratum;
rank-one forcing, strict barriers, propagation, all-degree control and
Xi transfer remain independent gaps.

The proposed follow-up is established-tool specialization, not a justified
proof_attempt/creative mechanism. Its main unresolved issue is whether
the frozen Hessian survives the Hankel directions at all. Any new creative
mechanism needs a separate nomination and essential coverage. This newly
written continuation assessment requires separate supervisor approval.

### Mathlib

Read the official statement of
[Matrix.det_fromBlocks₁₁](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/SchurComplement.html#Matrix.det_fromBlocks%E2%82%81%E2%82%81)
and Matrix.fromBlocks_eq_of_invertible₁₁: finite index types, commutative
ring, and an invertible top-left block; the other diagonal block need
not be invertible. Real finite matrices satisfy these ambient hypotheses.
This is supporting block algebra only. Matching formal coverage of the
higher determinant differential, corank-two Volterra balance and complete
actual-density target was not checked; no absence claim is made.
