# L108 — Fixed-line simultaneous Tate place section

## Hypotheses

Fix the one member, ordering o, elliptic curve E_o, fields G_o,C_o
and selected prime ell>=7 of L105. Retain L090's geometric-object
dictionary F_mod=Q and nonexceptional rational invariant
j=j(E_o), with 0<j<1728. Retain L103's rational pole support

    S={p : v_p(j)<0}, Sigma=S minus {ell}.

Thus Sigma is finite, contains three and excludes two and ell; E_o
is multiplicative at every C_o-place above Sigma. Use only L098's
unconditional reduction conclusion through L103, not its extra
ell-integrality assumption. Set K=K_C=C_o(E_o[ell]), with both
coordinates of the entire geometric torsion adjoined, exactly as in
L107. Fix L107's one line U subset E_o(K)[ell], once for all places.
No descent of U to C_o is assumed. Work with places as equivalence
classes of absolute values, including infinite places.

The qualified native source convention of L090/L103/L107 remains
in force. Initial theta-data, a III situation and a full field repair
are not hypotheses. Neither split reduction over C_o nor K/Q
Galoisness is assumed.

## Conclusion

There exists a section

    s: V(Q) -> V(K),   s(p)|Q=p,

such that, for every p in Sigma, the image of the same fixed U
under E_o(K)[ell] -> E_o(K_(s(p)))[ell] is the geometric Tate toric
line. This line is defined by transporting the image of mu_ell in
the Tate parametrization through any geometric pointed comparison.
It is independent of that comparison, including for nonsplit
multiplicative reduction downstairs.

In particular s(Sigma) is in bijection with Sigma. This selects
one lift per rational place; it makes no alignment assertion about
other lifts. The member, ordering, ell, C_o, K and U, and L107's
cover, are unchanged. This known-method specialization supplies no
native graph identification, cusp sign, compatible theta splitting,
full initial data, exact-generation repair or numerical comparison.
The separate step439 critical audit below validates this limited
specialization.

## Proof

