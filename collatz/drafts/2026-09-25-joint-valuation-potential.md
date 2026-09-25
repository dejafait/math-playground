# Joint valuation potential test, 2026-09-25

## Gap, intermediate target, and relevance

Universal eventual descent remains unproved. Even an infinite aperiodic
itinerary confined to the complete-block types (2,1) and (3,1) has not been
excluded. This single step tests the proposed intermediate certificate

    V(n) = log(n+5) + c v_2(n+5) + d v_2(11n+19),  c,d >= 0,

with strict decrease on every block of either type outside a finite set.
Since V(n)>=log(n+5) and both block types grow by at least a factor 9/8,
such a certificate would exclude every infinite itinerary in this alphabet.
Other block types and eventual return below the original start would remain
unresolved even if this restricted certificate succeeded.

The whole overview, DAG, prior changes, L002, L004, L005, and all five
attempt records were inspected. L004 rules out a correction using the first
valuation alone. L005 supplies the two shifts from the individual block
maps but does not control switching between them. Thus the joint test is
not a duplicate of either result. Existing work is preserved. The primary
[source](https://mathprize.net/posts/collatz-conjecture/) was rechecked on
2026-09-25 and retains the universal positive-integer target.

The discriminating test is to derive exact joint valuation transitions and
either exhibit feasible coefficients or an unavoidable positive potential
increment. A growing legal finite path that returns to its initial pair
of valuations would refute even an arbitrary correction F of the pair:
the correction cancels over the path. Such a counterexample must occur at
arbitrarily large starts to defeat a finite exception set. A failure of
this certificate will stop this specific route, not arithmetic research
or the Collatz target.

## Saved reasoning before verification

Put x=n+5, y=11n+19=11x-36, p=v_2(x), q=v_2(y). L002 gives

    (2,1): n = 11 mod 16,  x' = 9x/8,       y' = 9(y+4)/8;
    (3,1): n =  7 mod 32,  x' = (27x-36)/16, y' = 27y/16.

On a (2,1) block p>=4 and q=2; on a (3,1) block p=2 and q>=5.
Switching may exchange a loss of one valuation for a gain of the other.
For an initial x=32u with u positive odd, the formal two-block path
(2,1),(3,1) gives x'=36u and x''=9(27u-1)/4. A possible return
to the initial valuation pair (5,2) would require v_2(27u-1)=7.
The congruence u=147 modulo 256 appears to give the path

    n_0 = 8192s+4699,
    n_1 = 9216s+5287,
    n_2 = 15552s+8923,  s>=0,

with pairs (5,2), (2,6), (5,2). The necessary verification is that both
blocks have their exact maximal run lengths, all six valuations are exact,
and (n_2+5)/(n_0+5) has a uniform lower bound greater than 1.
Returning to the same valuation pair is not returning to the same integer;
no periodic positive orbit or infinite repetition is being asserted.

## Completed assessment

[L006](../lemmas/L006-joint-valuation-potential-obstruction.md) proves the
entire proposed witness family. The exact pair return (5,2), (2,6), (5,2)
gives total potential increase at least log(93/49)>0 for every function
F of the pair. This is stronger than the proposed linear test. The actual
required threshold was a negative increment on each permitted block;
at least one increment is instead at least (1/2)log(93/49). The starts
are unbounded, so a finite exception set cannot repair the certificate.

The [script](../scripts/joint-valuation/check_potential.py) and
[output](../scripts/joint-valuation/result.json) retain exact checks on
1,024 odd starts for the block domains and shifted identities, and on
261 parameter choices for the witness, totaling 5,924 shortcut transitions.
These computations check algebra and indexing; the proof is independent
of any finite sampling. Mathlib coverage is not checked.

The outcome of this one coherent test is NEGATIVE: it eliminates the
proposed joint potential, including arbitrary nonlinear corrections using
the same information. The [attempt record](../ATTEMPTS/006-joint-valuation-potential.md)
preserves the obstruction. No coefficient search, enlargement of finite
exceptions, or replacement of the linear correction by such an F can
repair this route. Consecutive exploration turns without an advance or
informative negative remain zero. Universal descent and aperiodic mixed
itinerary exclusion remain open; no complete candidate has appeared.

A different arithmetic mechanism is available for a later bounded test:
the inverse maps (8m-5)/9 and (16m-19)/27 impose powers-of-3 divisibility,
whereas this failed potential used only powers of 2. Determining whether
both inverse branches can extend through another legal earlier block may
give restrictions on long mixed words. Even forced backward decoding
would still need a height estimate to yield the uniform least-start bound;
that implication is unresolved and is not asserted here.
