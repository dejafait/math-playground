# L105 — Same-selected-prime large image downstairs and upstairs

## Hypotheses

Retain L089's fixed original family, algebraic closure and both domains,
L090's literal ordered Legendre equations and full-coordinate fields,
and L092's actual normal closures. Fix d=6 and epsilon_d=1. All finite
exceptions in this statement are fixed before the existential member
and prime are selected; this is not a statement about an arbitrary
previously chosen L101 witness. Any given finite parameter exception
set may be included. For the resulting member and one ordering put

    E_o: V^2=X(X-1)(X-t_o), T=Q(t_o)=Q(E[2]),
    F=G_o=T(iota,E_o[15]), C=C_o=G_o^nor, iota^2=-1.

Every division field includes both coordinates of every geometric
point of the specified full torsion module. Retain the qualified April
2020 IV reproduction and explicit Legendre-adjunction interpretation
of L091 used in L101. The P4-P6 subargument is imported independently
of its subsequent P7 assertion. Neither initial theta-data nor a native
III situation is assumed over F or C.

## Conclusion

There is a choice in L101, after fixing the P4 exceptions, such that
its same E_o/F, downstairs normalized height H and selected prime
ell>=7 satisfy P1-P3 and also

    E_o has no F-defined ell-cyclic subgroup scheme,       (P4)
    E_o has multiplicative reduction at a place over 3,   (local input)
    SL_2(F_ell) subset rho_(E_o,ell)(G_F).                (P6)

Here three is different from two and ell. Applying L104 to exactly
these fields and this prime gives

    SL_2(F_ell) subset rho_(E_o,ell)(G_C).

Both images are the full linear torsion representations; their actual
relative index divides four. No prime common to all six orderings,
full GL_2 image, ell-integrality or complete field repair is asserted.
The separate step423 critical audit below validates this specialization.
The local input is not the source's full selected-moduli-place P5
assertion; the shared P5 label in the original proof is only shorthand
for the multiplicative-place input to its image argument.
It supplies one repair prerequisite, not an essential IUT flaw or an
original finite B>=A comparison.

## Proof

