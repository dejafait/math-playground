# C096b — Literal d34 last-pair actual-word exclusion

## Hypotheses

Use L055's complete 25 indexed pairs in literal order, changing only
H_0=6 and H_24=32670655. Fix B=9250245 and an integer 0<=t<=B.
Set a_i=2 for 0<=i<=22, a_23=2+18t and a_24=2+18(B-t).

Let T(n)=n/2 at even positive integers and T(n)=(3n+1)/2 at odd
positive integers; O and E specify actual input parities. Suppose

\[
W_0\cdots W_{24},\qquad W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},
\]

is actual and closed at a positive integer. Require all junctions to
be positive odd integers congruent to 20 modulo 27 and each final
even tail to be exact. Repeated periods and coincident junctions are
allowed. No minimum, seed, least-root, first-return or primitive-period
premise is imposed. All logarithms are natural.

## Conclusion

No such actual closed concatenation exists for any integer
0<=t<=9250245 in this literal last-pair family.

This is a local RESEARCH/REPRODUCTION application under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-23-d34-last-pair-actual-word-application.md`.
It transfers audited C096a to actual words, using L041's established
finite-word necessities. It claims no new general theorem beyond the
checked source machinery. The separate step-430 critical audit below
found no defect within this restricted scope.
Early-support and cyclic-order reductions for d34, other tables,
universal entry, unrestricted cycles, divergence and universal eventual
descent remain unresolved. This is not a complete Collatz candidate.

## Proof

Suppose such a concatenation exists at n_0. Define chronological times
and junctions by

\[
u_0=0,\quad u_{i+1}=u_i+4J_i+H_i+a_i,\quad
n_i=T^{u_i}(n_0),\quad s_i=n_i+23/11
\quad(0\le i\le25),                                      \tag{1}
\]

where increments are defined for 0<=i<25. Each increment is the
positive number of letters in W_i. Thus i denotes an occurrence,
even when junction values coincide. Actual closure gives n_25=n_0
and s_25=s_0, also for a repeated representation of a shorter period.

For each input write n_i=20+27q_i with q_i an integer. Positivity
forces q_i>=0; oddness forces q_i odd, so q_i>=1. Therefore

\[
n_i\ge47>1,\qquad s_i\ge540/11\quad(0\le i\le25).          \tag{2}
\]

Every J_i in L055's table is at least 8. The changed H_0=6,
H_24=32670655 and all unchanged H_i>=72 for 1<=i<=23 are
integers at least 3. Both varying tails and every fixed tail are
integers at least 2 congruent to 2 modulo 18, throughout 0<=t<=B.
Consequently this actual closed representation with r=25 satisfies
L041's hypotheses, including its positive odd residue-20 junctions
and independent exact tails. We use only its audited passage
“Each occurrence's own prefix and the transfer to the next”, not
its minimum selection, seed, count estimates or primitive-cycle bounds.

Fix any 0<=i<25. At this word's own input let

\[
y_i=T^{4J_i}(n_i),\qquad z_i=T^{4J_i+H_i}(n_i).
\]

L041's arbitrary-tail finite-word necessities give

\[
y_i+1=(27/16)^{J_i}s_i-12/11,\qquad
z_i=(27/16)^{J_i}(3/2)^{H_i}s_i
          -(12/11)(3/2)^{H_i}-1,                         \tag{3}
\]
\[
11n_i+23\ge2^{4J_i+2},\qquad
2^{H_i}\le y_i+1<(27/16)^{J_i}s_i.                       \tag{4}
\]

These are imported established necessities for actual words, not a
parity-realization converse. The exact even tail has
n_(i+1)=z_i/2^{a_i}; hence (3) yields

\[
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
          -(12/11)(3/2)^{H_i}-1\right)+23/11.             \tag{5}
\]

Both subtracted offsets remain inside division by the actual tail,
while the shift 23/11 is added outside. This is an equality.

By (2) and (4) all required logarithms have positive arguments.
Since 11n_i+23=11s_i, taking logarithms in (4) gives

\[
4J_i\log2\le\log s_i+\log(11/4),                         \tag{6}
\]
\[
H_i\log2\le\log(y_i+1)
       <\log s_i+J_i\log(27/16).                         \tag{7}
\]

Thus the J guard is non-strict and the H guard is strict, including
when the lower power bound in (4) is equality. Each uses the same
outgoing row i and its own input s_i, in particular row18 with
(J_18,H_18)=(693015,3295208).

The arbitrary index includes i=24. Its endpoint (5) closes to s_0,
and (6)–(7) there are guards at input s_24. At t=B the final tails
are (a_23,a_24)=(166504412,2); L041's necessities cover this case
without changing any equality or guard. At t=0,1 the respective tail
pairs are (2,166504412) and (20,166504394), also within the same
hypotheses. No closing occurrence is omitted.

Now apply audited C096a to this single real tuple s_0,...,s_25.
Its literal d34 table, integer parameter, budget and complete tail
list are identical. Its lower domain is (2), closure is s_25=s_0,
its 25 exact endpoints are (5), and its own-input guards are (6)
and the strict consequence of (7). Every premise has been matched
before invocation. C096a excludes exactly such a tuple for the entire
closed integer interval 0<=t<=B, giving a contradiction.

There is no rotation or extra cut in this application. Occurrence
labels retain repetitions and coincident junctions. Neither junction
integrality nor a cycle-count theorem on arbitrary reals is needed by
C096a; actuality here supplies only the required finite necessities.
This proves precisely the stated actual-word exclusion.

### Sources, overlap and qualifications

The direct inputs are L041's audited finite-word necessity, L055's
pair table only and audited C096a. The prior assessment checks the
relevant known results, duplicates and failures; C093b/C094b concern
d=6,...,33, while the original-table last-pair applications concern
d=0. None is an identical d34 application or an extra theorem premise.
This local consequence does not establish novelty beyond checked sources.

The reused upstream affine reference is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its previously inspected finite-word composition scope suffices upstream;
no new fixed-point or parity-coding theorem is imported here. All needed
finite identities and valuation necessities are proved in L041's inspected
canonical passage, so no reproof or fresh external retrieval is necessary.
Its upstream mutable postspell source and unchecked external Lean build
retain their recorded qualifications; no external formal verification is
claimed. C096a's analytic certificates and completed audits are imported,
not rerun. This application needs no new numerical certificate.

Attempt032's failed full sufficient-test package remains failed and
unused. Actuality does not supply that package, an early-support/order
exhaustion, minimum, seed or realization converse. Both original d0
rational witnesses and preexisting unfinished work remain valid. No
universal eventual-descent conclusion follows.

### Independent critical audit — 2026-10-23, step 430

This RESEARCH/REPRODUCTION proof audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-23-d34-last-pair-actual-word-critical-audit.md`.
The test was to match every premise of C096a on the same chronological
tuple, correcting or narrowing C096b if a necessity, guard sign or
closing boundary failed. No such defect was found. This validates the
existing restricted application; it adds no exclusion beyond its statement
and claims no mathematical discovery beyond the checked inputs.

