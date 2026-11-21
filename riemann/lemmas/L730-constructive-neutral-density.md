# Lemma 730: constructive density of neutral arithmetic vectors

## Hypotheses

Let H=L²((1,∞),dy/y²), with inner product linear in the first entry.
For integers m≥2 use the definitions from L729:

    rho_m(y)=floor(y/m)-floor(y)/m,
    a_m=(m-1)/(2m),       f_m=rho_m+a_m,
    K_m(t)=∫_t^∞ f_m(y)dy/y²,       T_m(n)=sum_(j≥1)K_m(jn).

Let V_K=span_C{rho_2,...,rho_K}, D=union_(K≥2)V_K, and V=closure_H(D).
For a finite complex combination u=sum c_m rho_m set

    A(u)=sum c_m a_m,       B(u)=sum c_m T_m(1),
    W_K={u in V_K:A(u)=B(u)=0}.

These functionals are defined on D only. Their well-definedness and
the absolute convergence defining T_m are justified below. No extension
of A or B to V is assumed. No RH, simplicity, prime representer,
whole-step-space density or uniformity over a moving unit ball is assumed.

## Conclusion

The neutral spaces are nested and

    closure_H(union_(K≥2)W_K)=V.

More precisely, for every fixed M≥2 and fixed u in V_M, for every
sufficiently large integer K put R=floor(K/2)>M and S=K. There are
unique complex alpha_K,beta_K satisfying

    alpha_K a_R+beta_K a_S=A(u),
    alpha_K T_R(1)+beta_K T_S(1)=B(u).

Then u_K=u-alpha_K rho_R-beta_K rho_S belongs to W_K and, with an
absolute constant C independent of u,M,K,

    ||u-u_K||_H ≤ C (|A(u)|log K+|B(u)|)/sqrt(K) →0.

The onset may depend on M. The determinant is eventually at least
log(2)/8, through both even and odd K.

This is a local verification of bramble_trace, *Fixed and growing
neutral gradients of the anchored Selberg–Möbius approximant*, rStation
paper 18, displayed v3, 22 October 2026, (27)--(28),(33),(43)--(44):
https://rstation.ai/problems/riemann_hypothesis/papers/18 .
The primary definitions and these complete proof passages were inspected
on 2026-11-03. The manuscript is unreviewed. The replay is warranted
because this input was not audited in L729 and because separate
unboundedness of two functionals does not prove common-kernel density.
The endpoint is verified by finite sums and the standard named
Stirling formula instead of importing the source's contour argument.
No estimate beyond the cited source is claimed.

## Proof

### Definitions and the conditional endpoint

L729 proves, without requiring neutrality for these facts, that the
primitive F_m(t)=∫₀^t f_m(y)dy is bounded and periodic, that
|K_m(t)|≤m/(8t²), and hence that T_m(n) converges absolutely. It also
proves the finite jump inversion

    c_m=sum_(d|m)mu(d)Delta u_(m/d),       m≥2,

where u_j is the cell value on [j,j+1), u_0=0, and the jump at j=1
is included. If a finite combination is zero in H, every positive
cell has zero value, so the inversion gives c_m=0 for every m≥2.
The generators are therefore linearly independent over C. In
particular A and B are well defined on D and do not change when a
coefficient list is padded with zeros. It follows that W_K⊂W_(K+1).
Each W_K is a linear subspace of the finite-dimensional V_K and is
closed; this makes no assertion about continuity on V.

For fixed m, boundedness of F_m justifies the ordinary improper
integral ∫₁^∞f_m(y)dy/y. Indeed, for X>Y≥1, integration by parts gives

    ∫_Y^X f_m(y)dy/y
      =F_m(X)/X-F_m(Y)/Y+∫_Y^X F_m(y)dy/y².

Writing P_m=sup|F_m|, the absolute value is at most 2P_m/Y.
Thus the integral converges; it is not declared absolutely convergent.

For an integer q≥1, finite cell summation gives

    ∫₁^(mq) floor(y/m)dy/y=q log q-log(q!),
    ∫₁^(mq) floor(y)dy/y=mq log(mq)-log((mq)!).

For example, the first formula follows from
sum_(r=1)^(q-1)r log((r+1)/r); it also holds at q=1. Consequently

    ∫₁^(mq) f_m(y)dy/y
      =-q log m-log(q!)+(1/m)log((mq)!)+a_m log(mq).

The standard Stirling formula

    log(n!)=(n+1/2)log n-n+(1/2)log(2pi)+o(1)

as integer n→∞ shows, at fixed m, that the last expression tends to
(log m)/2-a_m log(2pi). In this substitution the coefficient of log q
is -1/2+1/(2m)+a_m=0; the surviving log m coefficient is
1/(2m)+a_m=1/2. The already proved improper convergence permits the
subsequence mq and gives the endpoint identity

    ∫₁^∞ f_m(y)dy/y=(log m)/2-a_m log(2pi).          (1)

