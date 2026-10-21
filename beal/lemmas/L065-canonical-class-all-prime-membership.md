# L065 — The fixed canonical class survives every finite-prime filter

## Hypotheses

Use L033's number field K, curves E0 and E1, dual isogeny
theta:E1 -> E0, and normalized connecting map delta with values in
K^*/K^{*5}. Use L034's complete projective modular map j:E0 -> P1.
Use exactly L062's entire canonical fiber Z at s0=9261/8, its
coordinate field D, fixed Q-algebra isomorphism sigma:D -> K,
point P_sigma and class alpha_sigma=delta(P_sigma). No new global
conjugate is chosen. Let S contain all K-primes above five and eleven,
as in L062.

For each rational prime p put A_p=K tensor_Q Q_p. For finite
s in Q_p minus {0,1728}, let B_(s,p) be the coordinate algebra of
the entire projective fiber j^(-1)(s). Define I_p to be the set of
delta(P_phi) in A_p^*/A_p^{*5}, where phi:B_(s,p) -> A_p is a
Q_p-algebra isomorphism, P_phi is obtained from the universal fiber
inclusion, and one common triple of nonzero a,b,c in Z_p satisfies

    a^3+b^4=c^11, s*c^11=1728*a^3,
    min(v_p(a),v_p(b),v_p(c))=0.

Retain additionally b odd, c even, a=7 modulo 8 at p=2, and
a=1 modulo 3, b^2=1 or 4 modulo 9, c a unit at p=3.
These are exactly the branch clauses in L046 and L049. Elsewhere
no extra branch clauses are imposed. The same triple and scalar are
used across every factor of A_p. All whole-fiber isomorphisms and
normalized exceptional connecting evaluations are allowed. No
integer solution, class/unit basis, GRH, rank, Sha, Selmer/point
equality, or cross-notebook result is assumed.

## Conclusion

For every rational prime p,

    loc_p(alpha_sigma) belongs to I_p.

Thus K(S,5) intersected with all loc_p^(-1)(I_p), over finite rational
primes p, contains alpha_sigma and is nonempty. At two, three and
thirteen its localized class is the identity. At every p other than
two and thirteen the membership can be witnessed at the same scalar
s0 using sigma tensor 1 and the explicit rational power triple below.
At two and thirteen different scalars realize precisely the same
localized class, using L046 and L064.

This establishes survival of one fixed class under exactly these
finite-prime necessary tests. It does not enumerate the intersection,
prove simultaneous power witnesses for the fixed global point at all
primes, or supply rational/integer primitive power lifting or branch
emptiness. Other Beal signatures remain unresolved. Independent
critical application audit completed on 2026-10-14 confirms this
assembly without a mathematical correction, as detailed below.

## Proof

### Standard inputs and the specialization

