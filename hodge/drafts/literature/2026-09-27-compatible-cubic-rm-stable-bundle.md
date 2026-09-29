# Compatible cubic RM stable bundle — literature assessment

TARGET: Assess whether a slope-stable locally free bundle on S x S can have SU(2)-invariant c_1 and c_2 for a common metric with Kahler class omega from L025 and a degree-four Chern-character action cU on T(S), for some nonzero rational c.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched prescribed Chern classes, stable resolutions, general asymptotic existence and hyperholomorphic product constructions; queries, newly read statements and reused comparisons appear below.
SOURCE_EVIDENCE: Mistretta, arXiv:math/0310185v2, Theorem 3.1 and Corollary 3.3, https://arxiv.org/pdf/math/0310185v2#page=7; Verbitsky, arXiv:alg-geom/9307008v1, Proposition 1.2, Lemma 2.1 and Theorem 2.5, https://arxiv.org/pdf/alg-geom/9307008v1#page=9; O'Grady, arXiv:2211.08970v3, Theorem 1.1, https://arxiv.org/pdf/2211.08970v3#page=2; further scope checks below.
COMPARISON: Stable-resolution existence is known for an ample integral polarization, and hyperholomorphicity is known conditional on stability and invariant Chern classes; neither supplies their simultaneous realization for L025's metric and the cubic action.
GAP: Check full Chern-data compatibility of the concrete stable-resolution construction, then stability at the required product Kahler class if compatibility survives; arbitrary compatible stable bundles and transverse transport remain unresolved.
REASON: Import the known construction and invariant-class criterion, then permit one bounded compatibility test in a separate research turn. Stable generation, a large numerical Chern bound and rational cohomological compatibility do not settle the exact existence target.

## Hypotheses

Retain the very general cubic S, operator U, and rational correction
A and Kahler class omega supplied by L025. Stability is with respect
to p_1^*omega+p_2^*omega. SU(2) is the diagonal action from the
same hyperkahler metric on both factors; ch_2 acts by the convention
in L006. Divisor and point-class contributions are allowed subject
to invariance. The target requires an actual locally free stable
bundle, not a virtual K-class, and imposes no Fourier--Mukai
equivalence. L025's matrices are not asserted to be Chern classes.

Reuse the [earlier bundle assessment](2026-09-27-hyperholomorphic-cubic-rm-representatives.md),
the [arithmetic assessment](2026-09-27-cubic-rm-kahler-eigenvector.md),
and the unchanged [rational Hodge target audit](../../foundations/01-target-and-scope.md).
No result on this product is substituted for the universal target.

## Conclusion

The exact saved TARGET now has a completed SPECIALIZE assessment.
No inspected theorem proves existence or nonexistence with all its
hypotheses. A known stable-resolution recipe gives a concrete
Chern-data test; it is not a certificate that the recipe escapes
the earlier syzygy obstruction. No calculation or construction
was performed.

The missing claim remains a representative extending the cubic
action into V_RM outside V_D. Success would justify investigating
that transport. An obstruction for one recipe would reject that
recipe only. The attained 21-dimensional span and three directions
against four required are unchanged. Arbitrary primitive fourfold
classes and higher codimensions remain unresolved.

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION, the first
exploration turn since L025. Reading known inputs does not reset
the count or establish novelty. A subsequent specialization using
only these tools should be classified as REPRODUCTION. There is
no complete candidate argument.

## Proof

The evidence is source comparison. An intermediate source checkpoint
was saved here and incorporated into this completed assessment.

### A known stable-resolution construction

