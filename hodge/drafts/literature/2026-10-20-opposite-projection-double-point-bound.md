# Opposite image projection and double-point count — source assessment

TARGET: Test whether a general linear projection of L137's original opposite image to P^4 yields a sharper ordered-coincidence bound via the double-point formula.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the registration's notebook-local duplicate/failure search, inspected L120/L121/L137/L139 and ATTEMPTS/070,073,078, and performed bounded external searches for the general-morphism double-point formula and projection of an unramified map with retained multiple fibres; exact queries and inspected sources are recorded below.
SOURCE_EVIDENCE: Fulton, Intersection Theory, 2nd ed. (1998), Theorem 9.3 with proof, pp. 165–167, Corollary 9.2.3/Example 9.2.1, p. 163, Example 3.2.11 and Appendix B.5.8; Fulton, Acta Math. 140 (1978), Theorem 2, Remarks 2.1–2.5 and Section 3, pp. 94–98; Stacks 0B1P, 0B1Q, 0B1R, 0B2L, 05F7 and 02GE; Huybrechts, K3Global author draft, Chapter 1 Section 2.4, equation (2.6) and following Noether calculation, printed pp. 12–13; statements and relevant proofs inspected on 2026-10-20.
COMPARISON: The known residual formula treats a smooth-source morphism without smooth-image or ordinary-double-value hypotheses; the primary triple-plane example explicitly retains six ordered contributions. Primary incidence/dimension tools cover the proposed method, but their smooth-embedded projection statements cannot be applied verbatim to the singular image; the source-parametrized incidence specialization remains the mathematical task.
GAP: Prove the actual general-projection hypotheses by source tangent/secant incidence, identify its finite residual scheme and original-pair contributions, evaluate the diagonal Chern term using L137's pullback, and compare the resulting upper count with L139; none of these specialized conclusions is derived in this literature turn.
REASON: Essential source coverage is now available for one bounded known-tool specialization, pending the supervisor's separate approval of this changed ready assessment; import the general formulas rather than reprove them, and supply only the actual-map incidence and numerical applicability arguments in a later research turn.
SCOPE: Hypothetical L071/L118 locally free Omega-polystable rank-two F with integral c_1=0 and full ch_2=-14e_1-21e_2-tau_D on identical marked K3 factors at the common metric; L120/L121 actual map, L137 original embedding and L139 comparison bound, including empty collisions, arbitrary original fibre sizes, linear degeneracy and N<=4; no projected ordinary-node assumption or F existence.
LITERATURE_REASON: New essential source scope: generic projection of an already self-identifying immersion and the applicable double-point formula with diagonal and multiple-fibre contributions.

## Initial registration retained

The following proposal was recorded before the source review; its missing
coverage is assessed in the completed comparison below, not silently
treated as a completed projection or count calculation.

The main gap remains universal primitive Hodge realization. The proposed
intermediate target is a sharper, geometrically controlled upper count.
Its plausible use is to replace L138/L139's large bound in a future
comparison; no contradictory lower count or F existence is known.

The literature turn should retrieve primary theorem hypotheses and the
relevant proof cases before deciding applicability. It must distinguish
the original image from its projection, verify that any chosen projection
is defined on the whole image, and determine whether the smooth source
map retains immersion and isolated reduced ordered coincidences. Original
fibres with more than two preimages must remain in scope. If a theorem
only permits ordinary double values, its application to the actual map
needs additional coverage, not an assumption that the original multiple
values disappear. The diagonal term and ordered/unordered convention
must be explicit. Low ambient dimensions or linear degeneracy may not
be silently omitted.

Essential inputs for a later mathematical attempt are L120, L121 and
L137, with L139 as the comparison threshold; their retained L071/L118
hypotheses remain conditional. This target does not replace the original
coordinate ring in L138's argument. L137's earlier instruction to retain
that ring belongs to its parameter calculation, not a global prohibition
on a separately justified auxiliary map.

The local comparison also consulted the recorded Markman mismatch in
`2026-10-20-opposite-hom-global-euler-count.md`: a full-moduli diagonal
Chern formula does not become a four-dimensional count formula by
changing its dimension. No such substitution is proposed. Preserve
ATTEMPTS/070,073,078; do not assume minimal normalization gluing,
coherent vanishing or an Euler-sign bound on the ordinary middle sheaf.

