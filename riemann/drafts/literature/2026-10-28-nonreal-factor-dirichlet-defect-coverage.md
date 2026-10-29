# Finite nonreal-factor Dirichlet energy: completed source comparison

TARGET: Review finite-Blaschke Dirichlet-energy defect identities for an annular L471 pair-mass bound that avoids Q_epsilon's disk suprema.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched finite-Blaschke factor removal, Dirichlet defect identities, stronger inner-factor formulas and zeta pair-mass applications; checked the nominated local selected-energy comparison and L471/L474. No inspected theorem controls the annular actual-Xi mass or gives its required little-o; bounded search, not a novelty claim.
SOURCE_EVIDENCE: Carleson (1960), unnumbered Theorem p. 190 and Section 2 (1)--(3) p. 191, visually read in the GDZ primary scan; Dyakonov arXiv:1004.3591v1 Section 2 conventions and Lemma 3.1/(3.1)--(3.3), p. 8, plus its finite-factor application (3.4)--(3.6), pp. 8--9. Reuse L471 definitions/majorant, L474 Sections 1--4 and L465's already assessed normalization. Richter--Sundberg (1991) remains inaccessible and is not imported.
COMPARISON: The exact normalized defect is a nonnegative boundary integral weighted by the finite inner factor's derivative; the quotient need not be outer and unselected zeros may remain. Neither primary statement bounds the pair-divided interior mass by that defect or makes its actual-Xi aggregate little-o. Positivity of the defect is not a saving on its size.
GAP: An annular defect-to-pair-mass comparison and an actual-Xi estimate for the selected boundary energy would both be additional inputs. No such inputs were found; the existing continuous norm bound cannot be called a vanishing defect estimate.
REASON: Primary access is resolved for the needed finite identity, but the proposed implementation only introduces another uncontrolled positive functional. Park it under the stated continuation test; do not derive an annular bound or generic countermodel this turn. Nominate an independent scale-adapted test on d_j log T>1 for separate source review.
LITERATURE_REASON: The target changes from zero-selected disk suprema to energy lost upon removing finite nonreal factors; the necessary primary identity and its source scope have not been read.
SCOPE: Fixed 0<epsilon<1, pairs in P_T with epsilon<d_j log T<=1, multiplicities and clipped J_j(T); no assertion for d_j log T>1, individual signs, mixed positivity or RH.

## Exact question and bounded test

Use L474's f_k(w)=Xi(c_k+8w/log T)/A(c_k) on the unit disk.
Let B_k be the finite Blaschke product at the annular nonreal pairs
assigned to that cell, including all multiplicities, and G_k=f_k/B_k.
The analytic quotient is already covered by L474's finite-factor
argument. Define the standard Dirichlet integral notation
D(h)=pi^(-1) integral_(|w|<1) |h'(w)|^2 dArea(w).
These are definitions for source comparison, not a claimed defect
identity, sign, estimate or theorem application. Xi extends beyond
the disk and its selected finite quotient is holomorphic there.

The question is whether a precise source identity involving
D(f_k)-D(G_k) retains enough pair-specific boundary information to
replace the supremum bound in the annular portion of L471's B(T).
The desired downstream threshold is an o(T(log T)^3) bound for that
annular portion for each fixed epsilon. The small sector remains
L474's O(epsilon^3 T(log T)^3); the sector d_j log T>1 and all
pointwise/higher-sign questions remain independent gaps.

First retrieve only the primary theorem and its finite smooth-factor
proof case; do not load either entire book or a large source corpus.
Check whether factors need to include every zero, whether the quotient
must be outer, which boundary values are allowed, and exact constants
and multiplicities. An identity for an outer function alone must not
be applied directly to Xi or to a quotient with unremoved real zeros.
Reuse Bettin and the local gamma scope rather than re-auditing them.

Continue toward one creative proof attempt only if the comparison
identifies an explicit defect-to-pair functional and a bounded test
of its normalized size beyond the existing O(T(log T)^2) norm cost.
If it merely replaces that norm by an equally uncontrolled positive
term, record that obstruction and park this mechanism. Do not claim
that a generic analytic model settles the actual-Xi estimate.
If the primary case remains inaccessible, record the access evidence
and choose an independent covered target instead of an access-only
chain. No mathematical derivation is authorized by this assessment.