**Table and occurrence scope.** The complete L055 table has J_i>=8
at all 25 rows. With exactly H_0=40-34=6 and
H_24=32670621+34=32670655 replaced, all H_i>=3; rows1 through23
have H_i>=72. In particular row18 remains (693015,3295208).
For every admitted integer t, both varying tails are integers at least
2 and congruent to2 modulo18; so are all 23 earlier tails. The times
in (1) increase by the exact lengths 4J_i+H_i+a_i. They label 25
outgoing occurrences, not distinct values. Thus repeated periods and
coincident junctions cause no loss of a word or of its own input.
Closure gives n_25=n_0. No relabeling or minimum selection is made.

For every input i=0,...,24, positivity and n_i=20+27q_i give
q_i>=0 (q_i<=-1 would give n_i<=-7); oddness makes q_i odd.
Consequently n_i>=47>1 and s_i>=47+23/11=540/11. The same
holds at the closing copy. Together with r=25, actuality and exact
tails, these facts match all L041 hypotheses. Its finite-word passage
applies independently of its later minimum, seed and count estimates.

**Every endpoint and both signs.** L041's inspected own-prefix passage
and its completed audit give (3) and (4) for an arbitrary occurrence,
with no restriction to tail2. Its valuation justification uses
2^H(2^a n_(i+1)+1)=3^H(y+1): the parenthesized factor is odd,
so v_2(y+1)=H. For H>=3 the factor
11*2^(H-2)u+3, where u=(y+1)/2^H is positive odd, is odd.
The affine identity therefore gives v_2(11n_i+23)=4J+2,
exactly the necessity used in (4). This checks the imported proof case;
it invokes neither a coding converse nor an E^2-only transport rule.

The actual a_i even steps give n_(i+1)=z_i/2^{a_i}. Substitution
of (3) yields precisely C096a's endpoint (1), with both negative
offsets inside division and the added 23/11 outside. This is checked
as an equality, without replacing it by a growth estimate. For the J
guard, (4J_i+2)log2<=log(11s_i) rearranges to (6), retaining
the non-strict sign and constant log(11/4). For the H guard,
2^{H_i}<=y_i+1 and the exact negative offset -12/11 give
y_i+1<(27/16)^{J_i}s_i. Logarithmic monotonicity on positive
arguments yields (7) and hence a strict H guard. Equality in the
lower power bound cannot change that strict upper inequality.
Both comparisons concern the outgoing row's original input s_i;
in particular row18 has exactly the strict H guard required by C096a.

**Closing case and invocation.** The arbitrary occurrence above includes
i=24: the endpoint is s_25=s_0, while both guards are at s_24.
Since 18B=166504410, the tail pairs at t=0,1,B are respectively
(2,166504412), (20,166504394), (166504412,2). Thus neither a
parameter boundary nor the final tail2 escapes L041's finite necessities.
There is no need to enumerate t: the same argument applies to each
integer in the complete closed interval.

C096a now has the identical table, literal cut, integer t, budget,
complete tail list, all 25 lower domains, exact cyclic endpoints,
non-strict J guards and strict H guards, on this one real tuple.
Its completed step-426 audit supplies exclusion of precisely this
subsystem. Invocation is therefore valid; none of its premises is
inferred merely from the desired conclusion. Its upstream analytic
certificates and audits are imported, not independently rerun here.

**Limits of the verdict.** The direct mathematical inputs remain L041,
L055 (table only) and C096a, as recorded in DAG.md. L031 was inspected
only to check L041's existing finite necessity and source qualifications;
no new direct theorem input was added. The precise primary citation and
mutable-source/unchecked-Lean qualifications recorded above persist.
Attempt032's failed full package is unused, as are minimum/seed,
primitive-count, integer-divisibility and realization-converse arguments.
Both d0 rational witnesses remain on a different table. Early-support
and cyclic-order reductions for d34 and universal eventual descent are
still unresolved. Full matching Mathlib coverage remains unchecked.
No statement, argument or direct dependency changed; PROOF.md and DAG.md
remain untouched. This canonical audit supersedes their pending-audit
wording for C096b only.

## Mathlib

Full matching coverage has not been checked. Supporting affine,
logarithmic and iterate identities are not a full matching theorem.
Unknown availability is not absence; no Lean verification is claimed.
