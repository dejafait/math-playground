# Verified divisor margin — step664 working record

Gate: the invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-05-verified-divisor-minor-margin-application.md`
covers exactly this application. Main gap: actual-Xi all-degree mixed
positivity. Target: the specified D_(6001,6000) floor. Possible use: a
later independently established absolute perturbation bound. Stop on
an unsupported divisor, residual sign or ordered Cauchy–Binet factor;
no hybrid-ratio replay or dense determinant calculation is attempted.

Use m=6000, r=6001, H=3000175332800. Select m positive-height zeros
with multiplicity from Platt–Trudgian's count; in G their zeros are
-4*gamma_j^2, each counted once rather than again at the reflected
negative height. Let P(w)=product_j(1+w/(4*gamma_j^2)) and B=G/P.
Deleting finitely many real factors in L832's absolutely convergent
genus-zero product leaves B(0)=G(0)>0, the same sector exclusion,
real grouped products and summable reciprocal zeros. Apply the cited
Schoenberg theorem to those finite products and pass to each fixed
minor; do not use PF division closure.

Finite factors have indices i=0,...,6000, h=0,...,12000,
j=0,...,6000: U_(i,h)=p_(h-i), V_(h,j)=b_(6000+j-h).
Their product is exactly the target Toeplitz matrix, since every
nonzero convolution term has i<=h<=6000+j. In the Cauchy–Binet sum
all factor minors are nonnegative. For S={6000,...,12000}, U[:,S]
is lower triangular with diagonal p_6000 and V[S,:] is upper
triangular with diagonal b_0=G(0). Thus the summand is
p_6000^6001*G(0)^6001, at least
G(0)^6001*(4*H^2)^(-36006000)>0.

This calculation is a standard specialization, not an all-order
argument or a comparison with the hybrid cofactor. Full proof and
precise source qualifications will be saved canonically as L833.
