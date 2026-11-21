# Lemma 901: the strict normalized-defect zero-set condition is equivalent to RH

## Hypotheses

Use the actual entire functions xi and f=Xi of L018, so
f(z)=xi(1/2+iz). Use precisely the full-line normalization of L898:
Phi(u)=K(|u|)/2, p=u+v, q=u-v, and

\[
 C_y(x)=\iint_{\mathbb R^2}p^2\operatorname{sinhc}(yp)
       \Phi(u)\Phi(v)\cos(xq)\,du\,dv,\qquad A_0(y)=C_y(0),
 \quad 0\leq y\leq\tfrac12.
\]

Here sinhc has its removable value 1 at zero. L898 supplies
0<A_0(y)<infinity and, for real x,y, the identity
P_y(x,y)=y C_y(x), where P(x,y)=|f(x+iy)|^2.
For real x and 0<t<1/4 define

\[
                 R_x(t)=\frac{C_{\sqrt t}(x)}{A_0(\sqrt t)}.
\]

The condition under examination is the following assertion, not a premise
assumed true:

\[
 (Z)\qquad \forall x\in\mathbb R\ \forall t\in(0,1/4),\quad
 C_{\sqrt t}(x)=0\ \Longrightarrow\ R'_x(t)<0.
\]

No simplicity hypothesis, exclusion of Xi zeros from (Z), endpoint
condition, or restriction on the real frequency x is imposed.

## Conclusion

Every R_x is continuously differentiable on (0,1/4), and

\[
                            (Z)\quad\Longleftrightarrow\quad\mathrm{RH}.
\]

More precisely, any hypothetical zero z_0=x_0+iy_0 of f with
0<y_0<1/2 satisfies C_{y_0}(x_0)=0 and

