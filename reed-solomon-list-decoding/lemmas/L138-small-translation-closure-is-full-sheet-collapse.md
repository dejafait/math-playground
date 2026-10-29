# L138 — Small translation closure already implies full-sheet constancy

## Hypotheses

Use the labeling setup of L030, restated in L135 before its additional
span-two assumption. Namely, q=137, T={16,64,70,102,112,118,121},
E=F_65537, F=F_(65537^28), H=<19139> of order 1024, and k=64.
Let C be any 61-subset of H and sigma any bijection from
(T times F_137) disjoint union four dummies onto H minus C.
Put x_(t,y)=sigma(t,y); all 959 such labels are distinct.

Let K be E or F. For every P=(u,v) in G=F_137^2 let
g_P(X)=a_0(P)+a_1(P)X+a_2(P)X^2 in K[X], allowing repetitions.
Assume the full-sheet constancies

\[
 g_P(x_{t,y})=d_{t,y}\quad\text{whenever }u+tv=y.
 \tag{1}
\]

Define U=span_K{1,a_0,a_1,a_2} inside the K-valued functions on G.
For e in G define (tau_e f)(P)=f(P+e). No action on the coefficient
image, translation closure, coefficient-span bound other than three,
or embedding of the auxiliary field into K is assumed.

## Conclusion

For each fixed nonzero e in G the following are equivalent:

1. tau_e U is contained in U.
2. Every g_P equals g_(0,0).

In particular the proposed two-unit-translation closure is equivalent
to full-sheet constancy. Even one of the two inclusions would suffice.
This is a conditional reduction, not a proof of either inclusion.

The nontrivial irreducible cyclic factor degrees are 136 over E and
34 over F. A finite-dimensional invariant function space containing 1
on which tau_e acts nontrivially must have dimension at least 137 or
35, respectively, whereas dim_K U is at most four.

No permitted nonconstant assignment or counterexample to closure is
constructed. No coefficient annihilator, retained-family bound or RS
transfer follows without the still-unproved closure premise. The
955–957 bracket is unchanged. This source specialization is not a
claim of progress beyond the checked module literature. The separate
critical audit on 2026-10-29 accepts this conditional equivalence over
both fields; it supplies no translation inclusion.

## Proof

**Source and assessed scope.** The pre-invocation EXPLORE
[assessment](../drafts/literature/2026-10-29-coefficient-function-translation-closure.md)
explicitly requires checking the cyclic factor degrees over both fields
and the conditional module implication. Import Evra, Kowalski and
Lubotzky, *Good cyclic codes and the uncertainty principle*,
L'Enseignement Mathematique 63 (2017), 305–332,
[Proposition 2.6 and its complete proof, pp. 309–310](https://ems.press/content/serial-article-files/44351).
For a finite field B of cardinality Q and prime p unequal to its
characteristic, every irreducible factor of Z^p-1 except Z-1 has
degree ord_p(Q), and all factors are distinct. The source also gives
the corresponding Chinese remainder decomposition into fields.
The retained primary text is
`drafts/sources/directional-fourier/evra-kowalski-lubotzky-2017.txt`.
The specialization below checks its arithmetic, applies it to the
actual translation operator, and then uses (1). No uncertainty theorem,
Fourier-minor assertion or new factorization theorem is being reproved.

**Exact orders.** The auxiliary prime 137 differs from characteristic
65537. Modulo 137, 65537=51 and

\[
 51^2=135=-2,\qquad 51^8=16,\qquad 51^{68}=136=-1,
 \qquad 51^{136}=1.
 \tag{2}
\]

For example 2^17=100 and 100^2=136 modulo 137, which verifies
51^68=(-2)^34=-1. The prime divisors of 136 are 2 and 17;
the nonidentity values at exponents 68 and 8 therefore certify
ord_137(65537)=136. For the extension field, its cardinality has residue
51^28=81, and

\[
 81^2=122,\qquad 81^{17}=136=-1,\qquad 81^{34}=1.
 \tag{3}
\]

The prime divisors of 34 are again 2 and 17. These values certify
ord_137(65537^28)=34, also equal to 136/gcd(136,28). It is the
cardinality of K, not just its characteristic, that enters this order.

**Conditional action on a small space.** Suppose tau_e U is contained
in U. The restriction A=tau_e|_U is a K-linear operator. Since the
nonzero auxiliary vector e has additive order 137, A^137=I. Its
iterates are restrictions of the ambient iterates because the assumed
inclusion keeps each intermediate vector in U; in particular A is
invertible with inverse A^136. Its minimal polynomial divides Z^137-1.
By Cayley–Hamilton its degree
is at most dim_K U<=4. The imported factorization and (2)–(3) show
that no nontrivial factor of Z^137-1 can divide that minimal polynomial:
their degrees are 136 or 34, both greater than four. Separability
excludes a repeated factor Z-1. The space contains the nonzero
constant function 1, so its minimal polynomial is not the constant
polynomial. It is therefore exactly Z-1, and A=I.

For the stated larger-space threshold, apply the source's Chinese
remainder idempotents to any finite-dimensional invariant space W containing 1.
Its fixed component contains 1 and thus has dimension at least one.
Indeed the idempotent for Z-1 acts as identity on 1 and all other
idempotents act as zero there. The quotient-ring action on W is the
unital action Z -> tau_e|_W; W is not being identified with a ring ideal.
Each nonzero component for a nontrivial factor is a vector space over
the associated degree-r field extension and hence has K-dimension a
positive multiple of r. If the action is nontrivial such a component
exists, so dim_K W>=1+r. This proves the thresholds 137 and 35.
It does not bound the dimension of the translate-generated space of
the given coefficients from above.

**One trivial translation forces constant messages.** From A=I we
have g_(P+e)=g_P for every P. Iteration gives invariance under every
multiple s e, s in F_137; here the auxiliary field is prime, so its
scalar multiples are precisely these iterates. Write e=(h,k) and
l_t(P)=u+tv. There is t in T with delta=h+tk nonzero: if k=0
all seven values equal the nonzero h; if k!=0 at most one t is
a zero. Fix such a t.

For any P and y in F_137 choose
s=(y-l_t(P))/delta in the auxiliary field. Then P+s e belongs to
A_(t,y), and g_(P+s e)=g_P. Applying (1) gives
g_P(x_(t,y))=d_(t,y) for every P and every y. Consequently, for
any P,Q the quadratic g_P-g_Q vanishes at all 137 distinct labels
x_(t,y). The polynomial root bound over K implies g_P=g_Q.
These labels lie in the prime subfield E of either K, so their
distinctness is unchanged on passing to F. No scalar from F_137 is
used in K: s e denotes iteration in the auxiliary index set alone.
This proves constancy. Conversely constant coefficients make U the
one-dimensional constant-function space, which every translation
preserves. Both directions of the equivalence are established.

**Why translation of the equations is insufficient.** This records
the exact obstruction encountered by the attempted closure proof.
For an arbitrary e, put delta_t=l_t(e), y=l_t(P),
x=x_(t,y), and x'=x_(t,y+delta_t). Equation (1) at P+e gives

\[
 g_{P+e}(x)=d_{t,y+\delta_t}
       +(x-x')\bigl(a_1(P+e)+(x+x')a_2(P+e)\bigr).
 \tag{4}
\]

