# Fixed negative-interval attempt1968: working checkpoint

Approved target: assessment1966, COVERED_TARGET, as reviewed in1967.
One classical specialization; no broader signed-payment calculation.

Provisional argument, pending the canonical write-up and local checks:
P_d(x)=x^d U_d(d/x); all roots correspond by z=d/u with multiplicity.
For I=[-2,-1], put h_z(x)=log|1-z/x|. If |z|<1/2,
integral_I |h_z|<=2|z|. For every complex z,
integral_I |h_z|<=log(1+|z|)+log2+2: the positive part is bounded
pointwise by log(1+|z|); the negative part is at most
log2+(-log|x-Re z|)_+, whose last term integrates to at most2.
This includes all real-root neighborhoods and endpoints.

Split the finite root multiset at |u|=2d. The strict outer part
has cost <=2d C(2d)^(-1/4) by audited C028f. For the closed inner
part choose a zero-free radius rho in (4d,6d). Jensen gives
sum_(|u|<=2d) log(1+d/|u|)<=sum_(|u|<rho)log(rho/|u|)
<=K(6d)^(3/4). C028f also bounds its count by B(2d)^(3/4).
Hence the prospective normalized bound is
[K6^(3/4)+2^(3/4)B(6+log2)]d^(-1/4), where C=4B.

Still to check in the full proof: exact finite coefficients, no origin
root, the positive/negative-part inequalities, every threshold endpoint,
all multiplicities, Jensen hypotheses and absence of an infinite-root
or degree-limit interchange. No effective value of K is needed.
The fixed-interval conclusion would not pay the full complement or
C028b's RH-equivalent height; C029f's quotient obstruction remains.

Completion: the checked derivation is now canonical in C029g. This
checkpoint preserves the unfinished reasoning and is not an independent
audit. No mathematical script or numerical evidence.
