# L114 — All-place etale injections on the reselected objects

## Hypotheses

Retain exactly L107's and L113's objects, fields and maps. In particular,
F=C_o and K=K_C are number fields in the fixed algebraic closure Fbar;
F contains iota with iota^2=-1; ell>=7; and

    X_F=E_o minus O, X_0=(X_F)_K, Y=B minus V,
    C_F=[X_F/{±1}], Z=(C_F)_K, A=[Y/{±1}].

The maps Y -> X_0 and A -> Z are L107's actual degree-ell covers,
and Y -> A and X_0 -> Z are the actual degree-two stack atlases.
Retain its geometric theta covers, with origin inversion, and L113's
section s', global cusp {Q,-Q} and pointwise bad-place witnesses.
No descent of U or B to F is stipulated. All inherited authentication,
source-version and def= qualifications remain in force.
The assertions about arithmetic theta models at designated bad places
use L113's step461 model assertions as hypotheses. Its separate step469
audit now validates that assembly. The step467 group audit below remains
a distinct argument and does not itself certify existence or native type.

For any place w of K (in particular every w selected by s'), put
u=w|F, h=F_u and k=K_w, using the actual embedded finite extension
h -> k. Choose a prolongation wbar to Fbar and compatible embeddings
in an algebraic closure Omega of k; h and k have this same algebraic
closure. At a complex place use the compatible embeddings in C.
Fundamental groups below are profinite etale groups, with compatible
geometric basepoints; their unpointed assertions are outer assertions.

## Conclusion

For T=Y,A,X_0,Z over K, and T=X_F,C_F over F, the natural completion
map pi_1(T_local) -> pi_1(T) is injective. Its image is exactly the
inverse image of the chosen absolute decomposition subgroup under the
structure map to G_K or G_F, with the induced profinite topology.
Geometric groups over Fbar, Omega and, at finite places, the completion
of Omega are naturally isomorphic under these specified embeddings.
These identifications preserve the actual geometric theta covering
subgroups, including their full profinite inverse-image descriptions.

All the following squares of group inclusions are cartesian: the
scheme/stack atlas squares for Y_k -> (X_0)_k and A_k -> Z_k; the
squares mapping these to X_F,h and C_F,h; their local-to-global
comparison squares; and the geometric and geometric-theta squares into
the local arithmetic groups. In particular, if D_T denotes pi_1(T_Fbar)
and D_T,theta denotes L107's geometric theta subgroup, both adjacent
squares in each of these arrays are cartesian:

    D_Y       -> pi_1(Y_k) -> pi_1((X_0)_k)
      |              |                  |
    D_A       -> pi_1(A_k) -> pi_1(Z_k)

    D_Y,theta -> pi_1(Y_k) -> pi_1((X_0)_k)
      |              |                  |
    D_A,theta -> pi_1(A_k) -> pi_1(Z_k).

Each arithmetic group in these arrays surjects onto the actual
G_k, identified with D_w inside G_K. At designated bad places, the
actual arithmetic theta-model groups from L113 inject too, retain
their geometric intersections D_Y,theta and D_A,theta, and surject
onto D_w. No arithmetic theta model at another place is asserted.

This establishes the group portion isolated in L113's narrowed
Definition 3.1(e) comparison, subject to its source qualifications.
It does not settle directed-cover hypothesis (*), complete initial
data, any tempered-group assertion, integral models at ell or 2,
or original finite B>=A. The separate step467 audit below validates the
group application with the stated conditional arithmetic-model scope.
L113 step469 subsequently discharges that model premise; neither result
is a complete flaw candidate.

## Proof

### Approved scope and imported results

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-25-all-place-group-injection-application.md`
and its completed scope comparison. These precise general results are
imported; the proof below checks their application and compatibility:

- Aaron Landesman, *Invariance of the tame fundamental group under
  base change between algebraically closed fields*,
  [arXiv:2005.09690v3, 20 January 2024](https://arxiv.org/html/2005.09690v3),
  Theorem 1.1 and the characteristic-zero observation preceding it.
  For our smooth connected punctured curves, normal separated finite
  type with smooth projective compactification, this gives the natural
  isomorphism of full etale groups under algebraically closed extension.
  The relevant smooth-curve proof case is Lemmas 2.6,2.9 and
  Proposition 2.10, as recorded in the scope assessment.
- Stacks Project, [Lemma 58.14.3, 0BTX](https://stacks.math.columbia.edu/tag/0BTX):
  the exact geometric/arithmetic sequence for a quasi-compact,
  quasi-separated scheme geometrically connected over its field.
- Vincent Zoonekynd, *The Fundamental Group of an Algebraic Stack*,
  [arXiv:math/0111071v1, 7 November 2001](https://arxiv.org/pdf/math/0111071v1),
  Corollary 6.4 and proof, printed pp.13–14: for a connected scheme T
  with finite constant group H acting on it,
  1 -> pi_1(T) -> pi_1([T/H]) -> H -> 1.
  Freeness of the action on T is not required. We use H={±1}.
- J. S. Milne, *Algebraic Number Theory*,
  [v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
  Corollary 7.62, p.132: a finite extension E/Q_p contains a number
  field N with Q_p N=E. Propositions 7.60–7.61 and their proofs,
  pp.131–132, justify that result. Section 8 opening/Proposition 8.1,
  pp.135–136, identifies the embedded finite completions. Proposition
  8.10 and its proofs, p.139, identifies a finite Galois decomposition
  group with the completion Galois group. Remark 7.41, p.124, records
  the algebraically closed completion C_p.
- The finite-etale subgroup/pullback correspondence is Stacks
  [Theorem 58.6.2, 0BND](https://stacks.math.columbia.edu/tag/0BND)
  and [Section 58.7, 03SF](https://stacks.math.columbia.edu/tag/03SF),
  already used, with the actual finite quotient-stack covers, in L107.
  Its geometric theta groups use Mochizuki, *The Etale Theta Function*,
  PRIMS 45 (2009), Proposition 2.2(i)–(iii), pp.262–264, and Definition
  2.3, p.264 ([journal PDF](https://ems.press/content/serial-article-files/41069?nt=1)).

The comparison predicate is *IUT I*, May 2020, Definition 3.1(e),
printed pp.62–63 in the qualified
[186-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf).
Its subscript w base-changes both F- and K-curves to K_w. Accordingly,
the displayed arrays use (X_0)_k and Z_k on the right. We also check
the intermediate F_u maps requested in the approved scope. We do not
resolve flattened source decorations by guessing: the basic geometric
and theta-geometric arrays are both given explicitly above.

Main gap remains finite B>=A. The intermediate can close the separate
etale-group obligation, without the directed-module obligation. Its
pass test is actual decomposition images, all places, full theta
subgroups and simultaneous cartesian identities. L107's global
application/audit and L113's narrowed assembly withheld precisely this
comparison; their statements are not duplicate completed proofs of it.
ATTEMPTS/031's marked-atlas issue and ATTEMPTS/035's authentication
stop remain parked. No new general invariance theorem is proposed.

### Absolute decomposition comparison at a finite place

First fix either global number field M=F or M=K, its actual completion
m, and the chosen embedding Fbar -> Omega prolonging its place.
The image of Fbar contains every element of Omega algebraic over M:
it is algebraically closed and contains M, so contains all roots in
Omega of every polynomial over M. For finite Galois L/M inside Fbar,
its completion at the induced place is the embedded field mL. Indeed
mL is finite over m, contains the dense image of L, and is its closure
there; this is the finite-completion identification cited above.
It is Galois over m because L/M is Galois.

These mL are cofinal among finite extensions in Omega. To verify this
on the actual embeddings, let E/m be any finite subextension of Omega.
Then E/Q_p is finite. Milne Corollary 7.62 supplies N contained in E,
a number field, with Q_p N=E. Thus N is in the image of Fbar. Take
L/M finite Galois in Fbar containing MN. We have

    E=Q_p N contained in mL contained in Omega.

Conversely each mL is a finite subextension of Omega. This proves
Omega is the union of this directed family; restricting to finite
Galois E gives the required cofinality for absolute Galois groups.
This is an application of the cited realization theorem, not a
reproof of Krasner's lemma or an assumption that Fbar is m-algebraic.

For each such L, let D_L be the stabilizer of the induced place in
Gal(L/M). Milne Proposition 8.10 identifies D_L with Gal(mL/m), by
restriction and continuous extension. These identifications commute
with restriction for nested global Galois extensions: both maps are
restriction of the same automorphism on the dense embedded fields.
A compatible family in the D_L defines an automorphism of Fbar fixing
M, and preserves its place because its restriction to every L does.
The converse is immediate. Hence, with the actual restriction maps,

    D_M = lim_L D_L
        = lim_L Gal(mL/m)
        = Gal(Omega/m).

The last equality follows from the cofinality just established. All
maps are continuous; inverse-limit topology is the subspace topology
of the closed stabilizer D_M in G_M. This proves a topological
identification of the actual groups, rather than an abstract isomorphism.
In particular, for the compatible F,K choices,

    D_K = D_F intersect G_K inside G_F,
    G_k -> G_h corresponds to D_K -> D_F.

Here and below D_K=D_w and D_F=D_u. Neither K/Q normality nor
surjectivity of D_w onto G_K is used.

The closure of Fbar in the completion Omega_hat is all of Omega_hat.
Indeed it contains Q_p, and each E above equals Q_p N for N in Fbar,
so it contains every finite E in Omega. Their union is Omega, which
is dense in Omega_hat. Thus the completion of the valued Fbar is
identified with Omega_hat, not with Omega itself. Omega_hat is the
algebraically closed C_p of the cited characteristic-zero situation.
We will use the two algebraically closed field extensions separately.

### Complex places

Every embedding of F in R would send iota to a real root of x^2+1,
which is impossible. Thus F and K have only complex archimedean
places. At any such compatible u,w, h=k=C, and Omega=C is already
algebraically closed and complete. The stabilizer in G_M of the
chosen complex place of Fbar is trivial. To see this, a stabilizing
automorphism extends continuously to C and fixes the dense image of
M, hence fixes C. Its restriction to Fbar is therefore the identity.
The density used here holds since the image of M contains
Q+iota Q, a dense subset of C. Thus D_u=D_w=G_C=1. No real-place
sequence or complex conjugation subgroup is inserted.

### Geometric comparison and arithmetic exactness on these objects

The scheme atlases X_F, X_0 and Y are smooth geometrically connected
punctured elliptic curves in characteristic zero. They are separated
and finite type and have their given smooth proper elliptic
compactifications. Any connected finite-etale geometric theta cover
of such a curve is again a smooth connected curve with smooth proper
compactification (normalize the proper curve; in characteristic zero
a normal curve over an algebraically closed field is smooth).
Landesman's cited case therefore applies to the natural maps for
Fbar -> Omega -> Omega_hat. At complex places use Fbar -> C.
It gives full etale-group isomorphisms; residue characteristics ell
or 2 cause no prime-to-residue-characteristic restriction here.

For W=X_F or Y and H={±1}, use Zoonekynd's natural exact sequence
for W and its base changes. The geometric comparison on W is an
isomorphism, and the quotient H maps identically to H. Comparing the
two exact sequences therefore gives an isomorphism also for [W/H].
This preserves the actual degree-two atlas and its stabilizers; it
uses no coarse-space replacement or fixed point for the inversion.

For completeness, the arithmetic exactness needed for these particular
stacks follows from the same sequences and 0BTX, rather than applying
a scheme theorem directly to a stack. The diagram for W_bar -> W has
rows

    1 -> pi_1(W_bar) -> pi_1([W_bar/H]) -> H -> 1
    1 -> pi_1(W)     -> pi_1([W/H])     -> H -> 1.

The left vertical map is injective by 0BTX, so the middle one is
injective too: its kernel maps trivially to H and is then tested on
the left. The structure map pi_1([W/H]) -> G_m is surjective because
its restriction pi_1(W) -> G_m is. Its kernel is exactly the top
middle group: for an element in the kernel, choose an element of the
top middle group with the same image in H. Their quotient lies in
pi_1(W), and has trivial G_m image, so belongs to pi_1(W_bar) by
0BTX. Conversely the whole top middle group has trivial G_m image
by its geometric structure map. This proves the required exact row.
Apply with m=h,k,F,K as appropriate. All the schemes are geometrically
connected, so every use of 0BTX meets its connectedness hypothesis.

Choose one geometric point above the scheme atlas Y in the common
algebraically closed overfield, and take all its images. For a theta
cover choose a point above this one and the induced fiber-functor
identification. The scalar-extension maps, atlas maps and covering
maps now give commuting homomorphisms in the same diagram. No
independently chosen conjugacies are asserted to agree.

For any listed T over M with completion m we consequently have a
commutative diagram of short exact sequences

    1 -> pi_1(T_Omega) -> pi_1(T_m) -> G_m -> 1
    1 -> pi_1(T_Fbar) -> pi_1(T)   -> G_M -> 1,

whose left map is the natural isomorphism and whose right map embeds
G_m as D_M by the preceding comparison. The middle map is injective:
a kernel element is geometric and the left map is injective. Its
image is the whole preimage of D_M: for gamma in that preimage, lift
its arithmetic image to pi_1(T_m), using the top surjection; the
remaining difference is geometric and lifts through the left
isomorphism. This also proves the stronger natural pullback identity

    pi_1(T_m) = pi_1(T) times_(G_M) D_M.

The continuous bijection is a homeomorphism since its source is
compact and its target is a closed subgroup of a profinite group.
No section of either arithmetic sequence was chosen.

### All the actual local intersections

Use L107's already audited global embedding in P=pi_1(C_F). Write
J=pi_1(X_F), S=pi_1(A), R=pi_1(Y), and q:P -> G_F. Its actual
cartesian atlas square and geometric connectedness give

    R=S intersect J,
    q(S)=q(R)=G_K,
    pi_1(Z)=q^(-1)(G_K).

Put D=ker(q). Thus D_A=S intersect D, D_Y=R intersect D, and
the geometric group of X_F is J intersect D. All these are the
actual subgroups with the compatible basepoints just specified.

The completion comparisons identify

    P_u=pi_1(C_F,h)=q^(-1)(D_u),
    P_k=pi_1(Z_k)=q^(-1)(D_w),
    J_u=pi_1(X_F,h)=J intersect P_u,
    J_k=pi_1((X_0)_k)=J intersect P_k,
    S_w=pi_1(A_k)=S intersect P_u=S intersect P_k,
    R_w=pi_1(Y_k)=R intersect P_u=R intersect P_k.

For example, q(S) is in G_K, so membership of an element of S in
q^(-1)(D_u) is equivalent to membership in q^(-1)(D_u intersect G_K),
which is q^(-1)(D_w). The local-to-global comparison for A identifies
that entire preimage, not only one subgroup of it. The same proof
applies to R. For X_0 and Z the constant-field cover K/F similarly
identifies their global groups with J intersect q^(-1)(G_K) and
q^(-1)(G_K), before the local restriction.

Taking intersections proves

    R_w=S_w intersect J_u=S_w intersect J_k.

These are exactly the group squares of the actual covers
Y_k -> X_F,h and A_k -> C_F,h, and of
Y_k -> (X_0)_k and A_k -> Z_k. The former horizontal maps include
the finite separable scalar extension k/h; the latter do not.
Both curve squares are 2-cartesian by L107's atlas square and base
change. Their full products are connected because they equal Y_k,
which is geometrically connected. The covering correspondence
therefore gives these full intersections, not a silently selected
component of a disconnected pullback.

The squares comparing the local and global groups are cartesian as
well. For instance S intersect P_u=S_w and R intersect J_u=R_w;
replacing F_u by K_w gives the analogous identities. Geometric
comparisons commute with each of these arrows and identify their
geometric intersections with D_A,D_Y,J intersect D and D. Every
closed intersection has its induced profinite topology. The covering
inclusions are open in their stated local targets, whereas the
completion image in the global group is asserted only to be closed.
These arguments hold for every w of K, and thus for every place of
s', including ell,2, undesignated bad places and infinity.

### Full theta pullbacks and the source's left-hand columns

Keep L107's quotient maps and finite subgroups, in its notation,

    q_A:D_A -> Q_A, q_Y=q_A|D_Y:D_Y -> Q_Y,
    D_Y=q_A^(-1)(Q_Y), L intersect Q_Y=M,
    D_A,theta=q_A^(-1)(L), D_Y,theta=q_Y^(-1)(M).

Here L is the order-2ell subgroup generated by M and the specified
order-two coset; it is not the present global extension field.
In particular L107 proves D_A,theta intersect D_Y=D_Y,theta.

Let f_A:D_(A_Omega) -> D_A be the natural geometric isomorphism,
and let f_Y be its restriction to the atlas subgroup. The actual
pullbacks of the retained theta covers have the full groups

    f_A^(-1)(D_A,theta)=(q_A f_A)^(-1)(L),
    f_Y^(-1)(D_Y,theta)=(q_Y f_Y)^(-1)(M).

These equalities are in the full profinite groups, not merely in
Q_A,Q_Y. Their indices remain ell,ell, and the theta atlas index
remains two. The same identities hold over Omega_hat or C.
To identify these pullbacks with the source's intrinsic geometric
theta construction, note that the natural isomorphisms preserve the
actual basic curve, its origin inversion and cusp, and hence the
closed commutator/power kernels defining the finite quotient. They
intertwine the inversion action and the designated coset in EtTh
Proposition 2.2. The arithmetic group over each algebraically closed
field is trivial; its cusp-section choice is therefore the unique
map from 1, just as in L107. The eigensubgroup M and subgroup L are
thus transported, not newly chosen. This proves the needed match of
finite constructions as well as the full inverse images.

Inside P, D is contained in P_k and P_u. Thus

    S_w intersect D=D_A, R_w intersect D=D_Y,
    D_A intersect R_w=D_Y,
    D_A,theta intersect R_w=D_Y,theta,
    D_A,theta intersect J_k=D_Y,theta.

The last equality uses D_A,theta contained in S intersect D,
R=S intersect J and D contained in P_k. These identities prove
both adjacent squares, and the outer square, in the two arrays of
the conclusion. They also prove their versions with J_u,P_u.
The finite geometric atlas square is the pullback of L107's theta
square. Over Omega the further maps to k are profinite-etale
covers: Omega/k is the union of finite separable extensions, and
the finite theta cover descends to one such extension, then is
pulled back through that tower. Scalar extension to Omega_hat gives
the same etale groups; the morphism Spec(Omega_hat) -> Spec(k)
itself is not being asserted to be profinite-etale. This distinction
avoids identifying an algebraic closure with its completion.

Finally, at a designated w=s'(p), p in Sigma, L113 supplies the actual
geometrically connected arithmetic theta covers T_w -> Y_k and
H_w -> A_k and their cartesian atlas square. The finite-etale
correspondence embeds their groups in R_w,S_w, and the comparison
just proved embeds these in the same global P. Their intersections
with D_A,D_Y are precisely the theta subgroups above, by L113's
same-origin geometric-model identification, retained here as an input.
The pullback comparison verifies transport of the geometric subgroups;
it does not independently establish those arithmetic models or their
native types. Geometric connectedness gives their
surjections to G_k=D_w. No global arithmetic theta splitting or
model at a nondesignated place has been inferred.

### Scope of the conclusion

The tests pass for the profinite etale arrows and squares just listed
on the unchanged objects. This is local notebook progress by a
REPRODUCTION application of the cited known methods; it supplies no
claim of mathematics beyond those sources. The separate step467 audit
validates only the conditional group application detailed below.
It closes neither directed (*) nor any full initial-data,
III/P7, exact-generation/full-repair, relative factor-four, actual
action/factorization/pilot, authentication/def=, essentiality or finite
B>=A obligation. No contradiction in IUT is established.

### Separate critical audit — 2026-10-25, step467

**Verdict and imports.** The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-25-all-place-injection-critical-audit.md`.
The listed group comparisons pass on the retained objects, using the
precise imports above and L107's audited global subgroup construction.
This is a REPRODUCTION audit, not a new general theorem. The final
arithmetic-model assertion is conditional on L113 step461: this audit
does not prove that assembly's local existence/type claims. Its former
parenthetical assertion that the model identification was also proved
here has been removed. The complex density sentence now explicitly
uses Q+iota Q. Neither correction changes a field, cover or group map.

**Embedded absolute limits.** For M=F or K and its finite completion m,
the image of Fbar contains all elements of Omega algebraic over M:
an algebraically closed subfield containing M contains every root of
every M-polynomial in Omega. Thus the N inside E in Milne 7.62 really
lies in that same Fbar, not in an independently isomorphic closure.
Since E/m is finite and m/Q_p is finite, that corollary applies to E.
Choose a finite Galois L/M containing MN in Fbar. Then E=Q_p N is
contained in mL. Conversely mL is finite Galois over m: the splitting
polynomials for L/M still split there and generate it over m.

The closure of L inside mL equals mL: it contains m, the closure of M,
and contains L, while mL is a complete finite extension of m. For
L contained in L', the finite decomposition isomorphisms from Milne
8.10 consequently commute with restriction, since their extensions
agree on the dense L. Cofinality implies that every element of Omega
belongs to some mL. A compatible family of finite decomposition
automorphisms therefore extends uniquely over their union Omega,
and restricts to the original place-preserving automorphism of Fbar.
Conversely an m-automorphism of Omega preserves its unique extended
valuation and restricts to the indicated global stabilizer. This
verifies both directions for the actual natural restriction map.

The stabilizer D_M is the intersection of the inverse images of the
finite D_L in G_M, hence is closed. Its inverse-limit topology is its
induced topology, since finite global Galois restriction kernels form
a neighborhood basis in G_M. The displayed absolute isomorphism is
therefore topological. No surjectivity onto G_M has been inferred.

For the two retained number fields, k=hK inside Omega. Indeed hK is
finite and complete over h and contains K; the closure of K contains
h and K, proving equality. Consequently an element of G_h fixes K
if and only if it fixes k. Under the actual restriction maps this
proves G_k corresponds to D_u intersect G_K=D_w. This checks the
otherwise essential intermediate F_u comparison without K/F or K/Q
normality. The closure of Fbar in Omega_hat contains Q_p and every N
above, hence every E=Q_p N and then all of Omega_hat. Algebraic closure
of Omega_hat is the separately cited C_p input, not a consequence of
density. No algebraicity of Omega_hat/k is claimed.

**Infinity, geometry and stacks.** Since iota lies in both number
fields, all archimedean completions are C. A stabilizer of a complex
place preserves its normalized absolute value, hence extends to the
completion. It fixes the dense Q+iota Q, so is the identity. Thus the
arithmetic image really is 1, and the local group is the geometric
group. This argument would not apply to a real completion, which the
retained field hypothesis excludes.

The scheme inputs to Landesman are smooth, separated, geometrically
connected punctured curves of finite type in characteristic zero, with
smooth proper compactifications. The same properties hold for their
connected finite-etale geometric covers. These are field extensions
of characteristic zero even above 2 or ell. Invariance therefore
concerns the full etale groups, not merely a prime-to-p quotient.
Zoonekynd 6.4 applies to each connected atlas and the finite constant
inversion group without a freeness hypothesis. Comparing its sequences
under the natural field extensions gives the claimed stack geometric
isomorphisms with the atlas subgroups retained.

The arithmetic stack argument uses only 0BTX for the geometrically
connected scheme atlas and 6.4. In its two-row diagram a kernel element
in the top middle group maps to 1 in H, hence to the injective left
column. For exactness at the bottom middle group, the top middle
group surjects to H; matching an H-image leaves an element of the
scheme arithmetic kernel, which is geometric by 0BTX. The geometric
middle group maps trivially to the field group by functoriality.
Surjectivity to the field group follows already from the scheme
atlas. This checks the chase, including the hypothesis that each
geometric atlas is connected, without using a scheme theorem on a stack.

For local-to-global comparison, the natural short-exact-sequence
diagram now has an isomorphism on geometric kernels and an injection
on arithmetic quotients. The proof's lifting argument identifies the
middle image with the *entire* preimage of D_M. Compactness and the
closed target give the asserted topology. All these homomorphisms use
compatible fiber functors through the same covers; they are not a
collection of separately conjugated abstract isomorphisms.

**Intersections and the two arrays.** In the one ambient P retain
R=S intersect J and q(S)=q(R)=G_K from L107. For H=S or R,

    H intersect q^(-1)(D_u)
      =H intersect q^(-1)(D_u intersect G_K)
      =H intersect q^(-1)(D_w).

The just-verified completion comparison identifies these full groups
with S_w,R_w. Similarly J_u=J intersect P_u and J_k=J intersect P_k,
so S_w intersect J_u=S_w intersect J_k=R_w. Intersecting any of these
equalities with D=ker(q) gives the geometric comparisons. In particular
R_w intersect D_A=D_Y. The finite covers on the two atlas squares have
full fiber product Y_k, which is geometrically connected; no choice of
one component is hidden in these intersection equalities. For the
constant-field cover K/F its local factor is precisely the chosen
k/h, as accounted for by D_w. Openness is required only for the stated
finite covering maps; completion images are closed, with no claim of
openness in global arithmetic groups.

**Full theta transport.** Reinspected EtTh Proposition 2.2(i)–(iii),
its proof and Definition 2.3, printed pp.262–264, at the journal URL
above, within the approved coverage. The retained origin inversion is
the one used there. The finite construction uses the closed commutator
and power kernels on the base punctured curve and its specified
rank-one covering subgroup. The natural geometric isomorphisms commute
with that covering diagram, and carry those kernels onto the matching
kernels. They thus induce compatible isomorphisms of Q_Y,Q_A, not just
equalities of orders. They intertwine inversion, hence carry its
specified eigensubgroup M and the characterized order-two coset to
their counterparts. The subgroup L generated by M and any representative
of that coset is unchanged by a representative change. Over an
algebraically closed field the cusp section has domain 1.

It follows that full inverse images, not only their finite quotients,
are transported by f_A,f_Y. Using L107's
D_A,theta intersect D_Y=D_Y,theta and D_A,theta contained in S intersect D
now gives

    D_A,theta intersect R_w=D_Y,theta,
    D_A,theta intersect J_k=D_Y,theta.

Together with S_w intersect J_k=R_w, these are exactly the left,
right and outer pullbacks in the theta array. Replacing theta groups
by the basic groups proves the first array; replacing J_k,P_k by
J_u,P_u proves the intermediate versions. Every equality is of actual
closed subgroups with induced topology. The finite indices ell,ell,2
are those already established in L107. The geometric theta covers
over Omega descend to a finite subextension of Omega/k and hence
give profinite-etale covers over k through that algebraic tower.
Base change to Omega_hat identifies their groups; it does not make
Spec(Omega_hat) -> Spec(k) a profinite-etale morphism.

**Conditional arithmetic models and boundary.** If T_w,H_w are the
geometrically connected finite-etale models with the specified
geometric fibers and atlas square asserted in L113 step461, their
groups embed in R_w,S_w by the covering correspondence, and then in
P by the proved comparison. Their intersections with D_Y,D_A are
exactly the prescribed theta subgroups by those geometric fibers.
Surjectivity onto G_k follows from geometric connectedness of T_w
and its scheme exact sequence, also for H_w through its atlas.
This establishes the claimed group consequences of the supplied model
assertions without certifying their construction or native type.

No new mathematical dependency is needed, and the DAG is unchanged.
The narrowed group input is now critically checked. L113's later
assembly, directed (*), full initial-data/III/P7, exact generation/full
repair, factor-four excess, actual action/factorization/pilot, source
authentication/def=, essentiality and finite B>=A are not settled.
No IUT flaw or complete candidate follows. Mathlib coverage remains
unchecked, rather than absent.

### Subsequent premise audit — 2026-10-25, step469

L113's separate step469 audit validates its step461 simultaneous assembly,
including the arithmetic theta models, their geometric fibers and atlas
square. Thus the model premise explicitly left conditional in step467
is now discharged with the same source and pointwise-choice qualifications.
The group proof above and the DAG are unchanged. L113 uses the covered
geometric base-change sources directly, not this lemma's dependent tail.
All other boundary statements of step467 remain in force.

## Mathlib

Full matching coverage is unchecked. No Lean theorem search or
formalization was performed; unknown coverage is not a claim of absence.
