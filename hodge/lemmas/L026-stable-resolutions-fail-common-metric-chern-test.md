# L026 — Stable resolutions fail the common-metric Chern test

## Hypotheses

Let S and the reduced cubic correspondence C in X=S x S satisfy L008
at a very general parameter. Put N=NS(S)_Q, T=N^perp, and let q denote
the cup-product pairing. Use L019's rational divisor basis F,O,E,P;
here E denotes the exceptional fibre component on S. The action of
[C] on T is L006's U, with

\[
U\sigma=\lambda\sigma,\qquad
\lambda=2\cos(2\pi/7),\qquad
f(\lambda)=0,\quad f(z)=z^3+z^2-2z-1.
\]

Fix an ample line bundle L on S, write ell=c_1(L), and put
H=p_1^*L tensor p_2^*L and h=c_1(H). Suppose that

\[
0\longrightarrow\mathcal E\longrightarrow P_2\longrightarrow P_1
\longrightarrow P_0\longrightarrow I_C\longrightarrow0,
\qquad P_i=\mathcal O_X(-m_iH)^{a_i}                 \tag{1}
\]

is exact, with the terminal bundle locally free of positive rank r. This includes
the terminal stable bundle in Mistretta's Theorem 3.1 on this fourfold.
No freedom to choose the integers independently, or extra stability
of an arbitrary resolution, is assumed.

Choose the same hyperkahler metric on the two factors, with Kahler
class omega in N_R, and use its diagonal SU(2) action on cohomology.
In particular this permits the metric with class supplied by L025.
Let M be any holomorphic line bundle on X.

## Conclusion

The first two Chern classes of the twist by M cannot both be
SU(2)-invariant. In fact the twist-invariant class

\[
\nu(\mathcal E)=\operatorname{ch}_2(\mathcal E)
                    -\frac{c_1(\mathcal E)^2}{2r}                 \tag{2}
\]

is not invariant. Every such twist still has ch_2 action U on T.
Thus the terminal bundles of this single-polarization construction
fail the saved compatible-bundle requirement before any stability
test at omega. This excludes that recipe, not arbitrary bundles
with the desired cubic action or other divisor-tensor corrections.

The attained cycle span stays 21-dimensional on the known family;
three RM directions are covered against four required. No transverse
transport or conclusion about the universal Hodge conjecture follows.

## Proof

