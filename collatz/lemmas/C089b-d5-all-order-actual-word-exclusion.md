# C089b — d=5 all-order full-allocation actual-word exclusion

## Hypotheses

Use L055's complete 25 indexed pairs, replacing only H_0=40 by 35
and H_24=32670621 by 32670626. All J_i and all other H_i are
unchanged. Let b_0,...,b_24 be nonnegative integers of sum
B=9250245, with a_i=2+18b_i attached to outgoing indexed row i.
Let pi be any permutation of {0,...,24}.

Use the shortcut map T(n)=n/2 for even positive integers and
T(n)=(3n+1)/2 for odd positive integers. O and E specify actual
input parities. Put W_i=(OOEO)^{J_i}O^{H_i}E^{a_i}. Suppose

\[
W_{\pi(0)}W_{\pi(1)}\cdots W_{\pi(24)}
\]

is an actual closed concatenation at a positive integer. Require
every junction to be positive, odd and 20 modulo 27, and every
final even tail to be exact. Repeated periods and coincident
junctions are allowed. There is no minimum, seed, least-root,
first-return or primitive-period premise. All logarithms are natural.

## Conclusion

No such actual closed concatenation exists, in any indexed cyclic
order over the full stated nonnegative integer tail-allocation simplex.

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE
assessment `drafts/literature/2026-10-20-d5-all-order-actual-word-application.md`.
It applies audited C089a's real exclusion using established finite
actual-word necessities. It makes no claim of mathematical progress
beyond the inspected source machinery. The separate critical audit below
found no defect. Other tables, universal entry, unrestricted cycles,
divergence and universal eventual descent remain unresolved.
Attempt 032 and both original d=0 rational witnesses remain valid.

## Proof

Assume such a concatenation exists, with starting input n_0. Define
its chronological boundary times and junctions by

\[
t_0=0,\qquad
t_{k+1}=t_k+4J_{\pi(k)}+H_{\pi(k)}+a_{\pi(k)}
\quad(0\le k<25),
\]
\[
n_k=T^{t_k}(n_0),\qquad s_k=n_k+\kappa,
\qquad\kappa=23/11\quad(0\le k\le25).
\tag{1}
\]

Each increment counts exactly the letters of its actual outgoing
word and is positive. Thus k labels successive time occurrences,
not distinct numerical values. Actual closure gives n_25=n_0 and
s_25=s_0, including when this representation repeats a shorter period.

At every junction write n_k=20+27q_k with integer q_k. Positivity
forces q_k>=0; oddness forces q_k odd, hence q_k>=1. Therefore

\[
n_k\ge47>1,\qquad s_k\ge47+23/11=540/11
\quad(0\le k\le25).
\tag{2}
\]

The complete L055 table has J_i>=8, and its H_i at indices
1 through 23 are at least 72. The changed values 35 and 32670626
also exceed 3. Thus every row has J_i>=2,H_i>=3. The attached
tails are integers a_i>=2 with a_i congruent to 2 modulo 18.
Set J'_k=J_{pi(k)}, H'_k=H_{pi(k)}, a'_k=a_{pi(k)}. These
chronological parameters, r=25, (2), actual closure, the stipulated
junction residues and exact tails meet L041's hypotheses. Use only
its passage “Each occurrence's own prefix and the transfer to the
next,” and its separately audited occurrencewise scope. The minimum
choice, seed and cycle-count estimates in other parts of L041 are
not inputs to that passage or to this proof.

Fix any k with 0<=k<25 and put i=pi(k), J=J_i,H=H_i,a=a_i.
The actual states after the two odd-prefix stages are

\[
y_k=T^{4J}(n_k),\qquad z_k=T^{4J+H}(n_k).
\]

L041's finite arbitrary-tail necessities, at this occurrence, give

\[
y_k+1=(27/16)^J s_k-12/11,\qquad
2^H(2^a n_{k+1}+1)=3^H(y_k+1),
\tag{3}
\]
\[
11n_k+23\ge2^{4J+2},\qquad
2^H\le y_k+1<(27/16)^J s_k.
\tag{4}
\]

The exact even tail also gives z_k=2^a n_{k+1}. Solving (3)
for n_{k+1} and then adding kappa gives

\[
s_{k+1}=2^{-a_i}(G_i s_k-Q_i)+\kappa,
\quad
G_i=(27/16)^{J_i}(3/2)^{H_i},\quad
Q_i=(12/11)(3/2)^{H_i}+1.
\tag{5}
\]

