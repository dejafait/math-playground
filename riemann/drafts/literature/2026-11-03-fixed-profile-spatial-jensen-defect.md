# Source assessment: averaged spatial Jensen defect

TARGET: For one fixed actual L703 profile, test whether the angularly averaged spatial Jensen defect of L666's complete G_n on |u|=1/2 is o(n).
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 154 completed the step-153 local duplicate/failure comparison, reused the ready full-spatial and L705 source readings, and made eight bounded external queries on norm/Mahler comparison, zero concentration, analytic-sum transitions and moment polynomials. Primary statements and the relevant proof cases were inspected as recorded below; no exact-family matching estimate was identified and no novelty claim follows.
SOURCE_EVIDENCE: Reuse Brunault--Zudilin Propositions 1.4-1.5/Lemma 1.6, Issa--Lalin Remark 3.8/Theorem 4.1 and Ash--Novinger Theorem 4.8.3/Lemma 4.8.4 from the two named ready assessments. Rechecked Defant--Mastylo arXiv:1508.05556v1 Theorem 3.1 and sharpness pp.7-8; inspected Hughes--Nikeghbali (2008) Theorems 1-4 pp.734-738 and complete Theorem 4 proof, and Sokal (2004) Theorem 1.5 p.226, Lemma 3.7 pp.240-241 and all four proof cases pp.241-242.
COMPARISON: Known root/integrability and boundary-Poisson tools cover the proposed interfaces once their local nonzero hypotheses are checked. Generic norm bounds retain growing-degree costs; concentration results require unproved coefficient-height control; fixed finite analytic-sum limit-set results do not supply logarithmic transition control for this growing family. L669/L683/L698/L705 neither settle nor duplicate the normalized radius-1/2 average.
GAP: Prove J_sp(n)=o(n), or a rigorous positive lower limit of J_sp(n)/n, for the same actual fixed profile, retaining actual degree, nonzero slices, all transition regions and signed interior. No source inspected supplies the needed family-specific uniform logarithmic control. Angular amplitude, full compensation, H/support and Xi realization remain independent gaps.
REASON: Essential comparison is sufficient for one bounded direct family-specific attempt under EXPLORE, after separate approval of this newly completed assessment. Import the known tools by citation; establish every quantitative specialization later. This literature turn proves no defect estimate and changes no lemma or mathematical script.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED changed the observable from two endpoint means to a normalized angularly averaged spatial loss; this turn completes the missing exact-target theorem comparison, reusing adequate earlier readings.
SCOPE: Exactly TARGET for one actual L703 profile selected before n=12q+3, with constants/onset allowed to depend on that profile; complete L666 G_n, unit masses, anchor, inverse angle, j=0, both endpoints and all M=n/3 moments on |u|=1/2. Direct root/normalized-polynomial or signed finite-response arguments may test this exact defect; no transition expansion, root-distribution limit, relative approximation, reflection, amplitude lower bound or Xi bridge is approved as a fact.

## Invocation-start nomination (historical; completed comparison below governs)

The following nomination was saved in step 153 without external source
comparison. Its prospective proof routing remains conditional on the
separate approval of the completed assessment below.

### Proposed mathematical target, not an established estimate

Fix the same actual L703 profile as in L705 before n=12q+3 varies.
Keep L666's full finite family, unit masses, anchor, inverse angle,
j=0 factor, both endpoints and every M=n/3 spatial moment. Put

    m_n(u)=mean_(|z|=1) log|G_n(u,z)|,
    S_n(u)=max_(|z|=1) |G_n(u,z)|,
    J_sp(n)=mean_(|u|=1/2) [log S_n(u)-m_n(u)].

All means are normalized. The exact proposed threshold is J_sp(n)=o(n)
along the full allowed sequence, with constants/onset permitted to
depend on that fixed profile. This notation does not replace L666's
original diagonal D. Nonzero spatial slices, finiteness and the use
of actual degrees must be checked for these angular radii; they are
not waived by the definition. No lower bound on S_n, no angular
amplitude estimate and no relative approximation are assumed.

The proposed mechanism separates the spatial cancellation loss from
the size of the complete signed response. L705 suggests examining
the spatial shape after normalization: its endpoint argument prevents
simultaneous cancellation at two spatial points, but only at the two
negative-real angular points already audited. It does not establish
this circle average. A source-supported investigation would need to
control the spatial zero distribution or normalized analytic family
through angular transitions, retaining any interior contribution.
No particular transition expansion is asserted or approved here.

