# Lemma 859: an even single-divisor contact admits a nonzero-J rank-one germ

## Hypotheses

Use the actual entire G and the positive constants R,C of L847,
with exactly its full form on X=(C minus zero)^2:

\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
 \qquad
 \omega=C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^3z_2^3}
                 dz_1\wedge dz_2.                         \tag{1}
\]

Explicitly hypothesize zeta eta != 0, zeta != eta, a zero of G at
zeta of one fixed finite even multiplicity n>=2, and G(eta)!=0.
Choose real lifts theta^0=(arg zeta,arg eta). No existence of an
actual even zero of G is asserted. The conclusions are conditional
on this pair; no RH, global torus, collar or prescribed tangent data
are assumed.

For a real C2 map u on an open neighborhood of theta^0, use
Phi_u,j(theta)=R exp(u_j(theta)+i theta_j), the original orientation
dtheta_1 wedge dtheta_2, and

\[
 J_u=\det(I-iDu),\qquad q_u=F(\Phi_u)J_u,
 \qquad \Phi_u^*\omega=q_u\,d\theta_1\wedge d\theta_2.       \tag{2}
\]

## Conclusion

There is such a local graph through (zeta,eta) with u real analytic,
q_u real and nonnegative on the whole neighborhood, and J_u nowhere
zero there. The first coordinate Phi_u,1 has real rank one throughout.
Its zero set G(Phi_u,1)=0 is a smooth curve through theta^0; q_u is
strictly positive off that curve. The other G factor and the coordinate
difference stay nonzero. The same conclusions, with the coordinates
exchanged, hold when only the second G factor vanishes at the center.

Moreover any C2 graph through the hypothesized pair with real
nonnegative q_u and J_u(theta^0)!=0 must have real rank one, rather
than rank two, for its vanishing coordinate at theta^0. This necessity
uses only a first-order expansion, not Cn regularity of u.

This is a freely chosen local germ. It gives no boundary matching,
periodic extension, forced contact, simultaneous-contact classification,
Xi mixed-minor sign or RH conclusion. The neighborhood is not effective
or uniform in n or the pair. The independent conceptual audit of
6 November 2026 below accepts this conditional local statement.
POTENTIALLY_NEW records only that the prior bounded source comparison
found no matching full-form/nonzero-J theorem; it is not a certified
originality claim or an advance beyond the checked sources as a whole.

## Proof

### Coverage, reused coordinates and scope of the calculation

The invocation-start assessment is
`drafts/literature/2026-11-06-even-single-contact-feasibility-scope.md`,
with decision EXPLORE. It covers this exact even, C2, nonzero-J target,
including rank one and either vanishing coordinate. Its inspected
primary tools include:

- Jiří Lebl, *Guide to Cultivating Complex Analysis*, v1.10,
  5 November 2026, [Theorem 2.4.7, pp49–50, and Corollary 3.2.12,
  pp67–68](https://www.jirka.org/ca/ca.pdf): finite-order zero
  factorization and a primitive on a star-like plane domain.
- Lebl, *Tasty Bits of Several Complex Variables*, v4.4,
  31 May 2026, [Theorem 1.2.1 and proof,
  pp20–21](https://www.jirka.org/scv/scv.pdf#page=20): polydisc
  power series and their converse, supporting the joint primitive.
- Marc Chaperon, *On the Cauchy-Kowalevski theorem*, 9 January 2007,
  [Section 1, Corollary 1 and real/complex justification,
  p2](https://webusers.imj-prg.fr/~marc.chaperon/Chaperon_Cauchy_Kowalevski.pdf#page=2):
  the analytic local inverse theorem at an invertible derivative.

Import these standard results; no reproof or singular PDE existence
claim is needed. L855's audited coordinate portion (3)–(5) already
checks all their applications to the present actual form and pair.
Its later monomial surface, which has J=0 at the center, is not used.
L853's finite jets and C858b's separately unaudited odd-contact
restriction are also not inputs.

Precisely, put w=z_1-zeta and factor G(zeta+w)=w^n g(w), g(0)!=0.
On a small product of discs, L855 defines the nonvanishing holomorphic
function and its joint primitive

\[
 H(w,z)=C\frac{g(w)G(z)(\zeta+w-z)^2}{(\zeta+w)^3z^3},
 \quad H_0=H(0,\eta)\ne0,\qquad
 V(w,z)=\int_\eta^z H(w,t)\,dt.                            \tag{3}
\]

The discs have closures in a larger holomorphic product, where every
displayed nonzero factor stays nonzero. The complex map (w,z)->(w,V)
has determinant H0 at (0,eta). Its inverse on an open neighborhood
B of (0,0) is (w,v)->(w,h(w,v)), with image in that product, and

\[
 h(0,0)=\eta,\quad h_w(0,0)=0,\quad
 h_v(w,v)=H(w,h(w,v))^{-1},\qquad
                    \omega=w^n\,dw\wedge dv.              \tag{4}
\]

These are exact identities, including w=0. Reusing them avoids
reproving the joint primitive theorem or replacing the actual form
by an unrelated model. The new checks below concern the surface,
the original angular orientation and its nonzero J.

### A real plane with the required angular orientation

Write m=n+1>=3 and D=zeta^(-m)/(H0 eta), which is nonzero. Choose
phi in (0,pi) such that

\[
 \beta:=\operatorname{Im}(D e^{-im\phi})>0,
 \qquad a=\zeta e^{i\phi},\quad b=a^{-m}.                  \tag{5}
\]

Such a phi exists: writing D=|D|exp(i delta), the open interval of
phases delta-m phi has length m pi>2pi, so it contains a phase with
positive sine. Also alpha:=Im(a/zeta)=sin phi>0. This choice is made
using the fixed nonzero H0; H0 does not depend on phi.

For real parameters (t,s) close to (0,0), set

\[
        S(t,s)=(\zeta+a t,\ h(a t,b s)).                    \tag{6}
\]

An open parameter neighborhood maps (a t,b s) into B by continuity.
Thus (6) is an actual real analytic surface, not a formal series.
Equations (4) and b=a^(-(n+1)) give exactly

\[
 S^*\omega=(a t)^n a b\,dt\wedge ds
                   =t^n\,dt\wedge ds.                    \tag{7}
\]

The exponent is even, so this coefficient is nonnegative for both
signs of t. It is positive when t!=0. This parameter sign alone is
not enough; the original angular projection is checked next.

Choose local logarithms of S1/zeta and S2/eta near 1, normalized
to zero at the origin. They exist by the complex inverse theorem
for exp, whose derivative at zero is 1. Define real analytic lifts
Theta_j=theta^0_j+Im log(S_j/S_j(0,0)). At the origin, (4) gives

\[
 dS_1=a\,dt,\qquad dS_2=(b/H_0)\,ds,
 \qquad D\Theta(0,0)=
 \begin{pmatrix}\alpha&0\\0&\beta\end{pmatrix},
 \qquad \lambda_0=\alpha\beta>0.                           \tag{8}
\]

In particular this is a check of the prescribed angular orientation,
not a free reorientation of the surface. The real analytic inverse
theorem applies to Theta. Take a sufficiently small open rectangle
U about (0,0), inside its injectivity neighborhood and all previous
coordinate and logarithm neighborhoods, with
lambda(t,s):=det DTheta(t,s)>lambda0/2 on U. On this same U all
factors in (3) remain nonzero and (a t,b s) remains in B. Continuity
and finitely many open neighborhood restrictions give this common
choice. Thus O=Theta(U) is open and Theta:U->O is an analytic
diffeomorphism with positive determinant everywhere.

Let (t(theta),s(theta)) be that inverse and define
u_j(theta)=log(|S_j(t(theta),s(theta))|/R). Nonvanishing of both
coordinates makes these real analytic real functions. The chosen
angle lifts give Phi_u=S composed with Theta^(-1). Consequently

\[
            q_u(\theta)=\frac{t(\theta)^n}
             {\lambda(t(\theta),s(\theta))}\geq0.          \tag{9}
\]

The set t(theta)=0 is a smooth curve: the first row of the derivative
of a diffeomorphism is nonzero. It is precisely the zero set of q_u
and of G(Phi_u,1), since g stays nonzero and a!=0. The differential
of S1 is a dt, of real rank one; composition with the inverse
diffeomorphism preserves that rank everywhere on O.

### The full complex Jacobian, including the contact

Differentiate (6) and use h_v=1/H. The h_w term repeats dt and drops
out of the wedge, giving

\[
 S^*(dz_1\wedge dz_2)=\frac{ab}{H(a t,S_2)}\,dt\wedge ds.
\]

Since (i z1)(i z2)=-z1 z2, L847's local identity (2) gives

\[
 J_u(\Theta(t,s))=
 -\frac{ab}{H(a t,S_2(t,s))\,S_1(t,s)S_2(t,s)\,\lambda(t,s)}.
                                                               \tag{10}
\]

Every numerator and denominator factor here is nonzero on U,
including t=0. Thus J_u is nowhere zero. No division by w, G,
F or q has occurred. For a separate full-density check, (1) and (3)
give F(S)=-w^n H(w,S2)S1 S2. Multiplying this by (10) gives
w^n ab/lambda=t^n/lambda on all of U, including the contact curve.
It is exactly (9), retaining both the normalization and the Jacobian.
This distinguishes the construction from L855's J=0 transverse germ.

### Why a feasible C2 contact cannot have rank two

Consider any C2 graph satisfying the hypotheses and the required sign,
and put p=theta^0, w(theta)=Phi_u,1(theta)-zeta. The same factorization
gives, on a sufficiently small neighborhood,

\[
 q_u(\theta)=w(\theta)^n K(\theta),\qquad
 K(\theta)=-C\frac{g(w(\theta))G(\Phi_{u,2}(\theta))
       (\Phi_{u,1}(\theta)-\Phi_{u,2}(\theta))^2}
       {\Phi_{u,1}(\theta)^2\Phi_{u,2}(\theta)^2}J_u(\theta).
                                                               \tag{11}
\]

K is continuous and K(p)!=0. Suppose the real-linear map Dw(p)
has rank two. Choose a complex number c with K(p)c^n=i, using polar
coordinates for a root of the nonzero number i/K(p). Surjectivity
gives a real vector v with Dw(p)v=c. Along p+epsilon v, epsilon>0,
differentiability and continuity yield

\[
 \frac{q_u(p+\epsilon v)}{\epsilon^n}
 =\left(\frac{w(p+\epsilon v)}{\epsilon}\right)^n
       K(p+\epsilon v)\longrightarrow c^n K(p)=i.           \tag{12}
\]

The left side is real and nonnegative, so its limit cannot be i.
This contradicts rank two. Rank zero is impossible as well, because
partial_1 Phi_u,1(p)=zeta(partial_1 u1(p)+i)!=0 for real u1.
The vanishing coordinate therefore has rank one. This calculation
uses only first-order differentiability and continuity of J, so it
does not assume nonexistent high derivatives when n>2. It does not
exclude rank-one contact; (6)–(10) realize it exactly.

### The other vanishing coordinate

Let P exchange two coordinates. From the constructed u define
u_tilde(theta)=P u(P theta) on P O, centered at the reversed pair
(eta,zeta). Then Phi_u_tilde(theta)=P Phi_u(P theta) and
Du_tilde(theta)=P Du(P theta)P. The coefficient F is symmetric in
its two coordinates, while determinant is unchanged by conjugation.
Thus, directly in the original ordered angle coordinates,

\[
 J_{\widetilde u}(\theta)=J_u(P\theta),\qquad
 q_{\widetilde u}(\theta)=q_u(P\theta).                    \tag{13}
\]

This also accounts for orientation: swapping the ambient form and
swapping the angular parameters each contributes a minus sign, which
cancel. All claimed signs, nonvanishing factors and ranks transfer,
with the second coordinate now of rank one. The rank-two contradiction
uses that coordinate and partial_2 Phi_u,2 instead. No exchange symmetry
of a global graph is asserted.

All conclusions are local under the explicitly hypothesized pair.
They settle the approved feasibility test, while the collar extension
and all-degree positivity problems remain unresolved.

### Independent conceptual audit — 6 November 2026

The separate invocation-start EXPLORE assessment is
`drafts/literature/2026-11-06-l859-even-contact-conceptual-audit.md`.
This audit reuses its inspected primary-source coverage and checks the
complete proof above against L847's full angular identity and L855's
audited coordinate portion. No new existence theorem, matching-source
claim or stronger conclusion is introduced. The following checks accept
(3)-(13) without a mathematical repair.

**Common domains and the two different inverses.** Finite-order
factorization applies to the explicitly assumed finite zero. The five
nonzero factors in H at (0,eta) permit a product of discs compactly
contained in a larger product with the same nonvanishing properties.
The segment primitive is jointly holomorphic by the polydisc argument
in L855; V(w,eta)=0 gives V_w(0,eta)=0. The complex derivative matrix
of (w,z)->(w,V) is therefore diag(1,H0) at the center. Its inverse gives
h_w(0,0)=0 and h_v=1/H on its open domain B. This proves (4) independently
of any angular inverse or surface sign.

The real map (t,s)->(at,bs) sends the origin into B. Restrict to its
preimage of B, then to the preimages of the two logarithm discs about 1.
On that open intersection Theta is real analytic. After verifying (8),
restrict further to the real inverse theorem's injectivity neighborhood
and to the open set det DTheta>alpha beta/2. An open rectangle about zero
inside this finite intersection is the claimed U. Its image O is open,
and its inverse is real analytic. This checks one common neighborhood,
not a collection of incompatible germs or a formal inversion.

**Phase and prescribed orientation.** The nonzero H0 is fixed before
choosing phi. For m=n+1>=3 the interval delta-m(0,pi) has length
m pi>2pi, so it meets a positive-sine interval. Thus alpha>0 and
beta>0 in (5). In particular b/(H0 eta)=D exp(-im phi). At the origin
dS2=(b/H0) ds because h_w(0,0)=0, and d arg Sj=Im(dSj/Sj).
These give exactly the diagonal matrix (8), with its positive
determinant in the order (theta1,theta2). No subsequent orientation
change is used to obtain nonnegativity. The logarithm lifts imply
exp(i Theta_j)=Sj/|Sj|, so the defined real u satisfies Phi_u=S
composed with Theta inverse for the specified radius R.

**Full density and nonzero J at the curve.** The normalization is
a^(n+1)b=1. Hence the primitive pullback is t^n dt wedge ds.
Independently, the coordinate wedge is (ab/H) dt wedge ds, whereas
the angular graph wedge is -S1 S2 J lambda dt wedge ds. Comparing
these gives (10), including at t=0. Multiplying by
F(S)=-(at)^n H S1 S2 yields F(S)J=t^n/lambda on all of U. Every factor
in (10) is nonzero there, so this equality does not cancel a vanishing
quantity at the curve. Even n and lambda>0 give the required signs on
both sides. The factorization G(S1)=(at)^n g(at) and nonvanishing of
g show that this is precisely the zero curve. The inverse map has
invertible differential, so dt is a nonzero real covector everywhere;
dPhi_u,1=a dt has rank one throughout O. The other G factor and the
coordinate difference retain their nonvanishing on the same domain.

**C2 necessity.** For a competing graph the factor K in (11) is
continuous, and each of its central factors is nonzero by the single-G
hypotheses and J(p)!=0. If Dw(p) were onto C as a real vector space,
choose c and v exactly as in (12). Differentiability gives
w(p+epsilon v)/epsilon->c; the open parameter neighborhood contains
that ray segment. The normalized densities are in the closed subset
[0,infinity) of C, while the proposed limit is i, a contradiction.
No derivatives of order n are taken. Rank zero is excluded by the
nonzero prescribed angular derivative zeta(partial_1 u1+i).
Thus the necessity argument applies to the stated C2 class, including
arbitrarily large fixed even n; it does not assert that all rank-one
jets are realizable or prescribe the tangent of the constructed germ.

**Exchange and scope.** F(Pz)=F(z), and
I-iD u_tilde=P(I-iDu)P, with det(P)^2=1. Consequently (13) holds in
the original ordered angular coordinates. Equivalently the minus
signs from the ambient and parameter exchanges cancel. The same
argument excludes rank zero or two for the second vanishing coordinate.
The only direct mathematical inputs remain L847 and L855. L858,
L853 and C858b are not used to infer any sign or contact here.

The audit accepts the stated conditional existence and rank restriction.
It establishes reliability of this local input, not a new result beyond
the existing construction or the literature checked. In particular it
does not establish an actual even zero, exclude simultaneous contacts,
match prescribed data, construct a torus, or prove an Xi minor sign.

## Mathlib

Full matching coverage is not checked. Coverage of the supporting
factorization, primitive, analytic inverse and differential-form tools
is also not checked in this step. The cited primary results and L855's
audited coordinate specialization are the inputs; no formal verification
or absence claim is made.
The conceptual audit does not change this unchecked coverage status.
