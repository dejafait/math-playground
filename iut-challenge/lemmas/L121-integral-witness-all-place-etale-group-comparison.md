# L121 — All-place etale group comparison on the integral witness

## Hypotheses

Fix L118's one member, one ordering and one prime ell>=7, and retain
L119's line U and L120's entire simultaneous construction. In particular
keep the literal E_o, the embedded number fields

    F=C_o, K=C_o(E_o[ell]), iota in F, iota^2=-1,

the full-coordinate division field, alpha,psi,B,V,Q and the reselected
full section s'. Put

    X_F=E_o,F minus O, C_F=[X_F/{±1}],
    X_0=(X_F)_K, Z=(C_F)_K, Y=B minus V, A=[Y/{±1}].

Use L120's actual finite-etale covers and stack atlases, its geometric
theta covers (2), and its pointwise arithmetic models (7),(8) at
w in s'(S), where S={p:v_p(j(E_o))<0} is L119's full bad support.
Retain all source-version, authentication, Legendre-adjunction and
native-dictionary qualifications. No initial theta-data, U/B descent
to F, K/Q normality or global arithmetic theta splitting is assumed.

For each place w of K, let u=w|F, h=F_u and k=K_w with their actual
embedding h->k. Fix a prolongation to the fixed algebraic closure
Fbar containing K. At finite w embed Fbar in an algebraic closure
Omega of k compatibly with this prolongation and K->k; write
Omega_hat for its completion. Omega is also an algebraic closure
of h. At infinity use compatible embeddings in C. Groups are full
profinite etale fundamental groups. Use compatible geometric basepoints
through the stated covers; without basepoints the statements are outer.

## Conclusion

For T=Y,A,X_0,Z over K, or T=X_F,C_F over F, the natural completion
homomorphism is a topological embedding. Its image is precisely

    pi_1(T_local) = pi_1(T) times_(G_M) D_v,                 (1)

where M is its global base field and D_v is the actual stabilizer
of the chosen prolonged place in G_M. Thus completion images are
closed with the induced topology. Under compatible choices,
G_k->G_h is the inclusion D_w=D_u intersect G_K inside G_F.
At infinity D_u=D_w=1 and h=k=C.

The natural geometric maps for Fbar->Omega->Omega_hat (or Fbar->C)
are isomorphisms preserving the atlas subgroups and the full geometric
theta covering subgroups. Write D_T for pi_1(T_Fbar), and D_T,theta
for L120's specified geometric theta subgroup. Both adjacent squares
and the outer square in each array are cartesian as profinite groups:

    D_Y       -> pi_1(Y_k) -> pi_1((X_0)_k)
      |              |                  |
    D_A       -> pi_1(A_k) -> pi_1(Z_k)

    D_Y,theta -> pi_1(Y_k) -> pi_1((X_0)_k)
      |              |                  |
    D_A,theta -> pi_1(A_k) -> pi_1(Z_k).

The corresponding arrays with X_F,h and C_F,h on the right are
cartesian too. The local/global cover and constant-field group squares
specified by (4)–(6) below are cartesian; the finite covers have open
inclusions in their local targets. These statements hold for every w,
including places above 2,ell and all infinite places.

At each w in s'(S), the actual arithmetic model groups pi_1(T_w)
and pi_1(H_w) from L120 also embed in these same local and global
groups, have geometric intersections D_Y,theta and D_A,theta, and
surject onto G_k=D_w. Their double-cover square remains cartesian.
No arithmetic theta model outside s'(S) is asserted.

This is a known-method specialization on the fixed integral tuple,
validated by the separate step497 critical audit below. It supplies neither full native
initial data nor directed hypothesis (*), and establishes no essential
IUT flaw or original finite bound B>=A.

## Proof

