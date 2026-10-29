# L119 — Full bad-support place section on the integral witness

## Hypotheses

Fix one member furnished by L118, then any one ordering o and one
prime ell>=7 furnished for that ordering. Keep its literal curve
E_o and embedded fields

    E_o: V^2=X(X-1)(X-t_o),
    G_o=Q(t_o)(iota,E_o[15]), C_o=G_o^nor over Q,
    K=C_o(E_o[ell]), M=E_o(K)[ell].

All division fields include both coordinates of every geometric
torsion point. Fix any one F_ell-line U in M, once for all places.
Let j=j(E_o)=j(E) and S={rational primes p:v_p(j)<0}, with
v_p(p)=1. Places are equivalence classes of absolute values and
include the infinite places. Retain L089/L090's family and geometric
object dictionary, including the qualified interpretation F_mod=Q.
Retain L118's source-version and Legendre-adjunction qualifications.

No old-witness section or cover is an input. No descent of U,
split multiplicative reduction over C_o, initial theta-data, or
Galoisness of K/Q is assumed.

## Conclusion

The full rational multiplicative support supplied by L098 on this
tuple is S. It is finite, contains three and excludes two and ell.
There is a section

    s: V(Q) -> V(K),       s(p)|Q=p,

such that at every p in S the image of the same fixed U under the
actual completion embedding into E_o(K_(s(p)))[ell] is the geometric
Tate toric line. This line is independent of the pointed geometric
Tate comparison, also when reduction downstairs is nonsplit.
Restriction identifies s(S) with S. The section includes arbitrary
lifts at all remaining places, including infinity.

The member, ordering, prime, C_o, K and U are unchanged throughout.
This is a known-method application, validated by the separate
step489 critical audit below. It supplies no cover, common cusp, theta splitting, full
native initial data, essential IUT flaw or finite B>=A comparison.

## Proof

