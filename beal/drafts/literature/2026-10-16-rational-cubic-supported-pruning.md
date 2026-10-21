# Rational-cubic supported units — restriction-rank source comparison

TARGET: Determine the rank of the combined rational-dyadic and rational-eleven-adic Kummer restrictions on the rational-cubic norm-square S-unit subspace of V_S.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the rational-cubic-unit and eleven-adic assessments; checked L071/L073 proof ranges, L074/L076 scope and ATTEMPTS/032–033; searched exact-cubic supported units, certified S-unit generation and simultaneous local two-descent, then inspected the primary statements and proof cases below.
SOURCE_EVIDENCE: Conrad Dirichlet's Unit Theorem, Theorem 4.4 and Corollary 4.6 pp.8–9 https://kconrad.math.uconn.edu/blurbs/gradnumthy/unittheorem.pdf ; Milne ANT v3.08 Theorems 4.3/5.11 pp.70/90 https://www.jmilne.org/math/CourseNotes/ANTc.pdf ; Bruin–Stoll 14 March 2008 Section 6, FakeSelmerSet and complete explanation pp.11–12 https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf ; official PARI stable General number fields entries bnfcertify/bnfsunit/bnfunits/nfislocalpower https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html ; reused Simon/BPT/Clark/Stacks inputs as identified below.
COMPARISON: Known complete-unit certification and finite local restriction methods cover the machinery; L071 already gives the full rational dyadic image and L073 the full rational eleven-adic images, but none of the inspected sources or local results supplies this family's complete generators or combined restriction rank.
GAP: Source coverage is adequate; the exact maximal order, supported generators and their completeness, norm-square kernel, image in D and combined local quotient rank remain mathematical obligations. No generators or rank are computed in this literature turn.
REASON: Approve one bounded specialization of known methods to the unchanged saved target; cite the general results and prove only the field-specific completeness, norm/transport and local linear-algebra calculations next turn.
SCOPE: Exactly TARGET and the family below, including complete cubic supported-unit generation, norm-square kernel and image bookkeeping, both rational eleven-adic restrictions and rational dyadic restriction; no full D-unit or localized class-kernel calculation, other base completions, rank bound or integer exclusion.
LITERATURE_REASON: The supplied REVIEW_REQUIRED gate concerns a new supported family and simultaneous restriction rank; the previous witness and dimension assessments did not cover complete S-unit generation or this combined calculation.

## Exact proposed scope

Use F=Q(t), t³−t²+t+1=0, embedded in the same D by
theta=8−14t+6t² as in L071. Let S_F be all maximal primes above 2
and 11. The proposed family is the image in V_S of

    ker(N_F/Q: O_F[1/22]*/O_F[1/22]*²
                 -> Z[1/22]*/Z[1/22]*²).

The mathematical continuation must check this image and its norm compatibility;
no injectivity of scalar extension to D is presumed. At the rational
dyadic base place of L046 and both rational eleven-adic base places of
L041, restrict the actual classes to the corresponding full cubic
algebra and quotient by the full local Kummer image. The target is the
rank of the resulting combined linear map on this image subspace.
Identical restrictions at different base places must not be counted as
independent. The degree-eleven dyadic and degree-ten eleven-adic base
places are outside this proposed calculation, and remain potential
additional filters.

Essential input IDs: L033 for K/E0; L041 and L046 for the chosen full
base completions; L069 for D and its field degree; L070–L071 for the
rational dyadic image and known removed unit; L073 for full rational
eleven-adic images; L074–L076 for support, containment and the baseline.
There is no cross-notebook input. No class-kernel value, fundamental-unit
basis, class-number-one assertion or square-class injectivity is assumed.

Main gap: primitive integer emptiness. Plausible use: certify independent
global S-unit directions actually removed by simultaneous local
conditions, toward L076's necessary five-direction pruning threshold.
The discriminating test is whether the combined rank is at least two,
strictly improving on L071's single removed direction. A complete rank
of at most one parks this rational-cubic family as a source of a second
direction; an uncertified subgroup or failed generator search does not
establish that negative result. No rank value is derived here.

Unresolved beyond this target are all other S-unit directions, localized
class-kernel arithmetic, the remaining local conditions, a containing
space of dimension at most eleven, and global point/integer lifting.
ATTEMPTS/032–033 remain valid for their stated failed mechanisms; this
target imposes actual local restrictions and retains eleven. Primary
coverage is recorded below; Mathlib coverage of the complete target and
supporting S-unit/local-restriction theorems is not checked. Unknown
availability is not absence.

## Complete supported-unit generation