These are precisely C089a's constants. Both subtracted endpoint
terms stay inside division by 2^{a_i}; kappa is added afterwards.
There is no replacement of an actual tail by a comparison tail.

All logarithms below have positive arguments by (2) and (4).
Since 11n_k+23=11s_k, the first bound in (4) implies

\[
4J_i\log2\le\log s_k+\log(11/4).
\tag{6}
\]

The second pair of bounds in (4) implies

\[
H_i\log2\le\log(y_k+1)
 <\log s_k+J_i\log(27/16).
\tag{7}
\]

In particular the required H guard is strict, even if its lower
power bound is an equality. Both guards belong to the same input
s_k and outgoing indexed row i=pi(k), rather than its successor.

The arbitrary choice of k includes k=24, whose actual tail ends
at n_25=n_0. Thus (5) includes the closing endpoint s_25=s_0,
and (6)–(7) at k=24 are guards at s_24 with the outgoing row
pi(24). L041's necessity holds for every a>=2 and an odd endpoint,
so it includes a_{pi(24)}=2 and tail 2 at every other occurrence.
No cyclic cut or time occurrence has been removed.

Now apply audited C089a directly to this chronological real tuple.
Its indexed table, budget B, permutation pi, integer allocation
b_i and attached tails a_i are identical to those stipulated here.
Its lower domain and closure are (2) and s_25=s_0. At every k,
(5) is its endpoint equation with row pi(k), and (6)–(7) are its
non-strict own-input J and strict own-input H guards. Every premise
therefore holds on the same tuple. C089a says no such real tuple
exists, a contradiction.

No new rotation is needed: C089a already handles every permutation
and its internal normalization cuts. Coincident numerical junctions
and repeated periods remain separate indexed time occurrences
throughout. This proves the stated restricted actual-word exclusion.

### Sources, overlap and qualifications

C089a supplies the audited all-order real exclusion; L041 supplies
the finite arbitrary-tail necessity at every chronological occurrence;
L055 supplies only the explicit pair table. L055's original witness,
minimum, seed and d=0 guards are not imported for the changed table.
C088b is the already audited literal-order subcase and a comparison
precedent, not a mathematical input. This application adds the
nonliteral chronological cases to that actual-word statement; it
does not add a new real-system estimate or ordering mechanism.

The reused upstream affine source is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The prior assessment records the inspected finite nonempty-word
hypotheses and essential printed induction cases. All words used
here are finite and nonempty. Any internal fixed-point denominator
qualifications are handled in C089a's audited inputs; this application
takes no new fixed point. L041's already proved actual-word necessities
are instantiated in (3)–(4), not reproved. The only algebra and
logarithms written here are the applicability checks needed to match
the exact shifted endpoint and guard signs. No fresh source retrieval,
numerical certificate or general affine/parity-coding reproof is needed.

The ready assessment and scoped duplicate check found the literal
application and all-order real exclusion, not a completed matching
all-order actual-word application. This is not originality evidence.
Attempt 032's failed full C077a sufficient-test conjunction is neither
invoked nor inferred from actuality. Both d=0 witnesses retain their
different table and scope. No minimum/seed at indexed row0, primitive
count threshold, shifted-integrality assertion, survivor feasibility
or realization converse is used. Other allocations are covered only
within this fixed table and budget. Other tables, universal entry,
unrestricted-cycle exclusion, divergence control and universal eventual
descent remain unresolved; this is not a complete Collatz candidate.

### Independent critical audit — 2026-10-20, step 377