### Source scope, duplication and bounded test

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-25-integral-witness-full-bad-support-place-section.md`.
The matching method is Dupuy–Hilado,
[arXiv:2004.13228v1, 28 April 2020](https://arxiv.org/pdf/2004.13228v1),
Lemma 5.6.2, printed p.31, full proof and footnote 19. Its all-place
wording, printed reversed SL_2 containment and cyclotomic-character
caveat prevent a literal import. L108 already implements and audits
the qualified geometric method on a different witness. Here its
existential conclusion is not invoked: the construction is instantiated
on the present tuple using these previously inspected standard inputs:

- Kedlaya, [*Introduction: the Tate curve*, fall 2004](https://kskedlaya.org/18.727/tate-curve.pdf),
  Theorem 1, p.3, and Theorem 2(a), p.4, with formulas (4)–(5),
  pp.2–3: Tate parametrization with kernel q^Z, and the unique
  small parameter and geometric pointed comparison for |j|>1
  over a finite p-adic field. The base-field comparison of
  Theorem 2(b) would require splitness; it is not used.
- Milne, [*Elliptic Curves*, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
  IV Proposition 7.13, nonexceptional case, p.140: in
  characteristic zero and j different from 0,1728, pointed
  geometric automorphisms are precisely ±1.
- Conrad, [*Transitive Group Actions*](https://kconrad.math.uconn.edu/blurbs/grouptheory/transitive.pdf),
  Theorem 4.21/full proof, p.10: SL_2 over a field is transitive
  on its projective line. Use F_ell, with no new group theorem.
- Milne, [*Algebraic Number Theory*, v3.08 (19 July 2020)](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
  Theorem 7.38/Corollary 7.40, pp.123–124; Proposition 8.2,
  p.136; Proposition 8.10 and preceding action, p.139: extension
  of places, uniqueness of the extended absolute value on finite
  extensions of complete fields, and (sigma w)(x)=w(sigma^(-1)x).

L098 is used as the audited conditional reduction/support theorem;
its complete proof retains the residue-two case and precise reduction
citations. L089/L090 supply the family and dictionary; L118 supplies
the actual joint witness. No reproof of those results is needed.
The qualified IUT I May 2020 [reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf),
Definition 3.1(b)–(f), pp.61–63, supplies only the compared section
predicate. Authentication and def= qualifications remain in force.

The main gap is original finite B>=A. This step could supply place
selection for a later native local-model comparison. The passing
threshold is one unchanged tuple and U, with alignment over all S
and no extra exception, descent or splitness assumption. ATTEMPTS/035
and 036 remain parked; neither authentication retries nor the failed
scalar-budget enlargement is used. The duplication comparison with
L108 concerns a known method, not an equality of existential witnesses.

### Apply the conditional support theorem on this tuple

L118 retains exactly a survivor of L089 and the six literal models
and full-coordinate fields of L090. In particular j is rational,
0<j<1728, v_2(j)>=8 and v_3(j)=-30. L118 also supplies the
additional premise v_ell(j)>=0, for this ordering's same ell>=7.
These are L098's hypotheses, including its formerly conditional
integrality premise. Apply L098 to this survivor, ordering and prime.

It gives semistability at every actual finite C_o-completion and
multiplicative reduction exactly over S, with good reduction over
the complement. Thus S is the full rational bad support for E_o/C_o,
not a support with ell silently omitted. It is finite, contains three
and excludes two and ell. This application uses neither L103's
old-selector support nor L100's q-order conclusions. L090's geometric
dictionary on any survivor gives F_mod=Q with its retained source
qualification. No later native assembly is transferred.

### Geometric toric lines on the new full division field

In characteristic zero E_o[ell] is finite etale of degree ell^2.
The full-coordinate prescription makes it split over K, so M has
dimension two over F_ell. Base change along each actual completion
embedding i_w:K->K_w gives all ell^2 distinct geometric local
torsion points as K_w-points. Hence i_w induces a linear bijection

    i_w: M -> E_o(K_w)[ell].                         (1)

For any w of K above p in S, the finite p-adic field K_w has |j|>1:
the extended valuation of a rational number has the sign of v_p(j).
Choose an algebraic closure of K_w. Tate's theorem supplies a unique
q_w in K_w with 0<|q_w|<1 and a pointed geometric comparison
f_w:E_(q_w)->(E_o)_(K_w). It may be defined over a finite extension.
With phi_q the Tate parametrization, put

    T_w=f_w(phi_(q_w)(mu_ell)),
    T(w)=i_w^(-1)(T_w) subset M.                    (2)

The kernel on mu_ell is trivial: q_w^n of absolute value one forces
n=0. Therefore T_w is a subgroup with ell elements, killed by ell.
By (1) it is already in E_o(K_w)[ell], so T(w) is a line in M.

Two pointed comparisons from E_(q_w) differ by a pointed geometric
automorphism of E_o. Since the field has characteristic zero and
j is not 0,1728, this is ±1 and preserves the subgroup T_w.
Consequently (2) is comparison independent. For different algebraic
closures transport to a common one over K_w; all local ell-torsion
is K_w-rational by (1), and the same argument gives literal equality.
No untwisted cyclotomic-character identification is used at nonsplit
places, and residue characteristic three does not change the
characteristic-zero automorphism calculation.

### Actual completion covariance

K/C_o is finite Galois: the full finite geometric torsion set is
G_(C_o)-invariant, so its coordinate field is normal, and it is
separable in characteristic zero. Its action on M is faithful
because the torsion coordinates generate K over C_o, and its image
is exactly rho_(E_o,ell)(G_(C_o)). L118 gives SL_2 containment in
this full linear image on the same module.

Let sigma be in Gal(K/C_o), let w lie above p in S, and put
w'=sigma w. Normalize the absolute values at both places by
|p|=p^(-1). The actual dense-field map

    i_w(x) |-> i_w'(sigma x), x in K,

is an isometry, since |sigma x|_w'=|x|_w. It and the analogous
map for sigma^(-1) extend to inverse field isomorphisms. Denote
the former by t_sigma:K_w->K_w'. It sends the embedded c in C_o
to the corresponding embedded c, because sigma fixes C_o. Hence
it transports the actual equation of E_o to that at w', and

    t_sigma(i_w(P))=i_w'(sigma P), P in M.           (3)

Extend t_sigma to algebraic closures. On every finite extension
containing the coefficients of f_w and the relevant roots of unity,
uniqueness of the extending absolute value makes the extension
isometric. These finite fields are complete. Transported q_w has
absolute value less than one and the same invariant as E_o at w'.
The uniqueness in Tate's theorem gives t_sigma(q_w)=q_w'.
The rational-coefficient Tate formulas commute with this transport:
their partial sums lie in such a finite complete field, so their
limits do too and continuity carries the limits to the corresponding
ones at w'. For zeta!=1 in mu_ell no denominator vanishes, since
q_w^n zeta=1 forces n=0 and zeta=1. The identity root maps
separately to the origin. Roots of unity are carried bijectively
to roots of unity. Thus the transported f_w is an allowed pointed
comparison at w', and comparison independence yields

    t_sigma(T_w)=T_w',
    T(sigma w)=sigma T(w).                          (4)

The second equality follows in both directions from (1)–(3).
It is an equality inside the one unchanged global module M.
Its value does not depend on a closure extension, because the
torsion points in question are rational over the completed base
fields. Neither K/Q normality nor a basis-only substitution was used.

### Independent choices give the full section

For each p in S choose a place v_p of C_o above p and an extending
place w_p of K; the place-extension theorem gives both. Line
transitivity and L118's full image give a sigma_p in Gal(K/C_o)
such that sigma_p T(w_p)=U. Set w_p'=sigma_p w_p. It still lies
over v_p and p, and (4) gives

    T(w_p')=U, equivalently i_w_p'(U)=T_w_p'.        (5)

This is the needed action direction. Each p can use its own
sigma_p: they select places, while the global curve, K and U
stay fixed. In particular this does not assert that U is invariant
under Gal(K/C_o), or that one automorphism works for all p.

Set s(p)=w_p' for p in S. At every remaining rational finite place
and at infinity choose any extending K-place, again by the
place-extension theorem. Such fibers are nonempty also at infinity.
They are disjoint for distinct rational places, so these choices
give a full section with s(S) in bijection with S. Equation (5)
is exactly the required alignment at every selected bad place.
No alignment at the other lifts is claimed.

The bounded test passes without changing any fixed object or adding
an exception. This supplies a full section on the joint witness by
known methods, not progress beyond the sources checked. It has not
constructed or transferred a cover, a global cusp, a native local
type or an arithmetic theta model. Full (a)–(c)/initial data/III/P7,
the directed-cover module hypothesis (*), exact generation/full
repair, relative factor-four excess, actual action/factorization/
pilot, authentication/def= qualifications, essentiality and original
finite B>=A remain unresolved. No U/B descent, full B[ell]
rationality, global theta splitting or complete flaw candidate is
asserted. The separate critical audit below verifies this limited application.

### Separate critical audit — 2026-10-25, step489

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-25-integral-witness-place-section-critical-audit.md`.
Reuse its inspected primary coverage and the precise citations above;
in particular the geometric clause of Kedlaya Theorem 2(a), rather
than the split-base clause (b), is the Tate input. This audit checks
the actual maps and same-witness quantifiers. L108's step439 audit
is a comparison with the same published method on a different
witness, not an existential theorem transferred to this tuple.