This establishes source equation (27) without an Abel-limit or Mellin
interchange. The required standard input is Stirling's formula; no
zeta-zero estimate or source representer theorem is used.

The finite summation identity in L729, at n=1 and any integer Y≥1, is

    ∫₁^Y floor(y)f_m(y)dy/y²
      =sum_(j≤Y)K_m(j)-Y K_m(Y).

The sum converges absolutely and the last term tends to zero. Thus
the left side tends to T_m(1), even though that integral is only
conditionally justified. For each finite Y use floor(y)=y-{y}.
The integral of {y}f_m(y)/y² is absolutely convergent since both
factors are bounded. Equation (1) therefore implies

    T_m(1)=(log m)/2-a_m log(2pi)-∫₁^∞{y}f_m(y)dy/y².

For integer J≥1 the exact identity

    ∫₁^J {y}dy/y²=log J-H_J+1

follows by integrating floor(y)=sum_(j≤J)1_(y≥j). The defining limit
gamma=lim_(J→∞)(H_J-log J) gives ∫₁^∞{y}dy/y²=1-gamma.
Putting c_0=1+log(2pi)-gamma and
h_m=⟨{y},rho_m⟩_H, which is real, proves source equation (28):

    T_m(1)=(log m)/2-c_0 a_m-h_m.                  (2)

Only a fixed-m limit was used in Stirling's formula. Equation (2) is
then exact for every m; the uniform bounds below do not require a
uniform asymptotic in that earlier limit.

### Generator norms and determinant separation

For 1≤y<m, rho_m(y)=-floor(y)/m, so |rho_m(y)|≤y/m.
For y≥m, write rho_m(y)={y}/m-{y/m}; hence |rho_m(y)|≤1.
It follows that

    ||rho_m||²≤(m-1)/m²+1/m≤2/m.

Since ||{y}||_H≤1, Cauchy–Schwarz gives |h_m|≤sqrt(2/m).
Equation (2) consequently proves, uniformly for m≥2,

    T_m(1)=(log m)/2-c_0/2+e_m,
    |e_m|≤|c_0|/(2m)+sqrt(2/m).                    (3)

In particular |T_m(1)|≤C_1 log m with an absolute constant C_1.

For R=floor(K/2), S=K, let
Delta_K=a_R T_S(1)-a_S T_R(1). Using the exact identity (2)
cancels the c_0 a_R a_S terms and yields

    Delta_K=(1/4)log(S/R)-log S/(4R)+log R/(4S)
                     -a_R h_S+a_S h_R.

The absolute difference from (1/4)log(S/R) is at most

    log S/(4R)+log R/(4S)
                 +(1/2)sqrt(2/S)+(1/2)sqrt(2/R),

which tends to zero. For even K the ratio S/R is 2; for odd K it
is 2+1/R. Hence Delta_K→log(2)/4>0 along all integers K, and for
every sufficiently large K it is at least log(2)/8. This is an
eventual lower bound, not a numerical claim about its onset.

### Complex repair and fixed-vector closure

Fix u in V_M, so A=A(u) and B=B(u) are fixed complex scalars.
Take K beyond the determinant onset with R>M. Cramer's rule gives

    alpha_K=(A T_S(1)-a_S B)/Delta_K,
    beta_K=(a_R B-A T_R(1))/Delta_K.

All matrix entries are real, but the equations and this solution are
complex linear; no conjugation of A or B occurs in the constraints.
The preceding determinant bound, a_R,a_S≤1/2 and (3) give

    |alpha_K|+|beta_K|≤C_2(|A|log K+|B|)

with an absolute C_2. Direct substitution into A and B shows
u_K=u-alpha_K rho_R-beta_K rho_S belongs to W_K. Since R≥K/3
for K≥3 and S≥R, the triangle inequality and the generator norm bound
give

    ||u-u_K||≤sqrt(2/R)(|alpha_K|+|beta_K|)
             ≤sqrt(6) C_2 (|A|log K+|B|)/sqrt K →0.

The limit holds because u, A and B are fixed. No bound on A or B
over the H-unit ball is used or inferred.

Every u in D is therefore in closure_H(union W_K). Closing this
inclusion gives V⊂closure_H(union W_K). The reverse inclusion follows
from W_K⊂V_K⊂V and closedness of V. This proves the conclusion. ∎

The result retains all fixed arithmetic directions under neutral
approximation. It does not identify V with the entire unit-cell step
space, control the complementary residual, identify Q with a prime
representer, improve L729's growing-support bound, or prove any Xi
sign or RH. Density here supplies no uniform convergence on the unit
ball and no full residual-norm estimate.

## Mathlib

Full matching theorem: not checked; availability is unknown. The
finite jump inversion from L729, Stirling's formula, finite-dimensional
linear algebra, Cauchy–Schwarz and closure arguments are supporting
inputs. No exact Mathlib declarations were verified in this step and
no absence claim is made. Documentation index:
https://leanprover-community.github.io/mathlib4_docs/ .
