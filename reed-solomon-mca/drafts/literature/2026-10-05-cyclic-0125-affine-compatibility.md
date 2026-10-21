# Source comparison: cyclic 0125 supports with independent weights

TARGET: Assess whether the sixteen cyclic supports {omega^t,omega^(t+1),omega^(t+2),omega^(t+5)} in the order-sixteen subgroup H of F_97^* can be the full-weight error supports of an L010 equality pencil over F_(97^20), allowing unrelated weights and sixteen distinct parameters.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: October 5 exact cyclic-support, affine-syndrome, transversal and GM-MDS searches found no inspected theorem deciding this family; queries and primary theorem scope are recorded below, with earlier adequate RS and transversal assessments reused.
SOURCE_EVIDENCE: Read Lovett FOCS 2018 Theorem 1.2 and its MDS condition, and Brakensiek–Gopi–Makam 2206.05256v4 Definition 1.4, Definition 1.8, Theorem 1.12 and Corollary 1.15 with proof; reused Hall Theorem 5.1.1 and del Campo III.D.1 from recorded primary readings; checked L009, L010 and L014's inverse compatibility argument.
COMPARISON: RS distance and moment invertibility cover the linear-code inputs; generic or selectable-evaluation GM-MDS results and common-intersection theorems do not decide a transversal line for fixed H; L009 requires one shifted weighted error, while L014 encodes actual compatibility without deciding these supports.
GAP: No theorem or exact certificate decides whether these cyclic supports with independently chosen nonzero weights lie at sixteen distinct points of one admissible affine syndrome line.
REASON: Essential ingredient coverage is adequate for one bounded fixed-family compatibility attempt; only the prescribed-support specialization remains, with no known theorem imported as its conclusion and no originality claimed.
SCOPE: The exact fixed cyclic-label family over F_(97^20), with unrelated full weights and distinct finite parameters, tested using existing RS/moment facts and L010/L014; excludes claims about arbitrary labelings, arbitrary families or ABF26.

## Exact scope and relevance

Here omega is any generator of H; exponents are modulo sixteen and
t runs over Z/16Z. The field, code and moments are those in L010,
specialized to H in F_97^* and F=F_(97^20). Sixteen pairwise distinct
finite parameters gamma_t and words e_t with exactly the displayed
supports would have to satisfy sigma(e_t)=u+gamma_t*v. All indicated
weights must be nonzero. The determinant and coordinate-locator
nonvanishing and equality gates of L010 must be retained. No prime-field
restriction on weights or parameters is allowed. This proposes only a
fixed cyclic-label family test, not exclusion under every labeling and
not a classification of arbitrary supports.

The essential continuation inputs are L010 and L025; L009 is the
known restricted weighted-orbit contrast, and L014 is a possible exact
compatibility tool with its splitting and nonzero-Hankel qualifications.
L024 is a prior exact-family exclusion, not an applicable theorem here.
Nothing from another notebook is needed. The matching-two and
small-union facts are now established in L025; affine compatibility,
arbitrary-support reductions beyond L022, and ABF26 correspondence
remain unresolved. Even an exclusion would leave other families open.

## Search and primary theorem comparison

Queries issued October 5, 2026:

- `"Reed Solomon" "syndrome" "line" "support"`
- `"rational normal curve" "secant" "transversal" lines subspaces`
- `Reed Solomon cyclic error supports independent weights affine syndrome pencil`
- `Reed Solomon syndrome affine line cyclic supports "0,1,2,5"`
- `"Sottile" "four" "eigenvectors" lines`
- `"GM-MDS" theorem support constrained generator matrix Lovett`
- `"Higher order MDS codes" "generic" "Theorem" Brakensiek Gopi Makam pdf`

