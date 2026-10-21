# C072a — Earlier-recipient all-order actual-word exclusion

## Hypotheses

Let T(n)=n/2 at positive even integers and T(n)=(3n+1)/2 at
positive odd integers; O and E denote branches at actual odd and even
inputs. Use exactly the 25 indexed pairs J_i,H_i in L055's complete
table. Choose integers 0<=j<=21 and 1<=t<=9250244, and attach

\[
a_j=20,\qquad a_{23}=2+18t,\qquad a_{24}=166504394-18t,
\qquad a_i=2\quad(i\notin\{j,23,24\}).
\]

Let pi be any permutation of {0,...,24}, carrying each outgoing triple
(J_i,H_i,a_i) intact. Set W_i=(OOEO)^{J_i}O^{H_i}E^{a_i} and
D_i=4J_i+H_i+a_i. Suppose W_pi(0)...W_pi(24) is actual at a
positive integer n_0. Define chronological junctions

\[
n_k=T^{\sum_{q<k}D_{\pi(q)}}(n_0)\quad(0\le k\le25).
\]

Assume n_25=n_0, every n_k for 0<=k<25 is positive odd and
20 modulo 27, and every final even tail is exact. Repeated periods
and coincident junctions are allowed. No minimum, first-return,
least-root, primitive-period, H-guard, seed or count-ray premise is
imposed. All logarithms are natural.

## Conclusion

