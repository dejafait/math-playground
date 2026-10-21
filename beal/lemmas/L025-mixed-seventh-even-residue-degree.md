# L025 — Conditional even residue degree at the modular coefficient primes

## Hypotheses

Let X,Y,Z be signed nonzero integers with X^5+Y^3=Z^7 and gcd(X,Y,Z)=1. Assume exactly the exceptional-algebra hypothesis

\[
\mathbb Q[T]/(15T^7-35T^6+21T^5-X^5/Z^7)
\simeq\mathbb Q[T]/(T^7-483T^2+3955T-3945).
\]

Use L020's geometric covariant Tate component of the Jacobian over F=Q(sqrt(5)), and the base prime q=(29,sqrt(5)-11). For each of its two coefficient embeddings iota, take any L024 triple (f_iota,lambda_iota,j_iota) realizing the stated residual isomorphism. Write K_iota for the newform coefficient field, k_iota=O_(K_iota)/lambda_iota, and

\[
d_{\lambda_iota}=[k_iota:\mathbb F_7].
\]

The form has parallel weight two, trivial character and L024's exact level (3)^e3(sqrt(5))^e5 with e3,e5 in {2,3} and all its coordinate clauses retained. The identification is over the algebraic closure of F_7 through j_iota. It does not identify k_iota with the geometric residue field F_49.

## Conclusion

For each iota and every such realizing triple,

\[
2\mid d_{\lambda_iota}.
\]

More precisely, if r is the reduction of t=-X^5/Y^3 at q, then r is one of 14,10,25,15, and the image under j_iota of the newform's q-Hecke eigenvalue modulo lambda_iota has degree exactly two over F_7 and is a root of the corresponding L016 polynomial. The four polynomials are irreducible over F_7. To display their complete factorizations, let w in F_49 satisfy w^2=5:

| r | Polynomial over F_7 | Discriminant in F_7 | Factorization over F_49 |
| --- | --- | --- | --- |
| 14 | T^2+6T+6 | 5 | (T-(4+4w))(T-(4-4w)) |
| 10 | T^2+6T+4 | 6 | (T-(4+w))(T-(4-w)) |
| 25 | T^2+4 | 5 | (T-4w)(T+4w) |
| 15 | T^2+2T+3 | 6 | (T-(6+w))(T-(6-w)) |

An odd-residue-degree prime cannot supply either required L024 identification. This is a necessary condition on the primes realizing those identifications, not on every prime above 7 of the same form. It gives no equality d_lambda=2, no condition replacing d_lambda by [K_iota:Q], and no elimination of actual forms without their prime-splitting data.

## Proof