### Imports, duplication screen and bounded test

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-24-selected-prime-simultaneous-tate-line-place-section.md`.
Its inspected primary inputs are imported, rather than reproved:

- Kedlaya, [*Introduction: the Tate curve*, fall 2004](https://kskedlaya.org/18.727/tate-curve.pdf),
  Theorems 1–2, pp.3–4, with formulas (4)–(5), pp.2–3:
  for a finite p-adic field and negative j-valuation, the unique
  small q gives a geometric pointed Tate comparison. The
  parametrization is a group surjection with kernel q^Z.
- Milne, [*Elliptic Curves*, second edition, 2021](https://www.jmilne.org/math/Books/EC2.pdf),
  IV Proposition 7.13 and its nonexceptional case, p.140:
  in characteristic zero, pointed geometric automorphisms at
  j different from 0,1728 are exactly ±1.
- Conrad, [*Transitive Group Actions*](https://kconrad.math.uconn.edu/blurbs/grouptheory/transitive.pdf),
  Theorem 4.21, p.10: SL_2 over any field is transitive on lines
  (indeed doubly transitive). Apply it over F_ell.
- Milne, [*Algebraic Number Theory*, v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
  Theorem 7.38, p.123, Corollary 7.40, p.124, section 8,
  Proposition 8.2, p.136, and Proposition 8.10 with its
  preceding place action, p.139: places extend to finite number
  fields; in a finite Galois extension the automorphisms act on
  them by (sigma w)(x)=w(sigma^(-1)x), with the induced completed
  field maps. The actual transport is written below.

The matching fixed-line/variable-place mechanism is already
Dupuy–Hilado, [arXiv:2004.13228v1, 28 April 2020](https://arxiv.org/pdf/2004.13228v1),
Lemma 5.6.2, p.31; compare Definitions 5.4.3–5.4.5, pp.28–29.
Only its qualified method is used. We do not import its all-place
wording, reversed containment in the proof or an untwisted nonsplit
module assertion. The following work checks this method on our fixed
objects, especially the nonsplit line and transport direction.
The covered native section convention is IUT I, May 2020
[reproduction, Definition 3.1(b)–(f), pp.61–63](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf).
Source authentication and L091's def= qualifications are not removed.

L053/L060 are methods on old objects and a selected singleton, not
simultaneous conclusions for this member. ATTEMPTS/029,030,031,034,035
remain parked: no core reapproval, rank-two cover substitution,
unverified coordinate normalization, cyclic normality separator or
authentication retry is used. L105's image and L107's fixed U are
the actual inputs. No new group-transitivity theorem is needed.

The main gap is still original finite B>=A. The intermediate target
is simultaneous line alignment, potentially useful for a later local
graph test. Continue only if geometric comparison independence,
completion covariance and the full-section quantifiers pass without
changing fields or adding splitness. Graph/sign/splitting, native
III/P7, exact generation, the relative factor-four excess, actual
input/action/pilot and essentiality remain independent gaps.

### The actual geometric toric line

Write M=E_o(K)[ell], a two-dimensional F_ell-vector space by L107.
For a finite place w of K over p in Sigma, let i_w:K -> K_w be the
completion embedding and choose an algebraic closure of K_w.
The local invariant has negative valuation because j is rational
and p is a pole. Tate's theorem gives the unique q_w in K_w with
0<|q_w|<1 and a pointed geometric isomorphism

    f_w: E_(q_w) -> (E_o)_(K_w).

The isomorphism is allowed to be defined over a finite extension.
Let phi_(q_w) be the Tate group parametrization, and define

    T_w = f_w(phi_(q_w)(mu_ell))
          subset E_o(overline(K_w))[ell].                 (1)

The restriction of phi to mu_ell is injective: its kernel is
mu_ell intersect q_w^Z={1}, since |q_w^n|=1 forces n=0.
It has ell elements and its image is killed by ell. Thus (1) is
a line. All geometric ell-torsion is already K-rational: its
ell^2 distinct points inject under i_w and exhaust the ell^2
geometric local points in characteristic zero. Consequently (1)
is contained in E_o(K_w)[ell], whether or not f_w itself is defined
over K_w. Denote the resulting linear bijection by

    i_w: M -> E_o(K_w)[ell],
    T(w)=i_w^(-1)(T_w) subset M.                         (2)

Any two pointed comparisons differ by a pointed geometric
automorphism of E_o. By the imported automorphism theorem this is
±1, which preserves every subgroup. Hence T_w and T(w) are
independent of the comparison. This also handles a change of
algebraic closure: after transporting into a common closure, the
two comparisons differ in just this way. In the nonsplit case the
same definition works geometrically; it does not identify its
Galois character with the untwisted cyclotomic character. All fields
here have characteristic zero, including at residue characteristic
three, so the automorphism hypothesis is satisfied.

### Completion covariance with the correct place action

The full coordinate field K/C_o is finite Galois: the entire finite
geometric torsion set is invariant under G_(C_o), so its coordinate
field is normal, and characteristic zero gives separability. Its
action on M is faithful and its image is exactly rho(G_(C_o)).
By L105 that image contains SL_2(F_ell).

Let sigma in Gal(K/C_o) and put w'=sigma w with the imported
place-action convention. Choose representatives of these finite places
normalized by |p|=p^(-1). The map on the dense subfields

    i_w(x) |-> i_w'(sigma x),   x in K,

is an isometry, because |sigma x|_w'=|x|_w. It therefore extends
uniquely to an isomorphism t_sigma:K_w -> K_w'. On the respective
copies of C_o it sends i_w(c) to i_w'(c); it consequently identifies
the two completions of C_o at v=w|C_o=w'|C_o. Since E_o is defined
over C_o, its transported equation is its actual equation at w'.
On torsion points the coordinatewise transport reads

    t_sigma(i_w(P))=i_w'(sigma P),   P in M.             (3)

To check what this does to (1), extend t_sigma to algebraic
closures. Each finite extension of a complete p-adic field has
its unique extending absolute value, so such an extension is
isometric on the finite fields containing the needed coefficients
and torsion points. The transported small q_w has the invariant
of the transported curve; uniqueness in Tate's theorem gives

    t_sigma(q_w)=q_w'.

The Tate formulas have rational coefficients. Their convergent
sums commute with this continuous transport, and roots of unity
of order dividing ell are transported bijectively. Thus the
transported f_w is a permitted geometric pointed comparison for
the actual curve at w', and comparison independence proves

    t_sigma(T_w)=T_w'.

Together with (2)–(3), this gives the required identity in the one
unchanged global module:

    T(sigma w)=sigma T(w).                              (4)

The construction used actual completion transport over C_o, rather
than an unrelated choice of basis. It also shows that different
extensions to algebraic closures have the same effect on these
lines. No normality of K/Q is involved.

### Independent place choices and the full section

For every p in Sigma choose a place v_p of C_o over p and an
initial extending place w_p of K. These exist by the finite-extension
place theorem. T(w_p) and U are lines in M. L105's actual image
contains SL_2(F_ell), so the imported transitivity theorem supplies
an element of that image sending T(w_p) to U. Lift it through
Gal(K/C_o) onto its image and call the resulting automorphism sigma_p.
Set

    w_p'=sigma_p w_p.

It still lies over v_p and p. Equation (4) gives

    T(w_p')=sigma_p T(w_p)=U,                            (5)

which is the desired direction: equivalently sigma_p^(-1)U=T(w_p).
Equation (2) now gives i_w_p'(U)=T_w_p'. Different sigma_p may
be used for different p; they choose different places, not
different global U's. In particular the isogenies and cover of
L107 have not been replaced by conjugates as global objects.

For p in Sigma prescribe s(p)=w_p'. For every remaining rational
place, including the infinite one, choose any extending K-place.
The finite-extension place theorem includes archimedean places,
so these choices give a full section. Distinct rational places
have disjoint fibers, hence the choices are consistent and s is
injective. Since F_mod=Q by L090, this is exactly a full place
section over the stated moduli field, and restriction identifies
s(Sigma) with Sigma. There is no additional coherence condition
between distinct place fibers in the covered section predicate.

This passes the bounded target by the known place-selection method.
It makes no claim that every extending place has (5), or that U
descends to C_o. In particular it does not select generators of
toric lines, prove the native tempered graph quotient or choose
one global cusp with the required sign at all places. EtTh
Definition 2.5's graph and compatible-splitting conditions remain
separate. Full initial theta-data/III/P7 and field repair, the
relative factor-four excess, marked factorization and pilot,
essentiality and original finite B>=A remain unresolved. This is
local progress by a checked-source method, not a result beyond
the sources compared or a complete flaw candidate.

### Separate critical audit — 2026-10-24, step439

**Scope and source check.** The invocation-start SPECIALIZE assessment
is `drafts/literature/2026-10-24-fixed-line-place-section-critical-audit.md`.
This is a REPRODUCTION audit of the stated section, using the existing
method assessment and its duplication/obstruction screen. Directly
rechecked Kedlaya's formulas (4)–(5), the convergence argument and
Theorems 1–2, pp.2–4; Milne ANT's place action preceding Proposition
8.10, p.139, and Theorem 7.38, p.123; and the qualified IUT I
Definition 3.1(b)–(f), pp.61–63. The inspected Milne EC2 IV.7.13,
Conrad Theorem 4.21, ANT Corollary 7.40 and Proposition 8.2 are
reused with the exact hypotheses recorded in the approved assessment.
The native PDF screenshots exposed no visible page images in this
tool run; the relevant extracted text was read. No new authentication
of the reproduction or removal of the def= qualification is claimed.

**Actual inputs.** L090's ordered pointed comparison retains the
rational j in (0,1728) and gives F_mod=Q. L103's support proof gives
v_3(j)=-30, v_2(j)>=8 and negative j-valuation at every place over
Sigma; it does not require ell outside S. L105's audited existential
choice supplies the full linear SL_2 containment over this C_o for
this ell, and L107 fixes precisely K=C_o(E_o[ell]) and one U. Thus
the application has not replaced the original member or used the
older mod-seven image. No further conclusion of L107's global
clause application is needed for the place argument.

**Geometric line and nonsplit case.** For each w under consideration,
K_w is a finite extension of Q_p with |j|>1. Tate's Theorem 2(a)
therefore supplies q_w and the geometric pointed comparison without
using its splitness clause (b). Theorem 1 gives an injective map on
mu_ell, since no nonidentity q_w-power has absolute value one.
Characteristic zero gives exactly ell geometric roots of unity and
ell^2 geometric elliptic ell-torsion points. The full global torsion
already contributes ell^2 distinct local points, so all local
ell-torsion, including the line, lies in the image of i_w.

For two comparisons f,g from the same E_(q_w), g f^(-1) is a
pointed automorphism of E_o. Its j is not 0 or 1728, and its field
has characteristic zero; Milne's theorem therefore makes it ±1.
It preserves the subgroup f(phi(mu_ell)), so the lines agree.
For two algebraic closures choose an isomorphism over K_w. It fixes
all the already rational local ell-torsion points, transports
mu_ell to mu_ell and turns the two comparisons into this same case.
Thus closure independence is also literal equality after (2), not
merely equality of dimensions or characters. No nonsplit character
is identified with the cyclotomic character.

**Actual completion map.** Normality of K/C_o follows from invariance
of the complete finite torsion set; its faithful action has exactly
the image in L105. For w'=sigma w, the displayed normalization makes
the dense-subfield map an isometry. Its inverse is the analogous
map for sigma^(-1), so its completion is a field isomorphism, not
just an embedding. It fixes the embedded Q_p and transports each
C_o coefficient of the actual equation to its coefficient at w'.
This proves (3) coordinatewise, including the projective origin.

Extend this field isomorphism to algebraic closures. For each finite
extension containing the coefficients of f_w and the ell-th roots
of unity, uniqueness of the extending absolute value in ANT
Theorem 7.38 makes the extension an isometry; the finite fields are
complete. All partial sums of the Tate expressions for those roots
belong to such a finite field. For a nonidentity root zeta, none
of the denominators vanishes: q_w^n zeta=1 would force n=0 and
zeta=1. Kedlaya's convergence argument therefore applies, and
continuity carries their limits to the corresponding limits at
w'. The identity root maps separately to the origin. There is no
use of completeness of the entire algebraic closure.

The transported q_w has absolute value less than one and its curve
is geometrically isomorphic to the transported E_o. Uniqueness in
Theorem 2(a) identifies it with q_w'. Hence the transported f_w
is an allowed comparison at w', yielding t_sigma(T_w)=T_w'.
Combining this with (3) gives both inclusions in (4): for P in M,
P belongs to T(w) if and only if sigma P belongs to T(w').
Different closure extensions cannot change this statement, since
the resulting torsion points are rational over the respective
completed base fields. Only K/C_o, not K/Q, was used as Galois.

**Direction, simultaneity and native quantifiers.** Apply the imported
SL_2 transitivity to the ordered pair (T(w_p),U). The resulting
sigma_p satisfies sigma_p T(w_p)=U, rather than the opposite
unqualified image condition. Then (4) proves (5). The chosen
automorphism need not fix U: it acts in the comparison of places,
whereas the global U and the quotient cover are retained throughout.
The separate choices do not need to be one common automorphism.

For all remaining rational primes and the infinite place, ANT
Proposition 8.2 gives nonempty extension fibers; choosing one in
each completes s. Its image V has exactly one element over every
member of V(Q), because different fibers are disjoint. In the
source's notation Vbad_mod=Sigma and Vbad=V intersect V(K)bad
therefore equal Sigma and s(Sigma), respectively, under restriction.
This is precisely the section predicate at the start of Definition
3.1(e). The further local-type requirement later in (e) and common
cusp condition in (f) are independent assertions and have not
been discharged. Nor has selection of V replaced the full F-place
fiber appearing in (b)–(c).

**Verdict.** L108 passes with its original conclusion and direct
mathematical inputs unchanged. The explicit absolute-value
normalization above clarifies the isometry convention without
changing the argument. This audit establishes a checked local input
by published methods, not a result beyond the sources compared or
a complete IUT flaw candidate. It supersedes pending-audit wording
for L108 in the unchanged overview. Graph/sign/splitting, native
III/P7, full repair/exact generation, relative factor-four excess,
actual input/action/factorization/pilot, source qualifications,
essentiality and original finite B>=A remain open.

## Mathlib

Full matching and supporting Mathlib coverage for this exact-object
specialization is unchecked. Unknown coverage is not absence; no
formal verification is claimed. Tate uniformization, automorphisms,
line transitivity and number-field place theorems are imported by
the precise citations above. The same-member application and
completion covariance are the limited REPRODUCTION in this file.
Step439 validates the informal specialization; no formal verification
or additional Mathlib coverage is asserted.
