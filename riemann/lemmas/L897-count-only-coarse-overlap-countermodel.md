# Lemma 897: a count-only coarse-overlap countermodel

## Hypotheses

Set k=6002, J=k+1, m=9000000000000, K=12363153437138 and
H=3000175332800. All logarithms are natural. Define the exact real function

\[
 U(t)=\frac{t}{2\pi}\left(\log\frac{t}{2\pi}-1\right)
       +b\log t+d,\qquad b=0.34536,\quad d=8.08344.
\]

The model class consists of strictly increasing positive ordinates
\(\gamma_j\to\infty\), with \(\gamma_J>4\),
\(\sum_j\gamma_j^{-2}<\infty\), inclusive count
\(N(t)=\#\{j:\gamma_j\le t\}\le U(t)\) for every real t>=e,
and N(H)=K. Its normalized product is
\(F(z)=\prod_{j\ge1}(1-z/(4\gamma_j^2))\), required to converge
uniformly on compact sets and have exactly simple positive real zeros.

Use only the scalar definitions from L836:

\[
 T=\gamma_J,\quad R=2(\gamma_k^2+T^2),\quad
 q=\frac{2\gamma_k^2}{\gamma_k^2+T^2},\quad
 a=\frac{R}{4T^2},\quad s=\frac{1+q}{2},
\]
\[
 V(T)=\frac{\log(T/(2\pi))}{\pi T}
       +\frac{b(\log T+1/2)+d-J}{T^2},\qquad
 \mathcal B(s)=\log\frac{1+sa}{1-a}
        +\frac{(1+s)R}{4(1-a)}V(T).
\]

No actual-Xi coefficients, zero locations, arithmetic identities, lower
count bound, sharper count envelope, or PF conclusion is imposed. L836's
actual-function conclusions are not imported as theorems for this class.

## Conclusion

There is a sequence in this class for which the **unrounded** expression

\[
 \mathcal H_m=\mathcal B(s)+2\log k+(2k-2)\log(1+q)
       +k\log2-2k\log(1-q)+(m+k+2)\log s
\]

satisfies \(\mathcal H_m>300099/100>3000\). Thus these product, ordering
and upper-count premises, even with the stipulated exact finite-height
total, do not force L836's coarse sufficient overlap inequality
\(\mathcal H_m<0\). This is an obstruction to that sufficient scalar
deduction, not a negative minor, failure of actual overlap, counterexample
to RH, or result beyond the assessed general product/separation theory.
The model itself has all its product zeros positive real.

## Proof

**Purpose and imported standard input.** The invocation-start SPECIALIZE
assessment is `drafts/literature/2026-11-07-count-only-overlap-obstruction-scope.md`.
We specialize prescribed-product theory to one explicitly count-admissible
sequence; neither the convergence theorem nor general separation theory
needs reproof. The product convergence input is NIST DLMF
[Section1.10(ix), M-test (1.10.20)–(1.10.21) and the following alternative
hypothesis](https://dlmf.nist.gov/1.10.ix): a summable uniform bound on
analytic factors' increments gives compact product convergence, and zeros
can occur only at factor zeros. This is applied below with an explicit
summable bound. Heittokangas–Laine, *Solutions of f''+A(z)f=0 with prescribed
sequences of zeros*, Acta Math. Univ. Comenianae LXXIV(2) (2005),287–307,
Section2/(2.1) p.289 and Example2.4 pp.291–292,
[primary journal PDF](https://emis.de/ft/28373), provides the assessed
prescribed-zero/nonseparation context; its example is not our construction
or a proof of this count or sign. The Bellotti–Wong upper envelope recorded
in L836 is imposed here as a model hypothesis, not applied as a theorem
about arbitrary products. No new external source is needed.

**1. Explicit complete sequence.** Let delta=10^(-12) and define

\[
 \gamma_j=10000-\frac{k-j}{k}\quad(1\le j\le k),\qquad
 \gamma_J=10000+\delta,
\]
\[
 \gamma_{J+l}=H-1+\frac{l}{K-J}\quad(1\le l\le K-J),\qquad
 \gamma_{K+n}=H+n\quad(n\ge1).
\]

The first packet starts at 9999+1/k and increases in steps 1/k to
10000. The selected omitted ordinate T=10000+delta is strictly larger.
It is below H-1. The next K-J ordinates increase strictly from above
H-1 to exactly H; all later ordinates are H+1,H+2,.... Thus every
boundary between packets is strict, all ordinates are positive and
distinct, T>4, and the sequence tends to infinity. Exactly K ordinates
are at or below H, including the one equal to H.

**2. Certified scalar bounds used for every height.** The exact-rational
certificate `scripts/count-only-overlap/countermodel-104.json`, generated
by `python3 scripts/count-only-overlap/countermodel-104.py`, proves

\[
 U(9999)>10152>J,\qquad U(H-1)-K>11,
 \qquad \frac{\log(9999/(2\pi))}{2\pi}>\frac{117}{100}>1. \tag{1}
\]

These are strict rational comparisons, not comparisons of decimal
previews. The following specifies the complete arithmetic certificate
method, including its truncation errors. Use Machin's identity
\(\pi=16\arctan(1/5)-4\arctan(1/239)\), with 50 alternating
terms of each arctangent series; its error lies between zero and the
first omitted term, with the appropriate sign. The identity follows,
for example, from tan(2 arctan(1/5))=5/12 and
 tan(4 arctan(1/5))=120/119, so subtracting arctan(1/239)
gives tangent 1 in (0,pi/2). For positive rational x write x=2^h y,
1<=y<2. With z=(y-1)/(y+1), use

\[
 \log y=2\sum_{n=0}^{49}\frac{z^{2n+1}}{2n+1}+E,
 \qquad 0\le E\le\frac{2z^{101}}{101(1-z^2)}. \tag{2}
\]

This is the usual integrated geometric series; each omitted denominator
is at least101, giving the displayed geometric tail bound. The same
formula at y=2 encloses log2, and signed interval multiplication by h
preserves its error direction. For a positive interval, monotonicity of
log applies (2) at its endpoints. Rational interval addition,
multiplication and division then enclose U and every other expression;
no floating-point operation enters the checks. The certificate stores
both complete rational endpoints and the small rational witnesses (1).
The Python source includes each operation and asserts all comparisons.
The Machin branch above is unambiguous since the difference is positive
and less than4/5<pi/2.

For t>=9999, differentiation gives

\[
 U'(t)=\frac{\log(t/(2\pi))}{2\pi}+\frac bt
      >\frac{\log(9999/(2\pi))}{2\pi}>1. \tag{3}
\]

The b/t term was **omitted**, not assumed increasing, in the uniform
lower bound. For every t>=e put x=t/(2pi)>0. The function
x log x-x has minimum -1 at x=1; hence
U(t)>=d-1+b log t>0, including heights below9999.

Now check all height regimes, with inclusive endpoints. For
 e<=t<gamma_1, N(t)=0<U(t). For gamma_1<=t<H-1, there are at most J
ordinates and t>9999, so (1),(3) give N(t)<=J<U(t). For
 H-1<=t<H, there are at most K ordinates and U(t)>=U(H-1)>K.
Finally for t>=H,

\[
 N(t)=K+\lfloor t-H\rfloor\le K+(t-H)
        <U(H)+(t-H)\le U(t).
\]

The last inequality follows by integrating (3), with equality permitted
only in that last comparison at t=H. Thus every finite packet jump,
the jump at H, all later integer-height jumps, and intervening heights
are covered. This proves the stipulated all-height upper bound.

**3. Summability, product and simplicity.** The first K ordinates are
at least9999, so their reciprocal-square sum is at most K/9999^2,
a finite number regardless of the large packet cardinality. For the tail,

\[
 \sum_{n\ge1}(H+n)^{-2}\le\sum_{n\ge1}n^{-2}
       \le1+\int_1^\infty x^{-2}\,dx=2.
\]

For |z|<=A, the sum of suprema of the factor increments is therefore
at most (A/4) sum_j gamma_j^(-2)<infinity. The cited DLMF M-test gives
compact convergence to an entire function F and no zeros away from the
prescribed factor zeros. F(0)=1. Fix a prescribed zero p=4 gamma_j^2.
Remove its factor. The residual product has the same convergence bound,
and no factor vanishes at p; the cited nonvanishing statement makes its
value at p nonzero. Thus F=(1-z/p) times an analytic function nonzero
at p, proving multiplicity exactly one. All its zeros are positive real
because all ordinates are positive and strictly ordered. Real factors
and compact limits give F(conjugate z)=conjugate F(z). This verifies
all product obligations; no extra exponential multiplier was inserted.

**4. All scalar domains and the exact sign.** Let g=gamma_k=10000.
Then T=g+delta and

\[
 \epsilon=1-q=\frac{2g\delta+\delta^2}{g^2+T^2}
       <\frac{3\delta}{g}=3\cdot10^{-16}<10^{-15}.
\]

Here delta<g and the denominator exceeds g^2. Consequently
0<q<s=1-epsilon/2<1 and 0<a=(1+(g/T)^2)/2<1. R>0, and every
logarithm argument in H_m and B(s) is strictly positive. In particular,
the packet-to-contour distances s-q and 1-q are strictly positive.
Certificate (2) and the same rational interval arithmetic also give

\[
 V(T)>17/100000>0,\qquad \log2>1/2. \tag{4}
\]

The full endpoints and all six separate terms of H_m are retained in
the certificate. For an independent coarse sign check that avoids
cancellation, use for 0<x<1 the elementary inequality
-log(1-x)<=x/(1-x). At x=epsilon/2 this gives

\[
 -\log s\le\frac{\epsilon}{2-\epsilon}<\epsilon.
\]

Since m+k+2<10^13, the **entire last term** is greater than -1/100.
Every other term of H_m is positive: (4) makes the second summand of
B(s) positive and (1+sa)/(1-a)>1 makes its logarithm positive;
k>1, 1+q>1 and 0<1-q<1 give the signs of the remaining logarithms.
Keeping k log2 explicitly therefore proves for the exact expression

\[
 \mathcal H_m> k/2-1/100=300099/100>3000.
\]

Nothing was replaced by an arbitrarily enlarged upper bound C_+.
In fact the rational interval evaluation of the full unrounded formula
also has a positive lower endpoint; that stronger numerical margin is
unnecessary to the conclusion. The threshold required for the coarse
sufficient overlap certificate is strict negativity, so this model
fails it decisively. No necessary sign condition or determinant value
was tested. Additional actual-Xi structure, finer finite-product
estimates, indexed data, growing shifts and mixed signs remain open.

### Independent conceptual audit — 7 November 2026, step106

The exact target in the prior SPECIALIZE assessment
`drafts/literature/2026-11-07-count-only-countermodel-audit-scope.md`
passes without a mathematical correction. This validates the local
obstruction, not a new general theorem or an actual-Xi sign.

**All-height quantifiers.** Section2's four ranges partition all t>=e.
The first ordinate is above 9999; T lies in the range with at most J
ordinates. There is no ordinate at H-1, and the last finite-packet
ordinate is exactly H. Thus N(H)=K and the stated floor formula holds
at every later integer jump and between jumps. The derivative bound
uses the increasing log(t/(2pi))/(2pi) and discards positive b/t; it
does not infer monotonicity of U' from an endpoint evaluation. Below 9999,
the global minimum of x log x-x supplies positivity of U. No height
interval or inclusive count endpoint is omitted.

**Product quantifiers.** K is finite, so K/9999^2 is a valid finite
head bound. The unit-spaced infinite tail supplies the summable
reciprocal-square majorant on every disk. The cited DLMF increment
M-test applies also after removing any selected factor. Distinctness
makes every remaining factor nonzero at that zero; the theorem's
nonvanishing conclusion, not compact convergence alone, gives a nonzero
residual value. The factorization persists under compact limits and
proves simplicity. F(0)=1 fixes normalization. No quantitative separation,
Xi identification or extra exponential factor is assumed.

**Complete rational evidence.** Reproduce the audit with
`python3 scripts/count-only-overlap/audit-106.py`. It executes the original
generator with a separate output path and preserves the original certificate
byte for byte. All 15 full rational intervals (nine bounds and six signed
terms) reproduce exactly; all 53 audit checks pass with no failures. The
full replay is `scripts/count-only-overlap/audit-replay-106.json`, and
the audit certificate is `scripts/count-only-overlap/audit-106.json`.
The latter records source/output hashes and exact outward rational
witnesses. Every endpoint is parsed completely; neither decimal previews
nor stored original pass flags establish the comparisons.

The source algorithms were also checked on paper. The 50-term arctangent
partial sums are lower bounds, with positive first-omitted-term errors;
the coefficient -4 reverses the appropriate Machin interval endpoints.
Log reduction leaves 1<=y<2, including arguments below 1 whose negative
shift reverses the log2 interval endpoints. The geometric remainder (2)
has exponent 101 and denominator 101. Interval divisors exclude zero and
logarithm arguments are positive. Fraction arithmetic is exact throughout;
Decimal is used only for previews. Replay uses the original implementation,
not an independent numerical library: the source audit and section4's
independent analytic lower bound are essential parts of verification.

For readable evidence, the following lower enclosures were rounded
outwards from the complete fractions to denominator dividing 10^12:

| Quantity | Rational lower enclosure | Required strict bound |
| --- | --- | --- |
| U(9999) | 5076090640060059/500000000000 | >10152>J |
| U(H-1)-K | 746868062299/62500000000 | >11 |
| log(9999/(2pi))/(2pi) | 586674030777/500000000000 | >117/100>1 |
| V(T) | 34951433/200000000000 | >17/100000>0 |
| (m+k+2)log s | -450000001/1000000000000 | >-1/100 |

**Signed expression and scope.** L836(15) and L835(4) give exactly the
six terms here; substituting r=m+1 yields m+k+2. The complete signed
interval sum equals the stored H_m interval, with its last term strictly
negative and its other five terms strictly positive. Separately, exact
epsilon arithmetic and the elementary log bound give
(m+k+2)epsilon/(2-epsilon)<1/100. With V>0 and log2>1/2 this verifies
H_m>300099/100 without relying on the much larger full numerical margin.
No enlarged C_+ replaces the expression being tested.

The declared abstract premises therefore do not force the coarse sufficient
inequality. Bellotti–Wong's stronger upper expression and lower bound are
not imposed, and its zeta theorem is not applied to F. No negative minor,
failure of finer overlap or off-line zeta zero follows. The DAG input
remains L836 for the scalar definitions; L835 supplies sufficiency context,
not an actual-function theorem applied to the replacement product.
No new mathematical dependency or missing sign assumption was found.

### Repeated verification — 8 November 2026, step118

The startup checkpoint nominated the exact audit already completed at
step106 above. A fresh analytic check of all four inclusive height
regimes, the summable removed-factor product and the unrounded six-term
expression found no defect. The exact replay again checked all 15 full
rational intervals and passed all 53 checks, with no failures. Separate
outputs are `scripts/count-only-overlap/audit-replay-118.json` and
`scripts/count-only-overlap/audit-118.json`. The five step104/106 source
and certificate artifacts retain their original hashes. This used the
existing audit source with only its two output filenames changed;
its algorithms and the proof above were unchanged. It is repeated
verification, with no new mathematical evidence, not a second advance
or informative negative. The count-only route remains closed at its
declared scope; no further identical audit is warranted.

## Mathlib

Full matching coverage has not been checked; no absence claim is made.
Supporting real-log inequalities, power series, infinite products and
finite rational arithmetic are standard, but neither the specific
count-admissible sequence nor this exact coarse-overlap calculation is
claimed formalized. This is an informally audited standard-method
specialization, not a new general product theorem or a formal proof.
