# Opposite image projective degree — completed source comparison

TARGET: Assess whether projective degree and surface regularity bounds control the total normalization defect of L120's opposite image without coherent-cohomology vanishing.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched reduced/nonnormal projective surface degree, regularity, arithmetic genus, Hilbert coefficients and normalization defect; located and read Hoa's reduced-ring bounds and Niu's normal-surface theorem. Compared L118/L120/L121, L107 and ATTEMPTS/070, 073, 078; reused the ready determinant-line assessment rather than repeating its discovery search.
SOURCE_EVIDENCE: Le Tuan Hoa, arXiv:math/0608118v1 (4 August 2006), Theorem 0.2, definitions pp. 4–5, Lemma 1.4/Theorem 1.5 and both induction cases pp. 6–8, Theorem 4.1 and proof/Proposition 4.3 pp. 15–16, https://arxiv.org/pdf/math/0608118v1 ; Wenbo Niu, arXiv:1306.6535, Theorem 1.1 p. 1, https://arxiv.org/pdf/1306.6535 ; reuse Huybrechts–Lehn (1997), 8.1.5/8.1.9–8.1.12 and 8.3/8.3.1(ii), pp. 180–185/195–197, https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf .
COMPARISON: Hoa covers reduced homogeneous rings without normality or CM assumptions and bounds Hilbert coefficients, not just hyperplane sections. The general determinant framework supplies ample lines on the fixed-determinant projective moduli space; the opposite family's pullbacks and all resulting projective parameters still require a separate calculation. L107 is only a forward-family comparison.
GAP: No actual-image degree, numerical very-ample threshold, Hilbert constant or defect bound is computed. Establish dependence of the embedding choices on fixed surface/moduli data rather than F or the unknown defect, then test whether the available bounds are quantitatively useful.
REASON: The essential singularity-scope source gap is resolved; approve only a separate known-tool specialization. A finite parameter-dependent bound, an effective numerical bound and a contradiction are distinct thresholds. No general theorem needs reproving.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes from the exhausted ordinary Hom Euler mechanism to projective degree/Hilbert-coefficient control of a possibly nonnormal original image; this essential coverage was missing.
SCOPE: L071/L118/L120/L121's hypothetical equality kernel and original integral reduced opposite image Z with K3 normalization B; possible empty collisions, arbitrary finite multiple fibres, no normality, CM hypothesis or coherent vanishing.

## Main gap and source-level test

Universal primitive rational Hodge realization remains open. The
intermediate target is quantitative control of Q=nu_*O_B/O_Z for
L120's original image. A bound could later be compared with local
normalization defects and coincidence data. F existence, usefulness
of that comparison and transverse transport remain independent gaps.

This turn meets the theorem-scope part of the continuation test:
a primary reduced-ring result is available. The projective-parameter
part is a concrete remaining calculation, not an established bound.
Continue once for the separately registered specialization below.
Park if it needs the unknown Hilbert constant/defect to choose its
embedding, or if no justified F-independent parameters can be retained.
Do not interpret a large or ineffective finite bound as a contradiction.

## Inspected primary bounds and conventions

