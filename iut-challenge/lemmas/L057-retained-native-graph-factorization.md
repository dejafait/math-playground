# L057 — Retained native graph factorization over unchanged N

## Hypotheses

Retain L056's hypotheses and objects, including L053's actual global
E_0/Q, F=Q(zeta_60,E_0[30]), K_glob=F(E_0[7]), Omega,u,w,
H=F_u subset N=(K_glob)_w, M>=max(M_tors,31), subgroup U,
alpha:E -> B=E/U, psi:B -> E and V=ker(psi). Use the fixed
pointed Tate isomorphism and the changed q_0 in Q_3 with
v_3(q_0)=30 and v_3(3)=1. Neither K_glob=N nor q_0=3^30
is assumed. Base change the retained maps to N.

Put R=O_N, k=R/(pi), and C=C_R with section S, precisely L055's
stable log cubic over the closed-point log base. Its formal completion
is hat C^log. Let f:D -> C, gamma:B_N -> D_N and the seven sections
be exactly L056's finite-etale extension, with f_N gamma=psi_N.
The source log is f^*M_C. No native graph factorization, native cusp
label, compatible theta splitting or full initial datum is a premise.

Let X_N=E_0,N minus S and let Pi_X be its arithmetic etale fundamental
group, with the log/tempered notation of EtTh section 1. Write

beta:Pi_X^tp -> Z,  beta_hat:Pi_X -> Z-hat

for that section's native graph quotient and its profinite completion.
The sign of beta is unspecified. Let mu:Pi_X -> V be the arithmetic
monodromy of L053's retained cover Y_N=(B_N minus V_N) -> X_N,
with the deck group identified by translations on B_N.

## Conclusion

The finite cover associated to beta^(-1)(7Z) is isomorphic over N
to the retained Y_N -> X_N. Its formal extension, including the
pullback log and all marking sections, is L056's hat D^log -> hat C^log.
Equivalently, there is an isomorphism of finite groups
c:Z/7Z -> V such that

mu = c composed with (mod 7) composed with beta_hat.

Thus ker(mu)=beta_hat^(-1)(7 Z-hat), including the arithmetic action,
not merely the restriction to the geometric fundamental group.
The isomorphism c is induced by the cover comparison; this statement
does not prescribe c(1)=Q or c(1)=-Q.

This is a known-method specialization. The separate 2026-10-14 critical
audit validates it with the finite-module descent and deck-action
justifications below made explicit. It closes only the graph-factorization clause of EtTh Definition
2.5(i) for this retained rank-one quotient. It does not establish the
independent compatible-splitting clause, a native label of Q, a full
native type or selected/theta datum, or the original finite B>=A.
It is not a candidate demonstration of an essential IUT flaw.

## Proof

### Approved target and standard inputs