No such actual closed concatenation exists for any admitted j,t or
cyclic order of these intact triples.

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-16-earlier-recipient-actual-word-application.md`.
It assembles existing arbitrary-tail necessity and audited L072, with no
claim of progress beyond the inspected sources. C071a fixes recipient
22, outside this recipient range; it is a precedent, not this conclusion.
The separate critical audit below found no defect in this application. Both known rational
witnesses retain their different allocations; other allocations, entry,
unrestricted cycles, divergence and universal eventual descent remain
unresolved. This is not a complete Collatz candidate.

## Proof

Suppose such a concatenation exists. L055's complete table has
J_i>=8>=2 and H_i>=40>=3. Only those indexed pairs are used;
its original tails, real witness, counts and minimum premises are unused.
The indices j,23,24 are distinct. Since
166504394=2+18*9250244, the last indexed tail is

\[
a_{24}=2+18(9250244-t).
\tag{1}
\]

Thus every attached tail is an integer at least 2 and congruent to 2
modulo 18 throughout the full closed interval. At t=1 the changed tails
(a_j,a_23,a_24) are (20,20,166504376); at t=9250244 they are
(20,166504394,2). Indexed row 24 may therefore have tail 2 wherever
it occurs chronologically, including away from the closing position.
These facts hold uniformly for all j in the stated range and survive
any intact permutation.

For each chronological input write n_k=20+27q_k with q_k integral.
Positivity forces q_k>=0, since q_k<=-1 gives n_k<=-7. Oddness
forces q_k odd; hence q_k>=1 and n_k>=47. Set s_k=n_k+23/11
for 0<=k<=25. Actual closure gives

\[
s_k\ge540/11\quad(0\le k<25),\qquad s_{25}=s_0.
\tag{2}
\]

In particular n_0>1. All of L041's actual-language hypotheses at r=25
hold with chronological parameters (J_pi(k),H_pi(k),a_pi(k)). Use
only its elementary wordwise necessity in “Each occurrence's own prefix
and the transfer to the next”; no seed, cycle-length or primitive-count
estimate is needed.

Fix any chronological occurrence k with 0<=k<=24. Put
J=J_pi(k), H=H_pi(k), a=a_pi(k), n=n_k, m=n_(k+1),
y=T^(4J)(n) and z=T^(4J+H)(n). The existing arbitrary-tail
identities and valuation necessity in L041 give

\[
y+1=(27/16)^J s_k-12/11,\qquad
2^H(z+1)=3^H(y+1),\qquad z=2^a m,
\qquad v_2(11n+23)=4J+2.
\tag{3}
\]

All hypotheses hold at this occurrence: J>=2, H>=3, a>=2, actual
branches and a positive odd endpoint m. At k=24 the endpoint is n_0
and has these same properties. L041's passage uses L031's “Exact
boundary valuations, without assuming E^2 transport”, already proved
for arbitrary final a>=2; it does not use a two-word closure converse.
Since 11n+23 is a positive integer, (3) implies

\[
2^{4J+2}\le11n+23=11s_k,\qquad
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).
\tag{4}
\]

This is exactly the non-strict guard at the outgoing row's own input.
Every logarithm has a positive argument. No minimum or incoming row is
substituted for that input.

Solving the middle identity of (3) for z, substituting the first,
dividing by the actual 2^a and adding 23/11 gives

\[
s_{k+1}=2^{-a_{\pi(k)}}\left((27/16)^{J_{\pi(k)}}
(3/2)^{H_{\pi(k)}}s_k-(12/11)(3/2)^{H_{\pi(k)}}-1\right)+23/11.
\tag{5}
\]

Both subtracted terms lie inside the division, and the endpoint shift
lies outside. Each tail stays attached to its indexed J,H and actual
outgoing input. Equation (5) holds also at k=24 with output s_0,
regardless of which row pi(24) closes chronologically. In particular
it includes the endpoint of indexed row 24 wherever that row occurs.
No rotation or new minimum assumption is needed. If the chronological
cut is changed, actual closure supplies the old edge internally and
the new closing edge, with each outgoing triple still at its own input;
none of the equations or guards is dropped.

Now compare with the full hypotheses of audited L072. The indexed pairs,
integer j,t ranges, intact permutation and attached tails are identical.
Equation (2) supplies its real lower domain and closure; (4) supplies
each of its 25 own-input non-strict J guards; (5) supplies all 25 exact
shifted endpoints. These exhaust its premises. L072 excludes such a
real tuple over both closed parameter ranges and every order. Thus the
shifted actual junctions give a contradiction.

The underlying general finite-affine input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta Arith.
78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The saved assessment reuses inspected chronological composition and
essential induction cases. This proof reuses established local wordwise
necessity and checks its specialization only; general coding is not
reproved. Actuality is assumed, so rational-parity sufficiency, a
fixed-point computation and an affine-closure realization converse are
unnecessary.

Every assertion is indexed by time occurrence. Repeated periods and
coincident junctions erase no guard or endpoint, and no difference of
junctions is divided out. No H guard, seed, minimum-location,
shifted-integrality diagnostic, primitive/count-ray theorem or imported
computational cycle cutoff is invoked. Attempts 026/031 and both rational
witnesses retain their scopes. This excludes only the stated actual-word
family and leaves every independent universal gap unresolved.

### Separate critical audit — step 253, 2026-10-16

This independent audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-16-earlier-recipient-actual-word-critical-audit.md`.
It checks the stated application, accepting audited L072 within its exact
scope; it does not repeat L072's upstream arithmetic. The complete C072a
proof, L055 indexed table, L072 hypotheses/conclusion and completed audit,
L041 actual-language hypotheses and relevant wordwise proof, and L031's
arbitrary-tail identities/valuation passage were inspected.

**Parameters and lower domain.** Every one of L055's 25 pairs has
J>=8 and H>=40. C072a uses only this indexed table, not L055's old
tails or real-witness assumptions. For every integer j in [0,21], the
indices j,23,24 are distinct; hence there is no conflicting assignment
of a tail. The exact equality 18*9250244=166504392 gives (1).
At t=1 the three designated tails are (20,20,166504376); at the
other endpoint they are (20,166504394,2). Between them both varying
tails are at least 2 and 2 modulo 18. All other tails equal 2.
These are indexed assignments, preserved by any intact permutation;
there is no assumption that indexed row 24 closes chronologically.

