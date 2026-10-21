# L039 — The whole fiber at two realizes both restricted local images

## Hypotheses

Work over Q5. Let A=Q5[k]/(m) be L033's entire degree-twelve algebra,
with m exactly as displayed in L038. Let E0, its modular map j and its
connecting map delta be those of L033–L035. Let B_2 be the coordinate
algebra of the whole scheme-theoretic fiber j=2. Let I_pow and I_fiber
be exactly L035's sets, allowing every whole-fiber isomorphism and using
one primitive scalar witness shared across all factors. No global
solution, GRH, rank, Sha, class basis or finite precision bound is assumed.

## Conclusion

For U_11 the unramified degree-eleven extension of Q5,

    B_2 is isomorphic to Q5 x U_11, and hence to A.
    I_pow and I_fiber are both nonempty.

This does not decide I_pow=I_fiber versus strict inclusion, compute their
classes, or exclude a global twist or any integer solution.

## Proof

### Presentation retains the entire fiber

Use L034's exact polynomials a,b,d,h,J, with d=(x-16)^11,
J=2a-b and a^2-ab-b^2g=-d h^3, where g=x^3-x^2-10x-20.
Set F2=h^3+2J-4d. Its ascending coefficients are

    [937879192455631322195, 1429561710781312402938,
     1109381808610629761636, 496978970443495172182,
     135569224509547150575, 18450202249217732554,
     353813357111952034, -239703196889826868,
     11173115113378933, -147711160675694,
     8460097184, -155492, 1].

