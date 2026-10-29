# L130 — Large retained families with zero ambient-star overlap

## Hypotheses

Let H be any set of size 1024, K a 60-subset, and a,b distinct elements
of H outside K. Put C=K union {a}, C'=K union {b}, and
Y=H minus (K union {a,b}), so |Y|=962. Use L030's unchanged construction:
q=137, T={16,64,70,102,112,118,121} in F_q,
Omega=(T times F_q) disjoint union D_0 with |D_0|=4, and
P={B_p:deg p<=2}, where B_p={(t,p(t)):t in T}, including zero p.
Fix any bijection sigma:Omega -> H minus C such that
sigma^{-1}(b)=(16,y_0) for some y_0 in F_q.

## Conclusion

There exist a bijection sigma':Omega -> H minus C' with a dummy
mapping to a, and subfamilies

\[
A_L\subseteq\{C\cup\sigma(B_p):p\in\mathbb F_q[X],\ \deg p\le2\},
\quad
A_R\subseteq\{C'\cup\sigma'(B_r):r\in\mathbb F_q[X],\ \deg r\le2\},
\]

such that every two distinct supports in A_L union A_R have
intersection at most 63, and

\[
|A_L|=2552584,\qquad |A_R|\ge2346329>1532496.
\]

The full ambient stars through b on the left and through a on the
right have zero common supports: the right star is empty. Both retained
common-support indicators are identically zero. Hence requiring at
least 1532496 retained supports on each side does **not** force even
one common ambient-star support, much less 18632, under these unchanged
ambient hypotheses. There is no prescribed marginal law or RS
realization. This is a counterexample to the intermediate implication,
not to the RS challenge. The separate critical audit below accepts this
restricted counterexample.

## Proof

