# L100 — Conditional P2 transfer without ell-integrality

## Hypotheses

Fix any survivor E/Q of audited L089, retaining the fixed family,
both domains and algebraic closure. For any of the six orderings o
use exactly L090's literal curve and full-coordinate fields:

    T=Q(E[2])=Q(t_o), E_o: V^2=X(X-1)(X-t_o),
    G_o=T(iota,E_o[15]), iota^2=-1, C_o=G_o^nor over Q.

Thus every coordinate of every geometric 15-torsion point belongs
to G_o, C_o contains G_o, and j(E_o)=j(E) is a nonzero rational
number. Use audited L092's degree of this same normal closure.
For rational primes use v_p(p)=1 and put

    S={p:v_p(j(E))<0}, n_p=-v_p(j(E)) for p in S.

At every finite place x of either number field, the curve height
h_x means GenEll Definition 3.3/Remark 3.3.1: zero for good
reduction, and the split Tate parameter's integer order divided
by the splitting extension's ramification index otherwise. The
valuation downstairs is surjective onto Z. Semistability and
integrality of these heights in the present setting are justified
below; they are not assumed from L098 outside its hypotheses.

Let ell>=7 be prime and assume precisely the conditional input

    (P2 over G_o) ell divides no nonzero h_v,
                 for every finite place v of G_o.        (1)

This is the clause read in IUT IV's April 2020 Corollary 2.2(ii)
proof, with the literal field F=G_o. Neither existence of such a
prime selected with the other source clauses, nor v_ell(j(E))>=0,
nor initial theta-data for these fields is assumed.

## Conclusion

Every rational pole order avoids ell:

    ell does not divide n_p for every p in S.             (2)

For every actual finite C_o-place w above any p in S,

    h_w=e((C_o)_w/Q_p)n_p>0, gcd(ell,h_w)=1.             (3)

At every actual C_o-place outside S the curve has good reduction
and height zero. Thus (P2) holds over C_o at all finite places.
The conclusions include p=ell if ell belongs to S; they do not
assert ell is outside S. All assertions hold separately for every
survivor and each of its six orderings satisfying (1).

This is a same-field specialization of known local theorems. It
clears a conditional height-avoidance prerequisite for a possible
normal-closure repair, without establishing that repair, native
selected support, an essential IUT flaw or original finite B>=A.
The separate step402 critical audit below validates this conditional
specialization with the same source qualifications.

## Proof

