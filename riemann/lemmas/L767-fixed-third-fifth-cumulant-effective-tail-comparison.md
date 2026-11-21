# Lemma 767: an effective tail for the fixed third/fifth cumulant comparison

## Hypotheses

Let K be the exact positive theta kernel of L019, and let B be its
complete n=1 summand:

\[
 B(u)=4\pi e^{5u/2}(2\pi e^{2u}-3)e^{-\pi e^{2u}},\qquad u\ge0.
\]

For F=B or K and integers m>=1 define

\[
 C_m(F;u)=\frac1{(m-1)!}\int_u^\infty(v-u)^{m-1}F(v)\,dv,
 \quad S(F;u)=-\det[\partial_u^{i+j}C_5(F;u)]_{i,j=0}^2.
\]

Write x=pi exp(2u), A=4x(2x-3)exp(u/2-x), and X=131072.
All inequalities below concern real u with x>=X.

## Conclusion

One has

\[
 S(B;u)>\frac{119}{100}\frac{A^3}{(2x)^9x^3}>0,
 \qquad
 \frac{|S(K;u)-S(B;u)|}{S(B;u)}
 <\frac3{10^{27}}<\frac12.
\]

In particular S(K;u)>S(B;u)/2 on this stated tail. Also the normalized
base determinant is 2x^(-3)+O(x^(-4)) as x tends to infinity.
This does **not** prove the fixed comparison on pi<=x<X, including
u=0. It proves no higher-order sign, effective all-order smoothing
threshold, exceptional coefficient transfer, or RH assertion.