**Assessed scope and standard input.** The prior SPECIALIZE assessment
is [the threshold-retention comparison](../drafts/literature/2026-10-26-threshold-retention-ambient-overlap.md).
The standard tools are finite averaging and the endpoint-deletion
alteration method: Noga Alon and Joel H. Spencer, *The Probabilistic
Method*, third edition, Wiley (2008), Theorem 3.2.1 and its proof,
printed pp. 29–30 (PDF pp. 48–49 of the
[primary book PDF](https://math.bme.hu/~gabor/oktatas/SztoM/AlonSpencer.ProbMethod3ed.pdf)).
That theorem's displayed independence bound does not supply balanced
retention in this instance. We import the standard averaging and
edge-endpoint deletion principles used in its proof, and verify their
instance-specific counts and losses below. No general alteration
theorem is reproved. No independence of conflict events is used, and
Markov's inequality is unnecessary. L030 supplies the local polynomial
families and packing; L125 supplies their distinguished-point counts.
L126 and L129 are comparisons only, not inputs.

**Eligible families and conditional sample space.** Delete from the
left family every block containing b. By L125, exactly q^2=18769
polynomials satisfy p(16)=y_0. Therefore the retained left family A_L
has q^3-q^2=2552584 supports, all of the form
K union {a} union U with U a seven-subset of Y. Distinct polynomial
blocks give distinct U, since sigma is bijective and distinct
degree-at-most-two polynomials cannot agree at all seven distinct T
points. No further left deletions will be made.

Fix one dummy d in D_0, and sample sigma' uniformly from all bijections
Omega -> H minus C' conditional on sigma'(d)=a. These exist and number
962!. Every polynomial block avoids d, and indeed all four dummies.
Consequently no right residual block contains a, and each full right
support is K union {b} union V for a seven-subset V of Y. The complete
right ambient star through a is empty for **every** labeling in this
sample space. Hence its intersection with the left ambient star is
empty regardless of any deletions. There are q^3=2571353 right supports.

For each fixed right polynomial r and each seven-subset V of Y,
exactly 7!955! conditional bijections send B_r onto V: choose its
bijection to V and then biject the remaining 955 domain labels with
the remaining Y labels. Thus sigma'(B_r) is uniform over all
binom(962,7) seven-subsets of Y. The three unfixed dummies are among
the remaining domain labels; they impose no additional condition.
This calculation is a marginal statement for each r, not independence
between images of different r.

**Every forbidden cross pair is counted.** Fix U from the eligible
left family and a right polynomial r. Left supports contain a but
not b; right supports contain b but not a. Thus these cross supports
are always distinct, and their intersection size is exactly
60+|U intersect sigma'(B_r)|. It exceeds 63 precisely when that
residual intersection has size j>=4. The conditional probability is

\[
p_*=
\frac{\sum_{j=4}^7\binom7j\binom{955}{7-j}}
     {\binom{962}{7}}
=\frac{5074362896}{148010696600541632}
=\frac{317147681}{9250668537533852}.
\]

The numerator chooses the j residual labels in U and the other 7-j
outside U. The range includes j=7, so even identical residual subsets
are counted as forbidden cross pairs; their full supports still differ.
No equality exception removes an edge here.

Let E(sigma') count all such forbidden pairs with one member in A_L
and one in the complete right family. This is a finite nonnegative
integer. Linearity of expectation, with no independence assumption,
gives exactly

\[
\mathbb E E=(q^3-q^2)q^3p_*
=\frac{3798592669695986594}{16880782002799},
\qquad 225024<\mathbb E E<225025.
\]

Finite averaging therefore supplies a conditional labeling with
E(sigma')<=floor(E E)=225024. The expectations and the zero-overlap
condition hold on the same sample space; overlap is deterministically
zero, so no intersection of separately favorable events is assumed.

**Deletion and all packing conditions.** Fix that labeling. Remove
every right support incident with at least one of its forbidden pairs.
The number removed is at most the number of pairs, because the edge
set maps onto those right endpoints. Repeated endpoints only reduce
the loss. Thus the remaining A_R has size at least
2571353-225024=2346329. There are no forbidden cross pairs left.
Within either side, L030 gives residual intersection at most two
between distinct blocks; adjoining its fixed 61-point core gives
intersection at most 63. Deleting blocks preserves this condition
and L030's local determinant-hyperedge avoidance. These statements
hold for the actual arbitrary label bijections; there is no assumed
field-preserving labeling or auxiliary packing realization.

The left and right margins above the required threshold 1532496 are
1020088 and at least 813833, respectively. The right loss cap 225024
is below its allowed deletion budget 2571353-1532496=1038857.
No retained left support contains b, and no ambient right support
contains a, so retained common indicators agree at zero as claimed.
All stated conditions therefore hold simultaneously. This negates the
assessed retention-to-overlap implication without touching the valid
high-overlap conditional obstructions or the unresolved RS target.

**Exact certificate and qualifications.** Run
`python3 scripts/finite-support/threshold_retention_alteration.py`.
The full arithmetic certificate is
`scripts/finite-support/threshold-retention-alteration.json`.
It records all eight intersection counts, checks each probability
against an ordered-injection calculation, checks both distribution
totals, the exact rational expectation and integer floor, both size
thresholds, and a separate fourth-subset union-bound comparison.
The symbolic conditional-sample-space and averaging arguments above
prove existence; no labeling was randomly sampled or asserted to be
an explicit deterministic example. The construction certificate is arithmetic support; the independent
critical audit below also checks the symbolic existence and packing proof. This finite specialization
is local progress beyond the general source tools; originality beyond
the sources assessed is not certified. No numerical RS-list evidence
or complete challenge candidate is claimed.


**Separate critical audit (2026-10-26, step 507).** The invocation-start
SPECIALIZE [audit assessment](../drafts/literature/2026-10-26-l130-critical-audit-coverage.md)
covers precisely this conditional-label construction. The audit accepts
all stated conclusions, with no changed hypothesis or bound. The
standard source contributes averaging and endpoint deletion only;
the following checks certify the finite specialization, not originality.

The input restriction from L030 is its actual seven-point polynomial
packing, not its permutation-averaged moments. The distinct elements of
T lie in the prime field F_137; evaluation at 16 is a nonzero linear
functional on three coefficients, giving exactly q^2 blocks through b
as used in L125. A difference of distinct polynomials has at most two
roots, proving distinct indexing and same-side packing for both
arbitrary bijections. None of L125's prescribed marginal laws, positive
probability event or rigidity conclusions is imported. The determinant
pattern avoidance claimed above is inherited from L030 under deletion;
no mixed-core determinant exclusion is claimed or required.

The conditional space fixes exactly one of 963 domain labels and one
codomain label. It is nonempty and has 962! elements. Each B_r avoids
all four dummies, so its image lies in Y; there are exactly 7!955!
extensions for every seven-subset image, with the other three dummies
unrestricted. This proves the fixed-block distribution even though
different block images are dependent. The deleted left blocks are
exactly those containing b, while all right blocks avoid a. Hence every
cross pair consists of distinct full supports and has intersection
60+j. The j=7 case is a forbidden edge, not an equality exception.
Zero right ambient-star size holds for every member of this very same
conditional space. Thus finite averaging for E automatically preserves
zero overlap; it does not intersect two merely positive-probability
events.

For independent arithmetic, run
`python3 scripts/finite-support/critical_audit_l130.py`.
It counts ordered images by successive draws without replacement.
If d_i(j) counts i draws with j labels in the fixed left seven-set,
the next draw contributes d_i(j)(955-i+j) to d_{i+1}(j) and
d_i(j)(7-j) to d_{i+1}(j+1), starting with d_0(0)=1.
These two choices exhaust the remaining labels. Dividing d_7(j) by
7! gives the following complete unordered-image counts:

| j | Seven-subset images |
| --- | ---: |
| 0 | 140611678829538150 |
| 1 | 7260244744623150 |
| 2 | 137562532003386 |
| 3 | 1205420014050 |
| 4 | 5064789975 |
| 5 | 9566235 |
| 6 | 6685 |
| 7 | 1 |

Their sum is 148010696600541632 and their j>=4 sum is 5074362896.
The resulting probability is exactly the p_* above. The independent
program compares all eight complete saved rows, both probability
representations, all parameters, 962!, the denominator, tail, exact
expectation, union-bound comparison, edge cap and retained-size fields.
All 42 checks pass; the full replay certificate is
`scripts/finite-support/l130-critical-audit.json`.
It records the complete ordered-draw layers, input digest and exact
recomputed fields; no large integer or row is certified from a preview.
The expectation's numerator minus 225024 times its denominator is
11580298144418, strictly between 0 and 16880782002799. Thus the floor
225024 and both claimed retained sizes and margins are exact.

Because E is integer-valued on a finite nonempty space, its minimum
is at most its mean and hence at most that floor. Distinct polynomial
indexing ensures E counts actual cross edges without multiplicity from
representations. Deleting their right endpoints removes at most E
supports, eliminates every cross conflict and leaves the left family
unchanged. Both sidewise packing bounds persist. Every selected left
support omits b and every ambient right support omits a, so the two
retained indicators on supports containing both cores are identically
zero. This verifies all conditions simultaneously under the original
labels. No explicit labeling, prescribed law, global extension or
common received-word realization follows. The accepted negative result
concerns the proposed intermediate implication only.

## Mathlib

Full matching counterexample and this finite conditional alteration:
**not checked**. Supporting finite averaging, finite-set counting,
hypergeometric probabilities and polynomial root bounds: **not checked**.
Unknown coverage is not evidence of absence. The standard alteration
input is imported by the precise citation above.
