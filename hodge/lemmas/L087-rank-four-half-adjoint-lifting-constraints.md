# L087 — Rank-four half-adjoint constraints exclude spin, retain nonspin

## Hypotheses

Use L079's conditional t=1 stable symmetric acyclic rank-four block
K=K_4 on its marked projective K3 S, at L052's identical real Kähler
class h. Thus K is actually locally free and h-stable, has integral
c_1(K)=0, c_2(K)=8 eta, and inherits the actual compatible
hyperholomorphic unitary connection and perfect parallel symmetric
form. Here integral_S eta=1. This is conditional on the L079 branch;
neither that branch nor its common product kernel F is constructed.
Use L052's exact perpendicular lattice Zk, k^2=-14, and its primitive
elliptic fibre divisor f_ell, f_ell^2=0. Use L061's ordinary versus
Brauer-twisted lifting and descending-index conventions, not its old
rank-three image or its numerical exclusion.

## Conclusion

Normalize the form compatibly with the connection and choose an
orientation of its real rank-four reduction R. Write e(R)=t eta;
this t is an Euler number, distinct from L079's trivial-line count.
There are actual holomorphic parallel rank-three half-adjoint bundles
A_+, A_-, with compatible connections at the same h. Label them so
that

\[
p_1(R)=-8\eta,\quad
c_1(A_\pm)=0,\quad c_2(A_\pm)=d_\pm\eta,
\qquad d_+=8-2t,\quad d_-=8+2t.                 \tag{1}
\]

Their projective rank-two factors have one common SL2 obstruction
w=w_2(R) and common Brauer image alpha. Their local rank-two lifts
have descending endomorphism bundles O_S plus A_±, are simple, and
have individual self-Ext dimensions

\[
(1,2-2t,1),\qquad(1,2+2t,1).                  \tag{2}
\]

Consequently the following are necessary:

\[
t\in\{-1,0,1\},\qquad w\ne0,\qquad
\mathcal P(w)=2t\,\rho_4(\eta),\qquad
w_4(R)=t\,\rho_2(\eta).                       \tag{3}
\]

The spin case w=0 is impossible. The surviving lifting alternatives
for these tests are:

* **Ordinary nonspin:** alpha=0 and w is the reduction of divisor
  classes. Every ordinary rank-two lift E_± is h-stable, with arbitrary
  determinant l_± in NS(S), and
  \[
  \rho_2(l_+)=\rho_2(l_-)=w\ne0,\quad
  l_\pm^2\equiv2t\pmod4,\quad
  4c_2(E_\pm)-l_\pm^2=d_\pm,\quad
  v(E_\pm)^2=d_\pm-8=\mp2t.                 \tag{4}
  \]
  Determinants need not have zero h-degree. If an individual
  determinant has zero degree, it is l_±=rk with r odd, and t must
  equal +1 or -1. These zero-degree possibilities also pass its
  section/Euler necessary test.
* **Brauer-twisted:** alpha is nonzero and the two rank-two factors
  are alpha-twisted (more precisely they admit local determinant-one
  lifts with the same mu_2 cocycle w). Their descending End bundles,
  not imaginary ordinary Chern classes, give (2) and twisted Mukai
  squares ∓2t. Both lie at least -2. No further obstruction on these
  cases is obtained here beyond (3).

Each Euler value in (3) has an ordinary formal numerical witness:
t=0 permits l_+=l_-=f_ell and charges 2,2; t=1 permits
l_+=l_-=k and charges -2,-1; t=-1 reverses the latter charges.
These witnesses satisfy the stated characteristic and simple-index
constraints; they do not assert existence, tensor stability or
acyclicity at h. Twisted compatibility is conditional on its actual
obstruction class, not a claim that every class in (3) is realized.

This is an informative NEGATIVE / REPRODUCTION specialization of known
tools: it narrows one image branch and removes its spin alternative,
but **does not exclude K_4 or F**. Stop this bounded lifting/index
filter. No common kernel, algebraic cycle, transverse transport or
resolution of the universal primitive Hodge gap is supplied. The
separate critical audit of 2026-10-11 preserves these conditional
conclusions and the stop; it supplies no existence assertion.

## Proof

