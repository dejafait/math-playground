# Combined joint operator: cancellation-preserving source comparison

TARGET: Assess source coverage for a cancellation-preserving contraction test of L929's combined operator B using an integral of complex Jordan factors, retaining both exact energy metrics and the Hardy phase at N=floor(T^(1/5)).
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step12 performed bounded searches for complex Jordan/GCD integral representations, divided differences and coupled shifted-moment cancellation; read de Boor Section9 and the primary source interfaces below. Reused scope-8/test-9 overlap and failure comparisons. No inspected theorem supplies the required joint contraction; no novelty claim.
SOURCE_EVIDENCE: de Boor arXiv:math/0502036v1 Section9 pp63-64, first-difference integral and (51)-(52), https://arxiv.org/pdf/math/0502036v1; Mattila v2 Proposition2.5 p6 https://arxiv.org/pdf/1403.5907v2; Bhatia Propositions1.3.1-2/Theorem1.3.3 pp13-14 https://assets.press.princeton.edu/chapters/s8445.pdf; Pratt--Robles v3 Remark1.1/Theorem1.2/Section3.2.1 https://arxiv.org/html/1706.04593v3; DLMF25.2(i),(4) https://dlmf.nist.gov/25.2#E4.
COMPARISON: The standard first-divided-difference integral preserves paired holomorphic endpoints, and complex incidence factorization is available at each finite parameter. These are representation tools only. Pratt--Robles gives paired main terms and a fixed-parameter collision limit, not a coefficient-uniform contraction. L929's termwise stop remains distinct from the proposed combined pole-part test.
GAP: The proposed exact pole-part integral must be verified against L928/L929 and bounded together with its regular-zeta residual in the full H metrics; no such bound is imported. The independently testable sufficient inequality is ||B_pole||+||B-B_pole||<=1-eta uniformly, eta>0 fixed, with B_pole defined in the continuation nomination below. L929 remains unaudited.
REASON: The required literature-only comparison is complete: finite integral tools support nomination of one bounded coupled residual test, but no application or contraction has been derived. The newly written continuation requires separate approval next turn; this review does not approve new mathematics.
SCOPE: L928's fixed w,Z, shifts +/-1/log T, T<=X<=2T, N=floor(T^(1/5)), arbitrary moving complex coefficient pairs; L929's exact H_-,H_+,W_+,W_- and beta_+,beta_-. No enlarged dictionary, matrix grid, zero-sum source limit, signed transfer or RH claim.

The following is the preserved step11 nomination, superseded only as a source-status record by step12 below. At nomination time this was not a ready mathematical assessment. The exact
combined operator is defined in L929 (6),(8); its proof has not had a
separate audit. Use that definition as the proposed object, and check
its source interface rather than assume a newly proved contraction.
Essential established inputs are audited L928, L737's finite identities
and audit, L637's normalization/phase, and L926/L927 for the already
charged downstream scale. L925 and cross-notebook results are excluded.

The proposed integral of complex Jordan factors is an unread lead, not
an identity or positivity premise. Compare a primary theorem's actual
hypotheses and endpoint terms before selecting any later calculation.
The source review should preserve the two summands' relative phase and
both complete energy matrices. A theorem giving only entrywise moduli,
separate norm bounds or ordinary GCD eigenvalues does not address the
loss in L929. Do not reopen that stopped majorant with different weights.

The downstream mathematical threshold remains a fixed relative bound
<=1-eta, eta>0, or an explicit positive joint margin dominating the
L928(3)-(5) remainder. A later test may stop at a quantitatively
informative residual, but a coordinate identity alone is no advance.
At the source stage continue only if a concrete coupled representation
and independently testable residual emerge; otherwise record the
obstruction and select a different mechanism. No representation has
been worked out in step 11, and no mathematical coverage is approved here.

The main gap remains L030-L032/C032a actual-Xi mixed positivity.
Even success here would address only a joint projection input; signed
realization and transfer remain independent. No central creative Xi-sign
target is justified by these unsigned tools, and the earlier critical-value
source screen is not to be repeated without a new signed input. The
recommended next task is literature_comparison / standard / high.
Full matching Mathlib coverage remains unknown.


## Completed source comparison — 9 November 2026, step12

LITERATURE_REASON: The target changed from an already covered termwise
modulus Schur certificate to an unassessed coupled integral mechanism.
This supplied REVIEW_REQUIRED gate required a literature-only step.
No lemma, mathematical program, integral identity for B, or bound was
proved here. STEP_OUTCOME is EXPLORATION, not a mathematical advance.

### Search and local overlap

Queries actually used: `"gcd matrices" "complex" "integral" Jordan`,
`"twisted second moment" shifts integral coefficients zeta cancellation`,
`"Jordan" "meet matrices" complex function factorization integral`,
`"complex" "Jordan totient" "integral"`,
`"twisted second moment" "integral" "alpha+beta" Pratt Robles`,
`"gcd matrices" "sine" positive definite`,
`de Boor Divided differences 2005 Genocchi Hermite complex nodes integral pdf`,
`"gcd matrices" "divided differences"`, and
`"Jordan totient" "contraction" matrix`.
The exact combined theorem was not identified in this bounded search;
no claim of exhaustive coverage or novelty follows. Most arithmetic
hits concerned other L-functions or coefficient restrictions and were
not imported. Secondary summaries and snippets were leads only.

