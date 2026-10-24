# L103 — Normal-closure omitted-ell arithmetic dictionary

## Hypotheses

Fix one L101 member, one ordering o and its selected prime ell>=7,
with the fixed L089 family, domains and algebraic closure, d=6 and
epsilon_d=1. Retain L090's literal equation and full-coordinate fields

    E_o: V^2=X(X-1)(X-t_o), j=j(E_o)=j(E) in Q,
    T=Q(t_o)=Q(E[2]), F=G_o=T(iota,E_o[15]), iota^2=-1,
    C=C_o=G_o^nor over Q.

Use the same original downstairs H of L101 and L102. Set

    S={rational primes p:v_p(j)<0}, U=S minus {ell},
    n_p=-v_p(j) for p in S, v_p(p)=1.

For every actual finite C-place w, let p_w be its rational residue
prime, f_w its absolute residue degree and h_w the GenEll integer
curve height of L100. Integer valuations ord_w have value group Z.
All divisors below are finite arithmetic divisors with zero infinite
part. Define them arithmetically, without asserting native theta-data:

    D_C^(not2)=sum_(w:p_w!=2) h_w [w],
    D_(U,C)=sum_(w:p_w in U) h_w [w],
    deg_C(sum_w a_w[w])=(1/[C:Q])sum_w a_w f_w log(p_w),
    log(q_C^(not2))=deg_C(D_C^(not2)),
    log(q_(U,C))=deg_C(D_(U,C)).

The last two symbols denote positive arithmetic degrees in the
source-shaped notation, not logarithms of chosen field elements or
pilot log-volumes. Reuse the qualified April 2020 IV and May 2020 I
reproductions and the explicit def= boundary in the saved assessment;
current author/journal authentication is unresolved.

## Conclusion

U is finite and nonempty, contains three, and avoids two and ell.
At every C-place over U the curve is multiplicative and its integer
height is prime to ell. At every finite complementary place away
from 2ell it has good reduction. These are the reduction/support
predicates only, not full initial theta-data.

There is an equality of arithmetic divisors and hence the exact identity

    D_C^(not2)-D_(U,C)=sum_(w|ell) h_w[w],               (1)
    Delta_C=(log(q_C^(not2))-log(q_(U,C)))/6
           =H_ell(C)/6 < sqrt(H)log(ell)/6.             (2)

Here H_ell(C) is precisely L102's complete weighted contribution.
Neither ell-integrality nor positivity of Delta_C is required.

For a native interpretation, independently supplied initial theta-data
and an IUT III comparison situation for this same E_o with base C,
moduli field Q and selected moduli support U must identify its q-divisor
with these ordinary q-orders on the complete inverse image of U.
Under that identification, computing the native arithmetic degree at
F'=C in K_C=C(E_o[ell]) gives exactly (2)'s arithmetic difference.
This conditional dictionary does not construct such data or apply IV
Theorem 1.10. Its pilot magnitude has the separate 1/(2ell) factor.

## Proof

