# Source review: one fixed-support rule family across the remaining blocks

TARGET: Assess primary coverage for certifying one fixed-35-index positive moment rule uniformly for C998v's dyadic blocks k=11,...,71, without per-block NNLS or inverse recomputation, at B^2 uniform error<=1e-7 and total preparation/validation work<=10^8.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review733 searched parameter-dependent/fixed-node positive quadrature, prescribed-support Tchakaloff results and shared-preconditioner verified linear systems; compared C998w Sections1-4, C998v Sections1-3/5 and assessments729/732. No theorem guaranteeing this fixed35-label family or its complete cost was found; no novelty inference follows.
SOURCE_EVIDENCE: S.M.Rump, Acta Numerica19(2010),287-449, corrected author PDF Sections10.3-10.5, Theorems10.2/10.6/10.8, (10.8)-(10.15), Algorithm10.7 and relevant proofs/interval-data cases; van den Bos--Sanderse arXiv:1902.07477v2 Section2.1/(2.4)-(2.6), Section3.1/Theorem2 and proof; Glaubitz arXiv:2009.11981v1 Theorem3.3/proof and Corollary3.4/Section4. Reuse729/comparison730's inspected residual and analytic-approximation sources.
COMPARISON: Verified interval linear-system results permit a finite family test with shared chosen preconditioners and fully enclosed input data; differentiability and a known condition number are unnecessary hypotheses. They do not guarantee inclusion, positive weights, the original-measure residual tolerance or affordable preparation. The inspected positive-quadrature existence/extension results do not guarantee this prescribed support.
GAP: Construct and validate the fixed35-label family: original moments through degree68, interpolation and Gram enclosures, quantitative positive margins, original-measure residual<=5e-19 for all61 remaining blocks, B^2 uniform error<=1e-7 and a complete work/storage ledger. All instance-specific inequalities and feasibility remain unproved.
REASON: Primary verified-system criteria supply the missing finite uniform validation mechanism after the source-specific732 stop. SPECIALIZE approves only an attempt at the listed finite test, not the existence or affordability of a rule family. No family bound, new lemma or mathematical script is derived733; the newly ready continuation receives separate approval next turn.
LITERATURE_REASON: Changed essential hypothesis and mechanism: one parameter-uniform fixed-support positive rule and shared validation replace61 independent NNLS candidates and separately regenerated inverses. Existing residual coverage does not justify uniform feasibility or conditioning.
SCOPE: Original C998v discrete measures, degree34, the k=10 active support labels, k=11,...,71, one common interpolation preconditioner and one common Gram preconditioner; no continuous-density replacement, new support search, per-block inversion or signed-scalar/sign conclusion.
COVERED_TARGET: Test the fixed k=10 support-label family for C998v's blocks k=11,...,71 using one shared preconditioner for each of the interpolation and Gram systems, certified original moments and interval inclusion, without per-block NNLS or inverse recomputation, at B^2 uniform error<=1e-7 and complete preparation/validation work<=10^8.

The nomination below is preserved as the invocation-start proposal.
Its pending-coverage statements are superseded only by review733 below.

The main gap remains L030-L032/C032a actual-Xi positivity and signed S3.
The downstream use remains only C998u's full derivative-measure scalar
preparation. This nomination is not a creative central-gap sign argument.

Keep the original discrete nu_J of C998v Section2, degree34, residual
epsilon<=5e-19, B=2^23, r>=0 including zero, prefix j<256, and tail
j>=2^72. For the remaining61 blocks, propose the SAME35 index labels
from C998w's successful k=10 active set, interpreted inside the existing
129-index prescription j_i=J+floor(i(J-1)/128). The selected labels are
an input to be read narrowly from the k=10 certificate next turn.
No weights, parameter formulas, uniform positivity or conditioning
bounds are calculated or asserted in this nomination. Do not treat
three feasible instances as a uniform theorem.

First compare primary results for parameter-dependent interpolatory
positive quadrature and verified finite linear-system perturbation,
including exact hypotheses, error propagation and positivity conditions.
Reuse ready residual/analytic-approximation coverage for its unchanged
part. Search exact statements and known obstructions before proposing
any derivation. A source that merely proves quadrature existence, or
continuity without a quantitative positive margin, is insufficient.
If the source gate is satisfied, specify a separately approved bounded
test using an anchor and certified parameter remainder, counting all
anchor/candidate generation, moments, directed arithmetic, control,
validation and storage. No731 or728 computation becomes free preparation
for a claimed cheaper complete construction. Reusable certificates may
serve as already verified mathematical inputs only with the accounting
scope made explicit.

