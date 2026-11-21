# C034u: uniform finite-scale primitive remainder, reproduced and replayed

## Hypotheses

Use the actual theta kernel, weighted space
\(E=L^2(\mathbb R,e^{-y/2}dy)\), unitary map \(Jv=e^{-y/4}v\),
translations \(T_rv(y)=v(y+r)\), and fixed real bump input
\(h=-g''+g/4\), \(g(y)=e^{-1/(1-y^2)}1_{|y|<1}\), of C034r.
Put \(Q=\log2\), \(\psi=C_\Phi h\), \(f=J\psi\), and
\[
 C_h(r)=\int_{\mathbb R}f(y)\overline{f(y+r)}\,dy,\qquad
 \rho(M)=\zeta(2)^{-1}\prod_{p\mid M}\frac p{p+1}.
\]
The inner product is linear in its first slot. For real \(X\ge1\), let
\[
 U_Xh=\sum_{X/2<n\le X}\mu(n)n^{-1/2}\log(X/n)
                      T_{\log(n/X)}\psi.
\]
All indices here and below are positive integers. For integer
\(1\le K\le X\), define the **unprojected primitive sector**
\[
 E_{\le K}(X)=X^{-1/2}
 \sum_{\substack{X/2<n,k\le X\\
              \max(n/(n,k),k/(n,k))\le K}}
 \frac{\mu(n)\mu(k)}{(nk)^{1/4}}
 \log(X/n)\log(X/k)C_h(\log(k/n)).                         \tag{1}
\]
This is a sector in a square expansion; it is not a Fourier projection
or an assumed nonnegative quantity. Define
\[
 w_Q(r)=\begin{cases}
 \displaystyle\int_{|r|/2}^{Q-|r|/2}
             e^{-s/2}(s^2-r^2/4)\,ds,&|r|<Q,\\
 0,&|r|\ge Q,
 \end{cases}
\]
\[
 M_K=\sum_{\substack{a,b\le K\\(a,b)=1}}
       \frac{\mu(a)\mu(b)\rho(ab)}{\sqrt{ab}}
       w_Q(\log(b/a))C_h(\log(b/a)).                       \tag{2}
\]
This agrees with C034s's definition when \(K\ge2\), and explicitly
extends that notation to \(K=1\). Its pole-pair assertions are not
inputs. No zero premise or arithmetic sign premise is imposed.

## Conclusion

There is a constant \(C_*\), independent of \(X,K\) and of the input's
norm, such that throughout the stated range
\[
 |E_{\le K}(X)-M_K|
 \le C_* C_h(0)X^{-1/2}K^{3/2}\log^2(2K).                 \tag{3}
\]
An admissible explicit constant is
\[
 \begin{split}
 B_Q&=3\{2Q^2+(Q^2/2+2Q)Q\},\\
 S_Q&=Q^{-2}+
       \frac{4\,2^{1/4}(1+Q^{-1})^2}{1-2^{-3/2}},\qquad
 C_*=B_QS_Q.                                             \tag{4}
 \end{split}
\]
In particular, for this fixed input and any fixed \(A>0\), the integer
\(K(X)=\lfloor X^{1/3}e^{-A(\log X)^{1/3}}\rfloor\) is admissible
eventually and the error in (3) is \(o(1)\).

Writing \(E_{>K}(X)=\|U_Xh\|_E^2-E_{\le K}(X)\), the exact source
split has error bounded by (3). For any additional vectors \(V_X\in E\)
satisfying the separately assumed estimate
\[
 \big|\|V_X\|_E^2-\|U_Xh\|_E^2\big|\le\epsilon_X,        \tag{5}
\]
it follows that
\[
 \big|\|V_X\|_E^2-M_K-E_{>K}(X)\big|
 \le \epsilon_X+C_*C_h(0)X^{-1/2}K^{3/2}\log^2(2K).       \tag{6}
\]
Consequently GC18 for the source's completed gamma vector follows
conditionally on its separate GC6 estimate. Neither GC6, an upper for
either signed sector, a cumulative-energy upper nor actual-Xi mixed
positivity is established here. No RH candidate results.

## Proof

### Source and reason for reproduction

