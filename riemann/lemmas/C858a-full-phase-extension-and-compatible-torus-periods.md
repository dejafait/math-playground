# Corollary 858a: the full phase extends with compatible torus periods

## Hypotheses

Retain all hypotheses and qualifications of L858. In particular, on
the oriented torus T^2=(R/2pi Z)^2 with coordinates (t,s), let

\[
 z_j=R\exp(u_j+i\theta_j),\qquad
 f=F(z_1,z_2),\qquad J=\det(I-iDu),\qquad q=fJ\geq0,
\]
\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2}.
\]

Here R,C>0 and G are exactly L847's actual data, u is real C2,
periodic and exchange-symmetric, and q is real everywhere. The graph
agrees with L849 on a strictly smaller open diagonal collar, retaining
its L848 analytic and trusted-software qualifications. Original J
zeros and f zeros may be nonisolated; all multiplicities of G are
allowed. The accepted L858 conclusion and constructed matrix fields
are inputs. No globally nonnegative torus is asserted to exist.

Fix any 0<epsilon<=epsilon_0 supplied by L858. Write

\[
 J_\epsilon=\det(I-iA_\epsilon)=J+\epsilon\chi\bar f.
                                                               \tag{1}
\]

L858 gives J_epsilon nonzero on the whole torus, exchange invariance,
agreement with J near the closed smaller collar, and

\[
                  fJ_\epsilon=q+\epsilon\chi|f|^2\geq0.    \tag{2}
\]

The two periods below mean integer winding numbers on
e_1(t)=(t,0) and e_2(t)=(0,t), each traversed from 0 to 2pi.

## Conclusion

The circle map f/|f| on {f!=0} has the continuous extension

\[
       \varphi=\frac{\overline{J_\epsilon}}{|J_\epsilon|}
                       \quad\hbox{on all of }T^2.          \tag{3}
\]

This constructed extension is independent of positive epsilon. At
every f zero it is exactly conjugate(J)/|J|; no division by f occurs.
Both periods of varphi, and both periods of J_epsilon/|J_epsilon|,
are zero. In particular varphi has a continuous real-valued periodic
argument on T^2.

In the actual ambient frame, the determinant is
-z_1 z_2 J_epsilon, whose phase has periods (1,1), not (0,0).
Forstneric's positive Gram normalization preserves those periods.
The ambient coefficient of omega is F/(-z_1 z_2); its extended phase
has periods (-1,-1). These two phases multiply to 1 everywhere after
extension. Thus the nonzero ambient-frame periods supply no
contradiction to the full-density sign condition or the exact collar.

This is a conditional first-phase calculation, not construction or
exclusion of the torus, forced contact, a new Xi sign or an RH
candidate. It retires the proposed two-period obstruction. Stronger
relative obstructions, global assembly and all-degree transfer remain
unresolved. The new application has not received a separate critical
audit; POTENTIALLY_NEW records only the scope of the prior search,
not certified originality or a new general Maslov theorem.

## Proof

### Imported tools and the exact specialization