**Lovett.** Read *MDS Matrices over Small Fields: A Proof of the
GM-MDS Conjecture*, FOCS 2018, printed pp. 194–195,
[Theorem 1.2 and Conjecture 1.1](https://ieee-focs.org/FOCS-2018-Papers/pdfs/59f194.pdf).
For zero sets S_i of k rows, the condition is
|I|+|intersection_(i in I) S_i|<=k for every nonempty I.
Over any field of size at least n+k-1 there exists a k-by-n MDS matrix
with those prescribed zeros. The algebraic formulation uses symbolic
evaluation points, then chooses distinct values. It does not assert
that a preassigned H realizes every pattern. Our errors are sparse
representatives of different cosets, not rows of a code generator matrix.
Thus no existence or exclusion is imported from this theorem. Its proof
of the GM-MDS conjecture was not needed or rereproved.

**Brakensiek–Gopi–Makam.** Read *Generic Reed-Solomon Codes Achieve
List-decoding Capacity*,
[arXiv:2206.05256v4](https://arxiv.org/html/2206.05256v4), specifically
Definition 1.4, Definition 1.8, Theorem 1.12, and Corollary 1.15 with
its proof. Generic evaluation points are independent indeterminates
over an arbitrary finite base field. MDS(ell) requires intersections of
ell column-span subspaces to have the generic dimension. Corollary 1.15
gives this property, GZP(ell) and LD-MDS(ell) for generic RS codes;
its proof uses GM-MDS, dual RS column scaling and Theorem 1.13.
Neither genericity of our fixed subgroup nor a suitable specialization
is certified. Furthermore a common intersection is different from
sixteen distinct intersection points with one affine line. These results
therefore do not decide the target. Theorem 1.5's generic list-decoding
statement was also inspected but is not an affine-line MCA bound.
No use of the full equivalence proof or generic dimension formula is
proposed as a premise.

**Reused exact ingredients.** The October 5
[two-block assessment](2026-10-05-two-block-moment-obstruction.md)
already records Hall, *GRS Codes*, §5.1, Theorem 5.1.1 and its complete
proof, printed pp. 63–64,
[author-hosted chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf).
Any field, distinct evaluation points, nonzero multipliers and 0<k<=n
give dimension k and distance n-k+1. H, unit multipliers, n=16 and k=8
meet these hypotheses over F_(97^20), yielding distance nine.
Reuse this citation and L010's kernel and eight-column Vandermonde
proof; a new distance proof or decoding algorithm is unnecessary.

The [four-block assessment](2026-09-26-current-target.md) records del
Campo, *Galois Groups of Schubert Problems* (August 2012), III.D.1,
printed pp. 29–30, with its graph/eigenline argument, and Sottile,
alg-geom/9510017v1, §7.1, pp. 14–15. Four general four-dimensional
subspaces in dimension eight admit a graph/eigenline description of
transversal two-planes when the required direct sums and graph
isomorphisms hold. This supplies a possible technique only: the selected
supports have overlaps, and no suitable quartet or invertible graph
maps have been established here. Generic split eigenvalue counts cannot
be used for this finite-field configuration. A later attempt must check
those hypotheses before using that description.

## Duplicates, failures and source limits

L009 and ATTEMPTS/004 stop the full orbit of a single weighted error,
even with scalar normalizations. They do not force independently chosen
weights into that form. L024 excludes a doubled eight-vertex family by
fixed-block affine lifting; its conclusion is not about the 0125 family.
L025 and ATTEMPTS/017 stop the universal six-edge/eight-vertex criterion.
No reduction to that criterion or to L022's saved disjoint triple is
allowed. L014's inverse test requires a candidate satisfying all product,
splitting and nonzero-Hankel gates; rank deficiency alone is insufficient.
Its proof was checked through the primitive coefficient argument and
the constant proportionality step. It is a ready tool, not a duplicate
solution of this target.

The earlier four-block and October 3 persistent-root reviews contain
the inspected general MCA/syndrome-space comparisons. Their random-RS,
strict-distance or common-lift hypotheses do not supply a fixed-H
sixteen-support decision. Reuse that coverage without another general
MCA audit. ABF26 and Jo remain unread leads with recorded access
blockers; neither is imported. Their missing challenge correspondence
is independent of this pinned-model restriction test, so the historical
four-block source stop does not block this bounded target.
Search hits on balanced generator matrices, decoder implementations
and patents were not used as theorem evidence. No novelty is inferred
from the exact query's lack of a match.

## Approved bounded continuation and decision test

Proceed with one mathematical attempt on the unchanged TARGET, allowing
all weights and parameters in F_(97^20). Reuse L010 and L025 as essential
inputs and L014 if its exact gates can be met. A direct support-subspace
or inverse-locator obstruction must be proved over the full extension;
a prime-field sample or generic dimension count cannot exclude it.
No new equations, lemma, mathematical script or obstruction were derived
in this source turn.

Continue this mechanism if the attempt supplies an exact, auditable
necessary condition eliminating the family, or a compatible full-weight
pencil passing every L010 equality gate. A witness must have sixteen
distinct finite parameters and nonpersistent actual coordinate locators.
Stop the proposed exclusion upon a valid witness. If the attempt only
imposes shifted weights, assumes unproved genericity, or samples F_97,
record that limitation and abandon that test as a decision procedure.
An inconclusive algebraic attempt must save its remaining obstruction;
it may not claim existence from unsaturated equations or impossibility
from failed sampling. Other support families, the global fifteen bound
and challenge correspondence remain unresolved in either case.

Mathlib coverage of this exact fixed-family theorem and the new
GM-MDS/higher-order-MDS inputs was not checked. Existing L010/L014
Mathlib notes concern supporting algebra; they do not certify this target.
