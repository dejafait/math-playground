# L101 — Same-member simultaneous P1–P3 selection

## Hypotheses

Retain audited L089's fixed family, algebraic closure, domains K_V
with support {infinity,2}, and all its survivor conditions. Use
L090's literal full-coordinate fields, with no replacement by a
normal closure when defining the source height:

    T=Q(t_o)=Q(E[2]), E_o: V^2=X(X-1)(X-t_o),
    F=G_o=T(iota,E_o[15]), iota^2=-1, C_o=G_o^nor over Q.

Fix d=6, epsilon_d=1 and delta=3317760. Let Exc be any fixed
finite subset of U(Q-bar), U=P^1 minus {0,1,infinity}; it may contain
the inspected corollary's finite exceptional set. The domains and
Exc are fixed before selecting a survivor. Every division field
adjoins both coordinates of every geometric torsion point.

The source convention is the qualified April 2020 IUT IV reproduction
and explicit Legendre-adjunction reading of L091. Import only the
prime-selection subargument preceding P4–P7, not the disputed claim
that this F supplies initial theta-data. Authentication against current
author/journal bytes and the alternative independent ordinary
F_mod-model division-field reading remain outside the application.

## Conclusion

There is one survivor E/Q such that all six t_o avoid Exc. For any
one fixed ordering of that same member, define the actual downstairs
GenEll integer curve heights h_v at all finite F-places and

    H=(1/[F:Q]) sum_v h_v f_v log(p_v),

where f_v is the residue degree over the rational prime p_v. There
is a prime ell>=7 for this F satisfying simultaneously

    sqrt(H)<ell<=10 delta sqrt(H) log(2 delta H),          (P1+)
    ell divides no nonzero h_v at any finite F-place,     (P2)
    h_v<sqrt(H) at every F-place over ell.                (P3)

The strict lower inequality retains the source construction's S1
exclusion, strengthening its displayed weak P1. This ell discharges
L100's premise for the same E,o,F,C_o. Hence ell avoids every rational
pole order of j(E), and every nonzero curve height over C_o is prime
to ell, including at p=ell if it is a pole.

This is an existential known-method specialization. The separate
step406 critical audit below validates it within the stated source
qualifications. It gives no explicit coefficients or prime,
no prime common to six orderings, no ell-integrality, P4–P7 or complete
normal-closure repair, and no essential IUT flaw or finite B>=A result.

## Proof