### Gate, known inputs and relevance

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-26-integral-witness-all-place-group-comparison.md`.
L114's method and its step467 audit are reused, not its conclusion
about another existential witness. L118 supplies this witness's fields
and iota; L119 supplies its full section/support; L120 supplies the
actual global diagrams and independently audited geometric models.
Its step493 audit uses geometric base change directly, without the
arithmetic injections being proved here. There is no circular premise.

Import only the assessed general results:

- Milne, *Algebraic Number Theory*,
  [v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
  Propositions 7.60–7.61/Corollary 7.62, printed pp.131–132:
  every finite extension E/Q_p contains a number field N with
  E=Q_p N. Use the embedded finite-completion description in the
  section-8 opening/Proposition 8.1, pp.135–136, and Proposition
  8.10, p.139, identifying a finite Galois decomposition group with
  the Galois group of the actual completion. Remark 7.41, p.124,
  supplies the algebraic closedness of the completed algebraic
  closure of a finite p-adic field.
- Landesman, *Invariance of the tame fundamental group under base
  change between algebraically closed fields*,
  [arXiv:2005.09690v3, 20 January 2024](https://arxiv.org/html/2005.09690v3),
  Theorem 1.1 and its preceding characteristic-zero observation,
  with the smooth-curve cases in Lemmas 2.6,2.9/Proposition 2.10:
  the natural full etale group is unchanged for our normal connected
  separated finite-type curves with normal proper compactification
  under algebraically closed characteristic-zero extension.
- Stacks Project, [Lemma 58.14.3, 0BTX](https://stacks.math.columbia.edu/tag/0BTX),
  the exact geometric/arithmetic sequence for a quasi-compact
  quasi-separated scheme with connected algebraic-closure base change.
- Zoonekynd, *The Fundamental Group of an Algebraic Stack*,
  [arXiv:math/0111071v1, 7 November 2001](https://arxiv.org/pdf/math/0111071v1),
  Corollary 6.4 and complete proof, printed pp.13–14: for a connected
  scheme W with an action of a finite constant group H,
  1 -> pi_1(W) -> pi_1([W/H]) -> H -> 1.
  Freeness is not required. Here H={±1}.
- Stacks [Theorem 58.6.2, 0BND](https://stacks.math.columbia.edu/tag/0BND)
  and [Section 58.7, 03SF](https://stacks.math.columbia.edu/tag/03SF),
  the finite-etale cover/subgroup correspondence and its functoriality,
  with quotient-stack descent through the actual atlases.
  L120's specific theta quotients are those of Mochizuki,
  [*The Etale Theta Function*, PRIMS 45 (2009)](https://ems.press/content/serial-article-files/41069?nt=1),
  Proposition 2.2(i–iii) and complete odd-level proof, pp.262–264,
  and Definition 2.3, p.264. Only the already assessed construction
  and its natural full preimages are used.

The comparison predicate remains the qualified May 2020 IUT I
reproduction, Definition 3.1(e), pp.62–63, specified in L120. This
proof makes explicit group assertions, not a verdict on all source
decorations or on the directed module/action (*).

Main gap: finite B>=A under the original hypotheses. This intermediate
can supply independent group prerequisites on the same integral tuple.
Its continuation test is that every actual map/image/topology and
theta intersection below is justified without changing any object or
assuming descent. An essential uncovered source case would require
narrowing or separate review. The scoped duplicate/failure check in
the assessment and ATTEMPTS/031,035–036 leaves those stopped mechanisms
untouched. No new general invariance theorem is being reproved.

### Embedded finite cofinality and absolute decomposition images

Fix finite w, and first consider either M=F or M=K, with completion
m=h or k. The image of Fbar in Omega contains every element of Omega
algebraic over M: it is algebraically closed and contains M, hence
contains all roots in Omega of every polynomial over M. For a finite
Galois L/M in Fbar, mL is a finite Galois extension of m. It is the
actual completion of L at the induced place: the closure of L
contains m (the closure of M) and L, hence mL; conversely mL is
complete and closed and contains L. Normality follows because the
splitting polynomials generating L over M still split over mL.

The fields mL are cofinal among finite extensions in Omega. Indeed,
for any finite E/m inside Omega, E/Q_p is finite. Milne 7.62 supplies
a number field N inside that actual E with E=Q_p N. Its elements are
algebraic over M, so N lies in the same embedded Fbar. Choose a
finite Galois L/M there containing MN. Then E is contained in mL.
Conversely every mL is finite over m and lies in Omega. In particular
Omega is the union of this directed family of finite Galois fields.

Let D_L be the stabilizer of the induced place in Gal(L/M).
Milne 8.10 identifies it by continuous extension with Gal(mL/m).
For nested L these identifications commute with restriction, since
both extensions agree on the dense smaller L. A compatible family
in the D_L defines an M-automorphism of Fbar preserving its place,
and every such automorphism gives that family. Cofinality then gives

    D_v = lim_L D_L = lim_L Gal(mL/m) = Gal(Omega/m).          (2)

This is the actual restriction homomorphism. In the other direction,
an m-automorphism of Omega preserves the extended valuation on every
finite subextension (uniqueness over complete m) and preserves Fbar,
so restricts to the stated stabilizer. The finite restriction kernels
form a neighborhood basis, and D_v is the intersection of the inverse
images of the finite stabilizers. Thus it is closed in G_M and (2)
is a homeomorphism for the induced profinite topology.

For the compatible F,K choices, k=hK inside Omega: hK is finite
complete over h and contains K, and the closure of K contains h
and K. Therefore an element of G_h fixes K exactly when it fixes k.
The same restriction maps in (2) give

    G_k -> G_h  =  D_w -> D_u,    D_w=D_u intersect G_K.      (3)

This uses no K/Q normality. The chosen k is the actual factor
corresponding to w, rather than a replacement completion.

The closure of Fbar in Omega_hat is all of Omega_hat: it contains
Q_p and every N above, hence every E=Q_p N, then Omega and its
completion. By the cited completed-algebraic-closure theorem Omega_hat
is algebraically closed. Omega and Omega_hat remain distinct; no
algebraicity of Omega_hat/k is asserted.

### Complex places

Both F and K contain iota, so neither has real places. At infinity
h=k=C. A stabilizer of the chosen place on Fbar preserves its normalized
absolute value and extends to C. It fixes the image of M, which
contains the dense Q+iota Q, so is the identity. Hence D_u=D_w=1,
in agreement with G_C=1. No real-place conjugation group is inserted.

### Natural geometric and arithmetic comparisons

The actual atlases X_F,X_0,Y are smooth geometrically connected
separated finite-type punctured elliptic curves in characteristic
zero, compactified by their smooth proper elliptic curves. Their
normal compactifications satisfy Landesman's hypotheses. Apply its
characteristic-zero case to Fbar->Omega and Omega->Omega_hat; at
infinity use Fbar->C. These are natural isomorphisms of full etale
groups. Even above 2 or ell the fields in these maps have
characteristic zero; no prime-to-residue-characteristic quotient or
integral-model conclusion is involved.

For the inversion quotients, compare Zoonekynd's atlas sequences.
The atlas geometric group map is the just-established isomorphism
and the quotient {±1} map is the identity. The middle map is thus
an isomorphism, retaining the atlas subgroup and interior stabilizers.

Arithmetic exactness for these particular stacks follows from the
same sequences and 0BTX on the scheme atlases. For an atlas W over
a field m occurring here, compare

    1 -> pi_1(W_bar) -> pi_1([W_bar/{±1}]) -> {±1} -> 1
    1 -> pi_1(W)     -> pi_1([W/{±1}])     -> {±1} -> 1.

The left vertical map is injective by 0BTX; a kernel element of the
middle vertical map maps to 1 in {±1} and is then killed by this
left injection. The structure map from the lower middle group onto
G_m is surjective already on pi_1(W). An element in its kernel
can be multiplied by an element of the top middle group with the
same {±1}-image. The quotient lies in pi_1(W) with trivial G_m-image,
hence in pi_1(W_bar) by 0BTX. Conversely the top middle group has
trivial G_m-image. This proves the exact geometric/arithmetic row
for each stack; it does not apply a scheme theorem directly to stacks.
All the atlases are geometrically connected, as required.

Fix a geometric point of Y over Fbar and all its images, then a point
above it on each geometric theta cover. For each w transport these
points through the chosen field embedding; choose arithmetic model
lifts compatibly where provided. Scalar extension and covering maps
then give commuting homomorphisms through the same fiber functors.
This avoids independently chosen conjugacies in different squares.

For any listed T over M with completion m there is now a natural
diagram of exact rows

    1 -> pi_1(T_Omega) -> pi_1(T_m) -> G_m -> 1
    1 -> pi_1(T_Fbar) -> pi_1(T)   -> G_M -> 1.

The left map is an isomorphism; the right map is (2), or the trivial
complex decomposition inclusion. A middle kernel element is geometric
and hence trivial. For an element of pi_1(T) over D_v, lift its
arithmetic image to the upper row and correct the difference using
the geometric isomorphism. This proves its image is the entire
preimage in (1). The resulting continuous bijection from a compact
group to a closed subgroup of a profinite group is a homeomorphism.
No arithmetic section has been chosen in this argument.

### Actual subgroup intersections and cartesian squares

Use L120's global cover diagram in the one ambient group
P=pi_1(C_F), with compatible basepoints, and write

    q:P->G_F, D=ker(q), J=pi_1(X_F),
    R=pi_1(Y), N=pi_1(A).

L120's connected cartesian atlas product and geometric connectedness give

    R=N intersect J, q(R)=q(N)=G_K,
    P_0=pi_1(Z)=q^(-1)(G_K),
    J_0=pi_1(X_0)=J intersect P_0,
    D_A=N intersect D, D_Y=R intersect D.                    (4)

Let P_u=q^(-1)(D_u) and P_k=q^(-1)(D_w). By (1) these are the
actual groups pi_1(C_F,h) and pi_1(Z_k). Similarly put
J_u=pi_1(X_F,h), J_k=pi_1((X_0)_k), N_w=pi_1(A_k) and
R_w=pi_1(Y_k). Equation (1) and (3) identify their full images as

    J_u=J intersect P_u, J_k=J intersect P_k,
    N_w=N intersect P_u=N intersect P_k,
    R_w=R intersect P_u=R intersect P_k.                     (5)

For example q(N) lies in G_K, so intersecting N with q^(-1)(D_u)
is equivalent to intersecting it with q^(-1)(D_u intersect G_K).
By (3) this is N intersect P_k, which (1) identifies with all of
pi_1(A_k). Thus no unspecified subgroup of this preimage is used.
The same argument applies to R. It follows that

    R_w=N_w intersect J_u=N_w intersect J_k,
    P_k=P_0 intersect P_u, J_k=J_0 intersect J_u.             (6)

Equations (4)–(6) prove the local atlas squares, their comparisons
to X_F,h,C_F,h, and the local/global cover group squares. They
also prove the constant-field group squares through P_0,J_0. The
chosen k/h is the factor selected by w; we do not identify
Spec(k) with the full potentially disconnected Spec(K tensor_F h).
For the atlas squares themselves the actual full 2-fiber product
is Y_k, by L120 and base change, and is geometrically connected.
There is no discarded component in these atlas intersections.

Since D is contained in P_k and P_u, intersecting the same identities
with D gives all geometric versions. In particular

    N_w intersect D=D_A, R_w intersect D=D_Y,
    D_A intersect R_w=D_Y, D_A intersect J_k=D_Y.

These are the left and outer pullbacks in the first array; (6)
is the right pullback. The same holds with J_u,P_u on the right.
All equalities are closed subgroup equalities with induced topology.
Finite cover inclusions are open in their local targets; completion
inclusions are claimed only to be closed globally. Every w was
arbitrary, including places outside the designated bad set.

### Full theta transport and arithmetic model images

Keep precisely L120's finite quotient maps and subgroups (2):

    q_A:D_A->Q_A, q_Y=q_A|D_Y:D_Y->Q_Y,
    D_Y=q_A^(-1)(Q_Y), L_theta intersect Q_Y=M_theta,
    D_A,theta=q_A^(-1)(L_theta),
    D_Y,theta=q_Y^(-1)(M_theta).

Let f_A:D_(A_Omega)->D_A and f_Y:D_(Y_Omega)->D_Y be the natural
geometric isomorphisms above. They commute with the actual covers,
origin inversion and closed commutator/power kernels
defining these finite quotients. They thus induce compatible quotient
isomorphisms, preserve the minus eigensubgroup M_theta, and carry
the specified order-two coset of EtTh Proposition 2.2(iii) to its
counterpart. The subgroup generated with M_theta is unaffected by
changing a representative within that coset. Over an algebraically
closed field the cusp section has trivial domain, so no additional
arithmetic splitting is required for this geometric construction.
Consequently the actual geometric theta pullbacks have groups

    f_A^(-1)(D_A,theta)=(q_A f_A)^(-1)(L_theta),
    f_Y^(-1)(D_Y,theta)=(q_Y f_Y)^(-1)(M_theta).              (7)

These are full profinite preimages, with indices ell,ell and atlas
index two. The same argument applies over Omega_hat or C. It
identifies the intrinsic constructions through their natural maps,
rather than matching only their orders. L120's same-origin geometric
model identification (8), independently audited in step493, is the
pointwise arithmetic-model input consistent with (7).

Since D_A,theta lies in N intersect D, (4) and the finite intersection
L_theta intersect Q_Y=M_theta give

    D_A,theta intersect R_w=D_Y,theta,
    D_A,theta intersect J_k=D_Y,theta.

Together with (6) these prove the second array and its intermediate
h-version, as full closed subgroup pullbacks. The geometric finite
theta atlas square itself is preserved by the same cover pullbacks.
Over Omega a finite theta cover descends to some finite subextension
of Omega/k and pulls back through that algebraic tower. Thus the
geometric-to-arithmetic arrows have the usual profinite-etale cover
interpretation. Scalar extension to Omega_hat preserves their groups;
Spec(Omega_hat)->Spec(k) is not asserted to be profinite-etale.

Finally fix w=s'(p), p in S. Retain L120's actual arithmetic models
T_w,H_w. Their finite-etale covering maps embed their groups in
R_w,N_w, hence in P by (1). L120's geometric identification (8),
followed by (7), gives exactly

    pi_1(T_w) intersect D_Y=D_Y,theta,
    pi_1(H_w) intersect D_A=D_A,theta.

Their cartesian double-cover square gives
pi_1(T_w)=pi_1(H_w) intersect R_w in P. They are geometrically
connected by L120, so their structure maps surject onto G_k, using
0BTX for T_w and the same atlas argument for H_w. Under (2)
this is precisely D_w. This uses their own actual place w and
pointwise models; it creates neither a global arithmetic model nor
models at other places. Their existence and local type come from
L120, not from the present group comparison.

### Boundary of the attempt

The stated tests pass on the unchanged integral witness. This is local
progress by REPRODUCTION of covered methods; no result beyond the
checked sources is claimed. The separate step497 audit below validates
these group assertions with their stated boundary.
Full (a)–(c)/initial data/III/P7, directed (*), exact generation/full
repair, factor-four excess, actual action/factorization/pilot,
authentication/def=, essentiality and original finite B>=A remain open.
Nothing here proves C_o-descent of U or B, global theta splitting,
full B[ell]-rationality or C_o q-order coprimality. There is no complete
flaw candidate.

### Separate critical audit — 2026-10-26, step497

**Scope and verdict.** Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-26-integral-witness-all-place-critical-audit.md`.
The claimed maps, images and group pullbacks pass this REPRODUCTION
audit. No hypothesis or conclusion requires narrowing, and no DAG edge
changes. This checks this integral tuple; L114's earlier verdict on a
different witness is not substituted. General theorems are imported
from the precise sources above, with the approved coverage reused.
No new general invariance or completion theorem is claimed.