**Premise matching and full support.** Fix the member supplied by
L118, one ordering and its prime before making any place choice.
L118 retains a survivor of L089 and precisely L090's literal E_o
and full-coordinate G_o,C_o. The geometric isomorphism in L090
identifies j(E_o)=j(E), even if that isomorphism does not descend.
L089 gives rational 0<j<1728, v_2(j)>=8 and v_3(j)=-30;
L118 gives v_ell(j)>=0 for this same ell>=7. Thus every hypothesis
of L098 is met. Its all-place statement gives actual semistability
and the good/multiplicative alternatives at every C_o-completion,
with support S exactly as in this statement. No selector in L103
or different prime enters this application.

In particular L098's residue-two coverage is available: full
15-torsion over C_o supplies level five at all residue primes
except five and level three at five. The prime level is invertible
in each relevant valuation ring. Its cited semistability theorem
and minimal-model classification distinguish good reduction from
multiplicative reduction by the sign of j. This is not an inference
from potential good reduction alone. The source-reproduction
authentication qualification remains in force. Rational j!=0 has
finite pole support; three is in it, and two and this ell are not.
Consequently the conclusion concerns all bad rational primes for
E_o/C_o, without an unexamined ell-place or residue-three exception.

**Entire local torsion and geometric comparison.** Over K the finite
etale group scheme E_o[ell] is a disjoint union of ell^2 copies of
Spec(K): both coordinates of every geometric torsion point are in K.
Base change to K_w gives ell^2 copies of Spec(K_w). Distinct global
points remain distinct, and these exhaust the geometric local
torsion. Hence (1) is an isomorphism on the entire module, not an
embedding of just one cyclic subgroup. It uses no embedding of the
global algebraic closure into the completed base field.

For w above any p in S, K_w is a finite extension of Q_p and its
normalized absolute value restricts to |.|_p. Thus |j|_w>1, so
Kedlaya's geometric theorem applies. In an algebraic closure,
mu_ell has ell elements. The parametrization kernel q_w^Z meets
mu_ell only in 1, since |q_w|<1. The image under a pointed comparison
is therefore a subgroup of order ell in the geometric ell-torsion.
All that torsion is already K_w-rational, by the preceding count.
This proves that (2) defines a line in the same global M.

