# 2026-10-04 — Saved cubic/cofactor upper-test reasoning

The saved SPECIALIZE assessment explicitly covers the current uniform
degree-67 upper test. No new source review was undertaken. The exact
dictionary is L015: M(v)=I(v)-66P_67(v), so M<=I. With Q=65537,
A=66, C=binomial(1024,66), and F_A(u) the unordered subset character
sum, Fourier inversion gives

    I(v)=Q^-3 sum_u psi(-u.v) F_A(u) R(u),
    R(u)=sum_{z in E} psi(u_1 z+u_2 z^2+u_3 z^3).

The imported monomial estimate applies on H union {0} with exponent
64, and on E with exponent 1. After zero deletion, the integer cycle
weights are 514 in degree two and 770 in degree three. Every cycle
length is at most 66<Q, preserving phase degree. The imported weighted
sieve therefore gives D_2=binomial(579,66), D_3=binomial(835,66).
The complete cofactor sum is zero in degree one, below 513 in degree
two and below 769 in degree three. The resulting certified cap is

    U=C/Q^2 + 513(Q-1)D_2/Q^2 + 769(Q-1)D_3/Q.

Exact scratch arithmetic puts U/threshold strictly between 320297 and
320298; its rational square-root refinement is between 294741 and
294742. These are bounds, not actual lists, and do not certify unsafety.

There is a stronger limitation of this particular estimate. Orthogonality
gives sum_{u_3!=0}|R(u)|^2=Q^3(Q-1). Hence
Q^-3 sum_{u_3!=0}|R(u)| >= (Q-1)/769. If every cubic F_A is replaced
by D_3 before absolute-value summation, its cubic error allowance alone
is at least (Q-1)D_3/769, between 35496 and 35497 times threshold.
This lower bound concerns the allowance of the method, not the actual
Fourier error. Cancellation or better nonuniform subset-sum estimates
may still help. A lower bound on P_67 sufficient to use the subtraction
has not been supplied.

This was an interim save before the proof and checks were completed.
The canonical result is now in
[L016](../lemmas/L016-cubic-cofactor-sieve-cap-and-limitation.md), with its
exact certificate in `scripts/coefficient-fibers/cubic-cofactor-upper-results.json`.
This changes no full-code grid bound. The prior dictionary, stopped
degree-66 family and source blockers are preserved.
