# L059 — Fixed CM characteristic-order upper bound

## Hypotheses

Use E/Q: y^2=x^3+1 and p=7. Retain the fixed arithmetic,
optimal-quotient, differential-scale, total-period and orientation
hypotheses verified in L057, including its inherited L028/L050/L052/L056
qualifications. Let Q_infinity be the cyclotomic Z_7-extension of Q,
Gamma its Galois group, and Lambda=Z_7[[Gamma]]=Z_7[[T]], where
T=gamma-1 and kappa(gamma)=8.

Let X be the Pontryagin dual of the classical Sel_{7^infinity}(E/Q_infinity)
as defined in foundations/03 and used in L002, and let f_X be any generator
of its characteristic ideal. Use exactly L057's primitive ordinary
trivial-Teichmuller-branch series L_7(E,T), with unit root alpha of
X^2+4X+7, symbols S(r)=F({infinity,r}), and total minimal real period
Omega(E). No Euler factor or primitive interpolation multiplier is removed.

## Conclusion

The following known one-sided order comparison applies to this CM curve:

\[
\boxed{\operatorname{ord}_{T=0}f_X(T)
       \leq\operatorname{ord}_{T=0}L_7(E,T).}
\]

Order of the zero analytic series is understood as infinity. This is
neither equality of characteristic ideals nor a comparison with complex
analytic order. It assumes no rational lower bound, finite Sha,
height nondegeneracy or lower-coefficient vanishing. No consequence of
L058's particular coefficient is asserted in this lemma.

## Proof

