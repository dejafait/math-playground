# Co-closed-base reverse trace: reasoning checkpoint

The unchanged approved target is the complete other/other cubic limit
and comparison with -12 gamma D_i. This attempt addresses L093's R_R,
not L102's gradient-base G_R. Its downstream use is to exclude stronger
growth in one remaining sector before attempting a joint cubic limit.

Use L103(3),(8) only as the exact generator stencil
G_T1=a^-1 W C_1, and L093's S=B C_1^T with
S_st=1_(t<s)+delta_st/2. In L093's actual trace order the candidate
layer formula is

    R_R=a^-1 sum_(k,l)c_(i;kl,a) sum_(s,t) S_st
      Tr[K_(t,s) Omega_(gh,k)(s)^T T G W_t^T Omega_(hh,l)(t)],
    K_(t,s)=R_ts(Delta_T) Q.

Check this block multiplication before claiming it. The useful feature
is that each K_(t,s) is positive semidefinite as a transverse operator:
the scalar pinned axial resolvent has nonnegative entries for every
lambda>0. Its row sums are at most 1/lambda. Consequently the sum
of these positive transverse traces is at most
(N-1) Tr_T(Delta_T^-1 Q), expected to be O(N^4).

The intervening operator has norm O(a^2 p(k)p(l)), since both actual
Omega factors have norm O(a p), ||T G^(1/2)||=1 and
||W_t G^(1/2)||<=C. This suggests O(a N^4)=O(N^3) for R_R,
without a bound on the free reverse-prefix block. Verify the full
three-dimensional relative spectral sum, the coefficient placement,
all endpoint rows and the exterior heat summation. No sign or limit
is inferred from this bound. Removing an exterior-circulation F factor
would give an additional a if the same ordered estimate applies.

Essential inputs: L085 L088 L091 L092 L093 L103; L094 remains the
contrasting operator obstruction. This uses neither L104's cumulative
formula nor its inverse error. Continue if the displayed exact layer
identity and O(N^3) bound are justified; otherwise retain the failed
estimate without interpreting it as signed growth. Transverse H,
scaled limits and evaluation/compensation remain unresolved.

Completed bounded attempt: L105 proves the exact layer formula and
the O(N^3) reverse-trace bound, importing the already available
positive-block trace sum from L095(13)--(14). The complete crossed
pair R_hx is consequently cubic-bounded. The same ordered estimate
removes both actual exterior-circulation terms with O(N^2) error.
No numerical script was needed. This is local REPRODUCTION; the
original-prefix operator obstruction in L094 remains valid.

Continuation within the unchanged approved target: test uniform
cubic-scale inverse regularization for L105(3),(6), retaining its
triangular S_st and both coefficient levels before any fixed-parameter
localization. Essential inputs are L085 L088 L093 L095 L103 L105;
L090 and L100 offer contrasting regularization methods, not estimates
already proved in this order. L094/ATTEMPTS/028, L096/ATTEMPTS/029 and
L099/ATTEMPTS/030 remain stop evidence for their specific shortcuts.
No uniform mass-removal error, local axial replacement, scaled limit,
sign or compensation is assumed. A useful continuation establishes a
limsup bound tending to zero with the regularization parameter, or a
specific obstruction to that estimate. The complete coefficient would
still require transverse H control and evaluated E/H/G/R limits to
compare with -4 gamma D_i before factor 3. L084 and L079/L080/L082
fix that reference and its saved-table/IEEE qualifications.