### Imports, overlap and bounded test

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-23-native-omitted-ell-term-identification.md`.
Reuse its inspected primary definitions without another source search:

- Mochizuki, *IUT IV*, April 2020,
  [87-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
  Definition 1.9(i)–(ii), printed pp.21–22; Theorem 1.10's hypotheses
  and definitions, pp.22–23; Corollary 2.2(i)–(ii), pp.41–43 and
  proof pp.44–47, especially P5 p.46 and the first display p.47.
  Finite arithmetic degree uses log(#k_w) and global division by
  [F':Q]; the q-divisor is supported on complete selected fibers.
  The non-dyadic variant omits two. The omitted difference has
  coefficient 1/6; the separate pilot magnitude is log(q)/(2ell).
  Definition 1.9(ii)'s normalized E-degree is not substituted here.
- Mochizuki, *IUT I*, May 2020,
  [186-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf),
  Definition 3.1(b)–(e), pp.61–63 and Example 3.2(iv), p.71:
  selected support is nonempty and odd, avoids ell, and is tested
  on all extending places; the geometric q-parameters are distinct
  from their 2ell-th roots. A place section does not replace a fiber.
- Mochizuki, *Arithmetic Elliptic Curves in General Position*,
  Math. J. Okayama Univ. 52 (2010),
  [Definition 3.3 and Remark 3.3.1, p.17](https://www.math.okayama-u.ac.jp/mjou/mjou52/_01_mochizuki.pdf#page=17):
  ordinary integer q-height, divided by ramification of a splitting
  extension when needed. Its complete semistable specialization,
  including nonsplit places, is already proved and audited in L100.

L102 proves the weighted numerical bound, but explicitly leaves this
divisor dictionary open. L098's extra ell-integrality hypothesis is
not used or removed. ATTEMPTS/035's authentication route stays parked.
No general theorem is reproved. The original gap is finite B>=A;
this intermediate dictionary could supply its omitted-term component
in a possible normal-closure repair. Continue only if complete fibers,
ordinary coefficients, sign and normalization give exactly (1)–(2).
Independent initial-data, generation and essentiality gaps remain.

### Support and ordinary coefficients at every actual place

S is finite since the nonzero rational j has only finitely many
denominator primes. L089 retains the original member's split Tate
height 30 at three, so v_3(j)=-30; this is a statement about that
same rational invariant and survives its geometric Legendre comparison
in L090. Hence three belongs to S. L089 also gives v_2(j)>=8, so
two does not belong to S. L101 gives ell>=7. Therefore removing
ell leaves three in U and U is nonempty, odd and disjoint from ell.

For every actual w, L100's semistability and local-height calculation
give good reduction if p_w is outside S and multiplicative reduction
otherwise, with

    h_w=e(C_w/Q_(p_w)) n_(p_w) if p_w in S,
    h_w=0 otherwise.                                   (3)

This uses full rational 15-torsion after each completion, and does
not presume split reduction everywhere. At a multiplicative place,
take the split Tate comparison over L/C_w from L100. GenEll uses
ord_L(q)/e(L/C_w)=h_w. The nonsplit splitting extension is unramified,
so even its ordinary Tate order is h_w, with no residue-degree factor
two. These are ordinary q-orders, not orders of q^(1/(2ell)).
The height is already integral over C_w; an extra absolute ramification
factor multiplying h_w would count the ramification in (3) twice.

L101 discharges L100's P2 premise for this very prime and member;
therefore every nonzero h_w is prime to ell. At each p in U all
extending places are consequently multiplicative with this coprimality.
If p is outside U and outside {2,ell}, then p is outside S, so (3)
gives good reduction at every extending place. This verifies exactly
the stated support predicates even when ell itself belongs to S.

### Complete coefficient subtraction and normalized degree

Both divisors have finite support by (3). Fix any actual finite w.
If p_w=2, both coefficients are zero, and w is not above ell.
If p_w is in U, both coefficients are h_w and cancel. If p_w=ell,
the first coefficient is h_w and the second zero. This holds also
when ell is outside S, in which case h_w=0. In the remaining case
p_w is outside S and neither 2 nor ell, so both coefficients are
zero by (3). These cases exhaust all actual places, proving (1).
In particular no pole other than ell is silently omitted.

Since #k_w=p_w^(f_w), applying the displayed degree definition to
(1) gives

    log(q_C^(not2))-log(q_(U,C))
      =(1/[C:Q])sum_(w|ell) h_w f_w log(ell)=H_ell(C).

Every place in the full ell-fiber enters once. There is no selected
representative, omitted residue degree, archimedean contribution or
extra ramification factor in this finite subtraction. The degrees
are nonnegative arithmetic quantities, so this is a positive-sign
contribution (possibly zero), rather than a difference of negative
pilot log-volumes. Dividing by six and applying L102 for the same
H and ell proves (2), retaining its strict bound even if the
contribution vanishes. No 2ell factor belongs in these divisors.

### Conditional native meaning and precise remaining boundary

L090 gives F_mod=Q for this geometric punctured curve; L092 gives
C/Q Galois of degree 2^13*3^3*5, prime to ell>=7. If native data
with base C are supplied, their ell-division field is K_C=C(E_o[ell]);
C is an allowed Galois intermediate computing field F' over Q.
No containment of C in the old F(E_o[ell]) is asserted or needed.
With selected moduli support U and the same ordinary local q-orders,
the source definition's complete inverse-image divisor at F'=C is
exactly D_(U,C). Its non-dyadic arithmetic analogue is D_C^(not2).
Thus the cited definition chain, under the explicit native
identification, makes its omitted arithmetic expression Delta_C.
The source's negative pilot log-volume instead uses the separate
magnitude log(q)/(2ell); it cannot change the 1/6 in (2).

This verifies an arithmetic dictionary and only a conditional native
one. It supplies no core/cover/section, full initial theta-data or
III situation. Under the fixed literal prescription, adjoining iota
and E_o[15] to T still gives F, whereas [C:F]=4 by L092. Accordingly
IV Theorem 1.10's exact-generation equality is not repaired here.
The relative factor-four excess, P4–P7/full repair, native input/action,
all-image factorization, marked pilot transport, authentication and
essentiality remain unresolved, as does original finite B>=A.
No complete-solution candidate or progress beyond checked sources
is claimed. The separate step414 critical audit below validates this
arithmetic identity and its explicitly conditional native dictionary.

### Separate critical audit — 2026-10-23, step414

**Scope and verdict.** The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-23-omitted-ell-dictionary-critical-audit.md`.
The arithmetic identity and conditional interpretation pass without
mathematical correction. The exact primary definition chain above is
reused within its inspected April/May reproduction and def= limits;
this audit makes no new authentication claim. It checks the application
of those definitions, not the disputed IUT III comparison itself.

