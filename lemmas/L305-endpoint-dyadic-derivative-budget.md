# Lemma 305: endpoint dyadic derivative budget

**Hypotheses.** Use W_r and T_r from L297, S_r from L303, and the admissible parameters r=2n and a=a_n=sqrt(4π²exp(4r)−25) from L302. Put K=ceil(exp(r/2))−1 and

H_r(a)=Σ_(1≤j,k≤K) W_r(j,k) exp(ia log(k/j)),
D_r=Σ_(j≤K) W_r(j,j),  O_r(a)=H_r(a)−D_r.

**Conclusion.** Uniformly in real a for the cutoff assertion,

|S_r(a)−H_r(a)|=O(r exp(−r/32)).                         (1)

Moreover D_r→ζ(2), while the absolute off-diagonal coefficient mass in H_r is 4r+o(r). At a=a_n, the classical second- and third-derivative tests, capped by the trivial bound, give no saving on any consecutive subinterval of any dyadic block in [1,K]. Applying those partial-sum bounds to the exact weights by Abel summation therefore supplies only the absolute off-diagonal certificate 4r+o(r). This does not bound |O_r(a_n)| from below or assert a negative sign. The certificate fails the sufficient diagonal-dominance target |O_r(a_n)|≤D_r−δ for any fixed δ>0, and does not establish L302's required positive margin.

**Proof.** The decreasing-coordinate property and Gaussian majorant from L297 give, with B=log K,

Σ_(j>K,k≥1) W_r(j,k)
 ≤∫_K^∞ W_r(x,1)dx+∫_K^∞∫_1^∞ W_r(x,y)dy dx
 ≤(4r/B+4r)exp(−B²/(8r)).

Indeed x=exp(u), y=exp(v) converts these integrals into integrals of Q_r(u) and (L−B)Q_r(L), respectively, and Q_r(L)≤exp(−L²/(8r)). A union bound for the two coordinates proves (1), since B=r/2+O(exp(−r/2)). This repeats L303's discrete-tail argument at a smaller cutoff, not merely a continuous-tail approximation. In particular the discarded mass divided by (1+r)²exp(−r/256) tends to zero, with exponential factor exp(−7r/256).

For each fixed j, W_r(j,j)=j^(−1)(1−log j/r)^r→j^(−2). The inequality (1−t)^r≤exp(−rt) gives 0≤W_r(j,j)≤j^(−2). Extend the truncated diagonal terms by zero for j>K. Dominated convergence for the summable sequence j^(−2) proves D_r→ζ(2). L297 proves that the full coefficient mass is 4r+o(r); (1), applied to absolute masses, gives the same asymptotic inside [1,K]². Subtracting D_r proves the off-diagonal mass assertion.

Here is the precise derivative-certificate test. On [N,2N], with N a power of two and N≤K, write e(f(x))=exp(ia log x), so f(x)=a log x/(2π). Then

|f''(x)|=a/(2πx²),  |f'''(x)|=a/(πx³).

Their lower bounds on the whole block are λ₂=a/(8πN²) and λ₃=a/(8πN³), with upper/lower ratios 4 and 8. Since a is asymptotic to 2πexp(2r) and N≤exp(r/2), uniformly λ₂ grows at least as exp(r) and λ₃ at least as exp(r/2), up to fixed positive constants. Both eventually exceed one. The sign-reversed phase obeys the same bounds.

For an interval of m consecutive integers in the block, the standard named van der Corput tests give scales

m sqrt(λ₂)+λ₂^(−1/2),
m λ₃^(1/6)+sqrt(m)λ₃^(−1/6).

The source is Olivier Robert, [On van der Corput's k-th derivative test for exponential sums](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf), Theorem 1, p. 5, and the third-derivative derivation preceding Theorem 2, p. 8, in the form recorded in foundations/notation-and-inputs.md. Empty and singleton sums are trivial. Each displayed scale is at least m when λ₂,λ₃≥1; in fact its first term divided by m tends uniformly to infinity here. Thus these tests combined with |Σ e(f(j))|≤m give only the latter bound, including every partial interval and the clipped final block. These are statements about the estimates, not lower bounds on exponential sums.

For completeness, let w_j=W_r(j,k) for a fixed k and j in any consecutive interval [p,q]. It is nonnegative and decreasing. With A_t=Σ_(j=p)^t exp(−ia log j), finite Abel summation gives

Σ_(j=p)^q w_j exp(−ia log j)
 =w_q A_q+Σ_(t=p)^(q−1)(w_t−w_(t+1))A_t.

Using just |A_t|≤t−p+1 makes the right-hand absolute bound exactly Σ_(j=p)^q w_j, by telescoping. Excluding j=k splits an interval into at most two intervals; the same calculation applies to each. Partition into disjoint dyadic blocks and sum in k by triangle inequality. This produces precisely Σ_(j,k≤K,j≠k) W_r(j,k)=4r+o(r), with all curvature weights retained. It supplies no cancellation saving over that certificate.

Finally H_r is real by swapping j,k. If |O_r(a_n)|≤D_r−δ were established for a fixed positive δ, then H_r(a_n)≥δ; (1) and L303's T_r−S_r estimate would preserve a fixed positive margin for T_r. That would dominate L302's error. Instead the available certificate grows linearly while D_r tends to a finite positive constant. Even an o(1) estimate for O_r is not obtained. Such diagonal dominance is sufficient, not necessary: the off-diagonal contribution could be large and positive. No claim is made about its actual sign or size. ∎

This stops only separate-row second- and third-derivative estimates followed by absolute dyadic summation. Differencing with further arithmetic information, estimates whose derivative order grows with r, cancellation between rows, and multiplicative regrouping are not ruled out. L174 and L231 concern other phases and thresholds; their derivative-budget failures are precedents, not mathematical inputs here. L304 concerns freezing a different coefficient array, whereas this calculation keeps W_r exact. No endpoint positivity, extended sign range, or RH candidate follows.

**Mathlib.** Full statement: not checked. Supporting finite Abel summation, dominated convergence, and the van der Corput derivative tests: not checked. No library match is claimed. Robert's named results above support only the unweighted finite-sum bounds, not this full endpoint statement. The discrete cutoff, diagonal limit, curvature comparison, weighted budget, and threshold comparison are proved here.
