# L077 — A quadratic adjunction rationalizes Legendre torsion and preserves the local packet

## Hypotheses

Fix the same auxiliary witness E=E_aux/Q and fields of L073,
with the root labelling and ordered-root equations of L074. Work
inside the fixed algebraic closure Q-bar of Q in Omega. In particular,

    F_aux=Q(zeta_60,E[30]),
    (F_aux)_u=H=Q_3(zeta_60),
    (F_aux(E[7]))_w=N=Q_3(zeta_420,3^(1/7)).

All these completion identifications use the retained embedding.
Division fields contain both coordinates of every geometric torsion
point. All geometric E[15] points are F_aux-rational by L073.

Choose distinct i,j for which r_i and r_j have different residues
in L076, let k be the remaining index, and set

    D=r_j-r_i, t=(r_k-r_i)/D,
    E_L: V^2=X(X-1)(X-t).

Choose s in H with s^2=D and put F'=F_aux(s), inside Omega.
L076 gives such an s: its two cross-residue differences are squares,
and reversing a difference preserves squareness since iota=sqrt(-1)
belongs to H. Write u' and w' for the places induced by this same
embedding on F' and F'(E[7]), respectively.

## Conclusion

For every such choice of D and either choice of its square root s,
the corresponding L074 ordered-root model E_L has full F'-rational
15-torsion, and the embedded completions satisfy

    F'_(u')=H,
    (F'(E_aux[7]))_(w')=N.

Thus all three requirements of the approved construction pass for
one and the same curve, root and embedding. This is a specialization
of known coordinate and completion theorems. It gives no equality
F'=T(sqrt(-1),E_L[15]), no native T/model identification or sufficient
initial data, and no essential IUT flaw or original finite B>=A
comparison. The separate step303 critical audit below validates this
specialization with these qualifications unchanged.

## Proof

### Imported results and why specialization is needed

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-18-auxiliary-quadratic-modification-local-packet.md`.
Import J.S. Milne, *Elliptic Curves*, second edition (2021),
[II Theorem 2.4(b), pp.52–53](https://www.jmilne.org/math/Books/EC2.pdf),
for invertible pointed Weierstrass coordinate changes on the complete
curves. Pointed elliptic-curve isomorphisms preserve their group laws
and hence full torsion, as in the inspected coordinate/torsion coverage
used in L074. No twist classification or new representation theorem
is required here.

Import Milne, *Algebraic Number Theory*, v3.08 (19 July 2020),
[section 8, introductory completion argument p.135 and Propositions
8.1–8.2 with proof p.136](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
For a finite separable extension B=A(alpha), its completion at a
specified extension of the place on A is A-hat(alpha), using the
chosen image of alpha. This is an induced-place statement, without
Galoisness or linear-disjointness hypotheses. These general results
are imported, not reproved. The specialization must check the actual
coordinate coefficients and the image of the same adjoined root for
both number fields separately.

### The root and complete pointed coordinate transfer

All r_m belong to F_aux by L074's full 2-torsion identification.
Thus D,t belong to F_aux, D is nonzero, and t is neither zero nor
one. The equation E_L is exactly the row (i,j,k) of L074, and is
nonsingular. Since D is algebraic over Q and s satisfies T^2-D,
s is algebraic over Q, even though it was selected in the completion
H. Hence it lies in our Q-bar inside Omega and F' is a number field.
This does not assume that s is in F_aux; L074 in fact excludes that
membership for every signed difference.

With this chosen s, use L074's actual map and inverse:

    phi(x,y)=((x-r_i)/D, y/(D s)),
    phi^(-1)(X,V)=(r_i+D X, D s V).

Every coefficient in both maps belongs to F', and their denominators
are nonzero. Direct substitution gives

    g_aux(r_i+D X)=D^3 X(X-1)(X-t),
    (D s)^2=D^3.

Thus both maps have the claimed equations and compose to the identity.
They are the cited pointed Weierstrass changes with u=s and r=r_i.
Equivalently their invertible projective linear transformations send
[0:1:0] to [0:1:0], so the complete curves and their origins are
included. If s is the negative of the radical chosen for this row in
L074, the forward map changes only by the F'-defined inversion on
E_L. This has no effect on the assertions.

The pointed F'-isomorphism phi induces a bijection from E[15] onto
E_L[15]. In detail, it commutes with [15], and the same holds for
its inverse, so both inclusions hold on all geometric torsion points.
Every E[15] point is F_aux-rational and therefore F'-rational. Its
image has both X and V coordinates in F' by the displayed formulas;
the identity maps to the rational identity. Conversely every geometric
E_L[15] point is such an image. Hence all of E_L[15] is F'-rational.
An x-coordinate field or a single torsion subgroup is not substituted
for this full-point argument.

### First induced completion

The finite extension F_aux(s)/F_aux is separable in characteristic
zero. Apply the imported completion theorem at its induced place u':

    F'_(u')=(F_aux)_u(s)=H(s)=H,

where the last equality uses the very same chosen s in H. These are
equalities in the fixed local embedding, not a comparison of abstract
degrees or an assertion about every place of F'. A possible global
quadratic extension can have local degree one here.

### The full seven-division extension and its induced completion

Let M=F_aux(E[7]), with all coordinates retained, so M_w=N by L073.
Since the same original curve E is defined over Q and F' contains
F_aux, adjoining its full seven-torsion gives the field identity

    F'(E[7])=F_aux(s,E[7])=M(s)

inside Q-bar. This is an identity of generated fields: both sides
are generated by F_aux, s and the same full coordinate list. No
disjointness, image surjectivity or torsion-kernel identification for
a different curve is being assumed.

Apply the completion theorem again, now to the finite separable
extension M(s)/M at the place induced by the fixed embedding:

    (F'(E[7]))_(w')=M_w(s)=N(s)=N.

Here H is a subfield of the fixed N by L073's embedded packet, and
s belongs to H, so its image lies in N. The second completion check
is independent of merely knowing the first one: it uses the actual
seven-division field M and its actual induced completion.

### Relevance and qualifications

All three continuation tests pass. The plausible downstream use is
a larger auxiliary field supporting this literal Legendre model's
full 15-torsion without changing the local packet H,N. This does not
contradict L074 or L075, which concern the unchanged F_aux. No
restriction of L073's global fixing element to a local decomposition
group is used. The same E_aux and q_aux remain in place; no equality
q_aux=3^30 or q_aux=q_0 follows.

The retained E_0,F,K_glob,Omega,embedding,u,w,H,N,q_0 are unchanged;
u',w' denote the new auxiliary induced places. Native T/model, exact
minimal generation, independent initial data, retained memberships and
scalar occurrence, source-marked all-image factorization, pilot
transport, essentiality and original finite B>=A remain unresolved.
The foundations/05 step272 source-version qualifications and
ATTEMPTS/027,028,031,032,033 remain intact. Neither an IUT instance
nor a complete candidate solution is asserted. No mathematical script
or numerical evidence is needed for this field specialization.

### Separate critical audit — 2026-10-18, step 303

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-18-auxiliary-quadratic-modification-critical-audit.md`
approves exactly this audit. Import the coordinate and induced-completion
theorems at the versions and locations cited above; their general proofs
are not repeated. L073's same-witness retention and separate audit,
L074's complete coordinate and torsion argument and separate audit,
and all of L076's local square proof and separate audit were checked.
All three conclusions pass without a correction or extra hypothesis.