**Same-member inputs.** L101 fixes one survivor, one ordering and one
prime ell>=7, with H computed over the literal F=G_o. L089 retains
v_3(j(E))=-30 and proves v_2(j(E))>=8 for that survivor. L090's actual
pointed geometric comparison preserves its rational j, and identifies
F_mod=Q and T=Q(t_o). L092 concerns precisely these full-coordinate
fields: [C:Q]=1105920=2^13*3^3*5 and [C:F]=4. L100's local-height
calculation applies to both fields, and L101 supplies its P2 premise
for this same prime. L102's audited contribution uses the same H and
ell. No retained earlier witness, common prime for all six orderings,
or old ell-division field is substituted. These are exactly the six
direct inputs recorded for L103 in DAG.md.

**Support and local theorem hypotheses.** Nonzero rational j has
finite pole support S; the retained valuations put three in S and
two outside it. Since ell>=7, U=S minus {ell} retains three and
avoids two and ell. Each C_w is a finite extension of Q_p with finite
perfect residue field. The complete geometric 15-torsion remains
rational there, as checked in L100: level five is invertible except
at p=5, where level three applies. Thus semistability is available
before using the sign of the j-valuation to distinguish good from
multiplicative reduction. In particular all places over U are
multiplicative, and every complementary place away from 2ell is good.
L101 and L100 make every positive height prime to ell, including a
possible height above ell. This proves only the stated support and
height predicates; multiplicative does not here assert splitness or
full initial theta-data.

For multiplicative reduction L100's inspected Tate and GenEll inputs
give ord_L(q)=-ord_L(j) in a splitting extension L/C_w. Restriction
of integer valuations and the height's division by e(L/C_w) cancel,
giving h_w=-ord_w(j)=e(C_w/Q_p)n_p. The nonsplit extension is unramified
quadratic: its residue degree two is not a multiplier of h_w. At good
places h_w=0. Thus the coefficient is an ordinary integer q-order,
not an absolute-normalized order, a root order h_w/(2ell), or an
order multiplied a second time by absolute ramification.

**Exhaustive coefficient check.** At a dyadic place both divisors
have coefficient zero, and it is not an ell-place. At a place over
U the coefficients are both h_w. At a place over ell the coefficients
are h_w and zero, because ell is neither two nor in U; if ell is
outside S, this same difference is zero. Every remaining finite
place is outside S, so both coefficients vanish. These disjoint cases
exhaust the finite places. Every divisor has zero infinite part.
Consequently (1) holds coefficient by coefficient, without any
ell-integrality assumption or omission of another pole. Both divisors
are finite because S is finite and every rational prime has finitely
many extending places.

**Weights, sign and strict threshold.** Definition 1.9(i) assigns
log(#k_w)=f_w log(p_w) to [w], divided by [C:Q]. Applying this linear
functional to the finite identity gives exactly

    deg_C(D_C^(not2))-deg_C(D_(U,C))
      = sum_(w|ell) h_w f_w log(ell)/[C:Q] = H_ell(C).

Here f_w is the absolute residue degree of C_w, including all residue
extensions already present. There is no residue degree from a new
splitting field in this sum, and no place-section representative can
replace the complete fiber. The expression is nonnegative, possibly
zero. L102's strict estimate, with H>25 and log(ell)>0, applies to
this very H_ell(C); division by the positive six proves precisely
Delta_C<sqrt(H)log(ell)/6. In particular the zero-height case still
satisfies the strict bound. The one-sixth is the arithmetic subtraction
coefficient in IV Corollary 2.2(ii), proof p.47. Negative pilot
log-volume and its separate magnitude log(q)/(2ell) do not redefine
these positive arithmetic degrees. Definition 1.9(ii)'s E-degree
normalization is not being used.

**Conditional native boundary.** C/Q is Galois of degree prime to
ell. If independent native data and a III situation for the same
E_o over C, with selected moduli support U, are supplied as stipulated,
then their own division field is K_C=C(E_o[ell]). The permitted
intermediate computing field F'=C lies between Q and K_C and is
Galois over Q. At this computing field the stipulated ordinary
q-orders and complete selected fibers give exactly D_(U,C). Hence
the definition chain identifies the arithmetic omitted expression,
without constructing a pilot or proving its comparison inequality.
An inclusion C subset F(E_o[ell]) is neither used nor inferred.

This conditional statement does not verify all initial-data clauses,
P4–P7, exact generation, or applicability of IV Theorem 1.10. For the
fixed literal model, T(iota,E_o[15]) is still F, strictly smaller than
C by degree four. The relative degree excess and other repair gaps
therefore survive this passing check. Authentication, native
input/action/factorization/pilot and essentiality remain unresolved;
original finite B>=A is unchanged. This verifies a known-definition
specialization, with no claimed result beyond the checked sources.
The argument and its direct inputs are unchanged, so PROOF.md and
DAG.md are unchanged; this audit supersedes the overview's pending
wording for L103 only.

## Mathlib

Full matching and supporting Mathlib coverage have not been checked.
Unknown availability is not absence. This is an informal specialization
of the cited degree definitions and audited local heights; no numerical
certificate, mathematical script or general theorem reproof is needed.

The separate step414 audit verifies the informal application only;
it is not a Mathlib formalization.
