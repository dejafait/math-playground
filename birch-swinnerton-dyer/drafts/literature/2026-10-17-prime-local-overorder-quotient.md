# Prime-local first-overorder quotient certificate — source comparison

TARGET: Assess a prime-local mod-31 quotient certificate for the first overorder, replacing full integral ideal-power expansion with explicit denominator-clearing and integral generation witnesses.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Zassenhaus p-radical multiplier order modulo p endomorphism ring algorithm Round 2; Del Corso Dvornicich Simon non-maximal orders enlargement localization; p-maximal order computation mod p radical ideal quotient integral basis Cohen; and Stevenhagen Proposition 9.3 multiplier kernel. Inspected the primary Stevenhagen chapter, not just its indexed excerpt. Targeted local comparison used L077, C077a, the first-31-overorder assessment, the maximal-order source notes, histories 292/293 and ATTEMPTS/041; no completed local overorder certificate is recorded there.
SOURCE_EVIDENCE: Peter Stevenhagen, The arithmetic of number rings, in Algorithmic Number Theory, MSRI Publications 44 (2008), pp.209--266, Lemma 6.4 p.221 and Section 9 pp.233--235, especially equation (9-2), Proposition 9.3 with proof and the full following kernel/lifting paragraph p.235, inspected at https://library.slmath.org/books/Book44/files/08psh.pdf . Reused Del Corso--Dvornicich--Simon, Acta Arith. 120 (2005), Proposition 9/Theorem 2 pp.238--240, DOI 10.4064/aa120-3-2, with the previously inspected proof coverage in the first-31-overorder assessment; checked its multiplier-order identification against the newly inspected source.
COMPARISON: Stevenhagen explicitly computes the same radical multiplier order as (1/p)ker[O -> End_Fp(I/pI)] and supplies its lifting rule; Del Corso--Dvornicich--Simon identifies that order with O_H+(1/31)B^46 U. Thus full action-kernel and integral preimage witnesses can identify the exact source lattice without expanding B^46. A dimension-two subspace alone still does not do so.
GAP: No essential theorem gap remains for this known-method first-enlargement mechanism. The actual radical, full action kernel, two integral preimage bases, inverse transports, complete products and computed index are still absent, and feasibility within the unchanged caps is unproved.
REASON: The source supplies the missing replacement mechanism, including the correct quotient I/pI and integral lifts. A later fixed-field implementation is justified; neither a new general identity nor a new overorder is proved in this literature turn.
SCOPE: Original audited L067/L077/C077a, entire degree-48 field, H=343h, prime 31, gcd T^2+24 and a degree-46 lift U only; no L026, new prime, residual factorization, second enlargement or cross-notebook premise.

LITERATURE_REASON: Step 293 changed the certificate mechanism after its byte-cap failure; essential coverage of the full action on I/pI and exact reconstruction was missing at invocation start. This review supplies it and does not repeat the already covered nonmonic construction theorem.

The main BSD gap remains arbitrary-curve rank equality at complex order at
least two. A successful future first correction could support complete
units/classes and L066 descent arithmetic; maximality, all index primes,
localization and rational membership remain independent missing inputs.

## Primary statement and essential cases inspected