[Hoa, *Finiteness of Hilbert functions and bounds for
Castelnuovo–Mumford regularity of initial ideals*, v1](https://arxiv.org/pdf/math/0608118v1),
Theorem 0.2: for a homogeneous ideal I in R=K[x_1,...,x_n],
S=R/I reduced, dim S=d>=2, e=deg S and a=adeg S,

    reg I <= (e(e-1)/2+a)^(2^(d-2)).

The arithmetic degree sums component multiplicities over associated
primes; pp. 4–5 distinguish it from degree and record equality for
pure-dimensional rings. Ring dimension is one greater than projective
dimension; reg I=reg S+1. These conventions must be retained.
Theorem 1.5 proves the bound using saturated generic sections and
local cohomology, with both d=2 and d>=3 cases inspected. CM is used
for the bottom-dimensional section, not assumed for S.

Theorem 4.1, pp. 15–16, uses c=n-d and
P_S(t)=sum_{i=0}^{d-1}(-1)^i e_i binom(t+d-1-i,d-1-i).
It gives |e_1|<=a^c reg I and, for i>=2,
|e_i|<=(3/2)a^c(reg I)^i. Its saturated-section proof, including
the top coefficient and odd-dimensional case, was read. Proposition
4.3 combines these bounds with reduced-ring regularity. These are
published inputs for later application, not newly derived bounds.
In particular a coefficient bound must still be translated to the
actual Hilbert constant using the displayed convention.

[Niu, *Castelnuovo–Mumford regularity bounds for singular surfaces*](https://arxiv.org/pdf/1306.6535),
Theorem 1.1, p. 1, gives reg X<=deg X-codim X+1 for a
nondegenerate normal surface in P^n, n>=4, with the listed rational,
Gorenstein elliptic or log-canonical singularities. Normality is
unavailable for Z. This sharper theorem is not imported for Z;
its proof was unnecessary after that hypothesis mismatch. Search
hits concerning other normal or locally-CM bounds remain unread leads.

## Original image and projective choices

L118 supplies a common very ample integral H on Y=S_2, chosen
uniformly over all sheaves with the fixed invariants, not using F's
unknown image. L120 supplies the finite birational map from B=S_1
onto its actual integral reduced image in the stable moduli open.
L121 supplies finite reduced off-diagonal coincidences, with no
cardinality bound. These inputs neither compute a projective degree
nor imply normality of that image.

Reuse [the complete determinant-line assessment](2026-10-15-equality-determinant-line-positivity.md):
Huybrechts–Lehn Theorem 8.1.5 gives descended lines and the actual
family determinant formula; Definition 8.1.9 fixes the alternating
pushforward convention; Proposition 8.1.10, Theorem 8.1.11 and
Remark 8.1.12(i) supply a sufficiently-large-exponent ample
combination on the fixed-determinant projective surface moduli space.
Section 8.3 and Proposition 8.3.1(ii) supply family GRR. The descent,
positivity and GRR proof cases were already inspected there; targeted
book statements were relocated today. No universal sheaf, primitive
vector or generic H is required by these particular inputs.

For the opposite application keep rank two, determinant O_Y and
charge 21, with the actual moduli space of L118. Its projective
semistable compactification is an algebraic embedding device only;
no extension of the harmonic metric is required or asserted.
Choose an ample determinant combination on that fixed space and a
very ample power before using its restriction to the original Z.
Track its exponent, the power and ambient projective dimension.
The cited existence theorems do not give numerical thresholds here.

The remaining applicability argument must evaluate the two actual
opposite-family pullbacks from F, show what controls the degree of
that chosen original embedding, and distinguish fixed auxiliary
parameters from unknown invariants of F or Q. It must then use the
normalization exact sequence and K3 HRR to compare Hilbert constants.
These are obligations for the separate attempt; no formula for any
of these quantities is proved in this literature turn. In particular
L107's forward H, charge and evaluated pullbacks are not substituted.

## Duplicates, limits and continuation

ATTEMPTS/070 refutes minimal defect from selected local branch data;
local arrangement regularity does not give this global Hilbert bound.
ATTEMPTS/073 parks automatic H^1(O_Z)=0; this test uses no such
vanishing. ATTEMPTS/078 parks the uncontrolled ordinary Hom Euler
term. Hoa's coordinate-ring input concerns a different sheaf and
embedding; it does not supply that missing Euler sign. The parked
order-five route and all earlier stop evidence are preserved.

No full matching Mathlib result was checked; no absence is claimed.
No novelty follows from this bounded search. Sources give general
known bounds, while their useful family-specific specialization is
still unproved. PROOF.md and DAG.md are unchanged because the argument
has not changed. No lemma or mathematical script was written.

The [separate continuation assessment](2026-10-20-opposite-projective-polarization-specialization.md)
records one bounded calculation with these inputs. It is newly written
ready coverage and requires separate supervisor approval next turn.
