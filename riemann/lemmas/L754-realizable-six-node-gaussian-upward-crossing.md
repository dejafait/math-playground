# L754: A compact neutral six-node Gaussian sum crosses upward

## Hypotheses

This is a finite synthetic spectral model, not the Xi zero multiset.
Use the complete multiset

\[
 Z_6=\{\tfrac12,-\tfrac12,
          1+\tfrac i4,1-\tfrac i4,-1+\tfrac i4,-1-\tfrac i4\},
 \qquad m_z=1\quad(z\in Z_6).                         \tag{1}
\]

For f in C_c^infinity(R;C) put

\[
 F(z)=\int_{\mathbb R}f(x)e^{-izx}\,dx,
 \quad F^\#(z)=\overline{F(\bar z)},
 \quad S_f(\tau)=\sum_{z\in Z_6}m_z e^{-2\tau z^2}F(z)F^\#(z).
                                                               \tag{2}
\]

The required test conditions are

\[
 \int e^{x/2}f(x)\,dx=\int e^{-x/2}f(x)\,dx=0.          \tag{3}
\]

No support interval or norm bound is prescribed, and no symmetry or
real-valuedness of f is assumed. The positive-window parameters are
H=3/4, r=1/2, a=1, b=1/4. All sums below include all six nodes
with their stated multiplicities; there is no omitted model spectrum.

