# L022 — A trace-preserving shear violates the shell-envelope bound

## Hypotheses

Let K=Q_3(pi), pi^27=3, v(3)=1, O=O_K, J=log(O^times), and I=J/6. Use the complete logarithm lattice of L016, including its exact genuine logarithms q_1 and q_2 and the integral functional

\[
\phi\left(\sum_{r=0}^{26}c_r\pi^r\right)
=3c_0-\frac{31}{3}c_1+9c_{15}-9c_{18},
\quad \phi(J)\subseteq\mathbb Z_3.
\]

Use L017's functional B=-3phi/496, integral on I, and its identities phi(q_1)=0 and phi(18pi q_1)=-992/3. L016 also gives phi(q_2)=0. Retain every analytic and all-unit-coverage qualification of L016; in particular neither q_j is a finite-precision substitute for an actual logarithm.

The packet is exactly L020's (K,Q_3) tensor packet, identified with K by multiplication. Its shell is I, its first-power shell envelope is pi I, its literal input is pi O union 3pi J, and its coarse prescribed radius is 81. The strict scalar a=pi, beta=1, factor exchange placing a in the last factor, and both conductor conditions are as justified in L020. The source is **Dupuy–Hilado, arXiv:2004.13108v2 (2020-04-29), Definition 4.3.1 and §6.2, printed pp. 18–20**, especially the separate coarse formula after (6.8): [versioned primary PDF](https://arxiv.org/pdf/2004.13108v2). This is an assumed auxiliary envelope, not an asserted actual-ind3 image.

Impose L019's necessary trace restriction on the test maps: a Q_3-linear automorphism T of K must satisfy T(I)=I and Tr(Ty)=lambda Tr(y) for all y in K, with one lambda in Z_3^times. The unchanged prior SPECIALIZE assessment is `drafts/literature/2026-10-06-trace-compatible-shell-envelope.md`. Its supporting primary trace theorem is **Hoshi–Nishio, On the Outer Automorphism Groups of the Absolute Galois Groups of Mixed-characteristic Local Fields, June 2022 revised text, Lemmas 2.2–2.3, PDF pp. 6–8** ([author-hosted source](https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1931revised.pdf)); L019 retains the additional full-pair unit-exponent qualification. Neither this theorem nor L019 supplies a converse realizing all maps that pass the trace test.

## Conclusion

Trace compatibility does **not** force T(pi I) into the radius-81 disc. Define

\[
z=\frac{q_2-(3/16)q_1}{6},\qquad
T(y)=y+B(y)z,\qquad x=\frac{\pi q_1}{6}.
\]

Then z is in I, T(I)=I, and T preserves trace on all K (lambda=1). Its inverse is T^(-1)(y)=y-B(y)z. The point x is in pi I and

\[
T(x)=\frac{\pi q_1}{6}+\frac{q_2-(3/16)q_1}{324},
\qquad v(Tx)=-\frac{16}{3}<-4.
\]

Thus the attained witness radius is 3^(16/3)>81. This is a lower bound supplied by one point, **not** a claim about the sharp radius of this map or the whole trace-compatible subgroup. No full-pair lift, native permitted action, actual-ind3 membership or essential IUT flaw is established.

## Proof

### An integral trace-zero direction and a square-zero shear

The scalar 3/16 is in Z_3, so L016's q_1,q_2 in J imply z in I. Its table gives constant coefficients 16/9 and 1/3. L019's power-basis trace computation gives Tr(y)=27c_0(y) for all y in K. Therefore

\[
c_0(z)=\frac{1}{6}\left(\frac13-\frac3{16}\frac{16}{9}\right)=0,
\qquad \operatorname{Tr}(z)=0.
\]

Both phi(q_1) and phi(q_2) are zero, whence B(z)=0. For any j in J,

\[
B(j/6)=-\phi(j)/992\in\mathbb Z_3
\]

because 992 is prime to 3. This proves integrality on the **complete** I, using the established complete J rather than sampling units.

