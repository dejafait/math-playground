# C084a — H-transfer actual-word exclusions for three tables

## Hypotheses

Fix d in {2,3,4}. Take the complete 25 indexed pairs (J_i,H_i)
displayed in L055, replacing only H_0 by 40-d and H_24 by
32670621+d. Fix integers b_i>=0 with sum_i b_i=B=9250245 and
attach a_i=2+18b_i to outgoing indexed row i. Let pi be any
permutation of {0,...,24}.

Use the shortcut map T(n)=n/2 for even positive integers and
T(n)=(3n+1)/2 for odd positive integers; O and E specify actual
input parities. Suppose that the chronological words

\[
W_{\pi(k)}=(OOEO)^{J_{\pi(k)}}O^{H_{\pi(k)}}E^{a_{\pi(k)}}
\quad(0\le k<25)
\]

form an actual closed concatenation at a positive integer. Require
every junction to be positive, odd and 20 modulo 27, and each final
even tail to be exact. Pairs and allocations remain attached to their
own outgoing rows. Repeated periods and coincident junctions are allowed.
There is no minimum, seed, least-root, first-return or primitive-period
premise.

## Conclusion

No such actual closed concatenation exists, for any of these three
tables, in any cyclic order over the full integer allocation simplex.

This is a local RESEARCH/REPRODUCTION application under
`drafts/literature/2026-10-19-h-transfer-actual-word-specialization.md`.
It transfers audited real-subsystem exclusions to actual words; it
claims no new general theorem beyond the inspected machinery. The separate
critical audit below found no defect in this application. The d=1 exclusion
is already C080b and is not counted here. Both original-table rational
witnesses remain valid. Other tables, universal entry, unrestricted
cycles, divergence and universal eventual descent remain unresolved.

## Proof

Assume such a concatenation exists. Write

\[
D_i=4J_i+H_i+a_i,\qquad
t_0=0,\quad t_{k+1}=t_k+D_{\pi(k)},\qquad
n_k=T^{t_k}(n_0),\quad s_k=n_k+23/11.
\]

Closure gives n_25=n_0 and s_25=s_0. Chronological indices k
refer to time occurrences, not necessarily distinct values. Every
positive odd integer 20 modulo 27 is at least 47: writing it as
20+27q, positivity gives q>=0 and oddness forces q odd, hence q>=1.
Thus every s_k>=47+23/11=540/11, including at closure.

The explicit L055 pairs have J_i>=8. The two replacements give
H_0 in {38,37,36} and H_24 in {32670623,32670624,32670625};
every other H_i is unchanged and at least 72. In particular all
J_i>=2 and H_i>=3, while a_i>=2 is 2 modulo 18. After listing
these pairs in chronological order, all hypotheses needed for L041's
elementary occurrencewise necessity hold. We use only that passage,
not its seed, cycle-mass bounds or imported primitive-cycle estimates.

Fix k with 0<=k<25, and abbreviate i=pi(k), J=J_i, H=H_i,
a=a_i, y=T^(t_k+4J)(n_0), z=T^(t_k+4J+H)(n_0). L041's
passage headed “Each occurrence's own prefix and the transfer to the
next” supplies the already established identities and necessities

\[
y+1=(27/16)^J s_k-12/11,\qquad
z=(27/16)^J(3/2)^H s_k-(12/11)(3/2)^H-1,
\]
\[
n_{k+1}=z/2^a,\qquad
11n_k+23\ge2^{4J+2},\qquad
2^H\le y+1<(27/16)^J s_k.
\tag{1}
\]

These are arbitrary-tail, own-input necessities for actual words,
not a converse asserting integer realization from real endpoints.
Set kappa=23/11, G_i=(27/16)^{J_i}(3/2)^{H_i} and
Q_i=(12/11)(3/2)^{H_i}+1, exactly as in L084's retained C077a
subsystem. Adding kappa to the endpoint in (1) gives

\[
s_{k+1}=2^{-a_i}(G_i s_k-Q_i)+\kappa.
\tag{2}
\]

Since 11n_k+23=11s_k, taking logarithms of the first necessity
in (1) yields precisely

\[
4J_i\log2\le\log s_k+\log(11/4).
\tag{3}
\]

The final pair of inequalities in (1), with positive arguments,
gives precisely the additional strict H guard

\[
0<\log s_k+J_i\log(27/16)-H_i\log2.
\tag{4}
\]

The strict sign follows from the strict upper bound for y+1 in
(1); the lower bound 2^H<=y+1 need not be strict. All quantities
in (2)–(4) use this same outgoing indexed row i and its actual input
n_k. No parameter or guard has been moved independently of its row.

In particular k=24 is included: its actual tail ends at n_25=n_0,
so (2) is the closing equation and (3)–(4) apply at its own input
n_24. The proof uses only a>=2, and therefore also covers a=2
wherever that tail occurs. There is no missing boundary equation.

We have obtained exactly L084's endpoint/domain/non-strict J/strict H
real subsystem for the same changed indexed table, the same integer
allocation of total B, and the same arbitrary permutation. Invoke
L084's audited infeasibility conclusion for this d directly. Its
independent sufficient-test certificates are established in L084;
they are not inferred here from actuality or from unchanged totals.
Its conclusion contradicts (2)–(4) and the lower domain just proved.