**Witness and independent inputs.** L118's literal G_o contains iota,
so F=C_o and K also contain it. Here F denotes C_o, not the G_o
called F in L118. L119 fixes the full-coordinate K, U and full bad
support; L120 fixes the actual covers and reselected section s'.
Its connected product A times_(C_F) X_F=Y is an equality of the
actual covers. Its geometric construction (2) and model identification
(8), including the step493 audit, use geometric base change and atlas
sequences directly. They do not use L121's arithmetic injections.
Thus neither the witness nor a desired injection is hidden in a premise.

**Embedded limits and topology.** For either global field M and its
finite completion m, the embedded Fbar is precisely the subfield of
Omega consisting of elements algebraic over M. Indeed, it is algebraic
over M and algebraically closed, so contains all roots in Omega of
every M-polynomial. If E/m is finite, then E/Q_p is finite. Milne
7.62 gives N inside this actual E, with E=Q_p N; consequently N is
inside the same Fbar. A finite Galois L/M containing MN yields
E contained in mL. Each mL is finite Galois over m and is the
completion of L: the closure of L contains the closure m of M and
L, whereas the finite complete field mL is closed. This proves the
required embedded cofinality, not just existence of isomorphic fields.

Milne 8.10 identifies the actual finite stabilizer D_L with
Gal(mL/m). For L contained in L', restriction commutes with these
maps because continuous extensions agree on dense L. A compatible
family in D_L therefore acts on the union of the mL, which is all
Omega, and restricts to its given action on Fbar. Conversely an
m-automorphism of Omega preserves Fbar and the unique extended
valuation, and hence its place. These constructions are inverse and
prove (2) for the actual restriction map. The finite restriction kernels
give the induced topology on D_v, which is closed as the intersection
of the inverse images of all D_L. This verifies the absolute image
and topology; no finite-level stabilizer is mistaken for the absolute one.

