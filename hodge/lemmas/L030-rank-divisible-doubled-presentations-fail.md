# L030 — Doubled presentations with divisible factor classes fail the Chern test

## Hypotheses

Use S, X=S x S, C, N, A, omega and W=im(A) from L029. Write
Lambda=W intersect NS(S). Thus W is rational, contains the ample
class omega, and A omega=lambda omega, where

\[
f(\lambda)=0,\qquad f(z)=z^3+z^2-2z-1.
\]

Use the same metric on both factors and its diagonal SU(2) action.
Suppose there is an actual exact sequence

\[
0\longrightarrow E\longrightarrow P_2\longrightarrow P_1
 \longrightarrow P_0\longrightarrow Q_0\longrightarrow0,
\qquad Q_0=I_C\oplus I_C,                                  \tag{1}
\]

where E is locally free of positive rank r and each P_i is a sum of
product line bundles L_ij. Assume the two factor classes satisfy

\[
a_{ij},b_{ij}\in r\Lambda.                                 \tag{2}
\]

The divisibility in (2) is an additional restriction on this tested
construction, not a property of all sequences in L029. Let M be any
actual line bundle and put F=E tensor M.

## Conclusion

If c_1(F) and c_2(F) are SU(2)-invariant, then r is 1 or 2.
Consequently every sequence (1)--(2) with r>=3 fails the required
Chern condition, independently of its maps, stability, twist and
the rational chamber conjugation used in L025. This is a necessary
rank condition; neither remaining rank is asserted to occur.

There are actual mixed product-line presentations (1) with

\[
(\operatorname{rk}P_0,\operatorname{rk}P_1,
  \operatorname{rk}P_2;\operatorname{rk}E)=(8,10,8;4),        \tag{3}
\]

all factor classes in 4Lambda, and an integral product-line twist
with c_1(F)=0. The original factor classes can span W in both
factors. The construction uses generating sections, including at
the three non-lci points. Every such rank-four example fails invariant
c_2 after any twist having invariant c_1, by the first conclusion.
No assertion that these terminal bundles are stable is needed.

This excludes the uniform divisibility method for making the
terminal twist integral, including an actual generic-map construction.
It does not exclude arbitrary factor residue classes in Lambda,
arbitrary doubled-source presentations, or other compatible bundles.
It adds no algebraic class or transverse surface: the known span is
21-dimensional and the attained RM directions remain three against
four required. The universal Hodge conjecture remains unresolved.

## Proof