Use [Stevenhagen's published chapter](https://library.slmath.org/books/Book44/files/08psh.pdf#page=27),
Section 9, pp.233--235. Here O is an order in a number field K, p is a
rational prime, and I is the radical of pO. The source computes I/pO as
the kernel of an iterated Frobenius on O/pO, choosing p^k greater than
its dimension. It then uses the entire O-module I/pI. If phi is the
action of O on I/pI and N=ker(phi), the stated construction is

\[
 (I:I)=p^{-1}N,\qquad pO\subseteq N\subseteq O.
\]

The paragraph following Proposition 9.3 states that lifts of a full
F_p-basis of N/pO, divided by p, generate the enlarged order over O.
The preceding argument places it between O and p^(-1)O; Lemma 6.4 gives
integrality from preservation of the finite module I. Proposition 9.3
proves strictness when O is not p-maximal. We import these statements,
including the published lifting rule, rather than proposing a new
quotient identity. This is not an action merely on I/pO or O/I.

The source's hypotheses and complete relevant cases were read: definition
of the p-maximal extension on p.233; radical and Frobenius criterion;
zero-radical versus singular/ramified case; multiplier bounds; strictness
proof; and the full action/kernel/lifting paragraph on p.235. Lemma 6.4's
finite-module determinant argument on p.221 was also read. The first
library2.msri.org PDF request timed out; the SLMath publisher mirror
returned the complete chapter. No essential source remains inaccessible.

Reuse the [earlier nonmonic assessment](2026-10-17-first-31-overorder.md)
for the complete Del Corso--Dvornicich--Simon theorem and proof. Its
Proposition 9 and Theorem 2(ii) concern exactly (I:I) for I=rad(31O_H).
Their equality with O_H+(1/31)B^46 U therefore identifies the integral
source lattice once the **whole** kernel preimage is certified. This
uses two named descriptions of the same object, without asserting that
B is globally trivial or that its power has been computed. Direct
generator logs for B^46 are unnecessary under this alternative proof
of source identification. Both integral lattice reconstructions in the
new representation remain mandatory, as specified in the construction
assessment below.

## Applicability and necessary finite witnesses

Take O=O_H from audited L077 inside audited L067's entire degree-48
field. An order is finite free over Z, so 31 is not a unit; no monogenic
or integral-t hypothesis is used. Apply the stated Frobenius criterion
with k=2, since 31^2>48. This is a source specialization, not an evaluated
Frobenius matrix. C077a supplies non-31-maximality and deg G=2, so the
already covered theorem predicts first-enlargement index 31^2=961.
The actual kernel dimension and index must still be independently checked.

The exact reconstruction obligations are finite and separate:

1. For I, certify the **full** Frobenius kernel, lift its basis in O,
   and reconstruct the integer lattice generated by those lifts and
   31 times every original basis element. Record a rank-48 integral
   basis and coefficient matrices proving both generator containments.
2. In that integral I-basis, reconstruct multiplication by every old
   basis element, checking integrality before reducing modulo 31.
   These are actions on I/31I, not actions on its image in O/31O.
   Certify the full stacked action matrix and its full kernel, with
   independently checked rank as well as kernel membership.
3. For N, reconstruct the preimage lattice from all kernel lifts and
   31O, again with explicit generation matrices in both directions.
   Divide its basis by 31, as in the cited lifting rule. Full basis
   inverses, old-order containment, exact index and integral new products
   still need verification in K; no local-only basis is substituted
   for a global Z-lattice.

These are proposed certificate requirements, not results of a calculation.
The source theorem bridges this exact reconstruction to the original
nonmonic source lattice. No unassessed polynomial replacement, denominator
discarding, new prime or second enlargement is licensed.

## Duplicates, failure comparison and decision

The earlier maximal-order notes mention Frobenius kernels and general
multiplier algorithms, but did not assess this certificate or inspect
Stevenhagen's exact I/pI kernel/lifting statement. Stein's incomplete
displayed stopping proof and implementation excerpts are not relied on
for the new theorem-level coverage. The prior full-power assessment is
reused for nonmonic hypotheses, not repeated as a new result.

ATTEMPTS/041 and all step-293 partial outputs remain intact and excluded
as premises. The proposed mechanism begins from original audited inputs
and computes one radical and one action kernel; it neither resumes nor
compresses the stopped ideal-power operation log. Complete matching
Mathlib coverage was not checked; no absence or novelty claim follows.

The source comparison is useful local progress because it removes an
essential coverage gap and permits a different, independently testable
finite certificate. It establishes no mathematics beyond the sources
checked, no computed overorder, maximality, class/unit completeness,
Selmer bound or rank advance. A proposed construction and its bounded
continuation/abandonment test are recorded in
[the construction assessment](2026-10-17-prime-local-overorder-construction.md).
That newly written ready assessment receives the supervisor's separate
approval on a later turn; no mathematical implementation runs here.
