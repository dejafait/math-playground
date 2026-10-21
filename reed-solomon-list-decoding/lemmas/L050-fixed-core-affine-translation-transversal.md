# L050 — Fixed-core affine-translation avoidance above the local cap

## Hypotheses

Use precisely L049's original core C={g^e:0<=e<=60}, subgroup
H=<g> of order 1024 with g=19139 in E=F_65537, and fixed labeling

\[
 \sigma(t_j,y)=g^{61+137j+\operatorname{rep}(y)},\qquad
 T=(16,64,70,102,112,118,121)\subset\mathbb F_{137}.
\]

Extend sigma by sending the four dummy points to g^1020,...,g^1023.
As established in L049, this is a set bijection onto H minus C,
not a field embedding. For p in F_137[Z] of degree at most two,
including p=0, write B_p={sigma(t,p(t)):t in T} and
P={B_p:deg p<=2}, the pinned L030 quadratic family.

Retain exactly L049's five polynomials

```text
q0=(33,27,3), q1=(106,120,2), q2=(0,0,0),
q3=(64,44,1), q4=(34,47,2)
```

in constant/linear/quadratic coefficient order. The added forbidden
collections are exactly

\[
 \mathcal E_{a,b}=\{B_{q_i+aZ+b}:0\le i\le4\},
       \qquad (a,b)\in\mathbb F_{137}^2.
\]

A family of seven-subsets of H minus C is called admissible here if it
is independent in L027's G_C and J_C and contains no complete
collection E_(a,b). Only this core, labeling and affine-translation
family is imposed; actual shifts or other obstruction embeddings are
not additional conditions in this definition.

## Conclusion

The designated-member set

\[
 R=\{B_{q_0+aZ+b}:(a,b)\in\mathbb F_{137}^2\}\subset P
\]

has exactly 18769 distinct members and hits every prescribed collection.
Consequently P'=P minus R is admissible and has exactly

\[
 |P'|=137^3-137^2=2552584>1532495,\qquad
 |P'|-1532495=1020089.
\]

The maximum alpha_C of admissible families on all seven-subsets of
H minus C therefore also satisfies alpha_C>=2552584. Any uniform
integer upper cap valid for a local class retaining this family cannot
be at most L027's sufficient benchmark 1532495.

This parks only the fixed-core cardinality diagnostic using precisely
these restrictions. It gives no failure of L027's nonuniform all-core
sum, common-center RS list, safety/unsafety conclusion, optimal deletion
number, or improvement of 955<=t_star(m)<=957. This is a REPRODUCTION
specialization of assessed finite tools. The separate step-158 critical
audit below retains the argument and its fixed-core scope.

## Proof

**Imported coverage and the necessary specialization.** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-11-auxiliary-affine-translation-cap-strength.md`.
Import the definition of a transversal from Artem Chernikov,
*Topics in Combinatorics*, updated 28 February 2017,
[Definition 4.1, printed pp. 21–22](https://www.math.ucla.edu/~chernikov/teaching/Combinatorics285N/CombinatoricsNotes.pdf).
Vertices here are original blocks B_p, and hyperedges are the complete
five-block collections E_(a,b). L049 ensures these are five distinct
members of P for every parameter. We exhibit the transversal directly;
no matching inequality or general removal theorem is needed or reproved.

For packing terminology, reuse R.A. Bailey and A.C. Burgess,
*Generalized packing designs*,
[arXiv:1107.4120v2](https://arxiv.org/pdf/1107.4120v2),
15 November 2011, Definitions 1.1.1/1.1.3, printed p. 2.
L030's pair intersections are at most two, so P is a
(963,7,3,1) packing, with 963>=7>=3. No packing extremal theorem
is applied. L048's designated-member method is a comparison only:
its 1024 loss and its all-core conclusion are not inputs here.
The sources do not themselves count this fixed affine-translation
transversal; that elementary application is the required specialization.

**Membership, distinct deletions and complete coverage.** L030 gives
|P|=137^3=2571353 and independence in both old local edge systems
for this bijection. L049 places every translated block in this same
family. In coefficient order,

\[
 q_0+aZ+b=(33+b)+(27+a)Z+3Z^2.
\]

As (a,b) ranges over F_137^2, its constant and linear coefficients
range bijectively over F_137^2. Thus these polynomials are precisely
all quadratics whose Z^2 coefficient is 3. Their graph blocks are
distinct: equality of B_p and B_r, pulled back through the injective
sigma, gives p(t)=r(t) at every t in T. A nonzero polynomial of
degree at most two cannot have seven distinct roots, so p=r, as in
L030's established graph injectivity. Therefore |R|=137^2=18769.
This counts distinct original members, rather than counting repeated
descriptions. There are no missing designated members in this full P.

For any (a,b), the full designated block B_(q0+aZ+b) belongs to both
R and E_(a,b). Hence E_(a,b) cannot be contained in P'. This argument
covers all 137^2 parameters without a rank-symmetry assumption or a
rank rerun. An unordered collection still contains its designated
member. If a collection has more than one parameter description,
each description supplies a deleted member, so it cannot escape.
No uniqueness of a pattern description is needed. Incomplete
collections are not violations, and deletion creates no new complete
collection. As an additional membership check, the other four
designated polynomials have quadratic coefficients 2,0,1,2,
respectively, unchanged by aZ+b; they lie outside R.

**Old restrictions and the exact integer comparison.** Every pair
or triple among P' already occurred in P, with identical labels
and intersections. Thus independence in both G_C and J_C is inherited
from L030. There is no claim of preserved moments after deletion.
Since R is a subset of the finite P, its exact complement size is

\[
 |P'|=2571353-18769=2552584
       =136\cdot18769,
 \qquad2552584-1532495=1020089>0.
\]

The finite admissible class on all seven-subsets contains P' and the
empty family, so its maximum alpha_C exists and is an integer at
least |P'|. It is not identified with L027's relaxed beta_C. Its
relevance to lists uses the imported local-list statement: at this
core an actual list's selected-support residual family I_C is
independent in both old systems. If it contained E_(a,b), injective
support selection would associate the five distinct residual blocks
with five distinct tuples agreeing with the one center on
C union B_(qi+aZ+b). Audited L049 forces all five tuples equal,
a contradiction. This includes extra agreements and every m>=1.
Thus this precise class is a valid local cardinality upper model,
but its maximum exceeds the proposed uniform benchmark.

L027's greatest sufficient uniform integer cap is 1532495;
equivalently, with its N,D,M,
N*1532495<D(M+1)<=N*1532496. A uniform integer bound valid at
this core must be at least 2552584, so cannot meet that sufficient
benchmark. The present construction provides only one core's lower
bound. It supplies no comparison of the total sum over all cores
with D(M+1); a larger local maximum at one core alone does not
rule out a sufficient nonuniform sum. Nor does the independent
family establish compatibility across cores or a common-center list.
The rank exclusions remain genuine, but exactly this fixed-core
cap test is quantitatively insufficient. Stronger patterns, changed
cores, other embeddings and compatible RS subfamilies are unresolved.

**Separate critical audit (2026-10-11, step 158).** This audit uses the
pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-11-auxiliary-affine-translation-deletion-critical-audit.md`.
The cited transversal definition and packing terminology above suffice;
no additional extremal theorem is invoked. L030's audited incidence
independence and L049's audited exhaustive ranks are imported within
their exact hypotheses, not re-enumerated. The following checks concern
the new deletion and cardinality bridge.