The invocation-start assessment is
`drafts/literature/2026-11-06-l858-full-phase-period-test.md` (EXPLORE).
Its source approval and duplicate/failure comparison are reused.
The needed covering-space input is Allen Hatcher, *Algebraic Topology*
(2002), Section 1.3, [Proposition 1.33 and proof, pp61–62](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf#page=70):
a based continuous map from a path-connected, locally path-connected
space lifts through a covering precisely when its induced fundamental
group lies in the covering's fundamental-group image. The torus has
these domain properties; the target covering used below is
R -> S1, a |-> exp(ia). We establish the whole-torus map and its
periods before applying this criterion.

For the frame convention use Franc Forstneric, *Analytic disks with
boundaries in a maximal real submanifold of C2*, Ann. Inst. Fourier
37(1) (1987), 1–44, DOI 10.5802/aif.1076,
[Section 2, equations (2.1)–(2.4) and Lemma 7/proof, pp11–13](https://www.numdam.org/item/10.5802/aif.1076.pdf).
These define the oriented orthonormal-frame determinant and retain
the complex coordinate multiplier. L858(10) already supplies the
exact normalization in this setting. Neither this source nor the
lifting theorem asserts extension through zeros. Only the explicit
application (1)–(3) and its periods are derived here. No general
covering or Maslov formula is reproved.

### Extension without a zero-set regularity assumption

L858 excludes {f=J=0} and makes J_epsilon nonzero everywhere.
Equation (2) is strictly positive at every point where f!=0: its
left side is then nonzero, and its right side is real nonnegative.
Taking absolute values and phases gives

\[
                 \frac{f}{|f|}
                   \frac{J_\epsilon}{|J_\epsilon|}=1.
                                                               \tag{4}
\]

Thus (3) agrees with the requested phase wherever it was defined.
It is continuous on the whole torus because its denominator is
everywhere positive. At an f zero, (1) gives J_epsilon=J!=0, so
the displayed value there is valid. At an original J zero, L858
gives f!=0, and (4) still applies; original total reality is not
needed. These two cases also show independence of epsilon pointwise:
on {f!=0} the value is f/|f|, and on {f=0} it is conjugate(J)/|J|.
No isolation, transversality, simplicity or empty-interior assertion
for either original zero set enters this argument.

### The two periods in the logarithmic frame

Put g=J_epsilon/|J_epsilon| and let n_j be its period on e_j.
L858's exchange relation gives g(t,s)=g(s,t), so n_1=n_2.
The diagonal loop d(m)=(m,m) represents the sum of the two
coordinate generators of pi_1(T^2)=Z^2. Since the induced map to
pi_1(S1)=Z is a homomorphism,

\[
                  \operatorname{wind}(g\circ d)=n_1+n_2.
                                                               \tag{5}
\]

This uses a circle map already defined on the full torus; no loop
is being moved through a missing point of its domain.

On that diagonal L858(6) and collar agreement give exactly

\[
 J_\epsilon(m,m)=J(m,m)=(1-ih'(m))(1-ib(m)).               \tag{6}
\]

Here h and b are the prescribed real periodic data. Both factors
have real part 1. Therefore the continuous periodic real function

\[
            -\arctan h'(m)-\arctan b(m)                  \tag{7}
\]

is an argument for g on the diagonal, and its winding is zero.
Equations (5)–(7) yield 2n_1=0 in Z, hence n_1=n_2=0.
Complex conjugation reverses a circle winding, so both periods of
varphi are zero too.

Apply Hatcher's cited lifting criterion now: the two generators
map to zero, so the full fundamental-group image is zero, equal
to the image from the simply connected covering space R. It gives
a continuous real argument alpha for varphi on T^2. As a function
of (t,s) on R^2 this lift is periodic. Choose its basepoint value
so that along the diagonal it equals
arctan h'(m)+arctan b(m); equality holds along that whole loop
because two lifts differ by a constant multiple of 2pi. On the
entire prescribed collar (3) uses the unchanged J, so the extension
also agrees with the original off-diagonal phase there. No new
collar data or sign condition is imposed.

### The actual frame and the full ambient coefficient

Let M_epsilon=diag(iz_1,iz_2)(I-iA_epsilon) and let E_epsilon
be its real Gram matrix. L858(10) gives

\[
 \pi(g_\epsilon)=
    \frac{-z_1z_2J_\epsilon}{\sqrt{\det E_\epsilon}},
       \qquad \det E_\epsilon>0.                         \tag{8}
\]

The source's determinant here is nonzero since the constructed
planes are totally real. Its unit phase, denoted psi, is

\[
 \psi=cg,\qquad
 c=\frac{-z_1z_2}{|z_1z_2|}=-e^{i(t+s)}.                 \tag{9}
\]

The positive denominator in (8) does not affect phase. The multiplier
c winds once on each coordinate loop. Since g has periods (0,0),
psi has periods (1,1). Its square accordingly has periods (2,2);
the unsquared and squared determinant conventions must be distinguished.
L858's auxiliary plane homotopy was not used as a totally real
homotopy to compute these windings.

Finally the coefficient in the ambient holomorphic trivialization
is exactly

\[
 \omega=\frac{F}{-z_1z_2}\,dz_1\wedge dz_2.              \tag{10}
\]

Its pulled-back coefficient phase extends as c^(-1)varphi, with
periods (-1,-1). Equations (3) and (9) give on the whole torus

\[
                     (c^{-1}\varphi)\psi=\varphi g=1.    \tag{11}
\]

Off the divisor this is exactly the phase of the full form on the
constructed frame, consistent with (2) and positive Gram normalization.
On the divisor (11) compares the continuous extensions, not a
nonzero value of the vanishing form. The ambient determinant's
nonzero periods thus cancel those of its coefficient. They do not
force a common contact or contradict nonnegativity. Integrability
of A_epsilon as a derivative of a new surface is never asserted.

## Mathlib

Full matching coverage has not been checked; no absence claim is
made. The cited lifting and determinant results are imported standard
inputs. The exact conditional extension and period computation above
are the notebook application, with the stated L858 and collar
qualifications, and are not formally verified.
