# Five scalar moments: two-atom feasibility calculation — step 121

The approved target is the COVERED_TARGET in
`drafts/literature/2026-10-14-cubic-benchmark-moment-obstruction.md`.
Its SPECIALIZE coverage is reused; this is a mathematical calculation.

The main gap addressed here is only whether the five selected scalar
constraints force positive normalized Delta jointly with negative Bcal.
The intermediate target is a law on at most six real atoms avoiding that
quadrant. A feasible law would identify the need for extra sign-sensitive
or physical input before inferring a favorable negative-Bcal clipped
weight. Continue if all four exact leading constants and the uniform
third-moment envelope can be proved; a failed ansatz is inconclusive.
Actual clipping, regulator scale, the total L367 margin, common-zero upper
counts and global mixed positivity remain independent gaps.

## Saved calculation before canonical write-up

For the exact positive constants a,b,beta,kappa extracted in the saved
assessment, put q=beta^2/kappa and p=q^2/(b ell^4). For ell sufficiently
large that p<1, propose the two atoms

    probability p:     (D,B)=(b ell^4/q, (kappa/beta) ell^2),
    probability 1-p:   (D,B)=(-(a ell+q)/(1-p), 0).

The positive atom has p D=q, p D^2=b ell^4,
p D B=beta ell^2, p D B^2=kappa ell^4 and
p B^3=(beta kappa/b) ell^2. The second atom corrects E D exactly
to -a ell, changes E D^2 only by O(ell^2), and changes none of
the mixed or B moments. Both atoms have B>=0. All coordinates are
finite at every fixed sufficiently large ell. No numerical solve,
phase assumption or actual-function realization is involved.

The complete proof and qualifications are now canonical in L410;
this draft preserves the saved calculation preceding that write-up.
No independent critical review has yet been performed. This is a
moment-only obstruction, not an RH counterexample or a clipping theorem.
