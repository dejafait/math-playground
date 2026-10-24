# L109 — Split Tate comparison over every selected completion

## Hypotheses

Retain all the fixed objects and hypotheses of L108: L105's one member,
ordering o, curve E_o, fields G_o,C_o and selected prime ell>=7; the full
coordinate field K=K_C=C_o(E_o[ell]); L107's one fixed line
U subset E_o(K)[ell] and its unchanged cover; and L108's audited section
s over F_mod=Q. Write Sigma=S minus {ell}, where
S={p:v_p(j(E_o))<0}. In particular Sigma contains three and excludes
two and ell. Use the actual completion embedding i_w:K -> K_w.

No splitness over C_o, descent of U to C_o, ell-integrality of j,
normality of K/Q, initial theta-data or IUT III situation is assumed.
The source-version/authentication and def= qualifications inherited
from L108 remain in force. The invariant j is nonexceptional, as in
L108, and every field in the argument has characteristic zero.

## Conclusion

For every p in Sigma, put w=s(p) and k=K_w. The unique small Tate
parameter q_w of (E_o)_k belongs to this unchanged k, and there is a
pointed algebraic k-isomorphism

    f_w:E_(q_w) -> (E_o)_k,    0<|q_w|<1.

Consequently (E_o)_k has split multiplicative reduction. For the
Galois-equivariant Tate parametrization phi_(q_w), the equality of
actual embedded subgroups is

    f_w(phi_(q_w)(mu_ell)) = i_w(U).                    (1)

The equality holds for every pointed comparison f_w over k, without
choosing a generator of U or a normalization of a cusp coordinate.
All parameters, comparisons and equalities here are local to the stated
completions; no number field, member, prime, place, U or global cover
is replaced. The separate step443 critical audit below validates this
known-method specialization. It supplies no stable log model, arithmetic graph-cover
kernel, common cusp sign, theta splitting or original finite B>=A bound.

## Proof

