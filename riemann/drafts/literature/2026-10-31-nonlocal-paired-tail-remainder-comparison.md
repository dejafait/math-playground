# Nonlocal paired-tail remainder — completed comparison

TARGET: Compare Planat 202608.1692 v1 Theorems 4 and 6 and their complete-block decomposition with L559, identifying whether nonlocal endpoint cancellation leaves an independently controlled signed remainder toward L233.
CHECKED: 2026-10-31
DECISION: IMPORT
SEARCH_EVIDENCE: Reused drafts/literature/2026-09-27-first-associated-parity-blocks.md lines 84--108 and the endpoint assessment; searched the specific 2026-10-31 paired-tail records for duplicates. Web queries: "202608.1692" "remainder"; "Nonlocal Cancellation" "Planat" theta. These locate the same v1 and the previously inaccessible Symmetry article; no signed theorem is inferred from snippets.
SOURCE_EVIDENCE: Michel Planat, Nonlocal Cancellation in a Theta-Kernel Decomposition of the Riemann Xi-Growth Derivative: An Obstruction to Phase-Aligned Blockwise Positivity, DOI 10.20944/preprints202608.1692.v1, posted 25 August 2026, https://www.preprints.org/manuscript/202608.1692 ; inspected primary HTML Sections 1.3, 2 Lemmas 1--3/proofs, 3 Proposition 1/Theorems 1--2/proofs, 4 Definition 2/Theorem 3/proof, 5 (38)--(50), Lemma 5/Theorem 4/proofs, 6 Lemmas 6--7/Theorem 5/proofs, and 7 Theorem 6/proof/Corollary 2. The page identifies v1 as latest and not peer-reviewed.
COMPARISON: The source uses L559's exact Phi, M, A, Q and complete blocks; its transverse expansion retains L559's two leading endpoints. Its master cancellation removes an earlier M-diagonal term, not those A-endpoints. The complete sum has an absolute exponentially small bound, not an independently signed residual. The negative-block conclusion supplies no L233 sign.
GAP: A lower bound for the complete residual uniform sufficiently near y=0 and at unbounded x is absent. Fixed-y estimates and compact-region block ratios do not supply it. The exact small-y identification with L233 needs a separate mathematical specialization.
REASON: The bounded source comparison is covered. IMPORT permits the qualified source comparison/obstruction only, not a positivity input or an independently certified reproof. Park citation-only positivity and independent-sector domination.
LITERATURE_REASON: L559 changed the proposed object from a boundary-free block to a complete nonlocal sum; the exact decomposition and signed-remainder hypotheses were essential unread coverage.
SCOPE: Fixed x>0, y>0, the explicit theta kernel, complete J_m blocks and the stated compact-region/fixed-y quantifiers. No uniform small-y estimate, global sign, numerical certificate or RH resolution is imported.

## Exact quantities and endpoints

Use L559's k=2x, W(a)=a sinh(2ya), E(a)=A(a,a), and
F(a)=partial_b A(a,a). Source (28)--(29), (38)--(39) are literally
L559's definitions. Its epsilon is W I1, not a boundary-free residual.
Lemma 5, (44), starts with

    I1=-E(a)cos(ka)/k+F(a)sin(ka)/k^2+...

Both endpoints whose deletion L559 refutes are retained. The source's
g1=-W E and g2=W F in (45) agree with those terms. This is a comparison
of printed definitions, not a new endpoint derivation.

Theorem 3, (31)--(37), starts with both terms of Theorem 1's double
integral. It cancels W(a)M(a,a)sin(ka)/k between T1 and T2, using the
moving-limit derivative of G=integral_0^a b sinh(2yb)M db. L559's proof
already distinguishes that diagonal from E and F. The later identity
therefore does not justify the earlier literal deletion. The exact
prefactor in the theorem and its proof is **2/x**, unlike the abstract:

    I(x,y)=integral_0^infinity [Q_y(a)sin(2xa)+epsilon_x(a;y)] da,
    partial_y |D(x+iy)|^2=(2/x)I(x,y).

