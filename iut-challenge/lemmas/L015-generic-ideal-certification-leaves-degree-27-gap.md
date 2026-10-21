# L015 — Generic valuation-ideal certification leaves a degree-27 gap

## Hypotheses

Let K/Q_3 be finite and totally ramified of degree e, with uniformizer pi, valuation v(3) = 1, O = O_K, J = log(O^times), I = J/6, and G the Q_3-linear extensions of Aut_(Z_3)(I). Write GY for the union of all g(Y). Let a != 0 satisfy v(a) > 0, and write a = 3^n b with n = floor(v(a)), s = v(b) = k/e, 0 <= k < e. When k = 0, n >= 1. No invariance of J under O^times is assumed.

Use the single-field bounds in April 2020 IUT IV **Proposition 1.2(i)**, printed pp. 10–11 ([author-hosted locator](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf#page=10), [inspected reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf#page=10)), the standard p-adic log/exp correspondence above v = 1/2, and **Dupuy–Hilado Lemma 4.2.3(1)**, [arXiv:2004.13108v2, printed p. 17](https://arxiv.org/pdf/2004.13108v2#page=17). Version/access qualifications and the exact approved test are in the [prior SPECIALIZE assessment](../drafts/literature/2026-10-04-general-one-factor-coarse-enclosure.md).

## Conclusion

Put h = floor(e/2) + 1, alpha = h/e. Suppose a cited outer bound gives v(y) >= w for all y in J, and put m = min(0,w). The valuation-ideal sandwich certifies

\[
G(a(O\cup J))\subseteq 3^n 3^{-q}I,
\qquad q=\lceil\alpha-1-s-m\rceil,
\]

with enclosing radius

\[
R_{\rm cert}=3^{q+1-w}3^{-n}.
\]

Its comparison with the actual required coarse radius is the sufficient inequality

\[
3^{q-w}\le e,
\qquad R_{\rm req}=3e\,3^{-n}.
\]

For the native outer bound, set t = floor(log_3(3e/2)), w = 1/e - t. If e >= 2, the resulting q equals t for k < floor(e/2), and t-1 otherwise. For e = 1 it equals 0, giving R_cert = 3^(-n) <= R_req.

For **every totally ramified degree-27 field**, the sharper cited analytic bound and discrete valuations give w = -2. The best q certified by this sandwich is then 2 for 0 <= k <= 13 and 1 for 14 <= k <= 26. Consequently:

| Residual scalar valuation | Certified upper radius | Required radius | Outcome of this certification |
| --- | --- | --- | --- |
| 0 <= s < 14/27 | 243 times 3^(-n) | 81 times 3^(-n) | Insufficient by a factor of 3 |
| 14/27 <= s < 1 | 81 times 3^(-n) | 81 times 3^(-n) | Containment proved |

In particular, K = Q_3(pi), pi^27 = 3, a = pi is a concrete undecided regime. The polynomial is Eisenstein, so it supplies the stated field and s = 1/27. **No violating point or actual orbit radius is asserted.** This is an informative limitation of a sufficient mechanism, not a refutation of the coarse theorem or an essential IUT flaw.

## Proof

### Imported inputs and applicability

The standard log/exp correspondence identifies log(1 + pi^h O) with pi^h O because h/e > 1/2. Hence H = pi^h O is contained in J. The strict inequality is retained, including for even e; the larger ideal at valuation exactly 1/2 is not imported.

Proposition 1.2(i) gives J contained in pi^(1-et) O. Its ambient notation inherits the at-least-two-field hypothesis of Proposition 1.1. Apply it to a family with K and an auxiliary Q_3 field and use only the individual-field assertion concerning K. No tensor-automorphism theorem is specialized to a singleton. The native inner ideal at p = 3 has valuation 1; H improves this using the independently cited log/exp theorem.

The log/exp input also puts 3O in J, so I contains O. Together with the imported boundedness of J this ensures I is a full Z_3-lattice. The logarithm image is a Z_3-module; compactness of O^times and continuity of log make it closed. Nothing here equips J with an O-module structure.

### General sufficient inequalities

For x in O union J, v(x) >= m. Therefore

\[
v(6\cdot 3^q b x)\ge 1+q+s+m\ge\alpha.
\]

This proves the genuine inclusion 6 times 3^q b(O union J) contained in H contained in J, equivalently b(O union J) contained in 3^(-q)I. Only the ideal H is multiplied by arbitrary O-scalars. Since every g preserves I and commutes with rational powers of 3, taking the whole orbit gives the claimed lattice inclusion. The outer bound on J implies v(I) >= w-1 and hence radius at most 3^(1-w). Rational scaling yields R_cert. Division by the required radius gives R_cert/R_req = 3^(q-w)/e.

The q above is the least integer for which this valuation lower bound places both branches in H. A smaller q is not certified by this argument; this does not say that the actual inclusion fails for that q.

For e >= 2, t >= 1 and w < 0, so m = w. Integer arithmetic gives

\[
q=t-1+\left\lceil\frac{\lfloor e/2\rfloor-k}{e}\right\rceil.
\]

The last ceiling is 1 precisely when k < floor(e/2), and 0 otherwise. For e = 1, w = 1, m = 0, alpha = 1 and s = 0, giving q = 0 as stated.

### Degree 27 and the sharper outer bound

Dupuy–Hilado Lemma 4.2.3(1) gives |y|_3 <= e/(exp(1) ln 3) for every y in J. For e = 27 the discrete value group improves this to |y|_3 <= 9, or v(y) >= -2. Here is an explicit check of the rounding, so no numerical approximation is load-bearing.

Let C = exp(1) ln 3. The positive exponential series and

\[
\ln 3=2\sum_{j\ge0}\frac{(1/2)^{2j+1}}{2j+1}
\]

give exp(1) > 27/10 and ln 3 > 109/100. Their elementary geometric tail bounds also give exp(1) < 2719/1000 and ln 3 < 1099/1000. Thus 29/10 < C < 3. The exact integer inequality 29^27 > 3^26 times 10^27 gives C > 3^(26/27). It follows that

\[
9 < 27/C < 3^{55/27}.
\]

The latter number is the next possible absolute value strictly larger than 9 in a degree-27 totally ramified field. Therefore the cited closed disc contains only elements of absolute value at most 9, proving w = -2 as a valid outer bound. This is a bound, not a claim that J attains its boundary. The rational series bounds and integer comparison are checked in the certificate below.

Now alpha = 14/27, m = -2, and

\[
q=\left\lceil\frac{41-k}{27}\right\rceil
=\begin{cases}2,&0\le k\le13,\\1,&14\le k\le26.\end{cases}
\]

Since 3^(1-w) = 27, the certified radii are 243 and 81, respectively, versus the required 3e = 81, all multiplied by 3^(-n). To achieve radius <= 81 with this outer bound requires q <= 1. For k <= 13, q = 1 gives lower valuation s < 14/27 for the logarithm branch, below H's threshold. This is the precise failure of certification. For k >= 14 the genuine inclusion already proved does certify the whole group orbit.

For comparison the native bound at e = 27 has t = 3 and w = -80/27. It yields q = 3 for k <= 12 and q = 2 otherwise, giving much larger upper radii 3^(188/27) and 3^(161/27), respectively. The strengthened analytic bound is therefore essential even to certify the successful scalar range. Neither of these loose radii is a lower bound on the actual orbit.

### Scope, source comparison and verification

The source coarse radius is the separate post-chain prescription in [§6.2, printed p. 20](https://arxiv.org/pdf/2004.13108v2#page=20); with one factor the two different norms cancel and |6|_3 = 1/3. The logarithm estimates are imported, rather than reproved. The specialization consists only of the scalar normalization, invariant-lattice inclusion and exact threshold comparison. It is classified **REPRODUCTION**, with no result beyond the checked literature claimed.

Run `python3 scripts/coarse-ideal/check_degree_27_bounds.py`. The certificate `scripts/coarse-ideal/degree-27-bounds.json` checks the rational constant bounds and all 27 residual classes, recording certified/required radii and the failed certification range. It does not compute an exact logarithm lattice or search for an automorphism witness.

The generic sandwich does not settle the small-residual-valuation range. A stronger inclusion into the actual J, or a more precise saturation analysis, would be needed. Original initial theta data, distinguished pilot transport, the full permitted image family, essentiality and normalized finite B >= A remain unestablished.

## Mathlib

Full general certification statement and degree-27 specialization: **not checked**. Supporting local-field valuations, p-adic log/exp, lattices and series results: **not checked**. The named primary results above support the logarithm estimates; they are not citations for a matching saturated-union theorem or a matching Mathlib statement. No absence from Mathlib is inferred.
