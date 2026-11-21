# Gaussian source audit1184 — saved reasoning

Approved target: coverage1183, Polson v24 Lemma7.6/(23)-(25) only.
The full source proof on printed p19 and the cited DLMF statements have
been inspected. Local comparison1183 and the finite-extension/class-bridge
stops1117/1181 are retained; this is reproduction, not a new sign mechanism.

The complex-kernel obligation can be discharged without assuming complex
Mehler convergence: form the explicit analytic right side as a function
of the disk parameter; identify its Taylor coefficients on real spatial
pairs by DLMF18.18.28; extend those entire coefficient identities in each
spatial variable; Cauchy's coefficient estimate gives compact geometric
convergence. At (z,conj(z)) the summands are nonnegative.

The finite Hermite expansion then gives (23). For (24), put d=2N-1:
r_N^(-d)=(1+1/d)^d<e and 1-r_N^2>=(3/(4N)); e<3 and pi>3 suffice.
For (25), fixed q and y>=0 permit the contour shift by a=y/6;
the vertical edges are bounded by a fixed polynomial in R times
exp(-R^2+a^2). At r=1/2, (23) gives exponent -x^2/3+3a^2;
the Fourier multiplier contributes -ya. Thus 3a^2-ya=-y^2/12,
and 2^(2N-1)*sqrt(3*pi)/(sqrt(pi)*sqrt(3/4))=4^N.
Negative y follows by conjugation; zero q and y=0 are included.

Pending at the initial save: write the complete canonical proof, check all
normalizations and limiting statements, and run scoped documentation
validation. No full Lemma7.7, explicit-formula, far-time or RH claim.

Completion1184: the exact proof and all analytic justifications are now
canonical in C030d. This preliminary note is retained as saved reasoning;
it is not a separate proof or a current next-action record.