Continue only if inspected sources cover an actual auxiliary map and
an evaluable count formula with controlled contributions, and hence
authorize a concrete comparison with L139. Otherwise identify the
specific failed projection or intersection hypothesis and park this
mechanism. Do not approve and derive the missing mathematics in one
turn. No formula, projection theorem, new lemma, mathematical script
or sharper bound is produced by this registration. Mathlib coverage
for this new target is not checked.

## Completed primary-source comparison, 2026-10-20

The main gap is unchanged: no universal realization of primitive rational
Hodge classes, and no existence of the conditional F, is supplied. The
intermediate target is exactly the registered projection/count test. A
smaller fixed upper count could help a later comparison, but no conflicting
lower count is known. This review establishes coverage for an attempt,
not a projected map, an improved estimate or progress beyond the sources.

**General-morphism formula, imported.** [W. Fulton, *Intersection Theory*,
2nd ed., Springer (1998), Section 9.3, Theorem 9.3 and proof,
pp. 165–167](https://djvu.online/file/8KbyCnh9POwWS) assumes a morphism
a:X^n -> Y^m of nonsingular varieties with X complete. On
Bl_{Delta_X}(X x X) it defines a residual scheme T to the exceptional
divisor in the inverse image of Delta_Y. Its support consists of ordered
distinct pairs with equal image and killed tangent directions. The
residual class pushes by the first source projection to

\[
 a^*a_*[X]-\{c(a^*T_Y)c(T_X)^{-1}\}_{m-n}\cap[X].
\]

If T has expected codimension m, its residual class is [T]. The proof
uses Corollary 9.2.3 and graph/refined-Gysin compatibility; Example 9.2.1
also treats an empty residual by separating connected components. This
is an identity for the smooth source, without a normal-image hypothesis.
For a count, finiteness/expected dimension and positive scheme lengths
must first be justified. The empty case remains in scope.

**Multiple values and failure case.** [Fulton, *A note on residual
intersections and the double point formula*, Acta Math. **140** (1978),
93–101, Theorem 2, Remarks 2.1–2.5 and Section 3,
pp. 94–98](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6234-11511_2006_Article_BF02392305.pdf)
gives the expected-codimension formula and its residual-intersection
proof repair. Remark 2.4 explicitly distinguishes the conductor: three
planes in P^4 meeting pairwise transversely at one point contribute six
to the double-point cycle, against conductor degree nine. Thus an
original fibre with more than two preimages is not a reason to discard
the formula. Remark 2.5 warns that the dimension of the source double
locus alone is insufficient: the blowup residual can be too large and
the resulting class negative. The later attempt must control that
residual scheme, not merely its projected support. Remarks 2.1 and 2.3
explain the ramification contributions and positivity when the residual
has the correct dimension. No conductor or normalization-length formula
is being imported into the proposed count.

**Projection coverage and its precise limitation.** The following Stacks
statements and proofs were read in the version served on 2026-10-20:

- [Lemma 43.23.1, 0B1P](https://stacks.math.columbia.edu/tag/0B1P)
  applies to any proper closed subscheme of projective space: projection
  from a point outside it is a finite morphism. Its proof uses properness
  and affine fibres and requires no smoothness or linear nondegeneracy.
- [Lemma 43.23.2, 0B1Q](https://stacks.math.columbia.edu/tag/0B1Q)
  uses tangent and secant incidence for a specified nonsingular point of
  an embedded variety. That pointwise theorem is not a uniform theorem
  on all branches of a nonnormal image. Its method is relevant; applying
  its conclusion directly at a singular value would be unjustified.
- [Lemma 43.23.4, 0B1R](https://stacks.math.columbia.edu/tag/0B1R)
  controls excess intersections of two projected subvarieties by a
  secant-incidence dimension estimate. The theorem with equal varieties
  is not by itself a self-coincidence theorem. The actual source-pair
  incidence must keep the original equal-image pairs separate.
- [Lemma 33.20.4, 0B2L](https://stacks.math.columbia.edu/tag/0B2L)
  gives the generic fibre dimension over the image of an irreducible
  locally algebraic scheme. [Lemma 37.30.1,
  05F7](https://stacks.math.columbia.edu/tag/05F7) permits shrinking an
  irreducible parameter scheme to constant generic fibre dimension for
  a finite-type morphism. They support the required uniform choice of
  projection parameters after the relevant incidence dimensions have
  actually been proved, component by component where necessary.
- [Lemma 29.36.13, 02GE](https://stacks.math.columbia.edu/tag/02GE)
  makes an unramified morphism's diagonal open. Together with
  separatedness this is the applicable clopen-diagonal tool; it does
  not assert that a projected map is unramified.

These primary tools cover the method's needed algebraic operations. The
remaining source-parametrized incidence argument is the identified
specialization, not an imported theorem already proved for this family.
It is necessary because B -> P^N is unramified but may identify points;
reproving the general residual formula or assuming B is embedded would
be unnecessary and incorrect respectively. No novelty claim is made.

For the later characteristic calculation, Fulton's Example 3.2.11,
printed p. 59, and Appendix B.5.8, printed p. 435, provide the projective
tangent Euler sequence. [Huybrechts, *Lectures on K3 Surfaces*, author
draft, Chapter 1, Section 2.4, equation (2.6) and following Noether
calculation, printed pp. 12–13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=13)
gives the K3 tangent Chern numbers c_1=0 and degree c_2=24. These are
standard inputs to be cited; their specialization to the auxiliary map's
double-point number has not been calculated here. No Chow-level assertion
about arbitrary K3 point cycles is required for a degree bound.

## Scope of the later bounded test

After separate approval, the saved target permits only this coherent
attempt with the inspected tools:

1. Start with L120/L121's actual B -> Z and L137's embedding of the
   original Z. Use source tangent-direction and distinct-image
   source-pair incidence to justify a nonempty open set of linear
   projections defined on the whole image. Prove finiteness of the
   residual and retain the original finite coincidence scheme. Do not
   impose smoothness on Z or apply a source theorem to Z's singular
   Zariski tangent space. If tangent injectivity is used, prove it for
   the actual composite, including each original collision branch.
2. Retain arbitrary original fibre sizes. Work with ordered source
   pairs on the blowup, not the set of image singular values; justify
   their contribution by the actual local schemes. Reducedness of
   every newly created projected pair is unnecessary if positive
   lengths suffice, but cannot be claimed without proof. Keep the
   diagonal Chern subtraction even if no tangent direction is killed.
3. Treat N<=4 by the original map followed by a linear inclusion into
   P^4 as appropriate, rather than postulating a nonexistent projection
   centre. For larger N, no linear nondegeneracy hypothesis may be
   silently inserted. Verify that the auxiliary map pulls back the same
   hyperplane line as L137. Use its actual pullback and the standard K3
   tangent Chern data only after the geometric hypotheses are proved.
4. Evaluate the resulting known formula and compare with the actual
   fixed K(K+1) in L139, retaining all admissible parameters and the
   empty case. A count upper bound is not an exclusion of F and supplies
   no algebraic cycle or transverse transport.

Continue if this specialization establishes a finite effective residual
with controlled original-pair contributions and a bound that improves
L139. If any required incidence or residual hypothesis fails, record
that precise failure and park this mechanism; if the bound is valid but
not sharper, report that comparison honestly. Do not replace the
original coordinate ring in L138 or reopen minimal gluing, coherent
vanishing or the middle-Hom Euler estimate.

The essential inputs are L120, L121 and L137; L139 is the comparison
threshold. Their retained L071/L118 assumptions remain hypothetical in
full. F existence, a contradictory lower count and universal primitive
Hodge realization remain independent unresolved gaps. This SPECIALIZE
assessment is newly completed and requires separate approval next turn.
No lemma, mathematical script or specialized count was produced here.
Full matching Mathlib coverage is **not checked**.

## Search and access record

Queries included `Fulton double point formula immersion multiple points
residual intersection formula 9.3`; `generic projection smooth surface
immersion P4 preexisting multiple points secant tangent lines double point
formula`; `linear projection unramified morphism projective variety
generic projection P 2n double points theorem`; `Fulton Laksov residual
intersections double point formula 1978 pdf immersion`; `generic projection
unramified singular surface immersion P4`; and `Fulton double point Theorem
15 Laksov`. Source statements and relevant proof cases above, rather than
search snippets, determine the decision.

The Johnson (1978) paper, generic-projection papers for smooth embedded
varieties, and Catanese's isolated-singularity paper were discovery leads,
not inspected theorem inputs or evidence of this exact specialization.
The Laksov DOI did not open; the accessible Fulton book supplies the
complete general formula and its proof, so that is not an essential
blocker. The first primary-PDF request failed but a repeat succeeded in
the web tool. Shell download failed at DNS and produced no source file;
no API key or paid access was used. The older equality two-branch
assessment and the saved Markman mismatch concern different targets.
No completed local projection-count duplicate was found in the scoped
registration/current search, and absence of a match does not imply novelty.
