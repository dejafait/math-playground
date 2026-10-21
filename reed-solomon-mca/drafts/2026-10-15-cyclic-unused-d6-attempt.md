# Unused D_6 versus the reconstructed quadratic — step 230

The unchanged ready EXPLORE assessment is
`drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`.
Main gap: exclude sixteen actual errors. This bounded intermediate test
substitutes L092's reconstruction into D_6 and reduces its numerator
modulo Q. A nonzero residual could further restrict a possible cyclic
kernel; an identity abandons D_6 as an independent constraint on this
reconstruction. Actual-error applicability, arbitrary families, triangle
twelve and challenge definitions remain independent gaps.

Inputs read: audited L089, the full L090–L092 proofs (still awaiting
separate audits), and ATTEMPTS/020,029,031,032. No new literature is
needed on this unchanged target. Preserve the prior stops; do not sweep
H-labelings or sample rank. One exact finite-field diagnostic may test
the algebraic remainder identity, with full evidence on disk.

Saved setup before calculation: use L092's projective normalization
b=infinity,p=0,f=1. D_1 gives j=c(1-g)/(1-c), and D_10 gives
k=(de+gj-d(g+j))/(e-d). All assigned transformed labels must be
distinct. D_8 gives m=h(12)=k(c-X)/(c-k). D_3 then gives
n=h(11)=de(g-m)/(g(d+e-m)-de). Use D_2's involution on n to
recover z=h(6), and compare the pairs (1,z),(j,Y),(m,k) in D_6,
where Y=tX+u and Q is exactly L092's genuine quadratic. Retain every
finite denominator and the inverse projectivity's pole, H-membership
and collision gates. The normalized values need not lie in H.

Do not infer uniform nonvanishing from a generic calculation, and do
not infer full-kernel deficiency from determinant gates. A diagnostic
outside transformed H can verify a rational-function nonidentity only.

Completed: [L093](../lemmas/L093-cyclic-unused-d6-seed-obstruction.md)
contains the canonical proof and all formulas. E mod Q is rho_0+rho_1 X;
the necessary seed equation is Delta=0. Nonzero rho_1 leaves at most one
completion, rho_1=0,rho_0!=0 leaves none, and both-zero leaves the prior
bound two. One exact specialization c=2,d=3,e=4,g=6 gives
rho=(17,84), Delta=42 mod 97, proving rational nonidentity only.
The complete short polynomial identity is written in L093, and the
supporting certificate is scripts/cyclic-shared-gates/d6-residual-certificate.json.
All 97 scalar identity checks pass; no H-label or rank sweep occurred.

Outcome ADVANCE is a local necessary seed restriction, not an H-uniform
exclusion or certified originality. L090–L093 remain unaudited. Next
bounded test: compare S_0 with Q and this residual, retaining the
both-zero branch. In normalized coordinates its equation is

    Y(d-X)/(X(d-Y))
      +(d-c)(z-j)(X-g)/((d-g)(d-j)(z-c))=1,

where z=Z/W and Y=tX+u. This is a proposed continuation formula
to verify against L091 before use, not an established new result here.
All displayed denominators must be retained. A redundant remainder
ends this particular unused-gate test. Uniform rank R>=3, subgroup
seed feasibility, full-kernel verification and independent challenge
gaps remain open. Zero mathematical EXPLORATION turns used or carried.
