# C099b — d34 all-order full-allocation actual-word exclusion

## Hypotheses

Use L055's complete 25 indexed pairs, changing only H_0=6 and
H_24=32670655. All J_i and all other H_i are unchanged. Set
B=9250245. Let b_i be nonnegative integers with sum_(i=0)^24 b_i=B,
put a_i=2+18b_i, and let pi be any permutation of {0,...,24}.

Let T(n)=n/2 for even positive integers and T(n)=(3n+1)/2 for
odd positive integers. O and E specify actual input parities. Suppose
the concatenation

\[
W_{\pi(0)}\cdots W_{\pi(24)},\qquad
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},
\]

is actual and closed at a positive integer. Require each junction to
be a positive odd integer congruent to 20 modulo27 and each final even
tail to be exact. Repeated periods and coincident junctions are allowed.
There is no minimum, seed, least-root, first-return or primitive-period
premise. All logarithms are natural.

## Conclusion

No such actual closed concatenation exists in any cyclic order over
the full integer tail-allocation simplex specified above.

This is a local RESEARCH/REPRODUCTION application under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-24-d34-all-order-actual-word-application.md`.
It transfers audited C099a to actual words using L041's established
finite-word necessities. It supplies no new general source theorem or
claim of progress beyond the checked machinery. The separate step450
critical audit below found no defect. Other tables, universal entry, unrestricted cycles, divergence
and universal eventual descent remain unresolved; this is not a complete
Collatz candidate.

## Proof

Suppose such a concatenation exists at n_start. Keep its original
chronological order and its indexed allocation fixed. Define

\[
u_0=0,\qquad
u_{k+1}=u_k+4J_{\pi(k)}+H_{\pi(k)}+a_{\pi(k)}
\quad(0\le k<25),
\]
\[
n_k=T^{u_k}(n_{\rm start}),\qquad s_k=n_k+23/11
\quad(0\le k\le25).                                      \tag{1}
\]

Each increment is the positive length of the outgoing word at position
k. These are chronological occurrences, even when their state values
coincide. Actual closure gives n_25=n_0 and s_25=s_0, including for a
representation repeating a shorter period.

For every input k, write n_k=20+27q_k with q_k integral. Positivity
forces q_k>=0, and oddness forces q_k to be odd; hence q_k>=1. Thus

\[
n_k\ge47>1,\qquad s_k\ge540/11\quad(0\le k\le25).          \tag{2}
\]

The complete table has every J_i>=8. Its changed H_0=6 and
H_24=32670655, and its unchanged H_i>=72 for 1<=i<=23, are all
integers at least3. Every a_i is an integer at least2 congruent to2
modulo18, for every allocation in the full simplex. Therefore the
chronologically ordered representation satisfies L041's hypotheses with
r=25, with occurrence parameters (J_pi(k),H_pi(k),a_pi(k)). L041
imposes no ordering of these parameters. Use only its audited finite
passage “Each occurrence's own prefix and the transfer to the next”.
Those identities and necessities apply at every original input without
performing its separate minimum rotation or using its seed or cycle
estimates.

Fix any k with 0<=k<25 and abbreviate i=pi(k). At this word's own
input define y_k=T^(4J_i)(n_k) and z_k=T^(4J_i+H_i)(n_k).
L041's arbitrary-tail finite-word passage gives

\[
y_k+1=(27/16)^{J_i}s_k-12/11,
\]
\[
z_k=(27/16)^{J_i}(3/2)^{H_i}s_k
                  -(12/11)(3/2)^{H_i}-1,                 \tag{3}
\]
\[
11n_k+23\ge2^{4J_i+2},\qquad
2^{H_i}\le y_k+1<(27/16)^{J_i}s_k.                       \tag{4}
\]

These are established necessities for an actual word with an odd endpoint
and arbitrary exact a_i>=2; they do not assert a realization converse.
In particular they are not restricted to E^2 tails. The actual final
a_i even steps give n_(k+1)=z_k/2^{a_i}. Define, exactly as in C099a,

\[
\kappa=23/11,\qquad
G_i=(27/16)^{J_i}(3/2)^{H_i},\qquad
Q_i=(12/11)(3/2)^{H_i}+1.
\]

Substitution of (3) then yields the exact endpoint

\[
s_{k+1}=2^{-a_{\pi(k)}}
       (G_{\pi(k)}s_k-Q_{\pi(k)})+\kappa.                \tag{5}
\]

Both subtracted offsets remain inside division by the actual tail;
kappa is added afterwards. No endpoint has been replaced by a bound.

All quantities to which logarithms are applied below are positive by
(2)–(4). Since 11n_k+23=11s_k, the first inequality of (4) gives
(4J_i+2)log2<=log11+log s_k. Subtracting 2log2 gives

\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).                 \tag{6}
\]

The second inequality of (4) gives

\[
H_{\pi(k)}\log2\le\log(y_k+1)
    <\log s_k+J_{\pi(k)}\log(27/16).                     \tag{7}
\]

Consequently the own-input J guard is non-strict and the own-input H
guard is strict. Equality in the lower bound 2^H<=y_k+1 cannot remove
the strict upper bound, whose negative offset -12/11 is retained in
(3). Each guard concerns outgoing row pi(k), its attached allocation
b_pi(k) and the same actual input s_k. In particular if pi(k)=18,
its strict H guard has that input and pair (693015,3295208), rather
than a neighboring junction or any selected minimum.

The arbitrary index k includes24. At that last occurrence (5) has
output s_25=s_0, while (6)–(7) remain guards at input s_24. A tail
equal to2 may occur at any indexed row or at the chronological closing
word; it satisfies the same finite necessities. No occurrence or closing
edge is lost, and repeated numerical values have not been identified.

Apply audited C099a directly to the single tuple s_0,...,s_25 in
this original chronology. Its table, B, nonnegative integer b_i, full
budget, a_i=2+18b_i and permutation pi are identical. Its lower domains
are (2), its closing equality follows from (1), all 25 exact endpoints
are (5), and its non-strict J and strict H guards are (6) and the
strict consequence of (7). Every premise therefore holds on the same
tuple before invocation. C099a excludes such a real tuple for every
cyclic order and allocation, a contradiction. Its internal normalization
and both cuts are already part of its audited proof; this transfer needs
no further rotation. This proves the stated restricted exclusion.

### Sources, overlap and qualifications

The direct inputs are L041's audited finite necessities, L055's complete
pair table only, and audited C099a. The prior assessment checked known
results, duplicates and recorded failures. C096b covers only literal d34
last-pair words, and C094b covers d6–33; neither is an input or the same
completed application. C099a supplies the table-specific real exclusion;
the added argument matches its premises on actual chronological words.

The inherited finite-affine reference is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section2, equations(2)–(4), Lemma2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its inspected finite composition scope is used upstream, with the
postspell identities and arbitrary-tail necessities explicitly justified
in L031/L041. There is no new fixed-point or parity-coding theorem
application and no reproof is needed. L031's postspell source is
Sodelin, AC-POSTSPELL-GUARDED-ROOT-DESCENT-001,
[sections2–3](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md),
live main inspected 2026-10-04 without an immutable revision or checked
Lean build. Those qualifications persist; no external formal verification
is claimed. C099a's upstream analytic certificates and completed audits
are imported, not rerun. No new numerical certificate is required here.

Attempt032's failed full sufficient-test package and failed S/C/H data
remain valid and unused. Actuality is not used to supply that package,
a minimum, seed, primitive count or realization converse. The proof
uses neither junction-integrality diagnostics nor a cycle theorem on
arbitrary reals. Both original d0 rational witnesses remain on their
different table, and unfinished work is preserved. Other tables and
every universal gap remain open. The step450 audit below secures this
application within its stated scope and inherited qualifications.

### Independent critical audit — 2026-10-24, step450

The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-10-24-d34-all-order-actual-word-critical-audit.md`.
This RESEARCH/REPRODUCTION proof audit found no defect in (1)–(7)
or their application to C099a. The test was to withhold verification,
correct or narrow the conclusion on any missing essential premise,
indexing error, lost closing occurrence or incorrect strict sign.
This secures the existing restricted application as a local input;
it adds no exclusion or progress beyond the inspected source machinery.