For each actual input, positivity and n=20+27q force q>=0, while
oddness makes q odd. Thus q>=1 and n>=47, including the input at
the chosen cut. Adding 23/11 gives exactly 540/11 as the lower
bound. Closure gives the same bound at k=25. This verifies L072's
whole real domain, and also n_0>1 and every other actual-language
hypothesis needed to use L041 at r=25.

**Own-input necessity.** Fix any chronological occurrence k and keep
J_pi(k), H_pi(k), a_pi(k) with n_k. The two identities in L041's
wordwise passage apply to this actual finite word with arbitrary a>=2.
In particular 2^a n_(k+1)+1 is odd, so that passage gives
v_2(y+1)=H and writes y+1=2^H u with u positive odd. Since H>=3,
11y+23=4(11*2^(H-2)u+3) has valuation exactly 2. Its actual
B^J identity 16^J(11y+23)=27^J(11n_k+23) therefore gives
v_2(11n_k+23)=4J+2. This is the existing necessity argument,
not the converse that derives actuality from a closed affine root.
Because 11n_k+23 is a positive integer, the valuation implies
2^(4J+2)<=11n_k+23=11s_k. Taking logarithms yields (4), with
the non-strict sign and the outgoing row's own J exactly as required.
No H guard, seed or estimate for a selected minimum is used.

**Offsets and closure.** Substitution in the same existing identities
gives z=(3/2)^H((27/16)^J s_k-12/11)-1. The actual even tail
gives n_(k+1)=z/2^a. After shifting by 23/11 the result is precisely
L072 (1): both negative offsets are divided by 2^a, whereas the
final +23/11 is outside that division. C072a (5) has these same
coefficients and signs. It holds for all 25 occurrences; at k=24
the actual endpoint is n_25=n_0. In particular the equation for
indexed row 24 remains present when it is an internal occurrence.

For completeness, changing the cut to any occurrence r amounts to
using n'_(k)=n_((r+k) mod 25) and pi'(k)=pi((r+k) mod 25)
for 0<=k<25, followed by n'_25=n'_0. Each new edge is one of the
old 25 edges; the old closing edge is retained, internally unless
r=0, and the new closing edge is the old edge entering occurrence r.
The same reindexing carries each outgoing J,H,a and its guard.
This checks both cuts without choosing a minimum. Coincident states
and repeated periods do not identify different time occurrences or
remove equations, and no division by a difference of states occurs.

**Contradiction and verdict.** The indexed pairs, j,t ranges, tails
and permutation agree verbatim with L072. The verified lower domain,
all 25 endpoints, all 25 non-strict guards and closure are its entire
remaining hypothesis set. The shifted actual junctions would therefore
be the real tuple that L072 excludes. No additional primitive/count-ray,
shifted-integrality, H/seed, minimum or realization-converse input is
needed. In particular L041's sourced cycle-length estimates and
computational cutoff qualifications are not used in this implication.

No defect or missing premise was found. This verifies the existing
restricted-family application; it proves no stronger exclusion and
repairs no mathematical error. The cited finite-affine source and its
inspected cases are reused as recorded above; no new external theorem
or general coding reproof is introduced. C071a's recipient-22 audit
does not substitute for the checks here. Attempts 026/031 and both
rational witnesses concern different allocations or questions and
remain valid. Universal eventual descent and all independent gaps remain
open. No numerical script is needed for these symbolic premise checks.
The argument and direct mathematical inputs are unchanged, so no DAG or
PROOF.md change is required. Full matching Mathlib coverage remains
unchecked. Completed classification: RESEARCH/REPRODUCTION; outcome
EXPLORATION, recording new audit work without claiming a new result.

## Mathlib

Full matching theorem coverage is **not checked**. Supporting ingredients
are finite affine composition, dyadic valuation bounds and real logarithm
monotonicity. No exact Lean declarations or formal verification are
claimed; unknown availability is not evidence of absence.
