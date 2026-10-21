# C069a — Arbitrary-order last-pair actual-word exclusion

## Hypotheses

Let T(n)=n/2 at even positive integers and T(n)=(3n+1)/2 at odd
positive integers. O and E denote these branches at actual odd and even
inputs. Use exactly the 25 indexed pairs J_i,H_i in L055's complete
table. For an integer 2<=t<=9250245 attach

\[
a_i=2\ (0\le i<23),\qquad
a_{23}=2+18t,\qquad a_{24}=166504412-18t.
\]

Let pi be any permutation of {0,...,24}, keeping each outgoing triple
(J_i,H_i,a_i) intact. Put

\[
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},\qquad D_i=4J_i+H_i+a_i.
\]

Suppose W_pi(0)...W_pi(24) is actual at a positive integer n_0 and
define the chronological junctions

\[
n_k=T^{\sum_{q<k}D_{\pi(q)}}(n_0)\quad(0\le k\le25).
\]

Assume n_25=n_0, and every n_k for 0<=k<25 is positive, odd and
20 modulo 27. Each final even tail is exact. Repeated periods and
coincident junctions are allowed. No minimum, first-return, least-root,
primitive-period, H-guard, seed or count-ray assumption is imposed.
All logarithms are natural.

## Conclusion

No such actual closed concatenation exists, for any permitted integer t
and any cyclic order of these intact triples.

