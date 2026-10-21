# C073a — Full literal allocation integer exclusion

## Hypotheses

Keep exactly L055's complete 25 indexed pairs J_i,H_i in literal order,
i=0,...,24. Let b_i be nonnegative integers with sum b_i=9250245,
and put a_i=2+18b_i. Require real junctions s_0,...,s_25 with
s_i>=540/11, s_25=s_0, and every cyclic endpoint

\[
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
       -(12/11)(3/2)^{H_i}-1\right)+23/11,
\qquad 0\le i\le24,
\]

and every own-input non-strict J guard

\[
4J_i\log2\le\log s_i+\log(11/4),\qquad 0\le i\le24.
\]

Logarithms are natural. Define n_i=s_i-23/11. No H guard, seed,
minimum location, parity/residue/exact-valuation realization, actual-word
hypothesis or primitive/count-ray premise is assumed.

## Conclusion

There is no such tuple with all unshifted junctions n_i, 0<=i<=24,
integral. In fact, any tuple satisfying the endpoint/domain/J hypotheses
has n_0 nonintegral. This does not assert nonintegrality of each n_i.

This is a local RESEARCH/REPRODUCTION assembly under the prior SPECIALIZE
assessment `drafts/literature/2026-10-16-full-literal-allocation-integer-assembly.md`.
It combines existing audited restrictions, without a new affine theorem,
residue computation or originality claim beyond the inspected sources.
The separate critical audit below found no defect in this assembly. Both
positive rational witnesses remain valid; nonliteral orders, other indexed pairs,
actual-word transfer and universal eventual descent remain outside scope.

## Proof

Set E=sum_(i=0)^22 b_i. Since the b_i are nonnegative integers,
either E>=1 or E=0. In the first case every hypothesis of L073 is
present: the indexed pairs and literal chronology, the integer allocation
and total, positive early support, the lower domain, all 25 exact
endpoints including closure, and all own-input non-strict J guards.
L073 excludes this case even without an integrality premise on n_i.

Consequently E=0. Each of b_0,...,b_22 is nonnegative and their sum
is zero, so each is zero. Put t=b_23. The remaining budget gives
b_24=9250245-t. Nonnegativity and integrality imply that t is an
integer in the full closed interval 0<=t<=9250245. The tails are
therefore exactly

\[
a_i=2\ (0\le i<23),\qquad a_{23}=2+18t,
\qquad a_{24}=2+18(9250245-t)=166504412-18t.
\]

At t=0 these last tails are 2 and 166504412; at t=9250245 they
are 166504412 and 2. Thus the match includes both endpoints and does
not omit a closing tail of length 2. No row or junction is permuted.
Every endpoint, including row 24 with s_25=s_0, is precisely C068a's
endpoint for this t. The lower domain and each guard use the same
indexed outgoing row's own input as C068a. Its coordinate n_i is also
exactly s_i-23/11, with no additional shift or integrality condition.
All of C068a's hypotheses are now matched, so its conclusion gives
n_0 nonintegral. Since an all-integral tuple would include n_0, it
cannot exist. These two support cases exhaust the full integer simplex.

C068a's audited proof already excludes t>=2 by L068 and identifies the
two survivor roots before invoking L056 and L066. Its nonintegrality
conclusion, including its coordinate and nonzero-denominator qualifications,
is imported here; no modular calculation or new root identification is
needed. The standard affine input retained by the audited inputs is
Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239, DOI
10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only formal chronological composition and the fixed-point formula with
nonzero denominator enter those inputs; their positive Lambda supplies
that qualification. This proof specializes their existing conclusions by
the exhaustive support split and tail identities, rather than reproving
the affine theorem or invoking integer-itinerary sufficiency.

The two known rational witnesses have E=0 and t=0,1 respectively.
C068a already distinguishes their unshifted nonintegrality from their
real feasibility. The fixed-order overlap with C063a/C067a is preserved,
as are Attempts 026–031: no stopped real-system or permutation-prime
diagnostic is restarted. No actual-word application is made here.

### Separate critical audit — 2026-10-16

The prior SPECIALIZE assessment
`drafts/literature/2026-10-16-full-literal-allocation-integer-critical-audit.md`
authorizes exactly this RESEARCH/REPRODUCTION audit. The review found no
defect in the stated literal-simplex integer exclusion. This establishes
a checked local input, without a new exclusion or a claim of progress
beyond the inspected sources. No actual-word consequence is derived here.

