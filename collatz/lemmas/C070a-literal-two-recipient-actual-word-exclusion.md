# C070a — Literal two-recipient actual-word exclusion

## Hypotheses

Let T(n)=n/2 at even positive integers and T(n)=(3n+1)/2 at odd
positive integers. O and E specify these branches at actual odd and
even inputs. Use exactly L055's complete indexed pairs J_i,H_i in
literal order i=0,...,24. For an integer 1<=t<=9250244 set

\[
a_{22}=20,\qquad a_{23}=2+18t,\qquad
a_{24}=166504394-18t,\qquad a_i=2\ (0\le i<22).
\]

Put W_i=(OOEO)^{J_i}O^{H_i}E^{a_i} and D_i=4J_i+H_i+a_i.
Suppose W_0...W_24 is actual at a positive integer n_0. Define
n_i=T^(sum_(j<i) D_j)(n_0), for 0<=i<=25, and assume n_25=n_0.
Every designated junction n_i, 0<=i<25, is positive, odd and
20 modulo 27. Each final even tail is exact. Repeated periods and
coincident junctions are allowed. No minimum, least-root, first-return,
primitive-period, H-guard, seed or count-ray premise is imposed.
All logarithms are natural.

## Conclusion

No such actual closed concatenation exists for any integer in the
stated closed interval.

