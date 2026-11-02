# Displaced spatial-face coefficient attempt, step 33

Invocation-start coverage: unchanged EXPLORE assessment
`drafts/literature/2026-11-02-displaced-angular-maximum-linear-rate.md`.
The approved full-angular target is unchanged. Test exactly the saved
bottom-spatial-face certificate, with D_ang=M(n-1), L_Q=mean log|Q|,
and every coefficient charged by binomial(D_ang,h).

Main gap: H>=-n/100-C log n uniformly remains unproved. A successful
certificate would supply the H input for L658/L661's localization;
support, Xi realization and mixed signs remain independent. Stop this
transfer if its certified value is below the threshold on an admissible
sequence, without interpreting that as an upper bound for H.

Partial reasoning saved before completing the proof: after division by
exp(L_Q), each summand of K(u,0) has J=n-1 factors of type C_a/U
and (M-1)J factors of type A_b/|b|. For a nonanchor summand the
remaining scalar has modulus (d/|a|)^(J+1)<=1. Pair all J C factors
with one A block; for the anchor choose any nonanchor block, and for
a nonanchor choose A_x. For a paired quadratic the absolute
coefficient bounds appear to be (3/4,8/5,4/5), hence coefficientwise
at most (4/5)(1+v)^2. Every leftover linear A factor is bounded by
1+v. Multiplication should give |[u^h]K(u,0)|/exp(L_Q)
<= (M/R)(4/5)^J binomial(D_ang,h), for every h and displacement.
Check the scalar and exact degree, Jensen transfer including zeros,
and the source degree-index bound before accepting this stop.

Relevant reads: L649 family; L657 clearing, root formula and
integrability; L658 finiteness/localization; L661 general diagonal;
L666 rational family; L670 endpoint identities and earlier stop;
step-32 history/working record and scoped coefficient/moment stops.
The coefficient theorem's ready primary evidence is Akhtari--Vaaler
arXiv:1810.12413v1 (1.3), p.1, and Theorem 1.1, p.2, with Section 2
already inspected in the inherited fixed-angle assessment. No new
external theorem, repeated source search or mathematical script is
needed. Existing unfinished work is preserved.

## Completed bounded attempt

The full proof is canonical in
`lemmas/L671-displaced-spatial-face-binomial-cost-stop.md`.
The exact degree is D_ang, since L670's top angular identity has
Re p_0>0 for every displacement vector. The Jensen/coefficient
transfer is valid including circle zeros. The pairing estimate and
the scalar (d/|a|)^(J+1) are verified. Thus B_face is uniformly below
log(M/R)-(n-1)/5 and misses the requested linear loss by at least
19n/100-O(log n). Outcome NEGATIVE; this is a bound on the
certificate, not on H. No numerical or asymptotic approximation is
needed. Independent critical audit remains undone.

The coefficient transfer is stopped. The only newly nominated target
is the angular anchor distance recorded as REVIEW_REQUIRED in
`drafts/literature/2026-11-02-displaced-angular-anchor-distance.md`.
No quantitative distance estimate or unapproved mathematical test
was performed. Its source comparison must precede any research.