J.S. Milne, *Algebraic Number Theory*, v3.08 (19 July 2020),
[author PDF](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
Theorem 4.3, printed p.70, gives integral ideal representatives of
every ordinary ideal class with norm at most

    (n!/n^n)(4/pi)^r2 sqrt(|disc(F)|).

Theorem 5.11, p.90, and its valuation-map proof use the full maximal
ring, finite support and roots of unity. These provide completeness
tools, not just a dimension count. The previously inspected Theorem
5.11 proof is reused; the Minkowski statement and nearby class-number
discussion were newly inspected. The future application must certify the actual
field discriminant and supported prime ideals before using either
result. A class-number-one assertion for this F is not imported here.

Keith Conrad, *Dirichlet's Unit Theorem*,
[27-page author PDF](https://kconrad.math.uconn.edu/blurbs/gradnumthy/unittheorem.pdf),
accessed 2026-10-16, no revision date identified: Theorem 4.4 (Artin),
pp.8–9, applies to an order O in a cubic field with exactly one real
embedding. For a real unit v>1 it gives |disc(O)|<4v^3+24.
Corollary 4.6, p.9, gives a fundamental-unit certificate: if a unit u>1
satisfies 4u^(3/2)+24<=|disc(O)|, then u is the positive fundamental
unit. Both complete proofs were read, including the discriminant
maximization and the corollary's exponent comparison. The inequality
does not apply to a unit between zero and one. This is a possible
certificate method, with no specialized inequality checked here.
Use the cited result rather than reprove Artin's bound. Maximality and
all hypotheses still require verification for our cubic.

The [official PARI stable catalogue](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html),
accessed 2026-10-16 without a printed release identifier, gives an
alternative: `bnfinit(f,1)` with `bnfcertify(bnf,0)=1`, followed by
`bnfunits(bnf,S)`, includes nonunit, fundamental-unit and torsion
generators. `bnfsunit(bnf,S)[1]` instead generates modulo ordinary
units. Its units must be supplied separately. The flag-one certification
does not establish full units. `nfislocalpower(nf,pr,a,2)` is an exact
completion-square test. The entry definitions were inspected; a later computation
must record its installed version and certification output. These
specifications are not an executed certificate.

Karim Belabas's [17 August 2022 developer explanation](https://pari.math.u-bordeaux.fr/archives/pari-users-2208/msg00006.html),
read in full, explains valuation/exact-sequence construction, compact
generators and the need for `bnfcertify` to remove GRH. It points to
Simon's relative-norm paper and thesis. The linked AMS paper returned
403 and the thesis was not opened; neither is claimed as inspected
coverage. They are optional leads, not essential premises: the inspected
complete-unit criterion and standard ideal/unit theory offer a separate
manual certificate route. No `gp` or `sage` was found on PATH in this
turn; direct shell retrieval also failed DNS, while web source retrieval
worked. Backend absence does not imply a mathematical obstruction.

## Combined local restrictions

Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic curves*,
Math. Comp. 78 (2009), 2347–2370,
[14 March 2008 author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf):
Section 6, pp.11–12, FakeSelmerSet steps 7–17 and the complete explanation
were read. They impose the norm condition and intersect preimages of
local images, computing localization on generators by finite linear
algebra. The class-group enlargement in its general construction must
not be read as saying supported units exhaust all unramified classes.
Odd degree keeps the full algebra square classes, without a scalar
quotient. Its Section 9, p.15, identifies the cubic genus-one case with
ordinary two-descent; this and the Section 2 exceptional convention,
Section 4 square-class precision, linear-root and reciprocal-chart
proofs are reused from the earlier inspected assessments. No inspected
passage computes our exact combined rank.

Reuse `drafts/literature/2026-10-14-rational-cubic-unit-dyadic-pruning.md`
for Simon (2002), Section 1.1, Propositions 1.1–1.2 p.8; BPT
arXiv:2001.02263v3, Lemma 1.3 and Remark 1.4 p.4; and Stacks
[Lemma 31.18.6, tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2).
They respectively supply the cubic Kummer evaluation, complete local
cardinality and determinant norm under base change. Reuse the Clark
Hensel/Eisenstein coverage in
`drafts/literature/2026-10-15-eleven-adic-even-valuation-containment.md`.
No new scope of these general results is needed: the fields and maps
are unchanged and the new family consists of supported units in that
same rational cubic. Full local images need no fresh point sampling.

L071 proves H2={1,[5-theta]} in the entire cubic dyadic field.
L073's rational-place proof gives H11={1,[(g'(alpha),alpha-beta)]}
in Q11 times Q11(sqrt(-11)), at both rational base places, with the
same distinguished generator and alpha=8 modulo 11. These are full
classes, not just valuation images. The later arithmetic must compare
with them factor by factor; all-even valuations alone are insufficient.
It must justify the effect of the two rational base embeddings rather
than count them as independent conditions automatically.

## Bounded search and the mathematical continuation

New queries were `"t^3-t^2+t+1" "unit"`,
`"t^3-t^2+t+1" "S-units"`, `"X0(11)" "S-units" descent`,
`"PARI" "bnfsunit" "bnfcertify"`,
`"2-descent" "S-units" "local" cubic square classes`, and
`"elliptic" "S-unit" "simultaneous" "2-descent"`.
The inspected matches supply general methods, not this exact rank.
Unrelated search hits and forum computations are not theorem inputs.
Earlier exact-curve comparisons, including Li's incompatible
square-free-discriminant assumption and the quadratic-twist examples,
are reused from the rational-cubic assessment, without refreshing their
unchanged scope or importing their stronger conclusions. Failure to
find an exact match does not establish novelty.

The next research attempt must give complete supported generators
(including torsion), exact norms and the full norm-square kernel, then
transport it to the specified image in V_S. It must justify both support
and norm compatibility with D, and any loss of square classes on scalar
extension. No even-degree injectivity is presumed. The local restriction
map must be well-defined on that image. Use proved square tests or the
certified interfaces above, and retain enough evidence to certify the
kernel and the rank of the combined quotient map. Independent local
nonmembership witnesses alone do not certify independent directions.

This approves a separate RESEARCH specialization of the unchanged
TARGET. No new unit, maximal-order claim, class number, specialized
norm identity or restriction rank has been derived here. A complete
rank at least two supports this mechanism; a complete rank at most one
parks this family for a second direction. Incomplete generators or a
backend failure require an honest partial result, not that negative
conclusion. The remaining degree-36 unit directions, localized class
kernel, other local conditions and primitive integer lifting stay open.
