# L075 — Full global Kummer containment with support above two and eleven

## Hypotheses

Let K be the entire degree-twelve number field specified in L033 and
let E0/K be y²+y=x³−x²−10x−20. Use L069's fixed model and generator

    g(X)=X³−4X²−160X−1264,   D=K[θ]=K[X]/(g).

For F=K,D let S_F be ALL maximal-ring primes above 2 and 11. Use
L074's spaces H_{F,S} of field square classes with even normalized
valuations outside S_F, and W_S=ker(N_D/K:H_{D,S}->H_{K,S}).
There are no sign restrictions. No primitive solution, class-group
value or unit-group computation is assumed.

## Conclusion

The full two-descent map is an injection

    δ₂:E0(K)/2E0(K) -> W_S,
    δ₂(O)=1,
    δ₂(x,y)=[4x−θ] for every finite point (x,y) in E0(K).

In particular every representative 4x−θ has even valuation at every
maximal prime of D outside S_D, including for points with coordinate
denominators, and its norm is a square in K*. The image at O has the
same properties. This is a KNOWN_IMPORTED application of Simon's
support theorem, not a new support theorem or a rank computation.

## Proof

Import Denis Simon, *Computing the rank of elliptic curves over number
fields*, LMS J. Comput. Math. **5** (2002), 7–17,
[DOI](https://doi.org/10.1112/S1461157000000668),
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8FAFF26D93D01A154C51CF897E4BE6CD/S1461157000000668a.pdf/computing_the_rank_of_elliptic_curves_over_number_fields.pdf),
Section 1.1, Propositions 1.1–1.2, printed p.8, and Section 1.2,
Proposition 1.4, printed p.9. For a number field k and a monic integral
irreducible cubic P, these give the map on y²=P(x) with O mapping to 1
and finite points mapping to [x−θ], kernel 2E(k), square norm, and even
valuations outside the following support: infinite places and primes
P of k(θ) for which P divides P'(θ) and the underlying prime p of k
satisfies p² dividing disc(P). The complete Proposition 1.4 proof,
including negative coordinate valuations and the discriminant-valuation-one
case, was inspected in the prior assessment
`drafts/literature/2026-10-15-supported-kummer-containment.md`.
We apply this theorem without rederiving its valuation argument.

L069 gives the origin-preserving K-isomorphism

    (x,y) -> (X,Y)=(4x,8y+4),   Y²=g(X),
    disc(g)=−256·11^5.

It also proves that this same g is irreducible over the entire K, so
D is the entire degree-three extension to which Simon applies. The
coefficients are rational integers, hence in O_K; characteristic zero
and the displayed nonzero discriminant give a smooth curve. The model
change has inverse x=X/4, y=(Y−4)/8 over K, and transports both the
origin and multiplication by two. Thus Propositions 1.1–1.2 give exactly
the displayed δ₂ on E0, with its asserted kernel and square norm.
Irreducibility ensures 4x−θ is nonzero for every finite K-point: equality
would put θ in K. No global finite two-torsion exception is suppressed.

For any maximal prime P of O_D outside S_D, its underlying prime p
of O_K is outside S_K. Both 2 and 11 are units at p, so

    v_p(disc(g))=v_p(−256·11^5)=0.

Consequently p² does not divide this polynomial discriminant, and P
cannot belong to Simon's exceptional support. Proposition 1.4 therefore
gives v_P(4x−θ) even for every finite K-point. This argument covers
EVERY outside-support maximal prime, irrespective of ramification or
residue degree, and uses the polynomial discriminant in O_K rather
than an order index or an assumed maximal-field discriminant. The theorem
already covers negative coordinate valuations. For O the representative
1 has valuation zero everywhere. All primes above 2 and 11 remain
permitted; no evenness assertion is made at them.

Thus δ₂ takes values in H_{D,S}. Its square norm has trivial class in
K*/K*², hence also in H_{K,S}, which is a subgroup of that field
square-class group. With L074's norm and support conventions, δ₂
therefore takes values in W_S. Simon includes infinite places in his
support without imposing signs; L074 also imposes no archimedean sign
condition, so there is no missing positivity premise. This proves the
claimed containment and injection.

