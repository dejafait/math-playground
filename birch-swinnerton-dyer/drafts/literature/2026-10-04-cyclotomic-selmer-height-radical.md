# Cyclotomic Selmer height radical and divisible Sha: source comparison

TARGET: Assess whether the radical of the canonical cyclotomic height on Sel(Q,V_p E) maps onto V_p Sha(E/Q) under L018's hypotheses, without assuming finite Sha.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched full-Selmer cyclotomic height radicals, universal norms, divisible Tate--Shafarevich quotients and derived heights; inspected Howard Theorem 4.2/Corollary 4.3, Bertolini--Darmon Theorem 2.18, and Macias Castillo--Sano Hypothesis 4.1/Theorem 4.2; exact queries and access limits appear below.
SOURCE_EVIDENCE: Howard arXiv:1202.6343v1 Sections 3--4, PDF pp. 12 and 15--17; Bertolini--Darmon (1995) Section 1.1, Proposition 1.1, Theorem 2.18 and Remark 2.21, printed pp. 1518 and 1539--1541; Macias Castillo--Sano arXiv:2603.23978v1 Section 4.1, Hypothesis 4.1/Theorem 4.2; Buyukboduk (2012) Section 2.1.3/Proposition 2.7, printed pp. 80--81; supporting finite-Sha regulator coverage is reused and rechecked.
COMPARISON: The inspected full-Selmer height exists without finite Sha and its first radical is the second derived Selmer filtration; Howard measures it through the augmentation filtration of X, not through rational rank. No inspected theorem states that this radical maps onto V_p Sha. L013 already supplies the relevant formal ordinary complex and marked quotient, so a new generic model would duplicate work.
GAP: The arithmetic surjection from the first-height radical to the quotient V_p Sha remains unsupported; a full-Selmer height criterion cannot yet be used to obtain r >= 2. The ready subtarget is only a compatibility audit of the existing formal model against L018's coefficient tower and divisible pairing kernel.
REASON: Import the known full-Selmer height/filtration statements rather than reprove them; specialize their Bockstein construction in L013 to test the proposed structural inference before seeking a new arithmetic height theorem. This assessment does not approve assuming the arithmetic surjection.
SCOPE: Retain L018's hypotheses for the arithmetic comparison. Approval for mathematical work is confined to the exact formal audit below; no elliptic-curve realization, actual Kurihara family, finite Sha, positive rational rank or complex/p-adic order comparison is assumed or established.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED and needed a primary full-Selmer height statement without finite Sha, an exact description of its radical, and comparison with the existing L013 model.
COVERED_TARGET: Apply the cited first-height/Bockstein construction to L013's ordinary complex and audit whether its radical maps onto the marked Sha quotient after retaining L018's compatible coefficient tower and divisible Cassels--Tate radical.

## Gap and continuation threshold

Use L018's notation: the full rational Selmer space has dimension two,
its rational Kummer subspace W has dimension r, and its quotient A is
V_p Sha of dimension 2-r. Here V_p Sha means T_p Sha tensor Q_p.
The saved target asks whether the quotient map q has
q(rad(h_cyc)) = A. Sha is a quotient, not a canonically embedded
subspace. The needed threshold is surjectivity onto all 2-r quotient
dimensions, not merely height vanishing on universal norms.

If this surjection and full-Selmer nondegeneracy were established
separately, they would remove the divisible quotient. Neither premise
is established here. Producing the two-prime premise from m(E)=2,
analytic comparison, and higher ranks would remain unresolved even
after that conditional success. The achieved bound remains r <= 2;
the required lower bound is r >= 2.

## Search and source record

Queries on 2026-10-04 included:

- `Schneider p adic height pairing Selmer group radical universal norms Tate Shafarevich`
- `cyclotomic p adic height Selmer radical divisible Tate Shafarevich group`
- `Nekovar Selmer complexes height pairing radical universal norms`
- `"Schneider" "height" "non-degenerate" "Selmer" finite`
- `"Derived p-adic heights" Bertolini Darmon pdf`
- `"p-adic height" "Selmer" "Shafarevich" "kernel"`
- `"height pairing" "radical" "Sha" cyclotomic`
- `"p-adic height" "radical" "divisible" Selmer`

