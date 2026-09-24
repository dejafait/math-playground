# Lemma 267: an associated-kernel variance sign test

**Hypotheses.** Let k(u)=K(|u|) be the positive even theta kernel of L019 and let n≥1 be an integer. Set

A_n(t)=∫_R s^(2n)k(s+t)k(s−t)ds,
M_j=∫_R u^j k(u)du,
Z_n=Σ_(j=0)^(2n) binom(2n,j) M_j M_(2n−j),
P_n=Σ_(j=0)^(2n) binom(2n,j) M_(j+2) M_(2n−j),
Q_n=Σ_(j=0)^(2n) binom(2n,j) M_(j+1) M_(2n−j+1).

Odd moments vanish. Write Ξ(a+iy)Ξ(a−iy)=Σ D_n(Ξ;a)y^(2n).

**Conclusion.** The positive finite variance

V_n=∫t²A_n(t)dt / ∫A_n(t)dt = (P_n−Q_n)/(2Z_n)

supplies the sufficient condition

2a²V_n≤1 ⇒ D_n(Ξ;a)≥0.

It is not a necessary condition. Failure of this test says nothing about the sign of D_n.

**Proof.** The superexponential bounds in L019 make every polynomially weighted double integral absolutely convergent. Positivity of k gives positive mass and positive second moment. Under u=s+t, v=s−t the Jacobian is 1/2. Expanding (u+v)^(2n) gives

∫A_n=Z_n/2^(2n+1).

Expanding (u−v)²(u+v)^(2n), and interchanging u and v in the v² contribution, gives

∫t²A_n=(2P_n−2Q_n)/2^(2n+3).

This proves the variance formula without numerical subtraction assumptions.

By L020 the whole-line transform F(z)=∫k(u)e^(izu)du equals 2Ξ(z). Multiplying its two absolutely convergent integrals at a+iy and a−iy and extracting the y^(2n) coefficient gives

4D_n(Ξ;a)=1/(2n)! ∫∫(v−u)^(2n)k(u)k(v)e^(ia(u+v))du dv.

Replace v by −v using evenness of k and apply the same change of variables. Hence

D_n(Ξ;a)=2^(2n−1)/(2n)! ∫A_n(t)cos(2at)dt.

Coefficient extraction is justified by exponential domination on compact complex y sets, as in L020. The elementary inequality cos x≥1−x²/2 now bounds this integral below by (∫A_n)(1−2a²V_n), proving the condition. ∎

This criterion alone does not bound V_n sharply or cover L266's required indices 1≤n≤K(a). In particular, a result only for sufficiently large n would leave the lower indices unresolved.

**Mathlib.** Full statement and supporting Fourier, moment, and cosine-bound results: not checked. No library match is claimed.
