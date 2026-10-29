# L120 — Simultaneous limited native assembly on the integral witness

## Hypotheses

Fix one member, one ordering o and its one prime ell>=7 from L118.
Keep the literal E_o: y^2=x(x-1)(x-t_o), G_o, C_o=G_o^nor and
the full-coordinate division field K=C_o(E_o[ell]). Write
M=E_o(K)[ell]. Fix L119's one line U in M and its full section
s:V(Q)->V(K). Let S={p:v_p(j(E_o))<0}. L119 supplies the full
bad support over C_o, with 3 in S and 2,ell outside S, and the
geometric toric alignment of U at every s(p), p in S.

Retain the source-version, Legendre-adjunction and F_mod=Q dictionary
qualifications of L118–L119. In particular the IUT I comparison is
with the May 2020, 186-page reproduction specified below, whose
identity with current author/journal bytes is unverified. No initial
theta-data or IUT III situation is assumed. Neither U nor its quotient
curve is assumed to descend to C_o; K/Q need not be Galois.

## Conclusion

On these unchanged objects construct the pointed isogenies

    alpha:E_o,K -> B=E_o,K/U,    psi:B -> E_o,K,
    psi alpha=[ell],            V=ker(psi)=alpha(M),
    X=E_o,K minus O, Y=B minus V, Z=[X/{±1}], A=[Y/{±1}].

The global cover/core and three cartesian-diagram predicates compared
in native Definition 3.1(d) hold for these objects. Fix any one
Q in V(K) minus zero. There is a full section s' obtained from s
only by U-stabilizer place reselection within its original C_o-fibers,
unchanged outside S, such that the following hold simultaneously:

- The designated set is all S, with selected set s'(S); the full
  C_o-fibers over it have multiplicative reduction.
- At each w=s'(p), p in S, the same Y->X and A have the local
  types of EtTh Definition 2.5(i). There are pointwise arithmetic
  theta covers T_w->Y_(K_w), H_w->A_(K_w) forming the cartesian
  double-cover square, whose geometric covers are the pullbacks of
  the geometric theta covers of these global objects.
- The single rational scheme cusp epsilon of A represented by
  {Q,-Q} is nonzero and has native label plus-or-minus one at every
  such w, through the actual marked graph comparison.

This is the limited assembly of L113 on the integral witness, with
full S in place of its earlier designated subset. This application
is validated by the separate step493 critical audit below. It proves neither all-place group
injections on the new tuple nor the directed-cover hypothesis (*),
and is not a complete (d)–(f) or initial-data verdict. No essential
IUT flaw or original finite B>=A bound follows.

## Proof