In the compatible F,K diagram, hK is finite complete over h and
contains K; the closure k of K contains h and K. Thus k=hK.
An element of G_h fixes K if and only if it fixes k, giving exactly
(3) under the same restriction maps. No normality assumption is needed.
The density of Fbar in Omega_hat follows because its closure contains
Q_p and every N just used, hence every finite E and then Omega.
Algebraic closedness of Omega_hat is the separately imported Milne
Remark 7.41, not an inference from that density. The two fields remain
distinct, and Omega_hat/k is not asserted to be algebraic.

At infinity M contains Q+iota Q, dense in C. A place stabilizer
preserves absolute value and extends continuously to C, where it
fixes that dense subfield. It is the identity. Thus both complex
decomposition groups are 1, with no real-place exception left untreated.

**Geometric and stack comparisons.** The actual scheme atlases are
smooth geometrically connected punctured elliptic curves; their smooth
proper elliptic compactifications satisfy Landesman's Theorem 1.1.
Both fields in each extension Fbar->Omega->Omega_hat, or Fbar->C,
are algebraically closed of characteristic zero. This gives natural
full etale isomorphisms, also at places above 2 and ell. No assertion
about an integral special fiber is used. Zoonekynd 6.4 applies to the
connected atlases and constant inversion group without freeness.
Its natural exact sequences give stack isomorphisms preserving the
atlas, rather than coarse-space comparisons that lose stabilizers.

