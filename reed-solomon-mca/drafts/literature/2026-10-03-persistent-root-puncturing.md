# Persistent locator roots: completed puncturing assessment

TARGET: For the pinned RS[F_(97^20),H,8] event on [1/4,5/16), test whether puncturing at a persistent root L(T,x)=0 identically yields at most fifteen bad parameters when D(T) is a nonzero polynomial, including singular parameters and failure on the original agreement support.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused recovery's ingredient screening; completed exact/common-root, puncturing, modified-syndrome and MCA searches on October 3, read the primary results behind new leads, and compared their hypotheses with the saved target. Queries, readings, exclusions and access qualifications are recorded in the completed-review section below; no full persistent-root fifteen-count match was established.
SOURCE_EVIDENCE: Reused the recovery readings below; additionally read Hall's author-hosted GRS and Modifying Codes chapters, Theorems 5.1.1, 5.2.2, 6.2.1 and Proposition 6.2.2 with the J-syndrome algorithm; BCHKS Theorem 1.3 and §2.3, and Theorem 4.6; Haböck ePrint 2025/2110, November 17, 2025, Definition 1, Lemma 1, Theorem 2 and its proof; WHIR's November 21, 2024 copy, Definition 4.9 and Lemma 4.10 with proof; Bordage–Chiesa–Guan–Manzur ePrint 2025/2051, May 19, 2026, Theorems 6.1 and 9.2; Chojecki's July 17, 2026-dated author TeX, SP2, HD1 and LC1–LC2 with proofs; Jeronimo 2609.05870v1, Theorem 1.2, Corollary 8.1 and §8.4; Gao–Yang–Xu–Kan 2607.10572v1, Lemma 3 and §4. No July ABF26 or Jo retrieval was repeated.
COMPARISON: Standard sources cover the auxiliary punctured code, adjusted syndromes, unique-decoding CA-to-MCA conversion and general support-event estimates; the read finite integral bound is also an auxiliary input to compare. None of these statements supplies the complete persistent-root reduction with its original-support exceptions and combined fifteen count. Import those covered ingredients; specialize only the missing transfer and count, without claiming a new decoder or general MCA theorem.
GAP: Verify the persistent-root reduction for all relevant parameters and control any loss of input failure at the removed coordinate, including D(gamma)=0 and multiple persistent roots; then prove or refute the combined bound of fifteen for arbitrary extension-field input words. No bound has been specialized or derived in this review.
REASON: The source comparison is complete enough for one bounded mathematical attempt on the unchanged pinned-model target. All selected supporting inputs are readable or already adequately covered; inaccessible July/Jo work stays parked. No citation alone closes the original support/count gap, and failure to find a match does not certify novelty.
SCOPE: The exact TARGET only: arbitrary a,b over F_(97^20), the order-16 H in F_97^*, four omissions, D nonzero as a polynomial, and at least one fixed x in H with L(T,x) identically zero; allow multiple such x and singular parameter values. Auxiliary punctured domains need not be smooth. Import standard puncturing, recurrence and MCA inputs and test only the stated transfer/count difference; do not reopen D identically zero, four-block equality, or challenge correspondence under this coverage.

The recovery screening below is preserved as a dated preliminary record.
Its pending language describes the assessment before this turn. The
completed review at the end and the fields above now approve the exact
TARGET as SPECIALIZE; they do not assert its conclusion.

## Gap and possible downstream use

Here H is the order-16 subgroup of F_97^*, and D and L are exactly the
polynomials defined in L010. The recorded budget at q=97^20 permits fifteen
bad parameters. L010's sixteen bound excludes pencils with a persistent
coordinate locator, while the global model bounds remain 10/q and 69/q.
Handling that excluded class would help assemble a uniform upper bound;
nondegenerate sixteen-count equality and identically singular pencils would
still require their own treatment. No improved bound is established here.

The proposed mechanism removes a fixed coordinate from the decoding problem
and compares the resulting syndrome/locator description with known GRS
decoding and proximity-gap inputs. It does not search the four prescribed
blocks, impose subgroup equivariance, or identify the model with ABF26.
Smoothness is required of the original code; it must not be silently assumed
for a punctured auxiliary domain. Using an auxiliary code does not change the
code for which the final event must be controlled.

