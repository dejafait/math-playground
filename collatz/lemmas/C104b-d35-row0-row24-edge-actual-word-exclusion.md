# C104b — d35 row0/row24 allocation-edge actual-word exclusion

## Hypotheses

Let T(n)=n/2 for even positive integers and T(n)=(3n+1)/2 for
odd positive integers. Letters O and E specify actual input parities
for T. Use the 25 indexed pairs (J_i,H_i) in the literal order of
L055's table, changing only H_0=40 to 5 and H_24=32670621 to
32670656. No other assertion of L055 is assumed.

Let B=9250245 and m be an integer with 1<=m<=B. Set

\[
b_0=m,\qquad b_{24}=B-m,\qquad b_1=\cdots=b_{23}=0,
\qquad a_i=2+18b_i,
\]
\[
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},\qquad
D_i=4J_i+H_i+a_i,\qquad q_i=\sum_{j<i}D_j,\qquad N=q_{25}.
\]

Suppose W_0...W_24 is actual at a positive odd integer n_0>1
and T^N(n_0)=n_0. Define n_i=T^{q_i}(n_0), 0<=i<=25.
Require every junction n_i, 0<=i<25, to be positive odd and
congruent to 20 modulo 27, and every final even tail to be exact.
Thus n_25=n_0. Repeated periods and coincident junctions are allowed.
No minimum, seed, first-return, primitive-period or relative-height
assumption is imposed. All logarithms below are natural.

## Conclusion

No such closed actual concatenation exists, for every integer m in
the full interval 1<=m<=9250245, including the closing-tail2 case m=B.

This is local RESEARCH/REPRODUCTION under the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-25-c104a-edge-actual-word-transfer.md`.
It applies existing occurrencewise necessities to an audited restricted
real-system exclusion; it claims no discovery beyond the sources
checked. A separate critical audit on 2026-10-25 retained the transfer
without repair, as recorded below.
It is a partial result, not a complete Collatz candidate.

## Proof

Suppose such a concatenation exists. Keep its original chronological
cut and the given m fixed. The full table has J_i>=8, and after the
two H replacements all H_i>=5 (the H_i for i>0 are at least 72).
In particular J_i>=2 and H_i>=3 at every row. The integer interval
for m makes every b_i nonnegative; hence each a_i is an integer at
least 2 and congruent to 2 modulo 18. These are precisely L041's
local parameter conditions with r=25.

Every D_i is positive. The intervals [q_i,q_{i+1}) partition the
given word, so W_i is actual at n_i with output n_{i+1}. This also
holds for i=24, whose output is n_25=n_0, positive odd. Use only
the occurrencewise necessities in L041's proof, section "Each
occurrence's own prefix and the transfer to the next", and its
corresponding audit. Those statements concern each actual word and
its own output independently of the size ordering of junctions or
the location of positive budgets. They require no upper-tail bound.
L041's separate minimizing relabeling, seed, represented-length bound
and global cycle estimates are not used.

Put kappa=23/11 and s_i=n_i+kappa for 0<=i<=25. Write a positive
odd junction as n_i=20+27k. Positivity forces the integer k>=0,
and oddness makes k odd, so k>=1. Consequently

\[
s_i\ge47+23/11=540/11>0\quad(0\le i<25),
\qquad s_{25}=s_0.
\tag{1}
\]

For each row put y_i=T^{4J_i}(n_i) and
z_i=T^{4J_i+H_i}(n_i). L041's exact occurrencewise identities give

\[
y_i+1=(27/16)^{J_i}s_i-12/11,
\qquad
z_i=(27/16)^{J_i}(3/2)^{H_i}s_i
       -(12/11)(3/2)^{H_i}-1,
\qquad n_{i+1}=z_i/2^{a_i}.
\tag{2}
\]

With G_i=(27/16)^{J_i}(3/2)^{H_i} and
Q_i=(12/11)(3/2)^{H_i}+1, adding kappa yields exactly

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa
\quad(0\le i<25).
\tag{3}
\]

Both negative terms remain inside this row's tail division, and the
shift remains outside it. This is an identity at every chronological
endpoint, including row24-to-row0; no tail is replaced by a total.

The same L041 passage supplies the occurrencewise necessities

\[
4J_i\log2\le\log s_i+\log(11/4),\qquad
2^{H_i}\le y_i+1<(27/16)^{J_i}s_i.
\tag{4}
\]

Its arbitrary-tail proof uses
2^{H_i}(2^{a_i}n_{i+1}+1)=3^{H_i}(y_i+1), with a_i>=2,
H_i>=3 and odd output. It therefore applies to each assigned tail
here, including tail2; it is not an E^2-only transport assertion.
All quantities in the second chain of (4) are positive. Strict
monotonicity of the logarithm and its product rule give

\[
H_i\log2<\log s_i+J_i\log(27/16).
\tag{5}
\]

The strict upper comparison in (4) comes from subtracting the
positive 12/11 in (2). It gives (5) even if 2^{H_i}=y_i+1.
The J guard in (4) stays non-strict. Both guards concern row i's
own input s_i and its own indexed pair.

Apply audited C104a to this single tuple (s_0,...,s_25). Its full
indexed table with the two H replacements is identical to ours.
Its parameter is this same integer m in [1,B], with b_0=m,
b_24=B-m, all other budgets zero and exactly a_i=2+18b_i.
Equation (1) supplies its lower domain and closure; (3) supplies all
25 of its endpoint equations. The first guard in (4) and (5) supply
its non-strict J and strict H guards at their required inputs.
No rotation, new coordinate choice, minimum or seed is involved.
C104a excludes any such real tuple, giving a contradiction.

For clarity, the argument is uniform over the full integer interval.
At m=1 the two changed tails are a_0=20 and a_24=166504394.
At m=B they are a_0=166504412 and a_24=2; the last occurrence
still ends at the odd integer n_0 and still has its equation (3)
and both guards. At every parameter the other 23 tails equal 2;
their occurrences and guards are retained as well. There is no
upper-tail premise in the imported necessity or C104a. Repeated
periods and coincident junction values leave the chronological
intervals as distinct occurrences. Neither input requires least
return or distinct junction values, so neither case escapes the
contradiction.

### Sources, overlap and qualifications

The direct mathematical inputs are L041's occurrencewise necessities,
L055's literal table only and audited C104a. The specialization above
matches their hypotheses rather than reproving a general affine or
parity-coding theorem. The precise upstream finite-affine reference,
inspected in the reused assessment, is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only finite actual-word identities are used through L041; actuality
is assumed, with no integrality-to-actuality converse or new fixed-point
argument. C104a's audited analytic input and its qualifications remain
imports. No certificate replay or external formal verification is
claimed for this substitution proof.

The prior assessment and scoped duplicate search found C101b and
C103b in the different b_0=0 domain; neither is an exclusion input
for this positive-row0 edge. Attempt032's failed sufficient support
package supplies no premise here and remains preserved, as do both
d0 witnesses and unfinished work. No claim establishes this table,
allocation support, residue language or entry/order reduction for
arbitrary cycles. Other positive-row0 supports, arbitrary ordering,
entry, unrestricted cycles, divergence and universal descent remain
unresolved.

### Independent critical audit — 2026-10-25

This separate RESEARCH/REPRODUCTION audit uses the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-25-c104b-actual-word-transfer-critical-audit.md`.
It checks the transfer against L041's occurrencewise proof and audit,
the complete literal L055 table, and audited C104a. No defect was
found and no statement, mathematical input or dependency edge changes.
This verifies the previously unaudited local application; it establishes
no result beyond the assessed sources or a complete Collatz candidate.

