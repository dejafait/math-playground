# C034s: the actual coprime ratio kernel does not remove a conjugate pole pair

## Hypotheses

Use the actual normalization, \(q=2\), \(Q=\log2\), fixed
\(g(y)=\exp(-1/(1-y^2))1_{|y|<1}\), \(h=-g''+g/4\), and
\(f=J(C_\Phi h)\) of C034r. Fourier transforms have phase \(e^{-ity}\)
and inverse factor \(1/(2\pi)\). Set
\[
 C_h(r)=\int_{\mathbb R}f(y)f(y+r)\,dy,\qquad
 w_Q(r)=1_{|r|<Q}\int_{|r|/2}^{Q-|r|/2}
              e^{-s/2}(s^2-r^2/4)\,ds,\qquad k=w_QC_h.
\]
The specified \(f\) is real; thus this \(C_h\) includes the conjugation
in the source's definition. Write
\[
 d(a,b)=1_{(a,b)=1}\mu(a)\mu(b)\rho(ab),\quad
 \rho(n)=\zeta(2)^{-1}\prod_{p\mid n}\frac p{p+1},\quad
 M_K=\sum_{a,b\le K}\frac{d(a,b)}{\sqrt{ab}}k(\log(b/a)).
 \tag{1}
\]
Here \(K\ge2\) is an integer. Assume conditionally that an actual
nontrivial zero \(\rho_*=\beta+i\gamma\) of zeta has exact finite
order \(m\ge1\), with \(\beta=1/2+\delta\), \(0<\delta<1/2\).
The star distinguishes the selected zero from the arithmetic weight.
No existence assertion, rightmost-zero premise, simplicity assumption,
uniform zero separation or RH premise is made.

## Conclusion

The double Dirichlet series
\[
 D(u,v)=\sum_{a,b\ge1}d(a,b)a^{-u}b^{-v}
       =\frac{\mathcal H(u,v)}{\zeta(u)\zeta(v)}
 \tag{2}
\]
converges absolutely for \(\Re u,\Re v>1\). Its Euler remainder
\[
 \mathcal H(u,v)=\zeta(2)^{-1}\prod_p
 \frac{1-\frac p{p+1}(p^{-u}+p^{-v})}
      {(1-p^{-u})(1-p^{-v})}
 \tag{3}
\]
is holomorphic on \(\Re u>0,\Re v>0,\Re(u+v)>1\), and
\(\mathcal H(\rho_*,\overline{\rho_*})>0\).

There is a nonnegative integrable Fourier density
\(\lambda=\widehat k\), with
\(\int\lambda(t)\,dt/(2\pi)=k(0)>0\). On
\(\Re u,\Re v>1/2\) the **actual ratio-integrated cutoff multiplier**
\[
 B(u,v)=\frac1{2\pi}\int_{\mathbb R}
       \frac{\lambda(t)}
       {(u-1/2-it)(v-1/2+it)}\,dt
 \tag{4}
\]
is holomorphic and satisfies
\[
 B(\rho_*,\overline{\rho_*})
 =\frac1{2\pi}\int_{\mathbb R}
       \frac{\lambda(t)}{\delta^2+(\gamma-t)^2}\,dt>0.             \tag{5}
\]
Consequently \(D(u,v)B(u,v)\) has a nonzero coefficient of
\((u-\rho_*)^{-m}(v-\overline{\rho_*})^{-m}\).
Neither the coprime factors nor the actual ratio integration remove
this local pole pair.

Both inclusive square cutoffs have the exact finite representation
(13) below, including Fourier tails, both Perron cutoff errors, their
product, and the height-end corrections incurred before integrating
the ratio variable. The complete local principal part is (17).
For \(x=K+1/2\), its double residue is exactly
\[
 R_{\rho_*}(x)=x^{2\delta}P_{\rho_*}(\log x),                    \tag{6}
\]
where \(P_{\rho_*}\) is a real polynomial of degree \(2m-2\) with
leading coefficient
\[
 \frac{\mathcal H(\rho_*,\overline{\rho_*})}
      {((m-1)!)^2}
 \left|\frac{m!}{\zeta^{(m)}(\rho_*)}\right|^2
 B(\rho_*,\overline{\rho_*})>0.                                \tag{7}
\]
This is a local residue in the exact representation, **not** an
asymptotic or lower bound for \(M_K\). No global contour is shifted.
Other poles, singly crossed residues, and any new horizontal integrals
remain unpaid. Cancellation with those terms is not excluded. Thus the
result rejects automatic local pole removal, not the one-sided upper
\(M_K\le C_\epsilon K^\epsilon\), not every signed-covariance mechanism,
and not RH. The finite identity and this conditional local conclusion
passed the independent conceptual audit2086 recorded in Section 6.

