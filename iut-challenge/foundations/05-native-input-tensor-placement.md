# Native local input and tensor placement — citation record

## Hypotheses

Use Mochizuki, **IUT III, May 2020**, 199 printed pages,
[author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf),
and **IUT IV, April 2020**, 87 printed pages,
[author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf).
IUT III's relevant continuous text was readable on 2026-10-16. IUT IV's
author endpoint returned metadata but failed on subsequent text requests;
the continuous text read was the
[April 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf).
Byte identity is unverified. These are printed-page references, not
journal pagination. Screenshot requests supplied no readable image
content and are not verification evidence.

The native construction assumes **all** initial Theta-data of IUT I,
Definition 3.1, and an LGP-Gaussian log-theta-lattice as in IUT III,
Definition 3.8(iii). Theorem 1.10 of IUT IV additionally assumes its
printed p.22 hypotheses: good reduction at every good finite F-place
not dividing 2ell, rational (3*5)-torsion, and the specified equality
F=F_mod(sqrt(-1),E_Fmod[2*3*5]) using the indicated tripodal/Legendre
model. These additional global hypotheses are **not** established for
the retained F merely by its containing Q(zeta_60) and full 30-torsion.
The local algebraic Propositions 1.1,1.2,1.4 do not require those global
hypotheses.

For the local propositions, p is prime, I is finite with |I|>=2, and
k_i/Q_p are finite subextensions of a fixed algebraic closure. Put
R_i=O_(k_i), R_I=tensor_(Z_p,i in I) R_i,
T_I=tensor_(Q_p,i in I) k_i, and let R_tilde be the normalization of
R_I in T_I. Write P_I=tensor_(Z_p,i in I) log_p(R_i^times).
The permitted **algebraic bound** uses any Q_p-linear automorphism phi
of T_I that preserves P_I. Its scalar lambda belongs to
(1/e_(i_dagger))Z for a distinguished i_dagger in I. The constants,
inclusions, and extra I* hypothesis are retained by precise citation
in [the enclosure record](04-native-local-enclosures.md).

## Conclusion

The source provides three distinct objects; they must not be conflated.

1. **Ambient packet and factor map.** IUT III, Proposition 3.1(i),(ii),
   pp.92–93, and Remark 3.1.1(i),(ii), pp.93–95, construct local
   holomorphic packets and their integral structures. A factor maps
   into a packet by tensoring with 1 in every other labeled factor.
   The finite portion relevant to volume uses selected completions
   K_(v_i). Proposition 3.2(i),(ii), pp.97–99, relates these packets to
   the mono-analytic packets by poly-isomorphisms; it does not select
   a fixed field-coordinate identification on both sides.

2. **Algebraic test input.** IUT IV, Proposition 1.2(ii), pp.10–11,
   and Proposition 1.4(iii), pp.13–14, bound phi(p^lambda R_tilde).
   Here p^lambda is placed through the distinguished field factor,
   in the source's fractional-ideal convention. This is a full tensor
   normalization, not an arbitrarily chosen field factor, additive
   subspace, logarithm lattice or upper envelope.

3. **Actual pilot-image region.** IUT III, Theorem 3.11(i)(a),(b),
   pp.153–154, represents a splitting monoid acting on labeled tensor
   packets. Its (Ind2) is formulated factor by factor, independently
   on each direct summand. Corollary 3.12, pp.173–174, uses the union
   of all relevant Kummer images with (Ind1),(Ind2),(Ind3), followed
   by holomorphic hull and procession-normalized log-volume. The
   union is not defined as all points of the algebraic test input.

IUT IV, Theorem 1.10 proof (iv),(v), **pp.26–28**, specifies the
comparison in (2): I=S^pm_(j+1)={0,...,j}, j=1,...,(ell-1)/2,
k_i=K_(v_i), for every tuple of selected places above the same rational
place, **including repeated places**, and i_dagger=j. At a good
distinguished place lambda=0; at a bad one it is
ord_p(bold_q_(v_j)^(j^2)). The normalized volume is subsequently
weighted over all tuples and averaged over j; it is not the valuation
of one component point.

