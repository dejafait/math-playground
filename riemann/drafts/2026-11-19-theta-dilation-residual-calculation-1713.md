# Arbitrary theta dilation: bounded calculation1713

Saved working reasoning under the pre-existing SPECIALIZE assessment1712.
Target: its exact quadratic/cubic uniform-scale diagnostic. This is a
known-method specialization, not a new general companion theorem.

Write a=binom(d,2)S_2, b=2binom(d,3)S_3, T=T_(d-1),
beta=beta_(d-1), gamma=beta_(d-2). At scale s>0 the candidate exact
residuals are alpha_(d,d-2)=s^2*T-a and alpha_(d,d-3)=b.
Evenness eliminates the reference's cubic and the quadratic basis
polynomial's next coefficient. The norm ratios should be
1/(s^2*beta) and 1/(s^4*beta*gamma), respectively.

Put t=s*sqrt(T)/d, A=a/d^2, B=b/d^3. The retained squared diagnostic
divided by d^2 becomes

    (T/beta)*(t^2-A)^2/t^2
      + (T^2/(beta*gamma))*B^2/t^4.

Since T>=beta+gamma, the prefactors are at least 1 and 4.
For d>=3, A<=S_2/2 and B>=2S_3/27. Split t^2>=S_2 or
t^2<=S_2. The first case should give S_2/4 from the quadratic;
the second gives 16*S_3^2/(729*S_2^2) from the cubic. Both are
positive and independent of degree and scale. Need finish checking
the actual Cholesky coordinates and all summands, including d=3,
before promoting this to a canonical result. No numerical evidence
is used. Actual H_d=o(d), signed cancellation and output realization
are not proved; a lower bound on the upper cost never reverses
H_d<=K_d(s).

Finalized in C028p after checking these coordinates, residuals, norm
ratios and both scale cases, including d=3. This saved working note
is not the canonical proof; the canonical result awaits a separate audit.
