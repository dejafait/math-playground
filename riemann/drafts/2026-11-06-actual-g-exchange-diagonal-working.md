# Exchange-equivariant radial graphs — bounded diagonal attempt

2026-11-06. Invocation-start coverage is the unchanged EXPLORE
assessment `literature/2026-11-06-actual-g-radial-graph-full-phase.md`.
The approved target is the actual r=2,k=1 full-form graph question.
This attempt tests only its exchange-equivariant subclass, as nominated
in the supplied checkpoint. The supplied overview/DAG and assessment
were used directly. Targeted reads of L018, L775's definition/radius,
L846(3), audited L847 and the named product failure/history found no
previous completed exchange-diagonal calculation. No source refresh,
cross-notebook input, or new general existence theorem is needed for
the elementary compatibility test.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Intermediate target: an obstruction or compatible periodic diagonal
data for exchange-equivariant graphs, retaining the complete Jacobian
and all zeros. Downstream use: decide whether this coupling ansatz
merits a two-variable construction. Such data alone would not prove
graph positivity, growing-order transfer, other shifts or RH.
Test: derive K along the entire diagonal; obtain a rigorous obstruction
at explicit scope or admissible data, or stop with the exact unclosed
condition. A phase formula alone is not an advance.

## Partial calculation saved before further work

Write t=m+delta, s=m-delta and impose u_2(t,s)=u_1(s,t).
On the diagonal set h(m)=u_1(m,m), b(m)=(partial_1-partial_2)u_1(m,m),
z(m)=R exp(h(m)+im), C=R^2/G(R)^2. The real derivative matrix
has eigenvalues h'(m), b(m), so its complex determinant is
(1-i h')(1-i b), with neither factor zero for finite real data.
The candidate exact limit, to be checked in the canonical write-up, is

    K(m)=lim_delta->0 q_u(m+delta,m-delta)/delta^2
        =4 C (G(z(m))/z(m))^2 (1-i h'(m))(1-i b(m))^3.

It follows by using z_1-z_2=2 z(b+i)delta+o(delta) in L847(3),
including the minus sign in F. It requires no division by G.
Nonnegative real q implies nonnegative real K. Off the finite zeros
of G on the radial diagonal curve, K would be strictly positive.

The cubic normal factor gives genuine phase freedom. If the diagonal
curve avoids zeros of G, periodicity of the two right-half-plane
factors suggests that the winding of G(z)/z must be zero; the usual
argument principle would then require exactly one enclosed zero,
counted with multiplicity. This conditional winding observation does
not decide curves that hit zeros and is not yet a final obstruction.
Next within this attempt: handle those zeros without deleting them,
and test whether actual admissible diagonal data can pass or must fail.
Do not infer a global graph from diagonal compatibility.

## Concrete candidate and existing rigorous evaluator

The bounded candidate is the radial parametrization of |z+400|=600.
Thus r(m)=-400 cos(m)+sqrt(600^2-400^2 sin(m)^2), h=log(r/R),
and h'=400 sin(m)/sqrt(600^2-400^2 sin(m)^2). Its radii lie in
[200,1000]. A sufficient uniform test is Re(G(z)/z)>0 on that circle.
If it holds, the principal phi=arg(G(z)/z) is smooth and periodic,
|phi|<pi/2, and b=tan((2 phi-arctan(h'))/3) is finite and periodic.
The formula for K would then be strictly positive. No such bound has
yet been claimed here; a sample is not a proof.

Targeted local searches located audited L778's entire polynomial P_0,
with all 97 coefficient intervals and |G-P_0|<3.141e-48 on |z|<=1600.
Read its complete evaluator/tail argument, regularity and audit/software
qualifications. This is a reusable existing actual-G input; no new
theta quadrature, zero census or unassessed source theorem is needed.
The next calculation tests only the stated circle with that evaluator,
retaining all coefficient widths and the full uniform error. Any use
of midpoint floating point is diagnostic only; a sign conclusion needs
complete rational-parameter circle coverage by interval enclosures.

## Certified sector and remaining extension issue

The stronger Re(G/z)>0 diagnostic failed (sample minimum about
-2.202e-6), and that diagnostic is preserved. The sufficient wider
sector Re(G/z)+|Im(G/z)|/3>0 instead passed a full interval cover of
|z+400|=600: 261 accepted arcs, five retained subdivision records,
lower bound >1.4825e-8, with every coefficient width and |G-P_0| kept.
Certificate: `../scripts/actual-g-radial-graph/exchange-diagonal-certificate.json`.
This is a new application pending independent audit, not a sample proof.
The sector implies |phi|<pi/2+atan(1/3)<5pi/8. Since |h'|<=2/sqrt(5)<1,
the above definition of b is smooth, periodic and finite. The complete
K formula should give strict positivity for every m.

There is an elementary global realization of these diagonal jets:
u_1(t,s)=(h(t)+h(s))/2+(b(t)+b(s))sin(t-s)/4 and u_2(t,s)=u_1(s,t).
It must not be mistaken for a positive torus. At (t,s)=(0,pi),
h'=b=0 at both endpoints, so Du=0 and z_1=-z_2=sqrt(200000).
Consequently q/C=-G(sqrt(200000))G(-sqrt(200000))/50000.
L778's zero count would make this strictly negative; the same evaluator
can check it directly. This is a failure of this particular extension,
not of the admissible diagonal data or of all exchange-equivariant graphs.
Complete certificate consistency checks and the canonical proof remain
to be written before closing the attempt.

## Completion

The full proof, sources, qualifications and certificate interpretation
are now canonical in L848. The interval sector margin is >14/10^9,
and the constructed data give K/C>4e-16 at every m. The particular
global extension has -4.546e-8<q(0,pi)/C<-4.545e-8. All 261 saved
arcs and all 97 inherited coefficient intervals were processed by
the exact saved-data checks, with no failures. This validation does
not independently regenerate the Taylor jets; the result awaits a
separate conceptual audit. The earlier winding idea was not used
or promoted to a theorem. No global positive graph was constructed.
The next assessment is a REVIEW_REQUIRED audit nomination, distinct
from the ready coverage used for this completed mathematical attempt.
