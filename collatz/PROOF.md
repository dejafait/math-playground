# Collatz conjecture: argument overview

The exact target and shortcut-map conventions are recorded in [foundations](foundations/01-target-and-scope.md). No complete candidate argument has been developed.

## Unresolved gap

The missing claim is that every positive starting integer greater than 1 eventually has a shortcut iterate smaller than itself. Strong induction would then give convergence to 1. This criterion is equivalent to the target and is not an established input.

A proposed sufficient route sought descent of log(n)+h(n mod q) within a common finite number of steps, outside a finite base set. Finite sublevel sets would make this enough for termination, after the base set was proved to converge. L001 rules out this route for every finite modulus, window, and correction h.

Allowing an entire maximal odd run followed by all consecutive even steps gives a variable-length block. L002 derives its exact endpoint but rules out automatic descent during that first block. L003 extends the obstruction to every fixed number of complete blocks, including finite residue corrections at their endpoints. L004 also excludes decrease on every block for log(n+5)+F(v_2(n+5)), with arbitrary real-valued F: an unbounded correction using this single valuation does not repair the route. Unbounded return times depending on the start, richer arithmetic information, and other mechanisms remain open. There is still no universal eventual-descent estimate.

Within the restricted alphabet {(2,1),(3,1)}, L005 excludes infinite eventually periodic block itineraries by an exact valuation bound for repetitions of any fixed word. It leaves aperiodic itineraries open. L007 gives forced backward decoding except at the earliest block, with at most two histories of any fixed depth ending at one integer. L008 converts this into an exact endpoint density, but its finite-interval error prevents the resulting upper bound from excluding all endpoints at a fixed starting cutoff. A starting-size lower bound tending to infinity uniformly over all mixed words would exclude infinite aperiodic itineraries too; none of these results establishes it, and even that bound would leave other block types and later compensation unresolved.

Adding both single-letter shifts to a potential does not close this restricted gap. L006 excludes decrease on every permitted block for log(n+5)+F(v_2(n+5),v_2(11n+19)), with arbitrary F. A legal growing two-block path returns to the same pair of valuations, so the correction cancels. This leaves unbounded return times and arithmetic information beyond this pair unresolved.

Adjoining the contracting block (1,1) preserves forced backward decoding: L009 bounds the number of histories of any fixed depth at one endpoint by three. This now covers both growth and contraction, but inverse size can increase and the fixed point 1 has histories of every depth. Every start greater than 1 must leave this enlarged alphabet if it is to reach 1; that escape claim remains unproved. The rigidity also still assumes even-run length 1 throughout.

## Partial results

L001 proves an exact obstruction: arbitrarily large starts have arbitrarily long growing shortcut prefixes that retain one residue modulo any prescribed modulus. Their corrected logarithmic size increases at every time in the window. This limits a proposed proof method; it establishes no new family of convergent orbits.

For odd n=2^a u-1 with u odd, L002 gives b=v_2(3^a u-1) and the next odd block endpoint R(n)=(3^a u-1)/2^b. Strict descent holds exactly when (2^(a+b)-3^a)u>2^b-1. Every positive pair (a,b) occurs infinitely often, and n=16t+11 gives R(n)=18t+13>n. This rules out first-block contraction; it does not control consecutive blocks.

L003 proves that the first K blocks all have (a,b)=(2,1) exactly when 2^(3K+1) divides n+5. Their endpoints satisfy R^j(n)+5=(9/8)^j(n+5), and no intermediate shortcut state descends below n. Multiplying n+5 by any modulus q keeps all endpoints in one residue, defeating bounded-block endpoint descent for log(n)+h(n mod q). Each fixed positive n has only floor((v_2(n+5)-1)/3) initial repetitions; this finite escape bound neither forces later compensation nor proves an infinite growing positive orbit.

That valuation loss can compensate for growth on (2,1) blocks, but L004 gives growing (3,1) blocks 128s+103 to 216s+175 with v_2(n+5)=2 at both endpoints. Every correction F of that valuation cancels, leaving potential change at least log(5/3)>0 for arbitrarily large starts. Other (3,1) blocks increase both size and valuation, with unbounded valuation gains. These facts refute the proposed correction at a single block; they supply no bound on later compensation.

For each finite mixed word, L005 gives one exact residue class and an affine endpoint (Pn+C)/2^D. The number of initial complete copies of that word is floor((v_2((P-2^D)n+C)-1)/D), finite for every positive start. Its starting-size bound diverges for a fixed word repeated increasingly often, but is not uniform over arbitrary words. Exact enumeration through length 12 supplies no infinite-length inference. The mixed word (2,3,2,2) starts at 603, below the repeated-(2,1) bound 8187, so that sharp bound cannot be transferred unchanged.