The possible downstream use is to convert a separately established
lower bound on the angular mean of log S_n into a lower bound on the
complete logarithmic mean in L657's radial accounting. That amplitude
bound remains independent and unproved. So do the inner-charge deficit,
outer annulus, H/support, Xi realization and actual-Xi positivity.
The defect estimate alone would not resolve any of those final claims.

Continue after source approval only with an identified mechanism that
can meet the sublinear loss, or a rigorous informative obstruction for
the same fixed actual profile. A positive lower limit of J_sp(n)/n
would stop this proposed sublinear transfer. A generic polynomial
counterexample, n-dependent displacement construction, scalar sample,
numerical Picard fit or failure of an upper certificate is not such
a counterexample. A useful intermediate estimate may leave the
amplitude lower bound and other independent gaps open.

## Reuse and nonduplication obligations for the next review

Start with
`drafts/literature/2026-11-03-full-spatial-root-contribution.md`
and the approved L705 audit assessment. Reuse their inspected primary
statements and proof cases; open only missing hypotheses or cases needed
for the new observable. Compare stronger norm/Mahler and zero-distribution
results with n-dependent degree and the exact signed rational family.
Do not treat fixed-degree continuity or a degree-proportional cost
as a sublinear estimate.

L669 allows the displacement vectors and their finite support to
change with the cancellation order and n; its fixed-angle result
neither gives this defect nor rules out the fixed-profile target.
L683 pays a generic root cost and leaves a signed norm lower bound
open; simply repeating that transfer cannot establish J_sp(n)=o(n).
L698's complete amplitude decay has a different angular radius and
does not by itself determine a normalized spatial shape. L687's
block-dual cost and L686's full-cube single-anchor limitation remain
preserved. None of these proofs is imported as a new premise here.
The local keyword search does not prove absence of another duplicate;
the source review must finish the comparison.

The mechanism differs from nested-radius anchor dominance, absolute
tail variation and endpoint-only global extensions: it concerns the
complete spatial polynomial after its own size is removed. It must
not discard the signed interior, angular exceptional sets or their
logarithmic contributions. No new lemma, script or result on this
observable is supplied by the nomination.

## Proposed proof routing after source approval

Nominate proof_attempt/creative, deep_research/max, only after the
missing exact-target source gate is completed. The precise obstruction
is that available generic norm-to-Mahler losses are linear in growing
degree, while complete angular compensation needs a sublinear loss.
The bounded test is the displayed J_sp(n)/n limit for the same actual
profile, retaining transition regions. Establishing sublinear spatial
cancellation, or a rigorous positive limiting loss, would change a
central local charge decision. This is a proposed new mechanism, not
a reclassification of today's conceptual audit of a source-based
specialization.
The immediate next invocation remains literature_comparison,
standard/high; no proof attempt is approved in this nomination.

Full matching Mathlib coverage is unchecked. Existing root and Mahler
support is not a formalization of this averaged asymptotic.

## Completed comparison — 3 November 2026, step 154

This completes the source gate for the unchanged TARGET under EXPLORE.
It is a literature EXPLORATION, not an estimate, a proof audit or a
finding of originality. Separate approval of this changed assessment
precedes research. No essential source is blocked.

### Reused primary inputs and their exact interface

Reuse the inspected readings and proof qualifications in
[the full-spatial assessment](2026-11-03-full-spatial-root-contribution.md)
and [the L705 audit scope](2026-11-03-inner-annulus-anchor-obstruction-audit-scope.md).
Their previous targets differ; the present application comparison is
new, while the underlying general theorems are unchanged.

F. Brunault and W. Zudilin, *Many Variations of Mahler Measures*,
ISBN 9781108794459, [Propositions 1.4-1.5 and Lemma 1.6,
pp.6-8](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf),
cover nonzero complex polynomials of any finite actual degree. The
root formula counts multiplicities, zero roots and circle roots; its
leading coefficient is the actual one. The saved boundary-arc proof
reading is reused. These exact identities do not assert sublinear
supremum-versus-mean loss for the present signed slices. Changing the
leading coefficient or degree along u must not silently change the
normalization used in J_sp.

