# Local signed collision flux — nomination959, source review960

TARGET: Assess source coverage for a collision-defect-free distributional Stokes identity for the localized space-time pullback of q^2 exp(-H) dq wedge dz under C466s's stopped raw flow.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Review960 searched raw singular-flow Stokes/zero extension, logarithmic-divisor pullback currents, removability of differential forms, rough transport and Lefschetz worldvolume boundary terms; read the primary passages and scoped local comparisons below. No exact matching theorem was identified; this is bounded coverage, not a novelty claim.
SOURCE_EVIDENCE: Harvey–Polking Acta Math.125(1970)39–56, Theorem2.1/Lemma2.2 with proofs pp40–41, Theorems4.1–4.2 and proofs pp45–46, Section5/Theorem5.2 and Green-formula proof pp48–49 https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6102-11511_2008_Article_BF02838327.pdf; Seguin–Hinz–Fried AMR66(2014)050802 Sections2.4/3/4 https://pmc.ncbi.nlm.nih.gov/articles/PMC4240036/; Fukuma–Matsumoto arXiv2012.08468v1 Section1(1.5)–(1.12), Section3.1(3.1)–(3.4) https://arxiv.org/pdf/2012.08468v1; TNV1706.03822v2 Section2.2/footnotes1–2 https://arxiv.org/html/1706.03822v2#S2.SS2. Reuse WKM/TNV variational coverage954/955/957, without another audit.
COMPARISON: General removability needs coefficient integrability plus neighborhood-mass, geometric-size or trace hypotheses; rough transport needs an appropriately evolving chain, or smooth invertible convection. None of these is supplied for the stopped survivor boundary by C466s. The sources support a bounded cutoff-flux proof attempt, not direct import of the identity.
GAP: Complete-form local integrability, control of the survivor-cutoff error at collisions and r=0, and passage to zero extension remain unproved; the full gamma_chi cutoff term must remain. Neither a regular hitting surface nor small geometric size of its parameter-space preimage is assumed.
REASON: Essential source comparison is now sufficient for one established-tool attempt; no persistent essential source blocker was found. The exact bounded continuation is nominated in assessment960 for separate next-turn approval. This source-only step establishes no new estimate, trace, identity or sign.
LITERATURE_REASON: The complete space-time current identity, unlike the ready fixed-time absolute-density target, needs essential coverage of weak exterior derivatives and stopping defects.
SCOPE: Source review only; unchanged C466s bidisk/raw-flow data, compact ambient cutoff, finite open time interval, test forms compact in the initial-parameter rectangle; no estimate, current identity or boundary trace is asserted by this nomination.

## Exact proposed question for source comparison

Retain all C466s hypotheses: 0<a<R, 0<b<L, finite common M_1,M_2,
fixed complex H_0, holomorphic H on B with its stated Hermitian
derivative bounds, initial (ir,s), unit flat raw flow, and maximal
survival in U=B minus {q=0}. Fix 0<T_0<infinity. Let
Q=(0,T_0) times I and let D_H be its surviving subset, excluding
r=0. Write Psi(t,r,s)=X(t,r,s) on D_H. No stopped map through the
divisor is defined. Let Omega=q^2 exp(-H) dq wedge dz on B and
choose an arbitrary smooth compactly supported scalar cutoff
chi on B.

The proposed source question concerns the coefficientwise zero
extensions to Q of the forms

    beta_chi = Psi^*(chi Omega) on D_H,
    gamma_chi = Psi^*(dchi wedge Omega) on D_H.

Are both extensions locally integrable, and does

    d beta_chi = gamma_chi

hold as distributions on Q, without an extra distribution supported
on the collision/stopping locus? This is a question, not a claimed
theorem or an inference from the fixed-time modulus. It includes the
artificially excluded initial-coordinate set r=0 and collisions
occurring within the support of chi. Compact support inside B
localizes away from the outer physical boundary; the explicit
gamma_chi term retains the cutoff cost. Test forms have compact
support in Q, so no initial/final time or parameter-edge term is
silently set to zero. Any eventual integral-invariance statement
would have to restore and pay those other boundary terms.

The source review must retain the complete pullback, including its
dt wedge dr and dt wedge ds coefficients. C466s controls only its
dr wedge ds coefficient after weighting. It supplies no cited
theorem on extension of this entire form, no distributional trace,
and no permission to interchange a singular limit and Stokes.
Local integrability is part of the proposed target, not an assumed
precondition for the displayed equality. No uniformity over
unbounded time, noncompact cycles or all contour orders is proposed.

## Bounded review and continuation test