Read L929's definition and scoped proof, L928's hypotheses/main form,
the prior test-9 assessment, and the termwise-stop attempt/history.
Used narrow passages from scope-8 and the two-shift arithmetic source
assessment to reuse the step226, unpaid-coercivity and approval-loop
comparisons. No sibling notebook was read. Existing complex-factor
coverage is not being advertised as a new result. L929's scalar sin(1)
pairing is not an upper norm bound and its proof remains unaudited.

### Primary statements and relevant cases actually inspected

* Carl de Boor, *Divided Differences*, Surveys in Approximation Theory
  1 (2005), 46-69, arXiv:math/0502036v1 (1 February2005),
  [Section9, pp63-64](https://arxiv.org/pdf/math/0502036v1).
  Read (51)'s analytic disk/contour hypotheses, the complete two-node
  derivative integral immediately before (52), and (52)'s simplex
  integral definition. For a function holomorphic on a neighborhood of
  the segment joining distinct complex x,y, the first divided difference
  is integral_0^1 f'((1-s)x+sy) ds. Only this first-order case is needed;
  it preserves the difference before taking a norm. This is a scalar
  identity, applicable entry by entry to finite holomorphic matrix
  functions. It asserts no matrix positivity or dimension-uniform norm
  bound. The contour case requires analyticity inside the specified
  disk; it cannot be applied to an uncancelled zeta pole. Higher-order
  formulas and real mean-value positivity are unnecessary. Author-hosted
  dvdsurvey.pdf and arXiv were accessible; the ETH mirror returned404,
  which is not an essential source blocker.
* Mattila, *On the eigenvalues of combined meet and join matrices*,
  [arXiv:1403.5907v2](https://arxiv.org/pdf/1403.5907v2),
  Section2, pp2,4-6, especially Proposition2.5 (printed p6).
  Rechecked complex-valued f, the locally finite lattice, ordered
  meet-closed S, convolution definitions and the complete factorization
  statement. This gives E D E^T, with convolution weights; the divisor
  prefix meets the algebraic hypotheses. It supports parameterwise
  finite complex Jordan factors, not a positive Gram integral or
  contraction. It cites Bhat's Theorem12; that original proof was not
  newly inspected. Reuse the standard finite identity, with no reproof.
* Bhatia, *Positive Definite Matrices* (2007),
  [pp13-14](https://assets.press.princeton.edu/chapters/s8445.pdf),
  Propositions1.3.1-2 and Theorem1.3.3: read the SVD argument,
  positive-definite congruence and both Schur-complement proofs.
  Arbitrary complex cross blocks are allowed; both diagonal energies
  must be strictly positive for the inverse-square-root case used here.
  This is a relative norm criterion, not a strict bound for our block.
  Neither nonunitary coordinate changes nor complex symmetric factors
  may be treated as unitary or Hermitian. The singular case is unused.
* Pratt--Robles, *Perturbed moments and a longer mollifier for critical
  zeros of zeta*, [arXiv:1706.04593v3](https://arxiv.org/html/1706.04593v3),
  1 June2018, Remark1.1, Theorem1.2 and Section3.2.1.
  Rechecked the paired zeta main term, the general-coefficient branch,
  and the proof's two functional-equation contributions through their
  combination. Reuse the full arithmetic remainder/weight application
  already audited in L928. Remark1.1's Laurent collision is a
  fixed-parameter statement: its O(s) cannot be used uniformly with
  log y growing as log T without a new estimate. The source's displayed
  auxiliary G divides by (alpha+beta)^2. No new moment theorem at a
  zero-sum shift, or uniform passage of its remainder through that
  shift, is imported. Finite main-form interpolation does not need
  that unproved analytic extension of the moment remainder.
* [NIST DLMF25.2(i),25.2.4](https://dlmf.nist.gov/25.2#E4):
  read the sole simple pole/residue statement and the complete Laurent
  expansion, including its corrections/source attribution. It supports
  removal of the scalar pole and a holomorphic regular part near0.
  It does not control that regular part after multiplication by the
  growing complex factor matrices and energy normalization.

### Applicability boundary and proposed discriminating test

The sources support a finite first-divided-difference representation
AFTER its endpoint function has been specified and the scalar poles
removed. Real logarithms of all positive integer bases are mandatory;
parameterwise finite incidence factors involve no infinite divisor
limit. Apply the named calculus identity, not a new general reproof.
There is no primary theorem here asserting that complex Jordan weights
on the interpolation segment are positive, nor that integration of
those weights gives a contraction in the two energy metrics.

The concrete future test is specified in
[the continuation nomination](2026-11-09-joint-pole-integral-residual-test-12.md).
It separates only the paired scalar pole contribution from the regular
zeta contribution, while retaining cancellation inside the pole pair.
It seeks a full relative norm bound for each of these two operators;
it does not return to separate moduli of the conjugate pole summands.
The unresolved quantities are explicit finite operators, so the test
can yield a bound or an informative loss without assuming Xi signs.
All identities, endpoint factors, uniform constants and potential margin
are future work. A coordinate rewrite alone is not progress.

This completes the saved source question with DECISION EXPLORE.
There is no accessible-source obstruction requiring indefinite browsing,
and no matching contraction theorem to import. One bounded application
may be considered after separate approval of the nomination. Stop that
selected estimate if its charged residual consumes its pole-part margin;
repetition then needs materially new input. Preserve the termwise Schur,
step226 and earlier route stops. The main Xi mixed-positivity gap and
independent signed realization/transfer gaps remain. Full matching
Mathlib coverage was not checked; supporting facts do not verify B.