Put N(y)=B(y)z. The identity B(z)=0 gives N^2(y)=B(y)B(z)z=0 on all K. Hence (id+N)(id-N)=(id-N)(id+N)=id. Since z in I and B(I) subset Z_3, both id+N and id-N map I into I. Their inverse relation proves T(I)=I and Q_3-linear invertibility. This explicitly verifies the field-specific shear; no general stabilizer-orbit theorem or kernel-basis classification is assumed or reproved.

For every y in K, Q_3-linearity of trace gives

\[
\operatorname{Tr}(T(y))=\operatorname{Tr}(y)+B(y)\operatorname{Tr}(z)
=\operatorname{Tr}(y).
\]

Thus a single allowed unit lambda=1 works on all K, not merely on the witness. Under L020's tensor identification this also defines a shell-preserving tensor map T tensor id. Tensor transport does not establish native admissibility.

### Exact membership and strict valuation comparison

Because q_1 is in J, q_1/6 is in I and x=pi(q_1/6) is in precisely the tested envelope. Rational linearity and the established value of phi give

\[
\phi(\pi q_1)=-496/27,\qquad
B(\pi q_1)=1/9,\qquad B(x)=1/54.
\]

Consequently T(x)=x+z/54, giving the displayed exact image.

Here are the full valuation obligations without reliance on numerical precision. L016 gives v(q_1)=-2. For q_2 the table's constant term has valuation -1; its degree-18 term pi^18/9 has valuation -2+18/27=-4/3. The degree-2,3,4,8,10 terms have nonnegative valuations. The remaining degrees 6,9,12,24 have valuations respectively -7/9,-2/3,-5/9,-1/9. Hence the unique minimum is -4/3 and v(q_2)=-4/3. In particular

\[
v((3/16)q_1)=-1>-4/3=v(q_2),
\]

so the ultrametric equality for summands of different valuations gives

\[
v(z)=-4/3-v(6)=-7/3.
\]

The constant coefficients cancel to make z trace-zero, but they are not its lowest-valuation terms. Explicitly its degree-18 coefficient is 13/864, also giving -3+18/27=-7/3. Thus there is no hidden cancellation of the claimed field minimum.

Now v(54)=3, so v(z/54)=-16/3. On the other hand

\[
v(x)=1/27-2-1=-80/27>-144/27=-16/3.
\]

These unequal valuations imply v(Tx)=-16/3. The radius-81 disc is exactly {y:v(y)>=-4}; the strict violation follows. Equivalently the cube of the witness radius is 3^16=43046721, while 81^3=3^12=531441. There is no real-number approximation in this comparison. The q_j already belong to the exact logarithm image by L016, so no new infinite-logarithm witness or additional tail assertion is needed.

