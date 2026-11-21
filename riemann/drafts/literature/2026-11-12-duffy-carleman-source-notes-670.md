# Duffy finite-cell source comparison670

Literature-only review of the exact TARGET in assessment669. Main gap:
L030-L032/C032a actual-Xi positivity and signed S3 coupling. Intermediate
use: one paid positive square term in a later full residual Gram, never
the whole Gram or a sign certificate. No lemma or mathematical script is
authorized in this turn. Preserve all earlier unfinished work.

Read C998e Sections1-2, especially(6)-(8), and C998a exact definitions
and Section1. C998e's product/conjugation/Fubini/projection argument is
still unaudited. Read the exact657/660/662 stop records: their prescribed
pointwise services exceed the ceiling; they are not lower bounds for
coefficient-coupled square integration. Reuse ready655/comparison656's
Trefethen19.3 and Johansson inclusion coverage and662/comparison663's
Folland coverage. No new general integration theorem is needed from
those sources and no source reproof is justified.

## Search and primary sources actually inspected

Queries included `Duffy transformation logarithmic singularity quadrature
error bounds analytic corner Gauss`, `Duffy 1982 quadrature over pyramid
cube singularity vertex pdf`, `Schwab quadrature singular surface integrals
Duffy analytic exponential convergence logarithmic pdf`, `Petras self
validating integration analytic functions error bounds logarithmic
singularities pdf`, `Duffy Carleman quadrature square kernel`, and
`Hermite Genocchi divided differences theorem integral Baxter Brummelhuis
pdf logarithm`. These searches did not identify a turnkey fixed-data
certificate. This is not an originality claim. Search extracts were leads,
not theorem evidence. The relevant notebook search covered12November
literature/attempt/history records, not sibling proofs or checkpoints.

