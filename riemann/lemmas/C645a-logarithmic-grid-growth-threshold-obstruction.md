# Corollary 645a: the sufficient logarithmic-grid threshold eventually fails

## Hypotheses

Fix \(\delta\in(0,1/2)\), put \(\beta=1/2+\delta\), and use the
completion of L018 and every definition of L645, without alteration.
In particular, condition on a **simple** zero
\(\rho=\beta+i\gamma\) with \(\gamma\ge e^5\), and retain its
\(s_*,a,d,R,M_\rho,H_\rho,A_\delta,q_\delta,\lambda_\delta,n_0\).
There is no assumption that such zeros exist at any height, that the
actual matrices are PSD, or that \(\zeta'(\rho)\) has a lower bound.
All logarithms are natural.

## Conclusion

For every fixed \(\epsilon>0\), there are constants
\(c_{\delta,\epsilon}>0\) and \(T_{\delta,\epsilon}\ge e^5\), independent
of the stipulated zero, such that at every such zero above that height,

\[
 H_\rho\ge c_{\delta,\epsilon}\gamma^{1/2-\epsilon}.
 \tag{1}
\]

Moreover,

\[
 0<\lambda_\delta<\log(5/4)<1/4.
 \tag{2}
\]

Consequently there exists \(T_\delta\ge e^5\) such that every stipulated
simple zero with \(\gamma\ge T_\delta\) satisfies, for
\(N=\lfloor\log\gamma\rfloor\),

\[
 H_\rho>A_\delta^{-1}\exp(\lambda_\delta N).
 \tag{3}
\]

Thus the strict sufficient inequality (7) of L645 fails, and its stated
\(n_0\) is greater than \(N\). This obstructs this particular
sufficient threshold at logarithmic grid size. It neither asserts PSD
of \(K_N(\gamma)\) nor excludes a smaller negative witness, and does not
refute L645's detector for all \(n\ge n_0\). No effective numerical onset,
small-displacement uniformity, multiple-zero extension or RH conclusion
is asserted. This is a specialization of classical estimates, not a
claim of a new growth theorem beyond the sources checked. A separate
critical audit accepted this corollary on 1 November 2026, as recorded below.

## Proof

### Imported standard estimates

The prior source assessment inspected the following primary inputs.
Only their applicability and the present ratio comparison are proved here;
there is no reproof of convexity or Stirling's formula.

1. S. M. Gonek, *Mean values of the Riemann zeta-function and its
   derivatives*, Inventiones Mathematicae **75** (1984), 123–141,
   Section 2, equation (20), printed p.127, and the complete following
   Cauchy-estimate paragraph
   ([published PDF hosted by the author](https://sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf)).
   Its unconditional critical-strip case gives, for fixed derivative
   order \(\nu\ge0\) and fixed \(\epsilon>0\),
   \[
   |\zeta^{(\nu)}(\sigma+it)|
        \ll_{\nu,\epsilon}|t|^{(1-\sigma)/2+\epsilon},
   \quad 0\le\sigma\le1,\quad |t|\ge1/2.
   \]
   We use only \(\nu=1\) and the fixed \(\sigma=\beta\in(1/2,1)\),
   allowing constants to depend on \(\delta,\epsilon\).
   The nearby selected-height logarithmic-derivative estimates are not
   used; neither RH nor a selected-height hypothesis enters (20).
2. NIST DLMF, version 1.2.8, release 15 September 2026,
   [5.11.9](https://dlmf.nist.gov/5.11.E9), with its bounded-real-part
   uniformity, gives
   \[
   |\Gamma(x+iy)|\sim\sqrt{2\pi}|y|^{x-1/2}e^{-\pi|y|/2}
   \]
   as \(y\to\pm\infty\), uniformly for bounded real \(x\).
   The inspected sector and complex-remainder qualifications are in
   [5.11(i)–(ii)](https://dlmf.nist.gov/5.11).
   Here only \(x=1\) and \(x=\beta/2\), with \(y=\gamma/2>0\),
   occur. These points meet the stated hypotheses.
3. NIST DLMF, same version, [27.4.3 and 27.4.5](https://dlmf.nist.gov/27.4),
   with the absolute-convergence condition \(\Re s>1\), give the
   Euler product and reciprocal series
   \(1/\zeta(s)=\sum_{m\ge1}\mu(m)m^{-s}\). On \(\Re s=2\),
   nonvanishing and absolute convergence therefore imply
   \[
   |1/\zeta(2+it)|\le\sum_{m\ge1}|\mu(m)|m^{-2}
                        \le\zeta(2),\qquad
   |\zeta(2+it)|\ge\zeta(2)^{-1}.
   \tag{4}
   \]
   This is a safe-half-plane bound, not a reciprocal series in the
   critical strip.

### The exact completed numerator and derivative

Write
\[
 G(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2).
\]
L018 gives \(\xi(s)=G(s)\zeta(s)\) near both \(s_*\) and \(\rho\).
Since \(\xi\) is entire, the maximum modulus principle on its closed
radius-\(R\) disk gives
\[
 M_\rho\ge\max_{|s-s_*|=R}|\xi(s)|\ge|\xi(s_*)|.
 \tag{5}
\]
The circle maximum defining \(M_\rho\) exists by continuity. This is
an application to the entire completion, not to its logarithmic
derivative, which may have poles inside the disk.

At \(s_*=2+i\gamma\), the exact prefactors satisfy
\[
 |s_*(s_*-1)|=\sqrt{\gamma^2+4}\sqrt{\gamma^2+1}\ge\gamma^2,
 \quad |\pi^{-s_*/2}|=\pi^{-1}.
\]
By input 2, for all sufficiently large \(\gamma\),
\(|\Gamma(1+i\gamma/2)|\ge c\gamma^{1/2}e^{-\pi\gamma/4}\)
for an absolute \(c>0\). Together with (4), this proves
\[
 |\xi(s_*)|\ge c_0\gamma^{5/2}e^{-\pi\gamma/4}
 \tag{6}
\]
with \(c_0>0\) independent of the zero.

Near \(\rho\), \(G\) is holomorphic and nonzero, since
\(0<\beta<1\) and \(\gamma>0\). L018 gives
\(\zeta(\rho)=0\), and differentiation gives exactly
\[
 \xi'(\rho)=G'(\rho)\zeta(\rho)+G(\rho)\zeta'(\rho)
            =G(\rho)\zeta'(\rho).
 \tag{7}
\]
Every term involving the derivative of a completion prefactor is in
\(G'(\rho)\zeta(\rho)\) and vanishes. Simplicity gives
\(\xi'(\rho)\ne0\), hence also \(\zeta'(\rho)\ne0\), permitting the
subsequent division. It supplies no quantitative derivative lower bound.

For fixed \(\beta\), \(|\rho(\rho-1)|\le B_\delta\gamma^2\) for
\(\gamma\ge1\), and \(|\pi^{-\rho/2}|=\pi^{-\beta/2}\).
Input 2 bounds the gamma factor above by
\(B_\delta\gamma^{\beta/2-1/2}e^{-\pi\gamma/4}\).
Input 1 and (7) thus give
\[
\begin{aligned}
 |\xi'(\rho)|
 &\le B_{\delta,\epsilon}
    \gamma^{2+\beta/2-1/2+(1-\beta)/2+\epsilon}
    e^{-\pi\gamma/4}\\
 &=B_{\delta,\epsilon}\gamma^{2+\epsilon}e^{-\pi\gamma/4}.
\end{aligned}
 \tag{8}
\]
The exponent identity is \(2+\beta/2-1/2+(1-\beta)/2=2\).
All estimates used are uniform over sufficiently large heights at this
fixed real part. Now (5)–(8), \(1+|F(s_*)|\ge1\), and the nonzero
derivative yield
\[
 H_\rho\ge\frac{|\xi(s_*)|}{|\xi'(\rho)|}
 \ge c_{\delta,\epsilon}\gamma^{1/2-\epsilon}.
\]
The exponential decays cancel because both gamma factors have exactly
the imaginary part \(\gamma/2\). This proves (1).

### A strict exponent gap and the floor

L645 proves \(0<q_\delta<1\), and hence \(\lambda_\delta>0\).
Its exact formula also gives
\[
 q_\delta^2-\frac{d^2}{R^2}
 =\frac{R^4-d^4}{R^2(R^4+d^2)}>0,
\]
since \(R>d>0\). As \(d=3/2-\delta>1\),
\[
 \lambda_\delta<\log(R/d)
 =\log\left(1+\frac{\delta}{2d}\right)
 <\log(5/4)<1/4.
\]
The last inequality is the strict elementary inequality
\(\log(1+x)<x\) at \(x=1/4\). This proves (2).

Use (1) with \(\epsilon=1/4\), and write its constant as \(c_\delta>0\).
For every integer \(N=\lfloor\log\gamma\rfloor\),
\[
 \frac{H_\rho}{A_\delta^{-1}e^{\lambda_\delta N}}
 \ge c_\delta A_\delta
       \gamma^{1/4-\lambda_\delta}
 \ge c_\delta A_\delta\gamma^{\mu},
 \qquad \mu=\tfrac14-\log(5/4)>0.
 \tag{9}
\]
Here \(N\le\log\gamma\) and \(\lambda_\delta>0\) justify the direction;
rounding only decreases the denominator. Increase the estimate's onset
to also satisfy
\(\gamma\ge(2/(c_\delta A_\delta))^{1/\mu}\).
Then (9) is at least 2, proving (3) strictly. This defines an existential
\(T_\delta\); no effective constant has been supplied.

Finally L645 gives \(H_\rho\ge1\). Equation (3) therefore implies
\(\log A_\delta+\log^+H_\rho>\lambda_\delta N\).
The real number inside L645's floor for \(n_0\) exceeds the integer
\(N\), so \(n_0=1+\lfloor(\log A_\delta+\log^+H_\rho)/\lambda_\delta\rfloor>N\).
This is only failure of its sufficient cutoff at \(N\). No inference
about actual PSD, the least witness size or existence of off-line zeros
has been made. Independent all-degree positivity remains unresolved.

### Independent critical audit — 1 November 2026

**Verdict: accepted as stated, with no mathematical repair.** This audit
reused the separately approved source scope and the primary extracts in
the prior growth assessment. It did not retrieve sources again, reprove
convexity, or extend the hypotheses. The local mathematical inputs remain
L018 and L645. The checks below validate the proposed specialization;
they are not a further growth theorem beyond the cited sources.

1. **Completion and zero hypotheses.** At the two points used in the
   proof, the completion identity of L018 holds without a removable-value
   ambiguity. At the stipulated zero, the polynomial prefactor has no
   zero, the gamma function is holomorphic and nonzero, and the exponential
   prefactor is nonzero. Thus differentiating gives precisely (7), not
   a bound involving a derivative of a prefactor. Simplicity permits
   division by the resulting nonzero derivative. It is not a quantitative
   lower bound and makes no assertion that the stipulated zeros exist.
2. **Numerator and denominator powers.** The absolutely convergent
   reciprocal series is used only at real part 2, giving the uniform
   lower bound (4). The two polynomial factors there contribute at least
   \(\gamma^2\), and the gamma factor contributes
   \(\gamma^{1/2}e^{-\pi\gamma/4}\). At the zero the corresponding
   powers are \(\gamma^2\),
   \(\gamma^{\beta/2-1/2}e^{-\pi\gamma/4}\), and, from Gonek's
   unconditional derivative bound,
   \(\gamma^{(1-\beta)/2+\epsilon}\). Their exponent sum is exactly
   \(2+\epsilon\). The cited derivative estimate is an upper bound;
   dividing the numerator lower bound by it gives a lower bound on the
   ratio, in the direction required by (1). Both gamma arguments have
   imaginary part \(\gamma/2\), so their exponential decay cancels
   exactly. There is no uncontrolled imaginary shift or residual
   logarithmic factor in this use of the epsilon-bound.
3. **Full-circle maximum and uniformity.** Entirety of \(\xi\)
   justifies bounding its center value by its boundary maximum, which is
   at most the defined \(M_\rho\). No maximum principle is applied
   to the meromorphic \(F\). The factor \(1+|F(s_*)|\) can be
   discarded for a lower bound, with no anchor estimate needed. At each
   fixed \(\delta\), the imported derivative bound and the two gamma
   estimates hold at all sufficiently large heights, uniformly over the
   stipulated zeros. Constants and onsets may depend on
   \(\delta,\epsilon\); no small-displacement uniformity is used.
4. **Contraction comparison.** Direct subtraction from L645's formula
   gives the displayed positive value of
   \(q_\delta^2-d^2/R^2\). Hence \(q_\delta>d/R\), so taking
   negative logarithms gives \(\lambda_\delta<\log(R/d)\), with
   the stated direction. Since \(0<\delta<1/2\) and \(d>1\),
   \(\delta/(2d)<1/4\). Together with L645's \(q_\delta<1\),
   this proves both strict ends of (2). In particular the fixed positive
   gap \(\mu=1/4-\log(5/4)\) in (9) is legitimate throughout the
   allowed displacement range.
5. **Strict onset, integer grid, and logical scope.** With
   \(\epsilon=1/4\), \(N\le\log\gamma\), and
   \(\lambda_\delta>0\), the denominator in (9) is at most
   \(A_\delta^{-1}\gamma^{\lambda_\delta}\). Increasing the
   common onset to the displayed threshold makes the ratio at least 2,
   not just at least 1. L645's \(H_\rho\ge1\) identifies
   \(\log^+H_\rho\) with \(\log H_\rho\). Consequently
   \(X=(\log A_\delta+\log^+H_\rho)/\lambda_\delta>N\);
   for integer \(N\), \(\lfloor X\rfloor\ge N\), so
   \(n_0>N\). This includes integral \(X\) and integral
   \(\log\gamma\). It proves failure only of L645's sufficient
   condition (7). Negating that condition cannot establish PSD or bound
   the least negative witness from below.

The accepted conclusion stops the unchanged sufficient-cutoff mechanism
at logarithmic grid size, for fixed displacement and sufficiently high
stipulated simple zeros. It leaves actual signs, multiple specified zeros,
effective overlap, small-displacement uniformity and RH unresolved.
L258 and C644a remain comparisons only, with no new DAG input. All checks
were analytic; no numerical experiment, mathematical script or Lean replay
was needed for these inequalities.

## Mathlib

Matching Mathlib coverage for this complete comparison, Gonek's
critical-strip derivative estimate, the vertical gamma estimate and the
reciprocal-series specialization was not checked; no absence is claimed.
The maximum modulus principle and elementary differentiation are named
standard inputs; their exact Mathlib theorem coverage was not inspected
in this step. No Lean replay or numerical certificate is claimed.
