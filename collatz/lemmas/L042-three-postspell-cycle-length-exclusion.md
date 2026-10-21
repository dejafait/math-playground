# L042 — Exclusion of actual closed three-postspell concatenations

## Hypotheses

Let T(t)=t/2 for even positive integers and T(t)=(3t+1)/2 for
odd positive integers. O and E denote actual input parities. For
i=0,1,2 let J_i>=2, H_i>=3 and a_i>=0 be integers with
a_i congruent to 2 modulo 18. Put

\[
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},\qquad
D_i=4J_i+H_i+a_i,\qquad N=D_0+D_1+D_2.
\]

Assume W_0W_1W_2 is actual from a positive odd integer n_0>1,
T^N(n_0)=n_0, and its junction occurrences
n_i=T^(D_0+...+D_(i-1))(n_0) are positive odd integers
congruent to 20 modulo 27. Each final even tail is exact; set n_3=n_0.
Independent tails, repeated periods and coincident junction values
are allowed. No least-root, primitive-representation, tail cap,
global-minimum or junction-height-ratio assumption is made.

## Conclusion

There is no actual closed concatenation satisfying these hypotheses.
This excludes only the specified three-word cycle language. It supplies
no three-word affine-closure converse, universal entry, exclusion of
other cycle languages, divergence bound or universal eventual descent.
The separate critical audit below found no defect; published inputs
retain their import qualifications.

## Proof

### Imported theorem and qualifications