Michael Bennett, Preda Mihăilescu and Samir Siksek, *The Generalized
Fermat Equation*, in *Open Problems in Mathematics* (2016), pp.173–205,
[DOI](https://doi.org/10.1007/978-3-319-32162-2_3),
[31-page author manuscript](https://samirsiksek.github.io/siksek.github.io/papers/bealconj.pdf),
Section 4, manuscript p.22, the construction immediately after (27),
gives the standard common-multiplier construction for pairwise coprime
exponents. Its primitivity qualification is essential: it does not
give primitive integer solutions. Here (3,4,11) are pairwise coprime,
and the already rational-cube ratio at s0 permits a particularly short
specialization. We verify that particular formula and its local
primitivity; we do not reprove the general construction or claim a
new general theorem. The ready SPECIALIZE assessment covers this
power correction and the exceptional assembly.

Schaefer–Stoll, *How to do a p-descent on an elliptic curve*, Trans.
AMS **356** (2004), 1209–1231,
[June 13, 2001 long manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Section 5, pp.8–9, supplies the connecting-map restriction diagram;
[Stacks Lemma 26.17.2, tag 01JQ](https://stacks.math.columbia.edu/tag/01JQ)
supplies entire affine-fiber tensor-product base change. Their
unconditional applicability to this fixed point, isogeny direction
and normalization is checked in L033 and audited L062. They apply
at every completion, without any splitting or unramified hypothesis
on A_p. L046 and L049 import the same manuscript's Lemmas 4.2–4.5,
pp.6–7, with the actual local fields, good reduction, Tamagawa numbers
and dual kernel mu_5 checked, yielding their full singleton images.
We use their audited conclusions rather than reproduce those field
calculations or the descent theorem. L064 supplies its audited exact
same-class thirteen-adic witness. No additional external source is
needed for these unchanged interfaces.

### One exact power correction, uniform away from two and thirteen

Put

    r=7/8, t=r^3=343/512, q=169/512.

Since 343+169=512, t+q=1, and 1728*t=9261/8=s0.
Define rational numbers

    a=r*q^33, b=q^25, c=q^9.

They are nonzero. Direct exponent identities give

    a^3=t*q^99, b^4=q^100, c^11=q^99,
    a^3+b^4=(t+q)*q^99=q^99=c^11,
    s0*c^11=1728*t*q^99=1728*a^3,
    (1728-s0)*c^11=1728*q^100=1728*b^4.

In particular there is one shared c in both scalar identities. These
are exact rational identities; no local root map, approximation,
finite-prime sample or eleventh-root surjectivity is invoked.

For every p outside {2,13}, q is a p-adic unit. The number r is
p-adically integral, with valuation one at seven and zero at every
other such prime. Consequently a,b,c are nonzero elements of Z_p,
b and c are units, and the valuation triple is (1,0,0) at seven and
(0,0,0) at every other p outside {2,13}. This verifies primitive
integrality uniformly, including the seven-adic nonunit case and
the derivative primes three and eleven.

At three the additional branch clauses also hold. Reduction gives
r=2 and q=2 modulo 3, hence a=2*2^33=1 modulo 3. Modulo nine,
169=7 and 512=8 with 8^(-1)=8, so q=2. Therefore
b^2=q^50=2^50=4 modulo 9, since 2^6=1 and 50=2 modulo 6.
The coordinate c is a unit. No cube-root lifting at three is needed.

The formulas are not primitive at the two omitted primes: at two
their valuations are (-300,-225,-81), and at thirteen they are
(66,50,18). We do not use this triple there or infer class exclusion
from its failure. Those primes require the separate assembly below.

### Whole-fiber and fixed-class transport at all uniform primes

For every rational prime p, base change gives

    B_(s0,p)=D tensor_Q Q_p,
    sigma_p=sigma tensor 1:B_(s0,p) -> A_p.

This is an isomorphism of entire algebras. Its induced scheme
morphism Spec(A_p) -> Spec(B_(s0,p)), followed by the fiber inclusion,
is exactly the base change of P_sigma. The scalar s0 is finite,
nonzero and different from 1728 over every Q_p; its rational value
does not change under embedding. Thus it is an allowed scalar.

L062 checks P_sigma is neither T nor O, so f is invertible on the
entire canonical fiber. On functions, with f|_Z in D, one has

    (sigma tensor 1)((f|_Z) tensor 1)=sigma(f|_Z) tensor 1.

The commuting restriction diagram identifies the normalized class
of this point with loc_p(alpha_sigma) in the full product quotient.
This holds at every factor of A_p, including ramified or split ones;
no independent local conjugate or factor is chosen. For p outside
{2,13}, the preceding common primitive triple and this same sigma_p
therefore witness membership in I_p. At five this proves full-class
membership, consistently with L062's list membership. At eleven it
likewise proves full-class membership, using more than its previously
stated valuation projection, without enumerating the unit image.
At three L049 also implies that this localized class is the identity,
since its unrestricted image is {1} over this exact entire algebra.

### Two exceptional class realizations

At two the base-changed P_sigma is still an E0(A_2)-point, whether
or not its scalar admits primitive power witnesses. L046 proves
delta(E0(A_2))={1}. Thus loc_2(alpha_sigma)=1. The same lemma
proves that the entire fiber at s2=55269/32 is isomorphic to A_2,
and supplies b=1, c=2 and a the two-adic cube root of 2047 with
a=7 modulo 8. Its triple is primitive, satisfies both scalar
identities, and retains every two-adic branch clause. Its class is
the identity under the same normalized delta, so it realizes exactly
loc_2(alpha_sigma) in I_2. Restricted nonemptiness is supplied by
that witness, rather than inferred from the unrestricted singleton.

At thirteen L064 fixes exactly this sigma before localization and
proves loc_13(alpha_sigma)=1. It identifies the entire fiber at
s13=3 with A_13 and proves its connecting class is also one. Its
common primitive witnesses are b=2, a^3=16/575 and
c^11=9216/575, with a=1 modulo 13 and c=10 modulo 13.
All three coordinates are units. Thus L064 directly gives
loc_13(alpha_sigma) in I_13. This application uses its full-field
and fifth-root checks, not merely a norm or a valuation. Its already
proved failure of primitive witnesses at the canonical scalar is
compatible with this class realization at a different scalar.

Every rational prime is now covered: outside {2,13} by one exact
formula and tensoring the fixed sigma; at two and thirteen by the
audited same-class witnesses. The audit list {2,3,7,13} is fully
accounted for: three by the exact residues, seven by the valuation
triple, and two/thirteen by the exceptional assembly. No unresolved
prime is hidden in a finite check.

Finally L062 gives alpha_sigma in K(S,5), so all these memberships
prove the asserted nonempty finite-prime class intersection. They
retire removal of this particular survivor using exactly the I_p
tests. Local scalar/point witnesses may differ with p; at two and
thirteen only their connecting classes agree with the fixed point.
Therefore this is not a single global primitive power triple, a
point/Selmer equality, or a resolution of the remaining integer gap.
It is local notebook progress by reproduction of the assessed methods,
with no claim of progress beyond the inspected literature.

### Independent critical application audit, completed 2026-10-14

The audit reuses the approved primary coverage and the completed input
audits; it checks this new assembly rather than repeating local-field
computations. The standard references and hypotheses are those in the
first proof subsection. In particular the common-multiplier source
does not assert primitive solutions. Exact identities and support must
supply that part of this specialization.

**Independent arithmetic and the universal quantifier.** Expanding the
proposed coordinates into primes gives

    a=7*13^66/2^300, b=13^50/2^225, c=13^18/2^81.

Consequently

    a^3+b^4=(343+169)*13^198/2^900
           =13^198/2^891=c^11,
    a^3/c^11=343/512, b^4/c^11=169/512,
    1728*343/512=9261/8.

This independently checks the exponents and the one common c; the
second scalar identity follows with the same denominator c^11. The
complete numerator/denominator prime support is contained in {2,7,13}.
The three valuations, for any rational prime p, are exactly

    (v_p(7)+66*v_p(13)-300*v_p(2),
     50*v_p(13)-225*v_p(2),
     18*v_p(13)-81*v_p(2)).

Thus the triple is integral and primitive at every p outside {2,13},
including (1,0,0) at seven. At two it is (-300,-225,-81); at thirteen
it is (66,50,18). These failures cannot be hidden by the uniform claim.
At three, a is 1 modulo 3 directly from its expanded expression.
Also b^2=13^100/2^450 is 4 modulo 9: 13 is 4 modulo 9,
4^3=1, 100=1 modulo 3, and 2^450=(2^6)^75=1 modulo 9.
The denominator is invertible, and c is a unit. These are exactly all
extra three-adic clauses. No root-surjectivity assumption is needed
at three, five or eleven. This symbolic calculation covers every
prime, not just finitely many tested completions.

**Global support and the same localized point.** L062's general support
argument applies to every E0(K)-point, without an integer-solution
hypothesis: both curves have good reduction outside eleven after
extension to K, and S contains every place above five and eleven.
Schaefer–Stoll Proposition 4.6 and Section 5 therefore put this fixed
alpha_sigma in K(S,5). Its construction does not rely on the local
membership conclusion being audited.

The fiber Z is finite affine and its entire coordinate field is D.
Since s0 avoids 0,1728,infinity in Q, it avoids them in every Q_p.
The base-change isomorphism is D tensor Q_p -> K tensor Q_p, in
the direction sigma tensor 1. Its contravariant scheme map followed
by Z's inclusion is exactly the base-changed P_sigma. The fact that
E0 is projective causes no affine-scheme shortcut: only Z is being
identified with Spec(D). L034's j(T)=-24729001 and j(O)=infinity
exclude the zero and pole of f throughout Z. Thus f|_Z is invertible,
and remains invertible after every tensor product. Evaluating under
sigma tensor 1 gives sigma(f|_Z) tensor 1; Schaefer–Stoll Section 5
identifies its class with the localization for the same normalized
theta:E1 -> E0, with kernel mu_5. This is equality in the full product
of local fifth-power quotients, including every ramified or split
factor. No norm, valuation projection or separate local conjugate is
substituted. The uniform witnesses therefore prove precisely I_p
membership for every p outside {2,13}, including the full class at
eleven. L049 additionally makes the class at three the identity.

**Exceptional replacement checks.** L046's hypotheses use these same
K, theta, f and entire modular map. Its audited unrestricted image
is the singleton on both factors of A2; hence the localized fixed
point has identity class regardless of its scalar's admissibility.
Its separately proved whole-fiber realization at 55269/32 supplies
b=1, c=2 and a^3=2047. Here 2047+1=2^11,
1728*2047/2048=55269/32, and a=7 modulo 8. Thus the witness meets
every defining clause of I_2 and has exactly that identity class.
The unrestricted singleton alone would not have proved membership.

L064 expressly fixes L062's same sigma, uses the same normalized f,
and proves that its localization at thirteen and the entire scalar-3
fiber's class are both one. Its audited field identification and exact
fifth-root lifts supply class equality, not just equality of norms or
valuations. Its common witnesses satisfy

    16/575+16=9216/575,
    1728*(16/575)=3*(9216/575).

The audited roots a=1 modulo 13 and c=10 modulo 13, with b=2,
are all units. Scalar 3 is finite and different from 0 and 1728 in
Q13. Consequently every required I_13 condition is met for the
localized fixed class. No assumption that the canonical scalar itself
is admissible at thirteen enters this replacement.

These cases exhaust the rational primes and establish one same-class
survivor in the stated intersection. The six direct lemma inputs in
the DAG are exactly those used in this proof; no new edge is needed.
The audit finds no failed obligation or missing hypothesis within this
scope. It confirms a relevant intermediate input by REPRODUCTION,
without a new restriction or claim of progress beyond the assessed
methods. The different points at two/thirteen do not give primitive
power witnesses for the fixed global point there. No global primitive
triple, complete intersection, class/unit basis, rank certificate or
integer emptiness follows. The failure of finite-prime removal recorded
in ATTEMPTS/030 is confirmed; another audit or prime search needs a
specific new defect. Exact symbolic verification suffices here, so no
new arithmetic script or finite sampling certificate is used.

## Mathlib

Full fixed-class all-prime membership theorem: not checked. Supporting
rational power identities, valuations, whole-fiber base change and
connecting-map localization declarations: not checked. Unknown
availability is not absence. The explicit identities and cited,
previously audited interfaces above supply the mathematical proof.