This RESEARCH/REPRODUCTION proof audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-20-d5-all-order-actual-word-critical-audit.md`.
It found no defect in the application to C089a. This establishes
local reliability of the existing restricted exclusion, not an
additional exclusion family or progress beyond the inspected sources.
The main gap remains universal eventual descent. The acceptance test
was a match of every C089a premise on one chronological tuple, with
no added realization, minimum or primitive-count premise.

**Table, allocation and actual chronology.** The complete L055 table
has minimum J equal to 8 and minimum H among rows 1 through 23
equal to 72. Replacing only its two stated entries gives H_0=35
and H_24=32670626, precisely as in C089a. Thus every row is in
L041's J>=2,H>=3 domain. This checks individual row hypotheses,
not merely invariant aggregate counts. L055 contributes its table,
not its original allocation or its real witness.

Both statements use nonnegative integer b_i of sum 9250245,
attached tails a_i=2+18b_i and the same arbitrary permutation pi.
At position k the actual word has 4J_pi(k)+H_pi(k)+a_pi(k)
letters: each OOEO contributes four shortcut steps, each terminal
O one and each E one. Therefore (1) locates the actual input and
output of that very row. In particular b_pi(k), not b_k, supplies
its tail. The increments are positive even when two junction values
coincide. The same definitions cover all 25 outgoing occurrences
of a representation that may repeat a shorter orbit.

**Lower domain and applicability of the finite necessities.**
A positive odd integer 20+27q has integer q>=0 and q odd,
hence q>=1. Thus every input has n_k>=47 and
s_k=n_k+23/11>=540/11. This also gives n_0>1, as L041 requires.
The chronological parameters J'_k,H'_k,a'_k satisfy all of L041's
word hypotheses with r=25; its indexed notation imposes no increasing
order on them. Actuality, exact tails and closure are stipulated for
contradiction and are not deduced from formal affine endpoints.

The inspected L041 passage gives the two identities in (3) at
each occurrence. Its necessity proof is independent of the earlier
minimum choice and seed: 2^a n_(k+1)+1 is odd, so the second
identity gives v_2(y_k+1)=H. For its positive odd quotient u,
11y_k+23=4(11*2^(H-2)u+3) has valuation 2 since H>=3.
The first affine identity then gives v_2(11n_k+23)=4J+2.
This verifies the hypotheses and exact scope of the imported
necessity used in (4). L031 (4) and its boundary-valuation passage
confirm that it holds for arbitrary a>=2; neither the two-word
closure converse nor an E^2-only transport is being imported.
L041's positive lower power bound and strict subtraction of 12/11
give the other pair of inequalities in (4). No cycle-length or
primitive-count estimate is used in these finite passages.

**Endpoint and both guard signs.** Dividing the second identity
in (3) by 2^H and substituting the first yields
2^a n_(k+1)=(3/2)^H((27/16)^J s_k-12/11)-1.
Consequently adding kappa after division by 2^a gives exactly
C089a (1), with Q_i=(12/11)(3/2)^H_i+1 inside that division.
The -1 is not lost or absorbed into kappa, and the actual a_i
is never replaced.

Since 11n_k+23=11s_k, taking logarithms of its positive lower
bound gives
(4J_i+2)log2<=log11+log s_k, equivalent to (6).
For H, monotonicity of log gives
H_i log2<=log(y_k+1)<log s_k+J_i log(27/16).
The strict upper sign follows from the strictly positive subtraction
12/11; it persists if 2^H_i=y_k+1. These are precisely C089a's
non-strict J and strict H guards, both at the input s_k of row
i=pi(k). No successor input or old d=0 guard is substituted.

**Closing occurrence and exclusion.** At k=24 the actual word
ends at n_25=n_0. The endpoint above is therefore the closing
equation s_25=s_0; both of its guards are at s_24 with row pi(24).
Even when a_pi(24)=2, the expression 2^a n_25+1 is odd and all
of the preceding necessity checks apply. The same observation
covers tail 2 at every interior occurrence. No distinctness of
junction values or primitiveness of the representation is needed.

The identical table, permutation, integer allocation and budget,
all lower domains, all endpoints, closure and both own-input guards
now supply the entire premise set of audited C089a. Its exclusion
applies directly to these chronological s_k. The normalization and
both cuts internal to C089a were checked in its step-373 audit;
this application neither adds a rotation nor requires a minimum
at indexed row0. This completes the contradiction.

**Source and scope checks.** The ready assessment's known-result
and duplicate comparisons were reused. The scoped records contain
the construction and proposed audit, not a previous completed
C089b audit. C088b is a literal-order comparison, not a proof input.
The precise primary affine citation and its qualifications above
remain unchanged. No new fixed point or general affine theorem is
needed, and no upstream certificate discrepancy calls for a rerun.
L031 was inspected only to check L041's existing finite passage;
the direct mathematical inputs remain C089a, L041 and L055.

Attempt 032's failed full support conjunction remains failed and
unused. Both original d=0 rational witnesses retain their different
table. No seed, minimum, primitive threshold, integer-realization
converse or assertion of an actual closed orbit enters. Other tables,
unrestricted cycles, divergence and universal eventual descent remain
unresolved. The argument and direct inputs did not change; PROOF.md
and DAG.md are therefore unchanged. This canonical audit supersedes
the overview's pending-audit wording for C089b.

## Mathlib

Full matching Mathlib coverage for this table-specific actual-word
exclusion has not been checked. Supporting finite permutation,
affine and logarithm facts are not a matching theorem. Unknown
coverage is not absence; no Lean verification is claimed.
