# Separated chamber/pair comparison1084 — saved reasoning

Invocation-start nomination1078/review1079 is EXPLORE for the exact
unchanged chamber-incidence/necessary-trace/fixed-pair compatibility
target. This is one RESEARCH proof_attempt/development. Reuse its
source coverage; no generic literature refresh or cross-notebook input.

Main gap: L030–L032/C032a actual-Xi all-degree algebraic-square
positivity. The intermediate test compares C467z's forced separated
trace T_c with C467p's fixed phi_p retained by C467y. Exact equality
with controlled errors supports this interface; one strict discrepancy
at fixed h>0 stops this fixed selection on every positive horizon.
The incoming h=O(t^2) layer from C467 is not forced by initial data.

Inputs read: C467z(1)–(16), C467p hypotheses/(19)–(26)/(32)–(36),
C467y hypotheses/(2), and audit1083's saved reasoning and stop1081.
Further needed ranges will be read before any load-bearing use. Keep
all original constants, actual B/beta/H/H0/F, raw time, divisor,
common minus sign, arbitrary allowed asymmetric f and inherited
finite-zero/product qualifications. No C467s or unknown scalar jet
is assumed. Existing unfinished work is preserved.

Initial mechanism to test: compare both physical graph momenta near
a separated lower double root, using v=(Q2-Q1)/2 and the common
endpoint v^2=2t+O(t^2). The pair graph linearly interpolates its
lower endpoint momenta; the chamber graph has their full curvature.
Their equality on the moving endpoint does not identify their time
or normal graph derivatives. A transport expansion must retain those
terms and integrate the discrepancy along the earlier-time paths.
At present no order, coefficient or strict mismatch is established.

Independent gaps remain: corner incoming data, integrability of a
chamber identity, all other interfaces/exterior payment, realization,
higher degrees and Xi transfer. No RH candidate is claimed.

## Intermediate calculation, still being checked

At fixed positive singleton separation use Q=(m-v,m+v,y), w=v^2.
Write a(z)=Re g(iz), j(z)=Im g(iz), k=tan(sum Im beta(iQ_j)).
The actual chamber graph has p_c=t A+O(t^2), A_j=-a(Q_j).
The pair graph interpolates the chamber graph at the two moving lower
endpoints w=w0(t,m,y), where w0=2t+O(t^2). Smooth lower-slot parity
therefore gives p_p-p_c=t(w-w0) B(t,Q). At t=0,
B1=[a(m-v)-a(m)+a'(m)v]/v^2,
B2=[a(m+v)-a(m)-a'(m)v]/v^2, B3=0, with smooth limits at v=0.
Thus B(x,0,y)=(a''(x)/2,a''(x)/2,0).

The velocity connection for an arbitrary small real graph p and graph
variation U is
  A_p(U)=k U-Dp U+(1+k^2)(div p+d dot p)U+O(p^2 U),
where d_j=2 sum_(l!=j)1/(Q_j-Q_l)+j(Q_j). Only lower-equivariant
graphs/variations are used; the lower inverse gap cancels. Its curvature
at p=0 is
  C(U,V)=(1+k^2)[DV U-DU V+(div U+d dot U)V
                 -(div V+d dot V)U]
            +k[(grad k dot U)V-(grad k dot V)U].
The n=1 specialization vanishes, a useful sign/cancellation check.

For the interpolation p_lambda=p_c+lambda(p_p-p_c), the terminal
point lies where p_p=p_c; the initial graphs also agree. The backward
endpoint variation is consequently the integral of C(A,p_p-p_c)
to leading order. The direct k partial_t(p_p-p_c) contribution has
zero net endpoint displacement, explaining the failed t^2 diagnostic.

Candidate next coefficient: for fixed (x,h>0), terminal w=2t+O(t^2),
the endpoint difference is t^3 K(x,h)+o_h(t^3), with
 K=C(A,B)/3+(1+k^2)[-2a'(x)B-a'''(x)A/3]
evaluated at Q=(x,x,x+h). The 1/h part is solely
C(A,B)=4(1+k^2)B1 A/h+O(1) as h decreases to zero.
Hence the proposed scalar coefficient obeys
 h lim_(t->0)(phi_p-T_c)/t^3
   -> -2(1+tan^2(3 Im beta(ix)))a(x)a''(x)f(x)^2 f'(x).
For a positive transition point of any allowed f, C467u's actual signs
would make this strictly positive. This is not yet a final claim:
check the interpolation factor, curvature orientation, boundary terms,
uniform lower-gap cancellation and the sequential-limit remainder.

## Completed bounded attempt

The full proof is now canonical in C468, equations(1)–(29), with
all input qualifications and Mathlib status. The interpolation factor,
two endpoint cancellations, exact variational sign, first-order
bilinear curvature estimates and the fixed-h O(t^(7/2)) remainder
are supplied there. Equation(29) isolates the sole separation pole;
the other coefficient terms remain bounded as h decreases to zero.
Selecting h first and time second gives the strict scalar mismatch
at every allowed bump's positive transition point.

Outcome NEGATIVE: a proposed stop of the fixed lower chamber/pair
match, pending independent conceptual audit; no claim that every
coupled selection fails, and no RH candidate. Classification is
POTENTIALLY_NEW within the bounded recorded comparison, not certified
originality. No mathematical script or new external source was needed.
The partial calculations above are preserved, with their provisional
status superseded only by the canonical proof, not by an independent
audit. The newly nominated audit remains REVIEW_REQUIRED for a
separate source-approval turn; no same-turn gate approval is made.
