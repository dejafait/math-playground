# L531 — Conditional common-signal continuation: analytic audit

## Hypotheses

Let K=Q(sqrt(-3)), and let eta range over all primitive finite-order Hecke
characters of K. Write L_eta(s)=L_K(s,eta). Use the classical Hecke
meromorphic-continuation and Euler-product theorem: L_eta is entire for
nonprincipal eta, has only a simple pole at 1 for principal eta, and for
Re(s)>1 has its absolutely convergent Euler product. A local value eta(p)
is zero at a ramified prime and otherwise has modulus one. In particular,
sum_p (Np)^(-2)<infinity, and L_eta has no zeros in Re(s)>1. These are
standard analytic inputs, not a fixed zero-free half-plane left of 1.

Define beta_* as the supremum of {1/2} together with the real parts of all
zeros rho of these primitive functions with 1/2<=Re(rho)<=1. Poles do not
count as zeros. Thus 1/2<=beta_*<=1. Fix sigma_0 in (1/2,1), suppose
Delta_0=beta_*-sigma_0>0, and fix c in R, with C(s)=s+c.

Assume there are numbers omega and sigma, independent of eta, satisfying
0<omega<Delta_0 and sigma>0. For each eta assume the following data exist:
a finite set S_eta of prime ideals; a function H_eta holomorphic on
Re(s)>sigma_0 satisfying |H_eta(s)-1|<=1/2 everywhere there; and a
complex-valued function J_eta(Z) for all sufficiently large positive real Z.
Set

\[
 P_\eta(s)=\prod_{\mathfrak p\in S_\eta}
       (1-\eta(\mathfrak p)(N\mathfrak p)^{-s}),\qquad
 L_\eta^S(s)=L_\eta(s)P_\eta(s),
\]
\[
 f_\eta(Z)=\frac1{2\pi i}\int_{\Re w=2}
 Z^{w+c}e^{(w-5/6)^2}\frac{H_\eta(w)}{L_\eta^S(w)}\,dw
 \quad(Z>0),
\]

where the line is oriented upward and powers of positive Z use real log Z.
Assume, as Z tends to infinity,

\[
 |J_\eta(Z)|=O_\eta(Z^{\sigma_0+c+\omega}),\qquad
 |J_\eta(Z)-f_\eta(Z)|=O_\eta(Z^{\beta_*+c-\sigma}).
\]

The constants, lower thresholds, S_eta and H_eta may depend on eta. The
common positive exponent margins may not. No construction of these data
or proof of these two estimates is included in this result.

## Conclusion

With

\[
 \epsilon=\min\{\Delta_0-\omega,\sigma\}>0,
 \qquad \alpha=\beta_*-\epsilon,
\]

one has sigma_0<alpha<beta_*<=1. For every eta, the stated contracts yield
a holomorphic continuation of 1/L_eta^S to Re(s)>alpha. They therefore
contradict the definition of beta_*. In particular all the hypotheses
cannot hold simultaneously with beta_*>sigma_0.

**Audit verdict:** the conditional analytic proposition passes the endpoint,
Fourier, pole and family-quantifier checks below. This reproduces a result
already proved in the source; it is not a new zero-free estimate. It does
not verify the manuscript's arithmetic estimates, H construction, parameter
selection, Hecke-to-Dirichlet transfer, formal import closure, or the external
premise retained in L452/L461. It supplies no initial Xi signs or RH proof.

## Proof

