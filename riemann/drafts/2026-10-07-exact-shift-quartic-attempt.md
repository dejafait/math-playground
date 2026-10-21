# Exact-shift quartic attempt — reasoning checkpoint

Approved target and assessment: the unbounded-family quartic test in
`drafts/literature/2026-10-07-exact-shift-polynomial-noncoincidence.md`.
Existing unfinished work is preserved. No external source refresh is needed.

Let a>40, x=a², Δ=a²−b² and P(z)=(z²−a²)(z²−b²).
At z=a−2i, direct multiplication gives real part 16−4Δ−16x
and imaginary part 32a−4aΔ. Hence the numerator of
Re[P(a−2i)/(5/2+ia)] is
40−8x−(10+4x)Δ. Its exact zero requires
Δ=−2+30/(2x+5), giving b²=x+2−30/(2x+5)>x.

For this choice, P(a−2i)=iK(5/2+ia), where
K=32a(x+1)/(2x+5)>0. Thus the entire divided value is nonzero
and purely imaginary, rather than a zero of the shifted polynomial.
The roots are ±a, ±b, with b>a>40, and P(0)=a²b²>0.
The completion model is f(s)=((s−1/2)²+a²)((s−1/2)²+b²).
It has reflection and conjugation symmetries and the exact prescribed shift.

Finalize the algebra and quantifiers in canonical L375. This is a
pointwise-family obstruction only; each fixed polynomial has finitely
many zeros. No actual-theta arithmetic, D≤0, response Laguerre sign,
count comparison or RH consequence follows. A separate audit remains due.
