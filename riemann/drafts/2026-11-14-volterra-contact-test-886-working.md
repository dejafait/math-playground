# Step886: bounded Volterra contact attempt (working)

The invocation target is exactly assessment884's retained-real-zero versus
cofactor-weighted actual-H tail test. Its prior EXPLORE approval is reused;
no new literature scope is being approved here.

Main gap: L030-L032/C032a all-degree actual-Xi algebraic-square positivity.
Intermediate target: an exact arbitrary-fixed-order spatial first-contact
forcing with a paid inward sign, using C466a's boundary density and the
retained-zero estimate. Downstream use would require separate treatment of
simultaneous contacts, compact continuation, all orders and Xi transfer.
Continue only with a strict inward sign or a proved local barrier; stop on
an uncontrolled cofactor ratio or an increasing verified-factor budget.

Inputs to inspect/reuse: C466a, L018/L024 conventions, assessment883's
Steutel--van Harn V.2.16 equation (2.23), Sra Hub v1 Lemma2.2 and
Proposition2.3, smooth zero extension, and compactly supported convolution
differentiation. L874/L611/U12 failures are contrasts, not inputs.

The symbolic calculation now has the following provisional reduction.
For A(x)=[p^(i+j)(x)], e=(-1)^(m(m-1)/2), and a contact x*, freeze
V(t)=-e tr(adj(A(x*)) A(x*-t)). Differentiating xp=H*p through the
smooth density gives H*A=xA+LA+AL^T, L_(i,i-1)=i. Taking the frozen
cofactor trace at the contact yields integral H V=0. The next derivative
gives x* D_m'=integral (-H') V after checking the singular endpoint.
Consequently any constant q may be subtracted:
x* D_m'=integral (-H'-qH)V. The retained term exp(-qt) cancels exactly
from this last forcing. These identities still require full written
endpoint and rank arguments before being treated as a result.

Proposed discriminating obstruction: D_(m-1)>0 makes the adjugate rank
one. If V vanished identically, a nonzero monic constant-coefficient
operator P(partial)^2 would annihilate p throughout (0,x*); flat initial
data would force p=0, contradicting positivity. Thus integral H V=0
with H>0 forces both signs. The scalar retained-zero lower bound cannot
be multiplied by this weight without a separate negative-part estimate.
No actual contact or failure of actual-Xi positivity is claimed.

The full endpoint, rank and normalization arguments and exact threshold
are now canonical in C466b. This working note preserves the chronology
of the attempt and is not a second proof. The scalar domination route
is stopped; the new result awaits independent audit. All existing
notebook changes are preserved. No mathematical script was needed.