\[
 R'_{x_0}(y_0^2)
       =\frac{|f'(z_0)|^2}{y_0^2 A_0(y_0)}\geq0.                 \tag{1}
\]

The value is strictly positive at a simple zero and exactly zero at a
zero of any multiplicity at least two. Under RH, C_y(x)>0 for every
real x and 0<y<1/2, so (Z) holds vacuously.

This is a logical obstruction to using (Z) as an independently available
input. It proves neither side of the equivalence and supplies no actual
theta sign or progress toward resolving L030-L032/C032a. The calculation
is a local specialization of known analytic and monotonicity tools; no
originality beyond the inspected sources is claimed.

## Proof

### Regularity and the exact derivative at a zero

Since f is entire, P is smooth in the two real variables x,y. On the
open interval y>0, the L898 identity gives C_y(x)=P_y(x,y)/y. In
particular both C_y(x) and A_0(y)=P_y(0,y)/y are smooth there.
Their real positive normalizer and the smooth map t -> sqrt(t) show
that R_x is smooth on (0,1/4). Thus differentiability here follows
from the analytic defect identity, not merely from L899's Lipschitz
bound. No complex nonvanishing of A_0 is required.

Fix x and write g(y)=f(x+iy). Holomorphic differentiation gives
g'(y)=i f'(x+iy) and g''(y)=-f''(x+iy). Ordinary real differentiation
of P=g conjugate(g) gives

\[
 \begin{split}
 P_y(x,y)&=2\operatorname{Re}\bigl(i f'(x+iy)\overline{f(x+iy)}\bigr),\\
 P_{yy}(x,y)&=2|f'(x+iy)|^2
       -2\operatorname{Re}\bigl(f''(x+iy)\overline{f(x+iy)}\bigr).
 \end{split}                                                   \tag{2}
\]

At f(z_0)=0 these are respectively 0 and 2|f'(z_0)|^2. Thus
C_{y_0}(x_0)=0. To track both quotient terms, put A(y)=A_0(y).
For y=sqrt(t)>0 the chain and quotient rules give

\[
 R'_x(t)=\frac1{2y}
 \left(\frac{P_{yy}(x,y)}{yA(y)}
       -\frac{P_y(x,y)}{y^2 A(y)}
       -\frac{P_y(x,y)A'(y)}{yA(y)^2}\right).                  \tag{3}
\]

At z_0, both terms containing P_y vanish; substituting (2) yields
(1). In particular no logarithmic division by f was made at its zero.
For a nonzero holomorphic function a simple zero has f'(z_0)!=0,
whereas every higher-multiplicity zero has f'(z_0)=0, by the analytic
Taylor theorem ([NIST DLMF 1.10.1](https://dlmf.nist.gov/1.10.E1),
the standard input already assessed for L900). Here f is not identically zero, since L018 gives
f(i/2)=xi(0)=1/2. These alternatives cover every possible zero
multiplicity. Strict negativity in (Z) fails in both cases.

### The condition excludes all off-line zeros

Suppose (Z) holds and RH fails. L018 identifies a nonreal zero of f,
preserves its multiplicity, and puts every zero in |Im z|<1/2;
the two boundary lines are excluded there. Reality of f gives
conjugate zeros with the same multiplicities. Hence one can choose
z_0=x_0+iy_0 with 0<y_0<1/2. Its squared height lies in exactly
the required open interval. Equation (1) contradicts (Z) at that
point. Thus every zero of f is real, which is RH by L018.
This argument requires neither a first crossing nor boundary data.

### The converse uses the strict product sign under RH

The imported source is Yuri Matiyasevich, Filip Saidak and Peter
Zvengrowski, *Horizontal Monotonicity of the Modulus of the Riemann
Zeta Function and Related Functions*,
[arXiv:1205.2773v1](https://arxiv.org/pdf/1205.2773v1), 12 May 2012,
Section 2, Lemma 2.1 (printed p.3) and the complete proof of
Theorem 1.1 (printed p.4). The latter is the Sondow-Dumitrescu theorem.
Its product argument explicitly establishes the differential conclusion

\[
 \operatorname{Re}\frac{\xi'(s)}{\xi(s)}>0
 \quad\text{if }\operatorname{Re}s>\sigma_0
 \text{ and every zero of xi has real part at most }\sigma_0.    \tag{4}
\]

This imports the source's convergent conjugate-paired logarithmic
product formula and its strict sign. We do not reprove Hadamard's
product or infer (4) just from strict monotonicity. The source's xi
normalization on printed p.2 agrees with L018 because
Gamma(1+s/2)=(s/2)Gamma(s/2), with the entire continuations understood.
Its Theorem 1.1 has no ordinate cutoff; the |Im s|>=8 hypothesis
of its separate zeta/eta results is not part of this input.

Assume RH only for this converse. Take any real x and 0<y<1/2,
and set s=1/2+y-ix. The functional equation in L018 gives

\[
       f(x+iy)=\xi(1/2-y+ix)=\xi(1/2+y-ix)=\xi(s).
\]

Under RH, xi has no zero at s, and (4) applies with sigma_0=1/2.
Differentiating in y, which has ds/dy=1, now gives

\[
        P_y(x,y)=2|\xi(s)|^2
                    \operatorname{Re}\frac{\xi'(s)}{\xi(s)}>0.
\]

Both the nonzero modulus and the logarithmic-derivative sign are
justified under this direction's explicit RH assumption. It follows
that C_y(x)=P_y(x,y)/y>0. Therefore no antecedent in (Z) occurs,
and (Z) is true. Real zeros of Xi, of any multiplicity and at any
real x, create no exception because every evaluated y is positive.
Neither t=0 nor t=1/4 is claimed or needed. This completes both
directions. No sign of a second derivative was inferred from
monotonicity. The ready assessment's restriction to strict negativity
is retained; a weak or zero-excluding condition is a different target.

### Scope and recorded failures

Retire (Z) as an independent input unless a materially new
theta-specific estimate proves it without assuming an equivalent
zero-location or global-defect condition. This does not forbid such
future work or prove that (Z) is false. L312's different conditional
law and C900a's displayed absolute-budget obstruction are contrasts,
not mathematical inputs to the equivalence. L899/L900 supply useful
regularity bounds elsewhere; their quantitative constants are not
used here. The direct local inputs are L018 and L898.

## Mathlib

Full matching coverage has not been checked; availability is unknown.
Supporting library results for holomorphic differentiation, Taylor
multiplicity and the completed-xi logarithmic product have not been
checked. This is an informal proof audit, with no formal or numerical
certificate. The primary theorem and analytic differentiation supply
the proof; no experiment is used as verification.