### Approved scope and precise imports

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-25-integral-witness-native-assembly.md`.
The intermediate target and passing threshold are exactly its TARGET:
the listed predicates must coexist on this fixed tuple over all S,
with no extra descent, field, splitness or excluded-prime premise.
The main gap remains finite B>=A. The downstream use is a tuple
combining integrality with these native prerequisites. ATTEMPTS/035–036
remain parked. This is REPRODUCTION, not a new general construction.

The general imports are the already assessed ones:

1. Mochizuki, [*The Absolute Anabelian Geometry of Canonical Curves*,
   2003 author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Canonical%20Liftings.pdf),
   Definitions 2.1,2.2,2.6(ii), Propositions 2.3(i,ii),2.7,
   author pp.8–11,14–15; Sijsling,
   [arXiv:1707.01158v2](https://arxiv.org/pdf/1707.01158v2),
   introduction/Lemma 1.1.1 and final Table 4, p.11.
2. Sutherland, [18.783 Lecture 5, 26 September 2023](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf),
   Theorems 5.8,5.11, pp.4–6, and 5.25, p.14; Milne,
   [*Elliptic Curves*, second edition, 2021](https://www.jmilne.org/math/Books/EC2.pdf),
   II.1.7, p.49, II.6.3, p.70. Finite-etale monodromy, henselian
   fibers and quotient-stack descent are Stacks
   [0BND](https://stacks.math.columbia.edu/tag/0BND),
   [03SF](https://stacks.math.columbia.edu/tag/03SF),
   [04GK](https://stacks.math.columbia.edu/tag/04GK),
   [04UV](https://stacks.math.columbia.edu/tag/04UV),
   [04ZP](https://stacks.math.columbia.edu/tag/04ZP),
   [04XD](https://stacks.math.columbia.edu/tag/04XD).
3. Kedlaya, [*The Tate curve*, fall 2004](https://kskedlaya.org/18.727/tate-curve.pdf),
   Theorems 1–2, pp.3–4, and torsion discussion p.5, citing
   Silverman, *Advanced Topics*, V.3.1/V.4/V.5.3; Sutherland,
   [18.786 Lecture 21, 6 May 2024](https://math.mit.edu/classes/18.786/2024/LectureNotes21.pdf),
   section 21.2, p.2, for nonexceptional pointed quadratic twists.
   The Tate same-field surjectivity is included; Proposition 3's
   transvection claim is not used here.
4. Conrad, [*Arithmetic moduli of generalized elliptic curves*,
   18 July 2006 author version](https://math.stanford.edu/~conrad/papers/kmpaper.pdf),
   Corollaries 2.2.3–2.2.4, section 2.5, equations (2.5.1)–(2.5.3),
   Example 2.5.1/Theorem 2.5.2, pp.8–9,17–18. Use L110's
   proved parameterized model/log/graph construction with its exact
   Kato, Hurwitz, Semi-graphs and Stacks citations, including
   [0A4Z](https://stacks.math.columbia.edu/tag/0A4Z),
   [039M](https://stacks.math.columbia.edu/tag/039M),
   [039H(2)](https://stacks.math.columbia.edu/tag/039H),
   [0A48](https://stacks.math.columbia.edu/tag/0A48) and
   [04DZ](https://stacks.math.columbia.edu/tag/04DZ).
5. Mochizuki, [*The Etale Theta Function*, PRIMS 45 (2009),
   227–349](https://ems.press/content/serial-article-files/41069?nt=1),
   graph/field conventions pp.237–244; Propositions 1.3,1.4(iii),
   pp.245–248; dotted diagram/Definitions 1.7,1.9/Theorem 1.10(iii),
   pp.253–256, retaining Remark 1.10.1(ii)'s correction;
   section 2 opening/Definition 2.1/Proposition 2.2(i)–(iii) and
   complete proof, pp.261–264; Definitions 2.3,2.5(i), pp.264–265;
   label discussion pp.267–269. The arithmetic cusp-torsor convention
   is Mochizuki, [*Galois Sections*, NMJ 179 (2005), author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Galois%20Sections.pdf),
   section 4/Definition 4.1(i–iii), author pp.14–15. Step491
   reinspected the EtTh section-2 hypothesis, proposition and full
   odd-level proof in the journal text; screenshot references yielded
   no viewable image and are not counted as visual verification.
6. Conrad, [*Transitive Group Actions*](https://kconrad.math.uconn.edu/blurbs/grouptheory/transitive.pdf),
   Theorem 4.21/equation (4.1), p.10. Actual completion transport
   is already proved for this tuple in L119, using Milne ANT v3.08,
   Theorem 7.38/Corollary 7.40 and Propositions 8.2,8.10.
7. Landesman, [arXiv:2005.09690v3, 20 January 2024](https://arxiv.org/html/2005.09690v3),
   Theorem 1.1, preceding characteristic-zero observation and smooth
   curve proof cases Lemmas 2.6,2.9/Proposition 2.10; Zoonekynd,
   [arXiv:math/0111071v1](https://arxiv.org/pdf/math/0111071v1),
   Corollary 6.4, pp.13–14, for the quotient-stack atlas sequence.

The compared native predicates are *IUT I*, May 2020,
[186-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf),
Definition 3.1(d)–(f), pp.62–63, under the inherited qualifications.
No authentication retry is made. The worked subarguments in
L106,L107,L109–L113 are reused below with their inputs substituted
explicitly. Their old-witness existence conclusions are never invoked.
These reused proof constructions are mathematical inputs, while L118
and L119 supply the actual witness. No L114 premise is used.

### Global construction on this tuple

Full torsion makes U a constant finite-etale subgroup over K. The
quotient theorem and complementary factorization give alpha,psi above.
They are separable isogenies in characteristic zero, of degrees ell
and ell: deg([ell])=ell^2. Thus both are finite-etale. The image
alpha(M) has ell points and lies in ker(psi), whose degree is ell;
finite etaleness gives equality of subgroup schemes. In particular
V=M/U is constant and the entire origin fiber is K-rational. No
full B[ell]-rationality is asserted.

The restriction Y->X is a degree-ell V-torsor with geometrically
connected source (an elliptic curve minus a finite set). Its geometric
monodromy therefore surjects onto V. Over the henselization of O in
E_o,K the isogeny is finite-etale with split residue algebra K^ell,
so 04GK makes it the split cover there. The whole cusp decomposition
group, including its G_K part, has trivial image in V. The actual
arithmetic monodromy factors through the elliptic quotient: it kills
the closed subgroup generated by geometric commutators and ell-th
powers. This is the same kernel obtained after the class-two and
power quotients in EtTh section 2, followed by abelianization. This
checks the arithmetic quotient, not only its geometric restriction.

Inversion is compatible with psi, and quotient-stack base change gives

    A times_Z X = Y.                                           (1)

Its atlas pullback is the actual finite-etale degree-ell cover Y->X;
descent makes A->Z representable finite-etale of that degree. Interior
stabilizers persist. Compactifications are (E_o,K,{O}) and (B,V),
with the marking logs, so EtTh Definition 2.1 applies once the core
is checked. These are the L107 constructions on the new U and K.

Here j is the rational invariant with v_3(j)=-30, by L118–L119.
The complete four exceptional invariants in Sijsling's final table are
2^14*31^3/5^3, 2^2*73^3/3^4, 1728, 0; their 3-orders are
0,-4,3,+infinity. Thus all are excluded on this member. The
scheme-cusp compactification in L106 applies to this literal Legendre
equation: retain the three order-two stack points over 0,1,t_o and
glue in the ordinary scheme neighborhood of infinity. It is proper
over P^1 by the finite quotient on the punctured open and the identity
on the cusp open. The degree-two map from E_o has ramification only
at O, of order two, giving log-dualizing degree 1/2 downstairs.
The atlas verifies geometric smoothness, normality, connectedness and
finite type. Thus every hypothesis of CanLift Definition 2.2 holds.

Over C the punctured elliptic curve is non-arithmetic by the table;
the actual degree-two atlas preserves arithmeticity through finite
index, as in CanLift Proposition 2.7. That proposition gives the
complex core. Proposition 2.3(ii), then (i), gives the K-core Z,
first over a separable closure and then over the actual number field.
The same composition/fiber-product argument as in L107 gives X and A
this core, without claiming that X or A itself is a core. For any
k=K_w, take an algebraic closure Omega containing a separable closure
of K. Proposition 2.3(i),(ii),(i) gives the core Z_k; all geometric
and scheme-cusp hypotheses just checked persist. No identification
of K with its completion is used.

For the global native diagrams put F=C_o,
X_F=E_o,F minus O and C_F=[X_F/{±1}]. Associativity in (1) gives
A times_(C_F) X_F=Y; the horizontal maps include the finite
separable extension K/F. In pi_1(C_F), choose compatible basepoints
and let J_0,R_0,S_0 be the open subgroups for X_F,Y,A. Then
R_0=S_0 intersect J_0 by this connected fiber product. If
D=ker(pi_1(C_F)->G_F), geometric connectedness over K makes
S_0 and R_0 have image G_K, and hence their geometric groups are
their intersections with D. The equality remains true after that
intersection. These prove the curve, arithmetic-group and geometric-
group cartesian diagrams, with actual open inclusions. They do not
assert any completion-group injection.

Over the fixed algebraic closure of K, apply EtTh Proposition 2.2 to
these same covers, origin O_B and odd ell. The arithmetic group is
trivial there. Denote the finite geometric quotients by Q_Y,Q_A,
their maps by q_Y,q_A, the minus eigensubgroup by M_theta, and the
subgroup generated by M_theta and the specified order-two coset by
L_theta. Define the full geometric theta subgroups as

    q_Y^(-1)(M_theta),       q_A^(-1)(L_theta).                  (2)

The proposition supplies L_theta intersect Q_Y=M_theta and the
required indices. Thus these are the geometric covers on the new
tuple; they have not been transferred from an old tuple.

### Actual split comparison, graph models and local fields

Fix an arbitrary p in S and initially put w=s(p), k=K_w. L119 gives
a finite p-adic k, p odd and p!=ell, |j|>1 and the toric equality
for U. Every geometric ell-torsion point remains k-rational because
the full field K was used. Tate uniformization supplies q in k,
0<|q|<1, and a pointed geometric comparison f:E_q->E_o,k. The
nonexceptional j gives a twisting character epsilon:G_k->{±1}.
Rationality of E_o[ell] implies gP=epsilon(g)P on E_q[ell]. Its
standard exponent quotient E_q[ell]->Z/ell sends the class of z,
z^ell=q^m, to m mod ell. It is onto and G_k-invariant since q
is fixed. Applying it to an exponent-one point forces epsilon(g)=1
mod ell. Oddness forces epsilon(g)=+1. Twist descent therefore gives
f over this unchanged k. L119's comparison-independent toric equality
now reads f(mu_ell)=i_w(U). This is the L109 subargument instantiated
with the new torsion and toric inputs; downstairs splitness is unused.

Let R=O_k and r=q. In L110's parameterized construction substitute
this complete noetherian DVR, this topologically nilpotent r, this
ell, this f and the isogenies just constructed. Conrad's models
C=T_1(r), D_r=T_ell(r) have generic fibers E_r,E_(r^ell), with
split one-gon and ell-gon special fibers. The formal rotation map
algebraizes to g:D_r->C, finite-etale of degree ell. Precisely the
conditions used in L110's algebraization/etaleness subargument hold:
proper source, separated finite-type target, compatible maps at every
nilpotent reduction, and equal residue fields at corresponding closed
points. The latter supplies the rank-one completed-ring isomorphism
in 039H(2)/039M; it is not inferred from etaleness alone. Properness
excludes a remaining non-etale generic locus. All ell origin markings
algebraize and form the entire split fiber.

The power isogeny a:E_r->E_(r^ell) has kernel the toric mu_ell.
Reduction on mu_ell is injective since p!=ell. Conrad's formal-group
identification h:(D_r)_k->E_(r^ell) has differential one, as does
rotation g; a has differential ell. Hence g_k h^(-1) a=[ell]:
their difference has zero differential and a nonzero characteristic-
zero elliptic homomorphism cannot have zero differential. Since
ker(h^(-1)af^(-1))=i_w(U), quotient uniqueness gives the actual
pointed comparison gamma:B_k->(D_r)_k with

    gamma alpha_k=h^(-1)af^(-1),       f g_k gamma=psi_k.        (3)

It identifies the full V-marking, not just a degree or an abstract
cyclic group.

The stable pointed one-gon, its boundary/marking log and its strict
pullback to D_r are exactly L110's construction. At a node write
r=u*pi^d with d>0. The chart
<x,y,c | x+y=d c>, with c mapping to pi, is fs in its own
groupification and has torsion-free relative groupification; its
chart ring is R[X,Y]/(XY-pi^d). At a marking the chart is N^2,
and elsewhere it is N. These meet the cited log-smooth criterion
for every positive d. In particular no coprimality of d with ell,
no q-order transfer from G_o to C_o and no extra ramification premise
is needed. The moduli pullback and strict completion preserve actual
overlap maps and all markings, as in the canonical L110 construction.

On the special fiber, each component maps isomorphically to the base
normalization, with its two ordered branches and origin marking.
The actual gluing is the cyclic chain of ell copies. L110's residue-
equalizer proof identifies it over the residue field with the native
infinite chain modulo ell Z, including branches and markings. All
components and markings are residue-rational, so there is no Frobenius
translation of the graph. Nilpotent invariance and proper henselian
full faithfulness lift this isomorphism and its deck maps before
puncturing. Combining it with (3) gives the arithmetic monodromy

    mu_w=c_w composed with (beta_hat_w mod ell),
    ker(mu_w)=beta_hat_w^(-1)(ell Z-hat),                       (4)

where c_w:Z/ell->V(k) is induced by the actual index-one deck map.
It is determined up to reversing orientation, not by an arbitrary
choice of generator. The full cusp decomposition image remains zero.
Every input of this L110 proof construction has now been matched;
none involved the older prime selector or its witness.

The literal Legendre curve has all four two-torsion points over k.
Same-field Tate surjectivity represents them by z in k^times/q^Z.
Only the two classes ±1 have even exponent in z^2=q^m, so an
odd-exponent class gives sqrt(q)=zq^(-(m-1)/2) in k. This verifies
the L111 field calculation on the new curve. Its original base
parameter is q, not q^ell from B. Thus EtTh's unindexed
double-dot k=k_2=k(sqrt(q),-1)=k. Independently iota in C_o embeds
in k and supplies sqrt(-1). This asserts no indexed radical equality.

### Theta-compatible splitting on these same local covers

The inputs to L112's local construction have now been reconstructed:
the actual local core, formal pointed log model, arithmetic graph
quotient (4), full 2-torsion, unindexed field equality, sqrt(-1),
odd p and ell. Apply that construction pointwise, as follows.

Use the domain copy E_o,k of [2], remove its full two-torsion, and
quotient by a nonzero rational two-torsion z different from the toric
point m. The remaining two cusps are exchanged by translation by m;
the affine involution [-1] composed with that translation has a free
orbit on them. This gives the source's dotted diagram and rational
scheme cusp. The two maps from a chosen common cusp to that cusp
and to O have local degree and residue degree one. Their complete
germ maps are t=a_1u(1+h(u)), a_1 in k^times, h in u k[[u]].
Thus their maps on the entire cusp inertia Z-hat(1) have exponent
one; normalized roots of 1+h exist compatibly at every integer level
in characteristic zero. The maps are over G_k and give the actual
affine isomorphisms of cusp splitting torsors. Any Kummer translation
from a_1 is retained. This is the proved L112 common-germ calculation,
whose hypotheses have just been checked on these objects.

Apply its covered EtTh normalization and sign construction: the
allowed unit orbit is O_k^times since double-dot k=k, its maximal
standard value is a unit, and the inverse unit normalizes it to one.
The identical dotted objects and identity comparison satisfy Theorem
1.10(iii)'s orbit hypothesis. The resulting nonempty sign reduction
is transported by the actual common-cusp maps, not replaced by an
arbitrary finite splitting. In the source quotient the cusp-inertia
kernel is ell Z-hat(1), over the same G_k. The two sign-related
sections reduce to the same finite class since -1=(-1)^ell in k.
Choose an actual member to obtain sigma_w:G_k->bar D_x. This uses
no surjectivity assertion about a map of splitting torsors. It
retains the primitive-twelfth-root correction in Remark 1.10.1(ii).

The splitting belongs to precisely the cover (3)–(4): its arithmetic
elliptic quotient, full cusp triviality and origin O_B were fixed
above. Hence Proposition 2.2(ii) applies with these inputs. Retain
these complete witnessed choices at each p for transport below;
there is no requirement that they form one global splitting.

### One global cusp by actual stabilizer transport

Let H={sigma in Gal(K/C_o):sigma U=U}. For sigma in H, quotient
uniqueness defines a semilinear map b_sigma on the fixed B, with

    b_sigma(alpha(P))=alpha(sigma P),
    psi b_sigma=sigma psi.                                    (5)

It preserves the origin and inversion and acts on V=M/U by the
quotient of its actual action on M. No action of the whole Galois
group on B is assumed. By L118 the image on M contains SL_2(F_ell).
In a basis (u,z) with U=<u>, the diagonal element (a,a^(-1))
stabilizes U and acts on M/U by a^(-1). Every nonzero quotient
scalar occurs. Thus H acts transitively on V(K) minus zero through
these actual semilinear maps.

L119 gives for w'=sigma w the isometric map
t:K_w->K_w', t(i_w(x))=i_w'(sigma x), fixing the underlying
C_o-completion, with t(q_w)=q_w' and T(w')=sigma T(w).
For sigma in H, this preserves toric alignment. Transport the whole
Conrad model, its log, markings, branch maps and (3) along t; on
the B source use b_sigma from (5). Uniqueness of the quotient
factor identifies the transported map with the reconstructed one
for this same psi at w'. Deck translation by v becomes translation
by b_sigma(v). The integral chain has its origin index fixed, so
its index map is n->n or n->-n according to orientation. The
proper henselian comparison that produced (4) preserves its deck
maps. Consequently, putting d_w=i_w^(-1)(c_w(1)), one obtains

    {d_(sigma w),-d_(sigma w)}
      ={b_sigma(d_w),-b_sigma(d_w)}.                           (6)

This is the L113 transport argument instantiated with actual new
models. It transports an integral marked graph, not just a mod-ell
kernel or a renamed finite generator. The complete dotted diagrams,
torsor maps and allowed theta normalizations transport along the
same field isomorphism. Their finite splitting therefore remains
compatible with the transported graph model. Roots, oddness and
core predicates persist under that isomorphism.

Fix Q in V(K) minus zero once. For each p in S choose sigma_p in H
with b_(sigma_p)(d_(s(p)))=Q and set s'(p)=sigma_p s(p). Leave
s'=s elsewhere. Each changed place has the same C_o-restriction;
distinct rational places have disjoint fibers. This is a full section
and (6) gives the required common native sign pair at every p in S.
Since ell is odd, Q!=-Q; its free rational inversion orbit gives the
scheme cusp epsilon of A. The origin O_B used for inversion remains
separate from this nonzero cusp. The full bad support is unchanged,
and L119's all-C_o-fiber reduction statement survives reselection.

### Arithmetic models and their full geometric preimages

At a reselected w retain the transported splitting sigma_w and cover.
Let P_Y subset P_A be the images of the full arithmetic groups in
EtTh's quotient, with finite geometric kernels D_Y subset D_A.
Proposition 2.2 gives |D_Y|=ell^2, [D_A:D_Y]=2, and its minus
eigensubgroup W of order ell, with P_Y/W=bar D_x. Put

    J=(P_Y->bar D_x)^(-1)(sigma_w(G_k)).

Then J intersect D_Y=W, J surjects onto G_k and [P_Y:J]=ell.
It is closed since the section image is compact, and open since
its finite coset space is Hausdorff. Apply part (iii) to this very
splitting, choosing an order-two representative tau of its specified
geometric coset. The source's odd-level proof, pp.263–264, makes
tau centralize P_Y/W and hence normalize J and W. Define

    J_A=J union J tau,         L_w=W union W tau.

These are subgroups, independent of the representative within tau W.
Since tau is geometric and outside P_Y,

    J_A intersect P_Y=J,      J_A intersect D_A=L_w,
    L_w intersect D_Y=W,     [J_A:J]=2, [P_A:J_A]=ell.          (7)

In the second equality, j tau^e is geometric exactly when j is
geometric, hence belongs to W. The pullbacks of J,J_A to the full
arithmetic groups define T_w,H_w. Both surject onto G_k, so their
geometric coset actions are transitive and their covers geometrically
connected. Equation (7) gives the cartesian double-cover square.
The previously checked field, graph and compatible-splitting premises
give all the stated local types by Definition 2.5(i).

It remains to identify models of (2), not merely covers of the same
degrees. Embed the fixed algebraic closure of K in Omega over K->k.
Landesman's cited characteristic-zero result applies to the smooth
connected curves X,Y, giving their natural geometric fundamental-group
isomorphisms. Their projective compactifications are the smooth
elliptic curves already constructed. Zoonekynd's atlas exact sequence,
with quotient {±1}, gives the corresponding isomorphisms for Z,A:
the left map is the curve isomorphism and the right map the identity
on {±1}. This preserves the actual stack atlases at fixed points.

The natural map on the original punctured curve preserves the closed
commutator and power subgroups defining the theta quotient; the
covering diagrams preserve the actual rank-one subgroup. Thus the
induced quotient maps identify D_Y,D_A with Q_Y,Q_A from (2).
They preserve O_B's inversion and identify W with M_theta. The
specified order-two coset is characterized by Proposition 2.2(iii),
so its image is the specified coset defining L_theta. If f_Y,f_A
are these natural isomorphisms on full geometric groups, (7) gives
the geometric covering subgroups of T_w,H_w as exactly

    (q_Y f_Y)^(-1)(M_theta),
    (q_A f_A)^(-1)(L_theta).                                 (8)

Here the arithmetic quotient kills only its stated geometric kernel;
its intersection calculations (7) are therefore taken before pulling
back to the full groups. Formula (8) proves the asserted model
identification by finite-etale correspondence, with compatible
basepoint conjugacy. It uses natural maps and full preimages, not
an order-only argument. The direct base-change imports avoid L114
entirely; no new-tuple arithmetic group injection is being assumed.

### Limited verdict and remaining gaps

Every p in S was arbitrary; only pointwise choices were required,
and the finite set of changes preserved each C_o-place, the global
cover, fixed U and fixed Q. The covered simultaneous test passes by
the reconstructed known methods. The old existential witness was
never substituted for this one. This is local progress validated by the separate audit below, not
progress beyond the sources compared.

Complete (a)–(c)/initial data/III/P7, directed (*), all-place group
injections on this tuple, exact generation/full repair, factor-four
excess, actual action/factorization/pilot, authentication/def=,
essentiality and original finite B>=A remain unresolved. In particular
no C_o-descent of U or B, global theta splitting, full B[ell]
rationality or q-order coprimality over C_o was used or proved.
There is no complete flaw candidate.

### Separate critical audit — 2026-10-26, step493

**Scope and evidence.** Executed the invocation-start SPECIALIZE target in
`drafts/literature/2026-10-25-integral-witness-native-assembly-critical-audit.md`.
Read this proof in full; checked the actual constructions in L106,L107,
L110,L112,L113, together with L118's statement and L119's statement and
completion covariance. Reused the approved component source assessments,
including the split-Tate and field arguments instantiated above. Reinspected
EtTh section 2 setup, Proposition 2.2 with its complete odd-level proof,
and Definition 2.5(i), printed pp.261–265, at the journal URL in import 5.
The direct geometric base-change imports in item 7 are reused, not replaced
by L114. ATTEMPTS/035–036 are contrasts, not mathematical premises.
This audit establishes applicability and compatibility of known methods;
it claims no new general result or progress beyond the checked sources.

**One tuple and the global predicates.** Fix the member and ordering before
fixing their L118 prime; then retain L119's K,U,s,S. The large image is on
the full module M over C_o, and the full division field is Galois over
C_o, irrespective of K/Q. In particular this supplies the actual
stabilizer automorphisms used below. L119's full support excludes 2 and
ell and includes 3; no further prime is deleted in this proof.

The quotient alpha has kernel U and degree ell; factorization of [ell]
gives psi of degree ell. The ell rational points alpha(M) exhaust its
finite-etale origin fiber. Therefore the whole henselian cusp action is
trivial, not just inertia. Geometric connectedness of B minus V supplies
surjectivity of the geometric rank-one monodromy. Its abelian exponent-ell
target kills the required geometric commutator/power generators
for factorization through the source's elliptic quotient. This does not
assert equality of its monodromy kernel with that defining kernel: the
rank-one quotient has a larger kernel. The source quotient itself kills
only its specified geometric kernel; full cusp triviality was checked
separately.

The inversion maps commute with psi. Thus the actual quotient-stack
fiber product in (1), including fixed points, is Y. The compactification
used for Z has a scheme cusp at infinity and retains the three interior
order-two stabilizers. L106's glued finite double map has log-degree
one upstairs and hence 1/2 downstairs. Its smoothness, properness and
scheme-cusp checks apply to the literal t_o!=0,1 here. The value
v_3(j)=-30 excludes each of the four classified exceptions. The two core
transfers are first across algebraically closed fields and then down to
the number field; completion coricity uses an algebraic closure containing
that fixed closure, not an identification of the fields. The finite-cover
category argument then applies to X and A without making either a core.

For the global diagrams, geometric connectedness over K gives the images
G_K of R_0,S_0 in G_(C_o). The connected stack fiber product gives
R_0=S_0 intersect J_0 inside the single ambient fundamental group.
Intersecting with its geometric kernel yields the geometric square.
These are actual open subgroup inclusions and compatible basepoints;
no unrelated conjugacies or descent of B to C_o enter.

**The local construction and splitting.** At any initial s(p), p in S,
the completion is finite p-adic, p!=2,ell, and full E_o[ell] is rational.
For the geometric Tate comparison the twist character acts by a scalar
on this module. The invariant exponent quotient has an exponent-one
point, forcing that scalar to be one for odd ell. Thus the split
comparison exists over the unchanged completion before any model is
constructed. Toric alignment identifies its mu_ell with U as a subgroup
scheme, so quotient uniqueness gives precisely (3).

Every parameter in L110's worked construction is available: complete
DVR, positive q-order, split comparison, p!=ell, and the actual isogeny
with the specified kernel. Its rotation algebraization uses equal residue
fields at corresponding closed points; its log chart is saturated in
its own groupification for every positive q-order. Neither check demands
coprimality of that order with ell. The full origin fiber and ordered
branches match the cyclic chain over the residue field. Proper henselian
full faithfulness is applied before puncturing and carries deck maps and
markings, proving (4) as arithmetic monodromy, not just a geometric kernel.

Full rational 2-torsion of the literal Legendre curve and same-field Tate
surjectivity give sqrt(q) in k by an odd-exponent representative. The
parameter is that of E_o, not B. The separate iota in C_o supplies
sqrt(-1). These are exactly the unindexed field premises used by L112.
In its dotted construction the two chosen cusp maps have local and
residue degree one. Their actual germ isomorphisms give inertia exponent
one and retain the leading-coefficient Kummer translations. Hence the
transported sign reduction is a reduction of the correct cusp torsor.
The allowed theta normalization and identity comparison have the field,
odd-residue-characteristic and orbit hypotheses stated in import 5;
the recorded twelfth-root correction remains in force. Pushing an actual
member of that reduction to the finite quotient gives the splitting.
Oddness identifies the two finite classes but is not an assertion that
an arbitrary finite splitting lifts compatibly. All these choices belong
to (3)–(4), and are kept together.

**Simultaneous reselection.** For sigma stabilizing U, conjugate alpha
and use quotient uniqueness. This produces the semilinear b_sigma and
both identities (5); on V it is the actual quotient action on M/U.
In a basis adapted to U, the available SL_2 diagonal matrices realize
every nonzero scalar on M/U, proving the required transitivity.

L119's completion isometry fixes the underlying C_o-completion and
carries the small Tate parameter to the small Tate parameter. Transport
of the full model, including its origin, branches, all V-markings and
quotient comparison, carries translation by v to translation by
b_sigma(v). The origin rules out an index offset; the ordered branches
permit only the two integral orientations. Full faithfulness retains
these maps on the generic cover. This verifies (6), rather than choosing
an arbitrary generator of its cyclic deck group. The dotted diagrams,
normalization and splitting transport by the same isometry.

For each rational p select just one sigma_p sending its initial d to the
fixed Q, and retain the transported witnesses at sigma_p s(p). Distinct
p have disjoint place fibers, so these choices impose no contradictory
local prescriptions. No coherent action on all auxiliary choices and no
global theta splitting are needed. Every changed place retains its
original C_o-restriction, U remains toric, and the section elsewhere is
unchanged. Since ell is odd, the pair {Q,-Q} is free under inversion and
defines the asserted rational scheme cusp, separate from O_B.

**Arithmetic intersections and full geometric preimages.** Use precisely
the transported splitting in defining J. The isomorphism
P_Y/W=bar D_x shows that a geometric element lies in J exactly when
it lies in W, since a section image intersects the finite inertia kernel
trivially. It also gives surjectivity J->G_k and index ell. Compactness
makes J closed, and finite index then makes it open. The odd-level
inversion assertion in import 5 provides the specified geometric coset;
its order-two representative centralizes P_Y/W and normalizes J. Thus
J_A=J union J tau is a subgroup. Its intersection with P_Y is J.
The image of j tau^e in G_k is the image of j, so its geometric
intersection is exactly W union W tau. This verifies all of (7), including
the actual subgroups and the cartesian double-cover square. Surjectivity
to G_k gives geometric connectedness of the resulting covers.

For (8), choose a common algebraically closed overfield Omega of k and
the embedded fixed algebraic closure of K. The smooth connected curves
X,Y and their smooth projective elliptic compactifications satisfy the
characteristic-zero base-change theorem of import 7. The natural maps
are geometric group isomorphisms. Comparing the quotient-stack atlas
exact sequences then gives the same conclusion for Z,A, with identity
on the quotient {±1}; this retains stabilizers.

More explicitly, the theta quotient of the original geometric group
kills the closed class-two and power kernel. The natural isomorphism
preserves those subgroups. Restriction to the actual rank-one covering
subgroup commutes with this quotient and preserves its kernel. The
arithmetic quotient uses this geometric kernel alone; its geometric
image therefore identifies with the intrinsic quotient over Omega.
This verifies D_Y=Q_Y and D_A=Q_A via the indicated maps, rather than
by their orders. Inversion at O_B is preserved, hence so is its minus
eigensubgroup. The characterization of the specified order-two coset
preserves its image modulo that eigensubgroup. Pulling back the two
intersections in (7) now gives exactly the full subgroups in (8).
Finite-etale correspondence, with the same basepoints, proves the
geometric-model assertion. No all-place arithmetic injection or L114
conclusion was used.

**Verdict.** The stated limited simultaneous assembly passes this separate
REPRODUCTION audit on the unchanged integral witness over all S. No
hypothesis or conclusion needed narrowing, and no DAG edge changes.
The source-version qualifications remain. Full initial data, directed
(*), all-place injections on this tuple and original finite B>=A are
not consequences of this audit; all other exclusions above persist.
There is no complete flaw candidate. Mathlib coverage remains unchecked.

## Mathlib

Full matching and supporting Mathlib coverage for this changed-tuple
assembly is unchecked. No absence claim or Lean verification is made.
This is an informal specialization of the cited results and the
explicitly reinstantiated canonical proof constructions.