**One algebraic root in the specified completion.** L073 places the
same original cubic's full 30-torsion in F_aux and gives its induced
completion H. Every (r_m,0) is therefore rational over F_aux, and all
roots lie in F_aux inside H. L076's complete residue-factorization
and three-case sign table give cross-residue square roots in H;
reversed signs are covered because iota^2=-1 in H. Thus D and the
chosen s are nonzero. Since Q(D)/Q is finite and s satisfies T^2-D,
transitivity of algebraicity puts this actual s in the fixed Q-bar
inside Omega. A locally chosen root has not selected a different
abstract quadratic field. Either sign gives the same global field
and belongs to the same H. L074's exclusion of s from F_aux is
consistent with its membership in the completion.

**Both complete maps and all geometric torsion.** The factors of
g_aux(r_i+DX) are DX, D(X-1), D(X-t), so their product is exactly
the stated D^3 multiple. Distinct roots give D!=0 and t!=0,1.
In Milne's convention x=u^2 X+r, y=u^3 V the inverse map has
u=s and r=r_i, since s^2=D and s^3=Ds. All coefficients of both
maps lie in F'. On the projective cubics the transformations are

    [x:y:z] -> [(x-r_i z)/D : y/(Ds) : z],
    [X:V:Z] -> [r_i Z+DX : Ds V : Z].

Their nonzero diagonal factors make them invertible projective linear
maps. Substitution transforms the homogeneous equations, both composites
are the identity, and each map sends [0:1:0] to itself. Thus the
complete pointed-isomorphism hypotheses hold, not merely an affine
birational relation. Imported group-law compatibility gives
phi([15]P)=[15]phi(P), also for the inverse. In particular any
geometric E_L[15] point has inverse in E[15], which is F_aux-rational
by L073. The displayed forward map then puts both its target
coordinates in F'; the remaining point is the rational origin.
This checks surjectivity onto the entire geometric torsion set,
without an x-coordinate-field or cyclic-subgroup substitution.
Replacing s by -s composes phi with rational inversion and changes
none of these conclusions.

**First induced completion.** Take A=F_aux and B=F_aux(s). These
are number fields; B/A is finite separable in characteristic zero.
The place is discrete nonarchimedean and induced by the fixed
embedding in Omega. With the chosen root image s in H, Milne's
section 8 theorem gives B_(u')=A_u(s)=H(s)=H as embedded
completions. Galoisness of B/Q, other places, and equality between
global and local degrees are not assumed.

**Second induced completion.** Now take A=M=F_aux(E_aux[7]) and
B=M(s). The field identity F'(E_aux[7])=M(s) holds because both
sides have the same generators F_aux, s, and the full seven-torsion
coordinate set of the original E_aux. L073 gives M_w=N. The place
on B restricts to that very w in the same embedding. This extension
is also finite separable, including the possibility s in M; the
completion theorem applies in degree one as well. Hence
B_(w')=M_w(s)=N(s)=N, using the already chosen s in H subset N.
This is a separate completion argument, not an inference from the
first equality or a comparison for an unexamined changed curve.

**Verdict and limits.** Full torsion and both completion thresholds
hold for every stated choice, hence simultaneously for one choice.
This validates a known-method specialization, with no claim beyond
the checked source methods. The direct inputs remain L073, L074 and
L076; no new DAG edge or repair of the original argument is needed.
L074/L075 exclude the unchanged F_aux, not this changed field. No
equality F'=T(iota,E_L[15]), identification of native T, or transfer
of independent global hypotheses to F' follows from the completions.
The retained witness and parameter, foundations/05 step272 qualifications,
recorded route stops and original finite B>=A gap remain unchanged.

## Mathlib

Full matching and supporting Mathlib coverage for this combined
specialization has not been checked. No absence or formal-verification
claim is made. The general coordinate and induced-completion inputs
are imported with precise citations; the complete torsion transport
and both same-embedding applications are the explicit specialization.
