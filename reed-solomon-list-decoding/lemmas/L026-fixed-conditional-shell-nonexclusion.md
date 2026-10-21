# L026 — Fixed conditional (67,68)-shell bounds reduce to passing individual caps

## Hypotheses

Use L022's unchanged pair witness at n=1024,w=68,v=956,d=10:
p_a=a_a^*/(2 binomial(68,a)binomial(956,a)) for a>=5, where
L021 specifies the exact positive rational vector a^*. Put
B_(2a)=binomial(68,a)binomial(956,a)p_a=a_a^*/2.
The objective and threshold are M=(U+1)/2 and T=65537^28/2^128,
where U=binomial(1024,64)/binomial(68,64).
No actual packing or full-SDP feasibility is assumed.

For d in {8,10}, define R_d on one or two valid (weight,length) blocks.
Complement each block to u=min(b,length-b) and delete zero weights.
With S the remaining total weight, set R_d=1 for S<d/2, including
the empty tuple; at S=d/2 use min floor(length/u) over positive blocks.
For S>d/2 take the minimum over every positive block of
floor((length/u)R_d(child)), shortening that block to (u-1,length-1)
and normalizing again. Invalid weights are rejected.

Set P_a=R_10((a,68),(a,956)) for a=67,68. For exactly the inputs
(63,68,4,888,8) and (63,67,5,889,10), set

\[
U'_d(w_1,n_1,w_2,n_2)
=\sum_{a=0}^{63}R_d((a,n_1),(w_1+w_2-a,n_2)).
\]