### Imports, overlap and bounded test

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-22-same-member-simultaneous-prime-selection.md`.
Its inspected general sources are imported, not reproved:

- Mochizuki, *Inter-universal Teichmuller Theory IV*, April 2020,
  [87-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
  Proposition 2.1(ii), printed p.40, and Corollary 2.2(ii)'s proof,
  pp.44–45 through S1–S3 and P1–P3: for the nonnegative integer
  semistable heights, [F:Q]<=delta and sqrt(H)>=xi_prm>=5, the
  construction chooses a prime outside the union of S1 (primes
  <=sqrt(H)), S2 (prime divisors of nonzero h_v) and S3 (residue
  primes of places with h_v>=sqrt(H)), with the upper bound in
  (P1+). These are one simultaneous construction. Its proof uses
  the normalized height sum, not Galoisness of F/Q or P4–P7.
  The constants and degree use also occur in Theorem 1.10's proof,
  (E3)–(E5), p.24, and the corollary's proof p.44. Corollary 2.2(i),
  pp.41/43, provides the source's bounded-discrepancy height
  comparison; the exact finite-height specialization below makes
  that comparison explicit for these rational j-values instead of
  treating coefficient size as H.
- Silverman, *Canonical Heights on Abelian Varieties*, AWS notes,
  dated 13 February 2024,
  [Definitions 4.4–4.5 and Proposition 4.6, pp.13–14; Theorem 4.8(d), p.15](https://swc-math.github.io/aws/2024/2024SilvermanNotes.pdf#page=13):
  absolute logarithmic height and independence of its computing
  number field, and Northcott finiteness for bounded absolute height
  and bounded degree with an ample divisor on a smooth projective
  variety over a number field. Apply the latter only to P^1/Q
  with O(1), not to a nonproper open curve or the torsion fields.
- Mochizuki, *Arithmetic Elliptic Curves in General Position*,
  Math. J. Okayama Univ. 52 (2010),
  [Definition 3.3 and Remark 3.3.1, p.17](https://www.math.okayama-u.ac.jp/mjou/mjou52/_01_mochizuki.pdf#page=17):
  the local curve-height convention. Its application, including
  nonsplit multiplicative reduction and all residue characteristics,
  is already proved and separately audited in L100.

L089 supplies infinitely many distinct moduli in fixed domains;
L090 identifies each literal field; L091 proves the same-member
finite-set avoidance mechanism; L092 gives the actual field degree;
L100 gives its actual local heights and the conditional transfer.
None has already made the simultaneous prime choice. L098–L099's
extra ell-integrality is not assumed or deleted. ATTEMPTS/035's
authentication/repeated-approval mechanism remains parked.

The main gap remains original finite B>=A. This intermediate result
could remove L100's conditional P2 premise for a possible field repair.
Continue only if the fixed exceptional set is finite before the member,
the source height is computed over literal G_o, and the same prime
meets all three clauses with ell>=7. A failed field, normalization or
height-threshold hypothesis stops this application. Relative degree
excess and integrality/native support are independent unresolved steps.

### The actual normalized height, before choosing a survivor

Consider any survivor and any ordering, temporarily, to obtain a
uniform calculation before fixing the low-height exception. Put
j=j(E_o)=j(E) and S={p:v_p(j)<0}. L089 gives j in Q and
0<j<1728. By L100's audited reduction and height calculation,
E_o is semistable at every finite F-place and

    h_v=max(0,-ord_v(j))
       =e(F_v/Q_p) max(0,-v_p(j)) for v over p.           (1)

Here ord_v is surjective onto Z. Good places have height zero;
the positive multiplicative heights are genuine integers even in
the nonsplit case. This part of L100's proof precedes, and does
not use, its conditional P2 hypothesis. Full level five is used
away from p=5 and full level three at p=5. Thus it applies before
ell has been chosen and requires neither F/Q normal nor initial data.

Since log Norm(v)=f_v log(p_v), substituting (1) in H identifies it
with the finite-place part of the absolute logarithmic height of j,
computed over F. Every archimedean embedding of F sends the rational
j to itself. With the standard real/complex local weights summing
to [F:Q], field independence of the cited height therefore gives

    h_abs(j)=H+log max(1,|j|).                            (2)

More concretely, write j=a/b in coprime integers with b>0. The
finite part is log b, so

    H=log b=sum_(p in S)(-v_p(j))log p,
    h_abs(j)=log max(|a|,b)=H+log max(1,|j|).             (3)

This is the absolute height formula, not an estimate from the size
of the original cubic coefficients. It uses all actual F-places
with their residue weights; it does not replace them by a selected
place or assume equal ramification indices. In particular H is
the source's height over literal G_o, although (3) shows it is
independent of the ordering in this family. From 0<j<1728<2000,

    H<=h_abs(j)<H+log 2000.                              (4)

### A fixed finite low-height exception and the same member

Fix the absolute source constant xi=xi_prm>=5. Before selecting a
survivor, define the parameter set

    Exc_low={t in U(Q-bar): [Q(t):Q]<=6,
                       h_abs(J(t))<=xi^2+log 2000},
    J(t)=256(t^2-t+1)^3/(t^2(t-1)^2).

This is finite. Indeed J is Q-defined, so
[Q(J(t)):Q]<=6. Northcott on P^1 with O(1) makes the possible
values J(t) in this bounded-height, bounded-degree range finite.
L089's displayed degree-six morphism J:P^1->P^1 has finite fibers:
for a finite value z its polynomial equation is

    256(t^2-t+1)^3-z t^2(t-1)^2=0,

a nonzero degree-six polynomial. Hence each of those finitely many
finite values has at most six preimages in U. No uniform statement
about the degrees of the torsion fields is needed for this finiteness.

Set Exc_total=Exc union Exc_low. This finite set is fixed after
the domains, d,epsilon_d and xi, but before the member. Apply L091's
finite-avoidance conclusion to Exc_total (or its degree-at-most-six
part, which is all that can contain a survivor parameter). There
is a single L089 survivor E whose six parameters all avoid this
set: its rational j is chosen outside the finite J-image of that set.
No change of domains or of the original family is made.

Fix any one ordering of this member, and henceforth keep its actual
E_o,T,F,C_o. If H<=xi^2, (4) would give
h_abs(J(t_o))<=xi^2+log 2000, putting t_o in Exc_low, a
contradiction. Consequently

    H>xi^2, sqrt(H)>xi>=5.                              (5)

This proves the required threshold for the same selected member,
after all finite exceptions have been fixed. It does not infer
unbounded H merely from infinitely many equations or from the
congruence modulus 3^M.

### One prime and the conditional normal-closure transfer

L090 makes F exactly the prescribed full-coordinate Legendre
adjunction for this member, and the parameter has degree at most
d=6 in the fixed K_V. L092 gives the distinct field-degree check

    [F:Q]=276480=delta/12<=delta=3317760.                 (6)

All heights are the nonnegative integers (1), and their support
is finite since j is a fixed nonzero rational number. Thus S1,
S2 and S3 in the cited construction are finite. Conditions (5),
(6) and the actual normalized height sum verify the inputs to
the inspected prime-selection subargument. Apply that subargument
by citation to obtain one ell outside S1 union S2 union S3 and
within the upper bound in (P1+); no prime-counting theorem is reproved.

Exclusion from S1 gives ell>sqrt(H)>5. As ell is prime, ell>=7.
Exclusion from S2 says exactly P2 over this F for every nonzero
h_v. Exclusion from S3 says every F-place over ell has
h_v<sqrt(H), exactly P3. All three hold for this one prime and
this unchanged field. The printed weak lower P1 alone is not
used to exclude the possible endpoint ell=5.

Now, and only now, apply L100 with this actual prime. Its hypotheses
are the same survivor/order/fields, audited L092's normal-closure
degree, ell>=7 and P2 over G_o, all verified above. It follows
that ell avoids every rational pole order and every nonzero C_o
height. This transfer asserts neither P1 nor P3 over C_o; the source
selection and H still belong to G_o. A possible pole at p=ell
is covered by L100 and is not excluded by P3's positive upper bound.

The passing test supplies an actual existential simultaneous
selection, rather than another conditional P2 statement. It is
local progress by the inspected known methods, with no claimed
advance beyond those sources. L092's relative factor-four excess,
ell-integrality/native support, full selected/theta data, exact
generation/complete repair, source authentication/def= qualification,
native input/action/factorization/pilot, essentiality and original
finite B>=A remain unresolved. No complete-solution candidate is made.

### Separate critical audit — 2026-10-23, step406

**Scope and verdict.** The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-23-same-member-prime-selection-critical-audit.md`.
The claimed selection and conditional transfer pass without changing
the argument or its direct mathematical inputs. Reuse the precise
primary citations above, the step403 selection assessment and L100's
step402 audit; no fresh source authentication or general theorem
reproof is asserted. This verifies a local known-method input, not
an advance beyond the inspected sources or a complete IUT objection.

