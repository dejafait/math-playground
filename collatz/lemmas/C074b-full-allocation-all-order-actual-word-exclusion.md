# C074b — Full-allocation all-order actual-word exclusion

## Hypotheses

Let T(n)=n/2 at positive even integers and T(n)=(3n+1)/2 at
positive odd integers; O and E specify actual input parities.
Use exactly L055's complete 25 indexed pairs J_i,H_i, 0<=i<=24.
Let b_i be nonnegative integers with sum b_i=9250245 and attach

a_i=2+18b_i, W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},
D_i=4J_i+H_i+a_i

to indexed row i. Let pi be any permutation of {0,...,24}.
Suppose W_pi(0)...W_pi(24) is actual at a positive integer n_0.
Define chronological inputs

\[
n_k=T^{\sum_{j<k}D_{\pi(j)}}(n_0),\qquad 0\le k\le25.
\]

Require n_25=n_0, every n_k for 0<=k<25 positive odd and
20 modulo 27, and every final even tail exact. Repeated periods and
coincident junctions are allowed. No minimum, distinguished tail,
first-return, least-root, primitive-period, H-guard, seed or count-ray
premise is imposed. All logarithms are natural.

## Conclusion

No such actual closed concatenation exists, over the full integer
allocation simplex and in every cyclic order of the intact indexed rows.