The script below verifies the elimination identities by exact integer
polynomial multiplication. Exact Sylvester determinants with checked
Bareiss divisions give Res(F2,b) nonzero and Res(F2,F2') nonzero;
their full integers are in the certificate's coordinate object. Also
F2(16)=10012538174581290616938483 is nonzero. Thus F2 has twelve distinct
geometric roots, none a zero of b or d. At each root, reconstruct

    y=(2d-a)/b.

The elimination identity

    (2d-a)^2+b(2d-a)-b^2g=-d F2

proves y^2+y=g, and the map formula gives j=2. Conversely, L034's pole
and exceptional-coordinate analysis retains every point: O and 3T
are poles, while the remaining point with x=16, namely 2T, has j=-121,
not 2. Any point of the fiber with b=0 and d nonzero would satisfy F2=0
by the same elimination identity, contradicting Res(F2,b) nonzero.
Every fiber point therefore has the displayed reconstruction. L034's
map has degree twelve and branch values only 0,1728,infinity; hence this
fiber is étale of dimension twelve. The twelve reconstructed distinct
points exhaust it, proving B_2=Q5[x]/(F2), including its full algebra.

### Complete local factor identification

Reduction modulo five and multiplication give

    F2bar=x H2,
    H2=x^11+3x^10+4x^9+x^8+3x^7+2x^6+4x^5
       +4x^4+2x^2+x+3.

In particular H2(0)=3. The certificate records R_0=x and every
R_(i+1)=R_i^5 mod H2 through R_11=x. The only prime divisor of eleven
is eleven. For r=R_1-x, ascending coefficients are

    r=[0,4,0,0,0,1],
    u=[2,1,2,1,1],
    v=[0,1,2,1,0,4,2,3,1,1,4].

Exact multiplication gives u H2+v r=1 in F5[x]. Therefore H2 divides
x^(5^11)-x and is coprime to x^5-x. The former polynomial is squarefree
(derivative -1), and its irreducible factors have degrees dividing eleven,
by the Frobenius orbit description of finite fields. Only degrees one
and eleven are possible; the latter coprimality excludes degree one.
Since H2 has degree eleven, it is irreducible. The degree-one factor x
is irreducible. An explicit coprimality witness for the two factors is

    u0=[3,1,0,2,2,1,4,3,2,4,3],  v0=[2],
    u0 x+v0 H2=1.

Import J. S. Milne, *Algebraic Number Theory*, [v3.08, July 19,
2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Theorem 7.33 and
Remark 7.36, pp.121–123; Corollary 7.42 and Remark 7.43, p.124; and
Proposition 7.50 and its proof, pp.127–128. These are the assessed
coprime Hensel lifting, degree formula [L:Q5]=ef, and classification
of unramified extensions by residue fields. F2 is monic integral, and
its displayed monic residue factors are coprime. They therefore lift
to coprime factors of degrees one and eleven, accounting for all twelve
dimensions. Each lifted factor has irreducible reduction, hence is
irreducible over Q5: any monic factorization would have integral
coefficients, since its roots are integral, and would reduce to a
positive-degree factorization. A root of the degree-eleven factor has
residue degree at least eleven. The degree formula forces f=11 and e=1;
the finite residue extension is separable. Thus its field is unramified
and is U_11 by the cited classification. The degree-one field is Q5.
The Chinese remainder theorem yields the claimed complete product.

L038 already identifies A with Q5 x U_11. Pair the degree-one factors
and the degree-eleven factors using the unramified classification.
This gives an isomorphism of the entire algebras B_2 and A, with both
dimension totals twelve. No ramified-field invariant, guessed root or
stabilized precision is used. General local-field theory is imported;
the explicit coefficient specialization needs its own arithmetic because
neither the sources nor L038 compute B_2.

### Primitive scalar witnesses and nonemptiness

Since 1728 is a 5-adic unit congruent to 3, both t=2/1728 and
q=1-t=1726/1728 are units. L036's case 1 applies with both valuations
zero; equivalently 2 belongs to 2+5 Z5 in its exact domain. Its proved
construction supplies nonzero a,b,c in Z5, with at least one unit,
a^3+b^4=c^11 and 2=1728 a^3/c^11, using the same c in both identities.

Choose the whole-fiber isomorphism above. L035 gives its point P in
E0(A). Combine it with this common scalar witness: delta(P) lies in
I_pow and thus I_fiber. It is a defined fifth-power class. Indeed no
fiber point is O or T, whose map values are infinity and -24729001;
L033's f has its only zero and pole there, so f(P) is invertible in A
and delta(P)=[f(P)]. This establishes nonemptiness without a global
integer witness or an assertion that either set is a subgroup.

### Exact evidence

Run `python3 scripts/full-fiber-at-two/check_factors.py`. The complete
[certificate](../scripts/full-fiber-at-two/factor-certificate.json)
contains source coefficients, F2, all three exact nonzero coordinate
checks, every Frobenius remainder, Bezout witnesses and bounds. The
complete load-bearing coordinate values, F2, remainders and witnesses
were inspected. Factor multiplication, irreducibility and coprimality
checks pass; dimensions actual=12, required=12, pairwise resultant
valuation actual=0, required=0. There are no failures or precision
cutoffs. Arithmetic helpers reproduce the existing exact finite-field
and Bareiss methods while preserving their scripts and certificates.

### Independent critical audit, 2026-10-08

No correction is needed. Run
`python3 scripts/full-fiber-at-two/audit_factors.py`; the separate
[audit certificate](../scripts/full-fiber-at-two/audit-certificate.json)
records 74 passing checks and no failures. This implementation imports no
construction code. It compares every coefficient of a,b,d,h,J with L034's
previously source-audited certificate, and m with L033's displayed defining
polynomial. It reuses the primary theorem coverage cited above, rather
than claiming a fresh source retrieval or reproof of local-field theory.

For x=0,...,24, it checks the definitions of d,h,b,J,F2 and both
elimination identities. Their degree bounds are respectively
11,4,10,11,12,23,23. The largest bound follows from deg(b^2 g)=23 and
deg(d F2)=23, while deg(a^2) and deg((2d-a)^2) are at most 22.
Twenty-five distinct exact zeros exceed every bound, so these are
polynomial identity certificates, not numerical sampling. Every residual
is saved and was inspected.

The two coordinate resultants are independently computed as determinants
of multiplication by b and F2' on Q[x]/(F2), in the basis
1,x,...,x^11. Monic polynomial reduction gives the columns; ordinary
Gaussian elimination over Q gives the determinants, without using the
original Sylvester matrices or Bareiss division. For monic F2 this
determinant equals the resultant: after scalar extension, multiplication
has eigenvalues q(r), with algebraic multiplicities, for the roots r of
F2. This identity does not require squarefreeness in advance. Both full
integers agree with the construction certificate and are nonzero.
F2(16) agrees as well. Thus b is invertible in the quotient, F2 is
squarefree and x-16 is invertible. Reconstruction gives all twelve
distinct points, and L034's degree-twelve finite locally free map leaves
no additional point or multiplicity. Independently checked torsion
numerators are zero at 2T and 81402749386839761113321 at 3T;
h(16)=214358881 gives the removable value -121. The leading terms at O
give its simple pole. Hence neither infinity nor either x=16 point is
lost in passing to this fiber presentation. The recorded j(T) is also
checked exactly.

For both m and F2 the audit multiplies the entire residue factorization,
checks multiplicity one, and verifies the polynomial Bezout identity
between the two factors. It independently recomputes every Frobenius
remainder using (sum c_i x^i)^5=sum c_i x^(5i) in F5[x], followed by
monic reduction, rather than the construction's binary powering.
Both degree-eleven sequences close at x and both proper-degree Bezout
identities give one; the degree-one factors are exactly x. The full
sequences and witnesses were inspected, including the A side of the
pairing. Thus the hypotheses of the cited coprime Hensel theorem hold
over Z5 for both monic integral polynomials. Every resulting field has
residue degree equal to its degree, hence ramification index one.
Unramified classification pairs the linear factors and the entire
degree-eleven fields. The dimension totals are 12 and 12, as required;
the mutual factor resultants have valuation zero on both sides. This
argument identifies whole algebras, not merely a selected factor or a
matching list of degrees of potentially ramified fields. It needs no
p-adic precision cutoff.

Finally the specialization of L036 can be written without any implicit
choice of different denominators: take b=1, choose the unique unit c with
c^11=864/863, and the unique unit a with a^3=1/863. Modulo five the
respective root residues are c=2 and a=3; both polynomial derivatives
are units. Clark's cited Hensel theorem therefore supplies these exact
roots. They satisfy a^3+1=864/863=c^11 and
1728 a^3/c^11=2, with all three coordinates units. This is precisely
L036's construction at the fixed scalar, not a global integer witness.
Any of the complete algebra isomorphisms just established transports the
universal fiber point to E0(A), with the same scalar 2 on both factors.
L033's map and divisor statements are defined over Q and apply over
each factor without assuming an original integer solution. Since this
fiber contains neither T nor O, f is invertible on its entire algebra.
The resulting class is therefore in I_pow by L035's definition, and in
I_fiber by inclusion. No additional compatibility with a chosen
isomorphism is imposed by those definitions.

This verifies the existing nonemptiness conclusion only. It establishes
no new image restriction, strictness/equality decision, global intersection
or integer exclusion. The direct mathematical inputs in the DAG remain
unchanged; no complete Beal candidate is claimed.

## Mathlib

The full explicit fiber comparison, its certificates and restricted-image
nonemptiness: **not checked**. Supporting Hensel lifting, finite-field,
Chinese remainder and unramified-classification declarations: **not
checked**. Unknown coverage is not absence. This is REPRODUCTION of
assessed local-field methods for a particular pair; no general novelty
or progress beyond those methods is claimed.
