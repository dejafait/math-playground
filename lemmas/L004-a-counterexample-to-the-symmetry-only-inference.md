# Lemma 4: a counterexample to the symmetry-only inference

**Hypotheses.** Let a=1/4+i and

P(s)=(s-a)(s-conj(a))(s-(1-a))(s-(1-conj(a))).

**Conclusion.** P is an entire polynomial with P(1-s)=P(s) and P(conj(s))=conj(P(s)). It is positive on the real axis and on the critical line, but all four of its zeros lie off the critical line, inside the open strip.

**Proof.** Conjugation permutes its roots and leaves the leading coefficient real. Reflection also permutes the roots, and the four negative signs cancel. The roots have real parts 1/4 or 3/4 and imaginary parts ±1. For real x,

P(x)=((x-1/4)²+1)((x-3/4)²+1)>0.

Writing u=s-1/2 and d=1/4 gives P(s)=u⁴+2(1-d²)u²+(1+d²)². Thus, for real t,

P(1/2+it)=(t²-(1-d²))²+4d²>0.

All claims follow directly. ∎