If f and g are two comparisons from the same E_(q_w), then
g f^(-1) is a pointed automorphism of E_o over the algebraic closure.
Milne IV.7.13 applies in characteristic zero with j!=0,1728, so
this automorphism is plus or minus one. Both preserve every subgroup,
including the toric subgroup. For different algebraic closures, an
isomorphism over K_w transports mu_ell and a comparison to the same
construction and fixes every K_w-rational torsion point. Thus the
resulting subgroup is literally independent of those choices.
Nonsplit reduction does not require a base-defined comparison here;
neither its character nor the comparison is asserted to descend.

**Actual field maps and convergence.** The full torsion coordinate
field is finite Galois over C_o, since every C_o-conjugate permutes
the finite torsion set and characteristic zero gives separability.
The resulting faithful action is precisely L118's full C_o-image.
For w'=sigma w and absolute values normalized by |p|=p^(-1),

    |i_w'(sigma x)|_w' = |i_w(x)|_w, x in K.

This verifies the action convention, not merely an abstract
isomorphism between local fields. The dense-field map extends to
an isometric field isomorphism t_sigma; the map for sigma^(-1)
is its inverse. Because sigma fixes C_o, each coefficient of E_o
is carried to its actual coefficient at w'. Equation (3) follows
on both affine coordinates and the projective origin.

An extension of t_sigma to algebraic closures restricts on every
finite extension to an isometry by ANT Theorem 7.38. Such finite
extensions are complete. Choose one containing the coefficients
of f_w and mu_ell. Tate's rational-coefficient formulas, including
their convergent series, commute with this isometry: each partial
sum is transported to the corresponding partial sum, and continuity
preserves the limit. For a nonidentity zeta in mu_ell no denominator
1-q_w^n zeta vanishes, because absolute values would force n=0
and then zeta=1. The root 1 is handled separately as the origin.
There is no assumption that the algebraic closure itself is complete.

The transported q_w lies in K_w', has absolute value less than one,
and gives a Tate curve geometrically isomorphic to E_o there.
Uniqueness in Kedlaya Theorem 2(a) therefore identifies it with q_w'.
Transport sends mu_ell bijectively to mu_ell and f_w to an admissible
comparison. Comparison independence proves t_sigma(T_w)=T_w'.
Combining this equality with (1) and (3), for every P in M,

    P in T(w) iff i_w(P) in T_w
              iff i_w'(sigma P) in T_w'
              iff sigma P in T(w').

This establishes both inclusions in T(sigma w)=sigma T(w).
Different closure extensions agree on the relevant subgroup because
its points are rational over the completed base fields. Only K/C_o
was required to be Galois; no K/Q normality was used.

**Selection and every remaining place.** L118's SL_2 containment is
on this full M and hence, by Conrad's transitivity theorem, some
sigma_p in Gal(K/C_o) sends T(w_p) to the already fixed U.
The correct choice is s(p)=sigma_p w_p. Its restriction to C_o is
the originally chosen v_p, and covariance gives T(s(p))=U. Thus
the method works even within that selected C_o-place fiber. Each
p in the finite set S has its own allowed choice of sigma_p; it
does not require a common sigma or an invariant U. No rational
bad prime is discarded and the tuple and U are never reselected.

ANT's extension-of-places theorem applies to the finite number-field
extension K/Q without a normality hypothesis, including at infinity.
Every remaining fiber is nonempty. Choosing a place in each gives
the full section; distinct rational places have disjoint fibers,
so restriction identifies s(S) with S. No alignment at all lifts
of a bad prime, or at a good or infinite place, is claimed.

**Verdict and limits.** All approved obligations pass without a
mathematical correction, new exception, new source hypothesis or
change of witness. This establishes a critically checked local input
by known methods, not progress beyond the compared sources. The
direct mathematical inputs remain L089,L090,L098,L118; no dependency
on L108's witness or later native assembly has been introduced.
This audit supersedes the pending-audit wording for L119 in the
unchanged overview; the mathematical argument and DAG are unchanged.
Common cusp, cover/core, local type, theta transport, full initial
data, directed (*), generation/full repair, factor-four excess,
actual action/factorization/pilot, authentication/def= qualifications,
essentiality and original finite B>=A remain separate. This is not
a complete candidate demonstration of an essential IUT flaw.

## Mathlib

Full matching and supporting Mathlib coverage for this same-witness
application have not been checked. Unknown coverage is not absence.
The Tate, automorphism, line-transitivity and place theorems are
imported by the precise citations above; no Lean verification is
claimed. This is REPRODUCTION of the covered method, with the
new tuple's conditional support premises explicitly discharged.