**Known tools and the difference being tested.** Reuse the prior
EXPLORE assessment for the exact doubled target. Chern additivity is
imported from the Stacks Project, [Lemma 42.45.2, tag 0F9C](https://stacks.math.columbia.edu/tag/0F9C)
and [Remark 42.56.11, tag 0FET](https://stacks.math.columbia.edu/tag/0FET).
L029 already specializes these tools and the invariant-form framework
to (1). The present difference is the arithmetic of (2) and its
compatibility with actual generation maps. The proof does not repeat
the Chern or SU(2) argument.

Serre's global generation theorem supplies sufficiently positive
twists of each actual coherent kernel. The reviewed multigraded
extension is Hering--Schenck--Smith, [Theorem 2.1, arXiv:math/0502240v2,
pp. 3--4](https://arxiv.org/pdf/math/0502240v2#page=3); it supplies
generation under its regularity hypotheses, not stability or the
present ranks. Here ordinary Serre generation suffices, applied
separately to each chosen ample product line bundle. The elementary
incidence argument below checks the specific numbers in (3) instead
of assuming that full evaluation, or an arbitrary proper subspace,
has the required maps. This is a reproduction/application of known
tools, with no originality claim.

**The integral normalized operator.** Put s_0=s_2=1, s_1=-1 and

\[
a=\sum s_i a_{ij},\qquad b=\sum s_i b_{ij},\qquad
\Theta=\sum s_i a_{ij}\otimes b_{ij}-\frac1r a\otimes b.
                                                               \tag{4}
\]

Write a_ij=r x_ij and b_ij=r y_ij with x_ij,y_ij in Lambda, and
put x=sum s_i x_ij, y=sum s_i y_ij. Then

\[
\frac{\Theta}{r}
 =r\sum s_i x_{ij}\otimes y_{ij}-x\otimes y
 \in\Lambda\otimes_{\mathbb Z}\Lambda.                       \tag{5}
\]

With the correspondence convention u tensor v acting by
w -> q(w,u)v, (5) gives an integral operator R/r on NS(S), where
R is the operator of Theta. This uses only the integral cup pairing;
no integral splitting of N into W and its complement is assumed.

If the first two Chern classes of F are invariant, L029 forces

\[
R=2(A-2\,\mathrm{id})\pi_W,
\qquad (R/r)\omega=\frac{2(\lambda-2)}r\omega.                \tag{6}
\]

Every eigenvalue of an integral matrix is an algebraic integer,
because its characteristic polynomial is monic with integer
coefficients. In particular theta=2(lambda-2)/r would be an
algebraic integer. The field Q(theta)=Q(lambda) has degree three:
f has no rational root (the only candidates are +/-1), and a
nonzero rational scaling and translation preserve the field.

The exact polynomial calculation is

\[
f(z+2)=z^3+7z^2+14z+7,
\]
\[
8f(z/2+2)=z^3+14z^2+56z+56.
\]

Thus the field norm is

\[
\operatorname{Nm}_{\mathbb Q(\lambda)/\mathbb Q}(\theta)
 =-\frac{56}{r^3}.                                         \tag{7}
\]

The norm of an algebraic integer to Q is an integer: its conjugates
have algebraic-integer product, and a rational algebraic integer is
an integer. Hence r^3 divides 56=2^3 times 7. For positive integral
r this permits only r=1 or r=2. This proves the exclusion for every
r>=3. For r=4 one can already see the failure from the trace of
R/r on W, namely -14/4, but (7) gives the uniform statement.

The argument retains every final line twist because the normalized
character and (4) are twist-invariant. It also retains any final
chamber: (5) uses its actual lattice Lambda, while (6)--(7) use the
unchanged cubic eigenvalue. No pre-chamber integral matrix is used.

**Integral mixed ample classes in the final W.** L025 gives
omega in W_R in the open ample cone. Since W is rational, Lambda
is a full rank-three lattice in W. The open intersection of that
cone with W_R contains three rationally independent rational points.
Multiplying each by a positive denominator gives three independent
ample integral classes d_1,d_2,d_3 in Lambda. They are represented
by actual ample line bundles D_1,D_2,D_3 on S. Here one uses the
usual equality of the ample cone and the Kahler cone in NS(S)_R;
positive square alone is not used as an ampleness test.

Products B=p_1^*D_u tensor p_2^*D_v are ample on X. At each
presentation stage choose the required number of such B_j, with
each index 1,2,3 occurring among both factor choices. For any
actual coherent target Q at that stage, choose m_j sufficiently
large that Q tensor B_j^(4m_j) is globally generated, and set

\[
L_j=B_j^{-4m_j}.                                           \tag{8}
\]

All factor classes belong to 4Lambda and span W in both factors.
All powers and all section maps in what follows are actual integral
line-bundle data. Their existence does not require an integral
matrix for L025's chamber conjugation.

**The incidence test for proper generating sections.** Suppose Q
has a finite stratification on which the fibre dimension
d(x)=dim_C(Q tensor k(x)) is constant, equal to d. For each of n
line summands L_j suppose Q tensor L_j^(-1) is globally generated.
The affine parameter space is

\[
V=\prod_{j=1}^n H^0(X,Q\otimes L_j^{-1}).
\]

At each point its evaluation onto the space of d by n fibre
matrices is surjective, because each column can be chosen
independently. For n>=d, the matrices of rank less than d have
codimension n-d+1. The bad incidence over a stratum of dimension
e therefore has dimension at most dim(V)+e-(n-d+1). If

\[
n-d+1>e                                                   \tag{9}
\]

on every stratum, the union of bad parameter images has closure
of dimension less than dim(V). A tuple outside that closure is
surjective on every fibre, hence defines a sheaf surjection by
Nakayama's lemma. This chooses one section for each negative line
summand, not its entire Hom space. The usual determinantal
codimension formula used here follows by specifying a rank-(d-1)
image and the map into it: that locus has dimension
(d-1)(n+1), of codimension dn-(d-1)(n+1)=n-d+1; lower ranks
have no greater dimension.

For these targets the strata are the smooth open pieces described
below and finitely many points, so the restriction sheaves have
constant locally free fibres there and this incidence count applies.
The bad surjectivity locus on X times V is closed; projectivity of
X also makes its projection closed. Thus the choices can be made
in a nonempty Zariski open set of actual maps at every stage.

**Local generator numbers for the doubled ideal.** L012 gives
projective dimension at most two for I_C, with singularities only
at the three surface double points. Off C the fibre generator
number of Q_0 is 2. On the smooth locus of C its ideal is generated
by a regular sequence of length two, so that number is 4.
At a double point the completed ideal is

\[
J=(r_1,r_2)(s_1,s_2)
 \subset R=\mathbb C[[r_1,r_2,s_1,s_2]],
\]

with four minimal generators. Tensoring the two length-one Koszul
resolutions of (r_1,r_2) and (s_1,s_2) gives its minimal resolution

\[
0\longrightarrow R\longrightarrow R^4\longrightarrow R^4
 \longrightarrow J\longrightarrow0.                       \tag{10}
\]

For exactness, r_1,r_2 is a regular sequence on R/(s_1,s_2),
so the corresponding positive Tor groups of the two quotient
rings vanish. Dimension shifting gives the required Tor vanishing
for their ideals and identifies their tensor product with their
product. Every entry of the Koszul differentials lies in the
maximal ideal, so the displayed resolution is minimal. Completion
preserves generator numbers and detects the local freeness used
below. The doubled ideal therefore has generator number 8 and
first-syzygy generator number 8 at each double point.

Use eight terms (8) for Q_0. The pairs (d,e) are (2,4), (4,2),
and (8,0). Their bad-rank codimensions are respectively 7,5,1,
all strictly greater than e. The incidence test supplies a
surjection P_0 -> Q_0 and a rank-six kernel Q_1.

Away from the three double points Q_0 has projective dimension
at most one, so Q_1 is locally free of rank six. At each double
point the rank-eight P_0 is a minimal free cover, because Q_0
needs exactly eight generators. By (10) its kernel has eight
minimal generators and projective dimension one. Thus Q_1 has
(d,e)=(6,4) off those points and (8,0) at them.

Choose ten terms (8) for this actual Q_1. The bad-rank
codimensions are 5 and 3, so another generic tuple is surjective.
Its kernel Q_2 is locally free of rank four, since Q_1 has local
projective dimension at most one. Finally eight terms (8) map
generically surjectively onto the actual Q_2: here d=4 everywhere
and 8-4+1=5>dim(X)=4. Their kernel E is locally free of rank four.
Composing the three surjections with their kernel inclusions gives
the exact sequence (1) and the ranks (3). The successive choices
are dependent on the previous kernels; no simultaneous genericity
or unverified multiplication-map hypothesis is being assumed.

**The integral twist and the stopping test.** Since every term
in (8) has both factor classes divisible by four, c_1(E) has
factor classes a=4a_0, b=4b_0 with a_0,b_0 in Lambda. Take the
actual product line bundle M with factor classes -a_0,-b_0.
The rank is four, so c_1(E tensor M)=0. This proves that actual
maps and an actual integral twist can be attained together in
the final W, rather than only in a formal pre-chamber model.

But (2) now holds with r=4, contradicting (7) if c_2 were also
invariant. Thus this concrete way to reconcile generation and
twist integrality fails before stability is decided. The earlier
split full-evaluation procedure is not being relabelled as a new
counterexample: the incidence argument allows proper generating
spaces and mixed line summands, and its exclusion uses their
divisibility. No splitting of these maps is asserted.

The alternatives left out of (2), including arbitrary integral
residues and possible rank-two terminal constructions, require
different presentation data and remain unresolved. This proof
does not compute any new Atiyah obstruction or permit an
inference about rational cycle classes from integral divisibility.

## Mathlib

Coverage of the full statement: **not checked**. No full Mathlib
match or absence from checked sources is asserted. The directly
linked Stacks results support Chern additivity; Hering--Schenck--Smith
supports conditional generation. Verbitsky's conditional
[Theorem 2.5, arXiv:alg-geom/9307008v1, p. 9](https://arxiv.org/pdf/alg-geom/9307008v1#page=9)
requires an existing stable bundle with invariant Chern classes and
does not supply one here. Serre global generation, the Koszul
resolution of a regular sequence, Nakayama's lemma, determinantal
rank loci, and integrality of eigenvalues and field norms are the
named supporting inputs. None is cited as a match for the complete
doubled-source target; the scoped calculation above is not a
certified originality claim.