### Imported statements, comparison and bounded test

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-22-literal-to-normal-closure-selected-prime-transfer.md`.
Reuse its inspected general sources without renewed discovery:

- Mochizuki, *Inter-universal Teichmuller Theory IV*, April 2020,
  [87-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
  Proposition 1.8(v), printed p.19 and proof p.20: full rational
  prime-level torsion of level at least three invertible in a complete
  DVR gives semistable reduction. Corollary 2.2(ii), proof pp.44–46,
  especially (P2), p.45, supplies the interpretation of (1). Current
  author/journal authentication remains unresolved. This proposition
  is conditional on (1), and does not reproduce prime selection.
- Silverman, *The Arithmetic of Elliptic Curves*, second edition
  (2009), [VII.5.5, pp.197–199, and A.1.3/A.1.4(b), pp.412–413](https://studylib.net/doc/28155304/the-arithmetic-of-elliptic-curves):
  the perfect-residue-field integral-j/potential-good criterion,
  including residue two, and the good/multiplicative minimal-model
  cases. Within semistable reduction, good reduction has integral
  j and multiplicative reduction has negative j-valuation.
- Silverman, [C.14.1(b,d), p.445](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf),
  and Kedlaya, *Introduction: the Tate curve*, fall 2004,
  [equation (3), p.2, Theorems 1–2 and relevant proof, pp.3–4](https://kskedlaya.org/18.727/tate-curve.pdf):
  the Tate parameter and pointed split comparison over finite Q_p
  extensions, the unramified quadratic splitting extension for
  nonsplit multiplicative reduction, and the convergent integral
  series j(q)=q^(-1)+744+sum_(m>=1)c_m q^m, c_m in Z.
- Mochizuki, *Arithmetic Elliptic Curves in General Position*,
  Math. J. Okayama Univ. 52 (2010),
  [local setup pp.16–17, Definition 3.3 and Remark 3.3.1, p.17](https://www.math.okayama-u.ac.jp/mjou/mjou52/_01_mochizuki.pdf):
  the extension-independent curve-height convention stated above,
  using integer valuation downstairs and division by ramification.
- Milne, *Algebraic Number Theory*, v3.08 (19 July 2020),
  [Theorem 3.34 and Galois proof, pp.59–60; Corollary 7.42/Remark 7.43, p.124; Exercise 4-2/solution, pp.83,155](https://www.jmilne.org/math/CourseNotes/ANT.pdf):
  existence of places over each rational prime, the Galois efg
  formula, restriction of integer valuations and multiplicativity
  of ramification indices. No absolute-base tameness is required.

No general theorem is reproved. L098 and L099 already carry out
related reduction and height specializations with an additional
ell-integrality premise. They are method comparisons here, not
unconditional premises after deleting that assumption. L061/L084
concern different fields. ATTEMPTS/035's authentication failure
is not reopened. The new local work is to check the actual G_o
heights and the implication from (1), then the transfer to C_o.

Original finite B>=A remains the main gap. The intermediate target
could remove height avoidance as a separate obstruction to normal
closure while leaving integrality/support and relative degree
unresolved. Continue only if complete torsion, downstairs height
normalization and prime-to-ell ramification hold at every required
place, including p=ell. A failed hypothesis stops this implication.

### Semistability over both fields, at every actual finite place

Fix a survivor, ordering and prime ell as in the hypotheses. Let
F be either G_o or C_o, let x be any finite F-place above p, and
write K=F_x. It is a finite extension of Q_p, hence complete and
discretely valued of characteristic zero with finite perfect residue
field. This uses no Galoisness assumption on F.

For n=3 and n=5, all geometric n-torsion points of E_o already
have both coordinates in G_o. In characteristic zero the kernel
scheme E_o[n] is finite etale of degree n^2, and all n^2 points
are rational over F. It is therefore the disjoint union of n^2
copies of Spec(F). Base change by the actual completion embedding
F -> K gives n^2 copies of Spec(K). Thus the full geometric local
n-torsion, not just x-coordinates or a cyclic subgroup, is K-rational.

At p!=5 use n=5 in IV Proposition 1.8(v); at p=5 use n=3.
Each chosen n is prime, at least three, and invertible in O_K.
The cited theorem gives semistability over K itself. This includes
p=2,3 and p=ell; the latter uses level five since ell>=7.

The rational invariant has integer valuation

    ord_K(j(E_o))=e(K/Q_p)v_p(j(E)).                     (4)

The cited semistable alternatives and their j-valuation signs now
give good reduction exactly for p outside S and multiplicative
reduction exactly for p in S. No potential-good-to-good implication
for an arbitrary twist is used, and multiplicative need not be split.

### Integer height over an arbitrary one of these completions

Suppose p in S. Take L=K in the split case, or the cited unramified
quadratic splitting extension in the nonsplit case. The actual
pointed curve over L is Tate(q), with ord_L(q)>0 and j(q)=j(E_o).
In the imported integral series, every term c_m q^m has order at
least m ord_L(q), tending to infinity. Every partial sum of the
remainder after q^(-1) is integral. Completeness and closedness of
O_L make its full convergent limit integral as well. Since q^(-1)
has strictly negative order, there is no cancellation at its order:

    ord_L(j(E_o))=-ord_L(q).

The height convention and restriction of integer valuations give

    h_x=ord_L(q)/e(L/K)
       =-ord_L(j(E_o))/e(L/K)
       =-ord_K(j(E_o))=e(K/Q_p)n_p.                    (5)

Both e(K/Q_p) and n_p are positive integers. This is the actual
positive integer height downstairs. In the nonsplit case e(L/K)=1,
although [L:K]=2; no erroneous factor two is inserted. No height in
an ell-division field is used. At p outside S the preceding good
reduction conclusion gives h_x=0 by the height definition. Formula
(5) applies without any inequality or distinction between p and ell.

### P2 downstairs forces rational pole-order avoidance

Fix any p in S. There exists a finite G_o-place v above p. Apply
(5) to K=(G_o)_v. Its height h_v=e((G_o)_v/Q_p)n_p is nonzero.
If ell divided n_p, it would divide this integer h_v, contradicting
(1). Thus ell does not divide n_p. Since p was arbitrary, (2)
follows for the complete rational pole support. This direction uses
no divisibility of a local degree by [G_o:Q]; G_o is nonnormal.

### Prime-to-ell ramification and transfer to every C_o-place

C_o/Q is finite Galois, being the normal closure of the actual
number field G_o in characteristic zero. Audited L092 gives

    [C_o:Q]=1105920=2^13*3^3*5.                         (6)

For every rational p and actual C_o-place w above p, Milne's Galois
degree formula gives [C_o:Q]=e_w f_w g_p, where
e_w=e((C_o)_w/Q_p). Hence e_w divides (6), so the prime ell>=7
does not divide e_w. This includes p=ell and makes no tameness
assumption at any p.

For p in S, equations (2) and (5) therefore imply
ell does not divide h_w=e_w n_p, proving (3) for every w, rather
than only a selected place. At p outside S every h_w is zero, so
there is no additional nonzero height to test in P2 over C_o.

For completeness, if v is the restriction of an actual w to G_o,
the actual completion tower and (5) give, at p in S,

    h_w=e((C_o)_w/(G_o)_v)h_v.

The local ramification factor here divides e_w by multiplicativity,
so it too avoids ell. This checks the transfer in the actual tower
without assuming G_o/Q Galois or identifying distinct completions.
The argument holds for each of the six orderings separately.

### Boundaries of the passing test

If p=ell is a rational pole, the proof gives the same positive
height and coprimality there. It does not exclude that case, and
does not prove an example of an actual selected prime in it. P2
is an explicit premise throughout; simultaneous prime selection
and finite-exception avoidance with the other source clauses have
not been established here. In particular L098-L099's extra
ell-integrality hypothesis has not been removed from those files
or inferred from their conclusions.

Native selected support, full selected/theta data, L092's factor-four
relative degree excess, exact generation/field repairs, the April
reproduction authentication and def= boundary, native input/action,
all-image factorization, marked pilot transport and essentiality
remain unresolved. This result supplies no finite B>=A estimate
and no complete-solution candidate. It is local progress by a known
method, with no claimed advance beyond the inspected sources.

### Separate critical audit — 2026-10-22, step402

**Scope and verdict.** The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-22-literal-p2-transfer-critical-audit.md`.
The conditional implication passes without correction or an additional
direct lemma input. Reuse the precise primary imports above. L089
fixes the survivor, L090 its literal equations and fields, and audited
L092 the degree of their actual normal closures. Fix one arbitrary
survivor and ordering throughout; this covers all six separately.

