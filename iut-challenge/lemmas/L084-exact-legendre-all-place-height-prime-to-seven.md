# L084 — All-place multiplicative reduction and prime-to-seven height over exact G

## Hypotheses

Retain L073's same auxiliary curve E=E_aux/Q and Galois number field
F_aux=Q(zeta_60,E[30]), with

    [F_aux:Q] dividing 2^14*3^3*5.

Over Q_3 this very E is the split Tate curve with its changed parameter
q_aux in Q_3 satisfying v_3(q_aux)=30, where v_3(3)=1. No equality
q_aux=3^30 is assumed. Retain L077's actual choices of distinct roots
r_i,r_j,r_k, D=r_j-r_i, s^2=D, t=(r_k-r_i)/D, and F'=F_aux(s).
In particular [F':F_aux]<=2, and the pointed F'-isomorphism is

    phi:E -> E_L, (x,y) -> ((x-r_i)/D, y/(Ds)),
    phi^(-1):(X,V) -> (r_i+DX, DsV),
    E_L: V^2=X(X-1)(X-t).

Retain L078's literal field G=Q(t)(iota,E_L[15]) subset F', with
both coordinates of every geometric torsion point included. L081
gives semistability of this E_L at every finite G-place. Work with
the same number fields and choices; G/Q is not assumed normal.

## Conclusion

At every place v of G above 3, E_L has multiplicative reduction
(possibly nonsplit). Its local height in the GenEll Definition 3.3
and Remark 3.3.1 convention, with the valuation on G_v surjective
onto Z, is the positive integer

    h_v=30e(G_v/Q_3),    gcd(7,h_v)=1.

This applies to all v above 3, not merely L078's induced place.
The unchanged embedded completions H,N remain as in L078.
This is a known-method specialization validated by the separate
step333 critical audit below. It supplies one local prerequisite, not sufficient initial
data, G/Q normality, an essential IUT flaw or finite B>=A.

## Proof

### Imported results and scope

Reuse the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-19-exact-legendre-all-place-q-order.md`.
Its inspected primary results, with the versions recorded there, are
the following. No general theorem is reproved here.

J. H. Silverman, *The Arithmetic of Elliptic Curves*, second edition
(2009), [VII Proposition 5.4(b), pp.197–198](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf),
gives persistence of good and multiplicative reduction under finite
extension. Its multiplicative case does not require splitness.
[C Theorem 14.1(b,d), p.445](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf)
gives Tate uniformization for nonintegral j and the quadratic splitting
description; in the nonsplit multiplicative case the splitting
extension is unramified. K. Kedlaya, *Introduction: the Tate curve*,
fall 2004, [Theorems 1–2, pp.3–4 and equation (3), p.2](https://kskedlaya.org/18.727/tate-curve.pdf),
gives the finite-Q_p-extension Tate construction and geometric
uniqueness of the parameter of positive valuation. Thus a pointed
isomorphism to Tate(q_aux) uses that same geometric Tate parameter.

S. Mochizuki, *Arithmetic Elliptic Curves in General Position*,
Math. J. Okayama Univ. 52 (2010), 1–28,
[local setup pp.16–17, Definition 3.3 and Remark 3.3.1, p.17](https://www.math.okayama-u.ac.jp/mjou/mjou52/_01_mochizuki.pdf),
uses a surjective integer valuation and defines height as the order
of the Tate parameter in the split setup. For potentially
multiplicative reduction, Remark 3.3.1 computes height over an
extension with multiplicative reduction and divides by that
extension's ramification index; the result is independent of the
extension. In particular a split extension can be used for a
nonsplit multiplicative curve. This is not a point's canonical local
height. The argument below computes this convention explicitly.

J. S. Milne, *Algebraic Number Theory*, v3.08 (19 July 2020),
[Exercise 4-2, p.83 and solution p.155; Corollary 7.42 and Remark
7.43, p.124](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
gives multiplicativity of ramification indices in towers, local
degree ef, and restriction of integer valuations. No normality is
required for these identities. Use also its Proposition 3.34,
pp.59–60, for e dividing the degree in a Galois number-field
extension, and section 8, pp.135–136, for induced completions of
finite extensions. These are the inspected tower/completion results
of the assessment. They will be applied separately over F_aux and G.

### An arbitrary place and the actual pointed comparison

Fix any v|3 of G. Extend this place to z of the finite number-field
extension F'/G, and let a be z restricted to F_aux. Such an extension
exists for a finite number-field extension. Write

    K=G_v, L=F'_z, A=(F_aux)_a.

The two inclusions G subset F' and F_aux subset F' give finite local
extensions L/K and L/A. They are two towers over Q_3; an inclusion
between K and A is not asserted. All three are finite Q_3-extensions
with finite residue fields. Their embeddings from Q extend the
canonical Q_3 embedding by completion.

The actual coefficients of phi and phi^(-1) belong to F', and their
nonzero denominators remain nonzero in L. L077's two inverse pointed
maps therefore base change to L and identify E_L over L with E
over L. E is defined over Q, so its base change through this place is
the base change of the same E/Q_3 in L073. In particular its Tate
parameter is the image of the same q_aux in Q_3, independently of
the choice of v,z,a. Geometric uniqueness of the Tate parameter also
identifies this parameter after the displayed pointed isomorphism;
neither the earlier parameter 3^30 nor an arbitrarily chosen pilot
root is substituted.

Consequently E_L over L is split Tate with parameter q_aux and has
multiplicative reduction. This assertion does not identify L with
the particular H in L078. It uses the complete F'-defined maps at
the chosen z, rather than transporting the one embedded H by fiat.

### Multiplicative reduction downstairs and height normalization

By L081, E_L over K is semistable, hence has either good or
multiplicative reduction. If it had good reduction, Silverman
VII.5.4(b) would give good reduction after the finite extension L/K.
The isomorphic split Tate curve just obtained instead has
multiplicative reduction over L, which excludes good reduction.
Thus E_L has multiplicative reduction over K. This does not assert
splitness over K: the actual comparison map need only be L-defined.

Let ord_K and ord_L be the surjective integer valuations. Since
v_3(q_aux)=30, valuation restriction in the Q_3 tower gives

    ord_L(q_aux)=30e(L/Q_3).

Use this actual split extension L/K in the cited GenEll height
convention. Its split height is ord_L(q_aux); hence

    h_v=ord_L(q_aux)/e(L/K)
       =30e(L/Q_3)/e(L/K)
       =30e(K/Q_3).

The last equality is the ramification tower identity through K.
It shows directly that the generalized height is a positive integer
here. In the nonsplit case Silverman's unramified quadratic
splitting description is consistent with the same formula; no
extra factor of two is introduced. Independence of the extension
in GenEll Remark 3.3.1 ensures that using this possibly larger L
has not changed the native height. This calculation uses the
valuation on K, not the valuation on the retained division field N.

### Prime-to-seven ramification through the other tower

L073 gives F_aux/Q Galois. At its arbitrary place a above 3,
Milne's Galois ramification formula gives

    e(A/Q_3) divides [F_aux:Q],

so 7 does not divide e(A/Q_3). This uses Galoisness of F_aux,
not of G. For the extension F'=F_aux(s), the induced completion
formula gives L=A(s_z), where s_z is the image of the same s
at z and satisfies s_z^2=D in A. Thus [L:A] is 1 or 2.
Local degree equals e(L/A)f(L/A), so e(L/A) is 1 or 2 as well.
The first ramification tower yields

    e(L/Q_3)=e(L/A)e(A/Q_3),

which is prime to seven. The separate tower through K gives

    e(L/Q_3)=e(L/K)e(K/Q_3).

Both factors are positive integers. Therefore 7 does not divide
e(K/Q_3). Since 7 does not divide 30, the height formula above
proves gcd(7,h_v)=1. No local index is claimed to divide the
possibly nonnormal global degree [G:Q]. As v was arbitrary,
both the reduction and height conclusions hold at every v|3.

### Relevance, stopping test and qualifications

All requested places pass the multiplicative-reduction, exact-height
and coprimality thresholds, using only the assessed methods. This
clears a local prerequisite for a possible selected moduli place
above 3. L079 is unnecessary for the all-v|3 conclusion: no native
moduli-place fiber is identified in this proof. L061 concerned the
earlier curve/field and is method context only, not an input here.
The GenEll journal height convention is imported precisely; the
recorded IUT reproduction/author source-version qualification is
retained, and no identity of unread source versions is asserted.

No curve, field, root or embedding was changed. The retained H,N
packet and all unfinished work remain intact. ATTEMPTS/027's
exact-curve stop and ATTEMPTS/034's cyclic normality-separator stop
are not reopened. G/Q normality, mixed radical/15-torsion data,
independent initial-data conditions, retained radical/scalar tests,
native input/action, all-image factorization, pilot transport,
essentiality and the original finite B>=A remain unresolved.
This is local progress by specialization of checked known results,
with no claim of a discovery beyond those sources. The separate
critical audit below checks the full arbitrary-place transport,
reduction descent, nonsplit normalization and both towers.

### Separate critical audit — 2026-10-19, step333

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-19-exact-legendre-all-place-height-critical-audit.md`
covers precisely this audit. The full proof above, the application
assessment's inspected primary hypotheses and proof cases, and the
relevant canonical proof/audit passages of L073,L077,L078,L081 were
checked. The primary imports and versions are exactly those in
"Imported results and scope" above. No fresh source retrieval, new
general theorem or reproof is needed for this unchanged scope.

**The quantifier over places and complete pointed transport.** L078
establishes the literal inclusion G subset F' before any assertion
about its selected completion. Therefore every v|3 extends to a z
of F'; restriction gives an actual place a of F_aux. The induced
embeddings into L=F'_z put both K=G_v and A=(F_aux)_a inside L,
each over Q_3, without requiring either to contain the other. All
are finite extensions of Q_3. In these embeddings the elements
r_i,D,s,t satisfy the same polynomial identities as in F', and
D and s remain nonzero. In particular the projective extensions
of the two maps are

    [x:y:z] -> [(x-r_i z)/D : y/(Ds) : z],
    [X:V:Z] -> [r_i Z+DX : Ds V : Z].

Their composites are the identity and each fixes [0:1:0]. The
identity g_aux(r_i+DX)=D^3 X(X-1)(X-t), together with
(Ds)^2=D^3, checks the equations at this place too. Thus they
identify the complete pointed curves over L, with no integral-map
extension assertion. L073's source curve is Q-defined, so its
Q_3-base change is the same at every such z. Its Q_3-defined split
Tate description base changes to L. The parameter is this curve's
q_aux in Q_3, of valuation 30, and the cited geometric uniqueness
prevents a different parameter after the pointed identification.
There is no identification of an arbitrary L or K with H or N.

**Reduction descent and the height convention.** L081 applies to
the exact nonsingular E_L/G, and hence makes its reduction over
K semistable. In dimension one this leaves good or multiplicative
reduction, with a possibly nonsplit torus in the latter case.
The split Tate curve over L has multiplicative reduction, so
Silverman VII.5.4(b)'s persistence of good reduction excludes the
good alternative over K. This uses no converse descent theorem
for arbitrary potentially multiplicative curves. The curve over
L satisfies GenEll's split local setup: L is a finite p-adic field
and its semiabelian special fiber is the split one-dimensional
torus. It is consequently an allowed extension for Remark 3.3.1,
even if the curve over K is nonsplit. With both integer valuations
surjective, the split height and the normalized height are exactly

    h_L=ord_L(q_aux)=30e(L/Q_3),
    h_v=h_L/e(L/K)=30e(K/Q_3).

The normalization divides by e, not the local degree ef, and not
the degree of any global field. The same tower identity proves
integrality rather than assuming it for every potentially
multiplicative curve. If the torus downstairs is nonsplit, the
cited unramified quadratic splitting description gives e=1 for
that smaller splitting extension and the same answer. The chosen
larger split extension is allowed by the height's extension
independence. No extra factor of two, pilot-root order or valuation
on the division field N enters this computation.

**Two ramification towers.** L073 supplies Galois F_aux/Q with
degree dividing 2^14*3^3*5 for this same witness. Thus at the
actual a the global Galois ramification formula excludes seven
from e(A/Q_3). The completion of F_aux(s) at z is A(s_z), with
s_z^2=D in A, so its local degree is at most two. The local ef
formula then makes e(L/A) either one or two. Consequently

    e(L/Q_3)=e(L/A)e(A/Q_3)

is prime to seven. Separately, K subset L gives

    e(L/Q_3)=e(L/K)e(K/Q_3).

All indices are positive integers, so the latter identity excludes
seven from e(K/Q_3). Combining it with 7 not dividing 30 proves
the required gcd exactly. No divisibility by nonnormal [G:Q],
normality of F'/Q, or relation between A and K is needed.

**Verdict and limitations.** All stated conclusions pass without
a mathematical correction or extra hypothesis. In particular the
argument treats every v|3, not only the induced selected place,
and gives exactly the requested height and coprimality. The direct
mathematical inputs remain L073,L077,L078,L081; no use of L061 or
L079 has been introduced. The unchanged choices retain L078's H,N
packet. This verifies a local known-method input, not a result
beyond the inspected sources or a solution of the IUT challenge.
The native moduli-fiber identification, G/Q normality, independent
initial data and the original finite B>=A comparison are outside
this audit. Source-version qualifications and all recorded route
stops remain in force. The argument and DAG are unchanged; this
canonical verdict supersedes the overview's pending-audit wording.

## Mathlib

Full matching Tate/reduction/native-height coverage is not checked.
The assessment inspected supporting
[Ideal.ramificationIdx_tower](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RamificationInertia/Ramification.html#Ideal.ramificationIdx_tower),
with its commutative algebra/scalar-tower, lies-over and flatness
hypotheses. It supports the abstract tower identity, not the complete
elliptic-curve application or this native height. No formalization or
absence claim is made.
