# L024 — Local witnesses for reduced multiplication

## Hypotheses

Work in the free noncommutative polynomial ring over F₂. The only free inputs are the original variables x and independent placeholders t for the original clause, Boolean and pair-once commutator axiom list A(x) of L021. Degree is formal polynomial degree after cancellation in independent x,t, before substituting A. Circuits are division-free, fan-in two, with ordered multiplication and sharing. All identities below are formal identities, not just Boolean equivalences.

Let a,b,z,w be supplied x-only reduced values. They may be shared circuits; they are not new free variables. For a proposed AND gate with reduced operands a,b and reduced output z, supply circuits H,B_a,B_b,K_ba,K_aw,K_bw over x,t. All six vanish at t=0 and satisfy

H(x,A)=z+ab,
B_a(x,A)=a²+a,                 B_b(x,A)=b²+b,
K_ba(x,A)=ba+ab,
K_aw(x,A)=aw+wa,               K_bw(x,A)=bw+wb.                    (1)

The local witness H need not correct the difference between z and any unreduced extension-value circuit. Existence of polynomial-size/degree values and witnesses satisfying (1) for arbitrary ER definitions is not asserted. The witnesses may be nonlinear in placeholders.

Let d,h>=1 bound, respectively, the formal degrees of the four reduced values and all six supplied witnesses. Let S include every node of their common input DAG, with original input labels and the axiom list accounted for separately in binary cost.

For certificate transport, let Q(x,t) be any supplied root with Q(x,0)=0. A surrounding certificate C may be L021's certificate or any supplied polynomial satisfying C(x,0)=0 and C(x,A)=1. When transporting a contribution, assume a displayed additive decomposition C=C_rest+(ab)Q, or C=C_rest+Q(ab). This is a conditional local operation; no efficient enumeration of all such contributions in an arbitrary DAG is assumed.

## Conclusion

Put p=ab and construct

M = a K_ba b+B_a b²+a B_b,
B_z = M+H z+p H+H,
K_zw = a K_bw+K_aw b+H w+w H,
D_1 = B_a b+a K_ba+H(1+a),
D_2 = a B_b+H(1+b),
D_3 = M+H p.                                                     (2)

Each output vanishes at zero placeholders. After t=A(x), they respectively equal

p²+p,  z²+z,  zw+wz,  z(1+a),  z(1+b),  (1+z)ab.                (3)

Thus D_1,D_2,D_3 witness the three defining-clause polynomials in definition order, even when z differs formally from ab. Negative literal values are handled by replacing a or b with their supplied signed values; no commutation is implicit.

All six outputs have degree at most h+2d. Their common construction adds at most 40 arithmetic gates to the shared inputs. With densely numbered references its binary length is O((S+1)log(S+2)) plus the supplied label and axiom-list encoding. Writing the fixed six outputs separately changes only a constant factor. This is simultaneous control of complete local witness size and degree, including all correction sectors.

In the two displayed orientations, replace the contribution by

zQ+HQ,                         or Qz+QH.                         (4)

The resulting full certificate retains both formal IPS identities. Each replacement adds at most three gates beyond its supplied roots and has degree at most deg(Q)+max(d,h). Nonlinear placeholder dependence is explicitly allowed; (4) does not assert placeholder linearity.

On the repeated-square diagnostic with every reduced value equal to x and every local relation witness equal to the original Boolean placeholder beta, the recursively transported Boolean witnesses have O(k) shared gates and formal degree exactly 2k+1 after k updates. All local outputs at update k have degree at most 2k+3. This verifies a linear-degree propagation example with the correction retained, as opposed to an exact lift of the exponentially high-degree unreduced value.

This passes the covered local multiplication test conditionally and permits testing a global propagation recurrence. It does not yet give a general ER-wide construction, the existence of the supplied reduced data, small trees, an arbitrary-circuit identity verifier, an all-certificate lower bound or a decision separation. The result is potentially beyond the checked full-statement comparison, with no originality claim.

## Proof

**Product Booleanity and relation transport.** L020's ordered product-Booleanity identity supplies M. Explicitly its substituted value is

a(ba+ab)b+(a²+a)b²+a(b²+b)=abab+ab=p²+p.

The two a²b² terms and the two ab² terms cancel. This retains the commutator correction. Set e=z+p, the substituted value of H. Then

e z+p e+e=z²+p²+z+p,

because the two pz terms cancel, without reversing any factors. Adding M(A)=p²+p gives z²+z. In particular H z+p H+H is required for transporting Booleanity; a witness for z+p alone is not a witness for z²+z.

For the commutator output, substitution in its first two terms gives

a(bw+wb)+(aw+wa)b=pw+wp.

The two awb terms cancel. The remaining terms substitute to e w+w e=zw+pw+wz+wp. Their sum is zw+wz. No Booleanity of w is needed.

**All defining clauses.** Again retaining multiplication order, the first two uncorrected parts evaluate to

(a²+a)b+a(ba+ab)=ab+aba=p(1+a),
a(b²+b)=p(1+b).

Adding e(1+a) or e(1+b) changes these to z(1+a) or z(1+b). For the third clause,

M(A)+e p=p²+p+(z+p)p=p+zp=(1+z)ab.