**Table and finite-word applicability.** Independently compared L055's
complete table with C099a and this statement. Both change exactly
H_0=40 to 6 and H_24=32670621 to 32670655. Every other pair is
unchanged, including row18 (693015,3295208). Every J is an integer
at least8, and every H is an integer at least6. L055 supplies no
witness allocation, count, seed or minimum premise. Both statements
use B=9250245, integer b_i>=0, sum b_i=B and a_i=2+18b_i.
Thus all tails are integers at least2 congruent to2 modulo18.
The exact same pi is a permutation of all 25 indexed rows.

L041's hypotheses require r>=3, J>=2, H>=3, nonnegative tails
congruent to2 modulo18, an actual closed representation at a positive
odd start greater than1, positive odd residue20 junctions and exact
tails. The first requirements follow from the table and allocation.
For the start and every junction, n=20+27q>0 with q integral gives
q>=0; odd n gives odd q, hence q>=1 and n>=47>1. Therefore
s=n+23/11>=540/11>0. This establishes every remaining domain
requirement, including the closing junction, without selecting a minimum.

**Chronology and imported finite scope.** In (1) the increment
4J_pi(k)+H_pi(k)+a_pi(k) is exactly the full outgoing word length.
The iterate composition law therefore identifies its input with n_k,
its prefix states with y_k and z_k, and its tail output with n_(k+1).
All increments are positive; equal numerical states remain different
time occurrences. Relabel L041's occurrence parameters by pi(k), not
the actual times or allocations. It has no sorted-order hypothesis.

