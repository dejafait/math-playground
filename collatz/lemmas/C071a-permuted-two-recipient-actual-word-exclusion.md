# C071a — All-order two-recipient actual-word exclusion

## Hypotheses

Let T(n)=n/2 at even positive integers and T(n)=(3n+1)/2 at odd
positive integers. O and E denote these branches at actual odd and even
inputs. Use exactly the 25 indexed pairs J_i,H_i in L055's complete
table. For an integer 1<=t<=9250244 attach

\[
a_i=2\ (0\le i<22),\qquad a_{22}=20,\qquad
 a_{23}=2+18t,\qquad a_{24}=166504394-18t.
\]

Let pi be any permutation of {0,...,24}, retaining every outgoing
triple (J_i,H_i,a_i) intact. Put W_i=(OOEO)^{J_i}O^{H_i}E^{a_i}
and D_i=4J_i+H_i+a_i. Suppose W_pi(0)...W_pi(24) is actual at
a positive integer n_0. Define chronological junctions

\[
n_k=T^{\sum_{q<k}D_{\pi(q)}}(n_0)\quad(0\le k\le25).
\]

Assume n_25=n_0 and that every n_k for 0<=k<25 is positive,
odd and 20 modulo 27. Every final even tail is exact. Repeated periods
and coincident junctions are allowed. No minimum, first-return,
least-root, primitive-period, H-guard, seed or count-ray premise is
imposed. All logarithms are natural.

## Conclusion