### Imports, duplicates and the bounded test

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-23-selected-prime-downstairs-large-image-application.md`
and its completed step419 source-scope comparison. The necessary
primary inputs, imported rather than reproved, are:

- Mochizuki, *IUT IV*, April 2020,
  [87-page reproduction, Corollary 2.2(ii), proof P4-P6, pp.45-46](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf#page=45).
  Under the preceding setup and P2, an F-defined ell-cyclic subgroup
  gives ((ell-2)/24)H <= 2 log(ell)+T_K, with a fixed positive
  bounded-discrepancy constant T_K. This is the isogeny-height
  subargument preceding P7, not an invocation of initial theta-data.
- Mochizuki, *Arithmetic Elliptic Curves in General Position*,
  [February 2009 author version, 25 pages](https://www.kurims.kyoto-u.ac.jp/~motizuki/Arithmetic%20Elliptic%20Curves%20in%20General%20Position.pdf),
  Proposition 3.4/Lemma 3.5, p.17, for that height input; Lemma
  3.1(iii), p.14, for the finite-field group implication from a
  transvection and absence of an invariant line. The local setup
  and Lemma 3.2, pp.14-15, and the final proof of Theorem 3.8(b),
  pp.19-20, give its torsion application. The
  [July 2016 comments](https://www.kurims.kyoto-u.ac.jp/~motizuki/Arithmetic%20Elliptic%20Curves%20in%20General%20Position%20(comments).pdf),
  especially (8),(13)-(16), retain the open-domain and proof
  qualifications. Journal pagination/byte identity is not asserted.
- Dupuy-Hilado,
  [arXiv:2004.13228v1, Lemma 5.4.1, pp.27-28](https://arxiv.org/pdf/2004.13228v1),
  including its nonsplit case: over a finite p-adic field, negative
  integer j-valuation prime to ell, for ell odd and different from p,
  gives a nonidentity transvection in the full mod-ell inertia image.
  Reuse the complete local proof coverage cited in the assessment;
  none of L041's global degree hypotheses is imported.
- Silverman, *Canonical Heights on Abelian Varieties*, AWS notes,
  [13 February 2024, Theorem 4.8(d), p.15](https://swc-math.github.io/aws/2024/2024SilvermanNotes.pdf#page=15),
  for Northcott on P^1/Q with O(1), with the height normalization
  in Definitions 4.4-4.5/Proposition 4.6, pp.13-14, as used in L101.

L047/L083 concern prime seven for different fields. L104 supplies
only a conditional transfer. Neither substitutes for occurrence at
this selected prime. Step419 screened those duplicates and the parked
cyclic-normality/authentication routes. No general large-image theorem
is reproved here, and the stronger GenEll Theorem 3.8(b) is not applied
directly to an unchecked moduli bounding set.

The main gap remains finite B>=A. This target can discharge L104's
premise as one independent normal-closure repair prerequisite. Continue
only if the finite exceptions precede selection, actual F supplies the
height and local hypotheses, and all image calculations keep the same
member and prime. Failure of any check would stop or narrow this
application. Relative degree excess, full native data and essentiality
are independent unresolved obligations.

### A finite P4 exception fixed before the member

For a temporary survivor and ordering, the portion of L100 independent
of its conditional P2 premise proves semistability at every finite
F-place. Full rational 5-torsion is used away from residue five and
full rational 3-torsion at five. Its actual nonnegative integer heights
and L101's complete normalized sum give

    h_x=e(F_x/Q_p)max(0,-v_p(j)),
    H=sum_p max(0,-v_p(j))log p,
    h_abs(j)=H+log max(1,|j|)<H+log 2000.              (1)

Here j=j(E_o)=j(E) is rational and 0<j<1728 by L089. All finite
places and their residue-degree weights enter the sum, without
normality of F/Q. These facts are available before prime selection.

Fix the P4 source constant T_K>0 for these fixed domains and fixed
source parameters. The P4 height implication is uniform in the member
and selected prime satisfying P2. For ell>=5, the elementary estimate
used in that source proof is

    2 log(ell) <= 48(ell-2)/24.

Consequently an ell-cyclic subgroup, under P2, would force

    H <= 48 + 24 T_K/(ell-2) <= 48+8 T_K =: B_4.       (2)

The numerator is ell minus two. No negative power of ell occurs in
this bound. There is no dependence on a subsequently chosen ell in
B_4. Fix now, before selecting a member,

    Exc_4={t in U(Q-bar): [Q(t):Q]<=6,
                          h_abs(J(t))<=B_4+log 2000}.

This set is finite by exactly the bounded-degree/fiber argument in
L101: J is Q-defined, so its values have degree at most six; Northcott
makes those bounded-height values finite; each finite value z has at
most six preimages because
256(t^2-t+1)^3-z t^2(t-1)^2 is a nonzero degree-six polynomial.
This uses projective height finiteness, not finiteness on a nonproper
open curve without a height condition.

Include Exc_4 and any initially given finite exceptions in L101's
Exc. Its own low-height exception is also fixed before selection.
Apply L101 once to obtain a survivor, then fix one ordering and its
actual E_o,T,F,C,H and simultaneous prime ell>=7 for the remainder
of this proof. All six parameters avoid Exc_4; for the chosen one,
(1) shows H>B_4, since H<=B_4 would put t_o in Exc_4.
P2 now holds for this same F and prime. If an F-defined ell-cyclic
subgroup existed, the cited height implication and (2) would contradict
H>B_4. This proves P4. Nothing is enlarged after choosing this member,
and nothing is asserted about every arbitrary earlier L101 choice.

### Actual-field P5 and the full torsion representation

The same survivor retains L089's original split height-30 local
condition, hence v_3(j(E))=-30. In particular three is a rational pole.
For any actual F-place x above three, L100's unconditional local
calculation gives multiplicative reduction and

    h_x=-ord_(F_x)(j)=30e(F_x/Q_3)>0.                 (3)

Such a place exists. Since ell>=7, it is away from two and ell.
This supplies the reduction property needed in P5 directly; the
source's additional P5 height exception is unnecessary for this
family. Multiplicative reduction is not assumed split over F_x.
L101's P2 says ell does not divide the integer (3).

The field F_x is a finite extension of Q_3, ell is odd and different
from three, and its integer j-valuation is negative with order prime
to ell. Thus the cited nonsplit-inclusive local theorem supplies a
nonidentity transvection on the full E_o[ell] in local inertia. A
choice of extending place embeds its local decomposition action in
the actual global G_F action, up to a common basis change. The full
geometric torsion is the same rank-two module after this embedding
(characteristic zero); no cyclic point field or x-coordinate quotient
replaces it. Therefore the global full image R_F contains a
nonidentity transvection.

An R_F-invariant one-dimensional F_ell-subspace of E_o[ell] would
be an F-defined ell-cyclic subgroup scheme: in characteristic zero
E_o[ell] is finite etale, and G_F-stable subgroups of its geometric
points descend to subgroup schemes over F. Conversely such a subgroup
gives an invariant line. P4 excludes it. Apply the cited GenEll
Lemma 3.1(iii) at this prime field and ell>=7 to R_F. It yields P6,
SL_2(F_ell) subset R_F. This is the cited P2/P4/local-transvection
method checked on the actual field; neither F/Q normality nor P7
has been assumed.

### L104 at the unchanged prime and limits

L090 identifies these literal fields and their actual normal closure;
L092 gives [C:F]=4. L101 supplied precisely the member, ordering and
prime retained above. We have now verified L104's extra full-image
premise over F. Its audited conditional conclusion therefore gives
SL_2(F_ell) subset rho(G_C), with actual image index dividing four.
The member, prime and source height H have not changed in this step.

This is local progress by known methods, not mathematics beyond the
checked sources. It does not identify native initial theta-data/III,
prove P7, repair exact generation or the relative factor-four excess,
or settle native input/action/factorization/pilot transport. The
reproduction authentication and def= qualifications remain. No
ell-integrality, essentiality, finite B>=A estimate or complete flaw
candidate follows. The separate audit below validates precisely this
application, with the local-P5 distinction made explicit.

### Separate critical audit — 2026-10-23, step423

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-23-selected-prime-occurrence-critical-audit.md`.
Reuse its complete primary-source coverage and the citations above;
neither the timed-out GenEll refresh nor IV authentication is retried.
This audit checks the application, not a new general height or image
theorem. L089/L090/L092 and the separate audits of L100/L101/L104 are
retained as established local inputs within their stated qualifications.