**Sources and scope of the specialization.** The general field criterion is imported from Keith Conrad, *Finite Fields*, Theorem 3.3 and its first proof, p. 6, with the subfield formulation in Theorem 2.8, p. 5, and the conjugacy statement in Theorem 5.5, p. 10, [primary notes](https://kconrad.math.uconn.edu/blurbs/galoistheory/finitefields.pdf), version retrieved 2026-10-05. For an irreducible polynomial of degree m over F_7, a root belongs to F_(7^d) if and only if m divides d. We cite this theorem rather than reprove it. The definition of number-field residue degree used here is J.S. Milne, *Algebraic Number Theory*, v3.08 (19 July 2020), pp. 59–60, [primary notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf). Number fields are finite separable extensions; O_K/lambda is a finite field of characteristic 7, of order 7^d_lambda. No Galois assumption on K_iota is made. The prepared SPECIALIZE assessment covers this field criterion and L020/L024's interface. What is reproduced here is the four-polynomial arithmetic and its conditional application; no originality is claimed.

**Factorization and exact root degrees.** The squares in F_7 are precisely 0,1,2,4: squaring 0,1,2,3 gives these four values and squaring their negatives adds none. For the four monic quadratics, the discriminants, computed in the displayed order, are

\[
6^2-4\cdot6=12\equiv5,\quad
6^2-4\cdot4=20\equiv6,\quad
0^2-4\cdot4=-16\equiv5,\quad
2^2-4\cdot3=-8\equiv6\pmod7.
\]

Neither 5 nor 6 is a square. In characteristic different from two, a monic quadratic has a root exactly when its discriminant is a square, by the identity (2T+b)^2=b^2-4c at a root of T^2+bT+c. A degree-two polynomial is reducible exactly when it has a root. Thus all four are irreducible over F_7 and their roots have degree exactly two.

Since 5 is a nonsquare, F_7[w]/(w^2-5) is a field with 49 elements. The inverse of 2 is 4. Square roots of the two discriminants in this field are w for 5 and 2w for 6, since (2w)^2=20=6. The quadratic formula gives the table. Direct multiplication also checks every entry: the root sums and products are respectively (1,6), (1,4), (0,4), and (5,3). Indeed 4^2-(4w)^2=16-80=-64=6; 4^2-w^2=11=4; -(4w)^2=-80=4; and 6^2-w^2=31=3, all modulo 7. These sums give the negative linear coefficients as required. Each root has a nonzero coefficient of w, hence none belongs to F_7. The two roots in each row are interchanged by seventh-power Frobenius: w^7=w(5^3)=-w. This explicitly retains both conjugates rather than selecting one.

**Transfer to each newform coefficient prime.** Fix iota and a realizing L024 triple. L020, using its conditional parameter bridge, gives 29 not dividing XYZ, r in {14,10,25,15}, good reduction at q, and

\[
\overline P_r(\operatorname{tr}\rho_iota(\operatorname{Frob}_q))=0.
\]

The same relation holds through the other geometric coefficient embedding; the parameter r is rational and does not depend on that embedding. The prime q is away from 7 and from L024's level, which is supported only at the base primes above 3 and 5. The unramified Hecke-trace normalization of L024 therefore gives

\[
\operatorname{tr}\rho_iota(\operatorname{Frob}_q)
=j_iota(\overline{a_q(f_iota)}).
\]

Here a_q(f_iota) is the integral q-Hecke eigenvalue, its bar denotes reduction in k_iota, and arithmetic Frobenius is the same covariant convention used in L020/L024. Trace is preserved by the residual isomorphism and by semisimplification. There is no inverse-Frobenius substitution or additional twist.

The field embedding j_iota fixes F_7, so its image is a field of order 7^d_lambda. It contains a root of the irreducible quadratic P_r. Conrad's cited theorem with m=2 now forces 2 to divide d_lambda. Equivalently the root generates the unique F_49 subfield inside that image. This does not force equality of the entire newform residue field with F_49. Repeat the argument separately for the other iota. The forms, primes and identifications may differ, so the proof does not impose an unproved common coefficient field or common prime.

**Achieved threshold and limitations.** Odd residue degree is excluded for any prime actually realizing an L024 identification in the assumed algebra branch. At the polynomial level, even degree is also sufficient to contain both roots of each row, by the same cited theorem; it is not sufficient to realize the residual representation or arise from a solution. L017/L020's earlier exclusion concerns reducible representations with trace 2 or -2. Here the criterion concerns the field containing a particular Frobenius trace, including irreducible representations; trace degree alone does not decide representation irreducibility. Thus the criterion can prefilter independently certified coefficient-prime data, but is neither a packet-exhaustion proof nor a repeat of the reducible-sector contradiction. No splitting list or actual eliminated form is supplied. Irreducible-sector exhaustion, global exceptional-algebra applicability and all other residual signatures remain unresolved. The full-space source blocker, L023's type-to-level blocker and the historical corrected-filter evidence are unaffected.

**Separate critical audit, 2026-10-06.** Reconstructing the quadratics from L016's integer rows via b=-A and c=B-58 gives these complete lists of values at 0,1,2,3,4,5,6 in F_7:

| r | Values of T^2+bT+c |
| --- | --- |
| 14 | 6,6,1,5,4,5,1 |
| 10 | 4,4,6,3,2,3,6 |
| 25 | 4,5,1,6,6,1,5 |
| 15 | 3,6,4,4,6,3,2 |

None is zero. Independently enumerating all 49 pairs representing a+bw gives exactly the two roots in each displayed factorization, with the stated sums and products; seventh powers swap those roots in all four rows. Run `python3 scripts/mixed-seventh-certificate/audit_residue_degree.py`; the complete evaluations and checks are in `scripts/mixed-seventh-certificate/residue-degree-audit.json`. These computations check finite arithmetic only. Nonsquareness of 5 justifies the extension-field model; Conrad's cited theorem supplies divisibility for every d_lambda, without a bounded degree search.

The full L020/L024 interface was checked separately. Signed primitive nonzero coordinates and the exact algebra isomorphism coincide with the hypotheses here. L020 supplies the four rational parameter residues and good-reduction trace relation for both embeddings. Its determinant 29 on each rank-two component gives B-58. L024 uses the same substitutions (a,b,c)=(X,-Z,Y) and t=-X^5/Y^3. In every e3/e5 coordinate clause its level is supported only above 3 and 5, so q is away from both the level and 7. Its integral unramified Hecke trace therefore reduces to the same arithmetic-Frobenius trace, with no twist or parameter change. This uses the existing source-backed Hecke normalization, not an independent reproof of PVT's theorem.

Fixing any realizing triple before applying the trace identity checks the universal quantifier over such triples. Its j fixes F_7, so the same irreducible quadratic applies; degree two of a root is not degree two of its containing field. Applying this separately to the second embedding needs no common form or prime. No arithmetic or quantifier correction was needed, and no new dependency or stronger conclusion follows. Splitting data, packet exhaustion, an independent verification of PVT's proof and global applicability of the algebra hypothesis are outside this audit.

## Mathlib

Full conditional even-residue-degree statement: **not checked**. Supporting finite-field subfield, polynomial factorization, residue-degree and Hilbert-newform trace declarations: **not checked**. Conrad and Milne supply the general imported field results; L020 and L024 supply the conditional representation interface. No formal verification or absence claim is made.