First, the seven label intervals are consecutive disjoint intervals
covering exponents 61 through 1019. The four dummy exponents complete
the complement of C, since g has order 1024. Thus the labeling is a
bijection of sets. Equality of two unordered graph blocks recovers the
point in each column uniquely; it gives equality of the polynomials on
all seven distinct elements of T. The degree-two root bound then makes
the coefficient-to-block map injective, including the zero polynomial.
There are exactly three freely chosen coefficients in the full family.

For a coefficient triple (c,l,3), the unique parameter inverse is
a=l-27, b=c-33 in F_137. Hence R is exactly one full coefficient plane,
not merely an image of size at most 137^2. Its members have nonzero
quadratic coefficient. In particular the zero polynomial remains in
P'. Adding aZ+b cancels from every difference q_i-q_j; these original
differences are nonzero, including q1-q4 despite their equal quadratic
coefficients. Graph injectivity therefore makes every E_(a,b) a
five-element set. Exactly one of its members has quadratic coefficient
3, namely its q0 member. Every prescribed collection is consequently
hit, even as an unordered set or if it had repeated descriptions.
This reasoning quantifies over every parameter and needs no sampling,
rank symmetry, optimal-transversal assumption or unique description.

Second, every forbidden old pair or triple in P' would already be an
identically labeled forbidden pair or triple in P. L030 excludes them.
This establishes heredity without any claim about preserved moments.
The admissible families form a nonempty finite class of subsets of
binomial(H minus C,7), so their cardinality maximum alpha_C is attained
and integral. It is a cardinality maximum for the stated restrictions,
not a claim that this maximum equals L027's relaxed beta_C.

For an actual list, fix one selected 68-support per tuple as in L027.
Its distinct tuples have distinct supports; at the fixed core,
S maps injectively to S minus C. A complete E_(a,b) in I_C would thus
give five distinct tuples, each agreeing with the same center on the
exact corresponding C union B_i^(a,b). Those are precisely L049's
hypotheses. Its audited full-rank conclusion forces equality in every
tuple row, including zero difference rows and extra agreement columns.
This contradicts distinctness and establishes I_C's membership in the
stated local class. It does not realize an arbitrary admissible family
as a list.

Third, exact integer arithmetic was independently reconstructed from
137, n=1024, k=64, core size 61 and the threshold 65537^28/2^128.
Reproduce with

```sh
python3 scripts/finite-support/audit_fixed_core_transversal.py
```

The complete arithmetic certificate is
`scripts/finite-support/fixed-core-transversal-audit-results.json`.
All ten checks pass: 2571353 original blocks, 18769 deletions,
2552584 survivors, cap 1532495 and excess 1020089. The full reconstructed
N, D, M and endpoint products were inspected; they agree with L027
and satisfy N*1532495 < D(M+1) <= N*1532496, with both corresponding
floored certificate comparisons checked. This arithmetic certificate
does not replace the preceding symbolic coverage and applicability proof.

Finally, a uniform integer upper cap valid for classes including this
family at the original core must be at least 2552584, above the greatest
sufficient value 1532495. There is no lower bound here on the sum of
maxima at the other cores. Thus the nonuniform certificate is undecided.
Actual shifts, other embeddings, compatible subfamilies and cross-core
consistency remain outside the conclusion. The audit found no repair
and retains the existing fixed-core stop; it supplies no stronger bound,
new mathematical discovery, common-center realization or safety result.
The direct mathematical inputs remain L027, L030 and L049.

## Mathlib

Full matching fixed-core affine-translation deletion/cardinality
statement: **not checked**. Supporting finite-set difference/image
cardinality, coefficient-translation bijections and hereditary
independence declarations: **not checked**. The polynomial root bound
and graph injectivity are imported through L030; no new Mathlib
coverage claim is made. Unknown coverage is not evidence of absence.
