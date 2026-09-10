# Lemma 48: smooth even extension and monotonicity of K

**Hypotheses.** Define A(u)=e^{u/2}ψ(e^{2u}) for every real u and K(u)=2A''(u)-A(u)/2.

**Conclusion.** K is smooth, strictly positive, and even on R. K'(0)=0, K'(u)<0 for u>0, and log K is strictly concave on R. In fact (log K)''<-(68/125)πe^{2|u|}.

**Proof.** On each compact real u-interval, e^{2u} has a positive lower bound, so the differentiated theta series converges uniformly in every fixed derivative order. Thus A and K are smooth on R. The theta transformation gives ψ(e^{-2u})=(e^u-1)/2+e^uψ(e^{2u}); multiplying by e^{-u/2} yields

A(-u)=A(u)+sinh(u/2).

Differentiate this identity twice. Since (sinh(u/2))''=sinh(u/2)/4, applying 2D²-1/2 cancels the extra term and gives K(-u)=K(u). Positivity on u≥0 is Lemma 19 and extends by evenness; differentiating evenness at zero gives K'(0)=0. Lemma 47 gives the strict curvature estimate for u≥0. Evenness extends it to u≤0 with |u|. For u>0, integrate (log K)''<0 from 0 to u, using (log K)'(0)=0, to get (log K)'(u)<0 and hence K'(u)<0. ∎
