# L048 — The unrestricted three-adic connecting image

## Hypotheses

Let H be L033's defining polynomial

    H(X)=X^12-6X^10+6X^9-6X^8-126X^7+104X^6+468X^5
         +258X^4-456X^3-1062X^2-774X-380,

let K=Q[X]/(H), and set A3=K tensor_Q Q3. Use L033's curves

    E0: y^2+y=x^3-x^2-10x-20,
    E1: Y^2+Y=X^3-X^2-7820X-263580,

and the dual five-isogeny theta:E1 -> E0, whose kernel is mu_5. The connecting map is identified by L033 with Kummer classes and ordinary evaluations of f=(x-4)y-4x^2+30x-55, with its good-divisor evaluations at exceptional points.

No primitive scalar or whole-fiber restriction is imposed in this lemma. No class group, global point, GRH, rank, Sha or Selmer/point equality assumption is made.

## Conclusion

The entire algebra A3 is a single degree-twelve field F over Q3, with ramification index six and residue field F9 (residue degree two). Its unrestricted connecting image is

    delta_F(E0(F)/theta E1(F)) = {1} in F^*/F^{*5}.

This certifies every local factor, rather than only one residue block or embedding. It computes neither a restricted image nor a global intersection, and excludes no integer solution or modular branch. L047's nonemptiness is a possible input to a later restricted comparison, not an input here.

## Proof

### Imported sources and the need for this specialization

The polynomial and the dual-kernel/Kummer interface are L033's inputs. The primary field source is Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents 2, 3, n*, Compositio Math. **156** (2020), 77–113, [June 10, 2019 final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf), Section 7.2, printed pp.25–27, Table 5. Its GRH-dependent Selmer calculations are not imported.