### Imports, duplicate screen and test

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-24-selected-completion-split-tate-prerequisite.md`.
Reuse its completed theorem/duplicate/failure comparison and step440
source notes. L108 already gives comparison-independent geometric
Tate lines, complete local torsion rationality and their equality with
U at s(p). It does not descend a pointed comparison. L056–L057 are
methods on different objects, not conclusions used here. ATTEMPTS/030
and /031 remain parked: neither a rank-two multiplication cover nor
an unverified marked-coordinate normalization is used.

Import the following known results with their hypotheses:

- Tate's uniformization and splitness criterion, in Kedlaya,
  [*Introduction: the Tate curve*, fall 2004](https://kskedlaya.org/18.727/tate-curve.pdf),
  Theorems 1–2, pp.3–4; see also the torsion description in the
  proof of Proposition 3, p.5. Over a finite p-adic field, a curve
  with |j|>1 has a unique small q and a geometric pointed comparison
  with the standard Tate curve. Its multiplicative parametrization
  is a Galois-equivariant group surjection with kernel q^Z, over
  the algebraic closure and over every finite extension. A base-field
  comparison is equivalent to split multiplicative reduction.
  Theorems 1 and 2 cite Silverman, *Advanced Topics in the Arithmetic
  of Elliptic Curves*, V.3.1/V.4 and V.5.3. We import these theorems,
  not the handout's printed a4 coefficient or its transvection claim;
  no valuation-coprimality assumption from Proposition 3 is used.
- Pointed nonexceptional twist classification over a field, in
  Sutherland, [MIT 18.786 Lecture 21, 6 May 2024](https://math.mit.edu/classes/18.786/2024/LectureNotes21.pdf),
  section 21.2, p.2. For j!=0,1728 the pointed automorphism group is
  {+1,-1}, with trivial Galois action. Twists are classified by
  continuous characters into this group, and the trivial character
  gives a base-field isomorphism. Here k is perfect of characteristic
  zero, and the pointed elliptic category is used, retaining origins.

The indicated source statements and relevant cases were rechecked in
this step within the saved coverage. The only specialization to prove
is that the actual full torsion forces the character trivial, followed
by (1). There is no reproof of uniformization or twist classification.

The main gap is original finite B>=A. The bounded intermediate test is
same-completion descent, potentially useful for later actual-model and
arithmetic graph-kernel comparison. Continue if the character vanishes
at every selected completion without changing fields or U; a surviving
character would stop or narrow this route. Graph kernels, sign/splitting,
III/P7, exact generation/full repair, relative factor-four excess,
actual input/action/factorization/pilot and essentiality remain separate.

### Full local torsion and the comparison cocycle

Fix an arbitrary p in Sigma and write w=s(p), k=K_w, E=(E_o)_k.
This is a finite extension of Q_p. Since j(E_o) is rational with
v_p(j)<0, its image has negative valuation in k. Tate's theorem
therefore supplies q=q_w in k and a geometric pointed isomorphism
f:E_q -> E over an algebraic closure kbar. Its j is not 0 or 1728.

Every geometric ell-torsion point of E is k-rational: the ell^2
points in E_o(K)[ell] remain distinct after the injective completion
embedding and exhaust the geometric ell-torsion, which has cardinality
ell^2 in characteristic zero. Thus every sigma in G_k fixes every
point of E[ell]. This uses the full coordinate field, rather than
rationality of U alone.

For sigma in G_k set

    c_sigma=f^(-1) composed with sigma(f) in Aut(E_q,kbar).

Both curves are defined over k. The imported pointed classification
identifies c_sigma with a scalar epsilon_sigma in {+1,-1}, and these
scalars form the continuous twisting character. For P in E_q[ell],
its image f(P) is in E[ell] and is fixed by sigma. Hence

    f(P)=sigma(f(P))=sigma(f)(sigma(P))
        =f(epsilon_sigma sigma(P)),

so, by injectivity of f and epsilon_sigma^2=1,

    sigma(P)=epsilon_sigma P,  for every P in E_q[ell].  (2)

The action in (2) is on the entire rank-two torsion, not merely its
toric line. We have not presumed that f is defined over k or that
Tate representatives of rational classes are fixed.

### The parameter-exponent quotient detects the character

Use the imported equivariant group isomorphism

    kbar^times/q^Z -> E_q(kbar).

A representative u of an ell-torsion class satisfies u^ell=q^m
for a unique integer m: the power belongs to q^Z, and q has infinite
order because |q|<1. Replacing u by u q^a replaces m by m+ell a.
Consequently

    e:E_q[ell] -> Z/ell Z,    e(phi_q(u))=m mod ell      (3)

is well-defined. Multiplication of representatives adds m, so e is
a group homomorphism. It is onto: choose any Q in kbar with Q^ell=q;
then e(phi_q(Q))=1. Its kernel is exactly phi_q(mu_ell): if m=ell a,
then (u q^(-a))^ell=1, and the converse follows by taking m=0.
The map on mu_ell is injective, since its intersection with q^Z is
{1}. This describes the standard Tate torsion quotient explicitly,
only to check its action for the present specialization.

For every sigma in G_k, q is fixed, and
(sigma(u))^ell=sigma(q^m)=q^m. Equivariance of phi_q thus gives

    e(sigma(P))=e(P),  for all P in E_q[ell].            (4)

In particular the quotient in (3) has trivial G_k-action. Combining
(2), (3) and (4) at P=phi_q(Q) gives

    1=e(sigma(P))=e(epsilon_sigma P)=epsilon_sigma
      in Z/ell Z.

Since ell>=7 is odd, -1 and +1 are distinct modulo ell. Therefore
epsilon_sigma=+1 for every sigma. This excludes a nontrivial local
quadratic twisting obstruction without any change of k. In particular
it does not infer a trivial twist merely from rationality of a
geometrically chosen toric line; the nonzero exponent quotient is
essential to this calculation.

The twisting character is trivial, so the imported classification
provides a pointed k-isomorphism f_w:E_q -> E. Equivalently, the
chosen f has c_sigma=1 for all sigma, hence is itself G_k-invariant
and descends in the pointed category. Tate's splitness criterion now
gives split multiplicative reduction over this actual completion.
It was not assumed over the downstairs field C_o.

### Equality with the one fixed U and the all-place quantifier

By L108, the actual subgroup i_w(U) equals the image of mu_ell
under phi_q and any geometric pointed comparison E_q -> E.
The k-isomorphism f_w just obtained is one such comparison. Applying
that comparison-independent equality proves (1), as a subgroup of
E(k)[ell]. It also proves (1) for every other pointed k-comparison;
no choice of basis, an abstract character isomorphism or mere dimension
comparison replaces this equality.

The argument applies to each arbitrary p in the finite set Sigma,
using its already selected w=s(p). Each completion has its own unique
small parameter; no simultaneous field adjunction or common parameter
is required. L108's s, the global U and the cover remain fixed. Thus
every selected completion passes the exact bounded test.

This closes only the same-field split comparison prerequisite. No
model extension or equality of arithmetic graph-cover kernels has been
constructed, and no assertion about a common cusp generator or theta
splitting follows. The independent native-data, field-repair,
factor-four, actual-input/action/pilot, source-qualification and
essentiality gaps, and the main finite B>=A problem, remain unresolved.
The result is local progress by the checked known methods, with no
claim of progress beyond the sources compared or a complete candidate.

### Separate critical audit — 2026-10-24, step443

**Scope and sources.** The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-24-selected-completion-split-tate-critical-audit.md`.
This REPRODUCTION audit checks the entire proof above and the actual
geometric-line/section conclusions and step439 audit of L108. Reused
the recorded duplicate and failure comparison; no new result is sought.
Rechecked the cited Kedlaya Theorems 1–2, pp.3–4, their group-law and
equivariance discussion, and the torsion description on p.5; rechecked
Sutherland section 21.2, p.2. These cover the characteristic-zero
local field, pointed nonexceptional automorphisms and twist descent.
Proposition 3's coprimality hypothesis and inertia conclusion are not
used. No printed coefficient formula, local ramification calculation,
new source authentication or unpublished source identity is needed.