Proposition 1 states Xi=4D. L019's displayed K and L020's entire cosine
representation are the matching local normalization references. No
new normalization lemma or small-y derivation is made this turn.

## Local estimates and excluded regions

Theorem 4 fixes y>0 and compact K strictly inside compact K1 strictly
inside (0,infinity). For sufficiently large x it applies uniformly
to alpha_m=m*pi/x in K, with J_m contained in K1:

    C_Q=-pi Q_y'(alpha_m)/(2x^2)
         -pi^2 Q_y''(alpha_m)/(4x^3)+O(x^-4),
    C_eps=pi [g1''(alpha_m)-g2'(alpha_m)]/(8x^4)+O(x^-5).

Its proof uses the full-period moments and all four terms of Lemma 5
before bounding the integral remainder. Constants (49) use fixed-y
derivative suprema on K1 and the compact triangle 0<=b<=a. Corollary 1
additionally requires inf_K |Q_y'|>0. Remark 4 excludes the origin,
stationary-envelope regions and the far tail from the ratio estimate.
It cannot be summed over all blocks with that same relative error,
nor applied to fixed m as x tends to infinity.

Theorem 6 chooses eta_y with Q_y'>0 on (0,eta_y], nondegenerate
K=[a_-,a_+] inside that interval, and delta=min_K Q_y'>0. It gives
C_tot<=-pi delta/(4x^2)<0 for alpha_m in K beyond x1(y,K). The proof
absorbs O(x^-3) and O(x^-4) into half the negative leading term and
then uses grid spacing pi/x<|K|. Lemma 6 supplies the increasing
interval from its small-a expansion; Lemma 2 supplies p'(0)>0.
Their proof cases, including the negative n=1 term and positive tail
bound in Lemma 2, were read. No independent arithmetic audit of its
decimal inequalities is claimed. This is a qualified source obstruction
to universal block positivity, not a sign of the total or a result on RH.

## Complete sum and missing sign

Theorem 5 fixes y>0, S=sum C_Q, E_sector=sum C_eps and S+E_sector=I.
It states complete opposite endpoint expansions, with leading terms
plus/minus y p'(0)Phi(0)^2 x^-5 and E_sector/S tending to -1.
The proof of cancellation uses **S+E_sector=I and Lemma 7**, rather
than an independently signed transverse estimate.

Lemma 7 bounds |I| by C(y)x^A(y)exp(-pi*x/2). Its proof returns to xi
and xi', uses Stirling and polynomial zeta bounds on the bounded
vertical strip around s=1/2+y+ix, and a Cauchy disc of radius
min(1/2,y/2). This is an absolute upper bound; the shrinking disc does
not provide the needed uniform small-y assertion. No comparison of
the surviving residual to a positive term with smaller error appears.
Theorem 2's positive growth criterion is explicitly RH-equivalent;
using it to sign I would assume the goal.

The saved continuation test therefore fails: the complete quantity
is specified but no independently controlled signed remainder is
supplied. Separate algebraic expansions cannot supply the missing
lower bound after cancellation. This is informative source overlap,
not mathematical progress beyond the inspected sources.

## Route and continuation boundary

Keep L559's obstruction. Park unrestricted endpoint deletion, universal
block positivity and independent-sector domination as sources of a
first sign. Section 1.3 leaves grouping, correlations and resummation
open; that permission supplies no testable signed mechanism by itself.
The Symmetry article is now a search lead; its full text was not loaded
and is unnecessary for this completed comparison. No retrieval loop
is needed. No source blocker remains for this bounded review.

A separately nominated transfer audit can identify the exact y-to-zero
coefficient against L233 while retaining the full residual. It closes
a normalization/limit gap only and must not promote fixed-y magnitude
bounds to uniform signs. A creative sign mechanism remains blocked
until an additional signed estimate with an independent test is named.
Higher signs remain separate. No cross-notebook input was used.
Mathlib coverage of the complete source theorems is not checked;
absence and formal verification are not claimed.
