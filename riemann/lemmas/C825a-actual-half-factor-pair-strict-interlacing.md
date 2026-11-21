# Corollary 825a: the actual centered half-factor pair strictly interlaces

## Hypotheses

Use L825's actual moment normalization, original centered monic coordinates,
and its audited coefficient inputs through gamma(3). In particular retain
the inherited L778/L791 complex analytic error and trusted evaluator/software
contracts. These are computer-assisted informal inputs; this corollary does
not independently attest or formally verify the transcendental backend.
Write

\[
 a=u_2/2,\quad b=u_3/2,\quad c=v_3/2,\qquad
 Q_2(y)=y^2+a,\quad Q_3(y)=y^3+by+c.
\]

No cubic hyperbolicity premise, common differential symbol, common measure,
degree-dependent dilation, or RH assumption is used. Only this pair is tested.

## Conclusion

Put t=sqrt(-a)>0. The roots of Q_2 are simple and satisfy

\[
 8.680209<t<8.680210.
\]

The residues rho_- and rho_+ of Q_3/Q_2 at -t and +t respectively obey

\[
 -67.520092<\rho_-<-67.520090,\qquad
 -73.589472<\rho_+<-73.589470.                     \tag{1}
\]

Consequently Q_2 and Q_3 are coprime, and Q_3 has three simple real roots
s_1<s_2<s_3 satisfying

\[
 s_1<-t<s_2<t<s_3.
\]

This is a finite known-method specialization, not a result beyond the
standard criterion in generality or a claim of certified novelty. It passes
and retires this two-pole diagnostic. It proves no uniform adjacent-factor
interlacing, all-degree factor realization, shifted/mixed compensation,
global positivity, or RH statement. No degree sweep follows from (1).

## Proof

