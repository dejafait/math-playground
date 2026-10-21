# Actual split harmonic metric — approved source comparison

TARGET: Test uniform two-sided bounds for the actual stable-open harmonic L2 metric in a local holomorphic frame of L111's free middle sheaf near each split point.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched elliptic-family small-eigenvalue reduction, cohomology jumps and L2 higher-image metrics; inspected BGS III and Mourougane--Takayama primary statements; compared audited L111, corrected L108, L110 and ATTEMPTS/063/066/067 with the saved reflexive-extension assessment.
SOURCE_EVIDENCE: Bismut--Gillet--Soulé III (1988), section 1(b)--(c), pp. 304--305, Theorem 3.5 with Lemmas 3.6--3.8 and complete proof, pp. 342--345; Hodge decomposition in Theorem 3.14 proof, p. 350; Mourougane--Takayama 0707.3551v2 Theorem 1.1 and metric distinction, pp. 1--2.
COMPARISON: The primary smooth relative-Dolbeault comparison and finite spectral complex cover the analytic reduction through a jump. They do not state the target norm estimate. L111 supplies the actual holomorphic Koszul splitting to specialize; a quantified comparison with the given harmonic quotient norm remains the mathematical task.
GAP: Construct the compatible comparison on this actual minimal complex and prove both direction-independent quotient-norm inequalities in its middle-sheaf frame. Neither an arbitrary derived equivalence nor smoothness of a determinant metric supplies these inequalities.
REASON: Approve one later REPRODUCTION attempt using inspected elliptic reduction plus L111; import the source tools and prove only their finite-dimensional norm specialization. This literature turn establishes no estimate, metric extension or semistability.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED because earlier algebraic and surface-extension coverage did not include the actual varying-kernel analytic comparison; this turn fills that essential source scope.
SCOPE: The hypothetical (14,21) family of corrected L108, audited L111's actual Koszul plane and free middle module, L110's actual coefficient variation, L094's split harmonic spaces and L095's smooth compatible connection; L071's full tensor and fixed common metric retained. Z is finite and may be empty.

## Exact test and downstream relevance

The main gap remains universal primitive rational Hodge realization.
The independently testable intermediate question is whether the *given*
harmonic metric G on M|_U, written in one local holomorphic frame of
the actual locally free M=E, admits constants 0<c<=C<infinity with

    c ||xi||^2 <= G_b(xi,xi) <= C ||xi||^2

for every frame coefficient xi and every sufficiently small b!=z.
Both constants must be independent of the direction of approach to z.
For Z empty there is no local puncture to test. This target is not
smooth extension of the metric or admissibility of its connection.

Potential use: a controlled metric estimate could supply one necessary
analytic input for later extension or semistability work on L108's
normal summand, whose exact conditional budget is now 800-|Z|.
Curvature integrability, a suitable extension theorem, semistability,
cardinality, F existence and transport would remain separate obligations.
No Chern inequality or kernel exclusion is inferred from boundedness.

The new ingredient relative to ATTEMPTS/066 is the audited *actual*
two-parameter Koszul splitting with a nondegenerate first-order plane
and free middle sheaf. The proposed mechanism is quantitative comparison
with the smooth family of elliptic Dolbeault complexes on the fixed
compact fibre, rather than automatic extension of a reflexive sheaf.
In particular, an algebraic or derived chain equivalence is not itself
a bounded equivalence on the spaces of harmonic representatives.
The missing analytic comparison is the point to assess and then test.
ATTEMPTS/063's singular-quotient metric/degree route and ATTEMPTS/067's
duality-only numerical bound remain parked and are not being repeated.

## Primary source review completed, 2026-10-16

Completed LITERATURE / ADVANCE / NOVELTY_UNCHECKED: the advance is access
and applicability of a known analytic input, not the two-sided estimate
or progress beyond the sources. No lemma or mathematical script was
written. The original proposal above is retained as the target and its
limits; its REVIEW_REQUIRED gate is discharged by this separate review.