**Exhaustive support split.** The quantity E in this assembly is the
integer sum of b_0 through b_22, not the positive error bound also
denoted E inside L073's proof. Each summand is a nonnegative integer,
so E is a nonnegative integer and the alternatives E=0 and E>=1 are
exhaustive. If E>=1, L073 has exactly the same 25 indexed pairs,
literal order, b_i domain and total budget. Its G_i expands to exactly
the coefficient in this statement; its two subtractive endpoint terms
and final shift also agree. Its lower domain and all 25 non-strict
own-input J guards coincide. Closure is the same s_25=s_0, so the
closing row is included. Positive early support is the sole additional
L073 hypothesis, and it is precisely this case. L073 therefore rules
out the whole case before any integrality condition is imposed.

No bound on the number, positions or magnitudes of later recipients
is required by L073. Its audited argument retains their actual tails
in the cyclic product, and uses tail-2 prefixes only before the first
positive early recipient. Thus the invocation covers allocations with
several recipients and allocations with all budget in early rows, as
well as single-recipient cases. No premise about a minimum, H guards,
seed or actual itinerary is hidden in this invocation.

**Zero support and both boundaries.** If E=0 and some b_j>0 for j<=22,
nonnegativity of the other summands would imply E>=b_j>0, a
contradiction. Hence every b_i=0 for i<23. With t=b_23 the unchanged
budget gives b_24=9250245-t. Integrality and nonnegativity give exactly
the closed integer range 0<=t<=9250245, with no divisibility or
strict-boundary restriction. Since 18*9250245=166504410, the tails
are a_i=2 for i<23, a_23=2+18t and a_24=166504412-18t.
These are C068a's formulas at the same indices. At t=0 they end in
(2,166504412); at t=9250245 they end in (166504412,2). At t=1 they
end in (20,166504394). The other 23 tails sum to 46 and the last
two sum to 166504414, preserving the full total 166504460.

**All equations and coordinates.** No rotation, reindexing or change
of cut occurs. For every i=0,...,24, the current endpoint is C068a (1)
with exactly these tails, the same J_i,H_i and the same input s_i.
In particular row 24 still maps s_24 to s_25=s_0 even at its tail-2
boundary. The domain s_i>=540/11 gives n_i=s_i-23/11>=47 in both
statements; s_25 has the same domain by closure. Every current J
inequality is C068a (2), including its non-strict sign and natural
logarithm convention. L051 (3)–(4) confirm these definitions, but its
other subsystem assumptions are not invoked. Referencing L055's table
does not import that witness's minimum, H guards, seed or primitive
scaling as hypotheses.

C068a's stronger conclusion is nonintegrality of its n_0 for every
tuple satisfying this matched system. This is the identical unshifted
quantity s_0-23/11 here. Its audited proof first uses L068's endpoint
uniqueness and full-interval guard classification: t>=2 is impossible;
t=0,1 have the respective uniquely identified literal cyclic roots.
The inherited multiplier 3^397573379/2^630138897 is less than 1 by
the audited positive Lambda bound, so uniqueness and the nonzero
denominator require no additional assumption on the current tuple.
L056 matches the t=0 root to Phi_0/Delta with Phi_0=4 modulo 5;
L066 matches the t=1 root to Phi_1/Delta with Phi_1=21 modulo 25.
Here Delta=2^630138897-3^397573379>0 is divisible by 5 in both
cases. These are the previously audited residues and coordinate
identifications, not fresh computations. They concern n_0, not s_0,
and no old-tail numerator is used for the changed-tail survivor.
Their hypotheses and qualifications are retained through C068a.

Thus every possible tuple lies in the zero-support case and has
nonintegral n_0. An all-integral collection n_0,...,n_24 would in
particular have integral n_0, giving the claimed contradiction. This
requires no statement that every individual n_i is nonintegral and
no converse from integer affine closure to a Collatz itinerary.

The direct mathematical uses remain L073 and C068a, exactly as in the
DAG. The precise primary affine citation above and the Mathlib
qualifications below are unchanged. This audit reuses the established
input results and their arithmetic audits; it does not rerun their
certificates or assert a new independent verification of their finite
data. No mathematical script is needed for this exhaustive conjunction.
Both E=0 rational witnesses, the survivor overlap with C063a/C067a,
and Attempts 026–031 remain valid. Nonliteral orders, other indexed
pairs, actual-word transfer and universal eventual descent remain
outside the conclusion. The assembled argument and DAG need no change.

## Mathlib

Full matching coverage of this family assembly is unchecked; no absence
claim or formal verification is made. The prior assessment records
supporting `padicValRat.defn`, `padicValInt_dvd_iff` and
`Rat.num_or_den_zero_padicVal` in
[PadicVal.Basic at commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean),
with prime, nonzero and reduced-pair coprimality qualifications. This
assembly uses C068a's nonintegrality conclusion and needs no new
valuation theorem.