This is a local RESEARCH/REPRODUCTION application under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-17-full-allocation-all-order-actual-word-application.md`.
It extends the order scope of C073b by applying audited C074a; it makes
no originality claim beyond the inspected sources. The separate critical
audit below found no defect. Both positive rational witnesses and
Attempts 026–031 remain valid. Other pair tables, entry, unrestricted
cycles, divergence and universal eventual descent remain unresolved.
This is not a complete Collatz candidate.

## Proof

Assume such a concatenation exists. The entire indexed table in L055
has J_i>=8>=2 and H_i>=40>=3. Only those pairs are imported, not
its original allocation, witness, minimum or additional guards.
Every attached a_i is an integer at least 2 and congruent to 2 modulo
18. Thus, with chronological parameters J_pi(k),H_pi(k),a_pi(k),
these are precisely 25 allowed actual words of L041.

Write n_k=20+27u_k with u_k integral. Positivity implies u_k>=0,
since u_k<=-1 would give n_k<=-7. Oddness implies u_k is odd,
hence u_k>=1 and n_k>=47. Define s_k=n_k+23/11 for 0<=k<=25.
Then

\[
s_k\ge540/11,\qquad s_{25}=s_0.
\tag{1}
\]

The closing input has the same lower domain by closure; in particular
n_0>1. All actual-language hypotheses of L041 at r=25 hold. We use
only its section “Each occurrence's own prefix and the transfer to the
next”, namely the existing finite actual-word necessity proved with
arbitrary tails in L031. No cycle-length or primitive-count theorem
from L041 is used.

Fix an arbitrary chronological position k in {0,...,24}, and abbreviate
i=pi(k), J=J_i,H=H_i,a=a_i. Set y=T^{4J}(n_k) and
z=T^{4J+H}(n_k). That existing necessity gives

\[
y+1=(27/16)^J s_k-12/11,\quad
2^H(z+1)=3^H(y+1),\quad z=2^a n_{k+1},\quad
v_2(11n_k+23)=4J+2.
\tag{2}
\]

All its hypotheses hold at this occurrence: actual branches, J>=2,
H>=3, a>=2 and a positive odd final endpoint. In particular when
k=24 that endpoint is n_25=n_0. The arbitrary-tail passage applies
also when b_i=0 and a=2, at any chronological position.

The positive integer 11n_k+23=11s_k is divisible by 2^{4J+2}.
Consequently it is at least that power, and logarithm monotonicity gives

\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).
\tag{3}
\]

This is the non-strict guard for this outgoing row at its own input.
The domain (1) makes all logarithms defined. Substitution in (2) gives

\[
s_{k+1}=2^{-a_{\pi(k)}}\left(
 (27/16)^{J_{\pi(k)}}(3/2)^{H_{\pi(k)}}s_k
 -(12/11)(3/2)^{H_{\pi(k)}}-1\right)+23/11.
\tag{4}
\]

Both subtractive offsets are inside the tail factor; only the final
shift lies outside it. The arbitrary k establishes (3)–(4) at all
25 occurrences, including s_24 mapping to s_25=s_0. No cyclic cut
has yet been changed, and no endpoint is omitted. The indexed tails
remain attached to their own outgoing pairs throughout.

Equations (1), (3) and (4) now match every hypothesis of audited C074a:
the same complete indexed table, nonnegative integer vector b of total
9250245, attached tails 2+18b_i, arbitrary permutation pi, lower domain,
chronological closure, exact shifted endpoints and non-strict own-input
J guards. Its G_i and Q_i expand exactly to the coefficients in (4),
consistent with L051's endpoint and J definitions. No additional
real-system conditions from L051 or L055 are being assumed.

Let q be the unique position with pi(q)=0. C074a's stronger audited
conclusion says that s_q-23/11 is nonintegral. Here that same coordinate
is exactly n_q, the actual positive integer input of indexed row 0.
This is a contradiction. Alternatively every n_k is integral, directly
contradicting C074a's all-junction exclusion. The shifted s_k need not
be integers. C074a already proves that its row-0 normalization retains
both the old closing edge and the new closing edge; this application
uses that result without identifying q with chronological position zero
or with a minimum. In particular an allocated tail equal to 2 is
retained whichever edge becomes closing under that normalization.

The underlying general affine reference retained in the audited inputs
is Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239, DOI
10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The saved assessment reuses the inspected chronological affine formula
and its essential induction cases; C074a retains its upstream nonempty-word
and nonzero-denominator qualifications. Here the necessary specialization
is the explicit actual-input match above. No general affine theorem,
fixed-point calculation, parity-coding sufficiency or closure converse
is reproved or newly asserted.

All indices denote time occurrences. Equal junction values or repeated
periods remove neither an endpoint nor a guard, and no difference of
junctions is divided out. No H guard, seed, minimum, distinguished large
tail or primitive/count-ray premise enters. C073b is the literal-order
overlap, not an additional input. The rational witnesses remain valid
because their tested unshifted roots are nonintegral; the conclusion
excludes actual integer words, not their real endpoint systems. Attempts
026–031 remain valid and none of their stopped diagnostics is reopened.
Only this table and tail budget are excluded, not arbitrary cycles or
divergent orbits, and universal eventual descent remains unproved.

### Separate critical audit — 2026-10-17, step 277

The prior SPECIALIZE assessment
`drafts/literature/2026-10-17-full-allocation-all-order-actual-word-critical-audit.md`
authorizes exactly this RESEARCH/REPRODUCTION audit. The verdict is no
defect in the stated restricted actual-word application. This verifies
a relevant local input; it adds no new exclusion or originality claim
beyond the inspected sources. Upstream audited results are imported,
not recertified by this application audit.

**Language and chronology.** Inspection of all 25 pairs in L055 gives
J_i>=8 and H_i>=40, so every pair meets L041's J>=2, H>=3 language.
The allocation hypotheses give integer a_i>=2 with a_i=2 modulo 18,
including a_i=2 when b_i=0. Each OOEO block has four shortcut steps,
so D_i=4J_i+H_i+a_i is exactly the length of W_i. The difference
between consecutive cumulative exponents defining n_k is D_pi(k).
Thus the actual outgoing word at n_k has precisely the attached
parameters J_pi(k), H_pi(k), a_pi(k), and its endpoint is n_(k+1).
At k=24 that endpoint is n_25=n_0. Permutation does not detach a
tail from its row. Repeated state values do not identify different
time occurrences or remove any of these 25 equations.

For every input n_k=20+27u_k, positivity forces the integer u_k>=0.
Since 20 is even and 27 odd, oddness of n_k forces u_k odd; hence
u_k>=1 and n_k>=47. Therefore s_k=n_k+23/11>=540/11>0,
including k=25 by closure. In particular n_0>1. This matches all
of L041's language hypotheses at r=25 with chronological relabeling,
without selecting a minimum. Only its elementary own-prefix passage
is needed; its count estimates and imported primitive-cycle results
are not used.

**Arbitrary-tail necessity and the guard.** L031's finite actual-word
identities and L041's complete own-prefix passage cover each actual
word separately. For the above y and z they give
2^H(z+1)=3^H(y+1), z=2^a n_(k+1), and
16^J(11y+23)=27^J(11n_k+23). The positive integer z+1 is odd
because a>=2. Taking dyadic valuations in the first identity gives
v_2(y+1)=H. Thus u=(y+1)/2^H is a positive odd integer, and

\[
11y+23=4\bigl(11\,2^{H-2}u+3\bigr)
\]

has valuation exactly 2: H>=3 makes the term preceding +3 even.
Since 27^J is odd, the second identity gives
v_2(11n_k+23)=4J+2. All quantities whose valuations are used are
positive and nonzero. These are the already proved necessity steps,
checked here for scope and signs, not a new valuation lemma or a use
of the two-word closure converse. They apply unchanged at a=2 and
to the final occurrence whose odd endpoint is n_0.

Divisibility of the positive integer 11n_k+23=11s_k by
2^(4J+2) implies 11s_k>=2^(4J+2). Taking natural logarithms
and subtracting 2 log2 gives precisely
4J log2<=log s_k+log(11/4). The inequality is non-strict and
uses that row's own input, rather than a minimum or the input of
another occurrence. Since k was arbitrary, it supplies all 25 guards.

**Both endpoint offsets.** The inspected finite identity is
y+1=(27/16)^J s_k-12/11. Consequently
z=(3/2)^H(y+1)-1
=G_i s_k-(12/11)(3/2)^H-1, with i=pi(k).
Dividing this entire expression by 2^a and adding 23/11 yields
(4). The negative 12/11 term and the negative unit term both stay
inside the tail factor; the positive final 23/11 is outside it.
This is exactly C074a (1), whose Q_i is
(12/11)(3/2)^H_i+1, and L051 (4). It also holds on the
chronological closing edge. No H guard, seed, minimum or count-ray
assumption from L051 has been imported along with its definitions.

**C074a and both cuts.** We have the identical indexed pair table,
integer b_i>=0 of the identical total, attached a_i=2+18b_i,
arbitrary permutation pi, real lower domain, closure, and every
endpoint and own-input non-strict J guard. These exhaust C074a's
premises. Its audited proof first obtains cyclic literal order, then
chooses the unique q=pi^(-1)(0); it does not assume a minimum
location or a distinguished large tail. At its normalized position i,
the original position is r_i=(q+i) mod 25 and the outgoing row is i.
Both its input and its attached allocation therefore move together.

The old edge 24 becomes new edge 24-q, still using s_25=s_0.
The new closing edge is old edge (q-1) mod 25. If q=0 these
are the same edge; if q=24, old edge 24 becomes new edge 0 and
old edge 23 closes the new tuple. For all other q the old closing
edge is interior and the old edge q-1 closes the rotated tuple.
Thus both cuts, including any tail equal to 2, are covered by the
imported audited normalization. Equal junction values do not affect
this bijection of occurrences.

**The integer being tested.** C074a's stronger conclusion explicitly
tests s_q-23/11. By the present definition this is n_q, an actual
positive integer iterate of T; positivity and integrality persist at
every actual branch. In C074a's rotated tuple the same quantity is
t_0-23/11, not s_q and not a predetermined chronological n_0
when q differs from zero. Its nonintegrality contradicts the actual
integer n_q. No assertion that every individual rational junction is
nonintegral, and no actual-itinerary sufficiency, is needed.

The direct uses remain L041's necessity, L051's definitions, L055's
indexed table and C074a, as in the existing DAG; L031 supports the
inspected L041 passage. The primary affine citation above and its
upstream nonempty-word and positive-Lambda/nonzero-denominator
qualifications remain unchanged. No new dependency or mathematical
script is needed. The argument has not changed. Full matching Mathlib
coverage remains unchecked, as stated below.

The two rational witnesses and Attempts 026–031 remain valid: this
contradiction uses an actual integer at the specified cut, not mere
real-system feasibility or incomplete prime diagnostics. Other pair
tables, entry, unrestricted cycles, divergence and universal eventual
descent remain unresolved. This is not a complete Collatz candidate.

## Mathlib

Full matching theorem coverage is unchecked; no formal verification or
absence claim is made. Supporting ingredients are finite affine
composition, dyadic valuation divisibility, real logarithm monotonicity
and finite indexing. No new valuation theorem or Mathlib declaration
is required beyond the established canonical inputs.
