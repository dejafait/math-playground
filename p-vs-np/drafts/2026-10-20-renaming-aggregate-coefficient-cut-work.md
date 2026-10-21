# Step 390 — aggregate coefficient-cut working note

The saved EXPLORE assessment for exact S_n is reused unchanged. This is
one mathematical attempt, not further literature review. Attempts 020/032
and the supplied source comparison were checked; no aggregate bound was
previously recorded there. Existing unfinished work is preserved.

Main gap: unrestricted SAT decision/separation. Intermediate target:
polynomial explicit affine-ABP compression of the B-substituted initial
seed contribution at K_n in L099, with later Z_i=0 before B, before b.
A superpolynomial exact-output rank bound would rule out that compression;
it would not control the sum with later seeds or alternative witnesses.

Working idea saved before verification: the degree-(i+1)n part
H_i of S_i obeys H_0=a and H_i=(rho_i H_(i-1)+H_(i-1))a. The third
summand has degree at least (i+2)n. Its proposed exact support is
the 2^i words a_U a_(U intersect {2,...,i}) ... a_empty, U subset [i].
At i=n and cut n, restrict rows to a_U for U subset {2,...,n};
the corresponding suffixes start with a_U and should give an identity
matrix of order 2^(n-1). All full-polynomial parity cancellations must
be retained; verify the degree induction, injectivity and n=1 case.

Continuation test: prove this exact submatrix and extend L033's finite
constant-closure factorization to 2n letters and unequal cut lengths;
then compare the original-graph vertex bound with Q<=C(n+2)^3.
If the submatrix fails, record the precise off-diagonal/cancellation
failure and leave compression unresolved. No literal copy count can
substitute for rank. No general SF normalization, exact fg transfer,
short-proof availability, universal W2 or SAT consequence is assumed.

Completed in this step: the exact component formula and the identity
submatrix both hold. The full all-size proof, citations, affine-model
specialization and scope qualifications are canonical in
`lemmas/L100-renaming-aggregate-seed-affine-abp-obstruction.md`.
The exact cut rank is 2^(n−1), exceeding the required polynomial-in-Q
threshold. The complete small recurrence checks n=1,2,3,4 pass; see
the script and full certificate referenced in L100. No independent
critical audit has yet been performed. The earlier pending test above
is retained as a record of the attempt, not a new next-action record.