Continue only if the review supports a finite uniform feasibility and
conditioning test with explicit error and full work/memory accounting.
Abandon this nomination on an essential unmatched hypothesis, absence
of a discriminating finite test, a certified negative weight/residual
failure in a later test, or an above-cap mandatory-work bound. No new
source result or mathematical approval is supplied732. If adequate
coverage is absent, keep REVIEW_REQUIRED or SOURCE_BLOCKED and do not
derive the uniform-family mathematics in the same turn as its approval.

Essential inputs: C998w's three finite rules and Section4's stop;
C998v Sections1-3/5; C998u Section2; C998t Sections1-3/6 and
C998s Sections1-2/6; C744z(1), C999l(1), unchanged C998r witness.
Retain334 shifts, identity2187,512 modes, full K14, exact P0,
ell=log(3)/2 and witness SHA256
99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a
(not replayed732). Analytic-response, neutral-core, IEEE754/Decimal and
unreplayed c_* contracts persist. Density/mixed interactions, h and
d0 C(0) preparation, remaining9e-7, other entries/endpoints, C744q/H2,
signed S3 and actual-Xi/global assembly remain open. No original-operator
inverse, RH or cross-notebook input is assumed. Full matching Mathlib
coverage for the proposed family construction has not been checked.

## Completed primary-source comparison733 — 13 November2026

### Verified systems: the missing finite test, not a feasibility theorem

Siegfried M. Rump, *Verification methods: Rigorous results using
floating-point arithmetic*, Acta Numerica19(2010),287-449,
DOI10.1017/S096249291000005X,
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf).
Read Sections10.3-10.5: internally numbered pp52-53 and55-59,
Theorems10.2,10.6,10.8, equations(10.8)-(10.15), their readable
proofs, and the complete Algorithm10.7 loop. This is the author's
corrected copy retrieved13November2026; its revision date is not given.
Internal page numbers differ from journal pagination. Some other pages
extract badly; no unread formula from those pages is an input here.

Theorem10.2 takes real square matrices A,R and real vectors b,x0.
For a subordinate norm, ||I-RA||<1 implies nonsingularity and

    ||A^-1 b-x0|| <= ||R(b-A x0)||/(1-||I-RA||).

The argument preceding the theorem is the convergent inverse-series
bound. R is a supplied finite real matrix; inverse accuracy is tested
by the inequality, not assumed. The discussion on p55 expressly applies
the result to every matrix inside enclosed interval input data. This
also supplies a source for validating a chosen preconditioner against
the original Gram matrices, rather than regenerating their inverses.

Theorem10.6 uses a finite interval vector X and the strict inclusion

    Rb+(I-RA)X subset int(X).

It concludes that A,R are nonsingular and that the solution belongs
to the displayed image. Its proof uses Lemma10.5's spectral-radius
criterion and convergence of the affine iteration. Equation(10.14)
gives the residual-centered version: with a real candidate x0, check

    R(b-A x0)+(I-RA)X subset int(X)

to enclose the solution in x0 plus that image. Section10.5 explains
why uninflated iteration can fail even in dimension1, then supplies
interval inflation; it does not make successful inclusion automatic.
Algorithm10.7 stops after at most15 iterations. Theorem10.8 and its
proof apply the point theorem to arbitrary members of the interval
matrix and right side, using outward inclusion. They cover every such
system, not merely the midpoint. The matrix-right-side remark on p59
also covers inverse enclosures. No new proof of these results is needed.

For the proposed family, the interpolation system is the35-by35
evaluation matrix of T_0,...,T_34 at the selected original nodes,
with right side the ORIGINAL nu_J moments through degree34.
The second system type is C998w's ORIGINAL-measure Gram matrix H,
which needs moments through degree68. These are finite real data,
so the cited theorems apply once those exact data are enclosed.
A chosen common interpolation preconditioner and a chosen common
Gram preconditioner are allowed inputs to the criteria; a different
inverse for each k is not a theorem hypothesis. This is an applicability
check, not an assertion that either criterion holds for these data.