**Local hypotheses and complete torsion.** For each p in Sigma,
w=s(p) is an actual place of the unchanged finite number field K.
Its completion k is a finite extension of Q_p. Negative rational
j-valuation persists under this completion, so the unique small
parameter lies in k before any descent of f is asserted. L108 retains
j!=0,1728. In particular the residue characteristic three causes no
exception to the characteristic-zero automorphism assertion.
The finite etale group E_o[ell] has ell^2 geometric points. Both
coordinates of all these points belong to K, and an injective field
map preserves their distinctness and the origin. Their images exhaust
the local geometric torsion, proving trivial action of the entire
G_k on E[ell]. Merely knowing that U is rational would not suffice.

**Cocycle direction.** Both source and target of f are defined over k,
so c_sigma=f^(-1)sigma(f) is a pointed automorphism of the source.
One has sigma(f)=f c_sigma, not c_sigma f. Also
c_(sigma tau)=c_sigma sigma(c_tau); the trivial action on {±1}
makes this a character. The isomorphism is defined over a finite
extension, so the character is continuous. For every P in E_q[ell],
the rationality just proved gives
f(P)=sigma(f)(sigma P)=f(c_sigma(sigma P)). Cancelling f gives
sigma P=c_sigma^(-1)P=epsilon_sigma P. Thus equation (2) has the
correct direction and concerns the whole torsion module. It does not
assume equivariance of the geometric comparison f.

**Complete exponent quotient.** Uniformization identifies every
ell-torsion point with a class [u] satisfying u^ell in q^Z.
Since q has infinite order, its exponent m is unique. Every other
representative is u q^a for an integer a, changing m by exactly
ell a. Thus (3) is independent of the representative, including the
identity class. Multiplication adds exponents, inversion negates
them, and an algebraic ell-th root Q of q gives a class of image 1.
No rationality of Q is required. If the image is zero, dividing u
by the corresponding integer power of q gives an ell-th root of
unity; conversely every such root has image zero. The root-of-unity
map is injective because no nonidentity q-power has absolute value
one. This verifies the full quotient, not just a chosen pair of points.

For each sigma, q is fixed and sigma(u)^ell=q^m with the same integer
m. Equivariance of the parametrization therefore proves (4) on every
class. Applying it to [Q] and using the scalar action gives
1=epsilon_sigma in Z/ell Z. Oddness of ell separates the two signs,
so every c_sigma is the identity. The proof has neither lifted a
fixed class to a fixed representative nor assumed a rational radical.
It makes no use of a coprime q-order in this full division completion.

**Descent and exact subgroup.** The trivial character supplies an
isomorphism over k by the cited twist classification; equivalently
sigma(f)=f for every sigma. The splitness criterion then applies
over this k itself. L108 equations (1), (2), (5) identify i_w(U)
with the toric subgroup for every geometric pointed comparison at
this particular selected w. The descended f is such a comparison.
Any other pointed comparison differs by ±1 and hence has exactly
the same subgroup image. This proves literal equality (1), not an
abstract isomorphism of lines, a generator equality or a cusp sign.
The reasoning applies separately to every p in Sigma with its
already fixed s(p); no global field, place section or U is replaced.

**Verdict.** L109 passes with its hypotheses, conclusion, proof method
and sole direct input L108 unchanged. The audit validates a relevant
local prerequisite by known methods, with no claim beyond the sources
compared. This supersedes the pending-audit wording for L109 in the
unchanged overview. Stable log models and arithmetic graph kernels,
the double-dot predicate, common cusp sign and theta splitting,
III/P7, exact-generation/full repair, relative factor-four excess,
actual input/action/factorization/pilot, source qualifications,
essentiality and original finite B>=A remain unresolved. There is no
complete candidate. No new mathematical script or lemma is needed.

## Mathlib

Full matching and supporting Mathlib coverage for this exact-object
specialization has not been checked. Unknown availability is not
absence, and no formal verification is claimed. Tate uniformization,
the splitness criterion and twist classification are imported above;
the local full-torsion/quotient calculation is the covered REPRODUCTION.
Step443 validates the informal specialization; it does not supply
formal verification or additional Mathlib coverage.
