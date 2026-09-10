# Lemma 20: entire Fourier cosine representation of Ξ

**Hypotheses.** z∈C and K is as in Lemma 19.

**Conclusion.** Ξ(z)=∫_0^∞K(u)cos(zu)du. This integral and its derivatives of every fixed order converge locally uniformly in z.

**Proof.** In I(1/2+iz), put x=e^{2u}; Lemma 17 gives I(1/2+iz)=4J(z), where J(z)=∫_0^∞A(u)cos(zu)du. Consequently Lemma 18 yields

Ξ(z)=1/2-2(z²+1/4)J(z).

For z in a compact set |z|≤R, |cos(zu)| and |sin(zu)| are at most e^{Ru}. Lemma 19 makes A, A', A'', and K times this bound integrable and makes all boundary terms at infinity vanish. The same holds after multiplying by any fixed power of u, so dominated differentiation proves local uniform convergence of every derivative.

Integrating twice by parts gives

∫_0^∞A''(u)cos(zu)du=-A'(0)+z∫_0^∞A'(u)sin(zu)du=-A'(0)-z²J(z).

At u=0 the first boundary term is -A'(0), while the second is zero because sin 0=0. It follows that

∫_0^∞K(u)cos(zu)du=-2A'(0)-2(z²+1/4)J(z)=Ξ(z),

using A'(0)=-1/4. All steps hold directly for complex z; no unsupported contour movement or extension of a real inequality occurs. ∎