Finally P_67,68=min(P_67,U'_8(63,68,4,888)) and
P_68,67=min(P_68,U'_10(63,67,5,889)). These prescribed coefficients
are upper bounds, with no exact-maxima assertion.

## Conclusion

Both conditional coefficients equal their individual caps:
P_67,68=P_67 and P_68,67=P_68. The source ratio is exactly 2,
so AVZ Proposition 17 rows (62)–(63) apply and both pass strictly.
They reduce respectively to P_68(P_67-B_134)>=0 and
P_67(P_68-B_136)>=0. Thus this fixed prescription does not exclude
L022's pair witness or its unchanged extension. Its objective remains
1.383<M/T<1.384, with floor(M)>T.

This parks only this diagnostic. Exact conditional or individual packing
maxima can be smaller; their rows, omitted SDP constraints, full-SDP
feasibility, actual packing/list realization and the 67/68-agreement
safety questions remain unresolved. The existing finite bracket does
not change. No claim about the optimal strengthened bound follows.

## Proof

**Imported shell theorem and applicability.** Erik Agrell, Alexander
Vardy and Kenneth Zeger, *Upper bounds for constant-weight codes*,
IEEE Trans. Inform. Theory 46(7) (2000), 2373–2395,
DOI 10.1109/18.887851, [June 24, 2000 institutional manuscript](https://publications.lib.chalmers.se/records/fulltext/local_14986.pdf),
Proposition 17 (57)–(64), Lemma 18 and proofs (65)–(72), printed
pp. 9–11, is imported without reproof. See the complete source
qualifications in [foundations/06](../foundations/06-conditional-shell-source.md).
Kim–Toan, [arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1),
Theorem 21, printed pp. 16–17, corroborates the formulas.

The code hypotheses are those already checked in L022: a nonempty binary
weight-68, length-1024 code of distance at least 10. For selected agreement
supports this applies to whole message tuples, uniformly in m; extra
agreements are allowed. Here delta=5, Delta=63, i=67,j=68 are distinct
members of {5,...,68}, w<=n/2 and i+j=135<=1019=n-delta.
The conditional input for P_ij bounds shell i when shell j is occupied;
it is T'(63,68,4,888,8). The swapped coefficient uses
T'(63,67,5,889,10). T' has a head-weight upper bound, not a fixed
head weight. Average shell occupancies need not be integers.

If Pi,Pj>0 and 0<=Pij<=Pi, 0<=Pji<=Pj are certified bounds, the
sign of Pij*Pj+Pji*Pi-Pi*Pj selects the source branch. A positive
sign gives the two necessary rows

\[
P_{ji}B_{2i}+(P_i-P_{ij})B_{2j}\le P_iP_{ji},\qquad
(P_j-P_{ji})B_{2i}+P_{ij}B_{2j}\le P_jP_{ij}.
\]

A nonpositive sign, including equality, gives row (64),
P_j B_(2i)+P_i B_(2j)<=P_iP_j. This test keeps the polynomial
form and would remain defined with a zero conditional coefficient.

**Known coefficient rules and implementation justification.** AVZ
Theorems 8–9, printed pp. 6–7, and Theorems 32,36, pp. 16–17,
give reflection, zero-block deletion, disjoint-support bounds and
integer shortening. Their omitted elementary proofs require the
following justification for this exact implementation; this is not
a new coding bound. Complementation is a Hamming isometry; deleting
a fixed zero block is injective and preserves distance. Valid weights
admit a word, including the empty tuple. For d=2h, S<h gives maximum
distance 2S<d and hence maximum code size 1. If S=h, distinct words
must have disjoint supports in every block, so size is at most
min floor(n_a/u_a). Choosing that many disjoint subsets in each
positive block and matching their indices attains the bound.

For S>h, any code of size N has N*u one-incidences in a positive
block of length n. At each coordinate its one-subcode shortens to
(u-1,n-1), preserving all pair distances because the deleted bit is
equal in all its words. Summing these subcode sizes gives
N*u<=n*K(child). Since 2u<=n after normalization, 2(u-1)<=n-1;
the child loses precisely one total-weight unit, even if u=1.
Induction therefore terminates and gives N<=floor(n*R_d(child)/u)
for every block. Their minimum is a certified upper bound. The two
cutoffs are h=4 and h=5, respectively, not a shared cutoff 5.

AVZ Theorem 26 and its full proof, printed p. 13, with parameter e=0
splits T'(c,n1,total-c,n2,d) into the exact-head-weight c term
T(c,n1,total-c,n2,d) and the lower-head-cap c-1 term. At every
stage c=63,...,1, p=min(c,n2-(total-c))>0, so 0<=e<p.
Neither block length changes when e=0. At cap zero Theorem 22,
pp. 12–13, gives the one-block constant-weight maximum. Iteration
thus bounds T' by the stated sum over a=0,...,63. Both heads and
tails are admissible: totals are 67 and 68, heads at most 63 in
lengths 68 and 67, and tails range from 4 to 67 or 5 to 68 in
lengths 888 and 889. Replacing each fixed-weight maximum by R_d
yields U'_d. Clipping gives valid conditional upper bounds because
min(P_a,U'_d)>=min(P_a,T'). All factors required by the source
proof are nonnegative.

**Exact coefficient certificate.** The computed values are

```text
P_67 = 323931483559693861712494525726301401249985411370443051865026726675428471168863189705770517299072
P_68 = 62630191503103646643487525762873230254001517534605050442497544763485499483720641838221579082943
U'_8 = 1329952494462326889903439850980361861901095385635370472486448106961741899967261834743122131197648
U'_10 = 83771725062833714395101626405865050717629303409828443962248059036445088402946892798997717525110
```

Both sums exceed their corresponding individual caps. Positivity and
clipping therefore give Pij=Pi, Pji=Pj and the exact branch sign
Pi*Pj>0, or ratio 2. The individual-cap slacks are

```text
P_67-B_134 = 902905760672464516606919162889102589430981024093139671279001812123225201092701346990579821436057089 / 4466 > 0
P_68-B_136 = 400370257483227733363235069895440894619578855934141459448238609092465270786134877296694961384590015 / 10208 > 0
```

Hence both applicable row slacks are strictly positive. Their identities
above exhibit the source's explicit redundancy case, rather than a
general claim about all upper-coefficient substitutions or all points.

`scripts/finite-support/conditional_shell.py` saves both pair inputs,
their original and normalized blocks, the two sets of 64 head-weight
summands, both complete sums, all 81537 reachable recursion states and
156800 shortening branches, every coefficient identity, the exact
ratio/sign, every applicable polynomial row and rational slack, and
individual-cap slacks in `scripts/finite-support/conditional-shell-results.json`.
Every branch is retained, including those not attaining the minimum.
The pair values are reconstructed from L021 and compared to L022;
no pair, triple assignment, shell choice or coefficient is retuned.

`scripts/finite-support/audit_conditional_shell.py` imports no generator
routine. Factorial binomials and polynomial convolution verify all 64
defining equations for the saved L021 vector. It independently rebuilds
both p_a and B_(2a), checking equality to L022's saved pair values.
It reconstructs normalization, both base cases, every actual child,
every rational-floor branch and every minimum in increasing total-weight
order. Reachability from the 130 roots establishes that all and only
the necessary states are present. Maximum shortening depth is 63.
It checks every head weight and summand, all Theorem 26 hypotheses,
both sums, clipping, positivity, orientation, the exact ratio branch,
every complete rational row and its separate individual-cap slack.
No sampling, floating arithmetic, or inspection preview supplies proof.

The independently reconstructed output is
`scripts/finite-support/conditional-shell-audit-results.json`. It reports
81537 reachable states, 156800 branches, zero violated rows and zero
audit failures. It also verifies 1+sum a_a^*/2=M, the unchanged
L022 objective, its exact ratio interval, and floor(M)>T. The
certificate identities and induction establish the coefficients and
the row tests. The original source rows with exact, possibly smaller
packing coefficients are not certified by this pass.

Reproduce from the notebook with
`python3 scripts/finite-support/conditional_shell.py` followed by
`python3 scripts/finite-support/audit_conditional_shell.py`.
The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-10-06-conditional-shell-fixed-coefficient-test.md`.
This is REPRODUCTION of assessed known tools and a local informative
negative diagnostic, not progress beyond the inspected source results.

## Mathlib

Full matching AVZ conditional-shell theorem, doubly-bounded-weight
partition, recursive coefficient rules and this finite certificate:
**not checked**. The source theorems are imported by precise citations;
the omitted elementary recursion proofs are justified above for the
distance-8 and distance-10 implementation. No library availability or
absence is inferred.
