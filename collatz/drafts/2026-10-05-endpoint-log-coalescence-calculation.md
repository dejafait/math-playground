# Endpoint clock — saved calculation

Approved target: the exact TARGET in
`drafts/literature/2026-10-05-residue47-endpoint-log-coalescence.md`.
Main gap: universal eventual descent. Intermediate use: constrain
two-path covers transferring convergence from a smaller residue-20
companion. Larger clocks, other cylinders and termination remain open.

Essential input is audited L026's shifted inverse identity and anchor
proof, with L025 entering through it. No least-root or convergence
assumption is made. CRT is the other standard input. Preserve actual
parities, positivity, residue guards, strict order and zero clocks.

Saved before final proof/checks: put r=t for t<=4 and r=t-1 otherwise,
h=s-t and j=r-a. Then lambda=2^h*3^j. If lambda>1 and h<0,
j>0 and lambda-1>=2^h, so 2^s/(lambda-1)<=2^t<=2^L.
If h>=0,j>=0, lambda is an integer at least 2 and this ratio is
at most 2^L. If h>=0,j<0, put b=-j>0; 2^h>3^b gives
lambda-1>=1/3^b and 2^s/(lambda-1)<=2^s*3^b<2^(s+h)
<=4^L. Thus n>4^L excludes all slopes above one using the unchanged
0<=d<=2^s-1 and q_t>=1. This includes all exponent signs and zeros.

Only the slope-above-one passage and the final n>47 conclusion used
L026's old size guard. The latter follows from n>4^L for L>=6.
The lambda<=1 anchor proof otherwise has the same congruences and
all its guards; its exact finite arithmetic claims are reused.

CRT modulus M=162*6^L. Selecting the first root strictly above 4^L
gives 4^L<n<=4^L+M<163*6^L. For fixed B>=0, take
L>=max(6,ceil((log(163)+B*log(12))/log(2))). Then
log(n)/log(12)+B<L. The roots are unbounded since n>4^L.

The continuation test passes analytically: the new guard is below
the CRT height scale, and that scale is strictly below 12^L.
No finite enumeration proves the all-horizon claim. The canonical
proof and focused exact checks will record the result; independent
critical audit remains required.
