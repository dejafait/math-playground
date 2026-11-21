# Signed index-five calculation — step480 working record

Approved target: Test the signed index-five residual against the
root-preserving coefficient interval of L791's fixed central degree-five model.
Reuse the supplied SPECIALIZE assessment dated 5 November 2026.

Main gap: actual-Xi all-degree mixed positivity. Intermediate output is
the signed index5 residual and distances to both collision boundaries
at the exact L791 solution, keeping its full box and L778 coefficient
errors. A finite margin can inform later residual control but gives no
growing-degree bound. Stop this transfer on strict necessary-bound
violation; enclosure failure is inconclusive. Do not change degree or D.

Inputs read: L791 in full; L778 evaluator definition and bounds (2)–(5),
including its complete coefficient-error rule; existing fixed-model and
rational-audit scripts. Existing unfinished work is preserved.

Planned normalization: t_actual=R5/(B R1)^5>0, t_model=-p5>0.
Q(x)=x^5+p1*x^4+p2*x^3+p3*x^2+p4*x-t. Let f=Q+t.
For ascending critical points x1<x2<x3<x4, Pereira Lemma1.1
gives max(f(x2),f(x4))<=t<=min(f(x1),f(x3)).
Strict interior plus t>0 gives five simple positive reciprocal roots.
The signed coefficient residual is -(t_actual-t_model).
The completed calculation is canonical in L792. It finds positive
delta in (2.94347417497914061298e-10,2.94347417514615466953e-10),
with both actual collision distances greater than4.5e-9. All four
critical points and their values are enclosed on the original box.
The first run's only failure was a harness assertion demanding the
opposite residual sign. Its complete certificate is preserved; the
assertion now certifies the observed sign without prescribing one.
Final evidence: `scripts/central-jacobi/signed-residual-certificate-480.json`,
140 checks, no failures. No degree/parameter change was made.