A. Defant and M. Mastylo, [*Lp-norms and Mahler's measure of polynomials
on the n-dimensional torus*, arXiv:1508.05556v1](https://arxiv.org/pdf/1508.05556v1),
23 August 2015, Theorem 3.1, PDF pp.7-8, states
||P||_p <= product_j Lambda(p,d_j) M(P) for 0<p<infinity,
separate degrees d_j and normalized torus measure, with
Lambda(p,d)=||(1+z)^d||_p. Its product extremizers and sharpness proof
were rechecked. The theorem does not state p=infinity; an endpoint
use must justify that limit rather than attribute it to the displayed
statement. Its sharp growing-degree cost does not give the requested
sublinear loss. Reuse Theorem 4.2, PDF p.11, for measurable E of
measure at least theta>0: its interpolation factor still contains
Lambda(p,m) in the separate degree m. It supplies no family-specific
small-value estimate through angular transitions. No reproof is needed.

Z. Issa and M. Lalin, [*A generalization of a theorem of Boyd and
Lawton*, arXiv:1203.5379v1](https://arxiv.org/pdf/1203.5379v1),
24 March 2012, Remark 3.8 and Theorem 4.1/proof, p.7, s=1,
cover absolute logarithmic integrability for a nonzero complex
polynomial on a finite-dimensional torus, including torus zeros.
This supports finite-n Fubini for a nonzero rescaled numerator
K_n(v/2,z); it does not give an n-uniform small-value constant or
uniform integrability after division by n. Clearing Q does not
permit dropping its poles or using its angular degree as a spatial
degree. L657's stated nonzero-slice conclusion is on |u|=1;
its extension to the new radius must be checked, rather than cited
verbatim. Individual W_a may have zeros there. Possible exceptional
slices and any removable rational singularities require explicit
treatment in the later attempt, even if they form a null set.

R. B. Ash and W. P. Novinger, [*Complex Variables*, Theorem 4.8.3
and Lemma 4.8.4, printed pp.33-36](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesWithHyperlinks.pdf#page=94),
apply to an analytic function on a neighborhood of the closed disk,
not identically zero, evaluated at an interior nonzero value. Reuse
the inspected boundary-factor proof and Corollary 4.7.4's kernel
normalization. Boundary zeros are allowed. A spatial Poisson lower
bound still needs a paid interior value and boundary upper control;
neither exists uniformly over the new angular circle by citation.
L705's two-point alternative at u=-1/2 is not such a circle-wide input.

### Additional primary comparisons

C. P. Hughes and A. Nikeghbali, [*The zeros of random polynomials
cluster uniformly near the unit circle*, Compositio Math. **144**
(2008), 734-746](https://web.williams.edu/Mathematics/sjmiller/public_html/cmu/21-499/handouts/polyzeros/HughesNikeghbali_CompMath_ZerosRandPolyClusterUnifNearUnitCircle.pdf),
DOI 10.1112/S0010437X07003302: inspected Theorems 1-4, pp.734-738,
and the complete Theorem 4 proof. For degree d with a_0*a_d!=0,
put L_d=log(sum|a_k|)-(log|a_0|+log|a_d|)/2. Theorems 1 and 3
give uniform angular clustering and radial count control when
L_d=o(d); the latter bounds the fraction outside
[1-rho,(1-rho)^(-1)] by 2L_d/(d*rho), 0<rho<1.
Theorem 4's proof uses Jensen at zero and the reciprocal polynomial
for the two radial tails. No randomness is needed for these statements.
For the present slices, endpoint coefficients can vanish and no such
height control has been proved. This is a sufficient coefficient
condition, not an automatic consequence of unit original masses.
Neither the count conclusion alone nor a bare weak zero limit supplies
the uniform logarithmic control required for this defect. No clustering
result is imported for G_n.

A. D. Sokal, [*Chromatic Roots are Dense in the Whole Complex Plane*,
Combinatorics, Probability and Computing **13** (2004), 221-261](https://discovery.ucl.ac.uk/id/eprint/9064/1/9064.pdf),
DOI 10.1017/S0963548303006023: inspected Theorem 1.5, p.226,
Lemma 3.7, pp.240-241, and all four proof cases, pp.241-242.
On a domain, take fixed finite m>=2 and fixed analytic, nonidentically
zero alpha_k,beta_k, excluding proportional unit-modulus bases whose
common dominance set has interior. For f_n=sum alpha_k*beta_k^n,
the limiting zero set comprises dominant-amplitude zeros and ties.
The proof handles unique dominance, a vanishing dominant amplitude,
all bases zero and competing dominance separately. Lemma 3.7 gives
compact logarithmic convergence in unique-dominance regions, not a
transition logarithmic integral. The displayed G_n has growing node
and spatial-moment counts and n-dependent product factors; no fixed
representation satisfying these hypotheses is available. Endpoint
asymptotics cannot be substituted for one. Thus this theorem is a
scope contrast, not a source for the proposed defect estimate; its
zero-limit conclusion also supplies no needed transition rate.

### Bounded search, duplicates and limits

The eight external queries were:

- `"polynomials" "Mahler" "supremum" "zeros" norm comparison`
- `"zeros" "polynomials" "Erdos" "Turan" "Hughes" "Nikeghbali"`
- `"Sokal" "Beraha" "Kahane" "Weiss" analytic functions theorem`
- `"polynomial" "Mahler measure" "supremum norm" "2"`
- `"logarithmic" "supremum" "Jensen" "polynomials" "defect"`
- `"Mahler measure" "moment polynomials"`
- `"Mahler" "Jensen defect" polynomial`
- `"Mahler measure" "power sums" "norm"`

The new inspected comparisons above were retrieved from primary
papers, not their search snippets. Other hits concerned arithmetic
Mahler measures, moment integrals over coefficient spaces, special
polynomial families or unrelated meanings of Mahler. The norm search
also located *Near-isometric duality of Hardy norms with applications
to power inequalities*, *Heights of polynomials over lemniscates*, and
a Rudin-Shapiro discussion. These remain unread leads: no theorem
from them is used or claimed inadequate after inspection. No adequate
exact-target match emerged from this bounded search; this does not
establish novelty or the absence of a stronger theorem. The primary
papers used were accessible; no source-access recovery is required.

The local comparison read L666's complete definition and rational
continuation, L703's fixed-profile hypotheses and conclusion, L657's
statement and nonzero/integrability proof interface, and the relevant
L669/L683/L698/L705 statements. It reused step 153's scoped search and
read the block-dual and exact single-anchor stop records. L669 changes
the displacement vector with cancellation order and n and studies
u=-1; it does not decide the fixed-profile normalized average.
L683 pays a generic spatial root cost before an angular maximum;
its linear loss is precisely what this target seeks to avoid.
L698 controls complete amplitude on a unit angular arc, without
relative normalized-shape control on |u|=1/2. L705's isolated-angle
means obstruct anchor dominance, without deciding this defect.
The block-dual and clearing failures concern their own observation
costs; neither becomes a counterexample to this different observable.
No historical stop is treated as a global prohibition.

### Ready scope, continuation and Mathlib

One direct family-specific attempt is justified after separate approval.
Use the exact TARGET, not an all-displacements uniform replacement or
a fixed-angle variant. The essential mathematical inputs are L666,
L703 and L657; L705 supplies audited endpoint information only.
Actual spatial degree is at most M-1 and may drop. The later attempt
must establish well-defined nonzero slices and finite means at the
new radius, then test whether normalized spatial shape permits a
sublinear angularly averaged logarithmic loss. Splitting angular
regions is permitted only with the transition contribution paid.
No assumed two-endpoint expansion, root separation, symmetry,
relative error or amplitude lower bound is part of this approval.

The bounded decisive test remains J_sp(n)=o(n) on the full allowed
sequence, or a rigorous positive lower limit of J_sp(n)/n for the
same fixed actual profile. A useful intermediate estimate may leave
independent gaps open, provided it gives a concrete paid mechanism
toward that threshold. A finite sample, generic polynomial example,
failed upper certificate or n-dependent replacement profile does not
stop or establish the target. An inconclusive attempt must save its
partial reasoning and identify a new input or refined mechanism
before repetition. This assessment resets no exploration counter.

The possible downstream use remains conversion of a separately proved
angular mean lower bound for log S_n into the complete logarithmic
mean in L657's radial accounting. That amplitude lower bound, the
remaining inner deficit, outer annulus, H/support, Xi realization and
actual-Xi signs remain unproved. No RH candidate is proposed.

Full matching Mathlib coverage is unchecked. Reuse the supporting
[MahlerMeasure module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html)
names recorded in the full-spatial assessment, including
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`
and `Polynomial.norm_coeff_le_choose_mul_mahlerMeasure`;
these are not a formalization of the averaged asymptotic. No new
coverage claim or independent Mathlib audit was needed here.

Prospective research routing after approval: proof_attempt/creative,
deep_research/max. The precise central obstruction is the gap between
generic degree-proportional cancellation loss and the required o(n)
loss for full angular compensation. The bounded test is the exact
fixed-profile defect limit above, retaining transitions. This is a
new mechanism to investigate, rather than reproduction of a norm
inequality or reopening the anchor-dominance certificate. Today's
actual completed task is literature_comparison, with no new theorem.
