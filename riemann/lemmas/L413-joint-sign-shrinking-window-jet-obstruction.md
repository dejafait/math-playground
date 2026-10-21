# Lemma 413: joint signs do not force a shrinking-window pencil margin

## Hypotheses

This is a generic pointwise ordinary-six-jet test, not an assertion about
the actual functions F_0 and G. Fix c>0, alpha>1/4, and arbitrary finite
nonnegative remainder constants C_0,C_1,C_2. At t=T-1, T>=41, put
L=log(T+1). Use L367's normalized ordinary jets P_j,V_j and its exact
definitions of ell, Bcal, Ccal, X_j and E_H, and L370's discriminant
Delta=Bcal^2-4 ell Ccal. The growth hypotheses tested are
|P_j|<=E_j sqrt(T)L^(-j), |V_j|<=D_j, with fixed positive finite
constants, and Ccal>=c. Only these forms, not the actual family's
unevaluated constants or arithmetic identities, are imposed.

## Conclusion

There are fixed compatible constants and real six jets at every
sufficiently large real T satisfying ell>=0, Bcal<0, Delta>0 and Ccal=c,
but for every 0<delta<=T^(-alpha),

    ell+delta Bcal+delta^2 Ccal >= 1/4 > -E_H(delta).

Thus these hypotheses do not imply L367's sufficient negative-margin
event on this interval, even if its remainder were zero. This does not
decide actual joint-sign occurrence, actual clipped means, any physical
margin, or RH. The separate step-137 critical audit below validates this
partial obstruction in precisely the stated generic scope.

## Proof

Write s=sqrt(c)>0 and choose, in j=0,1,2 order,

    P=(1,0,-1),       V=(0,s,3s).

Direct substitution into L367's definitions gives

    ell=0^2-1*(-1)=1,
    Bcal=2*0*s-1*3s-(-1)*0=-3s,
    Ccal=s^2-0*3s=s^2=c,
    Delta=9s^2-4s^2=5s^2>0.

These are compatible six jets rather than three independently assigned
coefficients. For completeness L370's zero-safe minor expression is
(3s)^2-4(s)(s)=5s^2, the same discriminant.

Choose E_0=E_1=E_2=1 and D_0=1,D_1=s,D_2=3s. All are positive and
independent of T and delta. Since log(T+1)^2/sqrt(T) tends to zero,
there is a finite T_g>=41 such that L^2<=sqrt(T) for every T>=T_g.
Then |P_0|=1<=sqrt(T), P_1=0 satisfies its bound, and
|P_2|=1<=sqrt(T)/L^2. The V bounds hold identically. No special relation
between c and the C_j is needed. These choices do not purport to be the
constants of the actual zeta family.

They are ordinary derivative data. For any positive A_T, the real
polynomial germs at t=T-1

    F_T(x)=A_T[1-L^2(x-t)^2/2],
    G_T(x)=A_T T^2[s L(x-t)+(3s/2)L^2(x-t)^2]

have precisely the six normalized derivatives specified above at t.
A_T may be the positive envelope value A(t); derivatives of the
envelope are not used as normalized jets. These germs establish local
compatibility only, not realization by one fixed global pair or by the
actual response relation. For each chosen epsilon=delta/T^2 the
ordinary derivatives of F_T+epsilon G_T are taken with epsilon fixed.

Take T>=T_*:=max(T_g,(4s)^(1/alpha)). This is a fixed finite onset.
For every 0<delta<=T^(-alpha), let u=s delta. Then 0<u<=1/4 and

    q(delta)=1-3u+u^2 >= 1/4+u^2 >= 1/4.

This includes the upper regulator endpoint. The excluded endpoint
delta=0 is not used; its continuous value would be q(0)=1. Also
delta<=1 and epsilon=delta/T^2<=1/(1+t^2), so the original regulator
domain in L367 is respected. Although alpha>1/4 is the approved domain,
the displayed obstruction works for every fixed alpha>0.

Retain the entire error, with X=(1,s delta,-1+3s delta). Since
u<=1/4, its exact expression on this whole interval is

    E_H(delta)=delta^2[2 C_1 s delta+C_2+C_0(1-3s delta)]
               +delta^4(C_1^2+C_0 C_2) >= 0.