**Transformation.** Mousavi--Sukumar, *Generalized Duffy transformation
for integrating vertex singularities*, Computational Mechanics45(2010),
127-140, DOI10.1007/s00466-009-0424-1,
[repository copy](https://escholarship.org/content/qt3fk9s522/qt3fk9s522.pdf).
Read Section2/(1a)-(1b), pp128-129; Section3.1, pp129-130;
Section3.3, p131; Appendix A, p137 (PDFp12).
The two-dimensional map is x=u^beta,y=u^beta v, with Jacobian
beta*u^(2beta-1). For polynomial p divided by r^alpha, the mapped
radial factor is u^(2beta-1-alpha*beta). Their radial exactness argument
requires a polynomial numerator and suitable integer powers; finite
cosines do not meet that polynomial premise. Section3.1's numerical
reference comparisons are not rigorous error certificates. We import
the substitution method, not an error constant, favorable node count,
or a claim that our logarithmic kernel becomes smooth. Original
Duffy1982 is an unread historical reference, not an essential input.

**Singular tensor quadrature.** Chernov--von Petersdorff--Schwab,
*Exponential convergence of hp quadrature for integral operators with
Gevrey kernels*, [ETH SAM Report2009-03](https://www.sam.math.ethz.ch/sam_reports/reports_final/reports2009/2009-03.pdf),
January2009. Read Definition1.1/(1.7), printed p4;
Theorem2.3/proof p5; Definition2.4, Theorems2.5/2.7 and proofs
pp6-7; Proposition2.8 and complete proof p7. Its hypothesis is

    |D^nu g(z)| <= A0*A1^|nu|*(nu!)^delta
                   *|z1|^min(0,alpha-nu1),

uniformly for z in[0,1]^d with z1!=0, all multiindices nu,
some A0,A1>0,delta>=1,alpha>-1. With sigma in(0,1),b>0,
m=ceil(b*n^(1/delta)), its specified geometric composite rule in
coordinate1 and Gaussian rules elsewhere give error
C*exp(-r*N^(1/(delta*d+1))) for some C,r>0.
The proof separately pays the terminal interval(2.13) and uses positive
normalized weights to propagate uniform parameter bounds. Those constants
and function-evaluation counts are not our finite scalar work bound.
Also read Assumption4.1 and Theorems4.2/4.5 statements pp18-19:
their stronger transformation result has additional hypotheses and is
not imported. Published version: ESAIM M2AN45(2011),387-422,
DOI10.1051/m2an/2010061; its PDF retrieval failed, so statement numbering
here refers only to the accessible report. No persistent source blocker.

**Coincident real nodes.** Baxter--Brummelhuis, *Functionals of
Exponential Brownian Motion and Divided Differences*,
[arXiv:1006.1996v1](https://arxiv.org/pdf/1006.1996v1),10June2010,
Section4, equation(4.2), printed p7, and Theorem4.2/(4.3)-(4.4), p8.
Read the n=1 proof case and the induction step. For f in C^n(R) and
not necessarily distinct real nodes, the divided difference equals the
simplex integral of f^(n) at their convex combinations. In particular
the n=1 integral uses f' and includes coincident nodes. This is a known
real-node tool for the later diagonal audit, not a floating-point
stability guarantee or a complex-ellipse theorem. Any logarithmic use
must restrict to a compact positive segment (and supply a C^1 extension
if invoking the globally stated theorem); it must not include zero.
No specialization to K_0 or new divided-difference identity is derived.

**Reuse.** Ready655/comparison656 already records the full proof of
Trefethen, *Approximation Theory and Approximation Practice*(2013),
Chapter19 Theorem19.3/(19.8), and Johansson,
arXiv:1802.07942v1 Sections2-2.1 plus Arb inclusion arithmetic.
Ready662/comparison663 supplies Folland2.37/2.39, finite products and
their exact hypotheses. Source-notes658's elementary precision passage
covers finite Taylor/rational interval design, not free special-function
calls. Re-read those relevant recorded passages; do not repeat browsing.
The Trefethen rule needs an actual bounded holomorphic extension on each
ellipse, with its(n+1)-point convention and affine interval factors.
Neither conjugation of complex arguments nor a real H1 bound supplies it.

## Scope decision and one bounded mathematical test

Decision SPECIALIZE: these known methods cover substitution, interior
error and inclusion, and a conditional singular tensor rule. They do
not prove C998e satisfies the displayed derivative hypothesis. The
alternative explicit proof may pay all remaining radial/angular strips
by integrable majorants, then use uniformly bounded holomorphic interior
panels. It must not cite Proposition2.8 if its one-singular-coordinate
hypothesis is false, nor silently apply it twice to an unverified corner.
No general quadrature theorem needs reproof. Local finite-cell formulas,
branch control, computable constants and cost are the identified
quantitative specialization, to be attempted only after separate approval.

Next test: independently audit C998e(6)-(8) before using its product;
then specify ONE Duffy/geometric-panel prescription for its square term,
retaining both parities, every off-diagonal column product and1/4.
Require combined corner, diagonal, panel, node/weight, coefficient and
finite-arithmetic error<=1e-10 per square-contribution entry and full
square-service work<=20000000 charged scalar operations. This is a
proposed test allocation, not an achieved bound or necessary accuracy.
Reserve<=10000000 separately for the audited diagonal setup; the rest
of the full100000000 ceiling must later pay ALL remaining terms.
This reservation makes the subtest discriminating without claiming that
the remainder suffices. A failed product audit blocks dependent quadrature.

Give each cutoff, panel count, degree and precision before a batch run.
Do not inherit11174 point queries or reinterpret function evaluations as
scalar operations. Couple the same exact six densities throughout; cache
identical values if justified, but charge all finite cosine/neutral
coefficient work, log/near-diagonal evaluators, constants, nodes, weights,
accumulation and register management under the retained work convention.
No assumption of polynomial radial exactness, constant-cost transcendental
calls, or cancellation of full-Gram cross terms is licensed. Real
conjugate traces require justified holomorphic extensions for complex
panel bounds. The defining integral in(6) is an available audit object;
subtracting nearby logarithms without an enclosure is not a diagonal rule.

Continue only with a passed identity audit and a complete finite
error/work ledger meeting both subtest thresholds. Otherwise preserve
the first precise analytic, inclusion or work failure and stop THAT
prescription without a parameter sweep. A loose sufficient upper bound
over budget is not a complexity lower bound. A later new mechanism needs
its own discriminating input rather than a renamed service657/660/662.

No transformed identity, regularity bound, new lemma, numerical enclosure,
mathematical script or feasible schedule has been produced in this review.
The advance is source coverage for one bounded known-method specialization,
subject to the supervisor's separate approval of newly ready coverage.

Essential local inputs for the next turn: C998a/audit655 and complete
654/655 evidence; C999q exact neutral completion; C998e(6)-(8) only AFTER
audit; C998f/audit669 for the separate setup reserve. Retain frozen652
SHA2562b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6,
ell=log(3)/2,a=ell/2 and the unchanged trial columns. C999/audit650's
floor and C999y/audit642's X are downstream, not quadrature inputs.
C744v/w/z,C999k,C999z/audit646 and all original analytic/arithmetic/
source-to-Xi/whole-core/c_* contracts remain unreplayed. C998b/c/d/e
remain unaudited. Full A-square, both mixed terms, moment integrals/
projection, residual size, inverse debt, S3 signs, higher/mixed endpoints,
C744q/H2, non-neutral coverage and global assembly remain independent.
Mathlib full matching coverage is unchecked. No cross-notebook input.
Creative central work is still blocked by the absence of a specified
signed S3 mechanism; this numerical specialization is not creative.

## Source-location repair671 (2026-11-12)

Recovery scope: the ready assessments669/670 referenced this note but
lacked direct source URLs in their SOURCE_EVIDENCE fields. Both now
contain the three primary PDF URLs already recorded above. All three
were retrieved successfully today. Rechecked Definition1.1/(1.7) and
Proposition2.8 with its full induction proof in SAM2009-03, and
Baxter--Brummelhuis Theorem4.2 with its base and induction cases;
Mousavi--Sukumar Appendix A again supplies the two-dimensional map.
This confirms the existing comparison, without expanding its scope:
uniform all-derivative bounds remain conditional, real coincident nodes
do not license complex-panel bounds, and polynomial exactness does not
cover finite cosines. No new theorem or numerical certificate is derived.
The remaining reused sources and precise versions stay as recorded above.
Mathlib matching coverage remains unchecked. This is a process repair,
not an additional mathematical advance or an exploration-budget reset.