Use the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-14-retained-native-graph-factorization-application.md`.
The main gap remains original finite B>=A and actual input/action/pilot/
essentiality. This test can supply one native cover prerequisite while
leaving the independent label and splitting obligations unresolved.

[Mochizuki, The Etale Theta Function and Its Frobenioid-Theoretic
Manifestations, PRIMS 45 (2009), 227–349](https://ems.press/content/serial-article-files/41069?nt=1),
section 1, pp.237–239, constructs beta from the universal graph cover
of a split singular type-(1,1) stable log curve over a finite p-adic
field. Its formal cover has chain special fiber. Definition 2.5(i),
p.265, requires graph factorization and a further compatible splitting.

[Mochizuki, Semi-graphs of Anabelioids, PRIMS 42 (2006),
221–322](https://ems.press/content/serial-article-files/40941?nt=1),
Definition 2.2(ii), p.246, and Remark 3.5.1, pp.261–262,
give the locally trivial constituent-isomorphism criterion and graph-cover
correspondence. Examples 3.10 and 5.6, pp.268–270,295–296, describe
the geometric special-fiber maps and their compatible arithmetic actions.
These are imported constructions, not a theorem that arbitrary equal-degree
geometric covers agree arithmetically.

[Stacks, Lemma 58.9.1, tag 0A48](https://stacks.math.columbia.edu/tag/0A48)
identifies finite-etale covers of a proper scheme over a henselian local
ring with those of its closed fiber, fully faithfully and essentially
surjectively. [Theorem 59.45.2, tag 04DZ](https://stacks.math.columbia.edu/tag/04DZ)
gives etale-site equivalence under a universal homeomorphism; here it
applies to nilpotent reduction immersions. The complete-noetherian case
of 0A48 and its lifting/full-faithfulness proof suffice for R.

The source statements and pertinent cases were inspected in step 199
and reinspected for this application on 2026-10-14. Journal locators
are used; retain the recorded author/journal clause-matching qualification
and the IUT I odd-level correction. No author/journal byte identity or
deleted author Remark 2.2.1 is used. L055 supplies the actual native
formal object over N. No general Tate, tempered, log or algebraization
theorem is reproved. The explicit nodal-gluing check below is necessary
to apply these known comparisons to actual covers rather than graph counts.

### Actual special fiber, constituent maps and descent

Write nu:C_k^nu -> C_k for normalization. L055 and L056 identify
C_k^nu with P^1_k, its two distinct k-rational node branches with
a,b, and the lifted infinity marking with a third k-point s.
Choose an order (a,b). L056's special fiber D_k has seven
k-defined P^1 components and seven split k-rational nodes, with one
of its seven smooth k-markings on each component. The map on each
normalization component is an isomorphism to C_k^nu: it is the
rotation construction's identity component map transported through
the actual target isomorphism h. This statement is over k, including
its structural map to C_k, not only after extending k.

Start with the component containing the reduction of gamma(0_B),
and number successive components i modulo 7 using the ordered node
branches. Under their normalization maps, denote their branch points
by a_i,b_i and their marking by s_i. The node identifications are
exactly b_i with a_(i+1), including b_6 with a_0. L056 checks that
one branch of each target type occurs at every vertex, so this indexing
never folds the loop or interchanges a single node's branch types.
Each normalization map carries (a_i,b_i,s_i) to (a,b,s).
In particular it preserves the actual marking map, not just an
unmarked rational component. The ordered triple also fixes the
normalization isomorphism uniquely.

Now use the native chain cover from EtTh section 1. Its special fiber
has copies of the same normalization C_k^nu indexed by j in Z,
with b_j glued to a_(j+1), and the lift of s on each copy. This is
the locally trivial universal graph lift: the component and branch
objects are copied with their structural maps, not replaced by unrelated
anabelioids. Quotient its graph by translation by 7. The resulting
special-fiber cover G_0 -> C_k has seven copies of C_k^nu and precisely
the gluing b_i=a_(i+1) above. All copies and all maps are over k.
For the geometric semi-graph with compact structure, the constituent
maps are consequently isomorphisms: the punctured normalization maps
are isomorphisms, the two node-branch inertia objects retain their
individual identifications, and the marking legs retain their simple
parameters. Definition 2.2(ii) and Remark 3.5.1 apply to this locally
trivial finite graph lift. No component is contracted into a node;
no node is mapped to a smooth point, the alternative cases in Example 3.10.

This comparison is an isomorphism of the special-fiber SCHEMES over
C_k. Here is the precise normalization/conductor check, using the
standard split-node results rather than assuming a graph determines
a scheme. For Z equal to C_k, D_k or G_0 and a split node z of Z,
put A=O_(Z,z) and let
A'=(nu_*O_(Z^nu))_z be its finite semilocal normalization. The reduced
one-dimensional local ring A is essentially of finite type over k,
hence Noetherian and Nagata. Its two normalization points have residue
field k. [Stacks, Lemma 53.19.11, tag 0CBW](https://stacks.math.columbia.edu/tag/0CBW),
items (1)–(3), gives A_hat=k[[x,y]]/(xy). The split case of
[Lemma 53.19.4, tag 0C4A](https://stacks.math.columbia.edu/tag/0C4A)
describes its normalization. By
[Lemma 33.39.5, tag 0C3V](https://stacks.math.columbia.edu/tag/0C3V),
applied to this reduced Nagata ring of dimension one,

A' tensor_A A_hat = k[[x]] times k[[y]].

The product is a statement AFTER completion. In particular A' for the
integral target need not be a product of uncompleted branch local rings.
The two actual residue maps define the A-linear map
delta:A' -> k, delta(t)=t(a)-t(b), with A contained in ker(delta).
Its completed map is (f,g) -> f(0)-g(0), whose kernel is precisely
the image of k[[x,y]]/(xy) in k[[x]] times k[[y]]. By
[Lemma 10.97.1, tag 00MA](https://stacks.math.columbia.edu/tag/00MA),
completion is exact on these finite A-modules and equals tensoring
with A_hat. Thus (ker(delta)/A) tensor_A A_hat=0. Faithful flatness of
maximal-ideal completion, [Lemma 10.97.3, tag 00MC](https://stacks.math.columbia.edu/tag/00MC),
gives ker(delta)=A. No algebraic closure of k is used.

Away from nodes normalization is an isomorphism. The preceding local
equalities therefore identify the structure sheaf with the subsheaf
of normalization functions having equal residues at each specified
node pair. A finite surjective normalization is closed, so the topology
is the quotient by precisely these pairs. Matching the normalization
maps and the pairs identifies both topology and this subsheaf, giving
a_0:D_k -> G_0. It is over C_k: each component identification commutes
with its actual normalization map to C_k, and the equalizer description
retains those pullbacks. All residue maps are k-linear, and the matching
of s_i retains the marking maps. Completed node rings are used only
to verify this equalizer; the integral target's uncompleted local ring
is not replaced by k[x,y]/(xy). These cited general theorems are imported;
the check applies them to this cover's particular node pairs and maps.

Every part of a_0 is defined over k. In particular residue Frobenius
fixes all seven components, their individual branches and markings.
An arithmetic twist translating the seven indices nontrivially would
permute components and markings, and would not have these k-defined
normalization maps. The comparison excludes that twist before invoking
a geometric tempered comparison. Starting at the component above 0_B
merely fixes a lift of a marking; it supplies no theta-compatible
splitting or label for Q. Reversing (a,b) reverses the chain orientation
and leaves the subgroup 7Z unchanged.

### Strict reductions, algebraization and the retained generic map

L055 checks all hypotheses of EtTh section 1 on precisely hat C^log:
finite p-adic N, prescribed closed-point formal log base, stable type
(1,1), split singular special fiber, and smooth algebraized generic log
fiber. Hence the native infinite formal graph cover is defined on this
object. The finite quotient associated to beta^(-1)(7Z) is locally
the seven-sheet quotient of that cover. It is an ordinary finite-etale
formal cover with special fiber G_0: on etale neighborhoods of a smooth
point or a split node, graph lifting just copies the same ordinary
neighborhood with its branch incidence, seven times. Its log is the
pullback of the fixed target log, so the map is strict. It is a graph
cover, not a ramified power map at a node or a marking.

Let C_a=C times_R R/(pi^a), for a>=1. Their reductions to C_k are
nilpotent closed immersions, hence universal homeomorphisms. By 04DZ
the finite-etale cover and the comparison a_0 lift uniquely, up to the
unique isomorphism extending a_0, to every C_a. Full faithfulness
also makes these isomorphisms commute with reduction a+1 to a:
the two prospective composites reduce to the same a_0. Consequently
L056's D_a -> C_a and the native finite formal cover agree on all
reductions, and therefore agree as adic formal schemes over hat C.

For the algebraic comparison apply 0A48 to C/R. R is a complete
noetherian DVR, hence henselian; C is the retained proper scheme.
It supplies a finite-etale algebraic G -> C lifting G_0 and a unique
isomorphism a:D -> G lifting a_0. Its completion is the preceding
native formal cover, by the same nilpotent full faithfulness.
Thus this is an algebraization of the finite native quotient over
unchanged R, not an existence assertion for an arbitrary ramified
log-etale cover. L056's identity f_N gamma=psi_N now identifies the
generic algebraic map with precisely the retained psi_N. Proper
comparison is used before deleting the marking; properness is not
claimed for X_N.

The comparison respects the entire fixed log. Both source logs are
pullbacks of M_C, so any cover isomorphism over C induces their unique
pullback-log isomorphism. At every node the chart is L055's same
P_n with x+y=n c and n=ord_R(q_0); its relation is not multiplied
by seven. Each marking has its same simple pulled-back parameter.
L055/L056's associated-log sheaf construction therefore gives these
isomorphisms on strict reductions and on completion, including units
and overlap cocycles. No exchange of monoid association with a limit
is used. Inverse images of S agree as schemes, so their seven sections
and generic punctures agree. More precisely, these inverse images
are finite-etale over S=Spec R. Apply 0A48 also to S over R:
a selected k-point in the special fiber is a map from the trivial
cover Spec k and lifts uniquely to a section Spec R. Thus the
chosen special marking lift determines its entire section, not merely
a point on a formally isomorphic neighborhood.

### Arithmetic monodromy and scope of the conclusion

In the native construction the subgroup beta^(-1)(7Z) is normal;
its finite quotient has deck group Z/7Z. The finite quotient of the
native formal cover, its algebraization just compared, and its generic
trivial-log locus represent that same finite tempered cover. EtTh's
profinite-completion convention Pi_X=(Pi_X^tp)^wedge identifies its
finite monodromy with (mod 7) beta_hat. This applies to the arithmetic
group over N, because every comparison above is over R or N and
the residue descent was checked over k.

Restrict a_N gamma to the complements of the seven markings. It gives
an N-isomorphism of L053's retained Y_N -> X_N with this native
finite cover. Transporting a native deck translation across this
isomorphism is an automorphism of the retained cover. L053's cover
is connected, Galois, and has the constant seven-element deck group
V given by translations on B_N. Thus transport gives an isomorphism
c:Z/7Z -> V. Explicitly, translation by one index on G_0 is a
k-defined deck map over C_k. Full faithfulness in 0A48 lifts it
uniquely to G, and then transports it to D through a; its powers
and seventh-power identity lift as well. Their formal restrictions
are the native finite-cover translations by 04DZ. On the generic
fiber, conjugation by gamma gives exactly an element of L053's
translation group V. The seven powers send the section above 0_B
to the seven different marking sections, as can be checked on their
reductions and then by uniqueness of section lifting. L056 identifies
their generic points with the seven distinct elements of V_N, so
the generic deck maps are also distinct. This realizes c through
maps of the actual covers, excluding an arbitrary abstract
identification. Fiberwise equivariance gives
mu=c (mod 7) beta_hat. A change of fiber lift only conjugates
monodromy, and both groups are abelian, so the equality is unaffected.
In particular the arithmetic kernels agree. The isomorphism also
preserves the original-cusp trivial decomposition image already proved
in L053; no arbitrary identification of two abstract deck groups was
used to force the equality.

This meets the approved test: component maps, node gluing, marking
legs, residue descent, all strict reductions and the exact generic psi
match. It proves the graph-factorization clause for the retained
elliptic quotient, which already comes from the compactified isogeny.
It does not compute which source rotation corresponds to Q: no claim
c(1)=plus-or-minus Q follows from the cover comparison alone. EtTh
Definition 2.5(i)'s compatible-splitting requirement remains independent.
Even with L054's retained field equality and odd l=7,p=3, no full
native type, complete selected/theta data, actual input/action/pilot/
essentiality or numerical comparison is asserted. Preserve ATTEMPTS/027,
030 and the historical point-group/source stop. This argument uses the
audited actual model unavailable to the historical point-group route.

### Separate critical audit — 2026-10-14

The pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-14-retained-native-graph-factorization-critical-audit.md`
covers this audit. Verdict: the limited factorization passes after
making the finite-module conductor descent and arithmetic deck-map
transport explicit above. No new lemma input or different field,
curve, marking, log structure or generic isogeny is introduced.

