# L118 — An integral selected prime with large image on the same member

## Hypotheses

Retain L089's entire fixed congruence family, algebraic closure and
bounding domains, and L117's fixed lattice and good-pair conditions.
Fix d=6, epsilon_d=1, delta=3317760 and the source constant xi>=5.
Let Exc_0 be any fixed finite subset of U(Q-bar), where
U=P^1 minus {0,1,infinity}. All these data precede member selection.
For each ordering o of a good member's cubic roots use exactly
L090's embedded fields and literal equation

    t_o=(r_(j_3)-r_(j_1))/(r_(j_2)-r_(j_1)),
    E_o: V^2=X(X-1)(X-t_o),
    T=Q(t_o)=Q(E[2]), F=G_o=T(iota,E_o[15]),
    iota^2=-1, C=C_o=G_o^nor over Q.

Every division field includes both coordinates of all full torsion
points. Retain L101/L105/L117's qualified April 2020 IUT IV
reproduction and explicit Legendre-adjunction interpretation. Neither
initial theta-data nor a native III situation is assumed over F or C.

## Conclusion

There is one good member with all six t_o outside Exc_0 such that,
for any one of its orderings, there is a prime ell>=7 satisfying,
for that same E_o,F,C and actual downstairs normalized height H,

    sqrt(H)<ell<=10 delta sqrt(H) log(2 delta H),       (P1+)
    ell divides no nonzero integer height h_v over F, (P2)
    h_v<sqrt(H) at every F-place over ell,             (P3)
    v_ell(j(E_o))>=0,
    E_o has no F-defined ell-cyclic subgroup scheme,  (P4)
    SL_2(F_ell) subset rho_(E_o,ell)(G_F),
    SL_2(F_ell) subset rho_(E_o,ell)(G_C).

Both representations act on the entire geometric E_o[ell]. In one
common basis the C-image is normal in the F-image and its index
divides four. The member is chosen once; the ordering and its prime
may be chosen afterwards. No prime common to six orderings is claimed.

This is a same-witness application of known methods, validated by the
separate step484 critical audit below. It does not identify two previously selected
existential witnesses. It gives no effective coefficient threshold,
full GL_2 image, full native P5/P7, complete initial-data repair,
essential IUT flaw or original finite B>=A comparison.

## Proof