For arithmetic stack exactness, a kernel element in the geometric
middle group of the displayed atlas diagram has trivial inversion
image, so belongs to the geometric atlas group; 0BTX makes its image
injective. For an arithmetic middle element with trivial G_m-image,
choose a geometric middle element having the same inversion image.
Their quotient belongs to pi_1(W) with trivial G_m-image and hence
to pi_1(W_bar) by 0BTX. Surjectivity onto G_m already follows from
the geometrically connected atlas. This verifies every part of the
stack arithmetic row without applying a scheme theorem to a stack.

In the resulting local/global rows the geometric map is an isomorphism
and the field map is the verified decomposition inclusion. A kernel
element of the middle map is therefore geometric and zero. Given
any global element over D_v, lift its field image locally, and lift
the remaining geometric difference through the geometric isomorphism.
This proves the entire preimage (1). Compactness and Hausdorffness give
the induced topology. Compatible geometric points and cover lifts
make these statements simultaneous; no arithmetic splitting is used.

**Every group pullback.** In the one ambient P, L120's connected
atlas product gives R=N intersect J. Geometric connectedness over K
gives q(N)=q(R)=G_K, so D_A=N intersect D and D_Y=R intersect D.
For H=N or R one has, as actual closed subgroups,

    H intersect q^(-1)(D_u)
      = H intersect q^(-1)(D_u intersect G_K)
      = H intersect q^(-1)(D_w).

