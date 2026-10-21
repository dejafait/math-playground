# Primitive dyadic whole-fiber two-descent image — source comparison

TARGET: Determine the two-descent Kummer-class set of primitive whole-fiber-compatible 54a1 dyadic points.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready ramified-image and complete-audit assessments; searched exact 54a1/cusp/Kummer and stronger signature variants; read FNS's excluded-domain clause, full local halving proof and final cusp case, then the corresponding author-code branches. Queries, inspected ranges and limitations are recorded below.
SOURCE_EVIDENCE: FNS final author manuscript dated June 10, 2019, Lemmas 7.3/7.5/7.6 pp.26–28, Lemmas 7.8–7.10 and Remark 7.11 pp.29–31, Lemma 7.12 final case pp.31–32; author section7.magma lines 1024–1079 and 1163–1193, with its GRH boundary at lines 4–15. Reused primary Bruin–Stoll/BPT/Hensel coverage is cited below.
COMPARISON: Established cusp parametrization, formal divisibility and square-neighborhood methods cover a proof attempt; the non-cusp constancy lemma excludes this domain, and the source's global elimination uses conditional Selmer data. Neither it nor the audited unrestricted image directly supplies this exact correlated primitive class set.
GAP: Prove the primitive scalar specialization, uniform full-fiber and embedding coverage, rational-component treatment, finite class reduction and exact realizations before enumerating a restricted image. No cardinality, properness, subgroup structure, global independence or rank improvement is established here.
REASON: Essential source coverage is now available for this independent local proof attempt; specialize known methods with checked coordinate maps rather than importing the conditional global elimination or inventing a new general local theory.
SCOPE: L033's entire K and E0, A2=K tensor Q2 as in L046, L069's two-descent map into (D tensor Q2)*/squares; all whole-fiber identifications at one common rational dyadic scalar, retaining the primitive (3,4,11) witnesses and L032's 54a1 dyadic clauses. No global class, rank or integer conclusion.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED; essential cusp-method and full-fiber comparison were unread. This completes that scope review, without repeating the ready unrestricted-image assessment or performing dependent mathematics.

The proposed set consists of delta_2(P), where s is in Q2, the entire
fiber B_s of the same modular j-map is isomorphic to A2, and P is the
point supplied by that entire identification. Retain every such
identification, including correlations between the rational and
ramified base components. Require one common a,b,c in Z2 with
min(v2(a),v2(b),v2(c))=0,

    a^3+b^4=c^11,  s=1728*a^3/c^11,

with a,b,c nonzero and the retained 54a1 conditions a=7 modulo 8,
b odd and c even. Here delta_2 is L069's map [4x-theta] on finite
points, with its correct origin evaluation. This is a definition of
the proposed target, not an existence or coverage assertion. Exceptional
fibers, removable charts and zero/pole evaluations must be assessed
rather than silently discarded. The displayed minimum is the primitive dyadic condition.

Essential input IDs: L032, L033, L034, L046, L069, L078, L079, L080,
L081. No cross-notebook input. No global unit basis, class-kernel value,
GRH, implicit Selmer/point equality or extra global independence is
assumed. L046's nonempty fifth-power singleton neither proves equality
nor properness for this two-descent target. The full ramified image of
2048 classes is an upper comparison, not the answer to the restriction.

Plausible use: a proper restricted set could add necessary information
to simultaneous global pruning, without solving the independent class,
unit-completeness or integer-lifting gaps. The set need not be a subgroup;
a smaller cardinality alone is not a new independent linear condition.
A complete equality certificate would retire this additional local
filter; a properness certificate would justify testing its global effect.

First compare the exact target with known FNS dyadic branch and
Selmer-group Chabauty methods, including the special cusp branch omitted
from the non-cusp constancy lemma. Reuse the full-image arithmetic
assessment only within its covered scope. Approve a later finite
calculation only after proving a uniform finite reduction with all
embeddings, realizations and square-class collisions retained. Park if
that prerequisite remains source-blocked; do not sample and claim an
exact image. Mathlib coverage has not been checked. No new mathematical
result, computation or ready continuation is supplied by this proposal.