For local lifting and factorization use Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields and Adeles*, [author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf), accessible 161-page version, revision date unidentified: Theorem 1.75 and Corollary 1.77, p.57 (coprime factor/simple-root lifting), Theorem 2.8, p.64 and Proposition 2.9/Corollary 2.10, p.65 (Eisenstein irreducibility, integer ring and total ramification). Degree and residue-field accounting also use J. S. Milne, [*Algebraic Number Theory*, v3.08, July 19, 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Theorem 7.33 and Remark 7.36, pp.121–123 (coprime monic factor lifting), Corollary 7.42 and Remark 7.43, p.124 (degree ef and valuation normalization). These general results are imported under the approved assessment; no local-field theorem is reproved.

For the image use Edward F. Schaefer and Michael Stoll, *How to do a p-descent on an elliptic curve*, Trans. AMS **356** (2004), 1209–1231, [DOI](https://doi.org/10.1090/S0002-9947-03-03366-X), [June 13, 2001 long author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf), Lemmas 4.2–4.5, printed pp.6–7. Locators refer to the 34-page manuscript, not presumed published numbering. For a kernel of exponent p away from residue characteristic p, when p divides neither Tamagawa number, Lemma 4.5 identifies the connecting image with unramified cohomology; Lemma 4.2 gives its size as the number of rational kernel points. The stated theorem is imported, including Lemma 4.4's cited size formula, rather than independently reproved. Foundations/15 records the general source qualifications.

The sources do not give this explicit three-adic factor or image. The calculation below verifies the needed specialization; it is reproduction of assessed methods, with no claim of novelty beyond the sources checked.

### The entire local algebra and its actual residue field

Direct coefficient reduction gives

    H mod 3 = X^12+2X^6+1 = (X^2+1)^6.

The polynomial X^2+1 is irreducible over F3: its values at 0,1,2 are 1,2,2. Let U=Q3(i), where i^2=-1. Irreducible reduction proves that its degree is two. Its integral root has residue generating F9, so its residue degree is at least two. The degree formula forces residue degree two and ramification index one. Thus 3 is a uniformizer of U and its residue field is F9. Write v_U(3)=1 and use a bar for reduction.

Over this residue field,

    H bar = (X-i bar)^6 (X+i bar)^6.

These monic factors are coprime because 2 i bar is nonzero. Coprime Hensel factorization therefore gives monic G_+,G_- in O_U[X], both of degree six, such that

    H=G_+ G_-,
    G_+ bar=(X-i bar)^6,    G_- bar=(X+i bar)^6.

This is exact factor existence, not an approximation or an assumed factorization of a maximal global order. In particular G_-(i) is a unit: its residue is (2 i bar)^6=2 in F3. Exact substitution using i^2=-1 yields

    H(i)=837+282i = 3(279+94i).

The factor in parentheses reduces to i bar, which is nonzero. Consequently v_U(H(i))=1 and, since G_-(i) is a unit, v_U(G_+(i))=1. Moreover the monic translated polynomial G_+(i+Z) reduces to Z^6. Every coefficient below degree six is divisible by 3, and its constant coefficient has valuation exactly one. It is therefore Eisenstein over U. The same argument at -i, using H(-i)=837-282i and G_+(-i) a unit, proves G_-(-i+Z) Eisenstein as well. Both lifted factors are irreducible over U and account for the entire degree twelve after base extension to U.

Let pi be a root of G_+(i+Z), set alpha=i+pi, and let F_+=U(pi). Eisenstein gives [F_+:U]=6, total ramification, and residue field F9. To descend the factor accounting to Q3, put F0=Q3(alpha) inside F_+. This is a finite complete extension. Alpha is integral and its residue in F_+ is i bar. Thus alpha^2+1 lies in the maximal ideal of F0, while 2 alpha is a unit. Simple-root Hensel lifting in F0 supplies a root j of Z^2+1 reducing to the residue of alpha. In F_+, the root i has that residue; the other root -i has a different residue, since 2 i bar is nonzero. The uniqueness clause therefore gives j=i. Hence U is contained in F0, and pi=alpha-i is in F0 too. It follows that

    F0=F_+,    [Q3(alpha):Q3]=2*6=12.

As H(alpha)=0 and H is monic of degree twelve, H is the minimal polynomial of alpha over Q3. Thus A3 is the single field F=F_+, rather than two unrelated degree-six Q3 factors. Its ramification index is 1*6=6 and its residue degree is 2*1=2. This certifies the actual residue field and the entire dimension twelve. The two U factors are interchanged by the nontrivial U/Q3 automorphism; they are not two primes of K above three.

### Good reduction, the rational kernel and the connecting image

L033's integral models have discriminants -11^5 and -11. Both are units in O_F. They give good reduction over F, including its ramification at three, and both Tamagawa numbers are one. The isogeny has kernel exponent five, different from the residue characteristic three. All hypotheses of Schaefer–Stoll Lemmas 4.2–4.5 therefore hold over F.

A fifth root of unity in F is a unit. Its residue lies in F9^*, of order eight, so its residue must be one. The polynomial Z^5-1 has unit derivative five at one. By uniqueness in simple-root Hensel lifting, its only root in F reducing to one is one itself. Therefore

    #E1(F)[theta]=#mu_5(F)=1.

The cited theorem now says the entire connecting image has cardinality one. The identity point maps to the identity cohomology class, so this image is exactly {1}. L033's Kummer identification transports this conclusion to F^*/F^{*5}, with every exceptional good-divisor value retained. No enumeration of points or omission of an exceptional chart is involved.

### Verification, thresholds and limits

Run `python3 scripts/three-adic-image/check_image.py`. The [full arithmetic certificate](../scripts/three-adic-image/image-certificate.json) records all thirteen original/reduced coefficients, both exact values H(±i), the normalized nonzero constant residue, coprime residue separation/resultant, both discriminants and the kernel count parameters. All ten checks pass. Actual constant valuation one matches required one; the residue resultant is one and the other factor's value at i is two, both nonzero; actual total degree twelve matches required twelve. Every load-bearing arithmetic field was inspected in full using the shared JSON inspector.

The factors are not approximated in the script. Their exact existence, irreducibility, root-field descent, ramification/residue degrees and the full-image conclusion require the theorem applications and proofs above. No higher-order Newton/Montes algorithm, output stabilization, numerical precision claim, GRH calculation or unproved maximal-order decomposition is used. Full-image cardinality one meets this step's certification test. It does not establish strict shrinkage by primitive powers, emptiness of a global intersection, or an integer exclusion. The independent critical audit below confirms this input without a correction.

### Independent critical audit (2026-10-10)

The audit reuses the approved primary theorem coverage above and checks
L033's exact polynomial, isogeny direction and good-divisor interface.
`python3 scripts/three-adic-image/audit_image.py` imports no construction
code. Its [complete audit certificate](../scripts/three-adic-image/audit-certificate.json)
was inspected in full for every load-bearing arithmetic field. All 18
checks pass; no mathematical correction was found. This is independent
validation of the stated local input, not a new restriction or an
independent proof of the imported general theorems.

Integer polynomial long division, independently of the construction's
Horner evaluation, gives

    H(X)=(X^2+1)Q(X)+837+282X,
    Q(X)=X^10-7X^8+6X^7+X^6-132X^5+103X^4
         +600X^3+155X^2-1056X-1217.

Reconstruction checks all thirteen coefficients, including the zero X^11
coefficient. In F9 the two degree-six residue factors, in their specified
order, are X^6+2iX^3+2 and X^6+iX^3+2. Their full product is
X^12+2X^6+1. Translating each by its own center gives precisely Z^6:
every one of its six below-leading coefficients is zero. The opposite
factor at either center is 2, and the resultant is (2i)^36=1.
Thus both monic factors occur and are coprime, not merely distinct
approximate roots. H(±i)/3 has residue ±i; the two integer component
valuations are 3 and 1. Linear independence of 1 and i in F9 precludes
cancellation at the smaller valuation. Both constant valuations are
exactly one, as required, not just at least one. Coprime monic Hensel
lifting gives integral factors; integral translation and these reductions
justify every Eisenstein coefficient hypothesis with uniformizer 3 in U.
The constants of the exact lifted factors inherit valuation one by
dividing H(±i) by the opposite factor's unit value.

The root-field descent needs no assumed inclusion of U. F0=Q3(alpha)
is finite, hence complete. Under its embedding in F_+, the restricted
valuation has the same valuation ring and maximal-ideal tests on F0;
its residue field embeds in F9. Alpha is a unit, alpha^2+1 has positive
valuation and 2alpha is a unit. Simple-root Hensel in F0 therefore gives
a root of Z^2+1 with alpha's residue. Inside F_+ that root is i, because
the only roots are i and -i and their residues differ. Hence i belongs
to F0, followed by pi=alpha-i, so F0=F_+. Eisenstein gives the actual
residue field F9 and relative degree six. The absolute degree is twelve,
which exhausts H and makes H irreducible over Q3. Both lifted U factors
were accounted for; they do not give two Q3 factors. No factorization
of a possibly nonmaximal global power order has been substituted.

Independently calculating (c4^3-c6^2)/1728 gives, respectively,

    (c4,c6,Delta)=(496,20008,-161051),
    (c4,c6,Delta)=(375376,229985128,-11).

These are integral models with unit discriminants over F; good reduction
persists under the ramified extension and both Tamagawa numbers equal
one. The isogeny to which the theorem applies is theta:E1 -> E0 with
Galois-module kernel mu_5, as established by L033, not its dual h with
constant kernel. Residue characteristic three differs from five. In F9
all fifth roots of unity consist of 1 (also checked over all nine residue
elements); in F any fifth root is a unit and its residue must be that
root. The derivative five is a unit, so uniqueness in the residue disk
of 1 excludes further roots in F. Schaefer–Stoll Lemmas 4.2 and 4.5
therefore give image cardinality one under exactly their hypotheses.
The identity point fixes the class as 1 under Kummer. L033's good-divisor
construction applies at all points, including T and O, so no exceptional
function value is omitted. Actual degree twelve and both constant
valuations one meet their required thresholds. No restricted-image
comparison, global class evaluation or branch exclusion was performed.

## Mathlib

Full matching local-algebra certificate and explicit connecting-image specialization: **not checked**. Supporting Hensel, Eisenstein, local ramification/residue, isogeny and Galois-cohomology declarations: **not checked**. Unknown coverage is not evidence of absence. The general source results are imported by precise citation, with every local hypothesis justified above.