In particular the source accepts an interval enclosure of a finite
family regardless of the way its data depend on k. The floor-defined
indices must be enclosed exactly; continuity, differentiability or an
unproved affine parameter formula must not replace them. Each of the61
actual dyadic parameter values must be included. Enclosing a larger
set of matrices is sound but can defeat the test through overestimation.
There is no need to import Rump's separate affine-parameter Theorem10.11;
no affine-dependence hypothesis has been verified for this family.

Successful inclusion alone proves no positive quadrature: the resulting
weight intervals must have positive lower endpoints (or a separate
rigorous nonnegativity certificate). An interval crossing zero is an
inconclusive sign test, not a negative weight. Likewise conditioning
of a midpoint is no substitute for the uniform criterion. No norm,
weight margin, parameter remainder or error constant is computed733.

### Positive quadrature: what the existence results do not supply

L.M.M. van den Bos and B. Sanderse, *A geometrical interpretation of
the addition of nodes to an interpolatory quadrature rule while
preserving positive weights*,
[arXiv:1902.07477v2](https://arxiv.org/html/1902.07477v2),23January2021.
Read Section2.1/(2.4)-(2.6) and Section3.1, including Theorem2/(3.12)
and its full proof. The setup uses a nonnegative density with finite,
exactly known moments and distinct nodes. The interpolation weights
solve the Vandermonde moment system. For one added node, Theorem2
characterizes nonnegative new weights by explicit inequalities involving
the old weights, the next-moment defect and nodal products. The proof
uses the explicit weight corrections. The last displayed proof line
(3.14) prints equality at the boundary despite the nonstrict hypothesis;
we do not import that display as an identity away from the boundary.

This is a useful scope comparison, not a matching theorem for our
changing discrete measures, moving floor-grid nodes and inexact moment
inputs. It supplies no positive margin for all the specified dyadic
blocks. Neither distinct nodes nor an existing positive rule alone
guarantees the desired sign after a change. We do not extend or reprove
this theorem. Rump's interval-data criteria, coupled to explicit sign
checks, are the appropriate source-backed test here.

Jan Glaubitz, *Constructing Positive Interpolatory Cubature Formulas*,
[arXiv:2009.11981v1](https://arxiv.org/pdf/2009.11981v1),24September2020,
pp2,9-11, restrictions(R1)-(R4), Theorem3.3/full proof,
Corollary3.4 and the Section4 construction were read. Theorem3.3
assumes a compact domain, constants in the fixed finite function space,
nonnegative discrete reference weights whose product inner products
converge to the continuous ones, and unisolvence of the positive-weight
subsequence. It gives eventual nonnegative least-squares weights as
the number of candidate points grows. Its proof requires convergence
of discrete orthonormal bases and a boundedness constant, then an
existential onset N0. The Section4 procedure grows the candidate set
before reducing it. It does not hold a prescribed35-point subset fixed.
The density/equidistribution corollary supplies no explicit onset or
bound for our selected support. We import none of these conclusions
for nu_J and infer no impossibility from their mismatched scope.

The published2023 paper *Construction and application of provable
positive and exact cubature formulas*, IMA J.Numer.Anal.43,1616-1652,
DOI10.1093/imanum/drac017, was found, but its publisher full text redirected
to an inaccessible CDN. Search excerpts mentioning renumbered
Theorem3.5/Corollary3.6 were NOT read as theorem evidence. Only the
explicitly versioned2020 primary text is compared above. This is not
an essential source blocker for the finite verified-system test.

### Reused coverage, finite prescription and complete accounting

Reuse assessment729/comparison730, rather than searching or reproving
its unchanged residual theorem (Piazzon--Sommariva--Vianello2017,
Proposition1.2/(7)-(15)) and analytic approximation (Trefethen ATAP,
Theorems8.1-8.2). C998w Sections1-3 already specialize them to nu_J,
including zero and the original-measure residual norm. Their premise
remains epsilon_J<=5e-19 on EVERY required block; its conditional
<7.245e-8 conclusion is not newly established here. A raw Chebyshev
residual alone still fails the hypothesis. Reuse C998v Section2 and
assessment729's coverage for finite-moment preparation; extending its
enclosed moment list through degree68 must be done and paid later.

The complete /solver/active value of the k=10 certificate was read with
the shared JSON inspector using --full. In its recorded order it is

    29,36,21,15,46,55,64,10,74,83,6,92,3,100,107,40,113,1,
    25,118,122,125,0,69,127,51,87,18,128,96,2,8,120,124,104.

These are input index LABELS i, not the integer spectral nodes j.
Use the existing j_i=J+floor(i(J-1)/128) and C998v's t_j,nu_J;
the finite-decimal k=10 weights are not fixed weights for other J.
This extraction is source inspection only. No certificate was replayed
and no other k was solved733. Preserve the original active order or
explicitly account for any column permutation in a later certificate.

The covered finite attempt uses the k=10 instance as an anchor and
encloses the actual differences in nodes, interpolation data and
original Gram/moment data for all k=11,...,71. It may form interval
boxes by finite enumeration of these61 values; that is uniform coverage
of the required finite family, not a theorem about a parameter continuum.
Fix the precision, inflation/iteration limits and work-stop rule BEFORE
running. Produce the two anchor preconditioners once, and use only
matrix products/residual iteration thereafter. No per-block NNLS,
normal-equation active-set Gram search or inverse recomputation belongs
to this prescription. Fixing a common preconditioner does not make its
products or moment enclosures free. Do not silently change support,
precision or anchors after failure; retain the failed test evidence.

Check a certified positive margin and the original residual for each
required instance, or for boxes rigorously covering them. Finite-decimal
output weights must receive their own residual check; existence of
enclosed exact weights does not certify their rounded replacements.
A shared Gram certificate may be used in C998w's existing residual
formula only after its hypotheses are verified. These are obligations
for the next research attempt; none is asserted to pass.

Before expensive validation, price the complete recipe against10^8
using C998v Section5's source-work convention. Charge the two anchor
constructions, candidate iterations, all69 original moments, node
generation, directed products, comparisons, bindings/stores, loop
control, validation and output preparation. Document treatment of
integer/Fraction internals and other previously omitted costs; a lower
bound convention is not by itself a complete upper-bound model.
Give peak storage in entries and bytes at the chosen precision, counting
moment data, both preconditioners, interval matrices, weights and output.
Printed iteration caps, asymptotic complexity and Rump's timing ratios
are not a complete source-work or memory bound.

State the input/cost boundary explicitly. Existing three rules may be
used as verified mathematical inputs for an incremental family test,
but that result cannot be called a cheaper complete construction with
their source production silently free. Any from-scratch full G claim
must pay their production or specify and validate a replacement recipe,
the256 retained atoms and the shared anchor costs, as well as the new61
blocks. The expensive728/731 runs do not become zero-cost preparation.
An incremental result can therefore pass feasibility while leaving
the complete-work gate open; report that distinction honestly.

Continue only if the prescribed finite test certifies all needed signs,
residuals and uniform hypotheses and the complete priced recipe meets
the cap with explicit storage. Stop the prescription on a certified
negative weight, a residual violation, an unsuccessful bounded interval
test or an above-cap ledger. Failure of an inclusion test is failure
of this sufficient certificate, not proof that the exact rule is bad.
Do not spend another unchanged turn seeking a positive margin by
continuity alone. Preserve732's independently valid cost obstruction.

Searches included `parameter dependent quadrature positive weights
fixed nodes`, `fixed nodes quadrature perturbation positivity`,
`Rump verification solutions linear systems interval matrices
approximate inverse theorem`, `parametric interval linear systems
Rump fixed preconditioner`, and `Tchakaloff prescribed nodes positivity
quadrature`. Popova's generalized parametric iterations, Hladik's
parametric-system bounds and randomized constructive Tchakaloff hits
remain unread leads, not essential inputs. No general fixed-support
family theorem or total-work result for our G was established.

Local progress is the newly checked source mechanism for a bounded
known-method specialization; no progress beyond the inspected general
results, family feasibility, scalar value, S3/H2 sign or RH is claimed.
All downstream contracts and unresolved gaps in the nomination remain.
Full matching Mathlib coverage has not been checked. No lemma,
mathematical script, PROOF/DAG or shared/runtime file is changed733.
