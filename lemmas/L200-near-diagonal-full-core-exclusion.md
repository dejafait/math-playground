# Lemma 200: near-diagonal full-core exclusion

**Hypotheses.** Let u,v,W be positive integers. The floor-cell part
of the full-core window in L199 requires a positive integer m with

                 uv+W <= m² <= u(v+1)-1-W.                 (1)

Write s=u+v, k=u-v, and e=0 for even s and e=1 for odd s.
For the counting conclusion, use ordered factors a,b,c,d in [N,2N],
u=ab, v=cd, |v-2N²|<=K N^(3/2), fixed K>0, and a positive
integer W comparable to N^(3/2).

**Conclusion.** A necessary condition for (1), and hence for integer
occupancy of the full L199 window, is

                    k² >= 4W+e(2s-1).                    (2)

In particular every tuple with |u-v|<2sqrt(W) has an empty integer
window, regardless of the other cutoffs or coprimality. The total
number of ordered quadruples violating (2) in the fixed central strip
is O_K(N^(5/2)), with constants also depending on the W scale.
This is o(N³). Thus this obstruction rules out a near-diagonal
construction but does not rule out the requested N³ occupancy count.
No positive occupancy lower bound is proved.

**Proof.**

If an integer m exceeds s/2, then m>=s/2+1/2. Consequently

m²-uv >= ((s+1)²-4uv)/4
        = (k²+2s+1)/4
        = u+(k-1)²/4 >= u.

This contradicts the upper bound in (1). Every permissible m
therefore satisfies m<=floor(s/2). Since m is positive, squaring
preserves this inequality. The exact identity

floor(s/2)²-uv = [k²-e(2s-1)]/4

now gives W<=m²-uv<=[k²-e(2s-1)]/4, proving (2).
Equality in (2) has not been excluded. In particular a perfect square
uv with u=v cannot furnish a full-core cell with W>0.

For the count, u,v<=4N² implies s<=8N². Failure of (2) implies

|u-v| < sqrt(4W+16N²) <= C N

for sufficiently large N, since W=O(N^(3/2)). For each fixed
ordered pair (c,d), the possible products ab therefore lie in an
interval of length at most 2CN. L197's elementary pair count gives
O(N) such ordered pairs (a,b). Explicitly, fixing a gives at most
2CN/a+1=O(1) choices of b, and there are O(N) choices of a.
The same interval count bounds the number of (c,d) in the strip
by O_K(N^(3/2)+N)=O_K(N^(3/2)). Multiplication proves the
O_K(N^(5/2)) bound. This is an upper bound on excluded tuples;
it makes no assertion that the other tuples have occupied windows.

## Qualifications, verification and formalization

Only the two floor-cell inequalities were used for the exclusion;
adding L199's safe-m cutoffs cannot restore occupancy. The opposite-side
factor-distance restriction can only reduce the excluded count. Neither
coprimality nor the totient threshold is used. Real window length,
integer occupancy outside this band, and signed-mass lower bounds
remain separate questions. This result changes no part of the RH argument.

`python3 scripts/heat/check_near_diagonal_exclusion.py` exhaustively
checks the necessary condition and the exact midpoint identity on finite
integer cases. The analytic proof supplies the uniform counting bound;
finite checks do not establish an asymptotic lower bound. Formalization
would require integer midpoint rounding, the two displayed polynomial
identities, monotonicity of squaring positive numbers, and the elementary
factor-pair interval count.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
