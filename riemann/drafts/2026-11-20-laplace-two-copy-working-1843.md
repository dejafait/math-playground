# Two-copy attempt1843 — working checkpoint

Approved scope: assessment1842, unchanged C034b d_j,e_j,T on [1,2].
Main gap L030-L032/C032a; local aim is the final ECT prefix, with
conditioning, weights/TV, full observations and Xi realization separate.

Candidate factors (not yet a completed proof): A=p-p(0),
B=p''-p''(0), f=A/x^2, g=B/x^2, dmu=x^2 Q_1(x) dx,
r=Q_2/Q_1. This finite positive measure avoids dividing by A.
The proposed entries are d_1=int f, d_2=int rf, e_1=int g,
e_2=int rg. Check origin removability, all four absolute products,
width differentiation and the complete double divisor sum before use.

Proposed full-T integrand: one half of
(f(x)g(y)-g(x)f(y))(r(y)-r(x))
 -(d_2-d_1)f(x)f(y)(r(x)+r(y)), integrated against mu x mu.
The cubic is retained. Test whether a pointwise ordering can control
this expression; do not assume f>=0 or divide by it. A strict full-T
margin is required for ECT. If only this identity and unpaid signs
remain, save the obstruction and park the attempt.

Existing source comparison1842 and stop1839 reused. No new source
search or mathematical script. Unfinished reasoning is preserved here;
canonical statements and the final decision will supersede this note.

Partial reasoning saved: r(t)=2(3t+2)(t+1)^2/((t+2)^2(3t+1)),
t=x^2. It satisfies 0<r<2; r>1 on x>=1 and r-1>9/10 on
x>=gamma-1>13. Thus D=Q_2-Q_1 has |D|<=Q_1, is positive
on x>=1, and exceeds (9/10)Q_1 on every retained positive core.
Reuse the entire C034b memberwise error proof, with no separate d_j
enclosures: the joint difference contributes more than
[279/320-9/20-2/125-1/10000]gamma^(-4)
=(16231/40000)gamma^(-4)>(2/5)gamma^(-4).
Consequently d_2-d_1>(2/5)S4 and the full cubic is <-S4^3/5.
This is a partial sign input, not the missing curvature bound.

The exact ratio log derivative in t has numerator 15t^2+9t-2,
so its sign changes once on t>0. Simple ordered-variable covariance
does not close. The concrete remaining sufficient inequality is
(1/2)int int (f(x)g(y)-g(x)f(y))(r(y)-r(x)) dmu(x)dmu(y)
<=S4^3/5 at every width. No bound of this strength is established.
The full integrand is strictly negative near a diagonal point where
f>0, since d_1>0 guarantees such a point; global sign still unpaid.

Completed attempt: the full proof and qualifications are now in
[C034c](../lemmas/C034c-origin-subtracted-two-copy-curvature-and-cubic-margin.md).
The initial tentative entries above remain as saved reasoning, not
additional canonical claims. The partial result awaits conceptual audit.