The k-defined component isomorphisms and both branch maps come from
L056's actual rotation quotient, transported through its target h.
The ordered triples remove a possible component-coordinate ambiguity;
the semilocal equalizer verifies gluing over k, including the structural
maps and all markings. Thus the special-cover comparison carries
residue descent, not just geometric incidence. The source's native
infinite graph lift is ordinary etale and copies these neighborhoods;
modulo 7Z it has exactly seven sheets and pullback log. This is the
finite ordinary etale case of the cited comparisons, with no node
ramification or power map smuggled into it.

For every a, C_1 -> C_a is nilpotent; 04DZ supplies the comparison
and forces reduction compatibility by faithfulness. The same pullback
log universal property from L055/L056 identifies the full associated
logs and their cocycles, not only their characteristic monoids.
Properness of C over the complete DVR permits 0A48 before puncturing.
The generic comparison uses the established equality f_N gamma=psi_N;
it cannot follow merely from degree seven or from matching point groups.
Deck-map transport and the arithmetic finite-cover correspondence then
give the displayed equality of monodromy maps up to c, hence equal
arithmetic kernels. Changes of fiber basepoint only conjugate the
abelian deck action. The original cusp decomposition remains trivial.

This validates one native-cover prerequisite by known methods. It
does not fix c(1) relative to Q or select a theta-compatible splitting.
The journal/author clause-matching and odd-level qualifications remain;
neither a full native type nor the original finite B>=A is proved.
No new discovery beyond the checked literature is asserted.

## Mathlib

Full matching Mathlib coverage of the arithmetic tempered graph quotient,
its retained formal/algebraic comparison and this specialization has not
been checked. No absence claim is made. The graph and henselian inputs
are imported by precise citations above; this is REPRODUCTION by known
methods, with no claim of progress beyond the inspected literature.
No mathematical script, numerical evidence or candidate IUT flaw is
used. The separate audit validates only the limited application stated here.
