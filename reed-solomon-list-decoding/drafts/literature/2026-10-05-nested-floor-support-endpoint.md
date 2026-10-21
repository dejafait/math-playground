# Nested-floor packing refinement: completed target review

TARGET: Determine whether the Johnson-Schonheim nested-floor packing bound certifies safety at error index 956 or 957 on C001a's fixed instance for every m>=1.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the prior support assessment's external search and primary packing lead; searched nested/Schonheim/Schönheim/packing in local assessments, histories and ATTEMPTS, and read the relevant support result and failure records. No new broad discovery or numerical refinement.
SOURCE_EVIDENCE: Retrieved Bailey-Burgess, Generalized packing designs, author-hosted November 14, 2011 manuscript, p. 2, Definitions 1.1.1/1.1.3 and Proposition 1.1.4; inspected its full ordinary-packing hypotheses and ordered floors. Read L001 in full, C001a and C012a instance/threshold passages; reused audited L019's unsafe endpoint.
COMPARISON: Proposition 1.1.4 covers selected agreement blocks with v=1024, block size b=68 or 67, strength r=64 and lambda=1; L001 supplies simultaneous common-support uniqueness independently of m. Only finite-instance arithmetic remains; no inspected theorem determines the actual RS list maximum.
GAP: Compute the ordered nested-floor values and compare each integer bound times 2^128 with 65537^28; actual safety when this upper certificate fails and the ABF-model comparison remain open.
REASON: Complete the missing target-specific applicability review using an inspected known theorem, without reproof, new mathematics or a novelty claim; approve the unchanged saved calculation target.
SCOPE: C001a's fixed instance, every m>=1, arbitrary received array, closed simultaneous agreement, errors 956 and 957 only; ordinary packing upper certificate with exact nested floors, ambient threshold and safe equality. No sharpness or exact packing-number claim.
LITERATURE_REASON: The prior support assessment excluded this refinement; agreement-block selection and uniqueness for the changed target required separate applicability approval.

## Proposed bounded test and continuation

The main gap is the exact arbitrary-center boundary; C001a leaves only
indices 956 and 957 undecided on this instance. The intermediate target is
whether the known nested-floor packing certificate decides either index.
Its downstream use is a tighter universal bracket. Continue this certificate
if its exact integer upper bound is <=65537^28/2^128 at either index; otherwise
stop it as a boundary improvement and preserve that failure as a certificate
limitation, not actual unsafety.

Essential inputs are L001's common k-subset uniqueness, C012a's admissible
instance and ambient threshold, C001a's existing bracket, and audited L019's
unsafe index. The known theorem uses v=1024, b=1024-t, r=64, lambda=1.
The review below checks that selecting b agreement columns per candidate
produces distinct blocks even when candidates agree on more columns, that
each r-subset occurs at most once, and that no alphabet-size or exponent-m
assumption is introduced. Nested floors must retain their order and threshold
equality is safe. No source inspected here gives the exact packing number
or actual list maximum. The ABF-model comparison remains independently open.

The previous support assessment's duplicate/failure checks remain relevant;
this does not reopen any stopped character-sum or energy family. Full matching
Mathlib coverage is not checked. This completed review approves only the stated
known-bound application and arithmetic, without asserting an improved endpoint.

## Inspected primary result and applicability approval

Robert F. Bailey and Andrea C. Burgess,
[Generalized packing designs](https://www.math.mun.ca/rbailey00/papers/packings.pdf),
November 14, 2011 author manuscript, p. 2, Definitions 1.1.1/1.1.3 and
Proposition 1.1.4, bounds the maximum block count for positive integers
v>=b>=r and lambda. A packing is a family of b-subsets of a v-set in
which each r-subset belongs to at most lambda blocks. The bound is

\[
U_\lambda(v,b,r)=\left\lfloor\frac vb
 \left\lfloor\frac{v-1}{b-1}\cdots
 \left\lfloor\frac{\lambda(v-r+1)}{b-r+1}\right\rfloor
 \cdots\right\rfloor\right\rfloor.
\]

This primary author statement is the imported theorem, not a new packing
lemma. Johnson and Schonheim's original papers remain unread; no assertion
about their precise statements is based on those references. The page names
the bound after them. Its later small-parameter constructions are outside
this target. The readable theorem extraction supplies the hypotheses and
floor order; a page screenshot was also requested. No new theorem proof is
inferred from a preview or search snippet.

For the applicability dictionary, fix an arbitrary received array and error
index t in {956,957}. Its candidates have at least b=1024-t common agreement
columns. Fix an ordering of the domain and select the first b agreement
columns for each candidate. L001 already establishes that no 64-subset can
be shared by two distinct candidates' full agreement sets. It applies to
whole polynomial tuples over the ambient field, not merely subfield messages
or separately counted rows. Therefore the selected blocks satisfy the
ordinary packing definition with r=64 and lambda=1. In particular repeated
selected blocks cannot occur: any such block contains a 64-subset, forbidden
by that same established uniqueness. Extra agreement columns cause no
problem because selection only deletes columns. The hypotheses v>=b>=r>=1
hold for both stated b. Maximization over centers is permitted because the
same theorem and parameters apply to every center. This checks the known
theorem's hypotheses; no alphabet size or power m enters its bound.

No reproof of Proposition 1.1.4 is needed. The necessary specialization is
only the existing support dictionary followed, next turn, by exact integer
arithmetic. To implement the displayed floor order, start u=1 and for
i=63,62,...,0 replace u by floor((1024-i)*u/(b-i)). Record every intermediate
integer, compare the final u by 2^128*u<=65537^28, and retain equality as
safe. No value of this recurrence has been calculated in this review.

## Duplicate/failure comparison and remaining qualifications

The local nested-floor search found only the prior support assessment,
the pending target and histories 034/035; no completed local refinement
calculation or canonical nested-floor result was found. C001a explicitly
applies L001 alone. Its existing 955<=t_star(m)<=957 bracket is preserved.
ATTEMPTS/007 and /008 stop unsigned-cycle energy and quadratic root-count
allowances for the degree-67 family, respectively. They do not obstruct a
universal support-packing certificate and are not reopened. The previous
support assessment's earlier duplicate/source checks are reused unchanged.

If both computed upper certificates exceed threshold, stop this refinement
as a bracket-improvement route; that finding proves no unsafety and supplies
no exact packing number. A successful certificate would only settle the
corresponding safe index uniformly in m, together with C001a and L019 as
applicable. The independent challenge-wide quantifiers, ABF comparison and
remaining arbitrary-center boundary cannot be inferred from this finite
instance. Mathlib full matching coverage remains not checked.