**Precise known input.** Import Balakrishnan--Muller--Stein,
*A p-adic analogue of the conjecture of Birch and Swinnerton-Dyer for
modular abelian varieties*, Math. Comp. 85 (2016), 983--1016,
DOI 10.1090/mcom/3029,
[Theorem 1.6 and equation (1.3), printed p.986](https://wstein.org/papers/mcom3029.pdf#page=4).
Within its standing good-ordinary scope, Theorem 1.6 states for an
elliptic curve A that f_A divides p^m L_p(A,T) for some integer m>=0;
equation (1.3) explicitly gives ord_T f_A<=ord_T L_p(A,T).
The preceding paragraph identifies f_A with the characteristic series
of the cyclotomic classical p-primary Selmer dual over Z_p[[Gamma]].
The statement has no CM exclusion or residual-surjectivity hypothesis.
This uses the published Kato theorem translation, not a fresh proof
or inspection of Kato's original argument.

**Applicability of the algebraic side.** Under the classical local
conditions and infinite-layer convention in foundations/03, the source's
X(E/infinity Q) is the X in these hypotheses. It is not a fine, strict,
relaxed or signed Selmer dual. L002 supplies finite generation and
torsion in this good-ordinary application, so its characteristic series
exists. Both conventions identify the completed group algebra with
Z_7[[T]] using gamma. A characteristic generator is determined up to a
Lambda unit; such a unit has nonzero constant term, hence does not change
order at T=0.

**Applicability of the analytic side.** L057's audited source matching
uses this same paper's Sections 2.1--2.3, pp.987--993. Its level-36
rational-coefficient newform, degree-one optimal model, and differential
scale one satisfy the construction's running c_A=1 hypothesis. Its
minimal discriminant -432 is prime to seven, and #E(F_7)=12 gives
a_7=-4, prime to seven. Thus the prime is good ordinary and the source
unit root is exactly alpha. CM of E does not change the coefficient
field Q of the newform.

L057 identifies the source's plus symbol with S(r), with the
infinity-to-r orientation and total period Omega(E). Its finite measure
uses precisely alpha^(-k) S(r/7^k)-alpha^(-(k+1)) S(r/7^(k-1)), summed
on the trivial branch in the coordinate kappa(gamma)=8. Its limiting
series is therefore the L_7(E,T) in the hypotheses. In particular the
factor (1-alpha^(-1))^2 remains in the primitive interpolation law;
there is no exceptional-zero division, period adjustment, generator
inversion or additional bad-prime Euler-factor deletion.

Apply the imported order inequality with A=E and p=7 to obtain the
displayed conclusion. The source's p^m qualification is retained:
7^m is a nonzero constant, with T-order zero, so it cannot affect this
order comparison. No integral equality or assertion m=0 follows.
Using the explicit published inequality avoids claiming an unspecified
stronger integral divisibility convention. A reproof of the Euler-system
theorem or CM-field character descent is unnecessary for this import.

**Limitations and review status.** This establishes a fixed known input
locally, not progress beyond the cited theorem. L004's non-CM hypothesis
is not weakened; L003's height converse is not invoked. Rational
directions, divisible Sha, augmentation semisimplicity, complex-order
comparison and uniform production remain separate gaps. The fixed
applicability assembly passes the separate critical audit below.

**Separate critical audit, 2026-10-14, BSD-205.** The audit used the
pre-existing IMPORT assessment
`drafts/literature/2026-10-14-fixed-cm-order-critical-audit.md`.
Its verdict concerns this precise theorem application, not a reproof of
Kato or a fresh replay of upstream numerical certificates.

The previously terse algebraic identification can be made explicit.
For each finite cyclotomic layer K=Q_n, put A=E[7^infinity]. The local
condition at every place v is the image of the Kummer map

\[
 E(K_v)\otimes\mathbf Q_7/\mathbf Z_7
 \longrightarrow H^1(K_v,A).
\]

The classical group is the kernel of the global localization map to
the product of the quotients by these images. Take its direct limit
under restriction as n increases, then its continuous dual. This is
exactly foundations/03's convention. The explicit standard definition
is in Greenberg, *Iwasawa Theory for Elliptic Curves*, arXiv:math/9809206v1,
[Section 2, printed pp.12--13](https://arxiv.org/pdf/math/9809206#page=13);
its classical dual and finite-generation/cotorsion statements occur in
[Section 1, printed pp.4--5, Theorems 1.2 and 1.5](https://arxiv.org/pdf/math/9809206#page=4).
This spells out the classical p-Selmer terminology used by BMS p.986;
BMS itself gives only the brief name, not this displayed local formula.
In particular the conditions at the bad primes 2 and 3 are retained,
and the condition at seven is its Kummer image. No replacement by a
zero, unrestricted, signed, or imprimitive condition is involved. No
comparison theorem between two different Selmer structures is assumed.

There is also no hidden change of cyclotomic field. Under kappa the full
cyclotomic group is mu_6 times (1+7 Z_7); its sixth-power subgroup is
1+7 Z_7, since raising to six is an automorphism on this pro-seven group.
Restriction identifies that subgroup with Gal(Q_infinity/Q), the
quotient by mu_6. Thus BMS's Gamma and the local Gamma agree. Both use
the usual contragredient action on the dual,
(g phi)(s)=phi(g^(-1)s), and T=gamma-1. Since v_7(log(8))=1, the chosen
element with kappa(gamma)=8 is a topological generator. No inverse
coordinate or Tate twist is inserted.

On the analytic side, the audit compared the complete L057 normalization
and its prior audit with the reopened BMS period, plus-symbol, measure,
coordinate and interpolation passages, pp.988--993. The verified
degree-one model and differential scale give the source's period choice;
the rational newform coefficient field is unchanged by CM. L057's
infinity-to-r identity fixes the sign of the source plus symbol.
Its exact residues index all six Teichmuller classes and the generator
8, with no averaging. The two powers of alpha, the two argument
denominators and every weight (1+T)^j agree term by term. The source's
coefficientwise limit is consequently the same series, not merely a
series sharing one interpolation value. The primitive multiplier stays
present. Arithmetic and normalization qualifications inherited from
L028/L050/L052/L056 are reused through audited L057.

Finally the source's good-ordinary scope and Theorem 1.6/(1.3) were
checked against this E and p. The nonzero discriminant modulo seven and
t=-4 satisfy that scope. The theorem makes no CM exclusion. Its
power-of-seven allowance has order zero in T; seven is not asserted to
be a unit of Lambda. The same is true of the T-order effect of changing
a characteristic generator by a Lambda unit. These checks validate only
the displayed inequality. L058 is not an input, and no coefficient
corollary, lower vanishing, height converse, or complex-order comparison
has been inferred. Direct lemma inputs remain L002 and L057.

## Mathlib

Full matching CM-inclusive characteristic-order theorem and its Selmer
and primitive-measure identifications: **not checked**. No absence or
matching-theorem claim is made. The mathematical authority here is the
precisely cited published theorem with the fixed applicability above.