Search exact and stronger terminology for singular-flow pullback
currents, zero extension across a logarithmic divisor, and relative
Stokes/transport identities for holomorphic top forms. Retrieve
primary theorem hypotheses and the essential zero-hit or boundary
case before broader excerpts. Reuse the inspected nonsingular
variational and compound tools; do not repeat their approval.
Separate any theorem requiring a proper smooth homotopy, finite
mass/current boundary, a regular hitting surface or a complete
modified metric from the stipulated raw stopped flow.

Continue only if a precise theorem imports the proposed identity,
or adequate primary coverage isolates a bounded proof/obstruction
test for its missing mixed minors and collision defect. If a
regularity or mass hypothesis is unpaid, preserve it as the explicit
gap; do not silently strengthen the premises. If an essential source
is persistently inaccessible, park the dependent target rather than
retrying that retrieval. No new estimate or lemma may be derived in
this next, literature-only step. A later mathematical attempt needs
its own approved matching scope.

## Recovery comparison and limitations

Three candidate directions were compared for nomination, not tried:

1. Change to the original-coordinate metric. This addresses a real
   application hypothesis but again seeks absolute volume control
   and does not by itself pay a signed boundary term.
2. Extend the absolute estimate to intersecting divisors. This is
   another unpaid local hypothesis, likewise leaving the signed
   deformation identity unresolved.
3. Study the distributional collision flux of the complete
   space-time form. Selected because it directly tests a missing
   signed-transport premise, is localized and independently
   falsifiable, and does not require pointwise positivity.

Stops927/932/941 rule out the recorded common-product phase,
conditional iid-square, and original marginal pointwise-sign
shortcuts, respectively. Stop947 rejects the finite-jet sign
discriminator; stop948 rejects unsupported collision smoothness as
a necessary phase condition. None of those mechanisms is proposed
here. In particular this question does not impose smoothness of a
collision-divided phase or infer signs from a modulus. Their evidence
and unfinished mathematical work remain unchanged.

Essential local input for later applicability is C466s; C466r/C466q
remain scalar comparisons, not additional premises. The global
target remains L030-L032/C032a actual-Xi all-degree algebraic-square
positivity. Even a defect-free local identity would leave the signed
integral's sign, original-coordinate metric, intersecting divisors,
global homology, noncompact/other endpoints, all orders and actual-Xi
realization open. No cross-notebook result or full matching Mathlib
theorem is imported; matching Mathlib coverage is unchecked.

No justified central creative sign mechanism has yet been isolated:
the link from a paid signed deformation to the actual determinant
sign is still missing. This source nomination prepares a concrete
boundary-payment question, not a creative classification by fiat.
At nomination959, REVIEW_REQUIRED deliberately left the new scope unapproved.
The completed audit959 remains valid independently of this nomination.

## Completed bounded source review960 — 14 November 2026

The exact question above was retained. No lemma, mathematical script,
cutoff estimate or counterexample was constructed. C466s was read in
full, including audit959; records954/955 and stop959 were checked.
Narrow searches of the collision/weighted-flow records found no local
proof of this identity. Stops927/932/941/947/948 were read: their
phase, conditional-independence, marginal-sign and local-jet
mechanisms do not settle a weak signed-transport identity. In
particular, stop948 does not justify imposing smooth collision phase
or smooth hitting boundary as a necessary condition.

Queries included `holomorphic gradient flow zeros determinant boundary
Stokes theorem singularities`, `flat differential forms removable
singularities distributional exterior derivative cutoff L1`,
`"gradient flow" "zero extension" "Stokes"`, `"Lefschetz" "Stokes"
"boundary" "zeros" flow`, `"pullback" "differential forms"
"removable" "flow" logarithmic`, and `"worldvolume" "Lefschetz"
"boundary" zeros`. Follow-up searches located the primary
Harvey–Polking paper and rough-transport article. No adequacy or
novelty claim is based on search snippets or secondary summaries.

### Primary theorem comparison