These are exactly the falsity products of (NOT z OR a), (NOT z OR b), and (z OR NOT a OR NOT b) in their stated order. Signed values obey 1+(1+r)=r over F₂, so the same formulas apply to signed gate inputs. Every summand of (2) contains a supplied zero-at-zero witness, so all outputs vanish at t=0. They introduce no augmented-axiom placeholder. Arbitrary clause sorting and duplicate deletion would additionally use the commutator and Boolean witnesses in the prescribed positions; no global normalization bound is proved here.

**Full local bounds.** The three terms of M have degrees at most h+2d,h+2d,h+d. The extra terms of B_z have degrees at most h+d,h+2d,h. The terms of K_zw have degree at most h+d. D_1 and D_2 have degree at most h+d, and D_3 at most h+2d. These are bounds on polynomials in the full free ring, including every placeholder sector, not degrees after the axiom substitution. Semantic degree bounds on supplied roots suffice even if their syntactic degrees are larger.

A conservative binary-gate count is: one gate for p; seven for M; five additional for B_z with p reused; seven for K_zw; six for D_1; four for D_2; and two for D_3. This is 32 gates even without every possible reuse, so 40 is a uniform allowance. Input roots are shared; no occurrence trees are unfolded. Numbering the common DAG yields the binary bound. If d,h and the supplied full encodings are polynomial in ER length T, the complete local size and degree are polynomial in T. This does not yet prove that a repeated global construction keeps those assumptions.

**Both certificate identities.** By (1), (z+H)(x,A)=z+(z+ab)=ab. Therefore (zQ+HQ)(x,A)=(ab)Q(x,A), and (Qz+QH)(x,A)=Q(x,A)(ab). At zero placeholders both replacements vanish because Q(x,0)=H(x,0)=0. Substitution in any fixed additive surrounding C_rest now retains C(x,0)=0 and C(x,A)=1. L021 supplies such identities when C is its certificate; the applicability argument does not require reproducing its construction. The degree and three-gate bounds follow directly from (4). These products may multiply two placeholder-dependent roots, so no inherited placeholder-linearity claim is made. They correct a reduced **local** product ab to z; they do not carry a correction from an unreduced value to z.

**Repeated squaring with only local relations.** Take one original variable x and original Boolean polynomial x²+x with placeholder beta. At every stage let a=b=z=x, set H=beta and K_ba=0, and start B_0=beta. With B_a=B_b=B_k, (2) gives

B_(k+1)=B_k x²+x B_k+beta x+x² beta+beta.                         (5)

Induction from the proved Booleanity transport gives B_k(x,x²+x)=x²+x and B_k(x,0)=0. The local relation is always x+x², regardless of the exponential degree of the unreduced repeated-square circuit. Each stage adds at most a constant number of gates, reusing B_k and x, so the shared network has O(k+1) nodes and O((k+1)log(k+2)) bits. The degree upper recurrence is deg B_(k+1)<=max(deg B_k+2,3), hence deg B_k<=2k+1.

This bound is exact. B_0 contains beta with coefficient one. B_1 contains the word beta xx with coefficient one. For k>=1, if B_k contains beta x^(2k), then in (5) the first summand alone contributes beta x^(2k+2): x B_k starts with x, and the three new local terms have degree at most three. Thus that word survives. Its length 2k+3 proves the next lower bound. Induction gives deg B_k=2k+1. Formula (2), with d=1 and h=2k+1, bounds every local output by 2k+3. This is an asymptotic proof of the diagnostic, not an inference from a finite table. Witnesses for the local defining clauses are included in this bound. No claim about the optimal certificate of an original CNF is made; even supplying all these local data leaves the global assembly obligation.

**Verification.** Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-reduction/check_reduced_product.py`. Free-word expansion checks all six universal identities and their zero identities, both contribution orientations, and three concrete gates: idempotent AND, a signed complementary pair, and a reordered product corrected by an original commutator. Five corrupted corrections are detected. Repeated-square expansion through k=8 checks both substitutions, exact Boolean-witness degree and bounds on every local output. Full small certificates are saved in `scripts/coefficient-reduction/reduced-product-results.json`. The proof above supplies the all-k statement and the local bounds; these computations do not certify a complete P-versus-NP argument.

## Mathlib

Coverage: **not checked** for this full reduced-product transport, degree bound or binary accounting. The ordered identities and all-k diagnostic are proved here. Li–Tzameret–Wang, [*Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, Lemmas 3.6–3.7](https://arxiv.org/pdf/1412.8746v4), supplies supporting formal formula-commutation mechanisms. Forbes–Shpilka–Tzameret–Wigderson, [*Proof Complexity Lower Bounds from Algebraic Circuit Complexity*, Theory of Computing 17(10), 2021, §4.2, Propositions 4.5–4.6 and Lemma 4.9](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf), supplies supporting commutative correction constructions under restricted representation/degree assumptions. Neither is a checked full match for the present supplied-local-relation, shared noncommutative statement. The difference from those results and L020 is the reduced output z, its local formal relation witness, and complete witness/transport degree accounting. No theorem on arbitrary canonical multilinearization is imported or reproved; the prior assessment's conditional Hrubeš obstruction is not a premise here.
