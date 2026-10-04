# Fixed rank-two fourth-Chern calculation checkpoint

Date: 2026-10-04. One mathematical specialization under the prior
SPECIALIZE assessment `drafts/literature/2026-10-03-rank-two-fourth-chern-test.md`.
The class is exactly V' in L044 (15); its chamber, line terms and
trivial twist are fixed. No residue search or change of class is made.

The normalization's finite double cover has trace decomposition
O_S direct sum O_S(-f_ell), hence chi(O_Y)=4 by K3 surface HRR.
All three point quotients give chi(O_C)=1. The ambient second Todd
term is 2(eta tensor 1+1 tensor eta), whose product with [C] has
integral eight. Thus ch_4(O_C)=-7 eta tensor eta.

Exact arithmetic for the saved signed line terms gives seven from
the Delta sum and minus twenty-five from each third finite difference,
since q(y,y)=-50. Together with 2 ch_4(O_C), this gives
ch_4(V')=-57 eta tensor eta. The full second-character square is
188 eta tensor eta: 32 from the pure factors, 36 from N and 120
from T. The imported fourth-character polynomial then gives
c_4(V')=(188/2-6(-57)) eta tensor eta=436 eta tensor eta.
The necessary ch_4 value for rank two is instead 188/12=47/3.

The direct signed-line Euler characteristic and ambient HRR both
give chi(V')=-33. This excludes a rank-two locally free representative
of this particular class, rather than arbitrary representatives of
the cubic action. The universal Hodge gap and three-versus-four
RM-direction threshold are unchanged. The calculation is a
REPRODUCTION of known tools, with no originality claim.

The canonical full proof is [L045](../lemmas/L045-fixed-rank-two-fourth-chern-exclusion.md).
The initial exact-arithmetic checkpoint above is preserved alongside
the completed proof and reproducible checker.
