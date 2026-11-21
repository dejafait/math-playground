# Approved annulus attempt1349 — working checkpoint

Scope is exactly assessment1347's approved annular observable. C019c,
Ono2610.38870v1 (3.2), (3.8)–(3.9), Lemma8, Lemma12/(4.3), and
the Euler-product estimates in Lemma13's proof are the retained inputs.
No Gaussian or Airy conclusion is imported. The exterior proof and
automatic-Airy failure have been read; existing work is preserved.

The exact algebra to verify is as follows. Set beta=-theta/2,
A=qr^2, C=2*kappa*r/Lambda, R=alpha/sin(alpha), z=exp(-i*beta).
Then A-1=C*R and
phi'(theta)=i*z*(U+i*V),
U=(A+1)*(cos(alpha)-cos(beta)), V=C*(R*sin(beta)-beta).
For the common eventual onset alpha<=epsilon_d/4, Lambda>=4,
epsilon_d<=theta_0, the annulus has beta>=2*alpha and beta<=1/20.
Proposed direct estimates: |phi'|>=3*theta^2/32 and
|phi''|<=2*|theta|. These avoid an unscaled O(1/Lambda) error.

Remaining before accepting: verify this differentiation and constants;
bound both a/a_s and its theta derivative using Re(1/2+w)>=4,
not the source's rescaled local C1 theorem; retain both endpoints and
both weighted remainder terms in one integration by parts. Expected
certificate is O(d^(-2/3)*epsilon_d^(-2))=O((log d)^(-2)).
This is only a working calculation, not yet a canonical result.

Independent gaps remain the local cubic comparison, its signed margin,
exceptional-root control and every-degree hyperbolicity. No conclusion
about the annular integral's lower bound or RH is asserted.

Completed: the full proof and actual bound are now canonical in
[C019d](../../lemmas/C019d-actual-jensen-shrinking-annulus-payment.md).
The above checkpoint records the pre-proof reasoning, not a separate
proof. Its expected certificate was obtained; independent audit remains.
