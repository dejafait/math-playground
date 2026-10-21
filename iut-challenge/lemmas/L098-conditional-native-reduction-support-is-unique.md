# L098 — Conditional unique rational support for the reduction predicates

## Hypotheses

Fix any survivor E/Q of audited L089, retaining its fixed
c,h,d_*,e_*, both domains and algebraic closure. Use the six literal
ordered-root Legendre curves and full-coordinate fields of audited
L090. For any one ordering o put

    T=Q(E[2])=Q(t_o),
    E_o: V^2=X(X-1)(X-t_o),
    G_o=T(iota,E_o[15]), iota^2=-1, C_o=G_o^nor over Q.

All coordinates of all geometric 15-torsion points are included.
In particular C_o contains G_o. The rational invariant j(E) is
nonzero, is the invariant of every E_o, satisfies v_2(j(E))>=0,
and has v_3(j(E))=-30 by L089's same-member local retention.
Use the absolute valuations v_p(p)=1 and their extensions.

Assume additionally that ell>=7 is a prime and

    v_ell(j(E))>=0.                                      (1)

This is an extra conditional hypothesis, not a conclusion about the
prime eventually selected by an IUT height argument. Set

    S={rational primes p : v_p(j(E))<0}.

No native initial theta-data for C_o, selected place section,
q-order coprimality, or exact-generation repair is assumed.

## Conclusion

For every actual finite place w of C_o above any rational prime p,
the unchanged E_o/(C_o)_w is semistable, and

    good reduction           iff p is outside S,
    multiplicative reduction iff p belongs to S.          (2)

Multiplicative reduction need not be split. In particular S is a
finite nonempty set, contains three, and avoids two and ell.

It is the unique nonempty rational-prime support U avoiding two
and ell with both of the following properties:

- E_o has multiplicative reduction at every C_o-place above U;
- E_o has good reduction at every C_o-place over a rational prime
  outside U and different from two and ell.

No prior finiteness assumption on U is necessary. This proves only
the stated reduction/support bridge under (1), using known reduction
theorems. It supplies no complete native initial data or essential
IUT flaw, and leaves original finite B>=A unresolved. The separate
step393 critical audit below validates this conditional specialization.

## Proof