The completion result identifies these with the full N_w,R_w,
respectively. Also J_u=J intersect P_u and J_k=J intersect P_k.
These identities yield (5),(6), including P_k=P_0 intersect P_u
and J_k=J_0 intersect J_u, so both constant-field and local/global
cover group squares are pullbacks. For the first array the left,
right and outer pullbacks are respectively

    D_A intersect R_w=D_Y,
    N_w intersect J_k=R_w,
    D_A intersect J_k=D_Y.

The same equations hold with J_u on the right because D is contained
in P_k and P_u. All maps have the induced profinite topology, so these
set-theoretic intersections are also topological group pullbacks.
Finite covers give open inclusions in their local targets. Completion
images are only asserted closed in the global groups. For constant
fields the selected k is one factor of K tensor_F h; none of these
group statements identifies that factor with the entire scheme product.
In contrast, the atlas product really is all of Y_k, geometrically
connected by L120, so its intersection does not discard a component.

**Intrinsic theta transport and pointwise models.** L120 (2) uses
the quotient of the actual punctured curve group and its actual
rank-one covering subgroup. Natural geometric comparison preserves
the closed commutator/power kernels, hence the indicated quotient
maps q_A,q_Y and the embedding Q_Y in Q_A. It respects origin
inversion, its minus eigensubgroup and the characterized order-two
coset of EtTh Proposition 2.2(iii). Over the geometric field the
cusp section has domain 1. Changing the representative of that coset
inside M_theta does not change its generated subgroup L_theta.
Thus (7) identifies the intrinsic full preimages through the actual
maps; equality of finite orders alone is not the argument.