This reproduces Leonard van Hemert, *Exact Zero Detection and Compact
Arithmetic Realizations for the Riemann Xi Function*, v1.0.0,
11 October 2026, DOI 10.5281/zenodo.23295277,
[tagged primary TeX](https://raw.githubusercontent.com/LeonardSEO/riemann-xi-zero-detection/refs/tags/v1.0.0/paper/paper.tex),
`thm:log-primitive-remainder`, GC12-GC18 and complete proof,
lines11613-11717. Assessment2089/source-notes2090 already approved
this exact specialization. The proof was retrieved in full again for
this audit. The manuscript already states (3): this is local verification
of a known assertion, not progress beyond the sources checked.
The reproduction makes its endpoint and constant uniformity explicit,
checks the actual C034r input and extends the gamma section's \(X\ge2\)
setup down to the source's stated \(X\ge1\).

The elementary coprime count used below is the radical specialization
of Giuseppe Molteni, *Analytic Number Theory*, Spring2026, revision9.0,
[Proposition3.2 (Eratosthenes-Legendre), printed pp68-69](https://sites.unimi.it/molteni/didattica/matematica/analytic_number_theory/appunti-AnNTh.pdf).
It counts integers in \((x,x+y]\) coprime to a squarefree modulus with
error at most the number of its divisors. Replacing a general modulus
by its radical preserves coprimality and \(\varphi(M)/M\).
The derivation below is the required square-divisor/weighted
specialization, retaining the restrictions and real endpoints; it
does not reprove a general sieve theorem. Other standard inputs are
Cauchy-Schwarz and finite summation by parts.

### 1. Square expansion, reduction and support

C034r proves \(\psi\in E\) and
\(JT_r\psi=e^{r/4}T_rf\). Cauchy-Schwarz and translation invariance
of unweighted \(L^2\) give
\(|C_h(r)|\le C_h(0)=\|f\|_2^2<\infty\).
For \(r_n=\log(n/X)\), a change of variable gives
\[
 \langle T_{r_n}\psi,T_{r_k}\psi\rangle_E
 =e^{(r_n+r_k)/4}C_h(r_k-r_n).
\]
Expansion of the finite sum therefore gives exactly (1) without its
primitive restriction for \(\|U_Xh\|_E^2\). There is no interchange
of infinite sums or integrals.

Write \(n=da,k=db,(a,b)=1\). If \(a\) or \(b\) is nonsquarefree,
the original slot vanishes, as does its proposed main term. Otherwise
\[
 \mu(da)\mu(db)=\mu(a)\mu(b)\mu(d)^2\mathbf1_{(d,ab)=1}.
\]
For \(m=\min(a,b),N=\max(a,b)\), set
\[
 \alpha=\frac X{2m},\quad \beta=\frac XN,\quad
 v_{a,b}(t)=t^{-1/2}\log\frac X{ta}\log\frac X{tb}.
\]
The slot in (1) is exactly
\[
 X^{-1/2}\frac{\mu(a)\mu(b)}{(ab)^{1/4}}
 C_h(\log(b/a))
 \sum_{\substack{\alpha<d\le\beta\\(d,ab)=1}}
                      \mu(d)^2v_{a,b}(d).                \tag{7}
\]
The lower endpoint is strict; the upper endpoint is inclusive.
If \(N\ge2m\), this interval is empty, including equality, and
\(|\log(b/a)|\ge Q\) makes (2)'s slot zero too. Such slots are
discarded with zero error, not assigned a reversed integral.
For all remaining slots \(\alpha<\beta\) and
\(1<\beta/\alpha\le2\). The interval can still contain no integers;
the summation-by-parts argument below includes that case.

### 2. Uniform squarefree count, including arguments below one

Let \(D(M)=2^{\omega(M)}\) and
\(A_M(Y)=\sum_{d\le Y,(d,M)=1}\mu(d)^2\). We claim, for all
positive integers \(M\) and positive reals \(Y\),
\[
 |A_M(Y)-\rho(M)Y|\le3D(M)\sqrt Y.                       \tag{8}
\]
For \(Y\ge1\), the identity \(\mu(d)^2=\sum_{k^2\mid d}\mu(k)\)
gives exactly
\[
 A_M(Y)=\sum_{\substack{k\le\sqrt Y\\(k,M)=1}}\mu(k)
                  \#\{\ell\le Y/k^2:(\ell,M)=1\}.
\]
The condition \((k,M)=1\) is essential. The cited coprime count
(at left endpoint zero), or its finite floor formula, bounds the
inner count minus \((\varphi(M)/M)Y/k^2\) by \(D(M)\).
The sum of these errors is at most \(D(M)\sqrt Y\).
The absolutely convergent main series is
\[
 \frac{\varphi(M)}M
 \sum_{(k,M)=1}\frac{\mu(k)}{k^2}
 =\frac{\varphi(M)}M\prod_{p\nmid M}(1-p^{-2})=\rho(M).
\]
If \(L=\lfloor\sqrt Y\rfloor\), then \(L\ge\sqrt Y/2\) and
\(\sum_{k>L}k^{-2}\le1/L\le2/\sqrt Y\). Extending the main
series therefore costs at most \(2\sqrt Y\), since
\(\varphi(M)/M\le1\). This proves (8) for \(Y\ge1\).
For \(0<Y<1\) its left count is zero and
\(0<\rho(M)Y\le Y\le\sqrt Y\), proving (8) there also.
No assumption that the main term dominates its error was used.

### 3. Weighted replacement, both endpoints and the main coefficient

In a nonempty real cap interval, both logarithms in \(v_{a,b}(t)\)
lie in \([0,Q]\). Consequently
\[
 |v_{a,b}(t)|\le Q^2t^{-1/2},\qquad
 |v'_{a,b}(t)|\le(Q^2/2+2Q)t^{-3/2}.                     \tag{9}
\]
These bounds hold at the endpoints too. For
\(R_M(t)=A_M(t)-\rho(M)t\), summation by parts with the right
continuous count on \((\alpha,\beta]\) is exactly
\[
 \begin{split}
 &\sum_{\substack{\alpha<d\le\beta\\(d,M)=1}}
      \mu(d)^2v_{a,b}(d)-\rho(M)\int_\alpha^\beta v_{a,b}(t)\,dt\\
 &=v_{a,b}(\beta)R_M(\beta)-v_{a,b}(\alpha)R_M(\alpha)
                         -\int_\alpha^\beta R_M(t)v'_{a,b}(t)\,dt.
                                                               \tag{10}
 \end{split}
\]
In particular, \(A_M(\alpha)\) excludes any atom at the lower
endpoint from the sum. Formula (10) remains true when the interval
has no integers. By (8)-(9) and
\(\log(\beta/\alpha)\le Q\), its absolute value is at most
\(B_QD(M)\), with \(B_Q\) in (4). This pays both endpoint terms;
in fact \(v_{a,b}(\beta)=0\), but no saving from that is needed.

Set \(r=\log(b/a)\) and substitute
\(t=Xe^{-s}/\sqrt{ab}\) in the integral in (10). Then
\[
 \log(X/(ta))=s+r/2,\quad \log(X/(tb))=s-r/2,
\]
and \(t^{-1/2}|dt|=\sqrt X(ab)^{-1/4}e^{-s/2}ds\).
The bounds become \(|r|/2\) and \(Q-|r|/2\), after reversing
the orientation. Thus
\[
 \int_\alpha^\beta v_{a,b}(t)dt
           =\sqrt X(ab)^{-1/4}w_Q(r).                     \tag{11}
\]
Multiplication by the outside coefficient in (7), and by \(\rho(ab)\),
gives exactly (2)'s coefficient \(\mu(a)\mu(b)\rho(ab)/\sqrt{ab}\).
There is no missing factor of \(X\), \(ab\) or two.

### 4. Summing the error: support, singleton and the last block

For coprime \(a,b\), \(D(ab)=D(a)D(b)\). Dropping \(|\mu|\le1\)
and using \(|C_h(r)|\le C_h(0)\), (7)-(10) bound the total error by
\[
 B_QC_h(0)X^{-1/2}
 \sum_{\substack{a,b\le K\\\max(a,b)<2\min(a,b)}}
             \frac{D(a)D(b)}{(ab)^{1/4}}.                 \tag{12}
\]
Enlarging from coprime to all pairs only increases this nonnegative
majorant. For real \(Y\ge1\), elementary divisor counting gives
\[
 \sum_{n\le Y}D(n)\le\sum_{n\le Y}\tau(n)
 =\sum_{d\le Y}\lfloor Y/d\rfloor\le Y(1+\log Y).        \tag{13}
\]
The pair \((1,1)\) contributes one. Partition the remaining pairs
into \(A<\max(a,b)\le\min(2A,K)\), \(A=1,2,4,\ldots<K\).
Support implies \(\min(a,b)>A/2\), so
\((ab)^{-1/4}\le2^{1/4}A^{-1/2}\). By (13), each block is at most
\[
 4\,2^{1/4}A^{3/2}(1+\log(2A))^2.
\]
This also bounds a truncated last block. Since \(A<K\),
\(1+\log(2A)\le(1+Q^{-1})\log(2K)\), and
\[
 \sum_{A=2^j<K}A^{3/2}
 \le\frac{K^{3/2}}{1-2^{-3/2}}.
\]
The singleton is at most \(Q^{-2}K^{3/2}\log^2(2K)\).
Together these prove the bound \(S_QK^{3/2}\log^2(2K)\) for the
sum in (12), including \(K=1\), when there are no dyadic blocks.
This proves (3)-(4), with no hidden dependence on \(X\) or \(K\).

### 5. Small X and the qualified energy interface

All preceding estimates hold for positive real \(\alpha,\beta\);
they never required \(X\ge2\) or \(\alpha\ge1\). Explicitly, if
\(1\le X<2\), admissibility forces \(K=1\), and the only source
index is \(n=1\). Hence
\[
 E_{\le1}(X)=X^{-1/2}(\log X)^2C_h(0),\quad
 M_1=\rho(1)C_h(0)\int_0^Q e^{-s/2}s^2ds.
\]
This is exactly (7)-(11) for \((a,b)=(1,1)\), including \(X=1\),
where the source is zero. At \(X=2\), the strict lower source
endpoint excludes \(n=1\); the upper term has logarithm zero.
Formula (10) still applies. Thus the extension is substantive and
contains no omitted small-scale endpoint.

For the specified integer cutoff, eventually \(1\le K(X)\le X\).
Writing \(L=\log X\), its remainder in (3) is at most
\[
 C_*C_h(0)e^{-3AL^{1/3}/2}(L+Q)^2=o(1).
\]
Here \(C_h(0)\) is fixed and finite. No assertion about an unapproved
varying input family is needed. The exact full square split gives
(6) immediately from (3) and the additional hypothesis (5).

For comparison with GC18, the source chooses the completed vector
\(V_X=\mathcal C_{1,X,M_*(X,\lceil X^3\rceil)}h\), using GC3-GC4:
\(\mathcal C=G-\mathcal B\), with the smallest minimizing integer
cap in \([\lceil X^3\rceil,2\lceil X^3\rceil)\), independently of
the input. Its separate GC6 claims (5) with
\(\epsilon_X\le C(e^{-c_\mu f_0(\log X)}+X^{-1})\|h\|_E^2\),
\(f_0(L)=L^{3/5}(\log L)^{-1/5}\), eventually. GC1-GC11,
lines11382-11600, specify that construction; its operator and Mertens
arguments are not audited by this proof. If that premise holds,
(6) yields GC18 for this fixed input and the cutoff just given.
The complete cross term in \(\|G-\mathcal B\|^2\) must remain;
replacing it by \(\|G\|^2\) would change (5).

The established error pays neither \(M_K\) nor \(E_{>K}\).
Both sectors are real, since reversing each pair conjugates its term,
but neither has been proved positive or subpolynomially bounded.
There is no projected-sector substitution, infinite limit interchange,
numerical zero evidence, RH assumption, or claimed cumulative-energy
conclusion. These qualifications preserve the main unresolved gap.

### Independent replay2092

The unchanged assessment2089 authorizes this independent replay of
(3)-(4), not an audit of GC6. The complete tagged GC12-GC18 statement
and proof, lines11613-11717, were inspected again; GC1-GC6,
lines11382-11454, were checked only for the conditional interface's
definitions, cap rule and quantifiers. The following checks supply
no stronger estimate or claim of novelty.

First, the linear-first-slot convention gives the correlation argument
\(r_k-r_n\), not its negative. Each square coefficient is
\(n^{-1/2}k^{-1/2}(nk/X^2)^{1/4}
=X^{-1/2}(nk)^{-1/4}\). Replacing \((n,k)\) by \((da,db)\)
therefore leaves \(d^{-1/2}\) inside and \((ab)^{-1/4}\)
outside. Equation (11) supplies the other \((ab)^{-1/4}\).
This independently recovers precisely (2), including its diagonal
\((a,b)=(1,1)\); no factor from pair symmetry is introduced.

For the arithmetic constant, finite inclusion-exclusion is exactly
\[
 \#\{\ell\le Z:(\ell,M)=1\}
 =\sum_{e\mid\operatorname{rad}(M)}\mu(e)\lfloor Z/e\rfloor.
\]
For \(Z\ge0\), replacing floors by their arguments costs at most
\(D(M)\). Thus the count error in (8), for \(Y\ge1\), is at most
\(D(M)\lfloor\sqrt Y\rfloor+Y/\lfloor\sqrt Y\rfloor\),
which is at most \((D(M)+2)\sqrt Y\le3D(M)\sqrt Y\).
The Euler factor at a prime dividing \(M\) is
\((1-p^{-1})/(1-p^{-2})=p/(p+1)\), verifying \(\rho(M)\)
for arbitrary \(M\), including \(M=1\). The separate \(Y<1\)
argument is necessary and valid; no estimate on a varying modulus
has been absorbed into the constant.

For a supported slot, (10) costs at most
\[
 3D(ab)\{Q^2+Q^2+(Q^2/2+2Q)\log(\beta/\alpha)\}
 \le B_QD(ab).
\]
The subtraction of the right-continuous \(A_M(\alpha)\) removes
an integer exactly at \(\alpha\), while \(A_M(\beta)\) includes
an integer at \(\beta\). At \(\beta\) one logarithm is zero.
At the strict lower endpoint it need not be zero, so that discrepancy
term cannot be silently deleted. This handles the jumps at \(X=2d\)
in the diagonal slot as well as empty integer intervals. If
\(N=2m\), both the interval and the defined weight vanish; there
is no reversed integral. If \(1\le X<2\), only the diagonal
slot and \(K=1\) are possible, and the formulas in section 5 follow
directly; they include the zero source at \(X=1\).

For a dyadic block, both \(N>A\) and \(m>A/2\) are used:
\(ab=Nm>A^2/2\). Hence the factor \(2^{1/4}A^{-1/2}\)
in (12)'s block estimate is valid. Enlarging to all pairs at most
\(2A\) gives exactly the stated factor \(4\,2^{1/4}\).
The blocks \(A=2^j<K\), together with the singleton, exhaust
all pairs even when \(K\) is a power of two. The geometric bound
and the inequality
\(1+\log(2A)\le(1+Q^{-1})\log(2K)\) therefore give (4)
without a \(K\)-dependent constant. For \(K=1\), the singleton
bound is an equality in its scalar majorant. There is no additional
restriction near \(K=X\).

All replayed inequalities pass on the full claimed range. The fixed
cutoff's exponential decay dominates its displayed logarithmic factor.
Finally, (6) is only the triangle inequality with (5); the primary
source's GC18 explicitly invokes GC6 as well as GC13. This replay
does not certify GC5/GC6, its cap estimates or vector Abel argument,
nor either signed upper or a cumulative-energy conclusion. The sole
notation repair above replaces a comma by the intended indicator;
no mathematical statement or dependency changes.

## Mathlib

Full matching coverage for this weighted primitive-sector decomposition
and its uniform remainder has not been checked; availability is unknown.
Supporting inputs are elementary Möbius square-divisor expansion,
coprime inclusion-exclusion, Cauchy-Schwarz and summation by parts.
No Mathlib theorem or numerical certificate is used as an unchecked
substitute for the endpoint and uniformity proof above.