This is the exact quadratic evaluation difference, including its sign.
For the unit vectors (1,0) and (0,1), delta_t equals 1 and t,
respectively. Every t in T is nonzero, so all these label differences
are nonzero. The bracket in (4) is not known to be constant on the
original line or to belong to U. Dropping it is unjustified.

The genuinely valid covariance changes the labeling as well:
sigma^e(t,y)=sigma(t,y+delta_t), with the four dummy images unchanged,
and g^e_P=g_(P+e). Each direction's intercept map is a permutation,
so sigma^e is another allowed bijection for the same C; this pair
satisfies (1) with common values d_(t,y+delta_t). However, sigma^e=sigma
would imply delta_t=0 for all t by injectivity. Two distinct t then
force e=0. Thus a nonzero translation changes the labeling. The
covariance supplies no equality tau_e U=U for the original family.

Locally the two evaluation rows cannot simply be identified: when
x!=x', the polynomial X-x' vanishes at x' but not at x. This is
only a one-line diagnostic. It is not an assignment to the whole
sheet and is not a counterexample to the target. Other directional
equations might force the missing memberships; this attempt does
not establish that implication or refute it.

**Verification and qualifications.** Reproduce the exact order check by
`python3 scripts/finite-support/coefficient_translation_orders.py`.
Its certificate is
`scripts/finite-support/coefficient-translation-orders.json`.
It retains every power for exponents 1 through 136 for both cardinality
residues and reports zero arithmetic failures. The short certificates
(2)–(3) suffice independently for the orders. The script verifies zero
of the six requested translated-function memberships and constructs
no full-sheet counterassignment; its successful arithmetic exit is
not successful verification of closure.

The separate audit and its full operator/directional checks are recorded
in `drafts/audits/2026-10-29-l138-critical-audit-working.md`.
Run `python3 scripts/finite-support/audit_coefficient_translation_orders.py`
for the independent repeated-multiplication replay. Its complete
certificate, `scripts/finite-support/l138-critical-audit-arithmetic.json`,
checks both full 136-entry power arrays and all displayed short-order
certificates, the prime fields and label budget: 37 checks, zero failures.
It certifies arithmetic only; the invariant-module and root arguments
are the proofs above, not conclusions of this finite calculation.

The two fields are treated directly, without assuming that any given
F-valued assignment descends to E. Repeated g_P cause no problem in
the root argument. Neither C137a nor L137 is used in this proof;
their geometric and source qualifications are not silently repaired.
No larger-field characteristic cutoff, affine labeling, or action on
messages is assumed. The full-sheet implication is strictly local
to (1) and leaves retention and RS realization unresolved.

## Mathlib

Full matching coverage and supporting theorem names have not been
checked. The imported result is EKL Proposition 2.6; Cayley–Hamilton
and the polynomial root bound are standard named supporting facts.
Unknown Mathlib availability is not evidence of absence.