**P4 setup and uniformity.** The temporary survivor has all six
parameters in the one fixed K_V of L089, at every required embedding.
Its domains lie inside the open parameter curve, including the finite
extension intersections at two. Thus the fixed-domain discrepancy
constant in the inspected IV P4 subargument applies uniformly. The
source parameters d=6 and epsilon_d=1 are also fixed. The actual base
is F=Q(t_o)(iota,E_o[15]); t_o is neither zero nor one, and the
Legendre equation has its full two-torsion over Q(t_o). Full 15-torsion
and iota are F-rational by the complete-coordinate prescription.
In particular, full 30-torsion is rational as well, since E_o[30] is
the sum of its 2- and 15-torsion subgroups. L100 establishes actual-field
semistability without P2. No normality of F/Q or P7 is needed for
these inputs. The ready source comparison identifies the P4 inequality
as preceding P7 and using P2, the fixed domains and these actual-field
conditions. It is not inferred from the stronger GenEll theorem on
an unchecked new moduli domain.

The source H is the normalized finite-height sum over F. For every
rational p, the general completion formula sum_(x|p)e_x f_x=[F:Q]
and L100's h_x=e_x max(0,-v_p(j)) give exactly (1), without equal
local degrees or a Galois assumption. The rational invariant satisfies
0<j<1728, so the archimedean contribution is strictly less than
log 2000. No property of the prime to be selected enters this identity.

**Cutoff, finiteness and quantifiers.** For real x>=5,
x-2-log x is positive: it is positive at five and has derivative
1-1/x>0. Hence 2 log ell<=2(ell-2) for every relevant prime.
Dividing the imported P4 inequality by the positive (ell-2)/24 gives
H<=48+24T_K/(ell-2)<=48+8T_K. A positive T_K can be fixed once for
the fixed source data; B_4 therefore does not depend on a chosen
member or prime. This is a bound for a hypothetical cyclic subgroup
under P2, not an unconditional assertion of P2 before selection.

