# C744a: Support-sensitive prime-delay payment in the fixed-family energy floor

## Hypotheses

Fix an integer \(K\ge2\), \(\ell=\log(3)/2\), \(L=K\ell\), and
the original complex Hilbert space \(X=L^2((0,L),dx)\), with inner
product linear in its first argument. All functions are extended by zero.
Use L743's complete Hermitian arithmetic operator

\[
 T_a u(x)=\mathbf1_{x>a}u(x-a),\qquad
 B_L=\sum_{2\le n<e^L}\frac{\Lambda(n)}{\sqrt n}
                       (T_{\log n}+T_{\log n}^*),\qquad
 C_{\rm prime}=2\sum_{2\le n<e^L}\frac{\Lambda(n)}{\sqrt n}.
 \tag{1}
\]

Here \(\Lambda(p^r)=\log p\) for every prime power \(p^r\), and is
zero otherwise. The sum is finite; a delay equal to \(L\) is zero.

For the complete-energy conclusion, use exactly L744's nonempty family
\(\mathcal F_{K,M}\), with fixed finite \(M\): its members are
\(w=\sum_{j=0}^{K-1}w_j(x-j\ell)\),
\(w_j\in C_c^\infty(0,\ell;\mathbb C)\),
\(\|w\|_2=1\), \(\|w\|_{H^2(\mathbb R)}\le M\), where
\(\|f\|_{H^2}^2=\|f\|_2^2+\|f'\|_2^2+\|f''\|_2^2\).
Fix the same real nonnegative \(\chi\in C_c^\infty(0,\ell)\), positive
on an open interval. For \(\sigma,\tau\in\{+1,-1\}\), define

\[
\begin{split}
 b_\tau(s)&=\chi(s)e^{\tau s/2},&
 G_{\sigma\tau}&=\int_0^\ell\chi(s)e^{(\sigma+\tau)s/2}\,ds,\\
 d_{j,\sigma}(t,w)&=e^{itj\ell}\int_0^\ell
                       e^{\sigma s/2}w_j(s)e^{its}\,ds,&
 h_{t,w}(x)&=\sum_{j,\tau}(G^{-1}d_j(t,w))_\tau b_\tau(x-j\ell),\\
 v_{t,w}(x)&=e^{itx}w(x)-h_{t,w}(x).
\end{split} \tag{2}
\]

Invertibility of \(G\) and this exact complex-linear correction are
established in L743 and used in L744. Let \(E_L\) be L744's complete
generator energy, including its continuous kernel and both rational
completion terms. Use its unchanged \(t_0\) and error
\(\epsilon_{K,M,\chi}\) from L744 (17), made explicit below.
No positivity conclusion or RH-conditional spectral input is assumed.

Import U. Haagerup and P. de la Harpe, *The numerical radius of a
nilpotent operator on a Hilbert space*, Proc. Amer. Math. Soc.
115(2) (1992), 371–379, **Theorem 1(1), p.372**, inequality proof p.376,
[DOI](https://doi.org/10.1090/S0002-9939-1992-1072339-6),
[published UNIGE copy](https://access.archive-ouverte.unige.ch/access/metadata/2e3d55fc-f7d2-42af-95ae-6c06df864dbb/download).
For a bounded operator \(T\) on a complex Hilbert space, \(T^q=0\)
and integer \(q\ge2\) imply
\(w(T)\le\|T\|\cos(\pi/(q+1))\), where
\(w(T)=\sup_{\|u\|=1}|\langle Tu,u\rangle|\).
This inequality allows an infinite-dimensional space and does not
require an attaining vector. Import it without reproof; its separate
equality-structure assertion is not used. Source coverage is reused
from the completed step450 assessment.

## Conclusion

For \(2\le n<e^L\), put \(q_n=\lceil L/\log n\rceil\), and define

\[
 C_{\rm nr}(L)=2\sum_{2\le n<e^L}\frac{\Lambda(n)}{\sqrt n}
             \cos\!\left(\frac{\pi}{q_n+1}\right).
 \tag{3}
\]

Then, for every \(u\in X\),

\[
 |\langle B_Lu,u\rangle|\le C_{\rm nr}(L)\|u\|_2^2,
 \qquad 0<C_{\rm nr}(L)<C_{\rm prime}. \tag{4}
\]

The saving is the explicit positive finite sum

\[
\begin{split}
 \Delta_L&=C_{\rm prime}-C_{\rm nr}(L)\\
 &=2\sum_{2\le n<e^L}\frac{\Lambda(n)}{\sqrt n}
       \left[1-\cos\!\left(\frac{\pi}{q_n+1}\right)\right]\\
 &\ge\sqrt2\log2\left[1-
       \cos\!\left(\frac{\pi}{\lceil L/\log2\rceil+1}\right)\right]>0.
\end{split} \tag{5}
\]

For every \(w\in\mathcal F_{K,M}\) and real \(|t|\ge t_0\), the same
nonzero corrected test (2) satisfies the improved complete-energy floor

\[
 \boxed{\quad
 \frac{E_L(v_{t,w})}{\|v_{t,w}\|_2^2}
 \ge\log\frac{|t|}{2\pi}-C_{\rm nr}(L)
                         -\epsilon_{K,M,\chi}(t).
 \quad} \tag{6}
\]

Thus the sufficient scalar condition is now
\(\log(|t|/(2\pi))>C_{\rm nr}(L)+\epsilon_{K,M,\chi}(t)\), with a
right side smaller by \(\Delta_L\) than L744's literal condition.
This is a REPRODUCTION/known-theorem specialization, not a new theorem
beyond the sources checked, an effective onset or a claim that a
particular newly admitted carrier has been evaluated. No joint
sharpness, bounded-frequency sign, unrestricted-envelope estimate,
growing-support uniformity, moment-complement positivity or RH follows.

## Proof

### 1. Exact interval powers, including the endpoints

For \(0<a<L\) and every integer \(j\ge1\), zero extension and induction
give, almost everywhere on \((0,L)\),

\[
 T_a^j u(x)=\mathbf1_{x>ja}u(x-ja). \tag{7}
\]

For the induction step, the two restrictions are \(x>a\) and
\(x-a>ja\), equivalent together to \(x>(j+1)a\). Equalities at
endpoints are null sets in \(L^2\). In particular, if \(ja\ge L\),
the operator in (7) is zero. If \(ja<L\), choose a nonzero \(u\)
supported in \((0,L-ja)\); then
\(\|T_a^ju\|_2^2=\int_0^{L-ja}|u(y)|^2dy=\|u\|_2^2\).
It is therefore nonzero. Also this integral formula for \(j=1\)
shows \(\|T_a\|=1\).

Consequently its exact nilpotency index is \(q=\lceil L/a\rceil\ge2\).
If \(L/a=r\) is an integer, \(q=r\), \(qa=L\), and
\((q-1)a<L\); the \(q\)-th power is already zero, not just the next
one. If \(r<L/a<r+1\), \(q=r+1\), \(qa>L\), and
\((q-1)a<L\). These exhaust the cases. For \(a=L\), \(T_a=0\)
already at the first power; the \(q\ge2\) theorem is unnecessary.
For \(a>L\) the same zero-operator observation holds. In particular
the \(q=2\) case includes both \(a=L/2\) and \(L/2<a<L\).

### 2. Imported numerical radius and the complete finite sum

Apply the cited theorem to \(T_{\log n}\) on the original complex
\(X\). Each retained delay has \(0<\log n<L\), norm one, and
annihilating power \(q_n\ge2\) by (7). Scaling a vector gives

\[
 |\langle T_{\log n}u,u\rangle|
 \le\cos\!\left(\frac{\pi}{q_n+1}\right)\|u\|_2^2. \tag{8}
\]

With the first-slot-linear convention,
\(\langle T_a^*u,u\rangle=\overline{\langle T_au,u\rangle}\).
Thus the quadratic form of \(T_a+T_a^*\) is exactly twice the real
part, bounded in absolute value by twice (8). All coefficients in
(1) are nonnegative. The finite triangle inequality gives (4)'s form
bound with exactly (3), without any interchange of limits, finite-rank
compression, moment restriction, modulation or common extremizer.
Every prime power is retained. Terms with \(\Lambda(n)=0\) contribute
zero; an integer with \(\log n=L\), if present, has zero delay
operator and is excluded from both constants in (1)/(3).

Since every \(q_n\) is finite and at least two,
\(0<\cos(\pi/(q_n+1))<1\). The integer \(n=2\) occurs for every
\(K\ge2\), since \(e^L\ge3>2\), and its coefficient is
\(\log2/\sqrt2>0\). This proves strict positivity of (3), strict
saving, and the lower bound (5), by retaining that summand alone.

As an exact small-window check within this scope, when \(K=2\),
\(L=\log3\), only \(n=2\) contributes. Since \(2<3<4\),
\(q_2=2\) and \(\cos(\pi/3)=1/2\). Hence
\(C_{\rm nr}(\log3)=\log2/\sqrt2\),
\(C_{\rm prime}=\sqrt2\log2\), and
\(\Delta_{\log3}=\log2/\sqrt2\). The boundary \(n=3\) contributes
nothing. This check asserts no simultaneous sharpness for larger sums.

### 3. Substitution into the unchanged complete energy

Use the Fourier convention \(F_f(\xi)=\int f(x)e^{-i\xi x}dx\)
and \(d\xi/(2\pi)\). The established L744 (6), for every smooth
compactly supported test in this fixed window, is

\[
 E_L(f)=Q_m(f)+2\Re(F_f(i/2)\overline{F_f(-i/2)})
                    -\langle B_Lf,f\rangle,
 \quad
 Q_m(f)=\int[\Re\psi(1/4+i\xi/2)-\log\pi]|F_f(\xi)|^2
                                                \frac{d\xi}{2\pi}.
 \tag{9}
\]

The tests (2) are smooth with compact support in their cell interiors.
Their two local moments vanish exactly, since \(G G^{-1}d_j=d_j\).
Multiplication of each local moment by \(e^{\sigma j\ell/2}\) and
summation give \(F_v(\sigma i/2)=0\) for both signs. Thus (9)'s
pole product vanishes exactly for these complex tests; none of its
terms is dropped by an asymptotic estimate.

For precision, the inherited constants and error of L744 (10)-(17) are
as follows, with \(T=|t|\):

\[
\begin{split}
 A&=2+8\sqrt2/3+\log(4\pi),\qquad c_T=\log(T/(2\pi)),\\
 R_\chi&=\|G^{-1}\|(\|b_+\|_{H^2}^2+\|b_-\|_{H^2}^2)^{1/2},\\
 H&=R_\chi\sqrt{33\ell e^\ell/8}\,M,\qquad \delta(T)=H/T^2,\\
 U(T)&=A+\log(2+T)+3+M^2,\\
 a(T)&=2M/T+(8+4M^2)/T^2\\
 &\hspace{8mm}+16M^2T^{-4}[A+\log3+3+\log(2\pi)+\log T],\\
 b(T)&=2\sqrt{U(T)(A+3)}\,\delta(T)+(A+3)\delta(T)^2,\\
 t_0&=\max\{2,\sqrt{2H}\},\\
 \epsilon_{K,M,\chi}(t)
 &=\frac{a(T)+b(T)+|c_T|(2\delta(T)+\delta(T)^2)}
             {(1-\delta(T))^2}\quad(T\ge t_0).
\end{split} \tag{10}
\]

As in L744, define the error to be zero below \(t_0\), where no
inequality is claimed. These constants depend only on the fixed
family and correction. For \(T\ge t_0\), L744 (13), (15)-(16) give
\(N=\|v_{t,w}\|_2^2\ge(1-\delta(T))^2\ge1/4\) and

\[
 \left|Q_m(v_{t,w})/N-c_T\right|
       \le\epsilon_{K,M,\chi}(t)=O_{K,M,\chi}(T^{-1}). \tag{11}
\]

These are prior proved estimates for the complete digamma multiplier,
the exact correction and its denominator, not consequences of L744's
weaker final energy inequality. In particular (11) does not use its
old arithmetic payment. Substituting the upper form bound (4) into
(9) after exact pole cancellation gives
\(E_L(v)/N\ge Q_m(v)/N-C_{\rm nr}(L)\), and (11) proves (6).
The inherited estimates use \(|t|\), so both signs of the carrier
and all members of the fixed family are covered with unchanged error.

The certified lower-bound expression improves by exactly \(\Delta_L\).
For any fixed error allowance \(\eta>0\), at carriers already satisfying
\(T\ge t_0\) and \(\epsilon(t)\le\eta\), the sufficient logarithmic
condition is \(T>2\pi e^{C_{\rm nr}(L)+\eta}\) rather than
\(T>2\pi e^{C_{\rm prime}+\eta}\). Their scalar thresholds have ratio
\(e^{-\Delta_L}<1\). This comparison does not compute the first
positive carrier or remove the two prior restrictions on \(T\).

The continuation test is met: a strict scalar saving and its exact
floor substitution hold. It does not improve L743's neutral/unrestricted
supremum comparison, which supplies no value for that supremum. It
reopens neither L746's half allocation nor L750's localization defect.
Actual-Xi positivity, joint bounded-frequency estimates, unrestricted
profiles, growing support and moment complements remain independent
gaps. No complete RH candidate is asserted.

### Separate proof audit (11 November 2026, step453)

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-11-c744a-support-sensitive-payment-audit-451.md`
was separately approved in step452. This audit accepts (4)-(6) in
their stated fixed-family scope without changing the proof or its
hypotheses. It verifies a known-theorem specialization, not a new
sign theorem beyond the sources checked. Haagerup-de la Harpe,
Theorem 1(1), p.372 and its inequality proof p.376, are imported
using the completed step450 source inspection; no new source-proof
replay or equality-structure claim is made.

1. **Exact operator and interval endpoints.** The operator is L743's
   original zero-extended translation on complex L2(0,L), not a
   compression to a chosen trial space. For j>=1 its squared norm
   on a vector is the integral of |u|^2 over (0,L-ja) when ja<L,
   and is zero when ja>=L. Thus the first vanishing power is
   q=ceil(L/a): at L/a=r integral, power r already vanishes and
   power r-1 does not; between r and r+1 the first vanishing
   power is r+1. This also verifies norm one for 0<a<L. In
   particular a=L/2 has q=2; a=L is already zero and is excluded
   from both sums rather than submitted to the q>=2 theorem.
   Null endpoints introduce no exceptional vector in L2.

2. **Complex form, complete arithmetic sum and strictness.** Under
   the first-slot-linear convention the adjoint quadratic value is
   the conjugate, so each Hermitian term is twice a real part.
   Applying the imported absolute numerical-radius bound therefore
   gives exactly the factor two in (3), with nonnegative coefficients
   Lambda(p^r)/sqrt(p^r) for every retained prime power, including
   r>1. Coefficient-zero integers cause no omission. Finite triangle
   inequality proves the absolute bound for the sum; it asserts no
   simultaneous extremizer or exact joint operator norm. Every
   retained q is finite and >=2, so its cosine is in [1/2,1).
   Since L>=log3>log2, n=2 has positive coefficient. Its contribution
   to the saving is exactly the right-hand lower bound in (5),
   proving both strict inequalities in (4). At K=2 the only retained
   integer is 2; 1<L/log2<2 gives q_2=2 and the stated exact half
   payment. The boundary integer 3 contributes zero.

3. **Identical correction and exact poles.** The definitions in (2)
   match L744 (1)-(3), including fixed K,M,chi, unit profile norm,
   full H2 bound and the unmodulated correction basis. On cell j,
   the two moments of e^(itx)w are d_(j,sigma); the complex-linear
   matrix equation G(G^-1 d_j)=d_j cancels them exactly. No
   conjugation of d_j belongs in that equation. Multiplying the
   local zero moments by e^(sigma j ell/2) gives both global
   F_v(sigma i/2)=0. The complete energy (9) is precisely L744 (6),
   with the same digamma symbol, minus the Hermitian arithmetic
   form and plus twice the real complex pole product. Both poles
   thus cancel before estimating, and the corrected test remains
   smooth with compact support in the cell interiors.

4. **Substitution before the old payment.** All constants in (10)
   agree term for term with L744 (10)-(17), including U, H, the
   two correction terms in b, and |c_T|(2 delta+delta^2). L744 (13)
   and (15) imply delta<=1/2 and N>=1/4 at the identical t0.
   Its (16) is an absolute estimate for Q_m(v)/N-c_T proved before
   any use of C_prime. Hence division is valid, v is nonzero, and
   E_L(v)/N=Q_m(v)/N-<B_L v,v>/N >= c_T-epsilon-C_nr(L).
   This proves (6) without trying to strengthen an already weaker
   final inequality. The error, denominator and both signs of t
   are unchanged; constants may depend on the fixed family. No
   high-frequency projection, growing window or unrestricted H2
   bound is inferred.

5. **Meaning of the threshold saving.** The two certified lower
   expressions differ by exactly Delta_L>0 for each common admitted
   carrier and profile. The ratio exp(-Delta_L) compares the stated
   scalar thresholds only after the common restrictions T>=t0 and
   epsilon(t)<=eta are imposed. It does not certify an actually
   newly admitted carrier or an effective first onset. Neutrality
   alone still cannot lower the prime-only supremum relative to
   the unrestricted one (L743); the bound here applies to both.
   L746's allocation counterexample and L750's localization defect
   remain unaffected. The bounded-frequency joint signed deficit,
   general profiles and moment complements remain open.

No defect requiring a mathematical repair was found. Direct inputs
remain L743 and L744; the latter carries the inherited L740/L741
normalization. There is no use of L742's conditional spectral
conclusion, of RH, or of another notebook. Full matching Mathlib
coverage remains unchecked. This audit changes no proof assembly or
dependency, and does not constitute a complete RH candidate.

## Mathlib

Full matching coverage of the nilpotent numerical-radius theorem,
the aggregate (3), and the complete-energy specialization has not
been checked. No absence or formal-verification claim is made.
The external theorem is imported by precise citation; the interval
powers, endpoint cases, complex quadratic forms, finite aggregation
and strict-saving comparison are justified here. The analytic
complete-energy and correction estimates are those proved in L744.