### Approved scope and imported inputs

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-25-integral-selected-prime-large-image-combination.md`.
L105's step423 audit validates its fixed-exception and component
method; L117's step480 audit validates its actual-family budget.
Their separate existential conclusions do not imply this conclusion.
We instead insert the fixed exception into one L117 construction and
check the component method at its prime. L104's step418 audit supplies
the restriction argument after its actual hypotheses are matched.

The imported mathematical results, with their retained versions, are:

- Mochizuki, *IUT IV*, April 2020,
  [87-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
  Corollary 2.2(ii), setup pp.41–42 and proof P4/P6 pp.45–46.
  Under the fixed-domain, level-structure and P2 hypotheses checked
  in L105, an F-defined ell-cyclic subgroup gives
  ((ell-2)/24)H<=2 log(ell)+T_K, with T_K fixed before the member.
  Only this component implication preceding P7 is imported.
- Mochizuki, [*Arithmetic Elliptic Curves in General Position*](https://www.kurims.kyoto-u.ac.jp/~motizuki/Arithmetic%20Elliptic%20Curves%20in%20General%20Position.pdf),
  February 2009 author version, Proposition 3.4/Lemma 3.5, p.17,
  for that height input; Lemma 3.1(iii), p.14, for SL_2 containment
  from a transvection and an element not upper triangular in the
  same basis over the prime field. Retain the
  [July 2016 comments](https://www.kurims.kyoto-u.ac.jp/~motizuki/Arithmetic%20Elliptic%20Curves%20in%20General%20Position%20(comments).pdf),
  (8),(13)–(16), pp.1–2, and L105's domain qualifications.
- Dupuy–Hilado, [arXiv:2004.13228v1](https://arxiv.org/pdf/2004.13228v1),
  Lemma 5.4.1 and its split/nonsplit proof, pp.27–28, as applied
  in L105: over a finite p-adic field, negative integer j-order
  prime to an odd ell different from p gives a nonidentity
  transvection in the full torsion inertia image.
- The fixed finite Exc_4 is already proved finite in L105 using
  Silverman, [AWS notes, 13 February 2024](https://swc-math.github.io/aws/2024/2024SilvermanNotes.pdf),
  Theorem 4.8(d), p.15 (Northcott), and the degree-six Legendre map.
  Its finiteness is used here without another proof.

L104 contains the precise Milne v5.10 and Conrad Theorem 3.3
citations for restriction and elementary generation. Those general
theorems, the local inertia theorem and the height theorem are not
reproved. L117 supplies its first-moment specialization; none of its
estimates needs changing for a different fixed finite exception.

### Fix the exception before the single construction

Fix L105's source constant T_K>0 using the unchanged domains and
d=6, epsilon_d=1. Use its already established quantities

    B_4=48+8T_K,
    Exc_4={t in U(Q-bar): [Q(t):Q]<=6,
                           h_abs(J(t))<=B_4+log 2000}.

L105 proves that Exc_4 is finite independently of member and prime,
and that the displayed cyclic-subgroup implication, for ell>=5,
forces H<=B_4. These facts precede its existential application of
L101; they are not restricted to its eventual witness.

Apply L117 with Exc=Exc_0 union Exc_4, fixed before R. Its theorem
gives good pairs for all sufficiently large R; choose one and keep
it for the rest of the proof. Every one of its six parameters avoids
Exc, lies in L089's fixed domains at the required embeddings, and
has degree at most six. Now fix any one ordering and the literal
E_o,T,F,C above. No field is replaced when the height is defined.

L101's unconditional height calculation applies to this good member
before prime selection: E_o is semistable at all finite F-places and

    h_v=e(F_v/Q_p) max(0,-v_p(j)),
    H=sum_p max(0,-v_p(j)) log p,
    h_abs(j)=H+log max(1,|j|)<H+log 2000,

where j=j(E_o)=j(E) is rational and 0<j<1728. These formulas use
all actual F-places with residue weights, without F/Q normality.
If H<=B_4, the last inequality and degree bound would put t_o in
Exc_4. Therefore this selected member has H>B_4.

L117 supplies its actual interval-pole budget T<=M(H) and
sqrt(H)>xi for this member/order. Apply L116 to that budget once.
It gives one prime ell>=7 with P1+, P2, P3 and v_ell(j)>=0.
Retain exactly this prime. We do not apply the existential conclusion
of L105 or choose a prime by its earlier selection procedure.

### Check P4 and the full downstairs image at that prime

The hypotheses of L105's component implication remain present:
the fixed domains and d,epsilon_d are unchanged, t_o is in U,
the literal equation is over T with full two-torsion, and F contains
iota and the full 15-torsion. Thus it also contains the full
30-torsion, as in L105's audit. Actual-field semistability and the
source height are the ones just identified. P2 now holds at this
same ell. No part of this setup imposes the original S1–S3-only
selector as an additional condition; L116's enlarged exclusion set
has preserved P1+/P2/P3. An F-defined ell-cyclic subgroup would
therefore force H<=B_4, contrary to H>B_4. This proves P4.

The unchanged member retains L089's original split height-30
condition at three, hence v_3(j)=-30. For any actual F-place x
above three the preceding semistable calculation gives

    h_x=-ord_(F_x)(j)=30e(F_x/Q_3)>0.

This is multiplicative reduction over the actual finite extension
F_x/Q_3; splitness over F_x is unnecessary. P2 says ell does not
divide precisely this nonzero integer. Since ell>=7 is odd and
different from three, all hypotheses of the cited local theorem
hold. It supplies a nonidentity transvection on the full E_o[ell]
in local inertia. Choosing an extending place identifies this local
action with a subgroup of the global full image R_F=rho(G_F), up
to one basis change, exactly as in L105. Thus R_F contains that
transvection, with no replacement by a projective or point image.

By finite-etale Galois descent in characteristic zero, an R_F-stable
line in E_o[ell] would be an F-defined subgroup scheme of order ell.
P4 rules out such a line. In a basis making the transvection upper
triangular its fixed line is therefore not invariant under R_F, so
some element of R_F is not upper triangular in that same basis.
GenEll Lemma 3.1(iii), with the prime field F_ell, now gives
SL_2(F_ell) subset R_F. This uses the covered group theorem rather
than an inference from the original Q-curve's mod-seven image.

### Restrict to the unchanged normal closure

L090 identifies C as the actual normal closure of this literal F,
and L092 gives [C:F]=4. The tuple has all L101 witness properties
that L104 uses: the same good member, literal fields, actual height,
ell>=7 and P1–P3. Its extra full downstairs containment has just
been proved. Although L104's statement names L101's selection, its
audited proof uses no property of that selector: the restriction
argument uses only these fields, their relative degree, ell>=7
and the full downstairs containment. Thus that argument applies to
this tuple without a new occurrence assertion or restriction theorem.
It gives R_C normal in R_F, [R_F:R_C] dividing four and
SL_2(F_ell) subset R_C, in the same full torsion basis.

All steps after the one L117 construction kept its member, ordering,
F,C,H and its one L116 prime. Since every ordering avoided Exc_4,
the argument applies separately after any ordering is fixed; it does
not require a single prime for all of them. This proves the conclusion.

This application supplies a common integrality/support and image
prerequisite before native assembly. It does not transport later
existential local choices automatically to this member. Full
(a)–(c)/initial data/III/P7, the directed-cover module hypothesis (*),
exact generation/full repair, relative factor-four excess, actual
action/factorization/pilot, authentication/def= qualifications,
essentiality and finite B>=A remain unresolved. No U/B descent,
full B[ell] rationality or global theta splitting is assumed.

### Separate critical audit — 2026-10-25, step484

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-25-integral-prime-image-critical-audit.md`.
Reuse its primary readings and the precise citations above, including
IV Corollary 2.2(ii)'s P4 implication, GenEll Lemma 3.1(iii),
Dupuy–Hilado Lemma 5.4.1 and L104's Milne/Conrad inputs. The source
comparison in step481 records explicitly that P4 uses P2 and the
fixed-domain setup, not a predicate requiring the original selector.
No fresh retrieval, authentication or stronger GenEll domain theorem
is used. The audited component results are inputs; this audit checks
their combination and actual proof hypotheses at the changed selector.