For every t in Exc_4, Q(J(t)) is a subfield of Q(t), so its degree
is at most six. Northcott applies on projective P^1 with O(1) and
the stated absolute height bound. Each resulting finite value z has
at most six preimages in U: the displayed polynomial has leading
coefficient 256 and degree six, so it never vanishes identically.
Thus Exc_4 is finite independently of a member. Union it with the
given finite exceptions before L101 adds its own fixed low-height
exception and makes its one selection. Infinitely many of L089's distinct
rational invariants lie outside the finite J-image of that union;
this excludes the union for every ordering of the chosen member.
After fixing an ordering, avoidance and (1) force H>B_4. L101 now
supplies P2 for exactly this F and ell>=7. A cyclic subgroup would
force the opposite inequality, so P4 follows. An arbitrary earlier
L101 witness is not upgraded by this argument.

**Actual local representation.** L089 retains v_3(j)=-30 for this
same survivor, and L090's geometric Legendre comparison preserves j.
Every actual F-place x over three is multiplicative by L100, with
h_x=30e(F_x/Q_3)>0. Places over three exist, and ell>=7 excludes
residue characteristic ell. P2 gives ell not dividing this precise
integer, not an order computed in a different division field.
The inspected split/reduction/nonsplit proof of Dupuy-Hilado Lemma
5.4.1 therefore applies to the finite 3-adic field F_x and supplies
a nonidentity transvection on its full geometric ell-torsion.
Nonsplitness introduces no missing hypothesis: the covered proof
passes to a splitting/cyclotomic extension of degree prime to ell;
its inertia is a subgroup of the original inertia, and the nonzero
parameter order modulo ell is retained. In the present multiplicative
case the splitting extension is unramified quadratic. The local
decomposition action embeds in the global torsion image after one
choice of extending place and basis. Consequently R_F contains the
same nonidentity transvection, not merely an element in a projective
or one-point quotient.

This proves the displayed local input. The source P5 is formulated
with selected moduli places; a local F-place alone does not establish
that whole assertion. Removing that possible reading of the label
does not remove any premise of the image argument, which uses only
the exhibited local transvection. No native P5/P7 is certified here.

**Invariant line, group theorem and transfer.** Characteristic zero
makes the entire E_o[ell] finite etale of rank ell^2. Finite-etale
Galois descent identifies an R_F-stable line in its two-dimensional
F_ell-space with an F-defined subgroup scheme of order ell. P4 rules
out every such line. Choose a basis with the transvection upper
triangular; its fixed line is then not R_F-invariant, so some element
of R_F is not upper triangular in that same basis. These are precisely
the hypotheses of the cited GenEll Lemma 3.1(iii) over the prime
field F_ell. Its conclusion gives SL_2(F_ell) subset R_F, with no
assumed full GL_2 image or changed prime. This imports the group
theorem rather than reproducing its classification.

Finally C is the actual normal closure of this F by L090, and
L092 gives [C:F]=4. The just-proved containment is exactly L104's
additional premise for L101's unchanged member, ordering and prime.
Its separately audited restriction argument therefore gives the
upstairs containment and image index in {1,2,4}. Neither F/Q normality
nor C contained in F(E_o[ell]) is substituted for that argument.

**Verdict.** The mathematical occurrence and transfer pass, with the
local-P5 wording clarified and no changed argument or direct inputs.
This establishes a checked known-method prerequisite, not a result
beyond the inspected sources. Native theta-data/III, exact generation,
the relative factor-four excess, full repair, input/action/factorization/
pilot, authentication/def= qualifications, essentiality and finite B>=A
remain unresolved. No ell-integrality or complete flaw candidate follows.

## Mathlib

Full matching and supporting Mathlib coverage for this exact-field
specialization is unchecked. Unknown coverage is not absence; no
formal verification or new general theorem is claimed. The primary
height, local inertia and finite-group inputs are imported by the
citations above; the work here is their exception-order and actual-field
specialization (REPRODUCTION).