In particular q(delta)+E_H(delta)>=1/4 everywhere in the allowed
interval, for arbitrary fixed nonnegative C_j; no small-error or
relative-error inference is needed. The forbidden event q<-E_H never
occurs. A universal implication with ell>=0 must apply to ell=1, so
this counterexample refutes it without making any assertion about the
separate boundary subclass ell=0.

For comparison, the two roots of this example's pencil are
(3-sqrt(5))/(2s) and (3+sqrt(5))/(2s), fixed positive numbers. The
negative interval therefore remains at a fixed scale while the allowed
upper endpoint tends to zero. This explains the downstream limitation:
a joint-sign theorem alone needs additional quantitative information
placing a negative interval inside the regulator window, followed by
comparison with the full error. No such actual-family information is
proved here.

This is elementary reproduction within the saved EXPLORE assessment
drafts/literature/2026-10-15-shrinking-pencil-joint-sign-test.md, not a
claim of originality. Its cited general constrained-quadratic input is
Boyd--Vandenberghe, *Convex Optimization* (2004, corrected seventh
printing 2009), Section 4.2.3, (4.21), pp. 139--140, Example 4.5,
pp. 140--141, and Section 4.4, (4.34), p. 152:
https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf.
No general optimization theorem needs reproof or is used to assert
convexity of q+E_H; the explicit compatible jets require direct checking.

### Critical audit, 2026-10-15, step 137

The complete proof survives independent checking against L367 (1)--(3),
(9), (15) and L370 (3). The normalized ordinary derivatives of the
displayed germs are exactly P=(1,0,-1), V=(0,s,3s): their first
derivatives are 0 and A_T T^2 s L, and their second derivatives are
-A_T L^2 and 3A_T T^2 s L^2. The factors A_T,T,L are fixed parameters
of each germ, not functions differentiated in that construction.
Consequently these are legitimate pointwise jets even when A_T is
chosen to equal the actual positive envelope at the comparison point.
They do not prescribe the jets of F/A. For a fixed chosen epsilon,
division of F_T^(j)+epsilon G_T^(j) by A_T L^j gives X_j=P_j+delta V_j
without any regulator-curve derivative.

Independent multiplication gives ell=1, Bcal=-3s, Ccal=s^2 and
Delta=5s^2. The three normalized minors in L370 (3) are respectively
3s, s, s, confirming the same Delta with no division by V_0=0.
For the growth bounds, L^2/sqrt(T) tends to zero on the real ray,
so the definition of this limit supplies one T_g valid for every
real T>=T_g, not just a sequence. The chosen E_j,D_j are strictly
positive and depend at most on c; none depends on T, delta or the
arbitrary fixed nonnegative C_j. The conclusion is existential in
these growth constants, as stated, rather than universal in prescribed
actual-family constants.

Since T>=41 and alpha>1/4, delta<=T^(-alpha)<1. The onset condition
T>=(4s)^(1/alpha) implies s delta<=1/4 even when 4s<1; the other
onset T_g already ensures T>=41. Thus 1-3s delta>=1/4 on the entire
interval, including its upper endpoint. Adding s^2 delta^2 proves
q>=1/4. Also epsilon=delta/T^2<=1/T^2<=1/(1+(T-1)^2), as required.
The excluded endpoint delta=0 is not needed, nor is attainment of a
minimum on a half-open interval invoked. The case ell=0 is not covered
by this example; ell=1 suffices to refute the stated ell>=0 implication.

Finally X_0=1, X_1=s delta>0 and X_2=-1+3s delta<=-1/4. Substituting
these signs into every absolute value in L367 (2) gives exactly the
displayed E_H, including delta^4(C_1^2+C_0 C_2). Each summand is
nonnegative for every allowed regulator and arbitrary fixed finite
nonnegative C_j, including all C_j=0. Hence q+E_H>=1/4 throughout;
no asymptotic smallness of E_H is used. The fixed positive roots quoted
in the proof agree with the quadratic formula and describe only the
unperturbed pencil, not a convexity claim about q+E_H.

No correction to the statement, constants or dependency edges is needed.
This verifies the existing elementary obstruction, not a new theorem
beyond the sources checked. The actual response asymptotic of L368,
actual moment laws, a fixed global realization and all actual-family
sign and margin assertions remain outside its hypotheses.

## Mathlib

Full matching result: not checked. The proof uses real polynomial
algebra and elementary logarithmic growth; supporting Mathlib theorem
coverage was not checked. Unknown coverage is not evidence of absence.
