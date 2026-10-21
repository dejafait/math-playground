# L062 — One canonical global class passes the five/eleven filters

## Hypotheses

Use L033's degree-twelve number field K, curve
E0: y²+y=x³−x²−10x−20, dual isogeny theta:E1 -> E0,
normalized connecting map delta and f=(x−4)y−4x²+30x−55.
Let S be all finite primes of K above five and eleven, and use
K(S,5) with valuations divisible by five outside S.
Use L034's entire degree-twelve modular map j:E0 -> P1.

Put s=9261/8 and Z=j^(-1)(s) over Q, with coordinate algebra D.
Use L047's unconditional identification D ≅ K of the entire canonical
fiber. Fix once and for all a Q-algebra isomorphism sigma:D -> K.
This is an intrinsic specification; no conversion to K's polynomial
power basis is required or asserted. Define P_sigma by the morphisms

    Spec(K) --Spec(sigma)--> Z --> E0.

The local tests are precisely L061's full five-adic class list and
L044's eleven-adic valuation filter, with L041's place order.
No integer solution, global class basis, GRH, rank or Sha hypothesis
is imposed. In particular the integer-solution hypotheses used for
L033's transported-solution clause are not assumed here.

## Conclusion

The intrinsically specified class

    alpha_sigma = delta(P_sigma) = [f(P_sigma)] in K^*/K^{*5}

belongs to K(S,5). Its localization at five, on the entire algebra
K tensor_Q Q5, belongs to L061's exact 55-element image. Its
eleven-adic valuation vector, on all three places in L041's order,
belongs to {(0,2,0),(2,0,0)}. These are two restrictions of the same
global class, not separately chosen local image elements.

Thus the intersection of K(S,5) with these two named necessary filters
is nonempty. This does not decide the full eleven-adic unit filter,
the all-place restricted intersection, or any rational or integer
power lift. It does not exclude the branch or settle any Beal signature.

## Proof

