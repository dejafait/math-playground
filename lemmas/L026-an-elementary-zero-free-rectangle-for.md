# Lemma 26: an elementary zero-free rectangle for Ξ

**Hypotheses.** z=x+iy with real x,y and |y|≤1/2. J(z) is as in Lemma 20.

**Conclusion.** |J(z)|<1/72. If also |x|≤4, then Ξ(z)≠0. Consequently every Ξ zero α satisfies |Re(α)|>4 and |Im(α)|<1/2.

**Proof.** For X≥1, n²≥n implies

ψ(X)≤Σ_{n≥1}e^{-πnX}=e^{-πX}/(1-e^{-πX})≤e^{-πX}/(1-e^{-π}).

Since |cos(zu)|≤e^{|y|u}≤e^{u/2}, the substitution X=e^{2u} gives

|J(z)|≤∫_0^∞e^uψ(e^{2u})du=(1/2)∫_1^∞X^{-1/2}ψ(X)dX
≤1/[2π(e^π-1)].

Use the elementary bounds π>3 and e³>1+3+9/2+27/6=13, so 2π(e^π-1)>72, proving the strict estimate. If |x|≤4, then |z²+1/4|≤|z|²+1/4≤16+1/4+1/4=33/2. Lemma 20 gives

|Ξ(z)-1/2|=2|z²+1/4||J(z)|<33/72=11/24<1/2.

Thus Ξ(z) cannot vanish in that rectangle. Lemma 18 and strip localization put every Ξ zero in |Im(α)|<1/2; applying the rectangle result proves the final assertion. ∎