**Height before P2.** Fix an arbitrary survivor and ordering only
temporarily. L090's full-coordinate adjunction gives full geometric
3- and 5-torsion over every completion of F=G_o. L100's semistability
argument uses level five for p!=5 and level three for p=5. These
choices are available without a selected ell or P2. Its Tate-series
and splitting-normalization calculation then gives (1), also for
nonsplit multiplicative reduction. Although L100's full statement
assumes P2, neither of these two parts of its proof uses that premise.
Thus their use here before prime selection is noncircular.

For each rational p, the number-field completion decomposition gives

    sum_(v|p) e(F_v/Q_p) f_v=[F:Q].

This is the general degree formula, not the equal-e,f formula for a
Galois field; it is the number-field degree input in the cited height
normalization and Milne Theorem 3.34. With n_p=max(0,-v_p(j)),
substitution of (1) therefore gives H=sum_p n_p log p. The sum is
finite because j is a fixed nonzero rational. Writing j=a/b in lowest
terms with b>0 identifies it with log b. At infinity every embedding
has the same rational j, and the real weights one and complex weights
two sum to [F:Q]. Their normalized contribution is exactly
log max(1,|j|), proving (2)–(3) with the cited absolute normalization.
L089's A>0 and odd nonzero B give 0<j<1728, so (4) holds uniformly.
No selected-place sum, equal local indices or height over C_o or an
ell-division field has replaced the source's G_o-height.