No additional normalization is required in this application: L084
already covers all chronological orders and its audited internal
normalization transports each outgoing row, tail, input and strict H
guard together across both cuts. We assume neither a minimum at an
indexed row nor a seed after rotation. Coincident junctions and repeated
periods do not affect the occurrencewise argument.

L055 is used only for its explicit indexed pairs, not its d=0
witness guards or feasibility. C080b is a duplicate-scope comparison
for d=1, not an input to this proof. Attempts 026–032 retain their
scopes; in particular L084's failed sufficient tests for d>=5 give no
feasibility verdict and are not tuned or reopened here.

The upstream finite-word affine input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The ready assessment reuses its inspected hypotheses and essential
printed proof cases. L084 already verifies the nonzero-denominator
qualification for its cyclic-root use; the words here are finite and
nonempty. L041 already establishes the actual-word necessities used
in (1). Neither general affine machinery nor the sufficient-test
certificates need reproof or new calculation in this application.

### Separate critical audit — 2026-10-19, step 341

This RESEARCH/REPRODUCTION proof audit uses the pre-invocation
SPECIALIZE assessment
`drafts/literature/2026-10-19-h-transfer-actual-word-critical-audit.md`.
It checks this actual-word application, importing L084's already audited
finite exclusions rather than rerunning their certificates. No defect,
changed hypothesis, new exclusion or mathematical repair was found.

**Table and chronological hypotheses.** The complete L055 table has
25 rows, J_0=8 and every J_i>=8. Rows 1 through 23 have H_i>=72;
the replacements at rows 0 and 24 are precisely the values displayed
above for d=2,3,4. Thus J>=2,H>=3 hold at every occurrence.
Nonnegative integer b_i give a_i>=2 with a_i congruent to 2 modulo
18, and their total and row attachments are exactly L084's. The
positive word lengths make the times t_0,...,t_25 strictly increasing.
Each interval [t_k,t_(k+1)) has the specified actual word. Each
positive odd residue-20 input is at least 47, so the alleged starting
input also meets L041's n_0>1 hypothesis. There are r=25>=3 words,
closure and exact tails, as required by that lemma. Its occurrencewise
passage and its audit explicitly apply independently of any ordering
of junction heights; the earlier choice of a seed minimum is unused.

**Both guards and both offsets.** At a fixed occurrence, L041's
already established identity is
2^H(2^a n_(k+1)+1)=3^H(y+1). The factor 2^a n_(k+1)+1 is odd,
and hence that necessity passage gives v_2(y+1)=H. With its positive
odd u=(y+1)/2^H, H>=3 makes
11y+23=4(11*2^(H-2)u+3) have valuation exactly 2. Its affine
prefix identity then gives v_2(11n_k+23)=4J+2. These are the
precise necessities used in (1), without invoking a two-word closure
converse or an E^2-only statement. Positivity permits logarithms;
11n_k+23=11s_k turns the non-strict lower power bound into (3).
For H, the exact identity y+1=(27/16)^J s_k-12/11 gives the
strict upper inequality even if 2^H=y+1. Thus (4) has the required
strict sign. The endpoint retains both negative terms in
Q_i=(12/11)(3/2)^H_i+1 inside 2^(-a_i), and adds kappa only
after that division, exactly as in (2). All three formulas use
i=pi(k) and the same s_k; no permutation of parameters alone occurs.
This is verification of L041's existing necessities, not a new
affine or valuation theorem.

**Closure and the invoked exclusion.** The same check applies at
k=24, where y and z are intermediate states of the last actual word
and its tail ends at n_25=n_0. Thus its endpoint is precisely the
closing equation, and its guards concern n_24. Taking a=2 anywhere
does not change the odd-factor or endpoint argument. Repeated periods
or equal junction values retain all 25 time occurrences; no distinctness
or primitive representation is needed.

L084's conclusion excludes every real tuple satisfying these lower
domains, endpoints, non-strict J guards and strict H guards, for the
same three tables, every permutation and the full integer simplex.
The checked application supplies all those premises. L084's audited
O/S/C/H prerequisite conjunction is an established input; actuality
and invariant counts are not substituted for it. In its internal
normalization the outgoing row, allocation, input and H guard move
together, preserving both cuts. C084a invokes that all-order theorem
directly and makes no extra choice of cut or minimum. The contradiction
is therefore to L084's stated real subsystem, without a seed,
survivor-feasibility premise, primitive-count bound, integrality of s,
or realization converse.

The primary affine citation and its nonzero-denominator qualification
above remain the reused source coverage; no fresh primary retrieval
or source reproof is claimed. L055 supplies the pairs, L041 the
occurrencewise necessities and L084 the contradiction, exactly the
existing direct DAG inputs. L055/L065's original-table witnesses and
Attempts 026–032 remain valid. The d=1 duplicate and d>=5 failed
sufficient tests are outside this conclusion. No C077a definition
mismatch arose requiring another input. This completed audit supersedes
the overview's pending C084a audit wording; the mathematical argument
and DAG are unchanged. Universal entry, other pair tables, unrestricted
cycles, divergence and universal eventual descent remain unresolved.

## Mathlib

Full matching coverage for this three-table actual-word exclusion has
not been checked. Supporting affine and logarithm results are not a
matching theorem; unknown coverage is not absence. No Lean verification
is claimed.
