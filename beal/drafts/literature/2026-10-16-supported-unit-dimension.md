# Supported norm-square S-unit dimension — source comparison

TARGET: Determine the exact F2-dimension of L074's norm-square S-unit space V_S using the complete prime decompositions above 2 and 11.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the bare-unit and supported-space assessments; inspected the relevant local proof ranges in L041, L046, L069, L071, L073 and L074 and stops ATTEMPTS/032–033; searched S-unit rank and coprime-degree linear-disjointness terminology and read the primary statements below.
SOURCE_EVIDENCE: Simon (2002) Section 1.2 p.8 reaccessed; Milne ANT v3.08 Theorem 5.11 p.90 and Propositions 8.1–8.2 pp.135–136 statements and relevant complete proofs read; Sharifi Abstract Algebra Chapter 6 Proposition 6.3.4 and Corollaries 6.3.5–6.3.6 statements and complete proofs read.
COMPARISON: Known S-unit structure and coprime-degree compositum theory cover the necessary machinery; the local inputs already describe the full base completions and rational cubic, but their assembly, all maximal-prime counts and the specialized dimension remain to be written and checked.
GAP: No essential source gap remains for this target; the mathematical continuation must justify the full dyadic tensor algebra, count every supported maximal prime and apply the square-class norm splitting with roots of unity retained.
REASON: The changed supported target needed its own source comparison; the general theorems are imported, and only their exact local assembly and dimension specialization need reproduction.
SCOPE: The exact saved target, including complete local field-factor counts, S-unit square-class dimensions and the norm-square kernel; no generators, class-kernel calculation, filtered dimension, rank or integer exclusion.

## Relevance, existing work and test

The main gap remains primitive integer emptiness. The intermediate target
is the full S-unit contribution in L074's W_S. It supplies a baseline
for the number of independent conditions a useful filtered descent
bound would have to remove, before the unresolved S-class contribution.
It is not itself a proposed bound below twelve.

L069 handles ordinary units only; L074 identifies the supported quotient
and already proves its scalar norm splitting. L075's audited containment
makes W_S relevant to the entire global Kummer image. No duplicate exact
supported-unit dimension was found in these records. ATTEMPTS/032 parks
the unfiltered rank shortcut, not this baseline. ATTEMPTS/033 requires
retaining eleven and forbids assuming universal even valuations there.

Continue by accounting for every local field factor and the entire
S-unit groups. If a factor count cannot be justified, isolate that exact
factor problem and stop the dimension calculation rather than substitute
a selected factor or a repeated residue factorization. No specialized
prime count, tensor decomposition or dimension is established this turn.

## Primary source coverage

Denis Simon, *Computing the rank of elliptic curves over number fields*,
LMS J. Comput. Math. 5 (2002), 7–17,
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8FAFF26D93D01A154C51CF897E4BE6CD/S1461157000000668a.pdf/computing_the_rank_of_elliptic_curves_over_number_fields.pdf),
Section 1.2, printed p.8, recalls Dirichlet's S-unit theorem with S
including all infinite places: torsion is the roots of unity and free
rank is |S|−1. Reuse the earlier inspected Proposition 1.3 and L074's
norm compatibility; no new descent theorem or reproof is needed.
Simon's reference [15] is Lang, *Algebraic Number Theory*, second edition
(1994); that book was not newly inspected.

J.S. Milne, [*Algebraic Number Theory*, v3.08, July 19, 2020](https://www.jmilne.org/math/CourseNotes/ANTc.pdf):
Theorem 5.11, printed p.90, uses a finite set of finite primes and gives
S-unit rank r+s+|S|−1, with torsion the roots of unity. Its proof uses
the valuation map, ordinary units as kernel, and class-number powers
of the supported primes to obtain full image rank. Propositions 8.1–8.2,
printed pp.135–136, identify irreducible completion factors with extended
places and express the tensor algebra as the product of completions
for a finite separable extension. The proof uses a primitive element,
base change and CRT; no polynomial-order maximality is assumed.
These conventions match L074's finite S and maximal primes; infinite
places enter via the signatures, with no sign restrictions imposed.

Romyar Sharifi, [*Abstract Algebra*, Chapter 6, Section 6.3](https://www.math.ucla.edu/~sharifi/notes/algebra-ch06.html),
author-hosted HTML accessed 2026-10-16, no revision date identified:
Corollary 6.3.6 states that finite extensions of coprime degrees in a
common overfield have compositum degree equal to the product. Its proof
uses tower divisibility and Corollary 6.3.5's product upper bound;
Proposition 6.3.4 supplies the spanning products of bases. Neither
normality nor a Galois assumption is required. For the proposed dyadic
application the common overfield can be an algebraic closure of Q2;
the input degrees are three from L071 and eleven from L046. The future
proof must relate the compositum map to the full tensor algebra, rather
than assume trivial intersection alone implies linear disjointness.

## Exact input scope and remaining obligations

Use L033 for K and E0, L069 for D, its degree and both signatures,
L074 for V_S, injection of S-unit square classes into field square
classes and scalar norm splitting, and L075 for downstream containment.
There is no cross-notebook input.

The local input ranges inspected were L046's complete decomposition
of A2, L041's full A11 factorization and Eisenstein degree-ten model,
L071's exact rational cubic coordinate change and translated Eisenstein
model, and L073's entire rational and degree-ten base-changed cubics.
In L073 both rational places are treated separately and all three roots
over the degree-ten field are exhibited. Its odd local valuation is
preserved; this assessment does not remove eleven from support.

Only the dyadic compositum-to-tensor application and subsequent assembly
are additional mathematical obligations for the saved target. Check
that all local degrees sum to the appropriate full global degree and
that maximal primes are counted once each, without weighting their
count by ramification or residue degrees. Retain the cyclic torsion
square-class contribution. Reuse L074's degree-three norm splitting;
do not assume norm surjectivity on unsquared S-units or a norm-compatible
abstract class splitting. No fundamental generators are required for
a dimension obtained from the structure theorem.

Unresolved beyond this target: explicit S-unit generators, the localized
class-norm kernel, simultaneous local filtering, a dimension useful for
rank below twelve, subgroup indices/cosets and primitive integer lifting.
No novelty is claimed for the general machinery or its proposed
specialization. Mathlib matching and supporting coverage: not checked.