## Completed review, 2026-10-17

The preceding proposal is preserved as the startup definition and test.
Its final statement describes the proposal date; this review supplies
method approval only. The target text is unchanged. The exact set has
not been computed, and no finite reduction is asserted as a new result.

### Primary source and conditional boundary

N. Freitas, B. Naskręcki and M. Stoll, *The generalized Fermat equation
with exponents 2, 3, n*, Compositio Math. **156** (2020), 77–113,
[DOI](https://doi.org/10.1112/S0010437X19007693),
[final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf).
The manuscript is dated June 10, 2019; the
[author's AG57 entry](https://mathe2.uni-bayreuth.de/stoll/schrift.html)
identifies its revision as 2019-06-13. Locators here use printed pages,
not the older manuscript's numbering. Read the primary statements
before their proof cases; the following is a scope assessment, not an
independent verification of source computations.

Lemma 7.6 (p.27) assumes a finite dyadic field without rational
two-torsion and explicitly excludes the 54a1 domain. Lemma 7.9
(pp.29–30) identifies the logarithm above parameter valuation 1/3;
valuation greater than 4/3 implies divisibility by two. Lemma 7.10
(p.30) assumes an analytic map into the reduction kernel, with φ(0)=O,
converging for v2(τ)>−c, c>0, with parameter valuation
ν+v2(τ) throughout that disk, ν>1/3,
and no rational two-torsion. With μ=ceil(ν−1/3)−1, division by
2^(μ+v2(τ)) gives classes constant on odd τ and on nonzero even τ;
ν−μ+min{1,c,ν−1/3}>4/3 merges those classes. Its full
logarithm proof was inspected. Lemma 7.12's cusp case (pp.31–32)
uses centers O and (16,60), the translated parameter
−(x−5)/(y−5), convergence v2(τ)>−5/11 and slope 5/11.
Its final Selmer comparison is conditional. Lemma 7.5's complete
coefficient inequalities and proof (pp.26–27) were read; any use must
check them. Lemma 7.8's global conclusion requires Selmer localization
injectivity, not just local divisibility.

The source does not furnish the requested primitive, fully correlated
set in L078's fixed labels. We therefore approve SPECIALIZE, rather
than import an unqualified answer. Keep the original conditional
classification boundary from the existing FNS assessment.

The [author code index](https://mathe2.uni-bayreuth.de/stoll/magma/index.html#GenFermat)
links [section7.magma](https://mathe2.uni-bayreuth.de/stoll/magma/GenFermat/section7.magma).
Inspected lines 4–15 (GRH setting), 1024–1079 (cusp relation,
translation, convergence check) and 1163–1193 (paired rational and
degree-eleven branches, evaluation, halving and Selmer comparison).
These corroborate the distinction between local branch arithmetic
and the global comparison; no code was executed. Stored Selmer
generators were not read or imported. The index's localtest.magma
was inspected only through its twist/parameter-function declarations;
it is an optional implementation lead, not a certificate for this set.
Finite Laurent precision and selecting a root in published code do
not discharge this notebook's exhaustive-coverage obligations.

### Reused coverage and remaining specialization obligations

Reuse the ready
[ramified-image assessment](2026-10-16-ramified-dyadic-two-descent-image.md)
and [audit assessment](2026-10-16-ramified-dyadic-complete-certificate-audit.md).
Their inspected primary inputs are Bruin–Stoll, *Two-cover descent on
hyperelliptic curves*, Math. Comp. **78** (2009), 2347–2370,
[author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Remark 2.1 and Section 4, especially Lemma 4.4 and the complete
SquareClasses/LocalImage cases; BPT,
[arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3), Section 1,
for the entire monic-cubic map and full-image size; and Clark's
[local-field notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
Corollary 1.77/Theorem 1.79 and Theorem 2.8/Proposition 2.9,
for Hensel and maximal-ring inputs. These remain adequate within
their documented hypotheses. The published general results need
citations, not reproofs.

The approved attempt must establish the following, rather than assume
these consequences of the source review:

1. Translate the original primitive witnesses into an exact scalar
   domain, checking every allowed v2(c)>=1 and all unit parts. Prove
   sufficiency with one common c and an actual fourth power b^4;
   L032's necessary unrestricted square-plus-cube domain alone does
   not provide that specialization. Use the assessed Hensel theorem
   only where its derivative hypotheses hold. L046 is one realized
   fiber, not a uniform-domain proof.
2. Match both analytic cusp branches to L034's complete modular map,
   prove reconstruction and degree-twelve exhaustion, and retain all
   algebra identifications into the fixed A2. A point in H alone does
   not identify the entire fiber. Keep the rational and H components
   at the same τ, including any automorphism action on the fixed
   generator and labels; independent component choices are inadmissible.
3. Check the coordinate change from the source's original x-coordinate
   to L069's X=4x and fixed θ. Treat O, the translated torsion center,
   and removable x=16 charts via the complete map and correct Kummer
   evaluations. The limiting cusp τ=0 is not a finite permitted scalar;
   a class represented only there needs a nonzero-τ realization.
4. Use the cited convergence/divisibility or square-neighborhood
   method to prove a finite reduction, with a uniform treatment of
   the infinite valuation tail. Show realizations for every retained
   case before any exact-set claim. Only then compute labels using
   audited L078–L081 arithmetic and compare complete class collisions.
   Do not promote the source's divided-point classes to classes of
   the original points without the explicit multiplication relation.

This is approval for one bounded proof attempt on TARGET, with finite
enumeration contingent on these proofs. It is not permission to sample
an unproved reduction or to assert that the list already shrinks.
If reduction or realizations cannot be proved, preserve the precise
missing claim and report the partial attempt. A source-method application
or an explicit precision certificate is a useful intermediate milestone.

### Discovery, duplicates, failures and decision test

Searches actually made included `Freitas Naskrecki Stoll "54a1" "cusp"`,
`"X0(11)" "2-descent" "2-adic"`,
`"generalized Fermat" "7.2" "Selmer" Stoll`,
`"54a1" "square class" "2"`, `"54a1" "Selmer" "cusp"`,
`"generalized Fermat" "whole" "fiber" "Kummer"`,
`"54a1" "Kummer" dyadic`, `"54a1" "dyadic" descent`,
and exact displayed-equation/signature variants. The useful matches
were FNS and its primary code. Most exact-signature variants returned
irrelevant hits; that is no evidence of novelty. Older export versions,
ResearchGate copies and unrelated search results are not substitutes
for the inspected final primary text. No stronger unconditional answer
to this precise set was located in this bounded search.

Targeted local checks covered L032's exact dyadic clauses, L033/L034's
map interfaces, L046's full local factor and realization proof, L069's
cubic map, L078/L079/L081's arithmetic/image statements, and history
261's completed audit. No duplicate restricted two-descent set was found
in those records. ATTEMPTS/014's equality concerns the different
five-isogeny map. ATTEMPTS/034–036's exhausted searches and
ATTEMPTS/037's missing unconditional class backend remain parked;
this local target requires none of those missing global inputs.

Continue if the attempt proves an exhaustive reduction or a concrete
certified milestone. Equality with the full correlated comparison would
retire this filter; properness would justify only a later global-effect
test. A smaller set need not be a subgroup or an independent linear
condition, and the 2048-class ramified list omits the rational-component
correlation. No upper bound fourteen-to-eleven improvement follows here.

Mathlib coverage of this exact restricted set and the cited local
specialization is **not checked**; no absence is claimed. No lemma,
mathematical script, DAG edge or assembled argument was changed.
The newly ready assessment is subject to the supervisor's separate
next-turn approval. This review establishes source scope, not new
mathematics or an unconditional signature exclusion.