The bad-place scalar is fixed by **IUT I, May 2020, Example 3.2(iv),
printed p.71**:
[author URL](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf),
[186-page reproduction actually read](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf).
If q_v is the geometric Tate parameter, bold_q_v is q_v^(1/(2ell)),
defined up to a mu_(2ell)-multiple. That passage invokes the native
2-torsion and full ell-division-field hypotheses for its membership
in K_v. No assertion q_v=3^30 or bold_q_v=3 is licensed by it.

For completeness the native shell convention is **IUT III, Definition
1.1(i), pp.23–24**: the pre-log-shell is the logarithmic image of
the fixed local units; the shell is its multiple by 1/p_v* with
p_v*=p_v for odd p_v and p_v*=p_v^2 for p_v=2. Retain separately
Theorem 1.10(v)'s displayed intermediate module
p^(floor(lambda)-|I|) * 2^(-|I|) * P_I and its subsequent nonpositive
integer p-power enlargement. The occurrence of 2 in that module must
not be silently substituted for the shell definition. The source
claims the enlarged container contains the pilot-image union; this
review imports no converse or equality with that union.

## Proof / source inspection and applicability boundary

These are imports of definitions and stated local propositions, not
a reproof of the full multiradial construction or Corollary 3.12.
The complete statement and relevant proof of Proposition 1.2(ii) were
read: the input is enclosed in an integer-power multiple of P_I before
using phi(P_I)=P_I. Proposition 1.4's statement and its (iii) proof
case identify the same input and the normalized outer integral
container. The full relevant text of Theorem 1.10(iv),(v) was read,
including the selected-field substitutions, asymmetric scalar,
nonpositive enlargement and tuple/procession averaging. Its opening
global hypotheses were read as well. Nothing in those inspected
passages asserts that every point in an upper container is an actual
pilot image. The general native theorem is the claim under
investigation; its pilot-image applicability is not certified here.

Under the retained **conditional** identification K_w=N, the source
allows the repeated-place tuple (w,w) at j=1, ell=7. Its finite tensor
portion is T=N tensor_(Q_3) N with R_tilde the normalization of
O_N tensor_(Z_3) O_N and P=J tensor_(Z_3) J. A candidate map to test
is the source factor map x -> x tensor 1 followed by multiplication
in the distinguished second factor by a native choice rho with
rho^14=q_0. The resulting **proposed** placement is x -> x tensor rho.
Its existence for the retained data, injectivity, integral containment,
action transfer, field-component behavior and relation to actual
pilot images have not been proved in this source-review turn.
In particular C=O_N intersect V is not identified with the full tensor
input; the proposed scaled image is not C itself.