**Known construction and the scope of this test.** Import Mistretta,
*Stable vector bundles as generators of the Chow ring*,
[arXiv:math/0310185v2, Theorem 3.1, pp. 7--9](https://arxiv.org/pdf/math/0310185v2#page=7).
It supplies (1) with a slope-stable terminal bundle for the ample
integral polarization. In its notation e=dim(X)-2=2, so there are
three presentation terms. L012 concerns a second syzygy with two
terms and specified vanishing hypotheses; its deformation exclusion
is not a verbatim theorem about this terminal bundle. Stability
alone does not reopen L012's stopped case.

Use the SU(2) framework in Verbitsky, *Hyperholomorphic bundles*,
[arXiv:alg-geom/9307008v1, Proposition 1.2, p. 4, and Theorem 2.5,
p. 9](https://arxiv.org/pdf/alg-geom/9307008v1#page=4).
The stable-bundle criterion presupposes invariant first two Chern
classes. We prove that necessary class condition fails here, without
invoking its sufficiency or assuming stability at the new metric.
The construction and framework are known; this is their scoped
application, classified as REPRODUCTION, without an originality claim.

**The full divisor action of the correspondence.** By L008 the smooth
normalization W has finite flat maps g_0,g_1:W -> S of degree two,
with g_1=g_0 rho, where rho is the rotation v -> zeta_7 v keeping
x,y fixed on the Laurent chart. Its map (g_0,g_1) is birational to C.
We check rho's action on the pullbacks of the entire basis of N.

- g_0^*F=2F_W, and a base rotation preserves the fibre class F_W.
- g_0^*O is the zero section O_W, preserved by rho.
- The base change is unramified over infinity. Thus g_0^*E is the
  sum E_0+E_infinity of the exceptional components in the two
  type-III fibres. The rotation fixes both base points and lifts
  equivariantly through the two A_1 resolutions, preserving each
  exceptional component.
- L019's P has constant Laurent coordinates (x_0,y_0). Its pullback
  is the section P_W with those coordinates, preserved by rho on
  the dense chart and hence on its closure.

Therefore rho^*g_0^*d=g_0^*d for every d in N, since these four
classes span N. It follows that g_1^*d=g_0^*d. The projection formula
for the finite degree-two map now gives

\[
T_{[C]}(d)=(g_1)_*g_0^*d=(g_1)_*g_1^*d=2d.        \tag{3}
\]

There is no averaging factor in (3): C is the multiplicity-one
image of this map. L006 identifies the action of this same pushed
rotation graph on T with U. Its rational Hodge decomposition has
no mixed N/T terms, as in L006. Consequently the mixed degree-four
operator of [C] is U on T and 2 id on N. The exceptional components
at both points over infinity have been retained in this calculation.

**Resolution signs and twisting.** Additivity in K_0(X) gives

\[
[\mathcal E]=[P_2]-[P_1]+[P_0]-[I_C].               \tag{4}
\]

The standard leading-term consequence of Grothendieck--Riemann--Roch
is ch_0(O_C)=ch_1(O_C)=0 and ch_2(O_C)=[C], also for this singular
reduced support. Hence ch(I_C)=1-[C] in degrees at most four.
Writing

\[
\begin{aligned}
r&=a_2-a_1+a_0-1>0,\\
d&=-a_2m_2+a_1m_1-a_0m_0,\\
s&=a_2m_2^2-a_1m_1^2+a_0m_0^2,
\end{aligned}
\]

expansion of (4) gives

\[
c_1(\mathcal E)=d h,\qquad
\operatorname{ch}_2(\mathcal E)=[C]+\frac{s}{2}h^2,
\qquad
\nu(\mathcal E)=[C]+\frac{b}{2}h^2,
\quad b=s-\frac{d^2}{r}\in\mathbb Q.                 \tag{5}
\]

These identities hold for the actual integers of every permitted
resolution; no assignment of unconstrained formal coefficients is
being asserted to arise from a bundle.

For t=c_1(M), the splitting principle gives

\[
\begin{aligned}
c_1(\mathcal E\otimes M)&=c_1(\mathcal E)+rt,\\
\operatorname{ch}_2(\mathcal E\otimes M)
 &=\operatorname{ch}_2(\mathcal E)+c_1(\mathcal E)t+\frac r2t^2.
\end{aligned}
\]

Substitution into (2) cancels both terms involving t and proves
that nu is unchanged by twisting. Also

\[
\nu(\mathcal E\otimes M)
=\frac{r-1}{2r}c_1(\mathcal E\otimes M)^2
                     -c_2(\mathcal E\otimes M).       \tag{6}
\]

Thus invariance of the two Chern classes would imply invariance of
the original normalized character, because SU(2) preserves cup products. All twist
terms in ch_2 are divisor products. Kunneth and H^1(S,Q)=0 express
every divisor class on X as a sum from the two factors. Such
products act trivially on T, so the ch_2 action remains U.

**The necessary common-metric eigenvalue.** Each Kunneth summand of
H^4(X,R) is preserved by the diagonal SU(2) action. The two summands
H^4(S) tensor H^0(S) and H^0(S) tensor H^4(S) act trivially on H^2(S).
On the mixed summand identify a tensor sum a_i tensor b_i with

\[
v\longmapsto\sum_i q(v,a_i)b_i.
\]

The cup pairing is SU(2)-invariant, so the tensor identification is
equivariant: applying g to the tensor conjugates the associated
operator by g. An invariant degree-four class therefore has an
operator commuting with this SU(2) action.

The metric's three Kahler forms span
W_+=span_R(Re(sigma),Im(sigma),omega), after rescaling sigma if
needed. Unit quaternions act on them by the usual three-dimensional
rotations. In particular some element takes a nonzero multiple of
Re(sigma) to omega. If an equivariant real operator takes sigma to
lambda sigma, with lambda real, it takes Re(sigma) to
lambda Re(sigma); commutation with that rotation then forces

\[
T_{\nu(\mathcal E)}\omega=\lambda\omega.              \tag{7}
\]

This is a condition on the whole mixed class. Knowledge of its
action on T alone would not establish it, and the point-class
terms cannot alter it.

**The rational spectrum gives the contradiction.** The mixed part
of h^2 is 2 ell tensor ell. Equations (3) and (5) therefore give

\[
T_{\nu(\mathcal E)}|_N=2\,\mathrm{id}_N
                         +b\,\ell\,q(\ell,-).       \tag{8}
\]

Since ell^2=q(ell,ell)>0, N is Q ell direct sum ell^perp. On these
summands (8) has eigenvalues 2+b ell^2 and 2, respectively. Both
are rational, with characteristic polynomial

\[
(z-2)^3(z-2-b\ell^2).                                \tag{9}
\]

The monic cubic f has no rational root: its only possible rational
roots are 1 and -1, and f(1)=-1, f(-1)=1. Thus lambda is irrational.
No nonzero vector of N_R can satisfy (7) for (8). Since omega is a
nonzero vector of N_R, this contradicts invariance. Equations
(2) and (6) prove the assertion for every line-bundle twist.

The argument is uniform in the construction choices and in the
selected common metric with omega in N_R. It does not impose
c_1=0 as a substitute for invariance, confuse Hodge type on the
original product with SU(2) invariance, or change the Chern data
using a virtual subtraction. The normalized character is only a
necessary-condition test on an actual bundle. General stable-bundle
existence and transport to the missing NS-fixed direction remain
unresolved. The exact algebra certificate checks the twist identity
and rank-one characteristic polynomial; the geometric and metric
arguments above supply the other steps. Reproduce the certificate with
`python3 scripts/cubic-kahler/check_resolution_chern_certificate.py`.

## Mathlib

Coverage of the full statement: **not checked**. No matching
Mathlib declaration or absence from checked Mathlib sources is
claimed. Mistretta Theorem 3.1 supplies the stable resolution;
Verbitsky Proposition 1.2 and Theorem 2.5 supply the invariant-class
framework. Their direct links appear above. They support this
application rather than state its full exclusion. The projection
formula, Kunneth decomposition, Grothendieck--Riemann--Roch,
splitting principle and quaternionic rotation of the three Kahler
forms are the standard inputs used in the displayed proof.