**Imported criterion.** Steve Fisk, *Polynomials, roots, and interlacing*,
[arXiv:math/0612833v2](https://arxiv.org/pdf/math/0612833v2), Section1.3,
printed pp12-14, basis setup and Lemma1.20(3), gives the strict-interlacing
criterion for real f of degree n with distinct real roots r_i, real g of
degree n+1, both with positive leading coefficient. In

\[
 g/f=dy+e+\sum_i \rho_i/(y-r_i),
\]

d>0, and strict interlacing with the two outside roots of g holds if and
only if all residues rho_i=g(r_i)/f'(r_i) are negative. We import this
criterion, rather than reprove it. Fisk's displayed Lemma1.8 endpoint
printing errors are not used as hypotheses or conclusions.

Independent coverage is Olga Holtz and Mikhail Tyaglov, *Structured matrices,
continued fractions, and root localization of polynomials*,
[arXiv:0912.4703v3](https://arxiv.org/pdf/0912.4703v3), Definition3.1,
Remark3.2 and Theorem3.4, printed pp44-49, especially condition2,
(3.6)-(3.7), and condition6. Their negative-type convention has positive
residues and nonpositive linear coefficient: apply it to p=Q_2, q=-Q_3.
The degree difference is one, and the linear part is -y; the quotient is
not treated as a proper fraction. The simple real poles and coprimality
required there are verified below. These primary statements, essential
proof cases and source qualifications were already inspected in the
step768 comparison; its ready SPECIALIZE assessment is
`drafts/literature/2026-11-13-half-factor-two-residue-test-768.md`.

**Coefficient and root enclosures.** The new calculation first checks all
seven step631 saved input hashes, the relevant saved audit checks and empty
failures, the source hash retained in L791's data, and equality of the whole
inherited evaluator with step433's audited replay. For j=0,...,3 it reads
the complete saved coefficient endpoints, retains the additional symmetric
error E_G/1600^j, and verifies containment in actual_a[j]. Here
0<E_G<3.141*10^(-48) bounds the analytic difference uniformly on the closed
complex disk |w|<=1600. It then checks
gamma(j)=8*4^j*j!*a_j containment and strictly positive gamma denominators.
Thus it retains both coefficient widths and the analytic Cauchy error;
no derivative estimate comes from a real-axis approximation.

Exact Fraction interval arithmetic recomputes R_j=gamma(j)/gamma(0),
h_2=R_1/R_2, h_3=R_2/R_3 and all three L825 coefficients. Each complete
recomputed interval is contained in its original saved interval and in
the following rational hull used in the final calculation:

\[
 a\in[-75.346033,-75.346032],\quad
 b\in[-216.455595,-216.455594],\quad
 c\in[-52.683490,-52.683489].                       \tag{2}
\]

All displayed decimals in (2) are exact rational endpoints. Addition adds
endpoints, multiplication takes the extrema of four endpoint products,
squaring includes zero when needed, and division reverses reciprocal
endpoints after excluding zero. There is no new floating-point or
transcendental evaluation. Shared coefficient correlations are enlarged,
which preserves enclosure of their actual values.

In particular -a is positive and lies in [75.346032,75.346033]. The exact
squares

\[
 (8.680209)^2=75.346028283681<75.346032,
 \qquad (8.680210)^2=75.346045644100>75.346033
\]

prove the asserted t enclosure without a numerical square-root backend.
The two roots +/-t are distinct and Q_2'(+/-t)=+/-2t is nonzero.

**Residues and source application.** Exact polynomial division gives

\[
 Q_3/Q_2=y+\frac{(b-a)y+c}{y^2+a}.
\]

At either simple denominator root r, r^2=-a, so

\[
 \rho(r)=\frac{Q_3(r)}{Q_2'(r)}
        =\frac{(b-a)r+c}{2r}
        =\frac{b-a}{2}+\frac{c}{2r}.             \tag{3}
\]

The complete partial fractions retain the linear part:

\[
 Q_3/Q_2=y+\frac{\rho_-}{y+t}+\frac{\rho_+}{y-t},
 \quad \rho_-=(b-a)/2-c/(2t),\quad
 \rho_+=(b-a)/2+c/(2t).
\]

Indeed rho_-+rho_+=b-a and t(rho_+-rho_-)=c, so their combined
numerator is (b-a)y+c. The certificate also expands the division and
cleared partial-fraction identities as full multivariate rational
polynomials, with no sample-value substitution.

Applying the exact enclosure operations to (2), the t interval and (3)
gives the complete rational intervals

\[
 \rho_-\in\left[
 -\frac{117217715084823}{1736042000000},
 -\frac{1172176991378249}{17360418000000}\right],
\]
\[
 \rho_+\in\left[
 -\frac{1277543988738667}{17360418000000},
 -\frac{127754411148781}{1736042000000}\right].
\]

Exact cross-multiplication places these closed intervals strictly inside
the open intervals (1), whose required sign threshold is zero. The direct
first expression in (3) also produces strictly negative enclosures; this
is a consistency check, not an independent analytic audit.

Both residues are nonzero, so Q_3 cannot vanish at either root of Q_2;
as these are all roots of Q_2, the polynomials are coprime. Their
coefficients are real, both are monic, and their degree difference is one.
All hypotheses of the cited strict criterion now hold. Applying it gives
the three simple real Q_3 roots and their asserted relative order. In the
Holtz–Tyaglov convention -Q_3/Q_2 has linear part -y and residues
-rho_-, -rho_+>0, giving the same conclusion. No prior cubic root claim
was substituted for relative root positions. Exact cancellation and
zero-straddling cases do not occur in these bounds.

**Evidence and reproduction.** Run
`python3 scripts/central-jacobi/half_factor_residues_770.py`.
It writes `scripts/central-jacobi/half-factor-residues-770.json`: PASS,
54 checks, no failures. That certificate retains complete input endpoints,
analytic-error additions, source/program hashes, exact recomputed
coefficients, hulls, square comparisons, symbolic identities, both complete
residue enclosures, actual bounds, required threshold and reproduction
command. The original certificates and programs are preserved. This is
not a fresh audit of the inherited transcendental implementation. The
separate finite audit below validates this specialization under those
unchanged premises.

### Independent finite audit — step772, 13 November 2026

The pre-existing SPECIALIZE assessment
`drafts/literature/2026-11-13-half-factor-residue-audit-770.md` covers this
audit. No defect was found in the stated coefficient/residue bounds or
source application. This is reproduction and validation of a finite
known-method specialization, not a new general theorem or RH progress
beyond the sources checked. Full matching Mathlib coverage is unchecked.

`python3 scripts/central-jacobi/audit_residues_772.py` writes
`scripts/central-jacobi/half-factor-residue-audit-772.json`: PASS,
72 checks, no failures. The checker imports and executes none of the
step770/631 arithmetic or polynomial code. It inspects all saved relevant
checks and failures, the twelve step770 input hashes, seven step631
inherited hashes, L791's evaluator hash, and equality of the entire
inherited evaluation record with step433's replay. All remain unchanged.
For each j=0,...,3 it checks the complete coefficient endpoints, the
additional E_G/1600^j error, actual-a containment, gamma normalization
and positive denominators. These checks retain the inherited complex
analytic and trusted, unattested transcendental/software premises;
they do not independently verify the backend.

Separate exact rational endpoint operations reproduce every endpoint
of the three step770 coefficient intervals and both residue intervals,
not only their displayed decimal previews. A second coefficient
calculation uses the algebraically identical formulas, with g_j=gamma(j),

\[
 a=\frac{g_0g_2-g_1^2}{2g_2^2},\qquad
 b=\frac{3(g_1g_3-g_2^2)}{2g_3^2},\qquad
 c=\frac{-g_0g_3^2+3g_1g_2g_3-2g_2^3}{2g_3^3}.
\]

Both calculations fit the rational hulls (2). Addition/subtraction use
endpoint bounds, products take all four endpoint products, division
inverts a zero-excluding interval, and squares account for zero.
These operations enclose all correlated actual values even though they
enlarge their ranges. The second expressions need not lie in the
narrower first-expression interval; the certificate requires only the
same stated hull. No such containment is silently presumed.

The two exact square comparisons above survive independently. To check
the residues without the old interval helper, set B=(b-a)/2. Its interval
is [-141109563/2000000,-141109561/2000000]. Since c<0<t, the interval
for D=c/(2t) has endpoints c_lower/(2t_lower) and
c_upper/(2t_upper), namely
[-26341745/8680209,-52683489/17360420]. Then rho_-=B-D and rho_+=B+D
reproduce the complete fractions displayed above and satisfy (1)
strictly. Thus zero, cancellation and nonreal denominator roots are
excluded. The direct residue expressions also reproduce their complete
saved intervals and remain negative.

The symbolic check collects every term: division has y^3+ay+by-ay+c;
the cleared partial-fraction numerator has

\[
 (b-a)ty-(b-a)t^2-cy+ct
 +(b-a)ty+(b-a)t^2+cy+ct
 =2t((b-a)y+c).
\]

Together with t^2=-a this verifies the complete identity, including
the linear quotient part. The derivative 2r at each pole r is nonzero,
and Q_3(r)=2r rho(r) is nonzero. Hence the coprimality conclusion does
not assume the numerator's roots. Real coefficients, monicity and
degree difference one are inherited explicitly from L825. All Fisk
Lemma1.20(3) hypotheses hold. In Holtz–Tyaglov's convention, q=-Q_3,
p=Q_2 has linear part -y and positive residues -rho(r). The oriented
Wronskian p q'-p' q is negative away from the poles because

\[
 (q/p)'=-1+\rho_-/(y+t)^2+\rho_+/(y-t)^2<0;
\]

at a pole it equals (2r)^2 rho(r)<0 as well. Thus the orientation and
simple strict-interlacing cases of Theorem3.4 are consistent with the
stated root order. This checks applicability of the cited theorem;
it does not reprove its general equivalence.

The initial audit draft's certificate contained a sign typo only in its
Wronskian prose at the pole. That draft is preserved at
`scripts/central-jacobi/half-factor-residue-audit-772-draft-first-pass.json`;
the corrected expression is (2r)^2 rho(r), as above. All arithmetic
checks passed in both runs; no original step770 evidence was overwritten.
This pair's diagnostic/audit sequence is now closed. No higher degree,
uniform sign estimate or mixed/global transfer follows.

## Mathlib

Full matching coverage is unchecked. No absence assertion is made.
The cited rational-interlacing theorem is the standard mathematical input;
the inherited analytic evaluator and this finite certificate are not
formally verified in Mathlib.
