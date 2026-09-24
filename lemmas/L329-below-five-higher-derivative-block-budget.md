# Lemma 329: higher-derivative cancellation and the below-five block budget

**Hypotheses.** Use L326's admissible sequence and exact weights:

r=8n/3, p=2n=3r/4, a=a_n=sqrt(4π²exp(4r)−(39/8)²),
W_r(j,k)=(jk)^(−1/2)(1−log(jk)/(2r))^p for jk<exp(2r),
E_r=(1+r)²exp(−r/200).

Put Y=exp(r/2), b=ceil(Y), c=floor(2Y), and define the unmollified first-row block

B_r=Σ_(k=b)^c W_r(1,k)exp(ia log k),
M_r=Σ_(k=b)^c W_r(1,k),
κ=1/4+(3/4)log(3/4).

The full sum S_r(a) in L326 contains B_r and its conjugate in the transposed first-column block. All these indices are inside its product cutoff for sufficiently large r. No conclusion from a finite Möbius convolution is assumed for B_r.

**Conclusion.** The exact coefficient mass is

M_r=(log 2+O(1/r))exp(κr), κ>7/216>1/40.             (1)

Keeping every term of the indicated derivative theorems and transferring their uniform partial-sum bounds by Abel summation gives the following certificates. The entries in the last column describe the exponential scales of the resulting upper bounds, not the size of B_r from below.

| Test | Uniform partial-sum bound on this block | Weighted certificate for B_r |
| --- | --- | --- |
| Classical fifth derivative | O(Y^(29/30)) | O(exp((κ−1/60)r)) |
| Classical sixth derivative | O(Y^(481/496)) | O(exp((κ−15/992)r)) |
| Heath-Brown fifth derivative | O_ε(Y^(19/20+ε)) | O_ε(exp((κ−1/40+ε/2)r)) |
| Heath-Brown sixth derivative | O_ε(Y^(29/30+ε)) | O_ε(exp((κ−1/60+ε/2)r)) |

Here ε>0 is arbitrary and fixed. The stronger fifth-order theorem gives a nontrivial relative saving, but even its envelope with the ε loss removed grows at least as exp(r/135), up to a constant factor. It therefore does not certify B_r=o(1), much less B_r=o(E_r).

Changing to another fixed derivative order in either of these two theorems cannot improve the saving beyond 1/40 in r. The same ceiling holds for any fixed finite collection of orders, even after division into shorter consecutive blocks, Abel summation within each block, and the triangle inequality between blocks. This is a limitation of these specified bound formulas, not an optimality theorem for exponential sums or a lower bound on |B_r|. Estimates using further phase information or cancellation between blocks are not excluded.

Thus this test supplies no positive arithmetic margin for L326, no new Laguerre sign, and no zero exclusion. Even success on this single block would have left the other blocks and the full arithmetic surplus unresolved.

**Proof.** Write w(x)=W_r(1,x) on [Y,2Y]. Set

w₀=Y^(−1/2)(3/4)^p.

For 1≤t≤2, uniformly as r→∞,

w(Yt)/w₀=t^(−1/2)(1−2log(t)/(3r))^(3r/4)
          =t^(−1)(1+O(1/r)).                          (2)

Indeed log(1−u)=−u+O(u²) uniformly for |u|≤1/2, and here u=2log(t)/(3r). Multiplication by 3r/4 makes the remainder O(1/r), uniformly in t. The summands in (2) are positive. The Riemann sum for t^(−1) has error O(1/Y), including the rounded endpoints, so

M_r=Yw₀(log 2+O(1/r)+O(1/Y)).

Since Yw₀=exp(κr), this proves the asymptotic in (1). Also w(b) is comparable to w₀ and w(c) is comparable to w₀/2. Direct differentiation gives

d log w(x)/d log x=−1/2−p/(2r−log x)<0,             (3)

so all discrete differences needed below are nonnegative. In particular the cutoff, monotonicity and weight comparison are checked for the actual coefficients, not an extended polynomial beyond its support.

We specify the two external finite-sum inputs. D. R. Heath-Brown, *A New k-th Derivative Estimate for Exponential Sums via Vinogradov's Mean Value*, [equation (1), p. 1](https://arxiv.org/pdf/1601.04493#page=1), records the classical bound

|Σ e(f(k))|≤C_d,A [m λ^(1/(2^d−2))
                     +m^(1−2^(2−d))λ^(−1/(2^d−2))],          (4)

when f has d continuous derivatives on a translated interval of m integers and 0<λ≤|f^(d)|≤Aλ. Here e(t)=exp(2πit); sign reversal handles a negative derivative. Fixed d and A suffice. Olivier Robert's [Theorem 3, equation (17), p. 8, and its restatement (30)–(31), p. 18](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf#page=8) give the same classical input. The kth-derivative hypothesis is explicit in Heath-Brown's statement and Robert's restatement; the double prime in the extraction of Robert's (16) is not used as a kth-derivative hypothesis.

Heath-Brown's [Theorem 1, p. 3](https://arxiv.org/pdf/1601.04493#page=3) gives, for fixed d≥3 and ε>0 under the same derivative comparison,

|Σ e(f(k))|≤C_d,A,ε m^(1+ε)
 [λ^(1/(d(d−1)))+m^(−1/(d(d−1)))
                   +m^(−2/(d(d−1)))λ^(−2/(d²(d−1)))].       (5)

Both are unconditional finite-sum estimates. They do not themselves involve the theta weights or assert any sign. Empty sums and singletons can always be bounded trivially.

For our actual phase f(x)=a log(x)/(2π),

