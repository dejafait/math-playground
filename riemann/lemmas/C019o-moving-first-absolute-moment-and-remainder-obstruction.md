# C019o — Moving first absolute moment and obstruction to the diagonal remainder budget

## Hypotheses

Use exactly the corrected elementary sum V, diagonal H, and remainder
R of C019n, with the scales and phase of C019l. Explicitly, d tends to
infinity through positive integers, and T>2*pi*e is determined by
\[
 d=\frac{T}{2\pi}\left(\log\frac{T}{2\pi}-1\right),\quad
 X=\frac{T}{\sqrt{2d}},\quad q=\log X,\quad
 B=(\sqrt2-1)X,\quad h=3\pi/q,
\]
\[
 J=[X,\sqrt2X],\quad D=[X,\sqrt2X-h],\quad
 t=t(Y)=Y^2/(2d),\quad \ell(Y)=\log(Y/(2\pi)),
\]
\[
 v_n(Y)=\ell(Y)/2-\log n,\qquad
 \vartheta(Y)=Y\ell(Y)/2-Y/2-\pi/8,
\]
\[
 a_n(Y)=n^{-1/2}e^{t(Y)(v_n(Y)^2-\pi^2/16)/4},\quad
 f_n(Y)=\vartheta(Y)-Y\log n+\pi t(Y)v_n(Y)/8,
\]
\[
 N(Y)=\left\lfloor\sqrt{Y/(2\pi)+Y^2/(32d)}\right\rfloor,
 \qquad V(Y)=2\sum_{n\leq N(Y)}a_n(Y)\cos f_n(Y).
\]
On D set V_+(Y)=V(Y+h), E(Y)=V(Y)^2+V_+(Y)^2 and
\[
 H(Y)=2\sum_{n\leq N(Y)}a_n(Y)a_n(Y+h)
                    \cos(f_n(Y)-f_n(Y+h)),
\]
\[
 I_H=\int_D\frac{H}{1+E},\quad
 I_V=\int_D\frac{VV_+}{1+E},\quad
 \mathcal R=I_V-I_H.
\]
Each translated value uses its own time and floor. C019n (4) supplies
H(Y)<=-kappa*q on all D, with kappa=1/(3*pi). All constants below
are absolute, and the common sufficiently-large-d onset is existential.
No RH, random value law, independence, nonvanishing, simplicity or
global bounded backward-heat operator is assumed.

## Conclusion

The actual moving finite sum satisfies
\[
 \int_J|V(Y)|\,dY=O(Bq^{1/4})=o(B\sqrt q).                 \tag{1}
\]
There is an absolute c_*>0 such that, eventually,
\[
 I_H\leq-c_*B\sqrt q,\qquad
 \mathcal R\geq c_*B\sqrt q-B/2.                           \tag{2}
\]
In particular R/B tends to positive infinity. The sufficient condition
R<=c_D*B/2 in C019n, for its fixed c_D>0, fails for all sufficiently
large d. This stops that sufficient closure, not (N), which asks for a
negative fixed-length margin for the bounded normalized product.
The sign of I_V and the actual-Jensen analogue remains undetermined.
The separate conceptual audit1393 below retains this local
specialization and obstruction; it is neither an RH candidate nor a
novelty claim.

## Proof

### Approved scope and standard imports

The prior SPECIALIZE assessment is
`drafts/literature/2026-11-17-jensen-first-absolute-moment-obstruction-1389.md`,
source review1390. It approves this deterministic real Fourier transfer
and the ensuing test of C019n's sufficient budget. The narrowly checked
Jensen assessments and attempt1387 contain no prior such transfer.
The earlier origin-continuity, absolute-variation and endpoint stops
are not reopened. The following results are imported without reproof.