**Primary reduction.** Bismut, Gillet and Soulé, *Analytic torsion and
holomorphic determinant bundles III. Quillen metrics on holomorphic
determinants*, Comm. Math. Phys. 115 (1988), 301--351,
DOI 10.1007/BF01466774,
[author scan](https://www.imo.universite-paris-saclay.fr/~jean-michel.bismut/Bismut/1988b.pdf).
Read section 1(b)--(c), pp. 304--305, and Theorem 3.5 with its complete
proof, including Lemmas 3.6--3.8, pp. 342--345. For a proper smooth map
of complex manifolds and a holomorphic vector bundle, Theorem 3.5
identifies the smooth scalar extension of each ordinary higher image
with relative smooth Dolbeault cohomology. No constant fibre-cohomology
hypothesis occurs. Its proof compares a finite holomorphic complex with
the relative complex, checks the central derived fibre (Lemma 3.7),
and passes through the smooth small-eigenvalue complex (Lemma 3.8).
The latter uses the Green inverse only on the spectral complement and
a smooth chain homotopy. Section 1 gives the cutoff bundle and its
induced Hermitian metric. Theorem 3.14's proof, p. 350, recalls the
harmonic Hodge decomposition. These are the imported tools; the target
estimate is not asserted there.

**Hypothesis match.** Apply the quoted bundle hypothesis to V=End_0(F),
not to the conjectural normal bundle. The projection p:S_1 x B -> B
is a smooth proper holomorphic map; V is an actual holomorphic locally
free coefficient under the conditional hypotheses. The product Kähler
metric and the metric induced by F's given compatible connection are
smooth across z. Thus the reduction does not involve an HE metric
chosen separately on each nearby stable bundle or a potentially
unbounded family of complex gauge transformations. Local Kählerness,
where used in the surrounding source, also holds for this product.

L111's minimal representative and its maps can be analytified on a
small neighborhood. Its coefficients are germs of regular functions,
so the actual splitting is convergent there. This is existing L111
input, not a newly constructed analytic normal form. The later proof
must match its derived-fibre comparison to the source's natural one;
smooth scalar extension must not be confused with ordinary base change
at z. In particular M_z/m_z M_z has dimension fifty, whereas derived
H^1 at z has dimension fifty-two. The cutoff retains the latter.

**Stronger-looking metric theorem screened.** Mourougane and Takayama,
*Hodge metrics and the curvature of higher direct images*, Ann. Sci.
Éc. Norm. Supér. 41 (2008), 905--924,
[0707.3551v2, 18 September 2008](https://arxiv.org/pdf/0707.3551v2),
Theorem 1.1, p. 1, assumes a smooth proper surjective Kähler map with
connected fibres and a Nakano-semipositive Hermitian coefficient bundle.
It gives locally free, Nakano-semipositive higher images of the relative
canonical bundle tensored with that coefficient. The discussion on p. 2
explicitly distinguishes its Hodge metric from the fibrewise harmonic
metric. Here the K3 relative canonical line is trivial, but no Nakano
semipositivity of V is supplied. Therefore this theorem is not an import
for the requested chosen metric. Its proof is unnecessary for this
hypothesis rejection; no claim based on its uninspected later proof is used.

**Discovery and access record.** Queries included “elliptic complex
families small eigenvalues finite dimensional reduction cohomology metric
Bismut Freed”, “cohomology jumping L2 metric harmonic representatives
locally free direct image bounded elliptic complex”, “holomorphic
families elliptic complexes finite dimensional reduction cohomology”,
and the exact BGS III title. This bounded search identified the primary
reduction above but no inspected theorem stating this full two-sided
specialization. It establishes no novelty claim. Ma, *Orbifold Submersion
and Analytic Torsions* (2021), section 3.3, pp. 157--159,
[author text](https://webusers.imj-prg.fr/~xiaonan.ma/mypubli/Ma_PM338_21.pdf),
was used only to locate the original reference, which was then read.
BF II's Project Euclid iframe was blocked; the accessible BGS III author
scan resolves the essential source need. A local urllib download failed
DNS; browser extraction of the primary text succeeded. The unrelated
1988c.pdf URL was screened and not used. No unread lead is a premise.

## Scope approved for the next mathematical attempt

SPECIALIZE approves exactly TARGET under the saved assumptions, with
REPRODUCTION classification. Reuse L094/L095/L108/L110/L111 and L071
through them. Their hypotheses and actual pairing must remain intact.
The useful new source input is the smooth finite reduction compatible
with ordinary sheaf cohomology; no uniform estimate for the jumping
harmonic projector is imported or assumed.

The remaining specialization must identify the actual middle-sheaf frame
in that reduction and control its cohomology quotient norm in both
directions on one full punctured ball. It must track any chain maps and
their norms across the centre, retaining every Koszul coefficient. The
usual finite-dimensional norm and Hodge orthogonal-projection arguments
are covered tools; their actual-family application is the work to do.
A source theorem alone does not certify the desired lower bound.

Continue if one obtains constants 0<c<=C<infinity independent of b and
its approach direction. A failed comparison must identify an actual
map or a genuine degeneration of this smooth coefficient family; an
arbitrary singular metric on an algebraically free sheaf does not test
TARGET. Directional estimates with radius-dependent constants do not
meet it. If the analytic reduction cannot be matched to L111's actual
frame, preserve that failure and reassess the mechanism before asserting
boundedness; do not silently replace the metric or assume constant rank.

Even a successful bound would leave curvature integrability, metric or
connection extension, semistability, the cardinality of Z, existence of F,
transport and universal primitive Hodge realization unresolved. Z may
be empty. ATTEMPTS/063/065/066/067 remain intact: this review reopens only
the specific estimate using the new actual splitting and inspected
elliptic input, not their automatic-extension or duality-only arguments.
Full matching Mathlib coverage is not checked; no absence claim is made.
