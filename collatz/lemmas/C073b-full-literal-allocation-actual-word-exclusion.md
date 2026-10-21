# C073b — Full literal allocation actual-word exclusion

## Hypotheses

Let T(n)=n/2 at positive even integers and T(n)=(3n+1)/2 at
positive odd integers. O and E specify branches at actual odd and even
inputs. Use exactly L055's complete 25 indexed pairs J_i,H_i in
literal order, i=0,...,24. Let b_i be nonnegative integers with
sum b_i=9250245, and put

\[
a_i=2+18b_i,\qquad W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},
\qquad D_i=4J_i+H_i+a_i.
\]

Suppose W_0...W_24 is actual at a positive integer n_0. Define
n_i=T^{sum_{q<i}D_q}(n_0) for 0<=i<=25. Assume n_25=n_0,
every n_i for 0<=i<25 is positive odd and 20 modulo 27, and
every final even tail is exact. Repeated periods and coincident
junctions are allowed. No minimum, first-return, least-root,
primitive-period, H-guard, seed or count-ray premise is imposed.
All logarithms are natural.

## Conclusion

No such actual closed concatenation exists over this full integer
allocation simplex in literal order.

This is a local RESEARCH/REPRODUCTION application under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-16-full-literal-allocation-actual-word-application.md`.
It applies audited C073a using existing wordwise necessity, without a
new affine theorem, modular computation or originality claim beyond the
inspected sources. The separate critical audit below found no defect in
this application within its stated scope.
Both positive rational witnesses remain valid. Nonliteral orders, other
indexed pairs, universal entry, unrestricted cycles, divergence and
universal eventual descent remain unresolved.

## Proof

Assume such a concatenation exists. The complete indexed table in L055
has J_i>=8>=2 and H_i>=40>=3 for every i. Only its indexed pairs
are used, not its original tails, real witness, minimum or counts.
For every admitted allocation each a_i is an integer at least 2 and
congruent to 2 modulo 18. No bound on the support size or on an
individual b_i is needed beyond the stated simplex.

Write n_i=20+27q_i with q_i integral. Positivity forces q_i>=0,
and oddness forces q_i odd, hence q_i>=1. Thus n_i>=47. Set
s_i=n_i+23/11 for 0<=i<=25. Then

\[
s_i\ge540/11\quad(0\le i<25),\qquad s_{25}=s_0.
\tag{1}
\]

In particular n_0>1. L041's actual-language hypotheses at r=25
are met, with these same chronological parameters and exact tails.
Use only its elementary wordwise necessity in “Each occurrence's own
prefix and the transfer to the next”, whose arbitrary-tail passage is
proved in L031. Its cycle-length estimates and primitive-count imports
are unnecessary here.

Fix any i in {0,...,24}, and set y=T^{4J_i}(n_i) and
z=T^{4J_i+H_i}(n_i). That existing wordwise necessity gives

\[
y+1=(27/16)^{J_i}s_i-12/11,\qquad
2^{H_i}(z+1)=3^{H_i}(y+1),\qquad
z=2^{a_i}n_{i+1},\qquad v_2(11n_i+23)=4J_i+2.
\tag{2}
\]

The passage requires actual branches, J_i>=2, H_i>=3, a_i>=2
and a positive odd endpoint; all hold at this occurrence, including
i=24 where the endpoint is n_25=n_0. In particular this is not an
E^2-only transport rule or a converse from formal closure to actuality.
Since 11n_i+23 is a positive integer, its valuation in (2) implies

\[
2^{4J_i+2}\le11n_i+23=11s_i,
\qquad 4J_i\log2\le\log s_i+\log(11/4).
\tag{3}
\]

All logarithm arguments are positive. This is the non-strict J guard
at this outgoing row's own input, with no selected minimum substituted.
Solving (2) for z and using its actual final tail gives

\[
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
 -(12/11)(3/2)^{H_i}-1\right)+23/11.
\tag{4}
\]

Both negative offsets are inside the division by 2^{a_i}; the final
shift is outside it. This holds at all 25 occurrences, with row 24
mapping s_24 to s_25=s_0 even when b_24=0 and a_24=2.
There is no rotation or change of indexed order.

Now every hypothesis of audited C073a is matched: L055's literal
indexed pairs; nonnegative integral b_i of the stated total; precisely
the tails 2+18b_i; the real lower domain and closure (1); all exact
endpoints (4); and every own-input non-strict J guard (3).
Its unshifted coordinate is exactly s_i-23/11=n_i. C073a therefore
gives n_0 nonintegral. But n_0 is an actual positive integer by
hypothesis, a contradiction. No integrality of s_i is asserted or used.

The underlying general affine source retained upstream is
Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239, DOI
10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The saved assessment reuses its inspected chronological composition and
essential induction cases. Here finite actual-word necessity and C073a's
audited nonintegrality conclusion suffice. No new fixed-point evaluation,
general coding reproof or rational-parity sufficiency is needed;
C073a retains its upstream nonzero-denominator qualifications.

All statements concern time occurrences, so repeated periods and equal
junction values drop no endpoint or guard. No difference of junctions
is divided out. No H/seed, minimum, primitive/count-ray theorem or
closure converse enters. The two rational witnesses are compatible with
this conclusion because their unshifted cut-zero roots are nonintegral.
The last-pair overlap with C068b and the restricted support overlap with
C072a are preserved, as are Attempts 026–031; no stopped real-system
or permutation-prime diagnostic is reopened. This proves only the
stated actual-word exclusion, not a Collatz candidate.

### Separate critical audit — 2026-10-17

This RESEARCH/REPRODUCTION audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-16-full-literal-allocation-actual-word-critical-audit.md`.
The audit found no unmatched premise or defect in the actual-word
bridge. It establishes a checked local application, not a new exclusion
beyond C073b's existing statement or a universal Collatz result.