The standard finite-separable tensor decomposition is already covered
locally by Stein, **Tensor Products, section 18.2, Lemma 18.2.1 and
equation (18.1)**,
[primary statement and proof](https://www.williamstein.org/papers/ant/html/node76.html)
(page dated 2004-05-06; statement, CRT proof and component maps
rechecked 2026-10-16). It supplies finite field components and
injective maps from each field factor, not an identification of a
whole tensor with N. Its specialization to the proposed retained
packet is deferred. No new CRT theorem or logarithm calculation is
needed merely to formulate that test.

The independent missing bridges remain full initial data, the native
field/rho application, permitted-action identification, actual-image
membership, marked pilot transport, essentiality and the original
finite B>=A comparison. A contained subregion of the algebraic test
input could test a cited local upper bound; it would still not be a
counterexample to the original comparison.

## Conditional j=1 application — 2026-10-16, step 256

### Hypotheses

Use exactly the separately approved pilot-scaled tensor assessment and
the audited L063–L067 data. In particular N has e=14,f=12,
J=log(O_N^times), E=W_J, V=Q_3 E and C=O_N intersect V.
Gamma is L063's finite-word reference group with inverses, with its
unchanged reciprocity and presentation choices. All unit torsion is
retained before logarithmic quotient. Assume, without establishing
native admissibility, K_w=N and rho in N with rho^14=q_0, where the
unchanged curve has v_3(q_0)=30. Retain all the independent global
qualifications above. These are conditional local hypotheses.

Set T=N tensor_(Q_3) N, R_0=O_N tensor_(Z_3) O_N,
R_tilde its normalization in T, and P=J tensor_(Z_3) J, viewed
inside T. The tensor of full free Z_3-lattices embeds in T and spans
it over Q_3. Put i_rho(x)=x tensor rho and Phi_h=h tensor id_N.

### Conclusion

The proposed placement is injective and lies in the stated algebraic
input. For every h in Gamma, the cited native enclosure applies:

    i_rho(C) subset (1 tensor rho) R_tilde,
    Phi_h((1 tensor rho) R_tilde)
      subset 3^k P subset 3^(k-27/7) R_tilde,
    k=floor(1/7-2d_N),

where d_N is exactly v_3 of a generator of the different of
O_N/Z_3. Fractional powers have the suitable-element/ideal convention
of Propositions 1.1–1.2; they are not rational scalar operators.
The same fixed outer module therefore contains the union of
Phi_h(i_rho(C)) over all finite words. No violation is obtained.
This is a REPRODUCTION/application of a known enclosure, closing
this conditional local objection without adding a new lemma.

### Proof

For x in C, x belongs to O_N, so x tensor 1 belongs to R_0
and hence R_tilde. Multiplication by 1 tensor rho gives
x tensor rho in the required input. The multiplication map
mu:T -> N, mu(x tensor y)=xy, is well defined over Q_3 and
satisfies mu(i_rho(x))=x rho. Since q_0 is nonzero, rho is
nonzero; thus i_rho(x)=0 implies x=0. This use of mu proves
injectivity of this placement only; it does not identify T with N,
identify P with a field lattice, or require a CRT component theorem.

L063 gives h(J)=J and h^(-1)(J)=J for every finite word h.
The tensor map Phi_h is Q_3-linear, with inverse
h^(-1) tensor id_N: both composites are the identity on every
pure tensor and hence on T. On the integral tensor lattice, a pure
tensor j_0 tensor j_1 maps to h(j_0) tensor j_1 in P.
Finite sums give Phi_h(P) subset P; applying the inverse gives
equality. Thus the exact preservation hypothesis is satisfied.
In particular

    Phi_h(i_rho(x))=h(x) tensor rho.

The scalar is in the second, distinguished factor. This calculation
uses no commutation of h with multiplication by rho inside N and
does not assert that Phi_h preserves the algebraic input order.

Apply IUT IV, April 2020, Proposition 1.2(ii), printed pp.10–11,
and Proposition 1.4(iii), pp.13–14, as cited in the enclosure record.
The permitted repeated-place tuple is I={0,1}, (w,w), with
i_dagger=1 and j=1,ell=7. Its scalar is rho, with
lambda=v_3(rho)=30/14=15/7 in (1/14)Z. In both factors

    e_i=14,  d_i=d_N,
    a_i=ceil(14/(3-2))/14=1,
    b_i=floor(log_3(3*14/(3-1)))-1/14=27/14.

For the last equality, 9<=21<27, so the floor is two.
Consequently d_I=2d_N,a_I=2,b_I=27/7 and
floor(lambda-d_I-a_I)=floor(1/7-2d_N)=k.
Take I*={0,1}: both e_i exceed p-2=1, as required.
Here I* is Proposition 1.4(iii)'s exceptional-index subset, not
Proposition 1.1's complement of a chosen index. The hypotheses
|I|>=2, the common algebraic closure, full tensor normalization,
admissible distinguished scalar and two-sided lattice preservation
all hold. Substitution into the imported inclusions gives the stated
fixed enclosing modules. No different estimate, evaluation of d_N,
auxiliary coarse radius or reproof of the enclosure is necessary.

The placement inclusion and its image under each Phi_h give the
conclusion for the candidate subregion, and then for its whole union.
L067's single-field sharp minimum cannot contradict this applicable
tensor enclosure; the tensor and pilot scaling have been retained.
The success of this test establishes neither actual pilot-image
membership nor native permission for Phi_h. It also does not settle
the additional global hypotheses, marked pilot transport,
essentiality, normalized volumes or the original finite B>=A gap.
ATTEMPTS/020,/024 and the auxiliary Ind3 source stop are unaffected.

### Mathlib

Full matching conditional tensor application and supporting tensor,
normalization and logarithm-lattice coverage: **not checked**.
No absence or formal verification is claimed. The primary enclosure
is imported by precise citation; only the listed applicability checks
are supplied here.

## Native Ind3 antecedent — source comparison, step 257

### Hypotheses

Retain the source versions and all native hypotheses above. In IUT III,
Proposition 3.5, printed pp.103–106, the input is a Gaussian
log-theta-lattice of distinct theaters relative to the given initial
Theta-data, with the labeled prime-strips, Galois actions and Kummer
maps of its part (i). Theorem 3.11, pp.153–156, uses the
LGP-Gaussian version. Neither input is supplied by a local field alone.
The passages read this turn were the [199-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%203.pdf#page=103)
and the [87-page IUT IV reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf#page=27).
The author endpoints supplied metadata but subsequent text requests
timed out. Byte identity remains unverified; the earlier source records
are preserved. Printed pagination is used throughout.

### Cited conclusions and proof locations

**IUT III, Proposition 3.5(ii)(a), pp.104–105:** for n,m in Z,
0<=j<=ell', and a nonarchimedean rational place, the coric tensor
log-shell contains the tensor Kummer images of the Galois-invariant
unit submodules at labels |t|=0,...,j. It also contains their images
under precomposition with each positive iterate of the log-links.
Iterates concern only their domains of definition: Remark 1.1.1 and
Remark 1.2.2(iii), pp.36–37. This is a forward inclusion into the
shell, not an equality, a reverse membership assertion, or an action
by arbitrary maps on the ambient rational tensor space.

Part (ii)(c), pp.105–106, treats the bad-place splitting monoids for
j>=1 separately. Across log-links, the only overlapping action
ambiguities specified there are root-of-unity multiplications, which
become zero under logarithm. This is not a statement that a fixed
nonintegral field scalar commutes with all log-links. Part (ii)(b)
uses a different archimedean surjectivity statement; it is not used for
the retained 3-adic packet. The proof on p.106 refers to the definitions
and references in the statement. The relevant explanatory proof case,
Remark 1.2.2(i),(iii), pp.36–37, uses the log-shell containing both the
integral elements and the logarithmic unit image, with partial iterate
domains retained. No independent reproof is supplied here.

**Theorem 3.11(ii)(a),(b), pp.155–156**, transports tensor packets and
splitting monoids through labeled Kummer isomorphisms; at that stage
(Ind1),(Ind2) have not yet been imposed. Its concluding (Ind3) clause
on p.156 cites precisely Proposition 3.5(ii)(a),(b). **Corollary 3.12,
proof Step (x), pp.180–181**, describes the resulting upper inequality
for procession-normalized log-volumes and their log-link compatibility.
It does not itself display a fixed-coordinate scalar-weighted module
inclusion for all pilot images.

**IUT IV, Theorem 1.10, proof (iv),(v), pp.26–28**, makes the
all-image enclosure assertion in the notation already fixed above:

    M_lambda = p^(floor(lambda)-|I|) 2^(-|I|) P_I.

It asserts that a suitable p^r M_lambda, r an integer with r<=0,
contains the pilot-image union. Its cited algebraic enclosure is
Proposition 1.4(iii); the nonpositive-exponent condition uses that
proposition's final d_I+a_I inequalities. This is an assertion about
the native image family, not all points of a substituted scalar-shell
envelope. Theorem 1.10's additional global hypotheses on printed p.22
were rechecked and remain exactly those recorded above.

### Applicability boundary

The cited unit-image inclusion is now a located source input, rather
than the unresolved auxiliary reference. The source's directions are
consistent with upper enclosure. This does not independently verify
the conversion from the labeled unit images and splitting actions to
the scaled all-image assertion of IUT IV. In particular, Step (x)'s
numerical statement alone must not be silently promoted to that set
inclusion, nor may a scalar-shell envelope be substituted without a
separate argument. A critical audit of that conversion remains open.
This is a limit of the present source comparison, not a claim that the
source has no such argument or that the native assertion is false.

For the retained packet, all previous conditional identifications,
initial-data and additional global qualifications remain. No native
permission for Gamma, actual pilot membership, or normalized B>=A
comparison follows. The argument in PROOF.md and its DAG do not change.
Matching and supporting Mathlib coverage for this native antecedent
is **not checked**.

## Mathlib

Full native packet/pilot comparison and matching tensor-placement
theorem: **not checked**. Supporting tensor and normalization coverage:
**not checked**. No absence or formal verification is claimed.

## Conditional IUT field/root dictionary — 2026-10-17, step 269

### Hypotheses

Retain the same E_0/Q, origin, embedded algebraic closure, and places
from L045 and L048, with M>=max(M_tors,31). In particular

    F=Q(zeta_60,E_0[30]), K_glob=F(E_0[7]),
    F_u=H=Q_3(zeta_60),
    (K_glob)_w=N=Q_3(zeta_420,3^(1/7)) subset Omega.

Both coordinate division fields contain both coordinates of every
geometric torsion point. Full geometric 30-torsion is F-rational.
L048 supplies a pointed Q_3-isomorphism E_0 ≅ E_(q_0), where
q_0 is nonzero in Q_3 and v_3(q_0)=30, with v_3(3)=1. Reuse
L054's same-base-curve parameter identification and L069's audited
fourteenth-root membership, without repeating their proofs.

Assume exactly L060's conditional native field/place setup. Write
r_place for its surjection V(K_glob) -> V(F_mod), and sigma for
its full section through w. Put v_*=r_place(w) and retain the
proposed selected bad subset {v_*}, whose selected lift is {w}.
F_mod is not computed or identified with Q. No assertion that all
initial Theta-data exist is made. This application evaluates the
field, base-change and root conventions only; it does not apply a
theta-evaluation theorem without its remaining hypotheses.

### Conclusion

For the unchanged F, X_F=(E_0 over F) minus its origin, and ell=7,
the field definition of IUT I Definition 3.1(c) gives K=K_glob.
At the retained selected lift w, Definition 3.1(e)'s completion and
underlying elliptic curve give K_w=N and q_w=q_0. Evaluating only
Example 3.2(iv)'s 2ell-th-root convention therefore gives

    {r in Omega : r^14=q_w} = rho_0 mu_14 subset N,
    rho_0^14=q_0,  v_3(r)=15/7 for every such r.

Here rho_0 is any one of L069's roots, and mu_14 is the full root
group in Omega, already contained in N. Thus every representative
allowed by this root convention belongs to the same unchanged N.
If the remaining native construction is supplied, its root
representative belongs to this set; this application supplies no
source-marked representative or transported theta value.

These assignments pass the approved conditional test. They discharge
the field/root membership prerequisites of the conditional tensor
application and L068 relative to this setup. The separate step 271
critical audit below validates this conditional application. This is
a known-definition specialization, with no beyond-source novelty
claim, all-image inclusion or numerical conclusion.

### Proof

**Imported conventions and scope.** Reuse the pre-invocation
SPECIALIZE assessment
`drafts/literature/2026-10-17-retained-native-field-radical-application.md`
and its completed source comparison. The precise source is
Mochizuki, *IUT I*, May 2020, Definition 3.1(a)-(f), printed
pp.61-63, especially (c) and (e), and Example 3.2 opening/(iv),
pp.69,71:
[author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf),
[186-page reproduction inspected in the reused assessment](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf).
The reproduction was accessible on 2026-10-17; the author endpoint
timed out. Author/reproduction byte identity and journal-version
equivalence remain unverified. No new retrieval or theta-evaluation
reproof is part of this mathematical application.

**Full kernel.** Let S_7 be the list of both coordinates of every
nonidentity point of E_0(Q-bar)[7], using the retained embedded
algebraic closure of F. For g in G_F, the full representation
rho_(E_0,7)(g) is the identity exactly when g fixes every point in
this list. An affine point is fixed exactly when both coordinates
are fixed; the origin is F-rational. Hence its kernel is exactly
the pointwise fixing subgroup of F(S_7). By the Galois
correspondence this is the kernel field F(S_7)=K_glob, precisely
the full-torsion field in Definition 3.1(c). The representation
and coordinate-kernel convention are those cited in L045
(Sutherland, Lecture 20, section 20.1; Yvon, arXiv:2407.14370v1,
Introduction); the Galois correspondence is Milne, *Fields and
Galois Theory*, v5.10, Theorem 3.17, as imported there. No
cyclic subgroup, one-coordinate field or chosen rank-one cover is
substituted for the full kernel. This checks the definition without
claiming that every other clause of Definition 3.1 is satisfied.

**Selected member and completion.** Under L060's stated surjection,
r_place(sigma(v))=v and sigma(v_*)=w. If a section member sigma(v)
lies over v_*, then v=v_*, so it equals w. Consequently

    sigma(V(F_mod)) intersect r_place^(-1)({v_*}) = {w}.

Thus the local field required at this selected member is the
completion at the original w, not at an arbitrarily exchanged
place, nor at every member of the whole fiber. Restriction of w
to F is the original u. L045, applied to the same curve by L048,
proves that F is dense in H and H(S_7)=N. K_glob=F(S_7) is
contained in the complete N, and its closure contains H and S_7,
hence N; it is therefore exactly N. This is the induced embedded
completion, as in Milne, *Algebraic Number Theory*, v3.08, section 8
before Proposition 8.1, pp.135-136, cited and checked in L045 and
L054. Thus native K_w=N, without identifying the number field K
with N or using a degree match. L060's conditional restriction
also retains residue characteristic three at v_*.

**Underlying curve and parameter.** Definition 3.1(e) uses the
base change of X_F at that completion. The coefficients and origin
of E_0 are Q-defined and the embedding restricts to Q -> Q_3,
so this is exactly (E_0 over N) minus its origin. The pointed
Q_3-isomorphism in L048 base-changes to N. L054's separately
audited application of Kedlaya, *Introduction: the Tate curve*,
Theorem 2(a),(b), p.4, checks parameter uniqueness over this finite
extension: j is unchanged, v_3(j)=-30, and q_0 remains a nonzero
parameter of positive valuation. Thus the underlying elliptic
curve in Example 3.2(iv) has q_w=q_0. No parameter of a covering
curve, or the old rational value 3^30, occurs in this assignment.

**Root convention.** Example 3.2(iv), printed p.71, takes a
2ell-th root of that geometric parameter, with mu_(2ell)
ambiguity. Its substitution here is X^14-q_0. L069 already proves
that its entire root set in Omega is rho_0 mu_14 subset N,
using L054's square root in H and the full seven-torsion of this
same changed curve. It also proves v_3(r)=15/7 for every root.
These are exactly the parameter, exponent and ambiguity in the
imported convention, so no additional radical or field enlargement
is required. This comparison does not independently identify a
theta value: Example 3.2 assumes initial Theta-data, and its
theta-evaluation statement is not invoked here to manufacture them.
The independent ell*Z covering ambiguity is retained; root-coset
membership does not resolve it or fix a marking across any link.

The full-kernel, selected-member, embedded-completion, unchanged-base
parameter and root-coset checks all pass conditionally. The resulting
prerequisite clarification can be used with the repeated (w,w)
packet above and L068's algebraic root-ambiguity conclusion. It
does not identify actual pilot images with an acted scalar shell,
establish native permission for the reference group, or prove the
source-marked all-image factorization. Full initial Theta-data and
IUT IV Theorem 1.10's additional global assumptions remain separate
obligations, including its specified global F equality. Essentiality
and the original finite B>=A gap remain open. ATTEMPTS/027,031,032
retain their stops; no exact-curve globalization, marked-coordinate
comparison or tensor-enclosure objection has been reopened.

### Separate critical audit — 2026-10-17, step 271

**Verdict and hypotheses.** The application passes the pre-invocation
SPECIALIZE assessment
`drafts/literature/2026-10-17-retained-native-field-radical-dictionary-critical-audit.md`.
No correction or extra mathematical premise is needed for its stated
conditional conclusion. The inputs remain L045,L048,L054,L060,L069,
with precisely the curve, origin, embedding, precision and places in
the hypotheses above. The inspected May 2020 reproduction is the source
being compared; author/reproduction identity and journal equivalence
remain unverified. This verdict neither verifies those identities nor
certifies the other clauses of initial Theta-data.

**Full kernel.** On the same E_0, the full level-seven representation
is trivial on an element of G_F exactly when that element fixes all
49 geometric torsion points. The origin is already rational; each
remaining point is specified by both affine coordinates. Therefore
this condition is exactly pointwise fixing of S_7, not preservation
of the set S_7. The finite coordinate field F(S_7) is Galois because
the representation kernel is normal, and the Galois correspondence
identifies that kernel's fixed field with K_glob. This checks Definition 3.1(c)
using the full-torsion convention and Milne Theorem 3.17 cited above.
It does not substitute L053's rank-one cover or its kernel. In
particular this equality requires no full GL_2 image assertion and
does not purport to verify clause (c)'s other conditions.

**Selected member.** In L060's conditional native setup,
r_place(sigma(v))=v for every moduli place and sigma(v_*)=w.
Applying r_place to a section member over v_* forces v=v_*;
conversely w is that section member. This proves both inclusions in
the displayed singleton equality. The whole restriction fiber may
contain other places. The audit uses the original w, with restriction
u on F, and neither replaces F_mod by Q nor assumes the independent
admissibility of the designated bad subset. The conclusion concerns
the local field at this member only.

**Embedded completion.** L045's agreement of the complete global
and local torsion sets is applicable to the same reselected E_0 by
L048. Consequently H(S_7)=N and K_glob=F(S_7) is contained in N.
The closure of F in N is H: it is dense in H, and the complete
finite extension H is closed in N. The closure of K_glob is a
field containing H and S_7, hence contains N; it is also contained
in N. Both inclusions give equality. The coordinate extension is
finite separable in characteristic zero and the valuation is the
chosen extended one, checking the hypotheses of Milne's embedded
completion statement cited above. Thus the equality K_w=N is an
embedded completion equality, not an identification K_glob=N or a
comparison of degrees. No completeness of the algebraic closure
Omega is assumed.

**Unchanged base parameter.** The actual coefficients and origin
are Q-defined, so base change of X_F at w is precisely E_0 over N
minus that origin. It is not a covering elliptic curve. The pointed
Q_3 Tate isomorphism of L048 base-changes to this curve over N.
The hypotheses of Kedlaya Theorem 2(a),(b) used in L054 remain
valid: N/Q_3 is finite, j has absolute valuation -30, and the same
nonzero q_0 has absolute valuation 30. Parameter uniqueness therefore
identifies the underlying curve's q_w with q_0. Neither rescaling
the discrete valuation on N nor choosing a Tate representative
changes this element. No equality with the former 3^30 is used.

**Complete root convention.** In the inspected Example 3.2(iv),
the exponent is 2ell for the underlying base parameter. With ell=7
and q_w=q_0 it is exactly the polynomial audited in L069. That
result supplies a nonzero rho_0 in N and all of mu_14 in N.
For any root r in Omega, r/rho_0 has fourteenth power one;
conversely rho_0 times every such root of unity is a root.
Thus the entire set, not just one representative, is rho_0 mu_14
inside unchanged N. Applying the absolute valuation gives
14v_3(r)=30 and v_3(r)=15/7 for each root. This uses the audited
L069 result, not a new radical construction or a theta-value theorem.
The simultaneous square/seventh-root identities for its constructed
rho_0 are not imposed on every other coset member.

**Applicability limit.** All five assignments pass as evaluations of
the cited conventions conditional on the retained setup. Example 3.2
assumes initial Theta-data for its actual theta evaluation; this
audit invokes only its root convention and makes no converse claim.
Root-set membership fixes neither a source marking nor the independent
ell*Z covering ambiguity. It proves no factorization of all images
through L068's acted shell, no permitted-action identification and no
additional global hypothesis of IUT IV Theorem 1.10. ATTEMPTS/027,031,032
remain intact. The result secures conditional prerequisites only;
essentiality and finite B>=A remain unresolved. It is a known-method
applicability audit with no beyond-source advance. No mathematical
script or numerical certificate is needed for these exact checks.

### Mathlib

Full matching coverage for this conditional IUT field/root dictionary
is **not checked**. Supporting Galois-kernel, embedded-completion and
Tate-parameter coverage is not checked here. No absence or formal
verification claim follows. Known results and definitions are imported
by the precise citations above; only their retained-object applicability
is checked.

## Specified global descent: source record — 2026-10-17, step 272

### Hypotheses

This section records sources only; it does not apply a new theorem to
the retained E_0,F. Use the same IUT IV version convention above.
The author endpoint supplied continuous text on 2026-10-17;
byte identity with the earlier reproduction remains unverified.
Retain the conditional native F_mod subset T=F_tpd subset F setup.

### Conclusion

IUT IV, **Theorem 1.10, printed p.22**, defines its field prescription
by F=T(sqrt(-1),E_L[15]), for a Legendre descent E_L/T of the
geometric curve. Its F_mod/30 notation abbreviates this prescription;
it does not select L045's arbitrary original E_0 model. The
Legendre equation is specified in **Corollary 2.2, p.41** as
y^2=x(x-1)(x-lambda), lambda!=0,1; the field hypothesis is repeated
on **p.42**. The retained equality is unproved.

### Proof / precise cited inputs and qualifications

Read [IUT IV](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf),
**Proposition 1.8(i)-(iv),(vi), pp.18-21**, including the proofs
of (iv),(vi). Over a perfect field, (ii) describes descent and the
j-field; (iii) makes the 2-torsion action independent of descent
when geometric origin-preserving automorphisms are {+1,-1}.
Part (vi) assumes additionally char(k)!=2, G_E=G_k and trivial
2-torsion action; its proof allows a quadratic twist before Legendre
form. Part (iv) compares two descents of one geometric curve over
the same perfect field: full rational ell-torsion on **both**,
ell>=3 invertible in that field, implies an isomorphism there.
Its proof invokes the faithful torsion action of (i) to identify
the descent section. It supplies no one-model rationality shortcut.

For a future conditional compatibility test, the known twist
classification is in [Sutherland, MIT 18.786, Lecture 21,
6 May 2024](https://math.mit.edu/classes/18.786/2024/LectureNotes21.pdf),
**section 21.2, p.2**: j!=0,1728 gives geometric automorphisms
{+1,-1} and continuous quadratic characters; characteristic other
than 2,3 permits the usual short-equation twist. The actual common
field, nonexceptional j and comparison isomorphism must be checked.
[Gonzalez-Jimenez, Lozano-Robledo and York,
arXiv:2408.04159v1, 8 August 2024](https://arxiv.org/pdf/2408.04159v1),
**Lemma 3.4 proof, p.12**, explicitly computes the formula
rho_(E^d,n)=chi_d rho_(E,n) in transported bases. Import only that
coordinate formula, for a number field, nonsingular short equation,
d!=0 and n>2. Do **not** import the stronger division-field
equality of part (2); its kernel step is not certified here.

The full-coordinate kernel convention is [Yvon,
arXiv:2407.14370v1, 19 July 2024](https://arxiv.org/pdf/2407.14370v1),
**Introduction, p.2**: ker(rho_(E,n))=Gal(k-bar/k(E[n])).
[Sutherland, Lecture 20, 1 May 2024](https://math.mit.edu/classes/18.786/2024/LectureNotes20.pdf),
**section 20.1, pp.1-2**, supplies the representations and closed
subgroup Galois correspondence. These apply to whole point sets,
not just x-coordinates or isomorphism classes of image groups.

L045,L048 establish full torsion for the retained E_0, with a fixed
F. They do not yet check the indicated Legendre descent's torsion
or exact generation over T(sqrt(-1)). An eventual F-isomorphism
alone would still leave that latter obligation. The source comparison
and unused stronger-result lead are recorded in
`drafts/2026-10-17-retained-global-model-source-comparison.md`.
No retained twist-character value, field equality, sufficient data,
marked transport, numerical conclusion or IUT flaw is proved here.

### Mathlib

Full matching and supporting coverage for this model/field comparison
is **not checked**. No absence or formal-verification claim is made.