This is a local RESEARCH/REPRODUCTION application under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-14-permuted-last-pair-actual-word-application.md`.
It transfers audited L069's necessary-subsystem exclusion to actual
words; it claims no advance beyond the inspected general finite-word
machinery. C068b already covers literal order, whereas this result covers
every cyclic order for t>=2. The t=0,1 allocations are outside these
hypotheses and their rational witnesses remain valid. The separate critical
audit below found no defect in this actual-word application. Other allocations, entry, unrestricted cycles,
divergence and universal eventual descent remain unresolved.

## Proof

Suppose such a concatenation exists. Every indexed pair in L055's
complete table has J_i>=8>=2 and H_i>=40>=3; only that table is used,
not L055's original tails or witness. The identity
166504412=2+18*9250245 gives

\[
a_{24}=2+18(9250245-t).
\]

Thus both varying tails, and all other tails, are integers at least 2
and congruent to 2 modulo 18 throughout the stated closed interval.
In particular a_24=2 is allowed at its upper endpoint. Permuting intact
triples preserves these wordwise language conditions.

For each chronological junction write n_k=20+27q_k with q_k integral.
Positivity forces q_k>=0, since q_k<=-1 would give n_k<=-7.
Oddness of n_k forces q_k odd, hence q_k>=1 and n_k>=47.
Put s_k=n_k+23/11 for 0<=k<=25. Then

\[
s_k\ge540/11\quad(0\le k<25),\qquad s_{25}=s_0.
\tag{1}
\]

In particular n_0>1. After assigning L041's chronological parameters
to be (J_pi(k),H_pi(k),a_pi(k)), all its actual-language hypotheses
hold at r=25. We use only its elementary wordwise necessity, not its
seed, length bounds or primitive-cycle inputs.

Fix any 0<=k<=24 and abbreviate J=J_pi(k), H=H_pi(k),
a=a_pi(k), n=n_k and m=n_(k+1). Both n and m are positive odd
actual junctions, with m=n_0 when k=24. Let
y=T^(4J)(n) and z=T^(4J+H)(n). L041's passage “Each occurrence's
own prefix and the transfer to the next” supplies

\[
y+1=(27/16)^J s_k-12/11,\qquad
2^H(z+1)=3^H(y+1),\qquad z=2^a m.
\tag{2}
\]

Its arbitrary-tail necessity supplies v_2(11n+23)=4J+2. Its
wordwise hypotheses are J>=2, H>=3, a>=2 and the actual positive
odd endpoint m; all have just been checked at this position. As
justified in L041 using L031's arbitrary-tail passage, (2) gives
v_2(y+1)=H, then v_2(11y+23)=2, and the identity
16^J(11y+23)=27^J(11n+23) gives the stated input valuation.
This invokes the already proved necessity, without E^2-only transport
or a new coding/valuation theorem. Since 11n+23>0, it follows that

\[
2^{4J+2}\le11n+23=11s_k,
\quad\text{so}\quad
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).
\tag{3}
\]

This is precisely the non-strict J guard at that outgoing row's own
input; no incoming row, selected minimum or distinctness is used.

The second identity in (2) gives z=(3/2)^H(y+1)-1. Substitution
of its first identity, division by the actual 2^a, and addition of
23/11 give

\[
s_{k+1}=2^{-a_{\pi(k)}}\left((27/16)^{J_{\pi(k)}}
(3/2)^{H_{\pi(k)}}s_k-(12/11)(3/2)^{H_{\pi(k)}}-1\right)+23/11.
\tag{4}
\]

Every tail stays attached to its original indexed pair, wherever that
row occurs in pi. The calculation includes k=24 with m=n_25=n_0,
so (4) also verifies the closing endpoint. No rotation of the actual
tuple or choice of its minimum is needed for this application.

The integer t, full indexed table, permutation and intact tails are
exactly those of L069. Equation (1) gives its real lower domain and
closure, (3) gives all 25 own-input J guards, and (4) gives all 25
exact endpoints. These exhaust L069's hypotheses. Audited L069 says
no such real tuple exists, a contradiction.

The underlying finite affine input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta Arith.
78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The prior assessment records inspection of its chronological convention,
hypotheses and essential induction cases. Existing local wordwise
necessity and audited L069 are reused; actuality is a hypothesis, so
neither rational-parity sufficiency nor a realization converse is needed.
The displayed substitutions check this application's coordinate and
guard matching rather than reprove the general affine theorem.

Every check concerns a time occurrence. Repeated periods and coincident
junctions therefore retain all 25 equations and guards. No H guard,
seed, integrality test, primitive-count bound or published computational
cycle cutoff is invoked. Attempts 027–031 and both rational witnesses
retain their scopes. This exclusion of a restricted cycle language is
not a Collatz resolution.

### Independent critical audit — 2026-10-15

The audit used the prior SPECIALIZE assessment
`drafts/literature/2026-10-15-permuted-last-pair-actual-word-critical-audit.md`
and found no defect. This is verification of an existing local
reproduction, not a stronger exclusion or a new general result beyond
the inspected sources. L069's separately audited real-subsystem theorem
is an input; its upstream arithmetic certificate is not recomputed here.

**Full language and parameter interval.** Inspection of all 25 rows of
L055 confirms J_i>=8 and H_i>=40. Only these indexed pairs are imported:
neither its original tails nor its rational-witness assumptions enter.
The exact identity 18*9250245=166504410 checks the rewritten a_24.
At t=2 the two changed tails are 38 and 166504376; at t=9250245
they are 166504412 and 2. Their affine dependence gives a>=2 and
a=2 modulo 18 throughout the full integer interval. No constant-tail
or growing-row premise is needed. The actual-word length is exactly
4J+H+a because each O and E is one shortcut step.

The positive residue-20 integers are 20+27q with q>=0, and oddness
forces q odd. Thus every outgoing input is at least 47; the closing
input equals n_0 and has the same bound. The shift is exactly
47+23/11=540/11, so all logarithms in L069 have positive arguments.
The actual initial input exceeds 1. Relabeling L041's chronological
parameters by pi verifies all its language hypotheses at r=25.

**Arbitrary-tail necessity and guard sign.** The inspected elementary
passage in L041 applies to each actual occurrence separately, as
justified by L031's arbitrary-tail passage. In its identity
2^H(2^a m+1)=3^H(y+1), 2^a m+1 is odd; hence the exact
valuation of y+1 is H. With y+1=2^H u, u positive odd,
11y+23=4(11*2^(H-2)u+3) has valuation exactly 2 because H>=3.
The identity with 16^J and odd 27^J then yields valuation 4J+2
at 11n+23. These are the existing necessity steps, with no E^2
restriction or closure converse. The positive integer 11n+23 is
at least 2^(4J+2). Taking logarithms and subtracting 2 log2 gives
exactly the non-strict inequality (3), since 11n+23=11s_k.
The row is pi(k), and its input is s_k at every occurrence.

**Offsets, closing edge and contradiction.** L041's exact identities
give y+1=(27/16)^J s_k-12/11 and
z=(3/2)^H(y+1)-1. Dividing this z by the attached 2^a and then
adding 23/11 gives (4), retaining both the negative 12/11 term
inside the division and the positive 23/11 endpoint shift outside it.
For k=24 the actual tail ends at n_25=n_0, so this same equation
has output s_0. Every pi(k), J, H and tail remains attached to
that outgoing input; no permutation of the inputs alone is made.

Comparing against L069's complete Hypotheses section leaves no missing
premise: the table, integer interval and intact permutation agree;
(1) supplies its lower domain and closure; (3) supplies every own-input
J guard; and (4) supplies every endpoint. Its conclusion is impossibility
of this real subsystem, so actual integer inputs would contradict it.
Shifted integrality is neither true by assumption nor needed. There is
no appeal to an integer-cycle theorem on arbitrary real junctions.

All checks are indexed by time occurrence, including the last one.
Neither coincident junctions nor repeated periods remove an equation
or require division by a difference of junctions. No minimum, H guard,
seed, count ray, primitive-period condition, integrality diagnostic or
realization converse is used. The finite-affine source citation above
is reused with its inspected chronological convention; no general
coding theorem is reproved. Attempts 027–031 and the t=0,1 witnesses
retain their scopes. No premise, conclusion or direct mathematical
dependency changed, and all universal gaps remain unresolved.

## Mathlib

Full matching theorem coverage: **not checked**. Supporting affine
composition, dyadic valuations and real logarithm facts have not been
matched to exact declarations here. No matching theorem, absence from
Mathlib or formal verification is asserted.