## Proof

### Source scope and why the specialization is needed

Equation (1) is the exact GC12 object in Leonard van Hemert,
*Exact Zero Detection and Compact Arithmetic Realizations for the
Riemann Xi Function*, v1.0.0, 11 October 2026, DOI 10.5281/zenodo.23295277,
[tagged primary TeX](https://raw.githubusercontent.com/LeonardSEO/riemann-xi-zero-detection/refs/tags/v1.0.0/paper/paper.tex),
GC12-GC18, source lines 11613-11702. That arithmetic decomposition is
not imported as an audited theorem here: (1) is our definition.
C034r supplies the verified actual kernel and fixed-input properties.
Its conditional energy detector is a possible downstream use, not an
input to this calculation. The GC13/GC18 decomposition, high primitive
estimate, scale errors, full energy estimate and mixed-form transfer
remain independent obligations.

The pre-existing EXPLORE assessment2081 and source-notes2082 cover this
bounded test. G. Bhowmik, D. Essouabri and B. Lichtin,
*Meromorphic continuation of multivariable Euler products*,
Forum Math. 19 (2007), 1111-1139,
DOI [10.1515/FORUM.2007.044](https://doi.org/10.1515/FORUM.2007.044),
[author proof PDF](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/multieuler.pdf),
Lemma 1 and Theorem 1, PDF pp. 4-8, give general zeta-factor extraction.
Their fixed-integer local polynomial hypotheses do not directly
include the prime-dependent \(p/(p+1)\) weight. The elementary extraction
below checks exactly that difference and the nonvanishing needed here;
it is not a reproof of their general theorem.

For finite-cutoff context, O. Ramaré, *Modified truncated Perron
formulae*, Ann. Math. Blaise Pascal 23 (2016), 109-128,
[Theorem 1.1, pp. 109-110 and endpoint proof p. 116](https://numdam.org/item/10.5802/ambp.356.pdf),
retains absolute truncation and short-interval errors. Its
[3 October 2021 addendum](https://ramare-olivier.github.io/Maths/TruncatedPerron-5-Addendum-04.pdf),
Theorem 1.1 and Note 1, pp. 1-4, does not license a simultaneous
good-height choice here. We use only classical Perron inversion and
prove the elementary fixed-height tail bound needed for our two
cutoffs. Fourier inversion and Plancherel are standard named inputs;
no smooth-kernel Mellin decay theorem is applied to the window's cusp.
The checked sources supply techniques, not (5)-(7).
No novelty beyond that bounded comparison is asserted.

### 1. The unmodified ratio kernel has a positive Fourier density

C034r's actual theta derivative bounds, convolved with the compact
smooth \(h\) and multiplied by \(e^{-y/4}\), show that \(f\) is a real
Schwartz function. Indeed its \(j\)-th derivative is a finite sum of
weighted convolutions with \(\Phi^{(l)}\), \(0\le l\le j\); outside
the support enlarged by one, each inherits the superexponential
decay proved there. Also \(f\ne0\): C034r's Fourier multiplier is
\(\Xi(t-i/4)\widehat{Jh}(t)\), a product of two nonzero entire
functions, and therefore it cannot vanish identically on the real line.

Define \(j_Q(t)=t e^{-t/4}1_{[0,Q]}(t)\). For \(0\le r<Q\),
\[
 \int j_Q(t)j_Q(t+r)\,dt
 =\int_0^{Q-r}t(t+r)e^{-t/2-r/4}\,dt=w_Q(r),
 \tag{8}
\]
by \(s=t+r/2\). Both sides are even in \(r\), zero for \(|r|\ge Q\),
and agree at the endpoints, so (8) holds everywhere. Both \(j_Q\)
and \(f\) are real in \(L^1\cap L^2\). Fubini for their correlations
and Plancherel give \(\widehat w_Q=|\widehat j_Q|^2\) and
\(\widehat C_h=|\widehat f|^2\). These are integrable, nonnegative,
even functions. Their inverse Fourier formulae and absolute Fubini give
\[
 \lambda(t)=\frac1{2\pi}
       \bigl(|\widehat j_Q|^2*|\widehat f|^2\bigr)(t)\ge0,\qquad
 k(r)=\frac1{2\pi}\int\lambda(t)e^{itr}\,dt.                     \tag{9}
\]
The convolution is integrable; it is also continuous since
\(|\widehat f|^2\) is bounded and uniformly continuous.
Its mass is \(2\pi\|j_Q\|_2^2\|f\|_2^2=2\pi k(0)>0\).
Thus (9) is a pointwise identity for the actual continuous \(k\).
No replacement by a different positive kernel has occurred.
In particular, the lack of smoothness of \(j_Q\) at \(Q\), and of
its correlation at zero, causes no omitted Fourier error.

### 2. Exact arithmetic factors and the local continuation domain

For \(\Re u,\Re v>1\), absolute convergence follows from
\(|d(a,b)|\le\zeta(2)^{-1}\). At each prime, squarefreeness and
coprimality allow only \((v_p(a),v_p(b))=(0,0),(1,0),(0,1)\).
Multiplicativity therefore gives the local factor
\(1-c_p(p^{-u}+p^{-v})\), where \(c_p=p/(p+1)\), and the single
constant \(\zeta(2)^{-1}\). Extracting the absolutely convergent
reciprocal-zeta factors proves (2)-(3) in this initial domain.

Put \(X_p=p^{-u}\), \(Y_p=p^{-v}\). The factor in (3) minus one is
\[
 \frac{(1-c_p)(X_p+Y_p)-X_pY_p}{(1-X_p)(1-Y_p)}.                \tag{10}
\]
On a compact subset of the asserted continuation domain, choose
\(\eta>0\) with \(\Re u,\Re v\ge\eta\) and
\(\Re(u+v)\ge1+\eta\). The denominators have modulus at least
\((1-2^{-\eta})^2\), while the numerator is bounded by
\(2p^{-1-\eta}+p^{-1-\eta}\). The sum over primes converges, even
when enlarged to all integers. The product of (10) plus one thus
converges normally, defining a holomorphic \(\mathcal H\).
It may have zeros elsewhere; none are ruled out without proof.
Equation (2) gives the meromorphic continuation on this connected
domain, by agreement on the absolute region.

At the selected conjugate pair each numerator is
\[
 1-\frac{2p}{p+1}p^{-\beta}\cos(\gamma\log p)
 \ge1-\frac{2p^{1-\beta}}{p+1}
 >1-\frac{2\sqrt p}{p+1}>0.
\]
The denominator is \(|1-p^{-\rho_*}|^2>0\). Absolute convergence
of the deviations from one and positivity of every factor make their
product strictly positive, not merely nonnegative. This proves the
claimed value of \(\mathcal H\).

### 3. The finite square, both boundary errors, and ratio integration

This section states an exact finite identity before any local pole
calculation. Fix \(c>1/2\), \(x=K+1/2\), \(T>0\), and \(R>0\).
Let \(\sigma=1/2+c>1\), and put
\[
 p_T(y)=\frac1{2\pi i}\int_{c-iT}^{c+iT}\frac{y^s}{s}\,ds,\quad
 H_n=1_{n\le K},\quad e_n=p_T(x/n)-H_n.
\]
Classical Perron inversion on a positive vertical line gives
\(p_\infty(y)=1_{y>1}\) for \(y\ne1\).
For completeness the finite-height error follows by integrating
each omitted tail \(\int_T^\infty e^{it\log y}/(c+it)\,dt\)
by parts. Its boundary has modulus at most \(1/(T|\log y|)\);
the derivative integral is at most the same, because
\(\int_T^\infty(c^2+t^2)^{-1}dt\le1/T\).
The negative tail gives the same bound. Hence
\[
 |e_n|\le\frac{2(x/n)^c}{\pi T|\log(x/n)|},\quad
 A_K=\sum_{n\le K}n^{-1/2}\le2\sqrt K,\quad
 b_T=\frac{2x^c}{\pi T}\sum_{n\ge1}
       \frac{n^{-c-1/2}}{|\log(x/n)|}<\infty.                  \tag{11}
\]
Here \(x\) is not an integer: neither cutoff encounters \(y=1\)
or a silently discarded half-weight. The series in (11) converges
since \(c+1/2>1\), with only finitely many near-endpoint terms.
In particular \(\sum n^{-1/2}|e_n|\le b_T\), and \(b_T\to0\)
for fixed \(x,c\).

Define \(k_R(r)=\int_{-R}^R\lambda(t)e^{itr}dt/(2\pi)\),
\(M_K^R\) by (1) with \(k_R\), and
\(\tau_R=\int_{|t|>R}\lambda(t)dt/(2\pi)\). Absolute convergence
on the initial lines, followed by finite-contour Fubini, gives
\[
 \begin{split}
 I_{T,R}
 &=\frac1{2\pi}\int_{-R}^R\lambda(t)
   \frac1{(2\pi i)^2}\int_{c-iT}^{c+iT}\int_{c-iT}^{c+iT}
   \frac{x^{s+z}D(1/2+s+it,1/2+z-it)}{sz}\,dz\,ds\,dt\\
 &=\sum_{a,b\ge1}\frac{d(a,b)}{\sqrt{ab}}
              k_R(\log(b/a))p_T(x/a)p_T(x/b)
  =M_K^R+E_{\rm cut}.
 \end{split}                                                   \tag{12}
\]
Explicitly \(E_{\rm cut}\) is the same absolutely convergent double
sum with the product of Perron factors replaced by
\(H_ae_b+e_aH_b+e_ae_b\). Thus **both** square boundaries and
their intersection are retained. Since \(|k_R|\le k(0)\),
\[
 |E_{\rm cut}|\le\zeta(2)^{-1}k(0)(2A_Kb_T+b_T^2),\qquad
 |M_K-M_K^R|\le\zeta(2)^{-1}A_K^2\tau_R.
\]

One further endpoint correction is essential if the ratio integral
is brought inside fixed contours. Set \(u=1/2+s+it\),
\(v=1/2+z-it\). The resulting contours are
\(U_t=[\sigma+i(-T+t),\sigma+i(T+t)]\) and \(V_{-t}\) with
the opposite shift, all oriented upward. Let \(U_0=V_0\) be
the unshifted segment and let \(\Delta U_t=U_t-U_0\),
\(\Delta V_{-t}=V_{-t}-V_0\) be oriented chains.
They consist exactly of the top and bottom end segments; for example
\(\Delta U_t=[\sigma+iT,\sigma+i(T+t)]
             -[\sigma-iT,\sigma+i(-T+t)]\).
Let \(E_{\rm height}\) be the \(\lambda(t)/(2\pi)\) integral of
\[
 \frac1{(2\pi i)^2}
 \left(\int_{\Delta U_t}\int_{V_0}
       +\int_{U_0}\int_{\Delta V_{-t}}
       +\int_{\Delta U_t}\int_{\Delta V_{-t}}\right)
 \frac{x^{u+v-1}D(u,v)}
      {(u-1/2-it)(v-1/2+it)}\,dv\,du
\]
over \(-R\le t\le R\). All these integrals lie in the absolute
domain. With \(B_R\) defined as in (4) over \([-R,R]\), we have
the exact identity
\[
 \boxed{\displaystyle
 M_K=\frac1{(2\pi i)^2}\int_{U_0}\int_{V_0}
       x^{u+v-1}D(u,v)B_R(u,v)\,dv\,du
       +E_{\rm height}-E_{\rm cut}+(M_K-M_K^R).}                \tag{13}
\]
This is a finite identity, not an interchange of conditionally
convergent infinite contours.

Even these height corrections can be bounded explicitly without
meromorphic continuation. For \(T>2R\), put
\[
 e=\frac{2R}{T-R},\qquad
 j=2\operatorname{arsinh}\frac{T+R}{c},\qquad
 D_\sigma=\zeta(2)^{-1}\zeta(\sigma)^2 .
\]
On either end chain the integral of the reciprocal denominator's
modulus is at most \(e\); on the fixed vertical segment it is at
most \(j\). Also \(|D(u,v)|\le D_\sigma\) there and
\(|x^{u+v-1}|=x^{2c}\). Consequently
\[
 |E_{\rm height}|
 \le\frac{k(0)D_\sigma x^{2c}}{(2\pi)^2}(2ej+e^2)
 \longrightarrow0\quad(T\to\infty,\ R,x,c\ \hbox{fixed}).       \tag{14}
\]
The order of limits that recovers (1) from (13) is first
\(T\to\infty\) at fixed \(R,x,c\), then \(R\to\infty\).
No error here is claimed uniform in growing \(x\).
Nor does (14) bound horizontal sides of a later contour shift into
a region where reciprocal zeta is large.

### 4. The complete integrated local principal part

In \(\Re u,\Re v>1/2\), the denominators in (4) are bounded
below on every compact set by fixed positive real-part margins.
The same holds for every differentiated reciprocal denominator.
The integrable majorant is therefore a compact-dependent multiple
of \(\lambda\). Differentiation under the integral proves joint
holomorphy of \(B\); it also proves locally uniform convergence of
all derivatives of \(B_R\) to those of \(B\).
At the conjugate pair the denominator product is exactly
\(\delta^2+(\gamma-t)^2\). Equations (5) and \(\delta>0\) now
give finite, strict positivity, using the positive mass in (9).
For all sufficiently large finite \(R\) the same holds for \(B_R\).
This is the actual kernel and includes both Perron denominators.

Choose a positive radius \(r<\delta/2\) small enough that the
closed disks about \(\rho_*\) and \(\overline{\rho_*}\) contain
no other zeros or poles of zeta, and their boundary circles contain
none. Such a radius exists for this fixed finite-order zero.
The product bidisk lies in the domains of both \(\mathcal H\)
and \(B\). Write \(U=u-\rho_*\), \(V=v-\overline{\rho_*}\), and
\[
 b(u)=\frac{(u-\rho_*)^m}{\zeta(u)},\quad
 \widetilde b(v)=\frac{(v-\overline{\rho_*})^m}{\zeta(v)},\quad
 \mathcal A(u,v)=\mathcal H(u,v)b(u)\widetilde b(v)B(u,v).
 \tag{15}
\]
The quotients extend holomorphically across their centers, with
\(b(\rho_*)=m!/\zeta^{(m)}(\rho_*)\ne0\) and the conjugate
value for \(\widetilde b\). Thus
\[
 DB=\frac{\mathcal A(u,v)}{U^mV^m},\qquad
 a_{00}:=\mathcal A(\rho_*,\overline{\rho_*})
 =\mathcal H(\rho_*,\overline{\rho_*})
     |m!/\zeta^{(m)}(\rho_*)|^2B(\rho_*,\overline{\rho_*})>0.
 \tag{16}
\]
After reducing \(r\) if needed the numerator is nonzero on this
bidisk. In particular the order is exactly \(m\) on each local
divisor. It is not a candidate arithmetic pole whose numerator
has been left unexamined.

For precision, the following specifies the *entire* principal part,
including terms singular in only one variable. Let \(T_U,T_V\)
mean Taylor truncation of a holomorphic numerator in the indicated
variable at its center through degree \(m-1\). For
\(\mathcal A_x=x^{u+v-1}\mathcal A\), the full polar part of the
integrand in (13), with \(B\) in place of \(B_R\), is
\[
 \frac{T_U\mathcal A_x+T_V\mathcal A_x
                    -T_UT_V\mathcal A_x}{U^mV^m}.             \tag{17}
\]
The remainder is holomorphic: its numerator is
\((I-T_U)(I-T_V)\mathcal A_x\), divisible by \(U^mV^m\)
by its convergent double Taylor series. The identical formula
holds at finite \(R\) using \(B_R\), with all coefficients
converging to (17). This pays the whole local finite-order
principal-part calculation; it does not drop the singly polar terms.

To extract the double residue, expand
\(\mathcal A=\sum_{j,k\ge0}a_{jk}U^jV^k\) on the bidisk, where
\(a_{jk}=\partial_u^j\partial_v^k\mathcal A
(\rho_*,\overline{\rho_*})/(j!k!)\).
Since \(x^{u+v-1}=x^{2\delta}e^{(U+V)\log x}\), the exact answer is
\[
 R_{\rho_*}(x)=x^{2\delta}
 \sum_{j,k=0}^{m-1}
 \frac{a_{jk}(\log x)^{2m-2-j-k}}
      {(m-1-j)!(m-1-k)!}.                                    \tag{18}
\]
This is the normalized integral of the complete local germ around
both positively oriented small circles, not a highest-order-only
approximation. The coefficient \(a_{00}>0\) gives (7).
For real \(\lambda\), \(B(u,v)=\overline{B(\bar v,\bar u)}\);
the same symmetry holds for \(\mathcal H b\widetilde b\).
It follows that \(a_{jk}=\overline{a_{kj}}\), so (18) is real.
When \(m=1\) it is the positive constant in (16) times \(x^{2\delta}\);
for general \(m\) it is eventually positive with the stated degree.

All local interchanges can also be made first at finite \(R\).
On the two small circles the denominators have real-part margins
at least \(\delta-r>0\), and \(\lambda\) is integrable. Fubini
therefore commutes the compact ratio integral and both local contour
integrals, then dominated convergence permits \(R\to\infty\).
For fixed \(R\), take \(T>|\gamma|+R+r\) in the original finite
representation if the translated circles are considered in the
\(s,z\) variables. No integral is commuted through a pole: the
circles stay a positive distance from it, and residues are taken
only after establishing the holomorphic numerator.

### 5. The precise stop and the remaining mathematical gap

Equation (13) connects the integrated germ used in (17)-(18) to
the actual finite square; all its pre-shift corrections are displayed.
Equations (16)-(18) reject the proposed local identity in which
coprimality and the fixed ratio kernel automatically annihilate
every reciprocal-zeta pole. The two unweighted neutral moments
of \(h\) cannot supply that identity, since (5) remains strictly
positive for the actual \(f\).

We have not deformed the fixed contours of (13) past this pair.
Such a deformation may cross other zeros, create single-residue
contour integrals from (17), and create horizontal integrals.
Their total may interact with (18); no estimate excludes that.
In particular, no assertion that a selected \(\rho_*\) is
rightmost enters this proof. A nonzero local residue is not by
itself a singularity of the fully diagonal one-variable sum.
If (18) were an uncanceled main term, its
\(x^{2\delta}(\log x)^{2m-2}\) scale would exceed a subpower bound
with \(\epsilon<2\delta\). Establishing that premise is precisely
what has **not** been done. The one-sided upper for \(M_K\) is
neither proved nor refuted. C034r's detector, both primitive uppers,
and actual-Xi algebraic mixed positivity remain separate.

### 6. Independent conceptual audit2086

The unchanged assessment2084, approved in2085, covers this audit.
The source comparison and precise citations above are reused; this is
verification of C034s, not a new theorem or a renewed source search.
C034r's actual theta bounds and weighted multiplier were checked as
the mathematical input. The following details make the limiting and
noncancellation checks explicit.

**Actual kernel and arithmetic.** The weighted convolution of the
compact smooth input with the theta kernel has integrable derivatives
of every order and superexponential tails, hence is Schwartz.
Fourier uniqueness and C034r's nonzero entire multiplier show that it
is not zero. In (8), the substitution has Jacobian one and endpoints
\(r/2,Q-r/2\); the exponential becomes exactly \(e^{-s/2}\).
Thus both correlations, the convolution factor \(1/(2\pi)\) in (9),
and the positive mass \(2\pi k(0)\) use the original window.
The arithmetic expansion permits one prime in at most one index;
\(\zeta(2)^{-1}\) occurs once, not once per prime or index.
The compact majorant in (10) is summable on the stated
domain. At the conjugate pair every factor is positive and the sum
of absolute deviations from one is finite. A sufficiently late tail
has factors within \(1/2\) of one, so its logarithms converge
absolutely; the finitely many earlier positive factors cannot make
the product zero. No nonvanishing assertion elsewhere is needed.

**Both cutoffs.** At every fixed \(T>0\), direct absolute integration
on the Perron segment gives
\[
 |p_T(x/n)|\le (x/n)^c\operatorname{arsinh}(T/c)/\pi.
\]
Together with \(\sum n^{-1/2-c}<\infty\) and \(\lambda\in L^1\),
this pays the finite-contour Fubini in (12), including the two infinite
index sums. The phase is \(a^{-it}b^{it}\), so its Fourier integral
is \(k_R(\log(b/a))\) with the displayed sign. In each omitted
Perron tail, integration by parts gives a boundary at most
\(1/(T|\log(x/n)|)\) and an integral at most the same.
Two tails and the factor \(1/(2\pi)\) give exactly (11).
Since \(x=K+1/2\), the finitely many near-cutoff logarithms are
nonzero; the remaining series is summable. Expansion of
\((H_a+e_a)(H_b+e_b)\) gives both single errors and their product,
with the signs in (13). The Fourier-tail estimate uses
\(\|k-k_R\|_\infty\le\tau_R\), without an unproved decay rate.

**Height chains and limits.** The substitution preserves
\(s+z=u+v-1\). Expanding
\((U_0+\Delta U_t)\times(V_0+\Delta V_{-t})\) as oriented chains
gives exactly the three corrections preceding (13), for either sign
of \(t\). For \(|t|\le R\) each end chain has total length
\(2|t|\). When \(T>2R\), its corresponding denominator has
imaginary part of magnitude at least \(T-R\), giving the bound
\(e\). On an unshifted segment, translation of its height variable
places the integration interval inside \([-T-R,T+R]\), giving
\(j\). All chains have real part \(\sigma>1\), so the absolute
Dirichlet majorant \(D_\sigma\) applies throughout. This proves
(14); its bound is \(O_{R,x,c}(\log T/T)\).
For fixed \(R,x,c\), (13) therefore tends to \(M_K^R\) in its
integral term as \(T\to\infty\). Only afterwards is \(R\to\infty\)
taken to recover \(M_K\). Neither a simultaneous limit nor an
estimate uniform in growing \(K\) has been used.

**Finite-R local germ and full residue.** If a compact set has
\(\Re u-1/2\ge\alpha>0\), \(\Re v-1/2\ge\beta_0>0\), then
for all integers \(j,k\ge0\),
\[
 \left|\partial_u^j\partial_v^k(B-B_R)(u,v)\right|
 \le \frac{j!k!\,\tau_R}{\alpha^{j+1}\beta_0^{k+1}}.
\]
The same bounds with \(k(0)\) justify holomorphic differentiation
of \(B\) itself. On the selected bidisk take
\(\alpha=\beta_0=\delta-r\). For sufficiently large \(R\),
\(\int_{-R}^R\lambda>0\); hence the conjugate-pair value of
\(B_R\), as well as its limit, is strictly positive. Multiplication
by the fixed holomorphic factors in (15) preserves local uniform
convergence and convergence of derivatives. Cauchy's formula on
smaller bidisks therefore verifies convergence of the Taylor polar
parts and of the double residues at each fixed \(x\).

In a convergent double Taylor series, the numerator in (17) retains
exactly those monomials with \(j<m\) or \(k<m\). All discarded
monomials are divisible by \(U^mV^m\). Thus single polar terms
are retained, and the remaining quotient is holomorphic. The
coefficient of \(U^{-1}V^{-1}\), after multiplication by
\(x^{2\delta}e^{(U+V)\log x}\), is precisely (18).
The only term of degree \(2m-2\) is
\(a_{00}/((m-1)!)^2>0\); this includes \(m=1\).
Real coefficients and symmetry of the arithmetic factors, together
with real \(\lambda\), give
\(\mathcal A(u,v)=\overline{\mathcal A(\bar v,\bar u)}\).
Consequently \(a_{jk}=\overline{a_{kj}}\), proving reality of the
whole polynomial, not just its leading coefficient.

**Scope verdict.** At finite \(R\) these are local germs of the
actual integrand in (13). Their limiting germ is consequently tied
to that representation, rather than to a substituted kernel. This
statement does not assign the local residue an uncanceled contribution
to \(M_K\): making such an assignment would require a global contour
deformation and estimates for everything else crossed or left over.
No error requiring retraction was found. Stop2084 is retained solely
as a conditional obstruction to automatic local annihilation.
The diagonal one-variable singularity, the one-sided GC12 upper and
all the other obligations in Section 5 remain unresolved. The audit
establishes reliability of this local input, not further progress
beyond C034s's claim or the checked literature.

## Mathlib

Full matching coverage for the weighted coprime series, the finite
two-cutoff representation and the integrated local residue has not
been checked; availability is unknown, not asserted absent.
No Mathlib theorem is used as an unverified substitute for these
hypotheses. Supporting mathematics is classical Fourier/Plancherel,
Perron inversion, normal convergence of holomorphic products,
Taylor expansion and the residue theorem. No numerical certificate
or computed zero is used. This conditional obstruction is not a
candidate solution of RH.
