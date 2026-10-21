# L018 — The compact involution has no full-pair lift over identity Galois

## Hypotheses

Let K = Q_3(pi), pi^27 = 3, let kbar be an algebraic closure of K, and put G_K = Gal(kbar/K). Use the **full model MLF×-pair** G_K acting on O_kbar^times, in the sense of Hoshi's Definitions 5.1–5.3. A pair automorphism is (alpha_G, alpha_M), with the two isomorphisms compatible with the Galois action. Require alpha_G = id_G_K. No forgotten, invariant-only or torsion-quotiented structure replaces this pair.

Put O = O_K, J = log(O^times), and I = J/6. Use L016's continuous logarithm homomorphism and its Z_3-stable image J. Use L017's Q_3-linear compact involution g, including its proved preservation g(I) = I. In L017's notation, for y = sum_(r=0)^26 c_r pi^r,

\[
\phi(y)=3c_0-\frac{31}{3}c_1+9c_{15}-9c_{18},\qquad
A(y)=\frac{27}{8}c_0,\qquad B(y)=-\frac{3}{496}\phi(y),
\]
\[
q=q_1\in J,\quad v_3(q)=-2,\quad w=9\pi q,\quad z=q/6,
\qquad g(y)=y+(A(y)-B(y))(w-z).
\]

The exact values imported from L017 are A(z)=1, B(z)=0, A(w)=0, B(w)=1. The lettered functionals here refer only to that local involution, not the original IUT volume comparison.

Import **Yuichiro Hoshi, Introduction to Mono-anabelian Geometry, Publications mathématiques de Besançon (2021), pp. 5–44, DOI 10.5802/pmb.42, Theorem 7.6(i–ii), pp. 39–40, and Corollary 7.7, p. 43**, together with Definition 5.5 and Remark 5.5.1, p. 30 ([published primary text](https://www.numdam.org/item/10.5802/pmb.42.pdf#page=36)). For MLF×-pairs, the kernel of Aut(G acting on M) → Aut(G) consists exactly of the exponent maps x → x^lambda for lambda in Zhat^times. This is the cited theorem, not a newly proved classification. The supplied SPECIALIZE assessment covers only its following fixed-Galois logarithm specialization and exact-map test.

## Conclusion

There is **no** automorphism (id_G_K, alpha_M) of this full model MLF×-pair whose induced action on J, under the fixed logarithm identification, equals g restricted to J.

Every such pair automorphism acts on J by y → lambda_3 y for some lambda_3 in Z_3^times, and hence preserves v_3 on every nonzero logarithm. In contrast,

\[
g(q)=54\pi q,\qquad v_3(g(q))=28/27\ne -2=v_3(q).
\]

This rules out only the identity-G_K full-pair realization of this particular auxiliary witness. It does not classify nonidentity G_K actions or quotient-only maps, identify the original ind2 group, invalidate L017's auxiliary orbit computation, or demonstrate an essential IUT flaw.

## Proof

**Restriction to the actual units.** The G_K-invariants of O_kbar^times are O_K^times: an invariant algebraic element lies in the fixed field K, and the unit condition is its valuation-zero condition. Conversely every unit of K is fixed. Equivariance over identity G_K and the equivariance of the inverse therefore make alpha_M restrict to a bijection of O_K^times.

By the imported kernel theorem, alpha_M(x)=x^lambda for one lambda in Zhat^times. Write lambda_3 for its component in Z_3^times. To justify its logarithmic action, choose integers m_n representing lambda modulo n!. Then m_n converges to lambda in Zhat, and to lambda_3 in Z_3. For a fixed x in O_K^times, the groups O_K^times/(1+pi^r O), r >= 1, are finite. For each r their orders divide n! once n is sufficiently large. Thus x^(m_n) converges to x^lambda in O_K^times: modulo each such quotient the powers eventually agree with the profinite exponent action. These subgroups form a neighborhood basis at 1, so the convergence holds in the unit topology.

L016's logarithm is a continuous homomorphism on all these units, including the residue-unit sign. Consequently

\[
\log(x^\lambda)
=\lim_n\log(x^{m_n})
=\lim_n m_n\log(x)
=\lambda_3\log(x).
\]

If two units have the same logarithm, this formula gives the same output; hence it defines an induced action on J without any injectivity assumption on log. Z_3-stability of J and the inverse scalar lambda_3^(-1) show it is a bijection of J. Since lambda_3 is a unit, v_3(lambda_3 y)=v_3(y) for every nonzero y in J. This is only a specialization of the exponent action; no general analytic theorem is being reproved.

**The exact-map obstruction.** Since J=6I and g is Q_3-linear with g(I)=I, g also preserves J. From A(z)-B(z)=1, its defining formula gives g(z)=w. Therefore, since q=6z,

\[
g(q)=6g(z)=6w=54\pi q.
\]

The input q is a genuine logarithm by L016, not just a finite-series approximation, and it is nonzero by v_3(q)=-2 from L017. As v_3(54)=3 and v_3(pi)=1/27, the displayed image has valuation 3+1/27-2=28/27. It cannot equal lambda_3 q for any lambda_3 in Z_3^times. Thus it cannot be the logarithmic action of a full-pair automorphism over identity G_K. This single exact input suffices; no matrix sampling, orbit recomputation or new logarithm certificate is required.

**Relevance and scope.** The target was a necessary lift condition on L017's already constructed witness. Its failure abandons that restricted lift route. The needed original tensor/initial-data realization, ind3 input, marked pilot transport, essentiality and normalized finite B >= A remain unresolved. In particular, importing this kernel theorem does not equate its fixed-Galois subgroup with all original ind2 transformations. Nonidentity G_K components require separate source coverage before mathematical investigation.

## Mathlib

Full matching Hoshi MLF×-pair kernel theorem and this particular degree-27 nonliftability statement: **not checked**. Supporting continuous-homomorphism, profinite exponentiation, p-adic logarithm and valuation coverage: **not checked**. The published Hoshi theorem is the classification input; the field-specific exact data come from L016 and L017. Unknown Mathlib availability is not evidence of absence. This application is classified as **REPRODUCTION**, with no claim of mathematical novelty beyond the sources checked.