This is a local quantitative development of the full-first-summand
comparison already proposed by John Nuttall, *Wronskians and the
Riemann Hypothesis* (August 2012), Sections 3.1–4.1, printed pp.2–5,
[author report](https://publish.uwo.ca/~jnuttall/wronskRH.pdf).
No sign conjecture or numerical table in that source is assumed.
The inspected source does not supply this certified fixed-order
relative tail estimate; that quantitative difference justifies the
calculation. No originality beyond the inspected sources is claimed.

## Proof

### 1. Exact normalization and differentiation

L019's exponential decay dominates every polynomial weight used here.
Differentiating a tail with m>=2 gives C_m'=-C_(m-1); its moving
boundary term vanishes. Dominated differentiation, locally in u,
therefore justifies all four displayed derivatives of C_5.
Removing the derivative signs by row/column sign changes and then
reversing both rows and columns leaves the determinant unchanged.
It becomes det[C_(1+i+j)] for i,j=0,1,2.

For p=0,...,4 let d_p=(2x)^(p+1)C_(p+1)(B;u)/A. Substituting
q=x(exp(2(v-u))-1), with epsilon=1/x, gives exactly

\[
 d_p=\frac1{p!}\int_0^\infty e^{-q}L(\epsilon,q)^p
             H(\epsilon,q)\,dq,
\]
\[
 L=\frac{\log(1+\epsilon q)}\epsilon
   =\int_0^q\frac{ds}{1+\epsilon s},\qquad
 H=(1+\epsilon q)^{1/4}
       \left(1+\frac{\epsilon q}{1-3\epsilon/2}\right).
\]

L(0,q)=q. Define s(d)=-det[d_(i+j)]_(i,j=0)^2. Factoring the
row and column powers of 2x yields

\[
 S(B;u)=\frac{A^3}{(2x)^9}s(d).
 \tag{1}
\]

### 2. Uniform entry expansions with explicit remainders

For 0<=epsilon<=1/4, direct multiplication to second order gives

\[
 d_p=1+a_p\epsilon+b_p\epsilon^2+r_p,\quad
 a_p=(p+1)(5/4-p/2),
\]
\[
 b_p=\frac{(p+1)(p+2)(12p^2-40p+15)}{96}
                      +\frac32(p+1),\qquad
 |r_p|\le R_p\epsilon^3.
 \tag{2}
\]

Here is a complete uniform Taylor-remainder bound. Put
U=(1+epsilon q)^(1/4), V=1+epsilon q/(1-3epsilon/2).
For k=0,1,2,3 the following polynomials majorize
|partial_epsilon^k U|/k! and |partial_epsilon^k V|/k!, respectively:

| k | U majorant | V majorant |
|---|---|---|
| 0 | 1+q/16 | 1+2q/5 |
| 1 | q/4 | 64q/25 |
| 2 | 3q^2/32 | 768q/125 |
| 3 | 7q^3/128 | 9216q/625 |

For U these follow from its first three derivatives and concavity;
for V they follow by differentiating epsilon/(1-3epsilon/2) and
using 1-3epsilon/2>=5/8. Furthermore

\[
 \frac{|\partial_\epsilon^k L|}{k!}
 =\int_0^q\frac{s^k}{(1+\epsilon s)^{k+1}}\,ds
 \le\frac{q^{k+1}}{k+1}\le q^{k+1}.
\]

Thus for p>=1 the kth normalized derivative of L^p is bounded by
binom(p+k-1,k)q^(p+k), by the product rule and the number of weak
compositions of k into p parts. For p=0 use 1 at k=0 and 0 otherwise.
Let U_i(q),V_j(q),T_(p,k)(q) denote these three majorants. A bound
for the third normalized derivative of H L^p is

\[
 P_p(q)=\sum_{i+j+k=3}U_i(q)V_j(q)T_{p,k}(q).
\]

All coefficients are nonnegative. Taylor's theorem with its integral
remainder, followed by integration against e^(-q)/p!, proves (2)
with R_p=(1/p!) integral e^(-q)P_p(q)dq. All differentiations and
integrations are justified by these integrable polynomial majorants;
there is no assumption that epsilon q is uniformly small. Using
integral_0^infinity e^(-q)q^j dq=j! gives:

| p | a_p | b_p | R_p |
|---|---|---|---|
| 0 | 5/4 | 29/16 | 878157/40000 |
| 1 | 3/2 | 35/16 | 3182643/10000 |
| 2 | 3/4 | 19/8 | 9409881/4000 |
| 3 | -1 | 53/8 | 111260019/10000 |
| 4 | -15/4 | 355/16 | 317946243/8000 |

### 3. Cancellation retained in the signed determinant

Set delta_k=sum_(j=0)^k (-1)^(k-j)binom(k,j)d_j. Applying the
lower-triangular row matrix with rows (1,0,0), (-1,1,0), (1,-2,1)
and its transpose gives [delta_(i+j)] without changing the determinant.
The finite differences of a and b, at index zero, are

\[
 (\Delta^ka_0)_{k=0}^4=(5/4,1/4,-1,0,0),\qquad
 (\Delta^kb_0)_{k=0}^4=(29/16,3/8,-3/16,17/4,3).
\]

Let R'_k=sum_(j=0)^k binom(k,j)R_j. Their exact values are

\[
 (R'_k)_{k=0}^4=
 (878157/40000,13608729/40000,120438111/40000,
 766406379/40000,498285603/5000).
\]

For epsilon>0 define v0=delta_0, v1=delta_1/epsilon,
v2=delta_2/epsilon, v3=delta_3/epsilon^2, v4=delta_4/epsilon^2.
Equation (2) gives their respective enclosures

\[
\begin{aligned}
 v_0&=1+5\epsilon/4+29\epsilon^2/16+[-R'_0,R'_0]\epsilon^3,\\
 v_1&=1/4+3\epsilon/8+[-R'_1,R'_1]\epsilon^2,\\
 v_2&=-1-3\epsilon/16+[-R'_2,R'_2]\epsilon^2,\\
 v_3&=17/4+[-R'_3,R'_3]\epsilon,\\
 v_4&=3+[-R'_4,R'_4]\epsilon.
\end{aligned}
\tag{3}
\]

For 0<epsilon<=1/131072 these imply the following rational bounds:

\[
\begin{split}
 &999/1000\le v_0\le1001/1000,\quad
 249/1000\le v_1\le251/1000,\\
 &-1001/1000\le v_2\le-999/1000,\quad
 4\le v_3\le9/2,\quad 11/5\le v_4\le19/5.
\end{split}
\tag{4}
\]

Expanding the signed three-by-three determinant now gives the exact identity

\[
 \frac{s(d)}{\epsilon^3}
 =-v_0v_2v_4+v_2^3+
 \epsilon(v_0v_3^2+v_1^2v_4-2v_1v_2v_3).
 \tag{5}
\]

Every epsilon-weighted term on the right is nonnegative by (4).
Consequently

\[
 \frac{s(d)}{\epsilon^3}
 \ge (999/1000)^2(11/5)-(1001/1000)^3
 =\frac{1192599199}{10^9}>119/100>1.
 \tag{6}
\]

Equations (1) and (6) prove the claimed signed base lower bound.
Also (3) gives v0=1+O(epsilon), v2=-1+O(epsilon), v4=3+O(epsilon),
with v1,v3 bounded, so (5) yields s(d)=2epsilon^3+O(epsilon^4).
In particular the leading constant is justified analytically, not fitted.

### 4. The entire theta tail, including every n>=2

Let t_p=(2x)^(p+1)C_(p+1)(K;u)/A. For the nth theta summand use
q=n^2x(exp(2(v-u))-1). Its contribution to t_p is exactly

\[
 \frac{e^{-(n^2-1)x}}{p!}\int_0^\infty e^{-q}
 [x\log(1+q/(n^2x))]^p(1+q/(n^2x))^{1/4}
 \frac{2n^2x+2q-3}{2x-3}\,dq.
 \tag{7}
\]

All summands are nonnegative; Tonelli justifies their interchange
with the integral. For x>=4 and n>=1,

\[
 x\log(1+q/(n^2x))\le q/n^2,\quad
 (1+q/(n^2x))^{1/4}\le1+q/16,
\]
\[
 0<\frac{2n^2x+2q-3}{2x-3}
 \le\frac85n^2(1+q/4).
\]

Replacing the product of the last two polynomial factors by (1+q)^2
bounds (7) above by

\[
 \frac85 n^{2-2p}(p^2+5p+5)e^{-(n^2-1)x}
 \le66n^2 e^{-(n^2-1)x},\qquad 0\le p\le4.
\]

For n>=3, n^2-4>=n and n^2<=4^(n-1). Since exp(4)>16,

\[
 \sum_{n\ge2}n^2e^{-(n^2-1)x}
 \le e^{-3x}\left(4+\sum_{n\ge3}n^2e^{-4(n^2-4)}\right)
 < e^{-3x}(4+1/192)<5e^{-3x}.
\]

Hence 0<=t_p-d_p<=330e^(-3x). The n=1 bound also gives d_p<=66;
330e^(-12)<1 implies t_p<67 for x>=4.

### 5. Signed relative error and threshold

The signed polynomial is

\[
 s(d)=d_0d_3^2+d_2^3+d_4d_1^2-d_0d_2d_4-2d_1d_2d_3.
\]

A difference of any product of three entries in [0,67], when the
maximum entry difference is eta, is bounded by 3*67^2 eta, by
telescoping the product. The sum of the absolute displayed
coefficients is 6. This proves, with no sign cancellation assumed,

\[
 |s(t)-s(d)|\le18\cdot67^2\cdot330 e^{-3x}
                =26664660e^{-3x}.
\]

The base cancellation was already paid by (6), not replaced by a
norm. Using its weaker lower bound s(d)>x^(-3), and
exp(3x)>=(3x)^10/10!, gives for every x>=X

\[
 \frac{|s(t)-s(d)|}{s(d)}
 \le26664660x^3e^{-3x}
 \le\frac{26664660\cdot10!}{3^{10}X^7}
 =\frac{43206625}{17524001897555043246290425111117824}
 <\frac3{10^{27}}<\frac12.
\]

The same positive factor in (1) applies to K, so this is the required
physical determinant comparison on the stated tail.

### Verification and limitations

Run `python3 scripts/cumulant-comparison/tail-certificate-394.py`.
It constructs the polynomial derivative majorants above using exact
fractions, integrates each monomial exactly, checks the finite
differences, verifies (3) implies (4), and checks (6) and the relative
threshold. Full evidence is in
`scripts/cumulant-comparison/tail-certificate-394.json`.
Earlier dyadic cutoff enclosures failed the lower-bound test; these
are failures of that estimate, not negative determinant values.
The script certifies rational arithmetic, while the analytic
justifications are the written proof above. No numerical integration
or finite theta truncation is used in the proof.

The separate `scripts/cumulant-comparison/diagnostic-394.py` and its
JSON output use uncertified floating-point quadrature and a finite
theta sum. They are exploratory only, including their value at u=0.
The remaining compact domain has no certificate in this lemma; L768
supplies that separate comparison. The later step397 audit below
accepts the present lemma on its stated tail.

### Independent audit — 2026-11-04, step397

The fixed-order statement and all analytic bounds above pass this
later-turn audit. In particular, the normalization uses
dv=dq/(2(x+q)); the factor (1+q/x) from B(v)/B(u) cancels this
Jacobian, leaving precisely H and the factorial p!. Removing
(-1)^(i+j), then reversing both rows and columns, multiplies the
determinant by 1 in each case. Factoring (2x)^(-i) from row i and
(2x)^(-j-1) from column j gives exponent 9 in (1). The triangular
finite-difference matrix has determinant 1 and gives delta_(i+j).
Expanding that three-by-three determinant gives (5), with its displayed
minus sign; no absolute-value determinant has replaced it.

The normalized derivatives of U and V in the table are bounded on
the full interval [0,1/4]. The integral representation of L bounds
every normalized derivative even when epsilon q is large. Multiplying
these nonnegative polynomial majorants gives an integrable dominant
function, including epsilon=0. Taylor expansion under the integral
therefore has the asserted uniform remainder. All coefficient values,
finite differences, enclosures and thresholds were replayed exactly.
An independent bivariate epsilon/q polynomial multiplication also
reproduced the five a_p, five b_p and five R_p, without calling the
original coefficient or majorant routines. The constant coefficients
are 1. The limits v0->1, v2->-1, v4->3 and bounded v1,v3 then give
the stated leading constant 2 in s(d)/epsilon^3.

For the nth summand the analogous substitution uses
dv=dq/(2(n^2x+q)); direct cancellation leaves exactly (7), with no
missing power of n. Its integrand is nonnegative. The three displayed
factor bounds and the exponential decay justify Tonelli and the full
n>=2 estimate. In the geometric tail, n^2-4>=n for n>=3 and
exp(4)>16 give the stated 1/192 bound; the n=2 term is retained.
The sum of absolute coefficients in s is 6, so telescoping cubic
products on [0,67]^5 gives precisely 18*67^2*330. The rational lower
and relative bounds are strict against 119/100 and 3/10^27.

Reproduce with `python3 scripts/cumulant-comparison/audit-397.py`.
The independent arithmetic evidence is in
`scripts/cumulant-comparison/audit-397.json`; the complete original
rational certificate is replayed, without overwriting it, into
`scripts/cumulant-comparison/tail-replay-397.json`. Source/certificate
hashes confirm preservation. The earlier failed cutoff enclosures
remain recorded and are not negative determinant values. This audit
establishes a checked local input in the known comparison program,
not new all-order mathematics or a resolution of RH.

## Mathlib

Not checked. Availability of a full matching theorem or supporting
formal statements is unknown; the elementary Taylor, product-rule,
Tonelli, and rational-arithmetic steps above are an informal proof.