L074's supported quotient now applies to an ambient space containing
actual global Kummer classes. Its S-unit kernel and localized class-norm
kernel still need arithmetic control and simultaneous local filtering.
L069's unfiltered dimension obstruction and L073's local odd valuations
at eleven are not contradicted: support has been retained, and no global
realization of those odd local classes has been asserted. No dimension,
rank, subgroup-index or primitive integer conclusion follows here. The
separate critical application review below confirms this import.

### Independent critical application audit (2026-10-16)

**Verdict: confirmed without correction.** This audit uses the prior
IMPORT assessment `drafts/literature/2026-10-15-supported-kummer-containment-audit.md`
and its recorded primary coverage of Simon, Propositions 1.1–1.2 and
1.4, printed pp.8–9. That coverage includes all three support-proof
cases, including negative coordinate valuations. No fresh source search,
general support-theorem reproof or mathematical script is needed.

The input is the fixed number field K and curve E0 defined in L033,
not the existence of the hypothetical primitive triple in L033's opening
hypotheses. Its field definition is an unconditional FNS input, separated
there from conditional Selmer computations. The relevant L069 proof
has been checked: the rational Q5 place embeds K in Q5, and the monic
cubic reduces to X³+X²+1 with nonzero values 1,3,3,2,1 at the five
residues. Thus g has no root over K and is irreducible. Its previously
audited polynomial discriminant is −256·11^5. These inputs supply the
entire cubic number field D, not a component of a split completion.
Neither class-group data nor a primitive solution is required.

The identity Y²=g(X) under X=4x, Y=8y+4 holds on E0, with inverse
x=X/4, y=(Y−4)/8. This is an invertible Weierstrass change over K;
it extends to the smooth projective curves, fixes O, and hence is an
elliptic-curve group isomorphism. It identifies multiplication by two
and its quotient. Simon's map therefore transports to exactly
[4x−θ], with no extra scalar factor, and O maps to [1]. Here θ is
the root of g; it is unrelated to L033's dual five-isogeny also named
theta. The target is D*/D*², not L033's K*/K*⁵.

For every finite global point, X belongs to K whereas θ does not, so
X−θ is nonzero. Also Y cannot be zero, since that would give a K-root
of g. With the monic polynomial and this sign convention, the norm
identity is N_D/K(X−θ)=g(X)=Y² in K*². Simon's kernel statement then
gives the claimed injection on E0(K)/2E0(K), not merely a map on a
subset of points. No exceptional global finite two-torsion evaluation
is omitted. Split local two-torsion cases are outside this application.

For each maximal prime P of D outside S_D, contraction gives a maximal
prime p of K outside S_K: a prime above 2 or 11 at the base would also
be above that rational prime in D. Thus the displayed polynomial
discriminant is a p-adic unit. In particular Simon's necessary condition
p² dividing disc(g) for an exceptional prime is false. The derivative
condition cannot reintroduce a prime failing that condition. This checks
every outside-support prime, with normalized maximal-ring valuations,
without assuming polynomial-order maximality or imposing a bound on
ramification. The imported theorem covers denominators as well as
integral coordinates; the model inverse need not be integral at the
retained primes. O is covered separately by the representative 1.
Every prime over two and eleven remains permitted.

Finally, L074 defines H_{F,S} as a subgroup of F*/F*² and defines W_S
using the induced element norm. Its norm is well-defined because at an
outside-support base prime the valuation of a norm is the residue-degree
weighted sum of the even valuations upstairs. The audited support
therefore puts the image in H_{D,S}, and the preceding square-norm
identity makes its image in H_{K,S} trivial. Neither replacing the
element norm by ideal norm nor assuming an S-unit representative is
necessary. Simon's allowed infinite support and L074's absence of sign
conditions agree. This verifies precisely the asserted containment in
W_S and retains the injection.

No premise from the uncomputed S-class norm kernel is used. The audit
secures an application of known mathematics; it supplies no new theorem
beyond Simon and no filtered dimension. ATTEMPTS/032's unfiltered-unit
obstruction and ATTEMPTS/033's local odd valuations remain intact.
The statement, mathematical argument and direct inputs are unchanged.

## Mathlib

The full supported Kummer theorem and this fixed-model specialization:
**not checked**. Supporting Kummer, elliptic model-isomorphism, field
norm and maximal-prime valuation declarations: **not checked**. Unknown
coverage is not evidence of absence. The result is KNOWN_IMPORTED;
no progress beyond Simon's cited theorem is claimed.
