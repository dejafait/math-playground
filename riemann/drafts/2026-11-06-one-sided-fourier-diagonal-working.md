# Fourier/diagonal period attempt: working checkpoint

Invocation target and prior EXPLORE coverage:
`literature/2026-11-06-one-sided-fourier-diagonal-period-test.md`.
Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
Intermediate test: derive K>=-|M|, or a precise new obstruction to
this threshold, for L868's full C1 class and L847's actual F.
No extra radial growth, regularity or feasible-approximation assumption.
L868 and the relevant L847 hypotheses/compact homotopy were read;
the named one-sided attempts and histories contain no completed test.
The ready primary Fourier/differentiation coverage is reused.

Unfinished calculation: write S=q+h and take angular coefficients
with exp(-i n.y). Compact C1 differentiation and periodic integration
by parts give partial_xj r_n=i n_j q_n and
partial_xj S_n=-i n_j r_n. The zero mode gives r_0 constant and
S_0=K, but does not itself bound K. For n!=0 the coefficients should
reduce to a one-dimensional radial profile along n.x; check that
reduction at C1 without assuming second classical derivatives of
the original functions. The actual diagonal is x1=x2 AND y1=y2.
Any diagonal reconstruction must use the approved Fejer limits,
not an assumed absolutely convergent double Fourier series.

Continuation test: retain original domination and h>=0 while testing
whether characteristic mode restrictions and the diagonal yield the
sharp period inequality. Identities with an unpaid zero mode alone
do not qualify as a successful period estimate. This is an unfinished
working record, not a canonical proof or a completed outcome.

Intermediate checkpoint: nonzero modes have S_n(x)=B_n(n.x),
r_n=i B_n', q_n=B_n'', h_n=B_n-B_n''. These derivatives are
derivatives of one-variable coefficient profiles, justified by the
first-order equations; they do not assume C2 original coefficients.
Product Fejer diagonal averages show A=mean q(s,s,.) is constant:
the modes (k,-k) are independent of s, and the diagonal average
vanishes. Consequently H=K-A=mean h(s,s,.)>=0 is constant.
For n1+n2!=0 every n.x is attained on x=(s,s), so positivity gives
the global coefficient bound |h_n(x)|<=H. If H=0 these modes vanish.
This is a candidate compatibility restriction, not yet an audited
result. It still leaves A, H and the resonant modes uncontrolled
at the numerical threshold K>=-|M|. The pure Fourier/diagonal
period attempt must not be repeated unchanged on these identities.

Completion: the full calculation, citations and qualifications are
now canonical in C868a, awaiting an independent audit. The completed
step is EXPLORATION: no demonstrated control of K at -|M| and no
strict-gain certificate. The attempt note records the unchanged-method
stop. This draft preserves the unfinished state rather than serving
as a second proof source.
