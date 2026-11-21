# Gaussian resolvent attempt1579 — working record

Approved target: assessment1577's subtracted even zero-pair identity and
uniform spectral tail on sigma in [1,2], |w|<=2. Main gap remains
L030-L032/C032a actual-Xi positivity. Success needs both the removable
identity and a vanishing explicit tail; numerical data and the residual
test are outside this attempt. Reuse notes1577; preserve stops1571/1576.

Partial derivation saved before the infinite-tail work: put a=gamma-i*delta,
k=2*sqrt(sigma), W(z)=exp(-z^2)*erfc(-i*z), D(z)=W(z)-exp(-z^2).
D is odd by DLMF7.4.3. For the single pair
f_a(x)=[G_sigma(x-a)+G_sigma(x+a)]/2, the proposed formula is

    r_a(w)=sqrt(pi)/(8*sqrt(sigma)*w)
            *[D((i*w-a)/k)+D((i*w+a)/k)],
    e_a(w)=sqrt(pi)/(2*sqrt(sigma))*integral_0^w
            [D((i*t-a)/k)+D((i*t+a)/k)] dt.

Derive the first identity initially on Re(w)>|Im(a)| by shifting
the Gaussian contour without crossing either pole and importing
DLMF7.7.2. The lower pole needs reflection of the integration variable.
The subtraction contributes the two exponential terms with exactly the
same prefactor. The numerator is entire and odd in w and vanishes at
zero; continuation must agree with the entire removable quotient.
These formulas are still being checked, not approved results.

Tail plan: apply C032m's quotient domination pair by pair with M=2,
X=5 and D0=sqrt(26). The compact part has an exponentially small
bound in gamma-D0; the spatial part also contributes gamma^(-2).
Use the imported Hasanalizade-Shen-Wong v1 Corollary1.2 to obtain an
explicit count bound, sum these three positive envelopes, and multiply
the R tail by8 along the full straight E primitive path. Include cutoff
zeros in the finite part. Finite coordinates and their certification
remain absent. C032q is downstream context, not an analytic premise.

Completed in this turn: the full derivation, constants, domination,
cutoff convention and finite-input interface are canonical in
[C032y](../lemmas/C032y-gaussian-resolvent-pairs-and-uniform-spectral-tail.md).
Both approved analytic obligations were met in the written proof; an
independent conceptual audit remains pending. This working snapshot is
retained as the pre-tail checkpoint, not a second current proof or an
approval of numerical use. No mathematical script or zero data was used.