**Exception order and a single member.** The domains, d=6 and
epsilon_d=1 fix T_K before any R, member or prime. L105's component
argument fixes B_4=48+8T_K and the finite Exc_4 at that stage.
Its Northcott/fiber argument has no dependence on its later choice
of witness: bounded-degree J-values of bounded absolute height form
a finite set, and each fiber has at most six points. Thus
Exc_0 union Exc_4 is a legitimate fixed finite input to L117.
No Galois or root-permutation stability of this union is required:
L117 removes pairs whose rational invariant lies in its finite
J-image, which excludes every one of the six parameters at once.
Its positive R^2/(8D) count for all sufficiently large R gives a
member after this exclusion. Increasing R to ensure q_R>xi^2
also precedes choosing that member. Fix it once, then fix an
ordering. All ensuing assertions refer to its literal E_o,F,C.

**Actual height and the one prime.** L101's unconditional calculation
applies to every good member, before any prime is chosen. It uses
L100's unconditional semistability portion, including residue five
and nonsplit multiplicative places; it does not use P2 to define H.
For each rational p the complete sum satisfies

    sum_(v|p) e_v f_v=[F:Q],
    (1/[F:Q]) sum_(v|p) h_v f_v=n_p.

Consequently H=sum_p n_p log p is the reduced-denominator height
used in L117, and h_abs(j)<H+log 2000 since 0<j<1728.
The degree of t_o is at most six. If H<=B_4, t_o would therefore
belong to Exc_4, contradicting the chosen member's avoidance.
This proves H>B_4 for each ordering without another exception.

L117's retained slice has q_R<=H<=K and sqrt(H)>xi. Its audited
first moment gives W_R<=B_R<=M(H); the actual interval endpoint
U(H) is at most Y, and each actual pole counted in T divides
4A^3+27B^2. Hence T<=W_R is in the needed direction even when
the numerator cancels some denominator factors. This is an actual
pole-budget bound, not ATTEMPTS/036's insufficient scalar cap.
For this ordering L116 uses exactly F, its integer heights and
delta=3317760; [F:Q]=276480<=delta by L092. Its enlarged exclusion
set contains S1,S2,S3 and all remaining interval poles. The finite-set
bound gives one ell in (sqrt(H),U(H)], outside all these sets.
Thus ell>=7, P2 holds at every actual F-place, P3 holds, and
v_ell(j)>=0. Keep this prime throughout the remaining argument.