Import John Simons and Benne de Weger, *Theoretical and computational
bounds for m-cycles of the 3n+1-problem*, Acta Arithmetica 117 (2005),
51–70, [Corollary 2 and complete proof, printed p. 53; shortcut-map
and period conventions, sections 1.1–1.3, printed pp. 51–53](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
For a positive nontrivial shortcut cycle, its number K of odd input
occurrences satisfies K>225640000. This is not a bound on total steps
or local minima. The published convention permits nonminimal periods;
we apply the result to the primitive period. The corollary imposes no
fixed value or upper bound on the full minimum count m.

The inspected proof invokes Lemma 1, the published computational
height input x_min>301*2^50, and continued-fraction denominators
q_18=225644606 and q_19=397573379. The height input is attributed to
distributed computations [Ro], with a Roosendaal personal-communication
footnote. These are imported published inputs; original certificates
and Crandall's original proof are not independently verified here.
The primary passages and complete corollary proof were inspected in
the reused assessments. No stronger bound or reproof is needed.

L041's inherited Hercher Theorem 16 and Simons–de Weger Lemma 12
estimates retain their precise citations and qualifications, including
the imported Rhin estimate and computational inputs. The recorded
June 2026 Hercher correction concerns Theorem 21, outside these
load-bearing estimates. No external Lean build is certified here.

### Applicability and count comparison

Suppose a concatenation in the hypotheses exists. It satisfies exactly
L041 with r=3, so L041 gives the represented ceiling N<11000 and
the input counts

\[
K=\sum_{i=0}^2(3J_i+H_i),\qquad
L=\sum_{i=0}^2(J_i+a_i),\qquad N=K+L.
\]

Here a_i>=2, so K>=27 and L>=12. The positive odd residue-20
junction n_0 is at least 47. A closed orbit containing it cannot be
a repetition of the invariant shortcut cycle {1,2}, and is nontrivial.

Use L041's audited primitive-period argument. Let p be the least
positive return time to n_0. If N=dp+s with 0<=s<p, periodicity
gives T^N(n_0)=T^s(n_0); minimality forces s=0, hence N=dp
with d>=1. The input parities repeat every p steps. Writing K_0,L_0
for the primitive odd and even counts gives

\[
K=dK_0,\qquad L=dL_0,\qquad p=K_0+L_0.
\]

The primitive orbit is positive, nontrivial and has both input
parities, since K,L>0. Its states are distinct: equality at times
0<=i<j<p would, after p-j further iterates, give a return at time
p-(j-i) strictly between 0 and p. Its cyclic parity sequence has
an E-to-O transition. The odd state u there has preceding state
2u>u and succeeding state (3u+1)/2>u, and is a strict local
minimum. Conversely an even state has a smaller successor, and an
odd state preceded by an odd state v has u=(3v+1)/2>v.
Thus E-to-O transitions are precisely the cyclic local minima.
The orbit is an m-cycle in the source's convention for its actual
positive full minimum count m. No substitution m=3 is involved.

Corollary 2 applies to this primitive cycle and gives K_0>225640000.
Since d>=1, K_0>0 and L>0, the represented ceiling implies

\[
\boxed{225640000<K_0\le K<N<11000,}
\]

which is impossible. This proves the stated restricted exclusion.

Coincident junction values do not remove input occurrences from K,L,N;
the three half-open word intervals partition the represented period.
Repeated representations are handled by d. Every tail remains in L
and N independently of the others. No junction is identified with the
global minimum in the published height input. No converse from affine
divisibility to actual three-word closure is asserted or used.

### Relevance and bounded decision

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-08-three-postspell-cycle-exclusion.md`.
This is a REPRODUCTION application of a known general theorem to
L041's audited restricted ceiling, not a new general cycle theorem
or a claim of progress beyond the sources checked. L040 is a
two-word method comparator, not a mathematical input here.
Attempt 019's guard-only failure and history 069's full-minimum-count
mismatch remain intact; this proof uses the independent length
comparison instead of either failed mechanism.

The continuation test succeeds within the approved scope: the primitive
odd-count threshold exceeds the represented total-length ceiling.
Entry, other word counts, arbitrary cycles, divergence and universal
eventual descent remain unresolved. The separate critical review of
this application is recorded below.

### Separate critical audit — 2026-10-08

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-08-three-postspell-exclusion-audit.md`.
The complete application above was checked against L041's hypotheses,
occurrence counts, primitive-period argument, exact ceiling and canonical
audit, and the published source's sections 1.1–1.3, pp. 51–53, including
Corollary 2 and its complete proof. Verdict: **no defect found within
the stated hypotheses and imported qualifications**. No mathematical
repair or stronger exclusion resulted. This is a REPRODUCTION audit,
not a new result beyond the sources checked.

Every L041 hypothesis holds verbatim with r=3: integer parameters,
their lower bounds and congruences, actual input parities, positivity,
closure, all three odd residue-20 junction occurrences and exact final
tails. Thus its audited N<11000 is available for this represented
period. Its proof uses natural logarithms and an all-real monotonicity
argument; no numerical cutoff search is substituted here. The inherited
cycle estimates keep their cited qualifications. In particular L041's
use of single-word estimates does not import a three-word converse
from L031's two-word closure equivalence.

The three intervals of input times are half-open and disjoint. Each
OOEO contributes three odd and one even input, each terminal O^H
contributes H odd inputs, and each E^a contributes a even inputs.
The input at time N is omitted. This proves the displayed K,L,N
counts even when a junction value occurs more than once. From a>=0
and a=2 modulo 18, a>=2, giving K>=27 and L>=12. Positive odd
integers in residue 20 modulo 27 begin at 47, so n_0 is outside
the invariant orbit {1,2}. Since the whole orbit returns to n_0,
it cannot enter {1,2} at any time; positivity and nontriviality are
therefore properties of its primitive orbit too.

For the period reduction, the nonempty set of positive returns contains
N and has a least element p. The equality T^p(n_0)=n_0 implies
T^(t+p)(n_0)=T^t(n_0) for every t>=0. Divide N=dp+s with
0<=s<p. Closure implies T^s(n_0)=n_0; if s>0 it contradicts
minimality, so s=0 and d>=1. This does not require p to end at
a designated word boundary. Its parity list repeats d times, proving
K=dK_0 and L=dL_0. In particular K_0,L_0 are positive integers.
If two states at 0<=i<j<p were equal, applying T^(p-j) would
give T^(p-j+i)(n_0)=n_0 with 0<p-j+i<p, again impossible.
Thus primitive state counts and primitive input-occurrence counts agree.

Both parities occur, so the finite cyclic parity list has an E-to-O
transition. At its odd state u the predecessor is 2u and the
successor is (3u+1)/2; both exceed u. Every even state has a
smaller successor, and any odd state preceded by an odd v exceeds
v. Consequently these transitions give precisely the full cyclic
minimum count. Rotating the primitive list to any such transition
meets the source's initial-local-minimum convention and leaves K_0,L_0
unchanged. The junctions need not be the primitive minima, and no
substitution of three for the source's m occurs. Its corollary has
no restriction on m.

The cited published Corollary 2 bounds the odd count K_0, not p or
N. Its proof uses Lemma 1, the published height input and the two
continued-fraction denominators recorded above. These are accepted by
precise citation, without independently certifying their computations.
The published height lower bound concerns the global cycle minimum;
no claim that a designated junction attains it is needed. Hence
K_0>225640000. With d>=1 and L>0, K_0<=K<N<11000, a strict
contradiction since 11000<225640000. There is no rounding issue or
missing period factor. Each independent tail remains in L and N;
an arbitrary repetition may change the number of words and is not
silently asserted to remain an exactly-three-word representation.

This completes the approved audit and leaves the argument and direct
DAG input L041 unchanged. Attempt 019 and history 069 still refute
their respective guard-only and minimum-count mechanisms; neither is
used here. The audit supersedes the overview's pending-audit wording
without changing its mathematical assembly. Original Rhin/Crandall
proofs, computation certificates, the external Lean build and exact
Mathlib coverage remain unchecked. Entry into the language, other
counts, arbitrary cycles, divergence and eventual descent remain open.

## Mathlib

Full matching theorem: **not checked**. Supporting return-period
divisibility, periodic occurrence counts and finite-word identities:
**not checked** for exact declarations. No matching theorem or absence
from Mathlib, and no formal verification, is asserted.
