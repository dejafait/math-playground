# Lemma 33: the first mixed determinant in moment coordinates

**Hypotheses.** Put a=M_2/(2M_0), b=M_4/(24M_0), c=M_6/(720M_0), d=M_8/(40320M_0), all positive. The symbols here are normalized moment coefficients, not the counterexample nodes of Lemmas 29–31.

**Conclusion.**

S_3=a³-3ab+3c,

S_4=a⁴-4a²b+2b²+4ac-4d,

D:=det H_1=S_2S_4-S_3²
=a²b²-4b³-2a³c+10abc-9c²-4a²d+8bd.

For the actual Ξ, H_1 is positive semidefinite exactly when D≥0, since S_2>0 is already proved. The sign of D is not established by this lemma.

**Proof.** Set t=z². By Lemma 21, Ξ(z)/M_0=1-at+bt²-ct³+dt⁴+O(t⁵). Expand the local logarithm at t=0, justified on the zero-free disk used in Lemma 25:

log(Ξ(z)/M_0)=-at+(b-a²/2)t²+(-c+ab-a³/3)t³
+(d-ac-b²/2+a²b-a⁴/4)t⁴+O(t⁵).

Comparing with -Σ_{k≥1}S_k t^k/k gives the two new identities and S_2=a²-2b. Expanding (a²-2b)(a⁴-4a²b+2b²+4ac-4d)-(a³-3ab+3c)² gives the displayed expression for D. Finally, for real x,y,

S_2x²+2S_3xy+S_4y²=S_2(x+S_3y/S_2)²+(D/S_2)y².

Lemma 27 gives S_2>0, so this form is nonnegative for all x,y exactly when D≥0. ∎