Since D_A,theta is contained in D_A and its intersection with D_Y
is D_Y,theta, the already checked first-array identities give

    D_A,theta intersect R_w=D_Y,theta,
    D_A,theta intersect J_k=D_Y,theta.

Together with N_w intersect J_k=R_w these are exactly the left,
outer and right pullbacks of the second array. Replace J_k by J_u
for its h-version. The same natural comparisons apply over Omega_hat
and C. A finite geometric cover over Omega descends, with its covering
map, to a finite subextension of Omega/k; its pullback over the
algebraic tower supplies the profinite-etale interpretation. This does
not assert that Spec(Omega_hat)->Spec(k) is profinite-etale.

At each actual w in s'(S), L120 (7),(8) independently supply the
geometrically connected finite-etale T_w,H_w and their connected
atlas product. Covering correspondence embeds their full groups in
R_w,N_w. Their geometric fibers give precisely the theta intersections
stated above, and their full atlas product gives
pi_1(T_w)=pi_1(H_w) intersect R_w. Geometric connectedness and the
scheme/stack exact rows give surjectivity onto G_k, identified with
D_w by (2). These are the models at their own reselected places;
no other-place or global arithmetic theta model has been inferred.

**Boundary.** This is critical validation of a covered specialization,
not a new result beyond the sources checked or a flaw in IUT. Full
initial data/(a)–(c)/III/P7, directed (*), generation/full repair,
factor-four excess, action/factorization/pilot, authentication/def=,
essentiality and finite B>=A remain unresolved. No U/B descent or
C_o q-order coprimality is proved by this audit. Mathlib remains
unchecked. The earlier attempt and its distinct audit are both retained.

## Mathlib

Full matching and supporting coverage is unchecked. No Lean search or
formal verification was performed; unknown coverage is not absence.