Heap, Radziwill and Soundararajan, *Sharp upper bounds for fractional
moments of the Riemann zeta function*, Q. J. Math. 70 (2019), 1387–1396,
DOI 10.1093/qmathj/haz027,
[arXiv:1901.08423v1, Theorem 1](https://arxiv.org/html/1901.08423v1),
states unconditionally, for real 0<=k<=2 and A>=10,
\[
 \int_A^{2A}|\zeta(1/2+iy)|^{2k}\,dy\ll_k A(\log A)^{k^2}.
                                                               \tag{3}
\]
Use only k=1/2. This is an ordinary critical-line moment, not a
theorem about V or moving heat time.

The critical-line approximate functional equation is
[DLMF 25.9.3](https://dlmf.nist.gov/25.9.E3), citing Titchmarsh,
*The Theory of the Riemann Zeta-Function*, second edition, revised
Heath-Brown (1986), (4.17.1), p. 88. Its two sums have the same
floor M(y)=floor(sqrt(y/(2*pi))) and error O(y^(-1/4)), as y tends
to positive infinity. Use the exact real Hardy function
Z(y)=exp(i*theta(y))*zeta(1/2+iy), where
\[
 \theta(y)=\operatorname{Im}\log\Gamma(1/4+iy/2)-(y/2)\log\pi
\]
uses the continuous gamma phase. Reality and |Z(y)|=|zeta(1/2+iy)|
are as in Gonek–Ivic,
[*On the distribution of positive and negative values of Hardy's Z-function*,
arXiv:1604.00517v1, (1.1) and its following discussion](https://arxiv.org/html/1604.00517v1).
The functional-equation factor on this line is exp(-2i*theta(y)),
so multiplying the two-sum equation by exp(i*theta(y)) gives
\[
 Z(y)=2\sum_{n\leq M(y)}n^{-1/2}
                  \cos(\theta(y)-y\log n)+O(y^{-1/4}).     \tag{4}
\]
Fixed-sector Stirling, [DLMF 5.11(i), (5.11.1)–(5.11.4)](https://dlmf.nist.gov/5.11.i),
applies at z=1/4+iy/2 in |arg z|<=pi/2, within a fixed sector
|arg z|<=pi-delta. It gives theta(y)=vartheta(y)+O(1/y).
Changing the phase in (4) costs at most
C*y^(-1)*sum_{n<=M(y)}n^(-1/2)=O(y^(-3/4)). Therefore
\[
 Z(y)=2\sum_{n\leq M(y)}n^{-1/2}
                  \cos(\vartheta(y)-y\log n)+O(y^{-1/4}). \tag{5}
\]
No derivative of a Stirling remainder is taken. All these error bounds
are uniform on [X/2,2X] once X is sufficiently large.

Finally use Fourier inversion on Schwartz functions from Tao,
[*245C, Notes 2: The Fourier transform*, 6 April 2009,
Definition 32, Example 33, Exercise 30 and (10)–(11)](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/).
Below the convention is explicitly rescaled from the source's 2*pi
convention. Only inversion and differentiation-to-decay are imported;
uniformity for this particular multiplier is proved next. These sources
do not directly state (1)–(2), which is why the specialization is needed.

### Ordinary floor and a uniform real kernel

C019l (4)–(5) give d asymptotic in scale to X^2*q^2,
t*q^2<=C, ell=q+O(1) and N(Y) asymptotic in scale to sqrt(X),
uniformly on J. Put M(Y)=floor(sqrt(Y/(2*pi))). The difference of
the quantities before taking their floors is nonnegative and at most
\[
 \frac{Y^2/(32d)}{\sqrt{Y/(2\pi)}}
       =O(q^{-2}X^{-1/2})<1.                                \tag{6}
\]
Thus N(Y)-M(Y) is either zero or one, including equality at every
entry. Any extra index is asymptotic in scale to sqrt(X). Since its
heat weight has bounded modulus by C019l (5)/(8), its contribution
to V is O(X^(-1/4)). Let V_0 be V with just its floor replaced by M:
\[
 V(Y)=V_0(Y)+O(X^{-1/4})\quad(Y\in J).                     \tag{7}
\]

Fix once and for all a real even C-infinity function chi with compact
support in [-2,2] that equals one on [-1,1]. For real xi define
\[
 m_Y(\xi)=\chi(\xi)
       \exp\{t(Y)q^2\xi^2/4-\pi^2t(Y)/64+i\pi t(Y)q\xi/8\},
\]
\[
 K_Y(u)=\frac1{2\pi}\int_{\mathbb R}m_Y(\xi)e^{-iu\xi}\,d\xi,
 \qquad m_Y(\xi)=\int_{\mathbb R}K_Y(u)e^{iu\xi}\,du.     \tag{8}
\]
The last identity is the imported inversion formula. All coefficients
t*q^2, t*q and t are bounded, and the support is fixed. Differentiating
the displayed exponential up to order five shows that every resulting
polynomial coefficient is bounded on that support. The fixed cutoff
and its first five derivatives are bounded as well. Hence
\[
 \|\partial_\xi^j m_Y\|_{L^1}\leq C_j\quad(0\leq j\leq5),
 \qquad |K_Y(u)|\leq C(1+|u|)^{-5}=:k(u).                 \tag{9}
\]
Indeed the j=0 bound handles |u|<=1, and five integrations by parts,
with vanishing boundary terms for the smooth compact support, handle
|u|>1. In particular integral k, integral u^2*k, and
U^4*integral_{|u|>U}k for U>=1 are bounded independently of Y,d.
This is one common pointwise envelope, not just individual L1 norms.
Also m_Y(-xi)=conjugate(m_Y(xi)), so K_Y is real.

For n<=M(Y), 0<=v_n(Y)/q<=ell(Y)/(2q)<1 at a common onset.
Thus chi is exactly one at both relevant frequencies. Put
\[
 W(Y,u)=2\sum_{n\leq M(Y)}n^{-1/2}
   \cos(\vartheta(Y)-Y\log n+u v_n(Y)/q).
\]
Inversion in (8) on the two conjugate exponential branches gives
the exact identity
\[
 V_0(Y)=\int_{\mathbb R}K_Y(u)W(Y,u)\,du.                 \tag{10}
\]
In particular the positive branch is multiplied by
exp(t*v_n^2/4-pi^2*t/64+i*pi*t*v_n/8), the exact heat amplitude
and phase in V; the negative branch is its conjugate. The sum is finite
and |W(Y,u)|<=C*X^(1/4) for every real u, so the integral is absolute.
No globally growing Gaussian multiplier has been used.

### Translated phase, every cutoff, and the full tail

Set U=X^(1/8). For |u|<=U let s=u/q and y=Y+s. Uniformly for Y in J,
y lies in [X/2,2X] eventually. Since vartheta'(Y)=ell(Y)/2 and
vartheta''(r)=1/(2r), Taylor's integral remainder gives
\[
 |\vartheta(Y+s)-\vartheta(Y)-s\ell(Y)/2|
       \leq C s^2/X.                                      \tag{11}
\]
This holds for both signs of s; only the explicit elementary phase is
differentiated. The phase in W is precisely
vartheta(Y)+s*ell(Y)/2-(Y+s)*log n. Summing the cosine error from
(11) over any common set of indices costs at most C*s^2*X^(-3/4).

The difference between sqrt(y/(2*pi)) and sqrt(Y/(2*pi)) has
absolute value at most C*|s|/sqrt(X)<=C*X^(-3/8)/q<1. Consequently
|M(y)-M(Y)|<=1, including when either argument is exactly an entry.
Every differing index is asymptotic in scale to sqrt(X), so replacing
the frozen floor by the translated ordinary floor costs O(X^(-1/4)).
Together with (5) this proves
\[
 |W(Y,u)-Z(Y+u/q)|
     \leq C X^{-1/4}+\frac{C u^2}{q^2X^{3/4}}
              \quad(|u|\leq U,\ Y\in J).                 \tag{12}
\]
Thus the deformed floor, the original ordinary floor and the translated
ordinary floor have all been paid, pointwise and at equality.

For the omitted |u|>U part of (10), use the finite frozen sum, not a
claim about remote zeta values. The full absolute cost is
\[
 \int_{|u|>U}|K_Y(u)W(Y,u)|\,du
       \leq C X^{1/4}U^{-4}=C X^{-1/4}.                   \tag{13}
\]
On the retained part, integrate (12) against (9); the zeroth and second
moments of k pay its two terms. Combining (7), (10), (12), (13) gives
\[
 V(Y)=\int_{|u|\leq U}K_Y(u)Z(Y+u/q)\,du+O(X^{-1/4})
                       \quad(Y\in J),                    \tag{14}
\]
with a uniform absolute constant. This representation has no unpaid
tail or assumption about the zeta function outside the nearby band.

### First absolute moment with the moving kernel

Use the triangle inequality and the common envelope (9) in (14).
Tonelli on the resulting nonnegative measurable integrand gives
\[
 \int_J|V(Y)|\,dY
 \leq\int_{|u|\leq U} k(u)
                \int_J|Z(Y+u/q)|\,dY\,du+CBX^{-1/4}.     \tag{15}
\]
For each fixed u in this range, the translated interval J+u/q is
contained in [X/2,2X]. Therefore its inner integral is at most
\[
 \int_{X/2}^{X}|\zeta(1/2+iy)|\,dy+
 \int_X^{2X}|\zeta(1/2+iy)|\,dy
       \leq C X q^{1/4}.                                  \tag{16}
\]
Here (3) is applied at k=1/2 with A=X/2 and A=X; both exceed 10
eventually, and their logarithms are comparable to q. Integrating the
fixed k(u) envelope proves (1), since B is a fixed positive multiple
of X. Specifically the ratio to B*sqrt(q) is O(q^(-1/4)), which
tends to zero. A Y-dependent kernel norm alone would not have
justified (15)–(16); (9) is the uniform domination used here.

### The sufficient remainder bound cannot persist

Since D and D+h are subsets of J, (1) gives an absolute C_1>=1 with
\[
 \int_D\sqrt{E(Y)}\,dY
 \leq\int_D(|V(Y)|+|V(Y+h)|)\,dY\leq C_1Bq^{1/4}.        \tag{17}
\]
Let G be the subset of D where sqrt(E)<=4*C_1*q^(1/4).
Markov's inequality applied to (17) gives |D\G|<=B/4. For sufficiently
large d, h<=B/2, so |D|>=B/2 and |G|>=B/4. On G we have
E<=16*C_1^2*sqrt(q). Using C019n's pointwise H<=-kappa*q on
the entire D, and then restricting the nonnegative integral, yields
\[
 -I_H\geq\kappa q\int_D\frac{dY}{1+E(Y)}
 \geq\frac{\kappa q B}{4(1+16C_1^2\sqrt q)}
 \geq\frac{\kappa}{4(1+16C_1^2)}B\sqrt q
       =c_*B\sqrt q,                                     \tag{18}
\]
where the last inequality uses q>=1. The constant c_*>0 is independent
of d. For all real V,V_+, 2*|V*V_+|<=E implies |I_V|<=|D|/2<=B/2.
The exact, absolutely integrable decomposition in C019n (5)/(9)
therefore gives
\[
 \mathcal R=I_V-I_H\geq-B/2+c_*B\sqrt q.                  \tag{19}
\]
This proves (2), and its ratio to B tends to positive infinity.
For any fixed c_D>0 it exceeds c_D*B/2 once
sqrt(q)>(1+c_D)/(2*c_*). No sign information on I_V was used.

### Qualifications and continuation

All onsets used above are a finite collection of requirements on
d alone: the inherited scale/diagonal onsets, q>=1, h<=B/2,
ell/(2q)<1, both pre-floor differences less than one, the nearby-band
containment and validity of the ordinary asymptotics and moment theorem.
Their maximum is one existential integer onset, uniform in Y,u in
their stated domains. The proof is asymptotic, not an effective certificate.

The negative diagonal is too large to dominate the bounded total with
the proposed small upper bound on R. This is an informative obstruction
to that particular sufficient condition. It neither rules out negative
I_V nor proves (N). A different signed balance would need additional
input. Ordered sign samples, reciprocal root mapping, bulk separation,
all-degree Jensen hyperbolicity and L030–L032/C032a positivity remain
independent unresolved gaps. Existing stop evidence is preserved.

The first derivation did not claim an independent audit. The separate
audit1393 below checks precisely its representation (14) and
concentration/inequality directions in (17)–(19).

### Separate conceptual audit1393 — 17 November 2026

The unchanged SPECIALIZE assessment
`drafts/literature/2026-11-17-jensen-first-moment-obstruction-audit-1391.md`,
separately approved in recovery1392, covers this audit. Equations
(1)–(2) are retained with their stated hypotheses and existential
onset. No mathematical defect was found, and no stronger estimate
is claimed. This is verification of the existing local specialization,
not a new fractional-moment theorem or certified original discovery.
The source statements and proof-case assessment1389/review1390 are
reused; the present work checks their application, not their proofs.

**Exact inputs.** The printed phase, including -Y log n, agrees with
corrected C019n and C019l (8). C019l (4) gives X,q tending to infinity,
d comparable to X^2 q^2 and t q^2 bounded throughout J. No inherited
actual-Jensen approximation is needed to prove (1)–(2) for this
explicit V. Such an approximation is a separate downstream input.
The only diagonal premise used is corrected C019n (4), not a sign
claim for the full product. Its pointwise scope is justified by
C019l's uniform sum-to-integral proof: the derivative of
x^(-1)g_Y(log x) has absolute integral O(1), and the logarithmic
floor error is O(X^(-1/2)). C019n (12)–(13) therefore hold uniformly
at every Y, including entries. In its limiting integral the cosine
has one sign change at z=1/6 on [0,1/2]. Replacing its increasing
positive weight by the value at 1/6 increases the integrand on both
pieces. Thus H<=-2q/(3*pi)+O(log q)<=-q/(3*pi) eventually on all D.
This does not promote C019l's integrated correlation to a pointwise
full-product inequality.

**Multiplier sign, inversion and domination.** Fixing the cutoff once
and for all makes its derivative bounds absolute. If a=t q^2/4,
b=pi t q/8 and c=-pi^2 t/64, then m_Y=chi exp(a xi^2+i b xi+c).
The parameters a,b,c range over bounded sets, and |xi|<=2 on the
support. Every derivative through order five is bounded there by a
constant depending only on this fixed cutoff and the scale constants.
Consequently the five integrations by parts have zero boundary terms
and give the common pointwise majorant in (9). This checks a moving
family, not an inference from its separate L1 norms.

For 1<=n<=M(Y), n<=sqrt(Y/(2*pi)), hence
0<=v_n/q<=ell/(2q)<1. Both frequencies lie in the plateau of chi.
With A=vartheta(Y)-Y log n and xi=v_n/q, the integral of the two
exponential branches of W is

\[
 n^{-1/2}\{e^{iA}m_Y(\xi)+e^{-iA}m_Y(-\xi)\}
 =2a_n(Y)\cos\{A+\pi t(Y)v_n(Y)/8\}.
\]

Here m_Y(-xi) is the conjugate of m_Y(xi), and the Fourier convention
in (8) gives a real K_Y. The displayed identity checks the positive
quadratic heat sign and the linear phase sign together. Summing proves
(10) exactly. Inversion applies to this compactly supported smooth
multiplier; it makes no assertion about the uncut backward-heat
operator. Absolute integrability follows from the common majorant
and the finite-sum bound O(X^(1/4)).

**All floors, phase errors and the tail.** Write A=Y/(2*pi) and
delta=Y^2/(32d). The first pre-floor difference is exactly
delta/(sqrt(A+delta)+sqrt(A))=O(q^(-2)X^(-1/2)). It is nonnegative
and less than one. The possible single added index has size comparable
to sqrt(X); its bounded heat multiplier pays (7), even at equality.
On |u|<=U=X^(1/8), s=u/q obeys |s|/X=o(1). The whole segment
between Y and Y+s lies in [X/2,2X]. Its elementary phase has second
derivative 1/(2r), so (11) holds for either sign of s. The total phase
error over the common finite sum is at most C s^2 X^(-3/4).
The two ordinary pre-floor arguments differ by at most
C|s|/sqrt(X)<=C X^(-3/8)/q<1; their floors therefore differ by at
most one, in either direction and at all equalities. Again that term
costs O(X^(-1/4)). DLMF's ordinary approximation is used only at the
translated positive ordinate in the nearby band. Replacing theta
there by vartheta costs O(X^(-3/4)), within the displayed error in
(12); no derivative of its asymptotic remainder is invoked.

The retained error is bounded by
C X^(-1/4) integral k + C q^(-2)X^(-3/4) integral u^2 k,
which is O(X^(-1/4)). On the complement, only W is integrated:
X^(1/4) integral_{|u|>U} k <= C X^(1/4)U^(-4)=C X^(-1/4).
In particular no zeta estimate at distant ordinates is tacitly needed.
These are all errors in (14), including the initial deformed floor.
Their subsequent height integral is O(B X^(-1/4)), negligible compared
with both B q^(1/4) and the required B sqrt(q) threshold.

**Ordinary moment applicability and the moving average.** All finite
sums are measurable with only finitely many entry points on J. The
kernel depends smoothly on Y before the finite sum is inserted, and
its common majorant makes the triangle/Tonelli step (15) legitimate.
For a fixed u the translation has derivative one: q is fixed by d,
not recomputed at Y+u/q. Its interval is contained in [X/2,2X].
HRS Theorem 1 is used with the admissible exponent k=1/2 and the
two bases X/2 and X, both at least 10 eventually. Their logarithms
are comparable to q, while |Z|=|zeta| for the exact real Hardy
function. Thus (16) and (1) follow with one absolute constant; the
ratio of the resulting bound to B sqrt(q) is O(q^(-1/4)), tending
to zero. No new moment theorem, independence, nonvanishing or
probabilistic distribution law has entered this step.

**Concentration, signs and exact cancellation.** Both D and D+h
are contained in J, so (17) is valid with an absolute C_1>=1.
Markov bounds the complement of G by B/4. Combining this with
|D|=B-h>=B/2 gives |G|>=B/4, and on G,
1+E<=1+16 C_1^2 sqrt(q). The global inequality -H>=kappa q is
essential: it makes restriction of the nonnegative integral in
(18) legitimate. For A=16 C_1^2 and q>=1,
q/(1+A sqrt(q))>=sqrt(q)/(1+A). Thus (18) has the correct
direction and a positive constant independent of d.

The exact integrals are finite since their denominator is at least
one and their numerators are finite sums on a compact band. Pointwise
2|V V_+|<=E gives |I_V|<=|D|/2<=B/2 without any sign assumption.
Consequently R=I_V-I_H>=c_*B sqrt(q)-B/2. Its lower bound divided
by B tends to positive infinity and exceeds c_D/2 once
sqrt(q)>(1+c_D)/(2c_*), exactly as asserted. C019n's O(B/q)
actual-Jensen transfer is not part of this equality and cannot be
silently used to change its diagonal or remainder.

All comparisons require only finitely many lower bounds on d, uniform
in Y and in the retained u range, so one common existential onset
suffices. This audit supplies no effective value. It removes the
provisional status of the small-R obstruction, while preserving (N),
the full-product sign, quantitative real-root counts and actual-Xi
all-degree positivity as unresolved. The original origin/variation
stop and earlier exterior/bulk stops keep their own scopes.

## Mathlib

Full matching coverage is not checked. No formal theorem identifier
for the moving-time estimate (1), the remainder obstruction (2), or
the imported fractional zeta moment is asserted. Fourier inversion,
finite sums, integration, Tonelli and Markov inequalities would support
parts only. The mathematical sources above were assessed in review1390;
no new Mathlib availability or absence claim follows from this proof.