Read Ernesto C. Mistretta, *Stable vector bundles as generators of
the Chow ring*, [arXiv:math/0310185v2, 15 March 2007](https://arxiv.org/pdf/math/0310185v2):
section 1.1, p. 2; Theorem 3.1 and proof, pp. 7--9;
Corollaries 3.3 and 3.5, pp. 10--11. The arXiv notice distinguishes
this version from Geometriae Dedicata 117 (2006).

For smooth projective X with ample polarization H, the theorem gives

\[
0\longrightarrow E\longrightarrow P_e\longrightarrow\cdots
\longrightarrow P_0\longrightarrow I_Z\longrightarrow0,
\qquad P_i=V_i\otimes\mathcal O_X(-m_iH),\quad e=\dim X-2,
\]

with E slope-stable and locally free. Corollary 3.3 gives rational
Chow-group generation by stable-bundle Chern characters. Import
these statements rather than reprove them.

The statement does not prescribe invariant c_1,c_2 or stability
at the saved irrational class. Its choices are constrained by
the construction. Group generation is not realization by one
bundle with all the requested properties. These are application
gaps, not an asserted impossibility.

### Hyperholomorphicity remains conditional

Reused the earlier criterion and reread Verbitsky,
*Hyperholomorphic bundles*, [arXiv:alg-geom/9307008v1,
29 July 1993, Proposition 1.2, p. 4; Lemma 2.1 and Theorem 2.3,
p. 7; Theorem 2.5, p. 9](https://arxiv.org/pdf/alg-geom/9307008v1#page=7).
Invariant forms have type (p,p) for all induced structures;
invariant two-forms have zero contraction with each induced
Kahler form. An existing stable bundle with invariant first two
Chern classes is hyperholomorphic. The product is allowed, but
the surface-only Theorem 2.4 cannot replace this criterion on a
fourfold. Invariant discriminant and projective hyperholomorphicity
alone remain weaker than the saved requirements.

Reread Schlickewei, *Hodge classes on self-products of K3 surfaces*
(2009), [section 1.2.3, Theorem 1.2.3.1 and the discussion following
Proposition 1.2.3.3, printed pp. 28--30](https://d-nb.info/1000464202/34#page=30).
The suitable polystable bundle is explicitly conditional. The
quadratic-RM compatibility precedent supplies no cubic
stable-bundle existence result.

### Numerical existence does not prescribe the full class

The broad asymptotic lead points to Maruyama, *Moduli of stable
sheaves, II* (1978). Its DOI and Project Euclid PDF routes failed.
Read its explicit attributed restatement in Nakashima,
*Existence of stable bundles on Calabi-Yau manifolds*, RIMS
Kokyuroku Bessatsu B9 (2008), [Theorem 1.1, p. 153](https://www.kurims.kyoto-u.ac.jp/~kenkyubu/bessatsu/open/B9/pdf/B09_008.pdf#page=1).
For fixed rank at least the dimension, first Chern class and an
integer lower bound, it gives a stable bundle with second Chern
number against H^(n-2) at least that bound. It does not prescribe
the full c_2 class. This is a scope check of that restatement,
not a reading or import of the original proof.

Also read Nakashima's own [Proposition 3.2 and Example 3.4,
pp. 156--157](https://www.kurims.kyoto-u.ac.jp/~kenkyubu/bessatsu/open/B9/pdf/B09_008.pdf#page=4).
The construction retains an H-minimal determinant, Hom-vanishing
and appropriate extension data. Its elementary-transform example
needs a smooth divisor and a generated line bundle on it. No
identification with the required metric and cubic class is given.
The later Picard-rank-one examples have different hypotheses.

The inaccessible original is not an input to the chosen test,
which uses Mistretta and Verbitsky. No claim about stronger
uninspected Maruyama assertions is made.

### Nearby hyperkahler results

Read O'Grady, *Rigid stable vector bundles on hyperkahler varieties
of type K3^[n]*, [arXiv:2211.08970v3, submitted 13 October 2023,
PDF dated 17 October 2023, Theorem 1.1 and Proposition 1.2,
pp. 1--3](https://arxiv.org/pdf/2211.08970v3#page=2).
Existence concerns a general polarized variety of K3^[n] type
with particular rank, determinant and discriminant proportional
to ambient c_2. Proposition 1.2 also assumes deformation
surjectivity. Neither statement concerns S x S. No passage from
a Hilbert scheme to the required stable product bundle is supplied.

Reuse the earlier assessment's inspected Markman (2024),
Proposition 5.15; Maulik--Shen--Yin (2026), Theorems 0.4, 0.7
and 0.9; and Hartlieb--Shah (2026), Theorem 1.3. Their versions,
direct links and limits are preserved there. Propagation starts
with a suitable bundle and extra stability/persistence hypotheses;
the isometry and equivalence constructions do not give the
specified cubic action. No fresh reading of these papers is
claimed. The withdrawn Verbitsky stability paper remains excluded.

### Search and access record

Queries on 2026-09-27 included:

- `"hyperholomorphic" "real multiplication" stable bundle existence`
- `"K3" "product" "stable bundles" "Hodge" Chern classes`
- `"Hodge conjecture" "K3" "real multiplication" 2026`
- `hyperholomorphic vector bundles product K3 prescribed Chern classes existence stable`
- `Mistretta stable vector bundles Chow groups resolutions stable bundles`
- `"hyperholomorphic" "product" "nonisometric"`
- `"Maruyama" "asymptotic" "theorem" stable bundles`
- `"Moduli of stable sheaves, II" Maruyama "pdf" "1978"`

Title/author and reference follow-ups led to the sources above.
The Mistretta author-host PDF failed; the pinned arXiv PDF supplied
its statements and proof. A shell download failed at DNS. Web PDF
text was read; no screenshot inspection is claimed. Nakashima's
full paper was available from RIMS. The Douglas--Reinbacher--Yau
discussion led to Maruyama's reference; it is not used as a
fourfold existence theorem.

Unread leads include Markman--Mehrotra, arXiv:1310.5782, on rigid
Azumaya sheaves, and originals behind the attributed surface
existence statements. The failed Mathsoc book retrieval is not a
read theorem. None is an input to the selected test. Search
abstracts are not theorem evidence; this bounded comparison
establishes no novelty and no full nonexistence theorem.

### Redundancy and one bounded continuation

Checked L012's exact hypotheses and
[Attempt 009](../../ATTEMPTS/009-second-syzygy-of-cubic-ideal.md).
Its sufficiently negative second syzygies are excluded without
assuming instability. Stability alone cannot reopen that result.
The new source's presentation length and choices must be compared
with those hypotheses, not silently identified. L004 and
[Attempt 003](../../ATTEMPTS/003-totally-real-isometry-generation.md)
already exclude rational self-isometry generation. L017 and
L024 concern specified supported sheaves, not all bundles.

Of the screened recipes, stable resolutions give a concrete
necessary-condition test. Elementary transforms leave the needed
quotient data unspecified; the known isometry kernels retain the
wrong action restriction. This ranking is a research decision.

Retain the exact TARGET for the next separate research turn.
First test full Chern-data feasibility of the terminal resolution
bundles for I_C, allowing line-bundle twists and an ample product
polarization H. Use the actual L025 metric and the entire mixed
degree-four class. Check for a verbatim existing exclusion first,
and import it if applicable. Do not replace SU(2) invariance by
the action on T alone or treat presentation coefficients as free.

A uniform failure of invariance stops this recipe only. Surviving
formal data justify further work only after checking integral
ranks and actual permitted choices; stability for H does not
establish stability for p_1^*omega+p_2^*omega. An inconclusive
test consumes the next exploration turn. Two turns remain before
the window must end in a continuation/stop decision. Actual
bundle existence and transport into the missing NS-fixed
direction remain later obligations after any positive class test.

No Chern specialization, twist calculation, stability proof,
construction, obstruction, or new lemma was derived this turn.

## Mathlib

Coverage: **not checked** for the full target, the selected
compatibility test, or the supporting bundle results. Named
theorems and direct links above are mathematical source references.
None is claimed to match the full saved statement; no Mathlib
absence is asserted.