Read L041's own-prefix passage and its completed audit case, and
L031's finite identities (4) and arbitrary-tail boundary-valuation
passage. The necessities concern each word separately. L041's earlier
minimum rotation serves its distinct seed estimate; neither that
estimate nor its cycle-count arguments enter here. In particular,
the valuation passage uses a>=2 and an odd endpoint, and remains
valid at a=2. It does not require the E^2-only transport or two-word
closure converse. This is a scope check of the imported necessities,
not a reproof or an upstream certificate audit.

**Exact endpoint and guard signs.** For the same i=pi(k) and input
s_k, L041 gives exactly the two identities in (3) and inequalities
in (4). Dividing z_k by the actual 2^a gives
2^(-a)(G_i s_k-(12/11)(3/2)^H-1); adding 23/11 yields (5).
Thus its G_i,Q_i,kappa agree term by term with C099a(1). Both
subtractions are inside division; no additive term has been dropped
and no endpoint inequality has replaced an equality.

For J, logarithm monotonicity applied to 11s_k>=2^(4J_i+2)>0
gives (4J_i+2)log2<=log11+log s_k. Subtracting 2log2 gives
exactly C099a's non-strict J guard, since log11-2log2=log(11/4).
For H, the imported 2^H<=y_k+1<(27/16)^J s_k is between positive
quantities. Taking logarithms and transitivity give
H_i log2<log s_k+J_i log(27/16), with a strict sign even if
2^H=y_k+1. The strict upper inequality retains the subtraction
12/11 in y_k+1; it needs no additional bound or feasibility assumption.
Both guards use the outgoing row's own input, including row18 wherever
pi places it. No neighboring state, normalized coordinate or minimum
has been substituted.

**Closing occurrence and complete C099a match.** At k=24 the same
iterate composition gives n_25=z_24/2^a_pi(24). Actual closure says
n_25=n_0, so the equation has output s_0 and the guards still have
input s_24. This includes a_pi(24)=2. Tail2 at any earlier occurrence
uses the identical argument. Repetition of a shorter period changes
neither the list of 25 occurrences nor these endpoint equalities.

C099a's full hypotheses have now been matched: its indexed table,
integer allocation, budget, tails and arbitrary permutation are the
original ones; the real tuple is the single chronological s tuple;
its 25 lower domains and closing equality were established above;
all 25 exact equations equal (5), and both guards equal (6)–(7).
There is no remaining count, seed, minimum, junction-integrality or
realization requirement in C099a. Its completed step446 audit is an
import securing its internal normalization and both cuts. Invoking its
real-system exclusion here is therefore justified without another cut
or an assumed feasible last-pair survivor.

**Evidence, sources and limits.** Complete C099b and C099a were read,
along with the targeted input passages above. The ready application
assessment, application working record and histories448–449 record an
application and proposed audit, not an earlier completed C099b review.
C096b and C094b remain different-scope comparisons, not added inputs.
Attempt032's failure was checked: no full C077a/L083 conjunction or
failed S/C/H datum is inferred from actuality. Both d0 witnesses and
all unfinished work remain valid.

The direct inputs remain L041,L055(table),C099a, exactly the existing
DAG row. The precise primary citations and mutable-source/unchecked
external Lean qualifications in the source section remain in force.
Upstream analytic certificates and audits are imports; no numerical
certificate rerun or mathematical script is needed for this finite
hypothesis audit. Mathlib coverage remains unchecked. No argument or
dependency changed, so PROOF.md and DAG.md receive no status-only
edit; this canonical audit supersedes their pending C099b audit wording.
Universal entry, other tables, unrestricted cycles, divergence and
universal eventual descent remain unresolved. This is not a complete
Collatz candidate.

## Mathlib

Full matching Mathlib coverage is unchecked. Supporting affine,
iterate, valuation and logarithm facts are not a formalization of this
table-specific application. Unknown coverage is not absence; no Lean
verification is claimed.