## Recovery comparison: three mechanisms

| Mechanism | Source coverage and local redundancy | Decision |
| --- | --- | --- |
| Classify identically singular Hankel pencils using symmetric Kronecker forms | The finite-characteristic classification cited below is available, but arbitrary congruences do not supply a count on prescribed error supports. L007 already treats the three-error cell, and L010 contains a weight-four determinant identity; check those overlaps before attempting a full classification. | Defer; no classification or new implication between the local results is derived. |
| Force a common support through lines in secant varieties | The cited secant-line statement assumes containment of an entire projective line in its specified rank set and works over C. These hypotheses are not supplied by finitely many split locators over F_(97^20). | Do not use as a direct finite-incidence shortcut. |
| Puncture at a persistent coordinate locator and compare the reduced decoder | Readable finite-field decoding inputs are available. The unresolved transfer is different from the four-block construction and does not require the missing July definition. | Select for the exact pending target above. |

L009 already stops the full subgroup orbit, and L008 already supplies ten
challenges. Neither is a reason to repeat those constructions. L010's
fixed-four-support auxiliary example also warns that q decodable parameters
need not be q bad parameters. The new review must retain that distinction.

## Search record

Queries actually issued on October 3 included:

- `"lines" "secant varieties" "rational normal curve"`
- `"Hankel" "pencils" "rank" "rational normal"`
- `"Reed Solomon" "syndrome" "affine" "singular"`
- `"symmetric matrix pencils" "minimal indices" "canonical" finite field`
- `"pairs of symmetric" "characteristic" "canonical" Sergeichuk`
- `"Reed Solomon" "puncturing" "generalized" notes`
- `Prony finite fields annihilating polynomial common root syndrome deflation`
- `"Shift-register synthesis and BCH decoding" pdf Massey`
- `"Reed Solomon" "persistent locator"`
- `"correlated agreement" "puncturing"`
- `"Ben-Sasson" "Carmon" "Haböck" "On Proximity Gaps" pdf`
- `"BCHKS25" "Theorem 1.3"`

The searches located supporting sources, not a checked full-statement match.
No novelty is inferred from a missing search result. ABF26 and Jo retain
their previously recorded unread status and are parked; they are not used
as premises for this independently defined model question.

## Supporting citations and qualifications

### Hypotheses

