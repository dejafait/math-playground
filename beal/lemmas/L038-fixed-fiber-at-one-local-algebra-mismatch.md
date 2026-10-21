# L038 — The whole fiber at one does not match the local algebra

## Hypotheses

Work over Q5. Let A=Q5[k]/(m), using the entire algebra of L033, where

    m=k^12-6k^10+6k^9-6k^8-126k^7+104k^6+468k^5
      +258k^4-456k^3-1062k^2-774k-380.

Let B_1 be the whole modular fiber at j=1 of L034. That result proves
B_1=Q5[x]/(F1), including reconstruction of y and all twelve points. The
ascending coefficient list of its monic polynomial F1=h^3+J-d is

    [937983888243151557338, 1429362010445765709011,
     1109222316649640440863, 496972133527726231221,
     135598893953462791071, 18454277087138301761,
     352678500146970855, -239867260458531398,
     11168042485075058, -147749484447433,
     8416976909, -156975, 1].

No primitive integer solution, GRH, rank, Sha condition, global basis or
chosen p-adic precision is assumed.

## Conclusion

For U_d the unramified extension of Q5 of degree d,

    A is isomorphic to Q5 x U_11;
    B_1 is isomorphic to U_6 x U_6.

Consequently B_1 is not isomorphic to A as a Q5-algebra. This rejects the
fixed scalar j=1 as a whole-fiber realization. It proves neither emptiness
of the compatible images over other scalars nor an integer exclusion.

## Proof

### Exact residue data and irreducibility

All coefficients in this subsection are in F5. Direct reduction and
polynomial multiplication give

    mbar = x H,
    F1bar = P Q,
    H = x^11+4x^9+x^8+4x^7+4x^6+4x^5+3x^4+3x^3+4x^2+3x+1,
    P = x^6+4x^5+4x^4+2x^3+2x^2+x+2,
    Q = x^6+x^5+x^4+2x^3+2x^2+x+4.

Here H(0)=1. P and Q are distinct. The following exact checks certify that
H,P,Q are irreducible; they do not rely on the exploratory trial-factor
algorithm. For a monic g of degree n define R_0=x mod g and
R_(i+1)=R_i^5 mod g. Check R_n=R_0 and, for each prime ell dividing n,
check gcd(g,R_(n/ell)-x)=1. Indeed the first equality says g divides
x^(5^n)-x, whose derivative is -1, so g is squarefree. Its irreducible
factors have degrees dividing n: a root of degree d over F5 has a Frobenius
orbit of length d and is fixed by the nth Frobenius exactly when d divides
n. If a proper divisor d of n occurred, some prime ell dividing n/d would
give d dividing n/ell, contradicting the corresponding gcd check. Thus all
factors have degree n and g itself is irreducible. This explains the exact
finite-field arithmetic test used here; no conjectural factoring input is
required.

The complete R_i sequences, all Bezout witnesses, and the original
polynomials are in the [certificate](../scripts/full-fiber-at-one/factor-certificate.json).
For clarity, the nontrivial proper-degree tests are listed below, with
ascending coefficients. In every row, r=R_i-x, and the recorded u,v obey
the exact polynomial identity u g+v r=1 in F5[x].

| g | i | r | u | v |
|---|---|---|---|---|
| H | 1 | [0,4,0,0,0,1] | [1,3,1,4,4] | [1,4,2,2,0,1,1,2,3,1,1] |
| P | 3 | [1,1,2,4,4,1] | [1,1,1,0,1] | [4,3,4,4,0,4] |
| P | 2 | [2,1,4,3,2,4] | [4,2,0,1,2] | [4,4,0,4,3,2] |
| Q | 3 | [1,3,1,2,3,1] | [2,4,4,2,3] | [3,3,4,0,4,2] |
| Q | 2 | [3,1,1,4,2,3] | [2,0,4,4,3] | [1,4,0,1,0,4] |

The final Frobenius remainders are R_11=x for H and R_6=x for P,Q.
`python3 scripts/full-fiber-at-one/check_factors.py` reproduces every
remainder by exact modular polynomial arithmetic, multiplies the complete
residue factorizations, verifies all displayed Bezout identities, and
checks both dimension sums against twelve. The full sequences and witnesses
were inspected. Degree-one x is irreducible directly. Pairwise coprimality
of x,H and P,Q also has exact Bezout witnesses in the certificate; it
follows already from irreducibility and their distinctness.

### Lifting every factor and identifying its field

Import J. S. Milne, *Algebraic Number Theory*, [v3.08, July 19,
2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Theorem 7.33 and
Remark 7.36, printed pp.121–123: over a complete discrete valuation ring a
monic polynomial with pairwise coprime monic residue factors has a unique
lifting to monic factors of the same degrees. Apply this to Z5 and each of
the two displayed complete residue factorizations. Both inputs are monic
and integral and both pairs are coprime. Thus m has lifted factors of
degrees 1,11 and F1 has lifted factors of degrees 6,6. Their mutual
resultants are units, because the residue resultants are nonzero. Hence
they are coprime over Q5 and the Chinese remainder theorem gives the
complete product algebras. Both dimension sums are exactly twelve.

Each lifted factor is irreducible over Q5. If a monic integral factor
with irreducible reduction factored into monic positive-degree polynomials
over Q5, all their coefficients would lie in Z5: its roots are integral,
so coefficients formed from subsets of roots are integral and their
intersection with Q5 is Z5. Reducing would contradict residue
irreducibility; monicity preserves both positive degrees.

For a lifted factor of degree d, its root alpha is integral in the
resulting degree-d field L. Its residue is a root of the degree-d
irreducible residue factor, so the residue degree f of L is at least d.
Milne Corollary 7.42 and Remark 7.43, printed p.124, give [L:Q5]=ef.
Therefore f=d and e=1. The residue extension is finite and separable,
so L is unramified. Milne Proposition 7.50 and proof, pp.127–128,
classify these unramified extensions by their residue extensions. The
unique degree-d finite field over F5 identifies L with U_d. This imports
the standard classification; no ramified-field comparison is needed.

The complete factor-degree multisets [1,11] and [6,6] differ. A field
product's primitive idempotents and their Q5 dimensions are intrinsic and
preserved by every Q5-algebra isomorphism. An isomorphism would have to
pair all factors with equal degrees, which is impossible. This proves the
negative decision without selecting a factor or comparing polynomial-order
discriminants. The scalar's primitive-witness admissibility alone cannot
overcome this whole-fiber mismatch.

## Mathlib

The full explicit algebra comparison and its particular factor certificates:
**not checked**. Supporting coprime Hensel lifting, finite-field
irreducibility, Chinese remainder and unramified-classification declarations:
**not checked**. Unknown coverage is not absence. This is an exact local
calculation using assessed standard theorems, classified REPRODUCTION;
the search did not identify a published comparison for this explicit pair,
and no general novelty is claimed.
