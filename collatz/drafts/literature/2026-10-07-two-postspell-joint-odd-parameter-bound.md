# Two-postspell simultaneous J,H restriction — completed scope review

TARGET: Establish explicit absolute A,B such that every actual closed two-postspell word has an index i with 4J_i+H_i<=A log(N)+B, retaining independent tails and repeated periods.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Six focused joint-parameter, postspell and odd-run/cycle-height queries completed; L031, L035 and L036's relevant proofs, L020's prefix formulas, the prior balance assessment, history 069 and Attempt 019 compared; exact queries and inspection limits below.
SOURCE_EVIDENCE: Simons–de Weger, Acta Arith. 117 (2005), section 1.2 p. 52, section 2.1 p. 56, Lemma 6 and proof p. 58, Lemma 7 and proof pp. 58–59, Lemma 12 and full proof plus Corollary 13 p. 61 inspected; Sodelin Postspell_Guarded_Root_Descent.md sections 1,3,4 inspected; prior Hercher and transcendence assessments reused.
COMPARISON: Published estimates and canonical actual-prefix identities cover the needed inputs, but no inspected theorem directly states the same-index 4J_i+H_i bound. L036 alone controls only a smaller J; source Corollary 13 controls the global cycle minimum with a full minimum-count factor, not one of the two designated junctions. A boundary-size specialization using L035 is still required.
GAP: Select one junction using the reciprocal upper bound and published lower bound, then obtain both its J and terminal H from its own positive actual-prefix heights; give explicit constants and retain all offsets and repetitions. Neither this joint estimate nor its constants is established here.
REASON: Essential joint-target coverage is now adequate for one later REPRODUCTION attempt combining existing inputs; no reproof of transcendence theory, parity coding or general run-length mathematics is justified.
SCOPE: Actual positive integer closure of W_1W_2 with W_i=(OOEO)^(J_i)O^(H_i)E^(a_i), J_i>=2,H_i>=3, independent a_i>=0 congruent to 2 modulo 18, positive odd residue-20 n,x,n>1 and exact tails; N is the represented total step count and repeated periods including x=n are allowed.
LITERATURE_REASON: The joint H parameter was outside the prior ready min(J_1,J_2) scope; section 2.1's primary run-length premise and its applicability to the terminal subrun required comparison before any joint derivation.

## Proposed use and discriminating test

The main gap remains universal eventual descent. The intermediate target
would restrict an entire odd-growth portion at a single junction, rather
than only the smaller J parameter. Its plausible downstream use is to
organize the remaining asymmetric integer-closure cases. It would still
leave the other word, the even-tail parameters, total length, entry,
other cycles and divergent orbits unresolved.

The approved proposed mechanism first seeks a polynomial upper bound
in N for b=min(n,x) using L035 and the published lower linear-form
estimate. Choose i by this boundary b, retaining either choice in a tie.
Next seek quantitative bounds for J_i and H_i from that same word's
boundary valuation and its intermediate height y=T^(4J_i)(b).
This is a plan for a later mathematical test, not a polynomial-height
or joint-parameter result. Separate minima for J and H do not meet the
target. No values of A,B are derived or approved in this note.

Continue the later attempt only if it proves the joint estimate with
explicit constants at that same index under the unchanged actual-word
hypotheses. Abandon if it needs an unsupported comparison between
junctions or parameters, or gives only separately selected minima.
Attempt 019 remains evidence against guard-only closure contradictions;
history 069's count mismatch and blocked Brox scope are not coverage.

Essential local inputs to assess are L031, L035 and L036, and the exact
published Simons–de Weger Lemma 12 already cited in them. L020 may supply
only its established affine identities. Source computations and Rhin's
original proof remain imported rather than independently certified.
No positive integer closed root or universal entry is presumed to exist.
Mathlib matching coverage is not checked.

## Primary statements and hypothesis comparison