The table has 25 rows, with minimum J=8. After exactly H0=5 and
H24=32670656 replace their old values, the minimum H is 5 and
every other H is at least 72. Thus the occurrencewise conditions
J>=2,H>=3 hold. For integer 1<=m<=B, the budgets are nonnegative
integers, and all tails are integers at least 2 and equal to 2 modulo
18. The definitions of q_i and D_i give 25 consecutive, nonempty
actual words. Each output is its next indexed positive odd junction;
row24's output is n25=n0. These are precisely the local actual-word
hypotheses of L041; its later minimizing relabeling is unnecessary.

At each occurrence, L041 gives
2^H(2^a n_next+1)=3^H(y+1). The factor 2^a n_next+1 is odd, so
v2(y+1)=H. Positivity gives y+1=2^H u with u a positive odd
integer. Since H>=3, the integer 11*2^(H-2)*u+3 is odd; hence
v2(11y+23)=2. The imported finite-affine identity
16^J(11y+23)=27^J(11n+23) gives v2(11n+23)=4J+2.
In particular 11s=11n+23>=2^(4J+2). Dividing by 4 and taking
natural logarithms gives exactly the non-strict own-input J guard.
This checks the arbitrary-tail necessity, including a=2, rather than
an assertion specific to a two-step tail. No cycle estimate, converse
parity theorem or assumption of minimum height enters this check.

The other imported identity is y+1=(27/16)^J*s-12/11.
Thus 2^H<=y+1<(27/16)^J*s, proving the strict own-input H
guard even if its first inequality is an equality. The positive
subtraction 12/11 is essential to strictness. Every logarithm has
positive argument: an odd positive 20-mod-27 junction is at least
47, so its shift is at least 540/11. Closure gives s25=s0 with
the same shift. Finally the exact identity
z=(27/16)^J*(3/2)^H*s-(12/11)*(3/2)^H-1 and n_next=z/2^a
gives C104a's endpoint with both negative terms inside 2^(-a)
and the added 23/11 outside. This establishes all its equations
on the single original chronological tuple, including the closing one.

C104a requires exactly these lower domains, closure, endpoints and
guards, with the identical indexed data and integer parameter. It
imposes no seed, minimum, integrality or primitive-period condition.
Its internal cut1 proof does not require rotating this tuple. Its
audited conclusion therefore contradicts the tuple just verified;
its analytic bound and log enclosure are imported, not recertified.
At m=1 the two tails are 20 and 166504394; at m=B they are
166504412 and 2, since 18B=166504410. All other 23 tails equal
2 throughout. There is no upper-tail restriction, so both endpoints
and every intervening integer are covered. Repeated periods and
coincident junction values preserve the indexed time intervals and
all local identities, and neither imported input requires distinct
values or a least return. This completes the announced audit test.

The direct mathematical inputs remain L041, L055 (table only), and
C104a. The precise finite-affine source and its applicability are
recorded above; no new general theorem or external source is invoked.
Attempt032, both d0 witnesses and unfinished work remain unchanged.
The other supports and all global reduction gaps listed above remain
unresolved. No mathematical script or certificate replay was needed
for this implication audit.

## Mathlib

Full matching coverage for this restricted actual-word exclusion is
unchecked, not known absent. Supporting affine, valuation and logarithm
facts alone are not a matching theorem. This proof is informal; no
Lean verification or external checked build is claimed. The separate
informal critical audit of the transfer is recorded above.