The audited source is OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, September 30, 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, Section 2, proposition
`lem:continuation-criterion`, including its complete proof and preceding
definition `old-eq:1.1b`. See the
[pinned primary TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
The following details check the stated operations independently. Reproduction
is warranted by the external input's unaudited analytic-reduction qualification;
the low/high contracts remain assumptions throughout.

### 1. Euler deletions, convergence and the small-Z endpoint

For Re(s)>0 each factor of P_eta is nonzero: its subtracted term has
modulus either zero or (Np)^(-Re(s))<1. Finite deletions thus neither remove
nor create zeros or poles in that half-plane. On Re(s)>=2, cancellation in
the absolutely convergent Euler product gives

\[
 \frac1{L_\eta^S(s)}
  =\prod_{\mathfrak p\notin S_\eta}
       (1-\eta(\mathfrak p)(N\mathfrak p)^{-s}),\qquad
 \left|\frac1{L_\eta^S(s)}\right|
  \le M_K:=\prod_{\mathfrak p}(1+(N\mathfrak p)^{-2})<\infty.
\]

The majorant converges since log(1+x)<=x for x>=0. The products converge
locally uniformly there; holomorphy on the larger open region Re(s)>1
also follows from the Euler product. The contract gives |H_eta|<=3/2.
For w=x+it in any fixed strip 2<=x<=B,

\[
 |e^{(w-5/6)^2}|=e^{(x-5/6)^2-t^2}\le C_B e^{-t^2}.
\]

Consequently the integral defining f_eta converges absolutely. Dominated
convergence on compact Z intervals in (0,infinity) proves its continuity.
For fixed Z>0 and fixed B>2, apply Cauchy's integral theorem to the rectangle
with real sides 2 and B and horizontal sides at imaginary parts +/-R.
There are no singularities inside. Each horizontal integral is bounded by
a constant depending on B,c,Z times (B-2)e^(-R^2); it tends to zero.
Both vertical tails tend to zero by the same Gaussian bound. Thus shifting
the line to B is justified without crossing any possible zero. On that line,

\[
 |f_\eta(Z)|\le C_{\eta,B,c} Z^{B+c}\quad(0<Z\le1).
\]

The contour argument uses fixed Z before taking the limit in R; the displayed
bound after the shift is uniform for 0<Z<=1. No estimate uniform in B is
asserted or needed.

### 2. The large-Z endpoint and Mellin holomorphy

Since epsilon<=Delta_0-omega and epsilon<=sigma, both exponents in the
two assumed estimates are at most alpha+c. By the triangle inequality,

\[
 |f_\eta(Z)|\le C_\eta Z^{\alpha+c}\quad(Z\ge Z_{0,\eta}),
\]

enlarging Z_{0,eta} to be at least 1. Also epsilon<=Delta_0-omega<Delta_0,
so alpha>sigma_0; epsilon>0 and beta_*<=1 give alpha<1.

For D={s:Re(s)>alpha}, define

\[
 F_\eta(s)=\int_0^\infty f_\eta(Z)Z^{-s-c}\,\frac{dZ}{Z}.
\]

Let E be a nonempty compact subset of D, and put
m=min_E Re(s)>alpha and M=max_E Re(s). Choose fixed B>max(2,M).
Near zero the absolute integrand, with respect to dZ, is bounded uniformly
on E by C Z^(B-M-1). Near infinity it is bounded by C Z^(alpha-m-1).
These exponents are respectively greater than -1 and less than -1.
On the remaining compact positive Z interval, continuity of f_eta provides
an integrable bound uniform on E. The same bounds multiplied by
|log Z|^j are integrable for each fixed nonnegative integer j, in particular
j=1. Differentiation under the integral is therefore valid locally, and
F_eta is holomorphic on D. Constants and thresholds depend on the fixed
eta; no sum over characters or uniform limit in eta is taken.

### 3. Fourier identification with the exact inversion hypotheses

For Re(s)>1 put A_eta(s)=exp((s-5/6)^2)H_eta(s)/L_eta^S(s).
Write a(t)=A_eta(2+it), which is continuous and satisfies
|a(t)|<=C exp(-t^2). Substituting Z=exp(u) in the original integral gives

\[
 g(u):=e^{-(2+c)u}f_\eta(e^u)
       =\frac1{2\pi}\int_{\mathbb R}e^{itu}a(t)\,dt.
\]

At positive infinity, |g(u)|<=C exp((alpha-2)u), and alpha<1. At negative
infinity choose any B>2 from part 1 to get |g(u)|<=C_B exp((B-2)u).
Together with continuity on finite intervals, this proves g in L1(R).

Use the Fourier conventions

\[
 (\mathcal F b)(u)=\int_{\mathbb R}e^{-2\pi ixu}b(x)\,dx,
 \qquad
 (\mathcal F^{-1}b)(u)=\int_{\mathbb R}e^{2\pi ixu}b(x)\,dx.
\]

Put b(x)=a(2*pi*x). Then b is continuous and integrable, and the ordinary
absolutely convergent change of variable t=2*pi*x gives

\[
 \mathcal F^{-1}b(u)=g(u),\qquad \mathcal F b(u)=g(-u).
\]

Thus **the forward transform** of b is integrable, as required by
`MeasureTheory.Integrable.fourier_fourierInv_eq` in
[Mathlib, pinned Inversion.lean](https://raw.githubusercontent.com/leanprover-community/mathlib4/d0207795ac79006da92d98544e1ce915ae386160/Mathlib/Analysis/Fourier/Inversion.lean),
commit `d0207795ac79006da92d98544e1ce915ae386160`, lines 170--174 in
the inspected rendered source. Its hypotheses are Integrable b,
Integrable (Fourier b), and ContinuousAt b at the evaluation point.
It concludes Fourier(inverseFourier(b))=b there. Apply this standard
inversion theorem at x=t/(2*pi), for every real t. It gives

\[
 a(t)=\int_{\mathbb R}e^{-itu}g(u)\,du
     =\int_0^\infty f_\eta(Z)Z^{-(2+it)-c}\,\frac{dZ}{Z}
     =F_\eta(2+it).
\]

Both the last change of variables and the Fourier integral are absolutely
convergent. No formal double-integral interchange is used. The source
assessment's corrected forward-transform hypothesis is satisfied by the
reflection identity above; inverse-transform integrability is not silently
substituted for it.

### 4. Analytic identity, continuation and poles

Since alpha<1, F_eta and A_eta are holomorphic on the connected half-plane
Re(s)>1. Their agreement on the line Re(s)=2 has accumulation points inside
that domain. The identity theorem gives F_eta=A_eta throughout it.
The lower bound |H_eta|>=1/2 on Re(s)>sigma_0 implies that

\[
 G_\eta(s)=e^{-(s-5/6)^2}F_\eta(s)/H_\eta(s)
\]

is holomorphic on D and agrees with 1/L_eta^S on Re(s)>1.
This construction did not assume nonvanishing at any point with Re(s)<=1.

To spell out why an unrelated analytic continuation cannot bypass a zero,
first take nonprincipal eta. L_eta^S is holomorphic on D. The function
G_eta L_eta^S equals 1 on Re(s)>1, hence equals 1 on all of D by the identity
theorem. A zero of L_eta^S anywhere in D, including hypothetically at s=1,
contradicts that identity.

For principal eta, define E_eta(s)=(s-1)L_eta^S(s). This is holomorphic
on D and E_eta(1)!=0 by the simple-pole theorem and P_eta(1)!=0.
The identity theorem now yields G_eta E_eta=s-1 throughout D. Near 1,
G_eta=(s-1)/E_eta is holomorphic, with a zero at 1: a pole of L_eta^S is
not an obstruction to its holomorphic reciprocal. Any zero rho of
L_eta^S in D must have rho!=1, so E_eta(rho)=0 would imply
0=rho-1, a contradiction. This also covers alpha<1 without excluding
the principal point from D or assuming a general nonvanishing theorem at 1.

### 5. Family supremum and uniformity

All preceding reasoning applies separately to every primitive eta on the
same D, because epsilon depends only on beta_*, sigma_0, omega and sigma.
It does not depend on any character-specific constants, thresholds, finite
sets or functions. We have proved that no member of this family has a zero
with real part greater than alpha.

If every member of the set defining beta_* had real value at most alpha,
then alpha would be an upper bound and beta_*<=alpha. But alpha<beta_*,
and the artificial member 1/2 is below alpha since alpha>sigma_0>1/2.
Therefore the definition of supremum supplies a genuine zero rho of some
primitive eta with Re(rho)>alpha. Attainment of beta_* is not required.
This contradicts part 4 and completes the conditional audit.

The necessity of a common epsilon is substantive: separate positive gaps
depending on eta would not give the same supremum contradiction. The source
explicitly assumes the required uniform omega and sigma; this audit does
not show that its subsequent arithmetic construction supplies them.

## Mathlib

Supporting Fourier inversion is present at the pinned source above, with
the exact theorem and hypotheses used in part 3. Its domain hypotheses are
a finite-dimensional real inner-product space with the Borel measurable
structure; its codomain is a complete complex normed space. R and C with
their usual structures meet these requirements. The normalization is matched
by b(x)=a(2*pi*x), and the forward L1 hypothesis is established explicitly.
The companion `MeasureTheory.Integrable.fourierInv_fourier_eq` has the same
integrability assumptions and the opposite composition.

Full matching Mathlib coverage of this Hecke-family proposition was not
checked. No Lean build, manuscript import-closure check, or verification of
the arithmetic contracts is claimed. The displayed analysis is an informal
audit using standard named analytic theorems, not a formal certificate.
