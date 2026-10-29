# C108b — d35 all-order full-simplex actual-word exclusion

## Hypotheses

Use L055's complete 25 indexed pairs, changing only H_0 to 5 and
H_24 to 32670656. All J_i and all other H_i are unchanged. Let

\[
B=9250245,\qquad b_i\in\mathbb Z_{\ge0}\ (0\le i<25),\qquad
\sum_{i=0}^{24}b_i=B,\qquad a_i=2+18b_i,
\]

and let pi be any permutation of {0,...,24}. Each indexed outgoing
row retains its own J_i,H_i,b_i,a_i under this permutation.

Let T(n)=n/2 for even positive integers and T(n)=(3n+1)/2 for
odd positive integers. O and E specify actual input parities. Set

\[
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},\qquad D_i=4J_i+H_i+a_i,
\]
\[
u_0=0,\qquad u_{k+1}=u_k+D_{\pi(k)}\quad(0\le k<25),
\qquad N=u_{25}.
\]

Suppose W_pi(0)...W_pi(24) is actual at a positive odd integer
n_0>1 and is closed: T^N(n_0)=n_0. For 0<=k<=25 define
n_k=T^{u_k}(n_0). Require every junction n_k for 0<=k<25 to be
positive, odd and congruent to 20 modulo 27. Require every final
even tail to be exact: if z_k=T^{4J_pi(k)+H_pi(k)}(n_k), then
v_2(z_k)=a_pi(k). In particular the last tail ends at the odd
junction n_25=n_0.

Zero budgets, including a tail of 2 on the chronological closing
edge, are allowed. Repeated periods and coincident junction values
are allowed. There is no prescribed minimum, seed, least-root,
first-return or primitive-period assumption. All logarithms are natural.

## Conclusion

No such actual closed concatenation exists, for any allocation in the
stated full integer simplex and any permutation of the intact rows.

