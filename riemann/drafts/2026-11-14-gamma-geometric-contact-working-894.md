# Fixed gamma/geometric contact attempt894

Prior gate: unchanged EXPLORE assessment892; exact fixed density
p=g_(3/2,1)*g_1, Lg_1(s)=product_(n>=1)(1+s/2^n)^(-1).
No parameter sweep or actual-Xi realization is authorized by this test.

Main gap: L030-L032/C032a actual-Xi all-degree positivity. Intermediate
target: the full smooth scalar-Volterra model with D1,D2 strictly positive
through a simple first downward D3 crossing. Its possible use is to test
the sufficiency of C466b's scalar premises beyond C466c's free jet.
Continuation requires proved admissibility and all prefix/contact signs;
an earlier lower-sign failure or incompatible contact geometry stops this
candidate. A negative sample alone is not a witness.

Read assessment891 completion892, assessment883's exact scalar-law
coverage, C466a's boundary statement, C466b's hypotheses/conclusion,
C466c and its recorded finite-root stop. These do not settle the model.
Reuse the assessed Khare finite-PF distinction, Kwasnicki geometric
smoothing construction and Steutel--van Harn scalar-law theorem. The
target and source scope have not changed. Matching Mathlib is unchecked.

Working plan, not conclusions: identify the kernel from the product;
justify smoothness, support and positivity using the cited smoothing
construction; establish strict pointwise log curvature rather than only
PF2; compare D3 at the endpoint and at infinity; isolate the missing
first/simple-contact condition if a full proof is unavailable. Preserve
all unfinished reasoning here before extended work. No model witness or
actual-Xi sign is asserted.

## Partial reasoning saved before canonical write-up

Let a=3/2, beta=1/2, lambda_n=2^n and g=g_1. The product gives
B(s)=a log(1+s)+sum log(1+s/lambda_n), hence the proposed H is the
canonical kernel. Its integral is a+sum lambda_n^(-1)=5/2. Apply the
assessed scalar-law theorem after verifying support and smoothness.

Strict D2: finite exponential convolutions are PF2 by the assessed
composition formula; their smooth infinite-convolution limit g is
log-concave. For the conditional density proportional to f(u)g(x-u),
(log p)'' is Cov(beta/u-1, (log g)'(x-u)). The first score is strictly
decreasing; the second is nondecreasing and cannot be constant on the
whole interval because g is flat at zero and positive inside. The
covariance is strictly negative. Differentiate on g or use f' in L1;
do not differentiate the singular gamma base twice under the integral.

Near zero: tilt by s, let mu=B'(s), sigma^2=-B''(s), N=floor(log_2 s).
Then N/4 <= s^2 sigma^2 <= N+3, mu decreases to zero. The centered
standardized characteristic function tends to exp(-t^2/2), and its
modulus is bounded by (1+t^2/(16N))^(-N/2). For N>=16 the common
majorant (1+t^2/256)^(-8) permits inversion through derivative order4.
The limiting signed third Gaussian derivative determinant is
2(2pi)^(-3/2)>0. Tilt/scale contributes a positive factor only.

At infinity set M=E exp(Y)=product lambda_n/(lambda_n-1), C=M/Gamma(a),
w(y)=exp(y)g(y)/M. Finite exponential heads show w^(j)(y)=O_j(exp(-y)).
For q=exp(x)p, transfer derivatives to w, split at u=x/2, and integrate
by parts on the far half: q^(j)=C x^(beta-j)[(beta)_falling_j+O(1/x)]
for 0<=j<=4. Thus D3(p;x)=-(C^3/4)exp(-3x)x^(-9/2)[1+O(1/x)]<0
eventually. The raw determinant of [(beta)_falling_(i+j)] at beta=1/2
is 1/4. A first zero exists with D3 positive before it and derivative
at most zero. Strict negativity of that derivative is STILL OPEN.

This narrows the fixed test to transversality of its first contact.
No numerical root or full model witness has been certified. Canonical
proof and all source/regularity qualifications are retained in
C466d; this working note records the unfinished line of reasoning.