**Complete torsion and reduction.** For n=3 or 5, E_o[n] is a subgroup
scheme of E_o[15]. In characteristic zero it is finite etale of rank
n^2. The full-coordinate definition of G_o makes all its points
rational, so its decomposition into n^2 rational points persists over
each actual completion of both fields. This verifies full local
torsion, rather than a cyclic subgroup or x-coordinates. Level five
is invertible at p=2,3 and every p>=7; level three is invertible at
p=5. Both are at least three, so IV Proposition 1.8(v) applies to
every complete DVR here, including p=ell, without normality of G_o.
The finite residue fields satisfy Silverman's perfectness hypothesis.
Only after semistability is established do the good/multiplicative
alternatives determine the sign of the j-valuation. Restriction of
integer valuations gives (4) because the same j(E_o)=j(E) is rational.
No identification of different completions or rational twist is used.

**Whole remainder and nonsplit height.** In the split comparison over
L/K, ord_L(q)>0. The entire remainder 744+sum_(m>=1)c_m q^m lies in
O_L: each term is integral, its order tends to infinity, and O_L is
closed. Its valuation is strictly greater than that of q^(-1), also
when the residue characteristic divides 744 or some c_m. Thus the
negative valuation of j is exactly -ord_L(q). GenEll divides the Tate
order by e(L/K), while restriction multiplies ord_K(j) by that same
factor. Their cancellation gives the actual downstairs height
e(K/Q_p)n_p. In the nonsplit multiplicative case Silverman's extension
is unramified quadratic: degree two is not ramification index two.
The height is a positive integer since both factors are positive
integers; good places have height zero. Neither p=ell nor an
ell-division-field height enters as an exception to this calculation.

**All places and actual ramification.** For every rational p in S,
there is a G_o-place v above it. Its positive height is e_v n_p, so
P2 rules out ell dividing n_p. This requires no local-degree
divisibility by a nonnormal global degree. By contrast C_o/Q is
normal and separable, so Milne's Galois efg formula applies at every
actual w. L092 gives 1105920=2^13*3^3*5; hence every e_w divides an
integer prime to the prime ell>=7. This also excludes ell from the
relative index in the completion tower, which divides e_w. Thus
h_w=e_w n_p is prime to ell at all poles; equivalently the actual
tower gives h_w=e((C_o)_w/(G_o)_v)h_v with a prime-to-ell factor.
Outside S all heights are zero and P2 has no nonzero height to test.
A possible pole p=ell is covered by the same argument. The assumption
that ell is prime and at least seven is used in excluding 2,3,5.

**Boundaries.** This verifies precisely the conditional transfer,
not the simultaneous P1–P3 choice, ell-integrality or P4–P7. The
retained mod-seven image does not select the source's prime. L098–L099
remain method comparisons with their extra premises intact. Actual
prime selection, native support/full data, the factor-four relative
excess, exact generation/repair, source-version/def= qualifications,
native input/action/factorization/pilot and essentiality remain open.
No finite B>=A conclusion or advance beyond the checked sources is
claimed. The argument and its three direct inputs are unchanged.

## Mathlib

Full matching and supporting Mathlib coverage have not been checked.
Unknown availability is not absence. This is an informal specialization
with precise source imports, not a formal proof; no mathematical script
or numerical certificate is used. The separate step402 audit above
validates the informal specialization, not a formalization.