### Imported results, source qualifications and scope

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-21-conditional-native-support-bridge.md`.
Its target is exactly the conditional support assertion above.
The scoped comparison with L089, L090, L096, L097 and step389 found
the reduction inputs but no prior proof of this support assertion.
L096's ramification result and L097's weighted inequality are not
mathematical premises here. ATTEMPTS/035 is not reopened.

Import Mochizuki, *Inter-universal Teichmuller Theory IV*, April
2020 [inspected reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
Proposition 1.8(v), printed p.19 and full proof p.20: over a complete
discretely valued field, full rational prime-level torsion of level
at least three invertible in the valuation ring gives semistable
reduction. This is the general torsion criterion, not the odd-residue
Legendre-only statement of part (vi). It permits nonsplit
multiplicative reduction. The general theorem is not reproved.

Import Silverman, *The Arithmetic of Elliptic Curves*, second edition
(2009), [VII.5.5, statement and proof pp.197–199](https://studylib.net/doc/28155304/the-arithmetic-of-elliptic-curves):
including the residue-two proof A.1.3 and A.1.4(b), pp.412–413:
over a complete discretely valued field with perfect residue field,
integral j is equivalent to potential good reduction, including
residue characteristic two. In its semistable reduction cases,
good reduction has integral j and multiplicative reduction has
negative j-valuation. Explicitly, the imported minimal-model
criteria give a unit discriminant in the good case and unit c4
with positive discriminant valuation in the multiplicative case;
j=c4^3/Delta gives these signs. Thus a semistable curve is good
exactly when j is integral. No implication from potential good
reduction to good reduction for an arbitrary twist is used.

For context only, the reduction predicates being compared are
IUT I, May 2020 [reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf),
Definition 3.1(b),(c), pp.61–62, and IV Theorem 1.10 opening,
p.22: selected multiplicative places exclude residue characteristic
ell, and complementary good reduction is required away from 2ell.
These predicates do not constitute all initial-data conditions.
The I/IV reproductions have not been authenticated against current
author/journal bytes. This qualification remains in force.

The main gap remains original finite B>=A. This intermediate target
could identify the rational support in L097's reduced divisor with
the support required by these reduction predicates, subject to (1).
Its pass test is classification at every actual place, nonemptiness
and both exclusions, and both directions of uniqueness. A failed
case would stop the assertion without changing its hypotheses.

### Full torsion and semistability at every actual completion

Fix an arbitrary survivor, ordering o and finite place w|p of C_o.
Write K=(C_o)_w. This is a finite extension of Q_p: it is complete
and discretely valued, has characteristic zero and finite perfect
residue field. Its embedding of C_o is the one defining w; no
selected completion or identification between different w is used.

For n=3 and n=5, E_o[n] is contained in E_o[15]. By construction
every coordinate of every such geometric point lies in G_o and
hence C_o. After the completion embedding, these are still the
entire geometric n-torsion sets over K. Indeed [n]'s kernel in
characteristic zero is a finite etale scheme of degree n^2. Its
base change to an algebraic closure of C_o is the disjoint union
of its n^2 points, all already C_o-rational here. Base change along
C_o -> K preserves that disjoint union and its points. Equivalently
the resulting n^2 distinct K-rational points exhaust the local
geometric n-torsion. This checks full torsion rather than one point,
one cyclic subgroup, or x-coordinates alone.

If p is not five, use n=5 in IV 1.8(v). Then n>=3, n is prime,
and n is a unit in O_K; this includes p=2 and p=3. If p=5,
use n=3, again a prime unit of level at least three, with its full
torsion rational over K. The cited theorem therefore proves
semistability of the same E_o/K in every case, without changing K.

### Classification by the rational invariant

L090's pointed geometric comparison gives j(E_o)=j(E) in Q for
each ordering. Consequently at the chosen w its absolute valuation
is exactly v_p(j(E)). If ord_w instead denotes the surjective
integer valuation, then

    ord_w(j(E_o))=e(K/Q_p) v_p(j(E)),

so its sign is unchanged. Semistability has already been established
for this actual E_o/K. The imported reduction cases now give good
reduction if and only if v_p(j(E))>=0, and multiplicative reduction
if and only if v_p(j(E))<0. The two cases exhaust semistable
elliptic reduction and are mutually exclusive. This proves (2)
for every w, independently of its ramification index or the other
places over p. No mere potential-good verdict is substituted for
actual good reduction.

### Existence and uniqueness of the support

The nonzero rational number j(E) has negative valuation at only
finitely many primes, so S is finite. Its valuation at three is
-30 by L089, hence three belongs to S and S is nonempty.
Dyadic integrality from L089 excludes two. Hypothesis (1) excludes
ell, and ell>=7 also distinguishes it from three. Applying (2)
at every actual place proves that U=S has multiplicative reduction
over its entire inverse image and good reduction on its complement,
in particular on the complement away from 2ell. Thus it satisfies
all predicates in the conclusion.

Conversely let U be any support satisfying those predicates and
avoiding two and ell. For p in U, choose a C_o-place w above p;
such a place exists since C_o is a number field. Multiplicative
reduction there and (2) force p in S. Thus U is contained in S.
For p in S, the exclusions already proved give p different from
two and ell. If p were outside U, the complementary predicate
would give good reduction at every w|p. Choose one such w.
But (2) gives multiplicative reduction there, a contradiction.
Hence S is contained in U. These two inclusions prove U=S, with
no finiteness assumption on U and with no ignored exceptional prime.

### Remaining limitations

The bounded test passes under exactly the additional ell-integrality
assumption (1). This is a same-member specialization of known
reduction theory, not progress beyond the sources checked. The
result does not assert (1) for the actual height-selected prime,
q-order coprimality at all places, stable pointed or full theta-data,
or the native exact-generation prescription for C_o. It does not
remove L092's factor-four relative excess. Native input/action,
all-image factorization, marked pilot transport, essentiality,
source authentication and original finite B>=A remain unresolved.
No prime-seven substitution or complete-solution candidate is made.

### Separate critical audit — 2026-10-21, step393

The invocation-start assessment is
`drafts/literature/2026-10-21-conditional-native-support-audit.md`
(SPECIALIZE). This audit reuses its inspected theorem coverage, including
the residue-two proof just cited. It does not retrieve or authenticate
the IUT reproductions again. L089 and L090 are the only direct lemma
inputs; L096 and L097 supply neither semistability nor support uniqueness
here. No new general reduction theorem is needed or reproved.

**Same member and every ordering.** L089's conclusion retains the local
height-30 property for each survivor; its uniform invariant calculation
gives a nonzero rational j with v_2(j)>=8 and v_3(j)=-30. The pointed
geometric maps in L090's arbitrary-member proof identify j(E_o)=j(E)
for each ordering. They need not descend to T or C_o: invariance of j
is geometric. The six equations are nonsingular because their parameters
avoid zero and one. C_o contains the actual full-coordinate field G_o,
not a field generated only by x-coordinates. Thus these inputs apply to
the very curve used throughout this proof, with no reselection.

**Full local torsion and all residue cases.** For each n in {3,5}, the
kernel scheme E_o[n] over C_o is already a disjoint union of n^2 copies
of Spec(C_o): characteristic zero makes it etale, and all its geometric
points are rational by the field prescription. Base change along the
actual C_o-to-K completion map therefore gives n^2 copies of Spec(K).
This avoids any need to embed an entire algebraic closure into K. The
origin remains rational and the n^2 sections remain distinct. The local
field K has all the completeness and perfect-residue-field hypotheses
of the imported reduction theorems. The assignments are level five at
p=2, p=3, and all p>=7; level three at p=5. In every case the level is
prime, at least three, and invertible in O_K. IV 1.8(v) applies to the
same curve over K itself. Neither a new extension nor splitness follows
or is required. In particular the dyadic case does not use IV 1.8(vi).

**Reduction and valuation signs.** The imported semistable alternatives
are good and multiplicative. In a minimal integral model, the good case
has unit discriminant and integral c4, whereas the multiplicative case
has unit c4 and positive discriminant order. Thus the cited reduction
criteria and j=c4^3/Delta distinguish the signs in every residue
characteristic. These are the known reduction cases used in the
inspected VII.5.5 proof; the residue-two coverage is retained explicitly
above. The proof never upgrades potential good reduction alone to good
reduction. Since j is rational, the extension of the absolute valuation
has the same value v_p(j); the integer valuation multiplies it by the
positive integer e(K/Q_p). Consequently (2) holds simultaneously for
every actual w, even when its local degree differs from another place.

**Support existence, exclusions and both inclusions.** Rationality and
j!=0 give finite pole support; v_3(j)=-30 makes it nonempty. Dyadic
integrality excludes two, and only the explicit premise (1) excludes
ell. Thus S itself satisfies the two reduction predicates by (2).
For any admissible U and p in U there is a place of the number field
C_o above p. Its required multiplicative reduction forces p in S.
Conversely, for p in S, the two established exclusions put p outside
{2,ell}. If p were omitted from U, the complementary condition would
force good reduction at an existing w|p, contrary to (2). This verifies
S subset U without applying the complementary condition at an exempt
prime. No assumption on the size of U or selected-place section is
hidden in either implication.

**Verdict and limits.** All stated tests pass under the original
hypotheses, including (1). This makes L098 a checked conditional input
for a later support comparison; it is verification of a known-method
specialization, not progress beyond the checked sources. It proves no
ell-integrality for the actual height-selected prime and no q-order
coprimality. L092's relative excess, exact generation, full native data,
the source-version/def= boundary, actual input/action/factorization/pilot,
essentiality and finite B>=A remain unresolved. The argument and its
direct mathematical inputs are unchanged, so PROOF.md and DAG.md are
unchanged; this canonical audit supersedes their pending-audit wording
for L098 only. No complete-solution candidate is asserted.

## Mathlib

Full matching and supporting Mathlib coverage have not been checked.
Unknown coverage is not absence. The proof imports the cited general
reduction theorems and verifies the actual-place specialization and
support implications informally; no mathematical script, numerical
certificate or formal verification is used.