**Puncturing.** J. I. Hall, [Notes on Coding Theory](https://math.msu.edu/~jhall/classes/codenotes/topstuff.pdf),
undated 204-page online copy read October 3, §6.1.2, printed p. 79, and
§6.2, Theorem 6.2.1 and Proposition 6.2.2, printed pp. 82–83, concern GRS
codes over a field, punctured at specified erasure coordinates. Theorem
5.2.2, printed p. 69, gives key-equation uniqueness with its degree,
coprimality and normalization assumptions. These are decoder inputs,
not uniform counts for affine families.

**Recurrences.** James L. Massey, [Shift-Register Synthesis and BCH Decoding](https://www.isiweb.ee.ethz.ch/archive/massey_pub/pdf/BI411.pdf),
IEEE Transactions on Information Theory 15(1), January 1969, pp. 122–127,
Theorem 3 on p. 124 and Theorem 5 and its corollary on p. 127, concern
shortest linear recurrences and BCH syndrome sequences. The sequence
field may be finite; the decoding corollary assumes 2t <= d-1.

**Proximity gaps.** Ben-Sasson, Carmon, Haböck, Kopparty and Saraf,
[On Proximity Gaps for Reed–Solomon Codes](https://www.math.toronto.edu/swastik/rs-proximity-gaps-2025.pdf),
author manuscript dated November 11, 2025: Theorem 1.3, printed p. 8,
assumes gamma in [delta/3,delta/2-1/n]. Degree bound d corresponds to
dimension d+1 and delta=1-d/n. Theorem 4.6, printed pp. 28–29, counts
same-support failure for gamma < 1-sqrt(d/n). The
[ECCC download](https://eccc.weizmann.ac.il/report/2025/169/download/)
was also accessible; version identity was not checked. Local dimension
eight uses degree bound seven.

**Other mechanisms.** Sergeichuk, [Classification problems for system of forms and linear mappings](https://arxiv.org/pdf/0801.0823v1),
January 5, 2008 corrected author version of the 1987/1988 article,
Theorem 4, printed pp. 27–28, treats pairs of forms in characteristic
different from two; Theorem 2(d), printed pp. 8–9, addresses finite fields.
Gesmundo, Han and Lovitz, [Linear preservers of secant varieties and other varieties of tensors](https://arxiv.org/html/2407.16767v2),
April 16, 2025 version, §2 and Lemma 7.1, work over complex varieties
and assume d >= 2r-1 and a line contained in sigma_r^circ(nu_d(PV)).

### Conclusion

Hall's Proposition 6.2.2 gives the punctured dual multipliers as
u_tilde_i = L_erased(alpha_i) u_i, rather than simple deletion of the
original dual entries. Massey's Theorem 5 identifies the connection
polynomial with product_j(1-X_j Z); its roots are reciprocal locators.
These conventions need to be reconciled with L010's monic locator in X.

BCHKS Theorem 1.3 gives a joint proximity conclusion when the number a
of close challenges is at least (delta-gamma)/(gamma(delta-2gamma)):
the joint distance is at most (1+1/(a-1))gamma. Theorem 4.6 supplies an
explicit Johnson-range bound for the support event. Neither statement
contains the proposed persistent-root reduction. No numerical
specialization or fifteen-count conclusion is made in this turn.

Sergeichuk provides canonical matrix-pair decompositions, not a locator
incidence bound. Gesmundo–Han–Lovitz Lemma 7.1 concludes containment in
an r-secant plane; it does not count a line's finitely many rank-restricted
points over a finite field. No positive-characteristic extension is imported.

### Proof

Use the named source statements for the covered ingredients; no reproof or
new specialization is supplied. The closest previously screened coding
formula is Chojecki's [Integral BCHKS completion](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
label `thm:literature-integral-completion`, equations LC1–LC2, in the mutable
author source dated July 17, 2026. Its reference was followed to the BCHKS
primary statement rather than treating an attribution as source recovery.
The formula assumes 3r >= R+1 and 2r < R, with R=n-k in dimension notation.
It gives no persistent-root transfer, and its CA-to-MCA conversion is not
adopted without checking the pinned support event. There is no claim of
identity with an ePrint version or with the July ABF26 text.

### Mathlib

Full persistent-root count: **not checked**. GRS puncturing, recurrence,
matrix-pencil and secant-line coverage in Mathlib: **not checked**. No
library theorem or absence claim is asserted. The existing ArkLib links
in foundations supply the model definition, not this proposed bound.

## Concrete review and eventual continuation test

The next literature assessment must determine whether the full reduction
and uniform bound are already covered, or isolate the exact specialization
remaining after the citations. In particular, it must assess these issues:

1. Whether the persistent root controls all relevant weight-four supports,
   and how the punctured dual and locator conventions relate to L010.
2. Whether failure on each original agreement support survives the proposed
   comparison. A common sparse lift cannot be counted merely by closeness.
3. How singular parameters with D(gamma)=0, errors omitting the persistent
   coordinate, and multiple persistent roots are included without imposing
   a new genericity assumption.
4. Whether a published bound applies to the actual auxiliary parameters and
   leaves at most fifteen challenges for the original pair, uniformly for
   words over F_(97^20), rather than just prime-subfield words.

A covered full bound would justify IMPORT; covered ingredients with a
precise missing transfer would justify SPECIALIZE. An adequate bounded
search without a match may justify EXPLORE, without a novelty claim. An
unsupported support transfer or a counterexample would reject that proposed
transfer and require a different test, not a return to the blocked PDF.
The review must finish with such an assessment before any derivation.

No calculation, experiment, mathematical proof, or challenge candidate was
produced. The full target remains NOVELTY_UNCHECKED; the supporting results
are known citations. This is a pending assessment for a different target,
not a cleared literature gate or a reset of the old exploration counter.

## October 3 completed source comparison — step 016

### Exact gap and continuation threshold

The completed target is exactly the TARGET above. The gap is L010's
excluded persistent-coordinate class with a nonzero determinant polynomial,
within the already pinned event. The intermediate aim remains a uniform
fifteen-parameter upper bound. That would cover one excluded class at the
recorded field budget; it would leave identically singular pencils,
nondegenerate sixteen-count equality and the actual challenge's definition
and sharp radius unresolved. The current sixteen bound and global
10/q–69/q interval are unchanged.

The discriminating test is whether puncturing can control the **original**
bad set with a combined count at most fifteen, including every exceptional
parameter. A punctured decoding statement, a common large support, or a
prime-subfield experiment alone would not pass this test. An explicit
counterexample to the transfer, or an unavoidable count above fifteen,
would justify stopping that proposed transfer and recording the obstruction.
An insufficient estimate would leave the target open, not prove unsafety.

### Search and access record

New queries actually issued on October 3 included:

- `"Reed Solomon" "mutual correlated agreement" puncturing`
- `"Reed Solomon" "locator" "common root" syndrome`
- `"Reed Solomon" puncturing "affine" "agreement"`
- `"On Proximity Gaps" punctur`
- `"Reed Solomon" "error erasure" "modified syndrome"`
- `"correlated agreement" "puncturing" "theorem"`
- `"persistent root" "Hankel"`
- `"affine" "syndrome" "common" "locator"`
- `site:math.msu.edu jhall codenotes Reed Solomon puncturing`
- `"mutual correlated agreement" "collinearity" Haböck`
- `"A note on mutual correlated agreement" Habock pdf`
- `"WHIR" "mutual correlated agreement" "n" "half"`
- `"Reed Solomon" "common root" "pencil"`
- `"Reed Solomon" "puncturing" "Hankel"`
- `"mutual correlated agreement" "persistent"`
- `"Reed Solomon" "affine pencil" "fifteen"`
- `"Shortening Bounds for Reed-Solomon MCA"`
- `"All Polynomial Generators Preserve Distance" "theorem"`

These searches found coding and MCA inputs and nearby puncture-and-append
and asymptotic results. They did not establish a full-statement match.
Search snippets and repository descriptions were used to locate primary
text, not as theorem evidence. In particular, an index snippet's attribution
for ePrint 2026/1463 was not used; the primary record names Chojecki.

The previously read combined Hall PDF and Massey URL returned Internal
Error in this turn. Hall's
[author index](https://users.math.msu.edu/users/halljo/classes/codenotes/coding-notes.html),
last revised January 7, 2015, supplied readable chapter PDFs. Their
statements were read directly; byte identity with the combined copy is
not asserted. Massey's prior adequate reading is reused, and Hall supplies
readable locator conventions, so no new Massey retrieval is required.
The [2026/1463 record](https://eprint.iacr.org/2026/1463) was readable but
its PDF was not. The author's already known TeX was readable; its date and
labels below identify that reading, without claiming PDF version identity.
July ABF26 and Jo remain unread and parked. Neither is an essential input
to the selected pinned-model specialization.

### Hypotheses

Hall's [GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
Theorem 5.1.1 (printed p. 63) and Theorem 5.2.2 (p. 69), and
[Modifying Codes](https://users.math.msu.edu/users/halljo/classes/codenotes/Mod.pdf),
Theorem 6.2.1 (p. 82), Proposition 6.2.2 (p. 83) and its subsequent
J-syndrome algorithm (p. 84), allow arbitrary distinct field evaluation
points and nonzero GRS multipliers. Erasures and remaining errors must
satisfy g+2e<=n-k. Decoder uniqueness includes the stated degree,
coprimality and normalization conditions. These inputs do not require a
smooth auxiliary domain or input words over the domain's smaller subfield.

The [BCHKS November 11, 2025 author copy](https://www.math.toronto.edu/swastik/rs-proximity-gaps-2025.pdf)
was reread at Theorem 1.3 (p. 8), its proof in §2.3 (pp. 20–21), and
Theorem 4.6 (pp. 28–29). It uses degree at most d, dimension d+1,
distance Delta=1-d/n, and arbitrary finite fields and domains. Theorem
1.3 requires gamma in [Delta/3,Delta/2-1/n]. Theorem 4.6 counts
failure on the same support for gamma<1-sqrt(d/n). Dimension eight
corresponds to d=7; the normalization must survive puncturing.

Haböck's [ePrint 2025/2110](https://eprint.iacr.org/2025/2110.pdf),
copy dated November 17, 2025, was read at Definition 1 (p. 2), Lemma 1
(p. 3), and Theorem 2 with proof (pp. 4–6). The theorem's radius is
gamma=1-(1+1/(2m))*sqrt(rho), m>=3, with rho=d/n for dimension d+1.
Its event uses the same agreement set for the combination and input failure.
This inspected version is not identified with the later author-uploaded
April 2026 copy encountered in search results.

The [WHIR November 21, 2024 copy](https://eprint.iacr.org/2024/1586.pdf),
Definition 4.9, Lemma 4.10 and its proof (pp. 23–24), separates the
general linear-code conversion from its RS corollary. The conversion
requires an already established proximity generator and radius strictly
below half the code's actual minimum distance. Reuse is restricted to
both delta<delta_C/2 and delta<1-B, as explicitly used in its proof;
no wider range is inferred from the displayed B-star formula. Corollary 4.11 uses
WHIR's own RS conventions. Its smooth-code context must not be silently
extended to the punctured auxiliary code. The definition numbering in
this copy differs from the earlier excerpt cited in foundations; this
reading does not change that pinned provenance or certify July ABF26.

Bordage, Chiesa, Guan and Manzur,
[All Polynomial Generators Preserve Distance with Mutual Correlated Agreement](https://eprint.iacr.org/2025/2051.pdf),
copy dated May 19, 2026, was read at Definition 1 (p. 3), Theorem 6.1
(p. 29), Definition 9.1, Theorem 9.2 and Lemma 9.3 (p. 40). The small
error branch of Theorem 6.1 requires gamma<delta_C/(ell+1), where ell
is the generator's output dimension; the separate RS theorem has its
displayed Johnson-range restriction. Neither premise is a persistent
coordinate locator assumption.

### Conclusion

Hall gives the punctured GRS code and dual multipliers
u_tilde_i=L_erased(alpha_i)*u_i. The J-syndrome incorporates these
factors. Its connection polynomial uses reciprocal locator roots.
This covers the coding transformation and decoder conventions, not the
affine-pencil bad-parameter count or preservation of input failure.

BCHKS Theorem 1.3 gives joint distance <=a*gamma/(a-1) when
a>=(Delta-gamma)/(gamma*(Delta-2gamma)); §2.3 identifies a common
affine family of the nearby codewords under those hypotheses. Its
Theorem 4.6 gives a same-support exceptional-set bound. The quantitative
formulas already recorded above are supporting inputs, not a proved
fifteen-count specialization here.

Haböck's Theorem 2 bounds the same-support exceptional set by
ell^7*(rho*n)^2/3, ell=(m+1/2)/sqrt(rho). The proof ends by charging
agreement improvements of each common affine family to coordinate zeros.
Lemma 1 assumes collinearity; it does not produce it. These results
support the required distinction between closeness and original badness,
and do not state a persistent-root puncturing theorem.

WHIR Lemma 4.10 transfers a supplied ordinary proximity-generator error
to MCA without increasing it, within its strict distance range. It is
a usable named conversion, not an unconditional estimate for every
auxiliary code or a theorem about loss at a removed coordinate.

Bordage–Chiesa–Guan–Manzur give the error
max{n*gamma,1}*(ell-1)/|S| on Theorem 6.1's small-radius branch.
Definition 9.1 and Theorem 9.2 provide a quadratic-in-n RS estimate
for polynomial generators. These general sampler results neither replace
the coordinate-factor transfer nor state the needed finite bound for
its excluded class. No source formula was numerically specialized here.

### Closest finite comparison and excluded alternatives

Chojecki's [July 17, 2026-dated author TeX](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex)
was read at `thm:exact-sparsification` (SP2),
`thm:exact-half-distance-sparse` (HD1), and
`thm:literature-integral-completion` (LC1–LC2), including their proofs.
The first splits the maximum into column-far and sparse mutual cases;
the second assumes 2r<=d_min-1. With R=n-k, LC1 assumes
3r>=R+1 and 2r<R; LC2 states

    B_C^MCA(n-r) <= floor(max{ n(R+1-r)/(r(R+1-2r)), r+1 }).

This is a precise finite auxiliary comparison. The original four-error
cell lies at 2r=R, outside LC1. The source's normalization, sparse branch
and integer limit were inspected, closing the earlier comparison gap for
that formula. No common-root transfer appears in these statements, and
no substitution for an auxiliary code is made here. The source's ABF26
attribution is not used to identify the challenge with the pinned model.

Jeronimo's [arXiv:2609.05870v1](https://arxiv.org/html/2609.05870v1),
dated September 5, 2026, Theorem 1.2, Corollary 8.1 and §8.4, was
screened as a new lead. The theorem states a polynomial exceptional
budget for sufficiently large lengths over prime fields. Corollary 8.1
permits puncturing and nonzero coordinate scalings with new length and
absolute agreement requirements. Section 8.4 discusses extensions under
explicit characteristic bounds depending on its interpolation parameters.
Thus it must not be dismissed simply as prime-only, but its stated
large-length and characteristic qualifications and constants have not
been certified for this length-16 field-extension target. It supplies no
ready exact fifteen bound and is not an essential selected input.

Gao, Yang, Xu and Kan,
[arXiv:2607.10572v1](https://arxiv.org/html/2607.10572v1),
Lemma 3 and §4, were reread for the puncturing lead. Their construction
punctures and appends a coordinate to obtain an MCA **lower** bound for
a related code; its RS version may change an evaluation point. This
cannot be imported as an upper bound on the original fixed code.
[Gao–Cai–Xu–Kan 2025/870](https://eprint.iacr.org/2025/870) was only
inspected as metadata in this turn; its full theorem is an unread,
nonessential lead, not an input. No random-domain guarantee is adopted.

### Proof obligations and decision

**SPECIALIZE** approves the unchanged target for a mathematical attempt.
The cited puncturing, decoder and general MCA results are covered
ingredients. Reproving them wholesale would duplicate known mathematics;
any local derivation should be confined to reconciling the determinant
locator with the coding conventions and proving the missing transfer and
finite count. The pending target is not declared known or novel.

The attempt must resolve all of the following within that single target:

1. Verify the error/support consequence of a persistent coordinate root
   at nonsingular parameters using L010's existing locator identities;
   do not assume the same consequence at D(gamma)=0.
2. Check membership and input failure on each original support, treating
   supports containing the removed coordinate explicitly. A punctured
   support that is jointly explained may still need a separate original
   test; an automatic equivalence has not been established.
3. Include every singular bad parameter and any common affine family
   for which many parameters are decodable but few are bad. The existing
   fixed-four-support example is a required regression case.
4. Compare the combined bound with fifteen, not just an auxiliary bound.
   Allow multiple persistent roots and arbitrary extension-field words.
   If the comparison fails, preserve exactly which implication or estimate
   failed rather than reopening the blocked quartet/source route.

These are saved proof questions, not a proof of the transfer. No new
locator, deflated syndrome, count, experiment or mathematical result was
derived. This completed source comparison is **EXPLORATION**,
STEP_KIND **LITERATURE**, STEP_CLASSIFICATION **NOVELTY_UNCHECKED**.
The next invocation may use this ready assessment for mathematical work;
further literature on the same target needs a concrete new source reason.
The old exhausted sequence remains preserved, and this review consumes
no mathematical exploration turn or scheduler reset.

### Mathlib

Full persistent-root count and transfer: **not checked**. Supporting
puncturing, decoder, collinearity and MCA statements in Mathlib:
**not checked**. The direct primary links and theorem labels above
describe source coverage, not formal verification or library absence.