No such actual closed concatenation exists for any admitted integer t
and any cyclic order of the intact triples.

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-15-permuted-two-recipient-actual-word-application.md`.
It assembles existing elementary necessity and audited L071; it claims
no new general result beyond the inspected sources. C069a retains
row 22 at tail 2; C070a covers only literal order. Neither supplies
this exact all-order changed-support application. The separate critical
audit below found no defect within the stated scope. Other allocations, entry,
unrestricted cycles, divergence and universal eventual descent remain
unresolved; both existing rational witnesses retain their scopes.

## Proof

Suppose such a concatenation exists. Every pair in L055's full table
satisfies J_i>=8>=2 and H_i>=40>=3. Only its indexed pairs are used,
not its old tails or rational-witness assumptions. Since
166504394=2+18*9250244, the last indexed tail is

\[
a_{24}=2+18(9250244-t).
\tag{1}
\]

Throughout the full closed integer interval, every tail is an integer
at least 2 and congruent to 2 modulo 18. The tails on indexed rows
22,23,24 are (20,20,166504376) at t=1 and (20,166504394,2)
at t=9250244. These properties survive any intact permutation. In
particular the indexed row-24 tail may equal 2, wherever it occurs
chronologically; it need not be the chronological closing row.

Write each chronological junction as n_k=20+27q_k, q_k integral.
Positivity forces q_k>=0, since q_k<=-1 gives n_k<=-7. Oddness
forces q_k odd, hence q_k>=1 and n_k>=47. Set s_k=n_k+23/11
for 0<=k<=25. Actual closure supplies

\[
s_k\ge540/11\quad(0\le k<25),\qquad s_{25}=s_0.
\tag{2}
\]

In particular n_0>1. L041's actual-language hypotheses hold at r=25
with its chronological parameters assigned to
(J_pi(k),H_pi(k),a_pi(k)). Use only its elementary arbitrary-tail
necessity in “Each occurrence's own prefix and the transfer to the
next”; its seed, length estimates and primitive-cycle inputs are unused.

Fix any chronological occurrence 0<=k<=24. Abbreviate
J=J_pi(k), H=H_pi(k), a=a_pi(k), n=n_k, m=n_(k+1),
and put y=T^(4J)(n), z=T^(4J+H)(n). The existing wordwise
identities and necessity in L041 give

\[
y+1=(27/16)^J s_k-12/11,\qquad
2^H(z+1)=3^H(y+1),\qquad z=2^a m,
\tag{3}
\]

and v_2(11n+23)=4J+2. All the wordwise hypotheses, including
J>=2, H>=3, a>=2 and the actual positive odd endpoint m,
hold at this occurrence, also when k=24 and m=n_0. This is the
arbitrary-tail necessity already justified there by L031's “Exact
boundary valuations, without assuming E^2 transport”, not a tail-2
transport rule or a closure converse. Positivity of the integer 11n+23
therefore gives

\[
2^{4J+2}\le11n+23=11s_k,\qquad
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).
\tag{4}
\]

This is exactly the non-strict J guard at this outgoing row's own
input. No minimum or incoming row replaces that input.

The middle identity in (3) gives z=(3/2)^H(y+1)-1. Substitute
the first identity, divide by the actual 2^a, and add 23/11 to obtain

\[
s_{k+1}=2^{-a_{\pi(k)}}\left((27/16)^{J_{\pi(k)}}
(3/2)^{H_{\pi(k)}}s_k-(12/11)(3/2)^{H_{\pi(k)}}-1\right)+23/11.
\tag{5}
\]

Every indexed tail remains attached to its own J,H pair and outgoing
input. At k=24 the actual endpoint is n_25=n_0, so (5) includes
the closing equation with output s_0, for whichever row is pi(24).
No rotation or minimum selection is needed.

Now the integer t, complete indexed table, permutation and all attached
tails agree exactly with L071. Equation (2) supplies its real lower
domain and closure, (4) supplies all 25 own-input non-strict J guards,
and (5) supplies every exact shifted endpoint. These exhaust L071's
hypotheses. Audited L071 excludes such a real tuple over the full
closed integer interval, so the actual junctions yield a contradiction.

The underlying finite affine input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta Arith.
78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The prior assessment and reused primary-inspection records cover its
chronological convention and essential induction cases. Existing local
necessity is reused; the substitutions above check only this
application's coordinates and attached guards. No general coding theorem
is reproved. Actuality is assumed, so rational-parity sufficiency and
an affine-closure realization converse are unnecessary.

All statements are indexed by time occurrence. Repeated periods and
coincident junctions remove no equation or guard. No H guard, seed,
minimum-location premise, shifted-integrality test, primitive/count-ray
theorem or published computational cycle cutoff is invoked. Attempts
026/031 and both rational witnesses retain their scopes. The result
excludes only this fixed allocation family in every cyclic order; it
supplies neither universal entry nor unrestricted cycle or divergence
control, and is not a Collatz resolution.

### Separate critical audit — 2026-10-16, step 245

The independent premise audit under the prior SPECIALIZE assessment
`drafts/literature/2026-10-16-permuted-two-recipient-actual-word-critical-audit.md`
found no defect. This verifies the existing application; it adds no
stronger exclusion or result beyond the inspected source machinery.
L071's completed arithmetic audit is reused as approved, with no
discrepancy requiring its numerical comparisons to be repeated.

**Language and full interval.** Every one of L055's 25 indexed pairs
has J>=8 and H>=40. Only that table is used, not its original allocation
or real-witness premises. The identity 18*9250244=166504392 verifies
(1). For every admitted integer t, a_23>=20 and a_24>=2, with both
congruent to 2 modulo 18; the fixed tails 2 and 20 meet the same
conditions. The triples of changed tails at the two extremes are
exactly (20,20,166504376) and (20,166504394,2). Thus row 24 may have
tail 2 without leaving the arbitrary-tail domain. The permutation
carries the entire triple and changes none of these conclusions.
Each word has exactly 4J+H+a shortcut steps, agreeing with the
chronological junction definition.

For each positive odd n_k=20+27q_k, positivity gives q_k>=0 and
oddness makes q_k odd. Hence q_k>=1, n_k>=47 and
s_k>=47+23/11=540/11. In particular n_0>1. Actual closure gives
s_25=s_0 and also the lower domain at index 25. All logarithms have
positive arguments. L041's language hypotheses at r=25 hold with its
chronological row k assigned to the intact indexed row pi(k).
No minimum selection is needed for its elementary wordwise passage.

**Necessity at the outgoing input.** Fix any chronological k, including
k=24. In L041's existing identities, actual E^a gives z=2^a m,
where m=n_(k+1) is the stated positive odd endpoint. Thus z+1 is odd,
and 2^H(z+1)=3^H(y+1) gives v_2(y+1)=H. In the upstream L031
justification, y+1=2^H u with u positive odd and H>=3 imply
11y+23=4(11*2^(H-2)u+3) has valuation 2. Its affine identity
16^J(11y+23)=27^J(11n_k+23) therefore gives valuation 4J+2
at the same actual input n_k. These are precisely the already proved
arbitrary-tail necessity steps; they impose no E^2-only transport or
two-word closure converse.

Positivity and integrality of 11n_k+23 now give
2^(4J+2)<=11n_k+23=11s_k. Logarithm monotonicity, followed by
subtracting 2 log2, gives
4J_pi(k) log2<=log s_k+log(11/4). The sign is non-strict,
the constant is unchanged, and the input is that of the outgoing
row pi(k). No incoming-row guard or guard at a designated minimum
has been substituted.

**Exact endpoints and the closing edge.** Substituting the existing
identity y+1=(27/16)^J s_k-12/11 into
z=(3/2)^H(y+1)-1, then dividing by 2^a and adding 23/11,
gives exactly (5). The term -(12/11)(3/2)^H and the term -1
are both inside the division; the endpoint shift +23/11 is outside.
The attached a is a_pi(k), including its dependence on t. At the last
chronological occurrence the same actual tail ends at n_25=n_0,
so the equation has output s_0. It is immaterial whether pi(24)=24:
the indexed row-24 endpoint and the chronological closing endpoint
are treated with their own actual rows. No cyclic rotation or new cut
is introduced by this application.

Comparison with L071's full Hypotheses section now accounts for every
premise: the same indexed pairs, integer interval, intact permutation
and attached tails; real lower-domain junctions and closure; all 25
exact endpoints; and all 25 own-input non-strict J guards. L071 excludes
this real tuple. Actual integer junctions, after the prescribed shift,
would be such a tuple, giving exactly the claimed contradiction.
Neither shifted integrality nor an integer-cycle theorem on arbitrary
real junctions is used.

All identities are indexed by time occurrence. Ties or repeated periods
erase no endpoint or guard, and no step divides by a difference of
junctions. There is no H guard, seed, minimum-location, primitive/count-ray
or affine-closure sufficiency assumption. The precise finite-affine
citation already given above is reused with the inspected chronological
convention and induction cases; no general coding theorem is reproved.
C069a has different tail support and C070a only literal order, so neither
was a substitute for this audit. Attempts 026/031 and both rational
witnesses retain their scopes. The direct uses remain L041, L055 and
L071; L031 is upstream through L041. No hypothesis, conclusion or
direct mathematical dependency changes. Other allocations, entry,
unrestricted cycles, divergence and universal eventual descent remain
unresolved. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching theorem coverage is **not checked**. Supporting ingredients
are finite affine composition, dyadic valuation bounds and real logarithm
monotonicity. No exact Lean declarations or formal verification are
claimed; unknown availability is not evidence of absence.
