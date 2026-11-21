# Corollary 868a: diagonal mean constancy bounds the nonresonant correction modes

## Hypotheses

Retain exactly L868(1),(3)-(5): the actual coefficient

\[
F(z_1,z_2)=-C G(z_1)G(z_2)(z_1-z_2)^2/(z_1^2z_2^2),
\quad z_j=R e^{x_j+i y_j},
\]

and real C1 functions q,r,h on R2 times the angular torus T2,
2pi-periodic in both angles, satisfying

\[
h\geq0,\qquad q^2+r^2\leq |F|^2,\qquad
r_{x_j}=q_{y_j},\qquad (q+h)_{x_j}=-r_{y_j}\quad(j=1,2).
\tag{1}
\]

Write S=q+h, and normalize every angular integral by (2pi)^(-2).
The constant angular mean of S is L868's K, and the angular mean
of F is its M. There are no radial growth, angular bandwidth,
absolute Fourier summability or extra regularity assumptions.
All F and graph-Jacobian zeros and L868's fixed orientation remain
in force. The proof uses the actual diagonal F(z,z)=0; it does not
replace (1) by constraints only on that diagonal.

For a function f write

\[
\widehat f_n(x)=(2\pi)^{-2}\int_{[0,2\pi]^2}
 f(x,y)e^{-i(n_1y_1+n_2y_2)}\,dy,
\qquad n\in\mathbb Z^2.
\tag{2}
\]

## Conclusion

There are real constants A and H such that, for every s in R,

\[
\widehat q_0(s,s)=A,\qquad
\widehat h_0(s,s)=H=K-A\geq0.
\tag{3}
\]

For every n!=0 there is a complex C3 function B_n on R for which,
with t=n.x,

\[
\widehat S_n(x)=B_n(t),\quad
\widehat r_n(x)=i B_n'(t),\quad
\widehat q_n(x)=B_n''(t),\quad
\widehat h_n(x)=B_n(t)-B_n''(t).
\tag{4}
\]

In particular the modes with n1+n2!=0 satisfy the global bound

\[
             |\widehat h_n(x)|\leq H\quad(x\in\mathbb R^2).
\tag{5}
\]

For n=(k,-k), k!=0, this argument bounds only the value at t=0;
it gives no bound by H at other t. Nor does (3) assert that
the zero mode of h equals H away from x1=x2.

If H=0, h vanishes on every equal-radius angular torus, and on
all R2 times T2 it is invariant under simultaneous angular rotation:

\[
 h(x,y_1+v,y_2+v)=h(x,y_1,y_2)\quad(v\in\mathbb R).
\tag{6}
\]

These are necessary compatibility restrictions, not a bound
K>=-|M|, a strict-gain certificate or a classification of the
admissible class. In particular (6) does not make h radially
independent, so L868's stopped subclass cannot be invoked from it.
The independent conceptual audit of 6 November 2026 below accepts
this exact restriction without changing its hypotheses or conclusion.
The approved bounded search found no matching period theorem; no
originality claim is inferred from that search.

## Proof

### Imported operations and their hypotheses

The prior EXPLORE assessment is
`drafts/literature/2026-11-06-one-sided-fourier-diagonal-period-test.md`.
Reuse its inspected sources, without a new literature search:

- Walter Rudin, *Principles of Mathematical Analysis*, third edition
  (1976), [Theorem 9.42 and proof, pp236-237](https://djvu.online/file/cNW6EtZ7m9PIB),
  for differentiation of a compact parameter integral.
- Loukas Grafakos, *Classical Fourier Analysis*, third edition (2014),
  Definition 3.1.8, Remark 3.1.9, Proposition 3.1.10 and
  Corollary 3.2.2 with its proof, pp180-183, for product Fejer
  reconstruction, and Theorem 3.3.9(a), pp196-197, for periodic
  integration by parts in Fourier coefficients; see
  [the book](https://www.math.stonybrook.edu/~bishop/classes/math638.F20/Grafakos_Classical_Fourier_Analysis.pdf)
  and [corrected Theorem 1.2.19(2)/proof, pp27-29](https://grafakos.missouri.edu/Books_Correction_Pages/CFA-Page27-29.pdf).

For each fixed compact radial neighborhood, the original functions
and their first derivatives are continuous on its product with T2.
They are uniformly continuous there and their slice integrals exist.
Rudin applies to each radial coordinate, and to real and imaginary
parts separately; integrating the resulting identity in the second
angle is justified on the compact rectangle. Periodicity removes
the boundary terms in the angular integration by parts. Normalize
y/(2pi) when using Grafakos's unit torus. His product Fejer sums
converge uniformly for each continuous angular slice. We use no
factorization theorem and no approximation that purports to preserve
the fixed modulus bound or its zero set.

### Nonzero modes have one radial variable

Applying just those compact operations to (1) gives

\[
\partial_{x_j}\widehat r_n=i n_j\widehat q_n,\qquad
\partial_{x_j}\widehat S_n=-i n_j\widehat r_n.
\tag{7}
\]

All coefficient functions in (7) are C1. At n=0 it follows that
r's zero mode is constant and S's zero mode is K; no analogous
radial differential equation for q's zero mode follows.

Fix n!=0. Along a straight line in R2 with direction v perpendicular
to n, (7) gives directional derivatives of both r's and S's
coefficients equal to zero. Each affine level set n.x=t is such
a line and is connected. Thus define C1 profiles

\[
R_n(t)=\widehat r_n(t n/|n|^2),\qquad
B_n(t)=\widehat S_n(t n/|n|^2).
\]

They represent the two coefficients at every x with n.x=t.
Choose an index j with n_j!=0. Differentiating
r's represented coefficient in x_j and using (7) yields
n_j R_n'(t)=i n_j qhat_n(x), hence qhat_n(x)=R_n'(t)/i.
Consequently q's coefficient is also constant on each such line;
write it as Q_n(t). It is C1, since it is q's C1 coefficient
restricted to t n/|n|^2. Formula (7), or differentiation on that
same transversal line, now gives

\[
R_n'=i Q_n,\qquad B_n'=-i R_n,\qquad B_n''=Q_n.
\]

Since Q_n is C1, B_n is C3. This extra regularity belongs to the
one-variable profiles; it was obtained from the first-order
equations, without taking second partial derivatives of q,r,h.
The identities give (4), including its signs.

### Diagonal reconstruction controls the mean along equal radii

On the actual diagonal x=(s,s), y=(v,v) one has z1=z2, so (1)
forces q=r=0. Fix s, and let q_N(s,s,y) be the product Fejer sum
of the angular function q(s,s,y). Put

\[
w_N(k)=\max\{1-|k|/(N+1),0\},\qquad N\geq0.
\]

This is the finite polynomial with coefficient
w_N(n1)w_N(n2) qhat_n(s,s). Uniform convergence on T2 implies
uniform convergence after restriction to y=(v,v), and therefore

\[
D_N(s):=\frac1{2\pi}\int_0^{2\pi}q_N(s,s,v,v)\,dv
                         \longrightarrow0.
\tag{8}
\]

Integrating this finite sum selects exactly n1+n2=0. For n=(k,-k)
with k!=0, (4) gives qhat_n(s,s)=B_n''(0), independent of s.
It follows exactly, for every N, that

\[
D_N(s)=\widehat q_0(s,s)+
       \sum_{0<|k|\leq N}w_N(k)^2 B_{(k,-k)}''(0).
\tag{9}
\]

For any two finite real s and s', subtract (9). Its finite sums
cancel. Both left sides tend to zero by (8), proving
qhat_0(s,s)=qhat_0(s',s'). This proves the assertion about A.
No unweighted infinite sum has been asserted, and no uniform
limit in the unbounded variable s was used. Since Shat_0=K,
the mean of h on these tori is H=K-A. It is nonnegative by h>=0,
which proves (3).

### Positivity propagates the nonresonant coefficient bound

For every n and every real s, positivity and the normalized
integral in (2) give

\[
|\widehat h_n(s,s)|\leq(2\pi)^{-2}\int h(s,s,y)\,dy=H.
\tag{10}
\]

Suppose m=n1+n2!=0 and fix any x. Set s=(n.x)/m. Then
n.(s,s)=n.x, so (4) makes hhat_n(x)=hhat_n(s,s). Applying (10)
proves (5), at every finite x, with one common H. This uses
availability of the original functions on all R2, but does not
assume or take a limit of their radial growth. If m=0, the equal-radius
line only samples t=0, which explains the stated exception.

If H=0, the continuous nonnegative function h(s,s,.) has zero
integral, so it is zero at every angular point. Also (5) makes
every coefficient with n1+n2!=0 vanish at every x. For fixed x,
each product Fejer sum of h(x,.) therefore contains only the modes
(k,-k). Each finite sum is invariant under simultaneous angular
rotation. Uniform convergence passes that identity to h(x,.),
proving (6). No angular derivative of a reconstructed infinite
series is needed.

### What the period test did not establish

The desired conclusion would be A+H>=-|M|. The preceding proof
gives H>=0 and controls each indicated correction coefficient by
H, but supplies no numerical lower bound for A+H at that threshold.
The modulus constraint also yields
|A|<=mean_y |F(R e^(s+i y1),R e^(s+i y2))| for every s; replacing
that right side by its infimum does not identify it with |M|.
L868(11) already records the unresolved absolute-mean comparison.

In particular, neither the zero Fourier mode nor the modes
(k,-k) away from t=0 may be discarded. The original constraints
at all other zeros of F are still required for any proposed
certificate. A product Fejer polynomial used in (8) or in the
proof of (6) is only a reconstruction tool, not an admissible
replacement for q,r,h. No K<-|M| example or full-class no-gain
result is proved here. Further progress needs additional control
that is not supplied by these identities alone.

### Independent conceptual audit, 6 November 2026

The invocation-start EXPLORE assessment was
`drafts/literature/2026-11-06-diagonal-fourier-correction-audit.md`.
This audit reuses the precise Rudin and Grafakos imports above and
the audited L868 system. Its purpose is to check the submitted
restriction, not to derive a further period theorem. No source
hypothesis, growth condition or approximation of the feasible class
is added.

For a C1 function f, on any compact radial neighborhood the compact
parameter integral gives a C1 coefficient fhat_n. Integration by
parts in y_j gives

\[
 \widehat{\partial_{y_j}f}_n=i n_j\widehat f_n:
\]

the boundary term is zero because both f and the integer-frequency
exponential are periodic. Thus (7) has exactly the displayed signs.
At n=0 only the means of r and S are radially constant; the equations
do not assert that qhat_0 is constant on R2.

For n!=0, along x+u v with n.v=0, both coefficient derivatives
vanish. Each such entire line is connected and lies in the radial
domain R2, so its value equals the value at the transversal point
t n/|n|^2. The resulting profiles R_n and B_n are C1. At any index
j with n_j!=0 the chain rule and (7) give

\[
 n_jR_n'(t)=i n_j\widehat q_n(x),\qquad
 n_jB_n'(t)=-i n_jR_n(t).
\]

Division is only by this nonzero integer, never by F or by a
coefficient. Restriction of qhat_n to the transversal is C1; call
it Q_n. Therefore R_n'=i Q_n, B_n'=-i R_n, and B_n''=Q_n.
In particular R_n is C2 and B_n is C3, with B_n'''=Q_n'
continuous. Also R_n=i B_n', verifying every sign in (4).
This includes n1=0 or n2=0 by choosing the other index. No second
derivative of an original function was assumed or used.

The actual diagonal requires both x1=x2=s and y1=y2=v modulo
2pi. On it F=0 and the modulus bound forces q=r=0. For each fixed
s, the cited product Fejer theorem applies to the continuous
angular slice. In particular

\[
 |D_N(s)|\leq
 \sup_{y\in\mathbb T^2}|q_N(s,s,y)-q(s,s,y)|\longrightarrow0.
\]

Integrating the finite polynomial along (v,v) selects n1+n2=0.
Its zero coefficient has weight one; every (k,-k) coefficient has
weight w_N(k)w_N(-k)=w_N(k)^2 and value B_(k,-k)''(0).
For arbitrary fixed s,s', the entire nonzero finite sum therefore
cancels before taking a limit. The exact identity is
D_N(s)-D_N(s')=qhat_0(s,s)-qhat_0(s',s'). Both terms on the left
tend to zero. This proves one finite real A on the whole diagonal
line, and H=K-A is finite and nonnegative. The argument needs
neither absolute summability nor convergence uniform in all s.

For each n, h>=0 implies |hhat_n(s,s)|<=H. When m=n1+n2!=0,
the point s=(n.x)/m is finite for each finite x, and the profile
identity makes hhat_n(x)=hhat_n(s,s). Thus the same H controls
every such mode at every x. Negative m and arbitrarily large finite
s cause no change: only the global domain, not a radial estimate,
is being used. If m=0, equal radii sample only t=0. The zero mode
has no profile equation at all. Neither exception is eliminated.

If H=0, continuity and nonnegativity imply h(s,s,y)=0 everywhere
on each equal-radius torus. At arbitrary fixed x, all nonresonant
coefficients vanish. Every finite product Fejer sum of h(x,.) then
contains only the frequencies (k,-k), including zero, and is
invariant under y -> y+(v,v). Uniform convergence of these sums
passes that equality to h for every v. There is no radial
differentiation in this step. As a consistency check using only the
already proved L868(12)-(13), its bump is angularly independent,
has S=0, and is supported on disjoint radial intervals. Hence it
has A=H=0 on equal radii, while h has a nonzero radial derivative
inside its support. This existing example confirms that H=0
does not activate the radial-independent-h subclass theorem.

Finally L868 gives integral_T alpha=-(2pi)^2 K and
integral_T omega=(2pi)^2 M, so the full-class no-gain threshold
would indeed be A+H=K>=-|M|. Nothing in the proof estimates A+H
at that value. The inequality |A|<=mean|F| on equal-radius tori
does not identify the infimum of those absolute means with |M|.
The uncontrolled modes do not themselves constitute a counterexample
to a period bound; the statement makes no such claim. Every other
F zero remains a condition on an admissible triple, and no Fejer
sum was substituted for such a triple. Fixed orientation and the
allowance of all J zeros are inherited unchanged from L868.

No mathematical defect was found. The exact coefficient profiles,
diagonal means, global nonresonant bound and H=0 rotation invariance
are accepted as an independently checked local input. There is no
new result beyond C868a, no strict-gain certificate, no full-class
no-gain theorem, and no conclusion about higher Xi signs or RH.
The only direct mathematical input remains L868; the cited compact
analytic operations have their applicability checked above.

## Mathlib

The full matching statement and supporting formal Fourier results
were not checked in Mathlib. Unknown coverage is not evidence of
absence. The cited classical results provide the compact analytic
operations; the specialization and its conceptual audit above are
informal. There is no numerical certificate, mathematical script or
formal verification claim.