### Imported results and applicability

Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents
2, 3, n*, Compositio Math. **156** (2020), 77–113,
[DOI](https://doi.org/10.1112/S0010437X19007693),
[June 10, 2019 final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, printed pp.25–27, gives the irreducible twelve-subgroup
canonical fiber and Table 5's 54a1 field. L047 verifies s=j(54a1)
and this entire field identification; L034 supplies the complete map,
including its exceptional charts. These inputs precede the separate
GRH-dependent Selmer computation, which is not used.

Schaefer–Stoll, *How to do a p-descent on an elliptic curve*, Trans.
AMS **356** (2004), 1209–1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X),
[June 13, 2001 long manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Proposition 4.6, printed p.7, and Section 5, pp.8–9, supply support
containment and the commuting global/local restriction diagram.
L033 verifies the dual-kernel mu_5 identification and its function
normalization, globally and at every completion. Its general proof
shows delta(E0(K)) ⊆ K(S,5), independently of an integer solution.
Both integral models have discriminants supported at eleven and hence
good reduction and Tamagawa number one away from eleven, also after
base extension. S includes every prime above five and eleven, so it
includes every place required by Proposition 4.6. No equality of
global point classes with Selmer classes is used.

[Stacks Lemma 26.17.2, tag 01JQ](https://stacks.math.columbia.edu/tag/01JQ)
identifies affine fiber products with tensor-product coordinate rings.
It applies to the finite affine fiber Z over Q and both completions.
We specialize these imported results; no general descent or base-change
theorem is reproved. The saved assessment authorizes this REPRODUCTION.

### A single global point and class

The rational numbers s, 1728−s=4563/8 are nonzero. Thus s avoids
the branch values 0,1728,infinity, and Z is finite etale of degree
twelve. The cited canonical-fiber theorem identifies its whole
coordinate algebra D as a field isomorphic to K. The map Spec(sigma)
is an isomorphism onto Z, with the indicated contravariant direction.
It therefore gives one K-point P_sigma on E0 with j(P_sigma)=s.

L034 gives j(T)=−24729001 and j(O)=infinity, both different from s.
Consequently P_sigma is neither T nor O; f has no zero or pole there
by L033's divisor 5(T)−5(O). It is a nonzero element of K and the
ordinary formula delta(P_sigma)=[f(P_sigma)] applies. Support
containment above proves alpha_sigma ∈ K(S,5). An intrinsic element
in the specified field is an exact witness, although its power-basis
coordinates and a class-group expression have not been computed.

For p=5 and p=11 let A_p=K tensor_Q Q_p. The entire local fiber is
B_(s,p)=D tensor_Q Q_p. Tensoring the same sigma gives

    sigma_p = sigma tensor 1 : B_(s,p) -> A_p.

Compose Spec(sigma_p) with the base-changed inclusion of the entire
fiber in E0. This is exactly the base change of P_sigma, and it retains
every factor of A_p. The connecting-map restriction diagram identifies
its class with loc_p(alpha_sigma). Equivalently, since f is regular and
invertible on this fiber, its value is the image of f(P_sigma) under
K -> A_p. No new local point or independent conjugate is selected.

### The primitive local scalar hypotheses

For the same rational s at both primes, the exact ratios are

    t=s/1728=343/512,   q=1−t=169/512.

At five, the integers 343,169,512 are all units, so
(v5(t),v5(q))=(0,0) ∈ (3 N0) × (4 N0).
L036 therefore supplies common nonzero primitive a5,b5,c5 ∈ Z5
with a5³+b5⁴=c5¹¹ and s=1728 a5³/c5¹¹.
For the compatibility disk, 9261−2·8=9245=5·1849 and 8 is a
five-adic unit, giving s ∈ 2+5 Z5. L061 consequently applies to
the whole isomorphism sigma_5 and yields loc_5(alpha_sigma) in its
55-element list. Any identification of its unramified degree-eleven
factor with L061's fixed model is permitted because the list retains
all eleven embeddings. This is a theorem-based membership certificate;
no particular Frobenius index has been evaluated.

At eleven, 343≡2, 169≡4 and 512≡6 mod 11, so all are units and
(v11(t),v11(q))=(0,0). L041's exact scalar-domain sufficiency supplies
common nonzero primitive a11,b11,c11 ∈ Z11 with the same scalar
identities. Its proof constructs c11 freely and lifts cube and fourth
roots; this application makes no eleventh-root claim in characteristic
eleven. Also 9261−4·8=9229=11·839, so s≡4 mod 11.
L044 applies to the entire sigma_11 and this common scalar witness.
With the actual K-places ordered by k residues 8,2,10 as in L041,
its valuation vector is (0,2,0) or (2,0,0). Both rational-factor
permutations are retained in the theorem. The fixed global sigma
determines which occurs; choosing between them is unnecessary to
certify membership in the specified filter.

The exact fraction and unit/residue checks are also recorded in
`scripts/canonical-global-class/scalar-certificate.json`: seven
arithmetic checks pass, with no failures. This certificate verifies
only the displayed scalar arithmetic, not the cited fiber or descent
theorems or their mathematical application.

The triples at five and eleven may differ. The global object shared
by the two tests is P_sigma and alpha_sigma, not an asserted rational
power triple. A single witnessed simultaneous membership meets the
approved stopping test. Full eleven-adic units, other local restricted
conditions and integer lifting remain unresolved. The independent critical
application review below confirms the stated two-filter result;
no complete Beal candidate exists.

### Independent critical application audit, completed 2026-10-13

The 2026-10-12 unfinished audit text and replay implementation were
preserved and checked on resumption. The completed review below reuses
the prior source assessment; it does not claim a fresh source retrieval.

All four interfaces pass without a mathematical correction. This is an
audit of the preceding application, not a new global-class search or a
reproof of the imported general theorems. The prior L033, L034, L047,
L044 and L061 audits are reused at their stated interfaces. In particular
the last two local results have already been audited; the older pending
wording in the overview is not an additional premise.

**General support.** In Schaefer–Stoll's June 13, 2001 manuscript,
Section 4's diagram and Proposition 4.6, pp.6–7, concern all global
point classes, with Section 5, pp.8–9, identifying their evaluations
and restrictions. L033's general proof, rather than its later
transported-integer-solution clause, is applicable. The isogeny is
theta:E1 -> E0, dual to the quotient by the rational point T.
The perfect pairing with T identifies its kernel with mu_5 over K
and every completion. The singleton evaluation algebra is K itself,
so the cohomology identification is an isomorphism globally and locally;
neither rational fifth roots of unity nor a point/Selmer equality is
required. The normalization is the same f in both local filters.

Recomputing the discriminants of the two displayed integral models
gives -161051=-11^5 and -11. At every finite K-place away from eleven
these remain units, so both curves have good reduction and Tamagawa
number one, even if the place is ramified over Q. S contains all places
above the isogeny prime five and all potentially bad places above eleven.
This checks every place required by Proposition 4.6, not just one chosen
place above a rational prime. Outside S, the Kummer unramified classes
are exactly those with valuation divisible by five, as justified in
L033's audit. Over C the fifth-power quotient is trivial; over R every
nonzero real number has a fifth root. Thus infinite places impose no
missing condition. The conclusion delta(E0(K)) subset K(S,5) applies
to the proposed point independently of an integer solution.

**Entire fiber and ordinary evaluation.** L047's rational equality
s=j(54a1) and FNS Section 7.2's entire-field identification apply before
the source's GRH-dependent Selmer computation. Here 1728-s=4563/8 is
nonzero and s is finite and nonzero. The degree-twelve fiber is therefore
etale, and its whole coordinate field D is the cited K. Fixing an
isomorphism D -> K, rather than merely a point of one local factor,
gives Spec(K) -> Spec(D) -> E0 in exactly the required contravariant
direction. Its composite with j is the constant scalar s.

L034's exceptional values are j(T)=-24729001, j(2T)=-121 and
j(4T)=-32768, with O and 3T above infinity. None equals s. In
particular the only zero and pole of f, namely T and O by L033's
divisor, are absent from the whole fiber. Thus f is a unit in D,
and sigma(f|_Z) is a nonzero element of K. Ordinary evaluation is
legitimate before and after localization. No reconstruction denominator
or unproved polynomial presentation is used in this intrinsic argument.

**One fixed class at both primes.** For p=5,11, tensor the same sigma
with Q_p. Under Stacks Lemma 26.17.2 (tag 01JQ), the resulting map
D tensor Q_p -> K tensor Q_p induces precisely the base change of
the global morphism above. On functions its evaluation is

    (sigma tensor 1)((f|_Z) tensor 1) = sigma(f|_Z) tensor 1.

The commuting restriction diagram of Schaefer–Stoll Section 5
therefore identifies the resulting connecting class with
loc_p(alpha_sigma). This equality holds in the entire product algebra
and hence at every factor. All factors are retained even though K is
a field and either local tensor product may split. No independently
chosen local point or local conjugate enters the construction.

**Exact local hypotheses and memberships.** Independent rational
arithmetic gives t=343/512 and q=169/512. All three integers are prime
to both five and eleven, so both valuation pairs are exactly (0,0).
These satisfy the nonnegative branches of L036 and L041. Their
sufficiency proofs keep one c in both identities and yield nonzero
integral primitive triples, which are exactly the local hypotheses.
At five, eleventh and cube roots of units exist since both exponents
are prime to four and five. At eleven, L041 instead chooses a unit u
with residue q^(-1), so q*u^11 has residue one, then lifts a fourth
root at one and a cube root using gcd(3,10)=1. Both derivatives are
units. Thus no eleventh-root surjectivity at eleven is assumed.

The differences s-2=5*1849/8 and s-4=11*839/8 certify the required
scalar residues. The entire sigma_5, with the L036 witnesses, satisfies
L061's hypotheses. Any identification of its degree-eleven factor with
the fixed unramified model is among the eleven embeddings retained by
that theorem. Therefore the localization is in the exact 55-class
list, without needing a Frobenius index. The entire sigma_11, with
the L041 witnesses, satisfies L044's hypotheses. The place order remains
k congruent to 8,2,10, and the third coordinate uses its normalized
uniformizer order, not v11. L044 retains both rational-factor
permutations and every ramified embedding, so the fixed localization's
vector belongs to its two-element set regardless of which permitted
permutation sigma induces. Both applications use L033's same normalized
delta and impose no integer-solution premise.

Run `python3 scripts/canonical-global-class/audit_scalar.py` for the
independent arithmetic replay. It reads no construction code and
recomputes both fractions, valuations, scalar residues, differences,
finite exceptional exclusions and curve discriminants. All seven
original check flags and both complete local evidence objects agree;
the new certificate has 11/11 checks passing and no failures. Its
full relevant values, as well as the original certificate's relevant
fields, were inspected using the bounded JSON inspector with selected
full values. The complete output is
`scripts/canonical-global-class/audit-certificate.json`. This arithmetic
does not independently reverify the cited theorems or the already
audited local enumerations; the preceding argument verifies their
application.

One same-class witness therefore meets the required threshold of one
survivor. The two named necessary filters cannot alone prove emptiness.
This confirms the existing conclusion, with no new mathematical
restriction, class basis, full eleven-adic unit-image enumeration,
all-place computation or rational/integer power lift. No progress
beyond the cited and previously proved inputs is claimed.

## Mathlib

Full canonical-global-class simultaneous membership theorem: not
checked. Supporting entire-fiber base change, connecting-map
localization, Kummer support and local power-domain theorems: not
checked. Unknown availability is not absence. The proof uses the
precise cited standard inputs and canonical local results above.