L006 constructs successive block endpoints 8192s+4699, 9216s+5287, 15552s+8923 for s>=0, with types (2,1),(3,1) and joint valuations (5,2),(2,6),(5,2). Every correction of this pair cancels over the two blocks, while the logarithmic increment is at least log(93/49)>0. Thus at least one block increases the potential by a fixed positive amount, at arbitrarily large starts. No linear or nonlinear correction using only this pair can meet the required per-block decrease.

L007 proves that an odd endpoint m has inverse branches G_2(m)=(8m-5)/9 when m=4 modulo 9 and G_3(m)=(16m-19)/27 when m=13 modulo 27. The respective predecessors can themselves have an allowed predecessor exactly when m=76 modulo 81 and m=175 modulo 243. These classes are disjoint, so at most one branch can extend. Induction bounds the number of depth-K histories at two, differing only in their earliest state. The backward size bound n_0<(8/9)^K m controls depth for a fixed endpoint, not for a fixed start with an unrestricted future endpoint.

L008 describes depth-K endpoints as 2^(K-1) disjoint odd residue classes, with exact density delta_K=(1/18)(4/27)^(K-1) among all integers. Their count below X differs from delta_K X by less than 2^(K-1). All histories starting at most N end below X_K=(27/16)^K(N+5), where the density contribution is 3(N+5)/(8*4^K), but the error bound grows. At N=175, K=4 the endpoint 1453 is below X_K while the density contribution is 135/512<1, refuting its use alone as an upper count. The true count's eventual vanishing and the required uniform least-start bound remain unresolved.

For {(1,1),(2,1),(3,1)}, L009 gives extendible inverse branches exactly on m=1 modulo 9, m=22 modulo 27, and m=13 modulo 81, respectively. These classes are disjoint; v_3(2m+1) forces the only possible extendible odd-run length. At most three histories end at any m at each depth, all sharing every state after the earliest. Only the constant history ends at 1. The new inverse (4m-1)/3 grows for m>1, so the old backward contraction bound does not extend and no forward escape estimate has been obtained.

[Tao's Theorem 1.3](foundations/02-known-results.md) is recorded as background: every diverging bound eventually dominates the orbit minimum for a set of starts of logarithmic density 1. It supplies neither the bound 1 nor the universal quantifier, and is not used to prove L001.

## Known traps checked

- The source target concerns every positive integer. Neither density-one results nor finite computation remove all possible exceptions.
- Computations check identities, finite residues, and finite histories only; the lemmas have full elementary proofs and use no probabilistic parity assumption.
- A witness is chosen after fixing the finite window. Arbitrarily long growth does not produce one positive integer growing forever.
- The two Collatz maps and their time conventions are distinguished in foundations. Reaching 1 is equivalent for them.
- Eventual descent is explicitly an unproved target-equivalent criterion. The fixed-window and fixed-complete-block strengthenings have been refuted, not smuggled into a proof.
- The complete-block formula retains its positive additive term. Consecutive (2,1) blocks are established by exact congruences, without assuming independence. Satisfying those congruences for all K would require n=-5, outside the positive domain.
- Arbitrarily long growing prefixes and their sharp exponential starting-size cost do not decide what happens after the prefix ends. The finite residue correction obstruction for complete blocks concerns endpoints only.
- Compensation for valuation loss on one block type is not a global potential inequality. L004 keeps the logarithmic and valuation terms together and gives the opposite of the required sign; it excludes only the stated single-valuation correction with decrease required on each block.
- An odd final affine endpoint implies a prescribed mixed itinerary only because L005 proves all intermediate exact run conditions. Finite word enumeration and exclusion of eventual periodicity do not exclude aperiodic infinite words. The repetition estimate holds a word fixed; no exchange with a limit over all words is made.
- The valuation pair returning in L006 is not an integer orbit cycle. The obstruction uses one legal two-block path at each of unboundedly many starts, without assuming that these paths concatenate indefinitely. It excludes the specified potential certificate, not aperiodic itineraries or Collatz.
- Backward rigidity in L007 does not turn a finite past at each endpoint into a finite future at a fixed start. The inverse congruences include positivity and exact maximal run lengths; their multiplicity bound is not a uniform least-start estimate.
- L008 keeps the residue-class boundary error when both the depth and endpoint cutoff grow. A shrinking density contribution is not a count below one. Its endpoint count includes histories starting above N; failure of this sufficient upper bound to shrink does not show that the true count fails to vanish.
- L009 recomputes extendibility for the enlarged alphabet and checks positivity and exact maximal runs. The fixed point 1 is retained. A unique extendible inverse branch can grow, so backward rigidity is neither a decreasing height nor a bound excluding infinite forward itineraries. The proof uses fixed even-run length 1 and establishes no claim for variable even-run lengths.
- Methods controlling later blocks and richer arithmetic information remain open. No global research stop or resolution is claimed.