### Reproduction and interpretation limits

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/coarse-ideal/check_trace_compatible_shear.py`. The full certificate is `scripts/coarse-ideal/trace-compatible-shear.json`. It parses all thirteen canonical representatives and the twenty-seven generators of H=pi^14 O from L016's description, checks B on all forty I-generators, records their forward and inverse images, verifies both inverse compositions and trace equality on all twenty-seven power-basis vectors, and computes the exact witness and every nonzero direction-term valuation. All twelve finite checks pass with zero failures. The proof above supplies completeness of the lattice argument through L016 and the explicit integral-combination/inverse construction; the certificate does not infer a subgroup statement from a matrix sample.

This new map is not L017's trace-violating involution. L019's exclusion of that involution remains intact. Passing its necessary trace test does not supply a full-pair realization of T. L020's whole-literal-union enclosure also remains intact: this calculation tests the larger envelope only. No sharp whole-subgroup radius or higher-power assertion follows.

The local result stops trace compatibility alone as a sufficient repair of this envelope bound. Its plausible downstream use is to require a stronger native-action or actual-region condition before using such an envelope estimate. Actual ind3 membership/equality, full-pair/native admissibility, original initial data, inter-summand permutations, pilot transport, essentiality and normalized finite B>=A remain unresolved. The original IUT challenge is still IN_PROGRESS with no candidate essential flaw.

The construction's classification **POTENTIALLY_NEW** means only that the prior bounded assessment found no inspected theorem deciding this precise subgroup-envelope target. The logarithm data, source definitions and necessary trace restriction are imported; originality beyond the sources checked is not certified. The separate audit below has classification **REPRODUCTION**.

### Critical audit, 2026-10-06

**Complete logarithm input.** Reviewed L016's filtration, strict log/exp range and infinite tail, rather than relying on the finite table alone. The thirteen successive quotients U_j/U_(j+1), for 1<=j<=13, and the residue sign cover every unit modulo U_14. Since 14/27>1/2, log(U_14)=H. Closedness of the continuous image of the compact unit group justifies Z_3 multiples. For k>=243 the uniform block bound 3^h-27h>=108, increasing to infinity for h>=5, puts every omitted logarithm tail in H. The exact rational table congruences therefore imply both q_1,q_2 in J and the complete forty-generator description. Read and reran `scripts/coarse-ideal/audit_degree_27.py`, which independently recomputes all 351 table congruences without importing the shear checker or a stored lattice diagonalization. There were no failed checks. Inspected the complete selected q_2 discrepancy vector in `scripts/coarse-ideal/degree-27-audit.json`; all congruences, including the required coordinate-dependent H depths, are verified by the inspected exact-fraction loop. No new analytic theorem or precision-based logarithm identification is used.

**Complete shell and inverse.** Read and reran `scripts/coarse-ideal/check_trace_compatible_shear.py` and inspected the complete forty-entry B-value vector, direction vector, direction valuations and witness image in its certificate. On the thirteen q_j/6 generators only q_3/6 and q_9/6 have nonzero B-values, respectively -1/248 and -3/992. On the H/6 generators only coordinates 0,1,15,18 have nonzero values, respectively -9/992, 1/32, -9/992, 9/992. All are integral at 3; these are complete generators, not sampled units. The direction is the integral combination q_2/6-(3/16)q_1/6. Its coordinates 0,1,15,18 are 0,-1/32,-1/48,13/864, giving phi(z)=31/96-18/96-13/96=0. Thus N^2=0 on all K and both id+N and id-N preserve I. Both inverse compositions and trace equality also pass on all twenty-seven power-basis vectors. These symbolic identities prove surjectivity and the all-K assertion independently of the certificate's image-construction checks, some of which simply repeat their defining formulas.

**Trace and strict witness.** L019's geometric-sum computation gives Tr(y)=27c_0(y) without requiring K to be Galois. The direction has c_0=0, so the same unit lambda=1 works for every y. A necessary full-pair relation on J extends to a proposed Q_3-linear action on K because H subset J spans K; no converse is imported. The exact functional evaluation gives B(x)=1/54. The degree-18 coefficient of z is 13/864 and attains -7/3; every other nonzero direction term has larger valuation, as checked in the complete valuation vector. Its contribution to T(x) has coefficient 13/46656 and valuation -16/3. Independently v(x)=-80/27>-16/3, so cancellation is impossible. This verifies the attained radius 3^(16/3), with cubed value 43046721 against the required 531441. It does not establish a sharp radius for T or the subgroup.

**Source specialization and limits.** Reused the approved primary coverage and checked L020's multiplication identification, log(Z_3^times)=3Z_3, tensor shell I, strict last-factor scalar after exchange, and both beta=1 conditions. The different valuations 107/27 and 0 cancel in the coarse exponent; its single denominator |6|_3=1/3 gives radius 81. Thus the input remains the assumed pi I envelope, distinct from pi O union 3pi J and from actual ind3 images. L015's individual-field bound retains its two-field-family qualification. L019's exclusion of the old involution and L020's literal-union enclosure remain valid. Passing trace does not certify a full-pair/native lift, higher powers, original data, pilot transport, essentiality or finite B>=A.

The audit found no load-bearing mathematical error and required no changed argument, new lemma or mathematical script. Its result is **EXPLORATION / REPRODUCTION**: independent checking of the existing auxiliary diagnostic, with no new bound or advance beyond the inspected sources. All twelve shear checks and the supporting logarithm congruences pass; the analytic and source qualifications above remain essential. This is not a candidate resolution of the original challenge.

## Mathlib

Full matching trace-compatible envelope obstruction and exact degree-27 logarithm lattice: **not checked**. Supporting finite-rank shear, nilpotent inverse, trace, local-field valuation and unit-logarithm coverage: **not checked**. Unknown availability is not evidence of absence; no formal verification is claimed.