The imported result is J.-F. Burnol, *The explicit formula in simple
terms*, [arXiv:math/9810169v2, 22 November 1998, printed pp.4-6](https://arxiv.org/pdf/math/9810169v2#page=5).
The unnumbered finite-interpolation argument at the start of
“Weil's positivity criterion and stochastic processes,” pp.5-6,
states that for any finite distinct complex s_j and arbitrary complex
c_j there is g in C_c^infinity((0,infinity);C) with

\[
 \widehat g(s_j)=c_j,
 \qquad \widehat g(s)=\int_0^\infty g(u)u^s\,\frac{du}{u}.
                                                               \tag{4}
\]

The Mellin convention is on p.4; the p.6 note includes adding
vanishings at 0 and 1. This finite statement is imported without
reproof; its later infinite-zero argument is not needed. The saved
EXPLORE assessment is
`drafts/literature/2026-11-04-neutral-gaussian-six-node-crossing.md`.
The work below is a REPRODUCTION/standard specialization, without
a claim of originality. L753 and C753a provide comparison conventions
only: no actual-Xi theorem is a mathematical premise of this model.

## Conclusion

There exists one fixed compact smooth complex f satisfying (3),
F(r)=1, and

\[
 S_f(\tau)=2e^{-\tau/2}-4e^{-15\tau/8}\cos\tau
       =2e^{-\tau/2}\bigl(1-2e^{-11\tau/8}\cos\tau\bigr)
 \quad(\tau\ge0).                                      \tag{5}
\]

This real analytic function has S_f(0)=-2 and a unique zero tau_*
in (0,pi/2), characterized exactly by

\[
 2e^{-11\tau_*/8}\cos\tau_*=1.
                                                               \tag{6}
\]

It is negative on [0,tau_*), and

\[
 S_f'(\tau_*)
   =2e^{-\tau_*/2}\bigl(\tfrac{11}{8}+\tan\tau_*\bigr)>0.
                                                               \tag{7}
\]

It also satisfies the all-time eventual bound

\[
 S_f(\tau)\ge e^{-\tau/2}>0
 \quad\text{for }\tau\ge\tfrac8{11}\log4.               \tag{8}
\]

Every spectral analogue specified in the assessment for C753a is
satisfied: conjugation and negation symmetries with orbit-consistent
positive multiplicities, the open strip, no zero node, reciprocal-square
summability, a complete real window, strict separation, and a visible
real node. Exact neutrality and the reflected products are realized
by the same f, rather than assigned as independent coefficients.

Consequently these abstract data do not imply
S_f'(tau)<=C_f,T max{-S_f(tau),0} on its nonpositive set, even
for this fixed test and a fixed T=pi/2 with any finite nonnegative
constant C_f,T. This stops only an abstract backward-sign comparison.
There is no zeta arithmetic explicit formula for (1) asserted here,
no negative actual-Xi Weil value, and no RH conclusion. The separate
step-338 audit in Section 5 accepts the statement without a mathematical
correction; it does not strengthen the earlier negative result.

## Proof

### 1. Import finite interpolation and pay the additive convention

Prescribe the eight Fourier values in the table. The second column
lists the corresponding distinct Mellin nodes; all eight are different.

| z | s=1/2-iz | prescribed F(z) |
|---|---|---|
| 1/2 | 1/2-i/2 | 1 |
| -1/2 | 1/2+i/2 | 1 |
| 1+i/4 | 3/4-i | 1 |
| 1-i/4 | 1/4-i | -1 |
| -1+i/4 | 3/4+i | 1 |
| -1-i/4 | 1/4+i | -1 |
| i/2 | 1 | 0 |
| -i/2 | 0 | 0 |

Apply (4) to exactly these nodes and values, obtaining g, and set

\[
 f(x)=e^{x/2}g(e^x).
\]

If supp(g) is contained in [A,B] with 0<A<B<infinity, then
supp(f) is contained in [log A,log B]. Composition and multiplication
by smooth functions show f is smooth; it is compactly supported.
Using u=e^x in the absolutely convergent compact integral gives

\[
 F(z)=\int_{\mathbb R}g(e^x)e^{(1/2-iz)x}\,dx
     =\widehat g(1/2-iz).                               \tag{9}
\]

Thus this single f realizes the entire table. In particular

\[
 \int e^{x/2}f(x)\,dx=F(i/2)=\widehat g(1)=0,
 \qquad
 \int e^{-x/2}f(x)\,dx=F(-i/2)=\widehat g(0)=0.
                                                               \tag{10}
\]

The integral defining F is entire, since on every compact z-set all
its z-derivatives are dominated on the fixed compact x-support.
Reflected conjugation therefore defines the entire F^# in (2).
This does not impose F(bar z)=overline(F(z)) or any symmetry of f.
No quantitative support or norm claim follows from the interpolation
input or is used here.

### 2. Complete geometry, multiplicities, and reflected products

Negation and conjugation each permute (1), preserving m_z=1.
Every node has |Im z|<=1/4<1/2, and no node is zero. The complete
reciprocal-square sum is

\[
 \sum_{z\in Z_6}m_z|z|^{-2}
   =2\cdot4+4\cdot\tfrac{16}{17}=\tfrac{200}{17}<\infty.
                                                               \tag{11}
\]

The inequalities for the approved parameters are

\[
 H=\tfrac34>\tfrac12,
 \quad0<r=\tfrac12<H<a=1,
 \quad0<b=\tfrac14<\tfrac12,
 \quad r^2=\tfrac14< H^2-\tfrac14=\tfrac5{16}.          \tag{12}
\]

The whole window |Re z|<=H consists exactly of +/-r, both real;
no node lies on its boundary. Also F(r)=1 is nonzero. These checks
cover the complete model, not a sampled sublist of a larger spectrum.

At either real node the table gives F(z)F^#(z)=1. At 1+i/4
the product is 1 times overline(-1)=-1, and at 1-i/4 it
is -1 times overline(1)=-1. The two nodes -1+i/4 and -1-i/4
give respectively the same products 1 times overline(-1) and
-1 times overline(1). Thus all four nonreal coefficients are -1,
with no omitted reflected factor. In general
F(bar z)F^#(bar z)=overline(F(z)F^#(z)); conjugate pairing is
therefore consistent. Each assigned coefficient is nonzero.

For z=+/-r, z^2=1/4. Two quartet nodes have
z^2=15/16+i/2, and two have z^2=15/16-i/2. Substituting all
six terms into (2) proves (5), including its reality. In particular
the signs at nonreal nodes are not replaced by modulus squares.
The finite sum is real analytic in real tau, so no convergence,
termwise differentiation or infinite-time limit interchange is needed.

### 3. A transverse upward crossing and a permanent later anchor

Let q(tau)=2e^{-11tau/8}cos(tau). On [0,pi/2] it satisfies

\[
 q(0)=2,\quad q(\pi/2)=0,\qquad
 q'(\tau)=-2e^{-11\tau/8}
       \bigl(\tfrac{11}{8}\cos\tau+\sin\tau\bigr)<0.
                                                               \tag{13}
\]

Strict negativity holds also at both endpoints. The intermediate
value theorem and strict monotonicity give exactly one tau_* in
(0,pi/2) satisfying (6), with q>1 before it and q<1 afterwards
within this interval. Formula (5) proves S_f(0)=-2 and the asserted
negative interval. Differentiating (5) at q(tau_*)=1 gives

\[
 S_f'(\tau_*)=-2e^{-\tau_*/2}q'(\tau_*).
\]

Since cos(tau_*)>0, (6) changes (13) at the root into
q'(tau_*)=-(11/8+tan(tau_*)), proving the strictly positive
formula (7). The exact defining equation and interval prove existence
and transversality; a numerical approximation to the root is unnecessary.

For every tau>=0, cos(tau)<=1 and (5) yield

\[
 S_f(\tau)\ge2e^{-\tau/2}(1-2e^{-11\tau/8}).            \tag{14}
\]

If tau>=8log(4)/11 the last parenthesis is at least 1/2,
proving (8) for every such time, regardless of subsequent oscillations.

For completeness the weaker window-based anchor has exactly C753a's
spectral constants. Write alpha=H^2-1/4=5/16,
beta=r^2=1/4, delta=alpha-beta=1/16. The chosen visible-node
coefficient is c_*=1 and the full complementary absolute coefficient
sum is B_H=4. Since each quartet node has Re(z^2)=15/16>alpha,
directly retaining one real term and bounding all four others gives

\[
 S_f(\tau)\ge e^{-\tau/2}(1-4e^{-\tau/8})
       \ge\tfrac12e^{-\tau/2}>0
 \quad(\tau\ge8\log8).                                 \tag{15}
\]

This verifies the anchor analogue without applying an actual-Xi
corollary to a synthetic multiset. The sharper bound (8) is optional
additional evidence within the same finite model.

### 4. What the crossing rules out

Set T=pi/2. At tau_*, the proposed negative-side comparison has
right side C_f,T max{-S_f(tau_*),0}=0, whereas (7) makes its
left side strictly positive. Thus no finite C_f,T>=0 works on
the nonpositive set including its boundary. This is a counterexample
to sufficiency of the retained abstract hypotheses for the full
proposed inequality; it does not replace that inequality by a test
only at zeros. Indeed it also fails on the strictly negative side
for every fixed finite C_f,T: as tau increases to tau_* from below,
-S_f(tau) tends to zero while S_f'(tau) tends to (7)>0.
The same argument excludes a locally bounded comparison coefficient
near the crossing, but says nothing about singular coefficients.

The finite-spectrum model lacks the actual zeta arithmetic
identity. Neither L753's complete prime-power pairing nor the actual
Xi spectrum is supplied by finite interpolation. Hence the result
leaves the actual-Xi negative-side estimate, all-test visibility,
infinite-spectrum control and mixed positivity unresolved. It parks
this abstract comparison mechanism; L751/L752's different stops remain
unchanged. A later arithmetic-specific approach would require a
materially new input, not just the spectral anchor again.

### 5. Independent bounded audit, 4 November 2026 (step 338)

This audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-11-04-neutral-gaussian-six-node-crossing-audit.md`.
Burnol's finite interpolation is a named import, with the exact version,
Mellin convention and printed pages specified in the hypotheses. Its
previously inspected proof coverage is reused; no source reproof or
infinite-zero interpolation is needed. The audit checks the entire
finite specialization, rather than a numerical preview.

**Eight evaluations and the single test.** The affine map z -> 1/2-iz
is injective. Its images at the two real nodes are 1/2-i/2 and
1/2+i/2; at the four quartet nodes, in table order, they are
3/4-i, 1/4-i, 3/4+i, 1/4+i; at i/2 and -i/2 they are 1 and 0.
The six nonreal Mellin nodes and the two real Mellin nodes are all
distinct, so the imported finite theorem permits every prescribed
value simultaneously. A compact subset of (0,infinity) lies in some
[A,B] with 0<A<B; the substitution f(x)=e^(x/2)g(e^x) therefore
gives a smooth compactly supported complex test. Directly substituting
u=e^x gives (9), with the minus sign in -iz unchanged. Hence
F(i/2)=integral e^(x/2)f(x)dx=0 and
F(-i/2)=integral e^(-x/2)f(x)dx=0. Both neutral conditions and F(r)=1
hold for this same f. No prescribed support size, test norm, reality
or evenness is part of the theorem or the claim. Compact support also
pays entirety of F by dominated differentiation on every compact
z-set, and reflected conjugation makes F^# entire.

**Geometry and every reflected factor.** Negation exchanges the two
real nodes and exchanges quartet nodes in pairs; conjugation fixes
each real node and exchanges the upper and lower nodes at each real
part. All multiplicities equal one. The strip is strict since the
only imaginary parts are 0 and +/-1/4. The squared moduli are 1/4
(twice) and 17/16 (four times), giving 8+64/17=200/17 in (11).
Only +/-1/2 belong to |Re z|<=3/4, including its boundary; neither
lies on that boundary. The required strict separation is
1/4<9/16-1/4=5/16. There is no zero node, omitted model tail or
invisible retained anchor. At the two real nodes the reflected products
are 1. In the quartet's table order they are respectively
1*overline(-1), (-1)*overline(1),
1*overline(-1), (-1)*overline(1), all equal to -1.
Conjugation, rather than an unsupported symmetry of f, supplies these
products. Thus replacing them by modulus squares would change the model.

**Exact whole sum and crossing.** The squared nodes are 1/4 twice,
15/16+i/2 twice, and 15/16-i/2 twice. Their full weighted sum is
therefore 2e^(-tau/2)-2e^(-15tau/8)e^(-i tau)
-2e^(-15tau/8)e^(i tau), exactly (5). In particular its realness
does not require f real. In (13), both cosine and sine are nonnegative
on [0,pi/2], and they never vanish together, so q' is strictly negative
including the endpoints. Its endpoint values bracket 1, proving the
unique root in this interval by the intermediate value theorem.
Before it, q>1 and S_f<0. At the root, differentiating the product
in (5) removes the derivative of e^(-tau/2) because 1-q=0.
The root equation gives -q'=11/8+tan(tau_*), yielding (7) with
the asserted strictly positive sign. Every differentiation is of a
finite real analytic sum; no limiting or summability hypothesis is hidden.

**Anchors at every later time.** For tau>=8log(4)/11 one has
e^(-11tau/8)<=1/4. Since cos(tau)<=1 at every real time, (14)
gives S_f(tau)>=e^(-tau/2), including at the threshold, without a
restriction to the first oscillation. For the weaker window-based
bound, alpha=5/16, beta=1/4, delta=1/16 and B_H=4. Retaining
one of the two positive real terms and using
Re(z^2)=15/16>=alpha for each complementary node gives
S_f>=e^(-tau/2)(1-4e^(-tau/8)). At tau>=8log8 the bracket is
at least 1/2, proving (15), including its threshold. These are direct
finite-model checks of C753a's spectral analogues, not an application
of C753a's actual-Xi arithmetic identity to this multiset.

**Comparison and exact scope.** The root lies strictly inside
[0,T] for T=pi/2. There S_f=0 and S_f'>0, so a finite comparison
constant cannot satisfy the stated inequality on the closed nonpositive
set. If only S_f<0 is tested, take times increasing to tau_*:
the right side tends to zero for any fixed finite constant while the
left tends to the positive value (7). Continuity gives the same
failure for a locally bounded coefficient. No claim about singular
coefficients follows. Conversely, no arithmetic explicit formula,
actual-Xi negative value, infinite-spectrum realization or all-test
visibility is established. Those remain independent missing inputs.
The empty L754 row in DAG.md is correct: Burnol is the direct external
input, all model conditions are checked here, and L753/C753a are only
conventions and scope contrasts. There are no new local dependencies.

The audit accepts all conclusions as written and finds no mathematical
correction. It verifies the previously recorded obstruction, without
establishing a new estimate or a result beyond the source-based finite
specialization. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage of Burnol's finite compact-test interpolation
or this complete finite-model statement has not been checked. There
is no absence claim. The existing source assessment records scalar
comparison support in
[Mathlib.Analysis.ODE.Gronwall](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/ODE/Gronwall.html),
including `le_gronwallBound_of_liminf_deriv_right_le`, which requires
a derivative inequality; no such input is used or proved here.
The specialization above uses the imported interpolation theorem,
elementary finite sums, differentiation and the intermediate value
theorem, with the exact inequalities written out.