This is a local RESEARCH/REPRODUCTION application under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-27-c108a-all-order-actual-word-transfer.md`.
It transfers the audited restricted real exclusion C108a to actual
words; the separate step533 applicability audit below finds no defect
relative to the audited inputs. It is not
a complete Collatz candidate or a claim of progress beyond the checked
source machinery. Entry into this language, other tables, unrestricted
cycles, divergence and universal eventual descent remain unresolved.

## Proof

Assume such a word, allocation and permutation exist. Keep the original
chronological cut, all occurrence indices and the indexed allocation.
Define

\[
\kappa=23/11,\qquad s_k=n_k+\kappa\quad(0\le k\le25).
\tag{1}
\]

For each input k write n_k=20+27q_k with q_k integral. Positivity
forces q_k>=0, and oddness forces q_k odd, hence q_k>=1. Thus
n_k>=47. Closure gives n_25=n_0, and consequently

\[
s_k\ge47+23/11=540/11>0\quad(0\le k\le25),\qquad s_{25}=s_0.
\tag{2}
\]

The complete table has every J_i>=8. The two changed H values,
5 and 32670656, and all unchanged H_i for 1<=i<=23, which are
at least72, are integers at least3. For every permitted budget,
a_i is an integer at least2 congruent to2 modulo18. Therefore
L041 applies with r=25 and occurrence parameters
(J_pi(k),H_pi(k),a_pi(k)). Its actual concatenation, closure,
positive odd residue20 junctions and exact-tail hypotheses are
precisely among the assumptions above. The times u_k are its
cumulative chronological word lengths. Independent tails, repetitions
and equal junction values are permitted by L041.

Use only L041's audited passage “Each occurrence's own prefix and
the transfer to the next.” Its identities and necessities hold at
every original occurrence; its global cycle estimates, minimum rotation,
seed and represented-length bound are unused.

Fix any k in {0,...,24}, put i=pi(k), and set
y_k=T^{4J_i}(n_k). The finite passage gives

\[
y_k+1=(27/16)^{J_i}s_k-12/11,
\qquad
z_k=(27/16)^{J_i}(3/2)^{H_i}s_k-(12/11)(3/2)^{H_i}-1,
\tag{3}
\]
\[
11n_k+23\ge2^{4J_i+2},\qquad
2^{H_i}\le y_k+1<(27/16)^{J_i}s_k.
\tag{4}
\]

These are necessities for an actual word with an odd endpoint and
arbitrary exact tail a_i>=2. In particular the imported valuation
argument uses H_i>=3 and imposes no upper bound on a_i. It does not
require all tails to equal2 or infer actuality from an affine equation.

The actual final a_i even steps give n_{k+1}=z_k/2^{a_i}. Define
the same indexed constants as C108a,

\[
G_i=(27/16)^{J_i}(3/2)^{H_i},\qquad
Q_i=(12/11)(3/2)^{H_i}+1.
\]

Substituting (3) and then adding kappa yields, for every occurrence,

\[
s_{k+1}=2^{-a_{\pi(k)}}(G_{\pi(k)}s_k-Q_{\pi(k)})+\kappa.
\tag{5}
\]

Both summands of Q_i remain inside the division by the actual tail;
kappa remains outside it. No endpoint or allocation is replaced by
a bound or a newly solved affine root.

All logarithms below have positive arguments by (2)–(4). Since
11n_k+23=11s_k, taking logarithms of the first inequality in (4)
and subtracting 2log2 gives

\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).
\tag{6}
\]

Taking logarithms in the second chain in (4) gives

\[
H_{\pi(k)}\log2\le\log(y_k+1)
 <\log s_k+J_{\pi(k)}\log(27/16).
\tag{7}
\]

Thus (6) is the required non-strict J guard and the strict consequence
of (7) is the required H guard. Even if 2^{H_i}=y_k+1, the strict
upper comparison persists because the subtracted 12/11 in (3) is
positive. Both guards concern the same outgoing row i=pi(k) at its
own input s_k; no bound at a neighboring junction is substituted.
This applies in particular to H_0=5 and H_24=32670656 wherever those
rows occur, with their unchanged indexed budgets attached.

The arbitrary k includes24. There (5) has output s_25=s_0, while
(6)–(7) are guards at input s_24, with row pi(24) and its actual
tail. If b_pi(24)=0 that tail equals2 and satisfies the same imported
necessities. All other zero budgets are also included. The proof has
not identified occurrences with equal values or required N to be a
primitive period; every one of the 25 outgoing equations remains.

Apply C108a, including its step529 audit, directly to the single
tuple (s_0,...,s_25). The indexed table and its two H replacements,
B, integer nonnegative b_i with sum B, tails a_i and permutation pi
are identical. Its lower domains and closure are (2); every exact
endpoint is (5); every own-input non-strict J guard is (6); every
own-input strict H guard follows from (7). These are all its premises
on this same tuple and allocation. C108a excludes such a real tuple
for every stated permutation and budget allocation, a contradiction.
Its audited proof already retains both internal cuts; this application
needs no further rotation and imposes no minimum or seed premise.

### Sources, comparison and qualifications

L041 supplies the established finite necessities, L055 supplies only
its complete pair table, and C108a supplies the audited real exclusion.
No witness, seed or special allocation from L055 is imported. The new
work is the explicit premise matching at the original chronological
cut, not a reproof of any finite-affine theorem or analytic certificate.
No numerical operand in the imported exclusions changes, so no
mathematical script or certificate replay is needed.

The inherited primary finite-affine reference is Halbeisen and
Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section2, equations(2)–(4), Lemma2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The prior assessment inspected the finite-word composition cases;
the postspell identities and arbitrary-tail necessities used here
are written out in L041 and its audit. No rational fixed-point
existence or integrality-to-actuality converse is used. The primary
source does not itself state this table-specific exclusion. The
upstream Sodelin live-main inspection has no immutable revision or
checked Lean build, as recorded in the prior assessment; no external
formal verification is imported.

C099b is a precedent at d34, with different H values, not an input.
C103b, C104b and C105a cover narrower literal d35 allocation domains.
The prior scope search found no identical completed transfer in the
checked files, which is not an originality claim. Attempts027,032–035
remain preserved: no failed sufficient package, prime-five diagnostic
or endpoint-only witness is reused as an actuality or exclusion premise.

Only this actual closed-word language is excluded. Nothing here shows
that an arbitrary positive integer enters it, that arbitrary cycles
have its table, residue conditions or budgets, or that divergent
orbits cannot occur. Fractional budgets and changed tables are outside
the conclusion. No complete candidate or universal descent claim follows.

### Separate critical applicability audit — 2026-10-28, step533

This RESEARCH/REPRODUCTION audit uses the invocation-start SPECIALIZE
assessment
`drafts/literature/2026-10-28-c108b-all-order-actual-word-critical-audit.md`.
The complete C108b and C108a, including C108a's step529 audit, were
compared with L041's hypotheses, occurrencewise finite passage and
corresponding audit, and L055's complete pair table only. The ready
primary-source assessment is reused. This checks the application of
audited inputs, rather than independently recertifying their numerical
exclusions or reproving the general finite-affine source theorem.

**All L041 hypotheses on the original chronology.** The table has
integer J_i>=8. Its unchanged H_i for 1<=i<=23 are integers at
least72, while the replacements H_0=5 and H_24=32670656 also exceed
or equal3. Nonnegative integer b_i give integer a_i>=2 congruent to2
modulo18, without an upper-tail restriction. Set r=25 and use L041's
occurrence parameters (J_pi(k),H_pi(k),a_pi(k)). The defining lengths
are D_pi(k), their cumulative sums are exactly u_k, and their total
is N. Therefore the assumed actual concatenation, return at the positive
odd start n_0>1, residue20-mod27 positive odd junctions and exact tails
are precisely L041's assumptions. Closure supplies its final junction.
No hypothesis concerning a minimum, seed, distinctness or primitive
period appears in L041. Its finite conclusions used here are independent
of its global cycle estimates and require none of their numerical bounds.

**One tuple with the required domains.** Write n_k=20+27q_k for
0<=k<25. If q_k<0 then n_k<=-7, contradicting positivity; hence
q_k>=0. Oddness of n_k makes q_k odd, so q_k>=1 and n_k>=47.
Thus the original s_k=n_k+23/11 satisfies s_k>=540/11. Closure gives
n_25=n_0 and s_25=s_0, also with that lower domain. This argument
does not choose a minimizing junction or solve a new endpoint root.

**Every exact endpoint.** For an arbitrary occurrence k, let i=pi(k)
and y_k=T^(4J_i)(n_k). L041's finite passage supplies

\[
y_k+1=(27/16)^{J_i}s_k-12/11,\qquad
z_k=G_i s_k-(12/11)(3/2)^{H_i}-1.
\]

The actual a_i even steps, with the specified exact tail, end at
n_(k+1)=z_k/2^{a_i}. Adding 23/11 gives exactly C108a's endpoint
at occurrence k. In particular Q_i=(12/11)(3/2)^{H_i}+1 has both
summands inside the division, and kappa=23/11 is outside it. This
uses the same indexed a_i, with neither a comparison tail nor an
independently chosen root.

**Both own-input guards and their signs.** The audited L041 passage
applies to arbitrary exact tails at least2. Its valuation argument
uses H_i>=3 and the odd endpoint to give

\[
11n_k+23\ge2^{4J_i+2},\qquad
2^{H_i}\le y_k+1<(27/16)^{J_i}s_k.
\]

All quantities whose logarithms are taken are positive. Substituting
11n_k+23=11s_k in the first inequality and subtracting 2log2 yields
4J_i log2<=log s_k+log(11/4), with the required non-strict sign.
The second chain yields
H_i log2<=log(y_k+1)<log s_k+J_i log(27/16), and hence C108a's
strict H guard. The strict upper step follows from subtracting the
positive 12/11 in the exact identity; it survives equality in the
lower step. Neither guard is inferred from the other. Both are at
input s_k of row i, including either replaced H value wherever that
row occurs.

**Closing edge, budgets and direct application.** The occurrence k
was arbitrary in 0,...,24, so the endpoint at k=24 has output
s_25=s_0 and both guards at s_24. If b_pi(24)=0 its actual tail is2,
which meets exactly the same L041 hypotheses. Every other zero budget
is likewise included. The permutation acts on intact indexed rows:
the unchanged b_i remain integers at least0 with sum9250245, and
each a_i remains 2+18b_i. Occurrences are never identified by value;
repeated periods and coincident junctions therefore lose no equation
or guard. The tuple has all25 endpoints, closure, all lower domains
and both own-input guards, with exactly C108a's table, constants,
simplex and arbitrary permutation. These exhaust its hypotheses.
Apply audited C108a directly. Its internal reindexing and both cuts
are part of that theorem; no new rotation or minimum assumption is
needed in this application. Its exclusion gives the contradiction.

**Verdict and limitations.** No defect, repair, narrowing or dependency
change is required. C108b is valid as stated relative to the audited
inputs. L041 supplies the finite necessities, L055 only the table,
and C108a the exclusion, as in the existing DAG row; none assumes
C108b. This validates the existing restricted input and does not
strengthen its conclusion or establish progress beyond the checked
source machinery. No changed numerical operand or arithmetic defect
justifies certificate replay. Attempts027,032–035 supply no premise
and remain preserved. Actuality is assumed, never inferred from a
real solution. Entry, other tables, unrestricted cycles, divergence
and universal descent remain open; no complete candidate is asserted.
The argument and dependencies are unchanged, so PROOF.md and DAG.md
are not edited by this audit. This canonical verdict supersedes the
overview's pending-C108b-audit wording. Exact Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage for this exclusion is unchecked, not known
absent. Supporting finite-word identities, dyadic valuations and
logarithm monotonicity are also unchecked for exact Mathlib declarations
here. No Lean verification is claimed.