John Simons and Benne de Weger, *Theoretical and computational bounds
for m-cycles of the 3n+1-problem*, [Acta Arithmetica 117 (2005), 51–70](https://www.impan.pl/shop/en/publication/transaction/download/product/82263),
section 2.1, printed p. 56, writes an actual start of k consecutive
odd steps as s=2^k u-1, u a positive integer, and its subsequent
even maximum as 3^k u-1. Section 1.2, p. 52, defines the local
minima, increasing runs and represented K,L, explicitly allowing a
nonminimal period. The source run formula's divisibility premise is
consecutive actual odd inputs. It is not an independence assumption
about parities or a uniform bound on the run length.

At the local y after (OOEO)^J, the terminal O^H is a subrun of a
longer run: the preceding last letter of OOEO is also O. Thus y
must not be substituted as a local minimum in source chaining
estimates. L031's already proved exact-tail argument instead gives
v_2(y+1)=H directly. Its equation (4), and L020's equation (4),
already give the corresponding intermediate height formula with the
additive 23/11 retained. L036's equation (2) gives a positive boundary
height bound for J alone, separately at each boundary. These canonical
inputs cover the finite arithmetic needed for the proposed same-boundary
specialization without adding a maximal-run or relative-growth premise.

The published Lemma 12, printed p. 61, states
Lambda= (K+L)log(2)-K log(3) > exp[-13.3(0.46057+log K)].
Its complete proof applies Rhin's Proposition p. 160 with
u_0=0,u_1=K+L,u_2=-K and Lemma 8. Reuse the adequate prior
assessment of that proof's computational and transcendence inputs;
Rhin's original proof and the computations are imported, not separately
certified. Here K=3(J_1+J_2)+H_1+H_2 and L=J_1+J_2+a_1+a_2
are L035's represented occurrence counts. Its positive nontrivial
closed cycle has the source shortcut convention, and neither source
nor local bound requires distinct junctions or a primitive representation.
Keep K<N when choosing constants; do not silently use primitive counts.

Corollary 13 and its proof on p. 61 bound the global minimum by
m exp[13.3(0.46057+log K)]. That minimum need not be n or x;
the full minimum count is not two. Lemma 6's complete proof p. 58
uses the actual local-minimum run representation and a verified lower
height X_0. Lemma 7's proof pp. 58–59 propagates that comparison
through every one of the m minima; Lemma 14's upper bounds retain m.
They cannot be used here by putting m=2. The prior minimum-count
assessment and history 069 already settle this scope issue. The
proposed specialization uses L035's two designated boundary contributions
instead, not an unproved junction/global-minimum identification.

Sodelin's [Postspell_Guarded_Root_Descent.md](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md),
node AC-POSTSPELL-GUARDED-ROOT-DESCENT-001, live main inspected
2026-10-07, section 1 supplies the same affine identities as canonical
L020. Section 3 states the exact terminal valuation under O^H E.
Section 4 leaves independently unbounded J,H and failed-exit finite
words. These do not contradict a conditional closed-word restriction.
Its descent assertion needs a final halving guard e>=J+H; that guard
is not supplied by our independent a_i and is not imported. No
immutable source revision or successful Lean build is claimed.

## Search scope, duplicates and limits

Queries: `Collatz cycle odd run length k log minimum Simons de Weger Lemma 7`;
`Collatz OOEO postspell cycle simultaneous J H logarithmic bound`;
`Collatz cycles run length bound minimum element log cycle length`;
`"Collatz" "odd run" "log" "length" cycle minimum`;
`"Collatz" "postspell" "logarithmic"`;
`"Simons" "de Weger" "ki" "xi" Lemma 7`.
Primary statements and relevant proofs above were inspected before
broader passages. The author manuscript v1.44 (2010-08-31) was located;
its relevant comparison and Hercher's Theorem 16 remain covered by
the prior adequate balance/reciprocal assessments. No refresh is needed.
Search hits for Halbeisen–Hungerbuhler rational-cycle bounds, Simons's
two-cycle paper, recent 94/95-cycle preprints and recent Lean repositories
were discovery leads only; their detailed theorems were not inspected
or imported. No novelty or Mathlib absence follows from these searches.

The exact target is not a duplicate of L036: both parameters must
belong to the word at the selected boundary. L031/Attempt 019 already
show that valuations follow from integer closure; this attempt combines
them with a different effective size constraint instead of seeking
another guard-only contradiction. No cross-notebook inputs were read.
This completed source review approves the unchanged Next action for
one research turn, classified REPRODUCTION if successful. It derives no
new inequality and does not alter any lemma or mathematical script.
