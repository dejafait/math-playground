# Lemma 19: the theta boundary derivative and a positive kernel

**Hypotheses.** u≥0, A(u)=e^{u/2}ψ(e^{2u}), and K(u)=2A''(u)-A(u)/2.

**Conclusion.** A'(0)=-1/4, and

K(u)=Σ_{n≥1}[8π²n⁴e^{9u/2}-12πn²e^{5u/2}]e^{-πn²e^{2u}}>0.

A, A', A'', and K decay faster than e^{-Bu} for every fixed B>0 as u tends to infinity.

**Proof.** Differentiate θ(x)=x^{-1/2}θ(1/x) at x=1, justified by Lemma 16. This gives 2θ'(1)=-θ(1)/2, hence ψ'(1)=-(1+2ψ(1))/8. Therefore A'(0)=ψ(1)/2+2ψ'(1)=-1/4.

Put x=e^{2u}. Differentiating gives

A''(u)=e^{u/2}[ψ(x)/4+6xψ'(x)+4x²ψ''(x)],

so K(u)=e^{u/2}[12xψ'(x)+8x²ψ''(x)]. The differentiated series in Lemma 16 gives the displayed formula. Each summand equals 4v(2v-3)e^{u/2}e^{-v} with v=πn²e^{2u}≥π>3/2, so every summand is positive. The elementary bound π>3/2 is sufficient. Lemma 16 bounds |A|, |A'|, |A''|, and |K| by C e^{9u/2}e^{-πe^{2u}} on u≥0, with a suitable finite C. For any fixed B this bound times e^{Bu} tends to zero and is integrable: e^{2u} eventually dominates any linear multiple of u. ∎