Only the primary texts below support the comparison. Search snippets,
unreviewed claimed BSD proofs and secondary reproductions were not
accepted as theorem evidence. This was a bounded search; absence of
a match in it is not a novelty claim or a disproof of the target.

### Full-Selmer heights and their radical

Benjamin Howard, *Derived p-adic heights and p-adic L-functions*,
[arXiv:1202.6343v1](https://arxiv.org/pdf/1202.6343v1#page=16),
submitted 2012-02-28 (the uploaded text has its own printed pagination):
read Sections 3--4, especially Lemma 4.1, Theorem 4.2 and Corollary 4.3,
PDF pp. 12, 15--17, printed pp. 12, 15--17. Theorem 4.2 places heights
on the compact Selmer space tensor Q_p, with first kernel S_p^(2).
Its dimension formula uses rank_Z_p(J X/J^2 X); the intersection of
all derived filtrations is the universal-norm space. Corollary 4.3(a)
characterizes first-height nondegeneracy by absence of higher
augmentation blocks and a free Lambda part. These statements do not
assume finite Sha. Section 4 retains good ordinary reduction,
unramified p in the base, ramification above p in the tower, and finite
decomposition of bad primes. Q and its cyclotomic tower meet the
field/tower conditions. The discussion after Corollary 4.3 explicitly
distinguishes Kato's torsion result from conjectural cyclotomic
nondegeneracy. No relation with the rational Kummer quotient is asserted
in these statements; Theorem 1.11's infinite-level pairing must not be
confused with the base first height.

Massimo Bertolini--Henri Darmon, *Derived p-adic heights*,
Amer. J. Math. 117 (1995), 1517--1554,
[author-hosted published text](https://www.math.mcgill.ca/darmon/pub/Articles/Research/13.Derived-p-adic/pub13.pdf#page=24):
read Section 1.1/Proposition 1.1, Theorem 2.18 and Remark 2.21,
printed pp. 1518, 1539--1541. Theorem 2.18(2)--(4) identifies the next
filtration with the radical, includes universal norms in the kernels,
and identifies the first height restricted to rational points with the
ordinary classical height. Its standing assumptions require odd p,
Tamagawa coprimality, good reduction above p, a residual Cartan, and
surjective local norms; Proposition 1.1 supplies the last condition
at ordinary non-anomalous ramified primes. L018 retains these
conditions. Remark 2.21 adds finite Sha to identify a rational-point
basis with a compact Selmer basis; that addition is unavailable here.

Daniel Macias Castillo--Takamichi Sano, *On Selmer complexes, Stark
systems and derived p-adic heights*,
[arXiv:2603.23978v1, Section 4.1](https://arxiv.org/html/2603.23978v1#S4.SS1),
submitted 2026-03-25: read Hypothesis 4.1, equations (4.1.1)--(4.1.3),
Theorem 4.2 and Remark 4.3. Hypothesis 4.1 asks for ordinary reduction,
Tamagawa and non-anomalous coprimality, and a residual Cartan; L018's
surjectivity supplies the residual condition. Their comparison
identifies Bertolini--Darmon heights with the negative of Nekovar's
Bockstein/cup-product heights for 1 <= k <= p-1, without finite Sha.
The first pairing is the usual height; its normalization and the
comparison sign do not affect the radical. Remark 4.3 permits a wider
Nekovar construction but supplies no rationality theorem. This is a
primary comparison source, not an import of the article's full Stark
system arithmetic or a statement about Sha radical surjectivity.

Kazim Buyukboduk, *Height pairings, exceptional zeros and Rubin's
formula: the multiplicative group*, Comment. Math. Helv. 87 (2012),
71--113,
[Section 2.1.3 and Proposition 2.7, pp. 80--81](https://ems.press/content/serial-article-files/43278#page=10),
was re-read for the Bockstein followed by Poitou--Tate construction
and the inclusion of universal norms in its kernel. It attributes
the latter to Nekovar Proposition 11.5.7/Section 11.5.8. Its later
multiplicative-group applications are not elliptic-curve inputs.

### Reused regulator coverage and access limits

The prior [regulator foundation](../../foundations/04-cyclotomic-height-criterion.md)
is adequate for its unchanged rational-point statement.
[Stein--Wuthrich, Theorem 6.1, printed p. 1776](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=20)
was reopened: equality of characteristic order with rational rank
retains both finite p-primary Sha and nondegenerate rational height.
It is not a match for the present full-Selmer surjection.
[Wuthrich, *Iwasawa theory of the fine Selmer group*, author text,
introduction and Theorem 1.1, PDF pp. 2--3](https://www.maths.nottingham.ac.uk/plp/pmzcw/download/fine.selmer.pdf#page=2)
also retains finite Sha for the cited rational-rank formula; fine and
ordinary Selmer conditions must not be interchanged.

The original [Nekovar volume](https://www.numdam.org/item/AST_2006__310__R1_0/)
was located, but its large PDF again failed in the web reader. His
separate *On p-adic height pairings* author PDF also failed to open.
No direct reading of either full original proof is claimed. The
accessible primary height comparison and Howard/BD statements above
provide the coverage needed for the bounded formal audit, so neither
blocker is essential to that next task. They remain parked for any
claim requiring stronger original arithmetic statements.

A new optional lead, John W. Jones, *Plater's p-adic orthogonality
relation for abelian varieties*, Houston J. Math. 21 (1995), 261--282,
appeared in searches. Its [located PDF](https://citeseerx.ist.psu.edu/document?doi=ccf95378e8082fb0ee75442cee2464062dbd93f9&repid=rep1&type=pdf)
returned HTTP 403. It is an **unread lead**, not an inspected theorem
or evidence for either surjectivity or its negation. No dependent
arithmetic application is queued.

The [current Clay page](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/)
and [Wiles's description, printed p. 2](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf#page=2)
were rechecked. The displayed rank/order assertion and Remark 1's
stronger leading-coefficient refinement retain the scope recorded in
foundations/01-target-and-scope.md.

## Comparison and approved bounded specialization

There is now adequate source coverage for the **definition** of the
full ordinary cyclotomic height without finite Sha. No checked source
settles q(rad(h_cyc)) = A under the actual two-prime arithmetic
hypotheses. Cassels--Tate divisibility is a different pairing statement;
L009's anticyclotomic vanishing is a different deformation. Replacing
either by the cyclotomic height would lose its hypotheses.

L013 already writes an ordinary two-term complex, its inverse-parameter
duality, the finite/strict/relaxed local triangles, a rank-one marked
rational lattice, a divisible Sha quotient and exact base integral
control. Its ordinary differential is explicitly recorded in equation
(6). Its coefficient tower was not the purpose of that determinant
test. Reuse this artifact rather than build a duplicate countermodel.
The remaining specialization is to apply the cited first Bockstein
height to that ordinary complex and explicitly audit the marked
quotient, downward coefficient maps and compatible prescribed basis.
No such calculation or conclusion is made in this literature turn.

The next test must retain a compatible Z_p^2 Selmer lattice, its
rank-one marked Kummer sublattice, the divisible quotient with its
zero Cassels--Tate pairing, and the already written local triangles.
It must distinguish the first **ordinary** Bockstein from L013's
global relaxed Bockstein. Continue an arithmetic radical route only
if an additional actual arithmetic hypothesis excludes a failed
formal inference. If this package permits a height radical whose
image fails to cover the quotient, stop seeking rationality from this
structural/height package alone and name the missing arithmetic input.
If compatibility instead fails, record the precise failing map rather
than claim an elliptic-curve counterexample. In either case the actual
Kurihara/Stark family and arithmetic realization are outside the model.
The audit is one bounded mathematical step, not a reproof of the
general height theorems or a new lemma quota.

This assessment completes the saved source review and approves only
the exact COVERED_TARGET. Its outcome is EXPLORATION: usable known
height coverage and a concrete test were found, while the proposed
arithmetic surjection remains unresolved. No result beyond the checked
literature, new rational-rank bound or complete candidate is claimed.

## Mathlib

Mathlib coverage of the full arithmetic radical-surjection statement
and of the supporting full-Selmer height/Bockstein formalism:
**not checked**. Howard Theorem 4.2, BD Theorem 2.18 and Macias
Castillo--Sano Theorem 4.2 match supporting height/filtration statements;
none is asserted as a match for the full arithmetic target or a Mathlib
declaration. Library absence and originality are not inferred.