This is a local RESEARCH/REPRODUCTION application under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-15-two-recipient-actual-word-application.md`.
It assembles existing wordwise necessity and audited L070, without
claiming a new general theorem beyond the inspected sources. C068b
and C069a retain row 22 at tail 2 and do not supply this changed-support
conclusion. The separate critical audit below found no defect within
this exact actual-word scope.
Other allocations/orders, entry, unrestricted cycles, divergence and
universal eventual descent remain unresolved. Both existing rational
witnesses retain their original scopes.

## Proof

Suppose such a concatenation exists. Inspection of L055's entire table
gives J_i>=8>=2 and H_i>=40>=3 for every row. Only its indexed pairs
are imported, not its tails or rational-witness assumptions. Since
166504394=2+18*9250244, the last tail is exactly

\[
a_{24}=2+18(9250244-t).
\tag{1}
\]

For every admitted integer t, all tails are integers at least 2 and
congruent to 2 modulo 18. At t=1 the last three tails are
(20,20,166504376); at t=9250244 they are (20,166504394,2).
Thus the full closed interval satisfies the arbitrary-tail language
conditions, including its final-tail-2 endpoint.

Write n_i=20+27q_i. Positivity gives integer q_i>=0, since q_i<=-1
would give n_i<=-7. Oddness forces q_i odd, hence q_i>=1 and n_i>=47.
Define s_i=n_i+23/11 for 0<=i<=25. Then

\[
s_i\ge540/11\quad(0\le i\le24),\qquad s_{25}=s_0.
\tag{2}
\]

In particular n_0>1. All of L041's actual-language hypotheses now
hold with r=25 and the literal chronological parameters above. Use
only its elementary wordwise necessity in the section “Each occurrence's
own prefix and the transfer to the next”; its seed, length bounds and
primitive-cycle estimates are unnecessary.

Fix any 0<=i<=24 and abbreviate J=J_i, H=H_i, a=a_i,
n=n_i and m=n_(i+1). The endpoint m is positive odd, including
m=n_0 when i=24. Let y=T^(4J)(n) and z=T^(4J+H)(n).
L041's existing actual-word identities give

\[
y+1=(27/16)^J s_i-12/11,\qquad
2^H(z+1)=3^H(y+1),\qquad z=2^a m.
\tag{3}
\]

Its arbitrary-tail necessity gives v_2(11n+23)=4J+2: the required
J>=2, H>=3, a>=2 and actual positive odd endpoint have all been
checked for this occurrence. This invokes the wordwise result already
justified in L041 by L031's arbitrary-tail passage; neither two-word
closure sufficiency nor E^2-only transport is used. Since 11n+23 is
a positive integer with that valuation,

\[
2^{4J+2}\le11n+23=11s_i,
\qquad
4J_i\log2\le\log s_i+\log(11/4).
\tag{4}
\]

This is exactly the non-strict J guard at the outgoing row's own
input. No incoming row or minimum is substituted for that input.

From (3), z=(3/2)^H(y+1)-1. Substitute its first identity, divide
by the actual 2^a and add 23/11. This gives exactly

\[
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
 -(12/11)(3/2)^{H_i}-1\right)+23/11.
\tag{5}
\]

The fixed tail at row 22 and both varying tails remain attached to
their literal outgoing rows. For i=24 the actual tail ends at
n_25=n_0, so (5) includes the closing equation with output s_0.

Now t, the complete literal table and every tail agree exactly with
L070. Equation (2) supplies its real lower domain and closure;
(4) supplies every own-input non-strict J guard; (5) supplies all
25 exact shifted endpoints. These exhaust L070's hypotheses.
Audited L070 says that this necessary real subsystem is infeasible
throughout the stated integer interval: its unique cyclic tuple
violates the row-24 J guard. The actual junctions would satisfy that
subsystem, a contradiction.

The underlying primary finite affine input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The prior assessment records inspection of its chronological convention,
hypotheses and essential induction cases. Existing local necessity and
audited L070 are reused; the displayed substitutions justify this
application's coordinate matching, without reproving general coding.
Actuality is assumed, so rational-parity sufficiency and an integer
closure converse are unnecessary.

All equations and guards concern time occurrences. Repeated periods
and coincident junctions therefore remove no premise. No shifted
integrality test, H guard, seed, minimum, primitive/count-ray theorem
or published computational cycle cutoff is invoked. Attempts 026/031
and both rational witnesses remain valid. The conclusion excludes only
this literal allocation family; it does not establish universal entry,
exclude other cycles or divergent orbits, or prove eventual descent.

### Separate critical audit — 2026-10-15, step 237

The independent premise audit found no defect. It reuses L070's
finished arithmetic audit rather than repeating its certificate: the
question here is whether an actual concatenation as stated supplies
every hypothesis of that real-system exclusion. The prior SPECIALIZE
assessment is
`drafts/literature/2026-10-15-two-recipient-actual-word-critical-audit.md`.

All 25 pairs in L055's table satisfy J_i>=8 and H_i>=40. None of
L055's original tails, rational junctions, minimum or count conditions
is imported. The equality 166504394=2+18*9250244 shows that every
tail in the entire closed integer interval is at least 2 and congruent
to 2 modulo 18. Both extreme triples in the proof are correct. In
particular the last tail may equal 2; no argument requires it to be
large. Each stated actual word therefore has the language hypotheses
of L041 at r=25. The positive odd residue-20 condition implies n_i>=47
by the parity of q_i in n_i=20+27q_i. Consequently n_0>1 and
s_i>=47+23/11=540/11, with s_25=s_0 from actual closure.

For each outgoing row, actual O^H followed by the actual E^a tail
gives 2^H(z+1)=3^H(y+1) and z=2^a n_(i+1). Since a>=2,
z+1 is odd. The already proved arbitrary-tail necessity in L041
and L031 thus applies at this same input, including row 24 with
n_(25)=n_0. Its exact valuation is v_2(11n_i+23)=4J_i+2:
the proof uses v_2(y+1)=H and H>=3, not a tail-2 transport rule.
Positivity permits the integer lower bound
2^(4J_i+2)<=11n_i+23=11s_i. Taking natural logarithms and
subtracting 2 log2 gives exactly the non-strict guard (4), with
constant log(11/4) and the outgoing row's own input. No incoming
guard, minimum selection or H guard replaces it.

The first equation of (3) gives
y+1=(27/16)^J_i s_i-12/11. Inserting this in
z=(3/2)^H_i(y+1)-1, then using n_(i+1)=z/2^a_i and
s_(i+1)=n_(i+1)+23/11, gives (5) with both offsets and the
actual a_i. This is literally L070 (1). At i=24 it supplies the
closing equation with output s_0, not an equation at a new free
junction. The fixed row-22 tail 20 and both varying tails stay
attached to their stated outgoing rows throughout. No change of
order or cut is performed.

L070 requires precisely the same integer parameter, literal indexed
pairs and tails, these 25 exact endpoints and closure, the lower
domain and all own-input non-strict J guards. Those premises are
now all supplied. Its audited strict row-24 guard failure contradicts
(4), so the conclusion follows on the full interval. No new numerical
comparison or additional hypothesis is needed. The direct mathematical
uses remain L041's elementary necessity, L055's table and L070's
infeasibility; L031 is the upstream justification already in L041.
DAG.md therefore needs no change.

Actuality is a hypothesis throughout; no affine-closure converse or
integer/parity realization is inferred. Integrality of s_i is neither
asserted nor required. Occurrences remain indexed in time, so repeated
periods and coincident junctions do not affect any equation or guard.
Neither a primitive-count threshold nor a computational cycle cutoff
enters this audit. C068b/C069a keep row 22 at tail 2 and do not
duplicate this changed-support result. Attempts 026/031 and both
rational witnesses keep their recorded scopes. This verifies an
existing local application, not a stronger exclusion or progress beyond
the inspected finite-word inputs. Other allocations/orders, entry,
unrestricted cycles, divergence and universal eventual descent remain
unresolved.

## Mathlib

Full matching coverage for this actual-word exclusion is **not checked**.
Supporting ingredients are finite affine composition, positive integer
valuation bounds and logarithm monotonicity. No Lean theorem or build
is claimed; unknown coverage is not evidence of absence.