f^(d)(x)=(−1)^(d−1)(d−1)!a/(2πx^d).                (6)

Every integer subinterval of [b,c] can be translated to [1,m], or to (0,m] for (5). The latter extension only needs x≥Y−1≥Y/2. On [Y/2,2Y] choose

λ_d=(d−1)!a/(2π(2Y)^d), A_d=4^d.

Then (6) satisfies both hypotheses, after conjugating for even d, and

λ_d is comparable to Y^(4−d),                       (7)

with constants depending only on the fixed order d. This follows from a/(2πY^4)→1 along the exact sequence; the small difference between a and 2πY^4 is retained, not substituted in the phases. The derivative sign never changes. Every prefix length is at most Y+1. Each power of m on the right of (4) and (5) is nonnegative for d≥3, so replacing m by 2Y bounds all prefixes with the same constant.

For d=5, the two exponents of Y in (4) are

1−1/30=29/30,
7/8+1/30=109/120.

The first dominates. For d=6 they are

1−2/62=30/31=480/496,
15/16+2/62=481/496.

The second dominates: keeping only the first would give an unjustified better exponent. In (5), after removing the common ε loss, the three exponents are respectively

d=5: 19/20, 19/20, 23/25;
d=6: 14/15, 29/30, 43/45.

This proves the partial-sum column of the table, including every short prefix and the endpoint rounding.

For the weighted transfer put A_t=Σ_(k=b)^t exp(ia log k). The exact finite Abel identity is

B_r=w(c)A_c+Σ_(t=b)^(c−1)(w(t)−w(t+1))A_t.

By (3) its absolute-value bound is at most w(b)max_t|A_t|. Thus a uniform certificate O(Y^(1−δ+ε)) becomes

O_ε(w₀Y^(1−δ+ε))
 =O_ε(exp((κ−δ/2+ε/2)r)).                           (8)

Equations (2) and (8) give the four weighted entries. They represent actual improvements on M_r, but none has negative exponential rate.

For completeness, the failure is not repaired by picking another fixed order in these formulas. For d≤4 the first term in (4) is at least a fixed multiple of m: (7) is bounded below for d=4 and grows for smaller d. Taking the minimum with the trivial certificate m still gives no power saving. For d≥5 the first term alone in (4) is comparable to

mY^(−g_d), g_d=(d−4)/(2^d−2).

One has g_5=1/30, and g_(d+1)≤g_d for d≥5. Cross-multiplication reduces the latter inequality to (d−5)2^d+2≥0. Hence even the optimistic first term restricts this classical certificate to a saving of at most Y^(1/30), or exp(r/60). Additional terms can only weaken it, as the sixth-order calculation illustrates.

For (5), ignore the harmless factor m^ε≥1 when finding a floor on its certificate. Its first term is comparable to mY^(−(d−4)/(d(d−1))). For d≤4 it again gives no power saving. For d=5 this term is comparable to mY^(−1/20). For d≥6 the second term, for every 1≤m≤Y+1, is

m^(1−1/(d(d−1)))≥C_d mY^(−1/(d(d−1)))
                         ≥C_d mY^(−1/20).           (9)

Thus the minimum of the trivial, classical and newer certificate scales is at least a fixed positive multiple of mY^(−1/20), for each fixed order and also for any fixed finite collection of orders. Constants may depend on that collection; a derivative order increasing with r is not being tested.

The same argument covers shorter-block subdivision. In a subinterval of m terms, the endpoint term in its Abel certificate is the final positive weight times the chosen full partial-sum certificate. Every such weight is at least w(c), comparable to w₀. Equations (9) and the preceding classical floor therefore give a certificate floor Cw₀mY^(−1/20). Summing those nonnegative certificate terms over a partition gives at least

Cw₀Y^(19/20)=Cexp((κ−1/40)r).                       (10)

This is a lower bound on the numerical right-hand sides produced by these triangle/Abel estimates, not on the sums being estimated. It precludes an improvement of the threshold merely by subdivision and taking minima of the listed fixed-order estimates. No statement is made about retaining correlations between the subintervals.

Finally, integrating the alternating geometric series on [0,1/3] gives

log(4/3)<1/3−1/18+1/81=47/162.

Consequently κ>1/4−(3/4)(47/162)=7/216, and

κ−1/40>7/216−1/40=1/135>0.                         (11)

Even (10), which drops every ε loss, tends to infinity; divided by E_r its scale is exp((κ−1/40+1/200)r)/(1+r)², also diverging. This compares the achieved certificate with both the intermediate o(1) target and the assembled error. Failure against E_r alone would not rule out dominance by a constant positive main term; the stronger failure against o(1) is what stops this block-removal test. L326 still requires a positive lower bound for the complete signed S_r, and none is supplied here. ∎

This result extends the derivative-budget check to small higher derivatives and to the cited stronger theorem. L305 concerns a different endpoint weight and only second and third derivatives; it is a contrast, not an input applied outside its hypotheses. L328's rough-ratio obstruction motivates the block but is not needed for the unmollified proof. No actual negative value, off-line zero, or RH candidate follows.

**Mathlib.** Full statement: not checked. Supporting finite Abel summation, logarithm differentiation, uniform Taylor estimates and Riemann-sum comparison: not checked for library coverage. The classical kth-derivative estimate in Robert's Theorem 3 and Heath-Brown's equation (1), and the stronger estimate in Heath-Brown's Theorem 1, are supporting external results at the direct links above; they do not match this full weighted statement. No Mathlib theorem name or full library match is claimed. The phase comparison, exact weight asymptotic, transfer, fixed-order certificate ceiling and required-bound comparison are proved here.