**Complete parameter and language domain.** All 25 rows of L055's
indexed table were inspected; their minima are J_0=8 and H_0=40.
Thus every row lies in L041's J>=2,H>=3 domain. Only these pairs
are imported. For every point of the stated integer simplex,
a_i=2+18b_i is an integer at least 2 and congruent to 2 modulo 18.
This includes b_i=0 at any row and allocations with several recipients
or the whole budget at one row. L041 imposes no individual upper-tail
bound. D_i counts exactly four branches per OOEO block, H_i terminal
odd branches and a_i final even branches. Therefore the defined n_i
are the actual chronological outgoing inputs. Positivity, oddness,
residue membership, exact tails and closure are explicit hypotheses.

For the lower domain, n_i=20+27q_i>0 with integer q_i forces q_i>=0:
q_i<=-1 would give n_i<=-7. Oddness forces q_i odd, hence q_i>=1.
Consequently n_i>=47 and s_i=n_i+23/11>=540/11. Closure gives the
same domain for s_25=s_0, as required even if C073a's domain is read
to include all 26 displayed indices. In particular n_0>1 and r=25>=3,
so every language hypothesis of L041 is met. Its use here stops at
the elementary wordwise passage, before any seed or cycle-length bound.

**Arbitrary-tail necessity and signs.** The full relevant passage in
L041 and the supporting L031 arbitrary-tail proof were checked.
At each occurrence the actual B^J prefix, B=OOEO, gives
16^J(11y+23)=27^J(11n_i+23), equivalently
y+1=(27/16)^J s_i-12/11. The terminal odd prefix gives
2^H(z+1)=3^H(y+1), and the actual tail gives z=2^a n_{i+1}.
These are the existing finite-word identities, used in their actual
direction only. Since a>=2, z+1 is odd. Taking dyadic valuations
in the odd-prefix identity yields v_2(y+1)=H. Thus y+1=2^H u
with u a positive odd integer, and
11y+23=4(11*2^(H-2)u+3) has valuation exactly 2 because H>=3.
The B^J identity then gives v_2(11n_i+23)=4J+2, with 27^J odd.
This checks precisely the previously proved necessity used in (2);
it does not reprove general affine coding or invoke a closure converse.

The positive integer 11n_i+23=11s_i is divisible by 2^(4J+2),
so it is at least that power. Taking increasing natural logarithms
and subtracting 2 log2 gives exactly the non-strict guard
4J log2<=log s_i+log(11/4). No strictness, minimum selection or
shifted-integrality assertion has been introduced. Solving the same
identities for the next shifted input gives (4), with both
-(12/11)(3/2)^H and -1 divided by 2^a and only then +23/11.
Thus the guard and endpoint use the identical outgoing row and input.

**Closing edge and contradiction.** The argument applies separately
to every i=0,...,24. At i=24 the actual tail ends at n_25=n_0,
which is positive odd by hypothesis. When b_24=0 its tail is 2;
the oddness of 2^2 n_0+1 and every identity above remain valid.
No prefix estimate requires a large final tail. There is no change
of cut or permutation: C073a's literal indexed pairs, full integer
budget, tails, lower domain, closure, endpoints and own-input J guards
all match. Its stronger audited conclusion is nonintegrality of
n_0=s_0-23/11 at this same cut. That quantity is exactly the actual
positive integer initially assumed, which is the contradiction.
No claim that each individual rational junction is nonintegral is needed.

Repeated periods and equal junction values are still separate time
occurrences; neither a distinctness assumption nor division by a
junction difference occurs. No H guard, seed, minimum, primitive/count
ray or rational-itinerary sufficiency is used. The existing rational
witnesses have nonintegral unshifted cut-zero roots and remain valid.
The narrower applications and Attempts 026–031 are preserved. The
primary affine citation and its upstream denominator qualifications
remain as stated above; no new source theorem or arithmetic evaluation
is needed. The direct mathematical uses remain L041, L055 and C073a,
exactly as in the DAG. No upstream numerical certificate was rerun.
The proof argument and graph are unchanged. Nonliteral orders, other
pairs, entry, unrestricted cycles, divergence and eventual descent
remain unresolved; this is not a complete candidate.

## Mathlib

Full matching theorem coverage is **not checked**. Supporting ingredients
are finite affine composition, dyadic valuation divisibility and real
logarithm monotonicity. No exact Lean declaration, absence claim or
formal verification of this application is asserted.
