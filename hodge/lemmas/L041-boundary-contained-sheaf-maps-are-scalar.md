# L041 — Boundary-contained stable sheaf maps have scalar action

## Hypotheses

Let S be a smooth projective complex K3 surface. Set
T=T(S)=NS(S)_Q^perp for the cup-product form q, and assume
that T has rank eighteen and its **full** Hodge endomorphism
field is

\[
\operatorname{End}_{\mathrm{Hdg}}(T)
 =E=\mathbb Q(\zeta_7+\zeta_7^{-1}).
\]

Let H be general in Yoshioka's sense and v-generic for
v=(2,0,-1). Retain these polarization hypotheses. Put
M=M_H(2,0,-1), choose an untwisted universal sheaf P on
M x S, and let f:S -> M be an algebraic morphism defined
on all of S. Write F=(f x id_S)^*P and let p,q:S x S -> S
denote the parameter and sheaf-factor projections.

Use the quotient Q, leading associated cycle Gamma_Q and
actual weighted-support morphism of L039. By L040 this
support is g=Phi_Q=rho Psi f:S -> S^{(3)}, where Psi is
Yoshioka's specified isomorphism and rho is Hilbert--Chow.
Assume that the whole image of g lies in the reduced
collision locus Delta: every support cycle has a repeated
point. No dominance or generic (2,1) hypothesis is imposed.

Use Markman's convention (0,t,0)^vee=(0,-t,0), so that
L039 gives the positive weighted action

\[
\alpha_f(t):=f^*\theta_v(0,t,0)
 =p_*\bigl(q^*t\smile[\Gamma_Q]\bigr).
\]

## Conclusion

There are unique regular morphisms a,b:S -> S such that

\[
g(s)=2a(s)+b(s)
\quad\text{as a weighted degree-three cycle},
\qquad
\Gamma_Q=2[\Gamma_a]+[\Gamma_b]
\tag{1}
\]

as dimension-two cycles on S x S, with
Gamma_h={(s,h(s)):s in S}. This includes a=b and images
contained in smaller subsets of either collision stratum.

For every t in H^2(S,Q),

\[
\alpha_f(t)=2a^*t+b^*t.
\tag{2}
\]

For any regular h:S -> S occurring here, let epsilon_h be
zero if h is nondominant, and the sign of h^*|_T if h is
dominant. Then epsilon_h belongs to {0,1,-1}, and

\[
\alpha_f|_T=(2\epsilon_a+\epsilon_b)\operatorname{id}_T.
\tag{3}
\]

In particular the coefficient is an integer between -3 and
3. This is a necessary bound for existing stable maps, not
an assertion that every coefficient or pair (a,b) has a
stable lift. The rational span of all these actions has
dimension at most one, against the three required by E.
They supply no non-scalar cubic-RM endomorphism.

## Proof