**Actual parallel half-adjoints.** L079 supplies a parallel real
reduction, not merely a topological class. In its normalization,
if Q(u,v)=g(u,Jv), replace J by its parallel isometric antilinear
involution j=J(J^2)^(-1/2). The symmetric form Q_0(u,v)=g(u,jv)
is parallel, holomorphic and nondegenerate, and on R=Fix(j) it
is the positive real metric g_R. It need not equal the initial
Q; this replacement preserves K and its actual connection.
Since S is simply connected, R is orientable. Its metric-oriented
volume form is parallel and holomorphic after complexification,
so the associated complex orthogonal frames form an SO4(C) torsor.
The real metric Hodge star on Lambda^2 R is parallel, squares to
one, and has two real rank-three eigenspaces. Its complex-linear
extension therefore gives global holomorphic parallel summands

\[
\Lambda^2K=A_+\oplus A_-.
\]

They inherit the same curvature type and zero Kähler contraction:
induced connection curvature is a Lie-algebra representation of
K's invariant curvature, and the two projections are parallel.
In particular their Chern connections are zero-Einstein at the
unchanged h. No surface Hodge star on differential forms is being
confused with this star on the coefficient bundle R.

Import Choe--Hitching, *Low rank orthogonal bundles and quadric
fibrations*, [arXiv:2203.06645v2, introduction and Section 2.3,
pp. 1,5](https://arxiv.org/pdf/2203.06645v2), for
Spin(4,C)=SL2(C) x SL2(C) and its standard rank-four tensor
representation. The Lie algebra decomposition identifies these
two half-adjoints with the two traceless rank-two End representations.
Theorem 4.2 over curves is not applied: no rank-two isotropic
subbundle or ordinary tensor factors on this K3 are assumed.

**One cocycle and the actual coefficient representation.** Take a
sufficiently small analytic cover and holomorphic lifts of K's
orthogonal transitions to pairs (g_ij^+,g_ij^-) in SL2 x SL2.
On triple overlaps their products are (epsilon_ijk,epsilon_ijk),
with epsilon_ijk in {1,-1}: this is precisely the kernel of the
cover onto SO4. Their two tensor transitions therefore have
triple product one and are exactly the transitions of K under
the standard representation, not an independently chosen bundle.
The two local determinant-one rank-two factors are twisted by
the same sign cocycle, and that twist cancels in their tensor.
Conjugation descends, giving honest bundles

\[
\operatorname{End}(E_\pm)=\mathcal O_S\oplus A_\pm.       \tag{5}
\]

The homomorphisms a -> a tensor 1 and b -> 1 tensor b also descend
as injective holomorphic algebra maps from these End bundles to
End(K). Their images intersect only in scalar endomorphisms.
Since K is stable, H^0(End K)=C; hence each factor has only
scalar descending endomorphisms. This proves simplicity even
when its rank-two bundle exists only on the gerbe.

The same central cocycle on the compact reduction is the defining
spin obstruction w_2(R). It is also the obstruction for either
SO3 half-adjoint to lift to SU2. Import Grove--Ziller,
*Lifting Group Actions and Nonnegative Curvature*,
[arXiv:0801.0767v1, Proposition 1.8 and (1.10)--(1.11),
pp. 7--8](https://arxiv.org/pdf/0801.0767v1): the two SO3
obstructions agree and p_1(P_±)=p_1(R)±2e(R). Their Proposition
3.3, p. 11, preserves the independent real Euler invariant.
S is compact, simply connected and real four-dimensional;
no group-action assumption is used in these bundle statements.
Complexification gives p_1(R)=-c_2(K)=-8 eta and
p_1(P_±)=-c_2(A_±), yielding (1). Reversing orientation exchanges
the labels and negates t. The Euler class here is not c_4(K),
which on a surface is zero for dimensional reasons.

Import Yoshioka, *Moduli spaces of twisted sheaves on a projective
variety*, [arXiv:math/0411538v2, Section 1.1 and Lemmas 1.2--1.4,
p. 2](https://arxiv.org/pdf/math/0411538v2), as covered in L061:
alpha is the image of w in H^2(O_S^*), alpha=0 iff w is in NS
modulo two, and an ordinary lift has determinant reduction w.
Thus ordinary liftability holds simultaneously for the two factors;
it does not follow from c_1(K)=0 or from the base being spin.

There are two different central covers here. The kernel of
SL2 x SL2 -> SO4 is the diagonal {(+1,+1),(-1,-1)}. The further
map SO4 -> PGL2 x PGL2 has kernel {+Id_K,-Id_K}; it records the
two adjoint actions. The first cover supplies w, while the second
accounts for the possible difference between two normalized tensors
with identified projective factors. Neither kernel may be omitted.

If alpha=0 and E_± are ordinary lifts, identify their projectivizations
with the actual factors above and refine the analytic cover. In the
chosen frames their transitions are e_ij^±=a_ij^± g_ij^± for
nowhere-zero holomorphic scalar functions a_ij^±. The ordinary
cocycle equations say that the triple product of each a^± is
epsilon_ijk^{-1}=epsilon_ijk. Thus a_ij^+ a_ij^- is an honest
line-bundle cocycle. Set m_ij=(a_ij^+ a_ij^-)^{-1}. These are
the transitions of a line M, and since det(g_ij^±)=1 they give
M^2=(det E_+ tensor det E_-)^{-1}. Now

\[
(e_{ij}^+\otimes e_{ij}^-)m_{ij}
   =g_{ij}^+\otimes g_{ij}^-.
\]

These are exactly K's transitions. The product of the two
determinant-wedge alternating forms gives the symmetric form on
the tensor; the displayed normalization identifies it and its
orientation with K's, after compatible constant choices. In terms
of classes, equality of l_± modulo two makes their sum twice an
integral (1,1)-class, hence twice an NS class by Lefschetz (1,1).
This agrees with the explicit line M, without half-normalizing
either determinant separately. If one instead first chooses a
square-root line and compares the two SO4 lifts, their remaining
central discrepancy for the second cover is a mu_2 torsor. It is
trivial: the Kummer sequence and Pic(S)[2]=0 give H^1(S,mu_2)=0
(all nonzero complex constants have square roots). This also
checks the ambiguity in those choices. No ordinary factors have
been constructed when alpha is nonzero.

**Spin and ordinary lifts inherit exact-h stability.** In the spin
case w=0 the actual lifted compact connection is an SU2 x SU2
connection. Each factor has invariant curvature with zero
contraction, so its induced holomorphic determinant-trivial bundle
is h-polystable by the Hermite--Einstein correspondence used in
L052. For an ordinary lift E, the compact projective reduction
supplied by K specifies a smooth projective Hermitian metric on
the actual holomorphic P(E). Choose an HE Hermitian metric on
the actual holomorphic det(E) at h. These determine a genuine
global Hermitian metric on E as follows. In a holomorphic frame
let H_0 be any positive Hermitian matrix representing the projective
metric and let delta>0 represent the determinant metric. Set

\[
H=\left(\frac{\delta}{\det H_0}\right)^{1/2}H_0.
\]

Its determinant is delta. Replacing H_0 by a positive scalar
multiple does not change H, and under a change of holomorphic
frame the two sides transform by the same Hermitian congruence.
Equivalently, each fibre has a unique positive metric with the
prescribed projective class and determinant metric. This uniqueness
proves gluing and smoothness globally; it needs no square-root
determinant line.

Take the Chern connection D_H of this metric on the given
holomorphic E. Its projectivization is the prescribed projective
connection: both preserve the same projective metric and the same
projective (0,1) operator, so local Chern uniqueness identifies them.
More explicitly, multiplying H_0 by a positive function changes
H_0^{-1} partial H_0 only by a scalar one-form, and hence leaves
its projective connection unchanged. The determinant connection of
D_H is exactly the chosen determinant Chern connection, by the
same uniqueness or by tracing H^{-1} partial H. The Lie algebra
map u(2) -> pu(2) plus iR, taking projective part and trace, is
an isomorphism; thus these two specified connections also determine
D_H uniquely. In particular its local expression is the actual
trace-free projective connection plus one half of the determinant
connection, with the required inhomogeneous frame-change terms.
It is not a connection on some different holomorphic lift.

The trace-free curvature has zero contraction at h by the induced
connection on A_±, and the determinant curvature has constant
contraction. Both have type (1,1). Hence D_H is HE at the lift's
own unrestricted slope, and E is h-polystable.

The precise ordinary local rules used here are Chern uniqueness
and induced tensor/determinant connections: Perego,
*Kobayashi--Hitchin corrispondence for twisted vector bundles*,
[arXiv:1910.01867v1, Lemma 2.25, pp. 18--19, Lemmas 2.32--2.34
and the exterior/determinant discussion, pp. 22--24](https://arxiv.org/pdf/1910.01867v1),
with twist one and zero B-field. These are manuscript page numbers.
The line HE metric and compact-Kähler correspondence are Huybrechts,
*Lectures on K3 Surfaces*, author-hosted draft,
[Chapter 9 Section 4.2, Remark 4.8(i) and Theorem 4.9,
pp. 181--182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=181).
They apply at the given real Kähler form, without a rational
polarization hypothesis. The metric construction above verifies the
additional prescribed-connection compatibility; no projective-lifting
existence theorem is being substituted for it.

For completeness the ordinary normalized tensor also respects the
original connection. Give M the metric whose square is the dual
of the product determinant metrics. In each local SL2 frame its
Chern connection cancels the sum of the two half-determinant
scalar parts. The remaining connection is precisely the tensor of
the two actual projective trace-free connections. The transition
identity above identifies this with K's SO4 connection; any finite
central ambiguity has already been removed. This checks compatibility,
not existence of ordinary factors in a nonzero-Brauer case.

If a factor were polystable but not stable, its equal-slope summand projection
would be a nonscalar global endomorphism. Through (5) and its
injection into End(K) this contradicts K's simplicity. Hence
both spin factors and every ordinary lift are strictly h-stable.
This argument neither assumes half-adjoint stability nor restricts
arbitrary determinants to the zero-slope lattice.

**Separate indices and characteristic congruence.** Each descending
End bundle in (5) has rank four, first class zero and charge d_±.
Surface RR and Serre duality therefore give

\[
\chi(\operatorname{End}E_\pm)=8-d_\pm,\qquad
h^0=h^2=1,\qquad h^1=d_\pm-6.                 \tag{6}
\]

For twisted factors these are their self-Ext dimensions: local
freeness on the gerbe makes the descending Hom bundle compute
Ext, as in L061. Import Yoshioka v2,
[Definition 3.1, (3.3), and Proposition 3.6, pp. 7--8](https://arxiv.org/pdf/math/0411538v2),
for twisted Mukai square -chi(E,E) and its simple-sheaf bound -2.
Simplicity has already been proved, so both d_± must be at least
six. Inserting (1) gives -1<=t<=1, and integrality of e gives
exactly the three Euler numbers stated. Their Mukai squares are
-2t,+2t, and their middle dimensions are those of (2); all are
nonnegative and even. The total half-adjoint middle dimension is
four, consistent with the aggregate adjoint index in L079.
The separate indices supply the new restriction on e.

Yoshioka v2, [Lemma 3.1, p. 6](https://arxiv.org/pdf/math/0411538v2),
as used in L061, gives for each projective factor

\[
d_\pm\equiv-\xi^2\pmod4                       \tag{7}
\]

for any integral lift xi of w. Such a lift exists because
H^3(S,Z)=0. By the integral-lift property of the Pontryagin square,
(7) is P(w)=-d_±=2t modulo four. Both signs agree, since their
difference is 4t. The top Stiefel--Whitney class of an oriented
real rank-four bundle is its Euler class modulo two, giving the
last condition in (3). No w_4 vanishing has been assumed.

If w=0, the two spin factors have determinant zero and, by (1),
charges d_+/4 and d_-/4, whose sum is four. L052's exact-h stable
rank-two test requires each charge to be at least four: sections
and dual sections vanish at slope zero and chi=4-c<=0. Their
sum would be at least eight, a contradiction. This excludes spin
independently of which Euler number had passed (6).

**Nonspin arithmetic and its limits.** For ordinary lifts, the
rank-two root calculation in L061 gives

\[
d_\pm=4c_2(E_\pm)-l_\pm^2,\quad
\operatorname{ch}_2(E_\pm)=(l_\pm^2-d_\pm)/4,\quad
v(E_\pm)=(2,l_\pm,2+(l_\pm^2-d_\pm)/4).
\]

Thus v(E_±)^2=d_±-8 and (4) follows. Surface RR gives
chi(E_±)=4+(l_±^2-d_±)/4. This Euler value is not assigned
nonpositive sign for an arbitrary nonzero-slope determinant.
If l_± has zero h-degree, L052 gives l_±=rk. Nonspin forces r
odd, since even r would give w=0. Its square is then 2 modulo
four, so (7) forces t=±1. Its charge may be negative: for
r odd and d equal to six or ten the discriminant is still d>0.
Its Euler value is at most -1 or -2 respectively, so stable
slope-zero section and dual-section vanishing is numerically
compatible. No rank-two charge-four bound is applied with a
nonzero determinant.

For t=0, the formal ordinary choice l_+=l_-=f_ell has nonzero
common w, P(w)=0 and charges 2,2. Its nonzero determinant degree
prevents the determinant-zero section argument; both simple
middle dimensions are two. For t=1, choose both determinants k:
d_+=6,d_-=10, charges -2,-1, Mukai squares -2,+2 and middle
self-Ext dimensions zero,four. Both factor Euler values are
negative and compatible with their zero slopes. Reverse labels
for t=-1. Each pair has an integral normalized tensor line M,
as above. These examples are only formal witnesses for the stated
necessary numerical tests; no individual lift, stable tensor or
acyclic rank-four bundle is constructed.

For alpha nonzero, one instead uses (5)--(7) and the two simple
twisted indices. An ordinary determinant, ordinary section index
or integral half-determinant normalization is unavailable and is
not substituted. These constraints leave the listed Euler numbers
and eligible nonzero w with the corresponding Pontryagin-square
residue; they do not select the actual w or assert exact-h existence.
The compatible ordinary examples already suffice to show that
this filter cannot exclude the branch. Stop it while preserving
all other L079 alternatives and the earlier aggregate-index and
natural-projector stops. The main primitive Hodge gap is unchanged.

**Separate critical audit, 2026-10-11.** The full conditional proof
was checked against L079's actual stable block, L052's fixed-metric
lattice and section test, and L061's lifting and descending-index
conventions, using the separately approved source coverage. No
substantive error or stronger obstruction was found. The audit makes
the two covers, normalized scalar cocycles and global ordinary-lift
metric/Chern gluing explicit above; it does not add an existence
theorem or change the mathematical conclusions.

The coefficient star is parallel for the actual connection, so its
eigenspaces are holomorphic via that connection's (0,1) part. The
Euler number remains independent of the complex top Chern class.
The common sign cocycle cancels in the tensor representation and
in each descending End; simplicity precedes the use of either HE
stability or a simple twisted index. The metric construction does
not require stable A_±, a square root of an individual determinant,
or integrality of h. For the twisted factors local freeness and
the descending Hom calculation, rather than ordinary Chern roots,
give both self-Ext indices.

Explicitly, at t=-1,0,1 the pairs (d_+,d_-) are (10,6), (8,8),
(6,10), with middle self-Ext dimensions (4,0), (2,2), (0,4).
The congruences -d_+=-d_-=2t modulo four agree; spin factors
would still have charges summing to four against at least eight
required by their two determinant-zero stability tests. The
ordinary formal witnesses keep nonzero common w: f_ell at t=0
has nonzero degree, while k at t=1 has charges -2,-1 and Euler
values -1,-2; reversing labels treats t=-1. An odd multiple of k
has square 2 modulo four and gives no section-index contradiction.
Neither these arithmetic checks nor the compatible twisted squares
select actual w or alpha, establish the factors, or give a stable
acyclic tensor or common F. The original stop is retained. This
audit is EXPLORATION / REPRODUCTION, with no mathematical advance
beyond the unchanged necessary constraints.

## Mathlib

The full holomorphic half-adjoint, twisted lifting and exact-h
specialization is **not checked** in Mathlib; no absence claimed.
The precisely cited group, characteristic, lifting and simple-index
results are imported. The actual connection, common cocycle,
simplicity, stable-lift applicability and numerical specialization
are the local REPRODUCTION required for this conditional image.
No complete Hodge candidate or new algebraic class is obtained.