**Finiteness and quantifier order.** Fix xi from the cited prime
theorem, the domains, d=6, epsilon_d=1 and the given finite Exc.
For every t in Exc_low, J is defined over Q, hence
Q(J(t)) is a subfield of Q(t) and its degree is at most six.
Silverman's Theorem 4.8(d) applies on the smooth projective P^1/Q
with its ample O(1), with the fixed absolute-height bound
xi^2+log 2000. Thus its possible values z=J(t) form a finite set.
There is no infinite-value case since t avoids the three cusps.
For each finite z the displayed polynomial has leading coefficient
256: its first term has degree six and its second has degree four.
It is nonzero and has at most six roots. This proves finiteness of
the entire Exc_low in Q-bar, not merely of its rational part.

The union Exc_total is therefore fixed before choosing E. If Exc
contains parameters of degree greater than six, discard those only
for the application of L091; no survivor parameter can equal them.
The finite J-image of the remaining set cannot contain L089's
infinitely many distinct rational survivor invariants. Selecting one
outside it makes all six parameters avoid the union simultaneously,
without requiring that union to be Galois stable. For any ordering
of this one member, H<=xi^2 would imply
h_abs(J(t_o))<xi^2+log 2000 by (4), contrary to its exclusion.
Thus (5) holds for that same member. Infinitely many equations or
large coefficients are not used as a replacement for this argument.

**Selection hypotheses and strict endpoint.** Fix one ordering now;
its literal F, E_o and normal closure remain fixed thereafter. L089
supplies t_o in the fixed domains and parameter degree at most six;
L090–L091 supply the stated Legendre adjunction in the qualified
source reading. L092 gives the actual, distinct degree
[F:Q]=276480=3317760/12<=delta. The heights are nonnegative integers
of finite support and sqrt(H)>xi>=5. These are the degree, height
and threshold inputs of the inspected IV Proposition 2.1(ii) and
Corollary 2.2(ii) proof, pp.44–45, through P1–P3. That construction
precedes P4–P7 and does not require normality of F/Q.

Import that one construction with its stated upper bound. Its one
prime avoids the union of all three finite sets. Since S1 includes
every prime <=sqrt(H), its exclusion gives the strict inequality
ell>sqrt(H)>5, hence ell>=7. S2 contains every prime divisor of
every nonzero h_v, including those over ell; its exclusion is P2
with the full all-place quantifier. S3 contains each rational residue
prime supporting any height >=sqrt(H); exclusion is P3 at every
F-place above ell. Zero heights introduce neither a divisor condition
in S2 nor a threshold violation in S3. There is no substitution of
three separately chosen primes or of the old prime seven.

**L100 and limits.** Only after this selection do ell>=7 and P2
supply L100's conditional hypotheses. The same survivor, ordering,
full-coordinate G_o and C_o occur in both statements. L092's actual
Galois normal-closure degree has only the prime factors 2,3,5, so
L100's already audited all-place transfer applies, including a pole
at p=ell. Neither P1 nor P3 over C_o nor j-integrality at ell is a
conclusion of this audit. The assertion is for each ordering
separately after selecting the member, not one prime for all six.

The April 2020 reproduction remains unauthenticated against current
author/journal bytes. L091's explicit def= reading remains in force;
an independent ordinary F_mod-model division-field requirement would
change the antecedent and is not certified here. P4–P7, ell-integrality
and native selected support, the relative factor-four excess, exact
generation/complete repair, native input/action/factorization/pilot,
essentiality and original finite B>=A remain unresolved. The canonical
audit supersedes the overview's pending-audit wording for L101 only.
The argument and DAG are unchanged, and no complete-solution candidate
is claimed.

## Mathlib

Full matching and supporting Mathlib coverage for this constrained
selection and transfer have not been checked. Unknown coverage is
not absence. This is an informal specialization of the cited height,
Northcott and prime-selection results; no mathematical script,
numerical certificate, new general selection theorem or formal
verification is claimed. The separate step406 audit validates the
informal specialization with its qualifications, not a formalization.
