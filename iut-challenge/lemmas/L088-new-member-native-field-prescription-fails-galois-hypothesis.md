# L088 — The new-member native prescription fails the Galois hypothesis

## Hypotheses

Fix exactly the member E=E_star/Q, root ordering r_1,r_2,r_3,
D=r_2-r_1=s^2, parameter t=(r_3-r_1)/D, literal equation

    E_L: V^2=X(X-1)(X-t),
    G_star=Q(t)(iota,E_L[15])

of audited L087, in its fixed algebraic closure Q-bar inside Omega.
Here iota^2=-1, D and s are nonzero, and t is different from 0,1.
Keep both coordinates of every torsion point. Let X be the geometric
once-punctured curve (E_L minus its origin)_Q-bar, without a level
marking. Compute its native F_mod and F_tpd using IUT I Definition
3.1(a),(b) and IUT IV Proposition 1.8(ii),(iii) and Theorem 1.10.
No assumption that G_star already supports initial theta-data is made.

## Conclusion

For this same geometric object, as embedded subfields of Q-bar,

    F_mod=Q,
    F_tpd=Q(E[2])=Q(r_1,r_2,r_3)=Q(t).

The very E_L above is a monic Legendre model over F_tpd, and

    G_star=F_tpd(iota,E_L[15]).

Thus this literal field satisfies the additional generation
prescription displayed in IUT IV Theorem 1.10. For the normal closure
G_star^nor of G_star over F_mod, however,

    [G_star^nor:G_star]=4 != 1.

In particular G_star/F_mod is not Galois, and F=G_star cannot satisfy
IUT I Definition 3.1(b) for X.

The two embedded completions H,N in L087 are unchanged. This is
an admissibility exclusion for this one field and geometric curve,
not a counterexample to either IUT theorem, an exclusion of all
possible choices, or a demonstration of an essential IUT flaw.

## Proof

### Precise imported inputs and source scope

Use the prior SPECIALIZE assessment
`drafts/literature/2026-10-19-new-member-native-field-hypotheses.md`.
The following general results are imported without reproof:

- Mochizuki, *Inter-universal Teichmuller Theory I*, May 2020,
  [Definition 3.1(a)–(c), printed pp.61–62](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf#page=61):
  F contains a square root of -1; F_mod is the field of moduli
  of the once-punctured curve; F/F_mod is required to be Galois
  of degree prime to ell; and full six-torsion must be F-rational.
  Clause (c) separately defines the ell-division extension. These
  clauses do not impose minimal torsion-field generation.
- Mochizuki, *Inter-universal Teichmuller Theory IV*, April 2020,
  [Proposition 1.8(ii),(iii), pp.18–20, and Theorem 1.10,
  p.22](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf#page=18):
  over a perfect field, (ii) describes the j-field and descent;
  when the geometric pointed automorphism group is {+1,-1},
  (iii) makes the two-torsion action independent of descent.
  Theorem 1.10 defines F_tpd as the full two-torsion field of
  any F_mod-model and, in addition to initial theta-data, assumes
  F=F_tpd(sqrt(-1),E_L[15]) for a Legendre model over F_tpd.
  Its abbreviated F_mod/30 notation uses this prescription.
- Milne, *Elliptic Curves*, second edition (2021),
  [I Proposition 4.18 and Remark 4.19, p.38; supporting
  Theorem 6.3, p.42](https://www.jmilne.org/math/Books/EC2.pdf):
  an isomorphism between nonempty opens of nonsingular projective
  geometrically irreducible curves over a perfect field extends
  uniquely to their completions.
- Sutherland, *18.786 Lecture 21*, 6 May 2024,
  [section 21.2, p.2](https://math.mit.edu/classes/18.786/2024/LectureNotes21.pdf):
  in characteristic zero, j different from 0 and 1728 gives
  geometric origin-preserving automorphism group {+1,-1}.
- Milne, *Fields and Galois Theory*, v5.10 (September 2022),
  [Theorem 3.17(b–d) and Remark 3.18,
  pp.39–40](https://www.jmilne.org/math/CourseNotes/FT.pdf):
  finite Galois correspondence and the normality criterion, applied
  inside L087's finite Galois ambient field. This is the same
  finite-Galois input already covered by the audit assessment.

The assessment inspected the author-hosted I and IV versions on
2026-10-19. Byte identity with earlier reproductions and the journal
versions is not asserted. Reuse that source coverage; no fresh
source retrieval or new general moduli theorem is needed. The work
below is the same-member specialization, not a transfer of L079's
different-witness conclusion.

### The same geometric object and its moduli field

L087 constructs the actual inverse pointed maps over Q-bar

    (x,y) -> ((x-r_1)/D, y/(Ds)),
    (X,V) -> (r_1+DX, Ds V).

They identify this E with this E_L, preserving their origins.
Both are nonsingular projective geometrically irreducible curves:
their defining cubics have distinct roots and characteristic is zero.
Their punctured opens are nonempty. Apply Milne's extension result
to an isomorphism between any two geometric conjugates of these
punctured opens, and also to its inverse, over the perfect field
Q-bar. Uniqueness makes the extended maps inverse. Since their
bijection already maps the two open complements onto each other,
it must map the unique omitted point to the unique omitted point.
Conversely, a pointed isomorphism restricts to the punctured opens.
Thus the punctured and pointed geometric moduli problems have the
same isomorphism predicate here; no ordered torsion marking is added.

In particular the Q-defined E is an actual descent of precisely
X's pointed completion. Its j-invariant is rational. The j-field
description in IV 1.8(ii) therefore gives F_mod=Q. This conclusion
uses the same global object and its Q-model, not its completion H
or a moduli field of a level cover.

### The native two-torsion field in this embedding

L087's invariant calculation gives v_3(j(E))=-30. This finite
value excludes j=0; it also excludes j=1728, whose valuation is 3.
The cited characteristic-zero automorphism classification therefore
gives Aut_Q-bar(E,O)={+1,-1}. Both signs act trivially on E[2].
The hypotheses of IV 1.8(iii) hold over the perfect base Q.
Consequently the native two-torsion action may be evaluated using
the actual rational descent E. A different geometric pointed
identification changes it only by a sign on two-torsion, hence does
not change this kernel in the same G_Q.

The nonzero geometric two-torsion points of the given monic model
are exactly (r_m,0), m=1,2,3; the origin is rational. Its full
coordinate field is therefore Q(r_1,r_2,r_3). Substitution in the
definition of F_tpd in IV 1.10 gives

    F_tpd=Q(E[2])=Q(r_1,r_2,r_3).

L087 already proves, for this actual ordering and member,
Q(r_1,r_2,r_3)=Q(t). Import that embedded equality; no new
ordered-level stabilizer calculation is required. This proves
the asserted native fields, including their actual inclusion in
G_star. Rational twisting of E_L is retained throughout.

### Generation and Galoisness are separate tests

The equation E_L is literally V^2=X(X-1)(X-t), with t in the
proved F_tpd and t different from 0,1. Its geometric pointed
comparison with E has already been checked. Substituting the
proved F_tpd=Q(t) into L087's defining generators gives exactly
G_star=F_tpd(iota,E_L[15]), not an abstractly isomorphic field.
This verifies IV 1.10's displayed prescription for this model.

For clarity, iota is already in G_star. Full two-torsion of E_L
is G_star-rational from its three displayed roots, and full
three-torsion is rational because it is contained in E_L[15].
For any P in E_L[6], the identity P=3P-2P expresses it as a sum
of a two-torsion and a three-torsion point. Thus full six-torsion
is rational as well. These checks do not imply the Galois clause.

That clause is over F_mod, not just F_tpd. We have proved
F_mod=Q, and L087's separately audited conclusion is exactly

    [normal_closure_Q(G_star):G_star]=4.

All fields are number fields, so the extension over Q is finite
and separable. A finite separable extension is Galois exactly when
it equals its normal closure. The achieved index four fails the
necessary index-one threshold over the correct base. Therefore
G_star/F_mod is not Galois, independently of the remaining
initial-data clauses or the prime-to-ell degree test. In particular,
no choice of those remaining data makes this literal F=G_star
into initial theta-data for X satisfying Definition 3.1(b).

No field is enlarged in this application. L087's completions are
still the completions of its original G_star and G_star(E_L[7]).
Replacing G_star by its normal closure would be a different target.
IV 1.10 assumes initial theta-data as well as its generation
equality, so an example failing that antecedent does not refute
its conclusion. Corollary 2.2 has further hypotheses not checked
here. Independent initial data on other fields, native input and
action, all-image factorization, marked pilot transport, essentiality,
old-witness questions and original finite B>=A remain unresolved.
This completes a known-method specialization; it claims no new
general result beyond the checked sources. The separate step349
critical audit below validates this application.

### Separate critical audit — 2026-10-20, step349

**Verdict and fixed scope.** The conclusion passes the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-19-new-member-native-field-critical-audit.md`.
The entire proof was checked against the native clauses and methods
recorded in the step346 assessment and step308 source notes, together
with L087's canonical audited conclusions. All uses concern its one
E_star, ordering, E_L, t and literal G_star in the same closure.
The general theorems are reused at the cited versions. No new theorem,
occurrence argument, old-member identification or field enlargement is
needed. The finite Galois citation above makes an existing import
explicit; no claim or hypothesis is repaired or changed.

**Geometric object and moduli base.** The two coordinate maps in the
proof are the actual mutually inverse pointed maps of audited L087.
Separability of the original cubic and t different from 0,1 imply
smooth projective geometrically irreducible genus-one completions in
characteristic zero. Their punctured opens are nonempty. Milne's
extension theorem therefore applies over the perfect field Q-bar to
each open isomorphism and its inverse. The composites are identity
on a dense open, hence on the completions by uniqueness. Their
bijection carries the open onto the open, so it necessarily carries
the complement singleton onto the complement singleton. There is no
unpointed translation freedom left in this comparison. Conversely,
every pointed isomorphism restricts to the punctured curve.

Thus the moduli stabilizers for the unmarked punctured curve and the
pointed elliptic completion agree. In particular the Q-defined E
is a descent of exactly this geometric object. Every element of G_Q
fixes its geometric isomorphism class; the native fixed field is Q,
in agreement with IV 1.8(ii)'s rational j-field. No ordered two-torsion
structure, covering curve or local completion is included in this
moduli object. This checks the field required in I Definition 3.1(b),
not merely a convenient base of definition.

**Two-torsion and embedded fields.** L087's same-member invariant has
v_3(j)=-30. The value is finite and differs from v_3(1728)=3,
so j is neither zero nor 1728. Over characteristic zero Sutherland's
classification gives precisely the two pointed automorphisms +1,-1.
Both fix every point of E[2]. Hence all hypotheses of IV 1.8(iii)
are met over Q. Changing a pointed geometric comparison modifies
the transported Galois action by these automorphisms; their action
on two-torsion is trivial. The entire fixing kernel in the same
G_Q can therefore be computed on the actual rational descent E.
This does not assert that the comparison with E_L is Q-rational.

For the original monic equation, the three nonzero two-torsion points
are exactly (r_m,0) and the fourth is the rational origin. Thus their
full coordinate field is Q(r_1,r_2,r_3), not an x-only surrogate for
higher torsion. L087's audited embedded equality with Q(t) applies
to this ordering and this member. IV 1.10's definition therefore gives
F_tpd=Q(t) inside the fixed closure. No new ordered-level stabilizer
calculation or rationally equivariant Legendre section is assumed.

**Literal generation and failed antecedent.** The stated E_L is already
the monic Legendre equation over this F_tpd. Substitution into the
definition of G_star is an equality of embedded generated fields,
including both coordinates of every point of E_L[15]. The extra IV
prescription is therefore met. The separate checks of iota and full
six-torsion also hold: for P in E_L[6], 3P lies in E_L[2], -2P
lies in E_L[3], and their sum is P. Both summands are rational over
G_star and the group law is defined there. These facts say nothing
about normality over the smaller native field.

Since F_mod=Q, L087's audited normal closure is exactly the closure
required here. Its index is four, whereas a finite separable extension
is Galois only when this index is one. Equivalently, the finite Galois
criterion cited above applies in L087's actual ambient field. No
relative normality over F_tpd can replace normality over F_mod.
Consequently the failed clause excludes this literal F=G_star
regardless of the untested remaining initial-data choices. It does
not exclude other fields, and enlarging to the normal closure would
change the prescribed field. L087's H,N equalities are simply retained;
no new completion theorem is being applied.

**Result and limits.** The audit validates the same-member native
admissibility screen; it finds no mathematical defect in L088. This
is verification of a known-method specialization, not a new general
result or a counterexample to IUT. Theorem 1.10 assumes initial
theta-data in addition to its generation equality, so this object
fails an antecedent. Corollary 2.2's independent hypotheses and exact
quantifiers remain untested. Independent initial data, actual native
input/action, all-image factorization, marked pilot transport,
essentiality, old-witness questions and original finite B>=A remain
open. The argument assembly and direct mathematical input are unchanged,
so PROOF and DAG need no edit. This canonical verdict supersedes only
the overview's pending-audit wording for L088.

## Mathlib

Full matching and supporting Mathlib coverage for this native-field
application has not been checked. Unknown availability is not
absence. The general inputs above are precisely cited imports;
the same-member hypothesis checks are informal and not formalized.