**Known inputs and the precise specialization.** Import the
partition-stratum normalization from de Cataldo--Migliorini,
[*The Douady Space of a Complex Surface*, Lemma 3.3.1,
printed p. 299](https://www.math.stonybrook.edu/~mde/MyPublishedPapers/DouadySpaceCplexSfceAdvances.pdf#page=18),
in the algebraic form stated in [*The Chow Groups and the
Motive of the Hilbert Scheme of Points on a Surface*,
section 2, printed p. 827](https://www.math.stonybrook.edu/~mde/MyPublishedPapers/MotiveHilbSchJournOfAlg.pdf#page=4).
For the partition (2,1), this gives the finite normalization

\[
\nu:S\times S\longrightarrow\Delta,\qquad(x,y)\longmapsto2x+y.
\tag{4}
\]

Finiteness can also be read from [Stacks, Lemma 33.27.1,
Tag 0BXR](https://stacks.math.columbia.edu/tag/0BXR).
These known statements concern the entire stratum closure,
including triple collisions. Their reproof is unnecessary.
What needs checking here is a regular lift of a possibly
nondominant parameter map, followed by its actual action.

**Regular descent without dominance of the stratum.** The
assumption on g's image makes g factor through the reduced
Delta as a morphism. Indeed every section of its defining
ideal pulls back to a regular function vanishing at all
closed points of a reduced finite-type complex scheme, so
that pullback is zero.

For every algebraically closed extension Omega of C, a
cycle in Delta(Omega) has the form 2x+y with x != y or
3x. In the first case x is its unique repeated point; in
the second the only pair is (x,x). Thus nu has exactly
one geometric point in every geometric fibre. This checks
more than birationality, which alone would not justify the
nondominant lift used below.

Form Z=S x_Delta (S x S). Its projection to S is finite
and surjective. Let eta be the generic point of S and
K=C(S). The finite K-scheme Z_eta has exactly one geometric
point after extending to an algebraic closure of K. Its
reduction is therefore Spec L for a finite extension L/K.
All finite field extensions in characteristic zero are
separable, so that extension has [L:K] geometric points.
Consequently L=K. Nilpotents in Z_eta do not affect this
argument or the reduction.

There is exactly one irreducible component W of Z dominating
S. Give it the reduced structure. It is integral, finite
over S, and has generic fibre Spec K. Hence W -> S is finite
and birational. Since S is normal, [Stacks, Lemma 29.55.8,
Tag 0AB1](https://stacks.math.columbia.edu/tag/0AB1)
makes it an isomorphism. Composing its inverse with the
second projection Z -> S x S gives the required regular
lift (a,b) of g. No dominance of g onto Delta has been used.
In particular this construction also applies when the
entire image is in the triple stratum, a curve, or a point.

Any two lifts agree at every closed point because the
geometric fibre in (4) has one point. The target is separated
and S is reduced and Jacobson, so their equalizer is all
of S as a scheme. The lift is unique. If the entire image
is triple, this same argument gives a=b as morphisms.

**The actual leading cycle across further collisions.** L039
supplies a flat length-three quotient Q with support finite
over the parameter S, not merely a pointwise CH_0 class.
At every closed s its support points and their lengths are
those of 2a(s)+b(s). Nakayama's lemma and the closed-point
description show that its reduced support is the union of
the two graphs. In particular no other dimension-two support
component can occur.

If a and b are different as morphisms, they are distinct
over the generic point of S. The two generic-stalk lengths
of Q are respectively two and one, since its generic
support cycle is 2a(eta)+b(eta). If a=b, its unique generic
support length is three. These are exactly the generic
lengths defining the associated cycle Gamma_Q in L039.
Also, any subset of the support over a proper closed subset
of S has dimension at most one, because the projection is
finite. It contributes nothing to this dimension-two cycle.
Thus in both cases Gamma_Q=2[Gamma_a]+[Gamma_b], proving (1).
Crossings of the two graphs and punctual module data add
no further leading-cycle component. Flatness of the support
scheme itself has not been assumed.

For a graph i_h:S -> S x S, p i_h=id_S and q i_h=h.
The projection formula consequently gives

\[
p_*\bigl(q^*t\smile[\Gamma_h]\bigr)=h^*t.
\]

Apply this identity to (1) and L039's positive weighted
action to obtain (2). Thus raw ch_2, reduced unweighted
support and any choice of punctual tangent direction have
not replaced the normalized universal-sheaf convention.
L040 ensures that the collision condition imposed on
Hilbert--Chow is precisely this actual support condition.

**Regular component maps on the transcendental space.** First
check that every regular h:S -> S preserves T. For d in
NS(S)_Q and t in T, the projection formula gives

\[
q(h^*t,d)=q(t,h_*d)=0.
\]

Here h_*d is an algebraic divisor class (possibly zero):
proper pushforward sends each divisor curve to its image
with its degree, or to zero if its image has smaller dimension.
Hence h^*t is orthogonal to NS(S)_Q. Pullback is a rational
Hodge map, so h^*|_T is a Hodge endomorphism of T.

If h is nondominant, its generic differential has rank at
most one, so h^*omega=0 for the holomorphic two-form omega.
This vanishes globally since it vanishes on a dense open
subset. Import the transcendental irreducibility and
holomorphic-line detection statement from [Huybrechts,
*Lectures on K3 Surfaces*, Chapter 3, Lemma 2.7, author
draft PDF p. 48](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=48).
A Hodge endomorphism of T killing its (2,0)-line is zero.
Thus h^*|_T=0, including curve and point images.

If h is dominant, import [Dedieu, *Severi varieties and self
rational maps of K3 surfaces*, arXiv:0704.3163v1,
introduction 0.2, PDF pp. 1--2](https://arxiv.org/pdf/0704.3163v1#page=2):
a dominant regular self-morphism of a complex projective
K3 surface is an automorphism. This uses regularity; it
does not assert the same thing for rational self-maps.
Its pullback is therefore a rational Hodge self-isometry
of T. The full field E is totally real, so import [Huybrechts,
Chapter 3, section 3.5, author draft PDF p. 59](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=59)
to conclude h^*|_T=+id_T or -id_T. This general-K3 source
input was already recorded in foundations/07. The quartic
statement of L004 is not being applied outside its hypotheses,
and no new isometry theorem is reproved here.

Substituting these component actions in (2) proves (3).
In the entirely triple case the same computation is
3a^*|_T; the nondominant and dominant cases already cover it.
Base-line-bundle changes of P leave the action unchanged by
L039. Exceptional Hilbert-cube lift data can affect the map
f but not this leading weighted cycle or its action on T.

This completes the saved test by a specialization and
reproduction of known normalization, regular-map and Hodge
inputs. No claim of progress beyond the checked literature
or certified originality is made. The bound stops the whole
boundary-contained supply, without excluding maps generically
outside the collision locus or arbitrary correspondences.
It supplies no new algebraic class or transverse surface:
the already covered cubic-family span remains 21, and its
three attained RM directions remain short of four. The
universal Hodge target remains unresolved.

## Mathlib

Coverage: **not checked** for the full scalar-action statement
or its symmetric-product normalization, finite descent, K3
map and universal-sheaf inputs. No absence from checked
Mathlib sources is claimed. The direct de Cataldo--Migliorini,
Stacks, Dedieu and Huybrechts references match the separate
supporting statements, not a theorem stating this full action
bound. The finite-pullback, generic-length and weighted-action
applications above are the identified specialization. L039
and L040 retain their stated source coverage and qualifications.