**P4 at that prime.** The parameter lies in the fixed domains,
E_o has its full two-torsion over T, and F contains iota and
the full 15-torsion. Full 30-torsion is therefore F-rational:
the 2- and 15-torsion subgroups sum to E_o[30]. The actual semistable
height and P2 have just been checked. These are the hypotheses
of the imported IV P4 component implication under the retained
Legendre-adjunction interpretation. A cyclic subgroup would give

    H <= 48 log(ell)/(ell-2)+24T_K/(ell-2)
      <= 48+8T_K=B_4.

Here ell>=7 implies ell>=5, log(ell)<=ell-2 and ell-2>=3;
the positive T_K is unchanged. This contradicts H>B_4. The
argument uses a pointwise implication, not L105's existential
conclusion or an identification of two witnesses. No P7 premise
is needed, and no new moduli-domain theorem is being assumed.

**Actual inertia and the entire representation.** The same good
member retains v_3(j)=-30. For any F-place x over three,
semistability and negative j-order give multiplicative reduction,
with -ord_(F_x)(j)=30e(F_x/Q_3)>0. Exclusion from S2 gives
ell not dividing this exact integer, rather than merely not
dividing the rational order 30. Since ell>=7, it is odd and
different from three. Dupuy–Hilado's cited local theorem and
its inspected nonsplit case therefore give a nonidentity
transvection in the full mod-ell inertia action over F_x.
Nonsplitness introduces no missing assumption: in this multiplicative
case the splitting extension is unramified quadratic, and the
covered splitting/cyclotomic proof preserves a nonzero order mod ell.
An extending place identifies that local torsion action with a
subgroup of the global action on the same E_o[ell]. No projective
quotient, point field or original Q-curve mod-seven representation
substitutes for this full module.

Over characteristic zero, finite-etale descent carries each
R_F-invariant line in E_o[ell] to an F-defined order-ell subgroup
scheme. P4 excludes every such line. In a basis with the exhibited
transvection upper triangular, its fixed line is therefore not
R_F-invariant; some element has nonzero lower-left entry in this
same basis. GenEll Lemma 3.1(iii) applies over the prime field
F_ell and gives SL_2(F_ell) subset R_F. This checks the local
input for the image argument, not the source's full native P5.

**Restriction and quantifiers.** Inspecting L104's entire proof
shows that its selector wording is not a mathematical premise
of the restriction argument. Here C is again the actual normal
closure of F/Q; hence C/F is Galois, and [C:F]=4. With
D=F(E_o[ell]), full-coordinate restriction gives

    R_C=Gal(D/(D intersect C)) subset Gal(D/F)=R_F,
    [R_F:R_C]=[D intersect C:F] dividing four.

The intersection is Galois over F, so this is an actual normal
matrix subgroup in the common torsion basis. L104's two elementary
unipotent families lie in R_F by the containment just proved.
Each nonidentity member has order ell, so its image in the quotient
of order dividing four is trivial. The cited elementary-generation
theorem puts SL_2(F_ell) in R_C. Neither integrality nor an older
prime-selection procedure enters this restriction proof.

The quantifiers are one good member, then each choice of ordering,
then one prime supplied for that ordering. The member and its
six exclusions were fixed before these prime choices; F,C,H and
ell do not change inside an ordering's proof. No common prime for
the six orderings is inferred. The direct DAG inputs are unchanged:
L101 retains L100 transitively, and L098 remains downstream only.

**Verdict.** All approved obligations pass without a mathematical
correction, new source hypothesis or change of witness. This
validates a known-method joint arithmetic prerequisite, not progress
beyond the checked sources. It does not transfer the later native
cover, section or theta choices to this witness. Full initial data,
directed (*), generation/full repair, the factor-four excess,
actual action/factorization/pilot, authentication/def= qualifications,
essentiality and original finite B>=A remain unresolved. No
complete candidate or essential IUT flaw is established.

## Mathlib

Full matching coverage for this constrained joint-witness application
and supporting coverage for its height, finite-etale descent, inertia
and restriction steps have not been checked. Unknown coverage is not
absence. No Lean verification, new general theorem or novelty claim
is made. This is REPRODUCTION using the cited inputs and the audited
local methods; step484 validates this joint application within its
explicit source qualifications.