**Harvey–Polking (1970).** The primary PDF cited in SOURCE_EVIDENCE
was read at the stated pages, including the cutoff and Green-formula
proofs. For a smooth-coefficient matrix differential operator P of
order m, relatively closed A, and f in L1_loc, Theorem2.1 assumes
Pf=0 off A and
liminf_{epsilon->0} epsilon^(-m)||1_{K_epsilon}f||_1=0
for every compact K subset A; it concludes Pf=0 everywhere.
Lemma2.2 supplies smooth cutoffs with derivative bounds O(epsilon^(-j)).
Theorem4.1(b) instead requires bounded f and H^(n-m)(A)=0;
finite measure alone does not suffice. Theorem5.2 assumes f smooth
off a smooth hypersurface, Pf=0 there, normal order k>=1 and equal
weak one-sided normal jets through order k-1; the resulting
distributional extension solves PF=0. Its proof retains jump terms.
Identification with an L1 zero extension also needs checking here.
These hypotheses have not
been checked for our complete forms. The proposed equation is
inhomogeneous; its operator/unknown formulation must also be
justified in a later application. The ambient complex divisor's
dimension is not a bound on the stopping locus in Q. The stopped
complement itself is not stipulated to be a thin exceptional set.
Thus neither general removability nor a zero jump is imported.

**Seguin–Hinz–Fried (2014).** Read the authors' article
*Extending the Transport Theorem to Rough Domains of Integration*,
AMR66, 050802, DOI10.1115/1.4026910, Sections2.4,3,4: Stokes (40),
Theorem3.1/(68), and (69)–(78). Theorem3.1 assumes a regularly
evolving differential chain and a differentiable form in the stated
Banach classes. The convection specialization assumes a smooth map
with each time map invertible. Its boundary/density terms are
retained, not proved zero. C466s provides no such chain regularity
or smooth stopped convection. This review article illustrates the
framework; its cited original Seguin–Fried, M3AS24(2014)1729–1779,
is an unread lead, not an imported theorem or an essential blocker
for the selected cutoff method.

**TNV (2017).** Reused the variational coverage954/955/957. Newly
read the raw blow-up cases in Section2.2, printed pp5–6,
(2.15)–(2.21), both Jacobian footnotes, and the distinction from
Sections3.1–3.2. Footnote2's bounded weighted-Jacobian discussion
concerns its displayed real one-variable example; it is not a
theorem about all mixed minors of our space-time form. The later
completeness argument changes the metric. Neither passage supplies
the required stopped-current trace. No completeness or signed
invariance is imported for our arbitrary bidisk H.

**Fukuma–Matsumoto (2020 preprint).** Read the primary
arXiv2012.08468v1, 15 December 2020, printed pp3–4 and9–10,
equations (1.5)–(1.12) and(3.1)–(3.4). Its Cauchy deformation
discussion assumes entire integrands and fixed boundary at infinity;
its worldvolume geometry assumes a smooth embedded (N+1)-manifold,
independent constraints and a tangent basis. Our local zero-extended
map is not asserted to meet these premises. These are no substitute
for a collision-defect estimate, and chi introduces the retained
inhomogeneous term. No worldvolume manifold structure is imported.

Primary extracted text was readable. The initial HP fetch timed out
but a later fetch succeeded. Some screenshot requests timed out or
returned references only; no visual verification is claimed. The
publisher worldvolume page failed, so the versioned arXiv primary
PDF supplied the actual evidence. A mistakenly opened unrelated
arXiv1906.03122 was excluded entirely. No essential source remains
inaccessible for the proposed method. Supporting Mathlib coverage
and a full matching theorem remain unchecked.

### Decision and bounded continuation

The review finds no direct import. It does find primary coverage of
the cutoff method and of the hypotheses that a general extension
theorem would require. EXPLORE therefore covers preparing one
bounded proof/obstruction attempt, not a conclusion about the
identity. The future attempt must treat every coefficient of beta
and gamma, including the dt wedge dr and dt wedge ds coefficients;
the known bound on dr wedge ds cannot stand in for them.

The nominated test is to construct survivor-domain cutoffs whose
complete-form limits exist in L1_loc and whose exterior-derivative
error has zero distributional limit, or find an admissible H and
compact test detecting failure. The precise target, hypotheses and
threshold are in
[assessment960](2026-11-14-collision-current-cutoff-attempt-960.md).
No such cutoff or estimate has been derived here. Failure of a
convenient norm bound alone would be a method limitation, not a
counterexample. HP's homogeneous theorem is not being silently
applied to the inhomogeneous target.

This is an established-route development, not a central creative
sign mechanism. A local identity could pay one signed boundary step;
it still leaves the resulting integral's sign, original-coordinate
metric, divisor intersections, global cycles, other endpoints,
all-order signs and actual-Xi transfer unresolved. The blocker to
a justified central creative nomination remains the absent link
from such transport to actual determinant positivity.

Outcome EXPLORATION records new bounded source coverage, not a
mathematical advance, informative counterexample or repeated
assessment. No mathematical exploration turn or counter reset is
claimed. The new ready continuation requires its separate approval
next turn; the completed source review remains valid independently.