Potential future creative purpose: preserve a measurable energy cost
of nonreal factors that L474 loses when replacing each cell by its
supremum. The decisive test must distinguish a genuine saving from a
full-scale re-expression of B(T); a new name for its missing moment
does not count. Creative routing remains blocked by primary coverage
and by the absence of a demonstrated defect-to-mass comparison.

No cross-notebook input. Full matching Mathlib coverage is not checked.

## Completed source review, 28 October 2026

The nomination above is retained to fix the question and its original
continuation test. This completed step is LITERATURE / NOVELTY_UNCHECKED,
with outcome NEGATIVE: the theorem comparison changes the route decision,
without proving a new bound or refuting the annular target. No lemma,
mathematical script, dependency or main argument is changed.

### Primary identity and essential finite proof case

Lennart Carleson, *A representation formula for the Dirichlet integral*,
Math. Z. **73** (1960), 190--196, DOI
[10.1007/BF01162477](https://doi.org/10.1007/BF01162477).
The publisher PDF link redirects to metadata. The original scan is
available from the Niedersaechsische Staats- und Universitaetsbibliothek
Goettingen, [GDZ article LOG_0035](https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0073/LOG_0035.pdf),
in volume PPN266833020_0073. Its IIIF manifest locates printed pp.
190--196 at scans 200--206. Direct download succeeded although the
web reader failed. The PDF has a repository cover followed by the seven
article pages; its mathematical pages have no extractable text. Visually
read printed pp. 190--193, with p. 191 supplying the complete finite
case required here. The outer/singular-factor completion later in the
article is unnecessary and was not audited.

Carleson uses the UNNORMALIZED integral
`D_C(h)=integral_D |h'|^2 dArea`. On p. 191 Section 2 he writes
`f=b_a g`, initially with a nonzero disk zero a and g' continuous
on the closed disk. Partial integration gives his (1):

    D_C(f)=D_C(g)+(1/2) integral_(-pi)^pi
               [(1-|a|^2)/|exp(i theta)-a|^2]
               |f(exp(i theta))|^2 dtheta.

The proof explicitly proceeds by induction to (3), removing any finite
initial list of factors. It does not require the remaining g_n to be
zero-free or outer. Repeated occurrences are retained in the list;
there is no simplicity or separation hypothesis. The smooth finite
case uses partial integration and induction, not the subsequent infinite
limit. Read also the intervening approximation argument (2), but the
analytic-across-the-circle case here does not need it. The p. 190 theorem
separately lists a zero at the origin with its multiplicity m.

For a convenient primary statement including arbitrary finite inner
factors, read Konstantin M. Dyakonov, *Local abc theorems for analytic
functions*, [arXiv:1004.3591v1, 20 April 2010](https://arxiv.org/pdf/1004.3591v1#page=8),
Section 2's measures and Lemma 3.1, (3.1)--(3.3), p. 8. His domain is
bounded and simply connected with rectifiable Jordan boundary; the disk
is included. His seminorm is exactly `D(h)=D_C(h)/pi`. For g in that
Dirichlet space and inner B, Lemma 3.1 states

    D(g B)=D(g)+(1/(2pi)) integral_boundary |g|^2 |B'| ds.

He interprets the derivative as angular in general, then expressly uses
only finite Blaschke products. For a finite product on the disk all
boundary functions here are ordinary smooth functions. Read the proof
discussion citing Carleson and conformal invariance, and the full finite
application (3.4)--(3.6), pp. 8--9: its analytic quotient is not assumed
outer, and its boundary modulus is retained. This is a cited classical
identity, not a proposed new energy lemma. No conformal extension or
infinite-inner case is needed for our question.

### Hypothesis comparison with the nominated cells

L474 already proves that its finite selected B_k divides f_k analytically.
Here B_k contains exactly the annular selected zeros with their full
multiplicities; it need not contain all zeros in the disk. Since f_k is
entire and finite cancellation removes the selected zeros, G_k extends
holomorphically across the closed disk. Thus both derivatives are square
integrable there, and the finite smooth source hypotheses are adequate.
Real zeros left in G_k, including a zero at the cell center, do not
invalidate this identity. Boundary zeros of f_k are allowed as well;
the identity has no logarithm or division by its boundary value.

In the notation of the nomination the source identity is precisely

    E_k:=D(f_k)-D(G_k)
       =(1/(2pi)) integral_(-pi)^pi
            |f_k(exp(i theta))|^2 |B_k'(exp(i theta))| dtheta.

Replacing |G_k| by |f_k| on the boundary is the finite inner-factor
boundary-modulus property, not a claim about their interior values.
This records the source formula's notation and hypotheses; no new
defect-to-mass inequality or estimate for E_k is derived here. In
particular, E_k does not itself display the pair-divided F_j or the
clipped J_j(T) appearing in L471. Those data cannot be suppressed when
proposing a subsequent comparison.

### What the identity does and does not supply

The strongest relevant inspected conclusion is the exact nonnegative
factor-removal cost, with the finite product's multiplicities intact.
There is no vanishing parameter or arithmetic cancellation assertion
in either source statement. Knowing a positive norm difference does
not estimate that difference from above by a quantity tending to zero.
L474 (12) controls summed disk suprema at O(T(log T)^2), while the
annular goal requires o(T(log T)^3) for the pair mass. No conversion
from E_k to this required saving is present in the sources checked.

A possible later argument would need BOTH a bound of annular pair mass
by an explicitly normalized sum of defects and an estimate for that sum
which improves on the available full scale. Neither is being imported,
proved or assumed. A new name for this missing weighted norm fails the
nomination's continuation test. The identity's positivity alone is
insufficient grounds for a creative invocation, so park this mechanism.
This is a source-scope conclusion, not a theorem that every future
Dirichlet-energy method fails, and not a counterexample for actual Xi.

### Search, duplicates, inaccessible leads and next direction

Queries included `Carleson 1960 representation formula Dirichlet
integral Blaschke product finite D Bf D f formula`, `Richter Sundberg
1991 local Dirichlet integral formula inner factor finite Blaschke
pdf`, `Dirichlet integral Blaschke defect zeta`, `Local abc theorems
for analytic functions Dyakonov Carleson formula`, and `Blaschke
Dirichlet pair zeta energy`. The Dyakonov primary result was followed
to Carleson's finite proof rather than accepted from a search extract.
No matching actual-Xi annular saving was inspected. Search absence
does not establish novelty or an impossibility result.

Richter--Sundberg, *A formula for the local Dirichlet integral*, Michigan
Math. J. **38** (1991), 355--379, DOI 10.1307/mmj/1029004388, remains
unread: the Project Euclid PDF and old URL failed, and the download
iframe returned a security notice. No access circumvention was used.
It is not an essential blocker now that the needed finite global case
has been read in Carleson. Ross's survey Theorem 3.3 and the Primer's
Theorems 4.1.3/7.6.1 were search leads, not substitute primary imports;
their snippets are not proof evidence for additional conclusions.

The narrow duplicate check used L471's definitions and lost displacement,
L474's finite factors/continuous norm, the completed selected-energy
assessment, and its history. They already exclude calling a generic
bounded norm a selected little-o. Neither old stop proves the annular
target false. The inspected L473 audit history also confirms that its
finite-law audit is complete; repeating it is not an independent next
attempt, despite the stale audit wording in the supplied overview.

The independent remaining sector d_j log T>1 is not addressed by this
identity or L474's fixed microscopic disks. Nominate a source review of
scale-adapted disks and shifted second moments for that sector. This
changes the displacement regime and the size of real shifts, so the
small-shift Bettin specialization cannot be silently reused outside its
scope. No new inequality, reproof or ready creative target is asserted.
The main missing initial signs and global mixed positivity remain open.
Full matching Mathlib coverage is not checked; no absence is claimed.
