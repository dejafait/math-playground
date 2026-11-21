# Lemma 885: actual conjugate arc kernels have local negative product sectors

## Hypotheses

Retain L847's actual entire function, with its real positive coefficients,

\[
 G(z)=\tfrac18\xi(\tfrac12+\tfrac{\sqrt z}{2})
       =\sum_{n\geq0}a_nz^n,\qquad r=(a_0,a_1,a_2).
\]

Assume L882's matched conjugate branch, including its smooth real
periodic stationary graph, nowhere-zero J, fixed fibers, zero-free
complementary radial interiors and two simple boundary zeros
zeta and conjugate(zeta), which are distinct. Retain all other zeros
and multiplicities. These are conditional hypotheses, not assertions
that such a zero pair or graph exists. The calculation below uses
only the actual entire G, the simple nonreal pair and L883's exact
fixed-lift primitives. It adds no disk, symmetry, sector, convexity,
product-graph or sign hypothesis.

Write sigma=rho*exp(i*theta) for the upper member of the pair, where
rho>0 and 0<theta<pi. Use the increasing lifts theta, 2pi-theta and
theta+2pi. With L883's H_j, set

\[
 v=-i\{H(\overline\sigma)-H(\sigma)+i(2\pi-2\theta)r\},
 \quad w=2\pi r-v,
\]
\[
 S(x,y)=x_0y_2-2x_1y_1+x_2y_0,\qquad
 \alpha=S(v,v),\quad\beta=S(v,w),\quad\gamma=S(w,w).
                                                        \tag{1}
\]

If L884 originally names the lower member zeta, this convention
exchanges v and w and hence alpha and gamma; beta is unchanged.
Thus the disjunction alpha*beta>=0 or gamma*beta>=0 is unchanged.
No hypothesis on d=a1^2-a0*a2 is used, including its nonvanishing.

## Conclusion

For 0<=t<=pi put

\[
 k_j(t)=\operatorname{Re}\{\rho^{-j}e^{-ijt}G(\rho e^{it})\},
 \quad k=(k_0,k_1,k_2),\quad K(t,s)=S(k(t),k(s)).
\]

Then, with P=[0,theta] and N=[theta,pi], the actual vectors satisfy

\[
 w=2\int_P k(t)\,dt,\qquad v=2\int_N k(t)\,dt,
                                                        \tag{2}
\]
\[
 \alpha=4\int_{N^2}K,
 \quad\beta=4\int_{N\times P}K,
 \quad\gamma=4\int_{P^2}K.                              \tag{3}
\]

All polar terms and the full residue increments are included in (2).
Writing exp(-it)G(rho exp(it))=X(t)+iY(t), the exact paired kernel is

\[
 K(t,s)=\frac{2}{\rho^2}
 \{X(t)X(s)(\cos t\cos s-1)-Y(t)Y(s)\sin t\sin s\}.
                                                        \tag{4}
\]

Define the strictly positive number

\[
                    \kappa=2\sin^2\theta\,|G'(\sigma)|^2>0.
                                                        \tag{5}
\]

There is delta>0, smaller than min(theta,pi-theta), such that for
0<|t-theta|,|s-theta|<=delta, K(t,s) is strictly negative on the
same side of theta and strictly positive on opposite sides.
For 0<epsilon<=delta let

\[
 v_\epsilon=2\int_\theta^{\theta+\epsilon}k,
 \quad w_\epsilon=2\int_{\theta-\epsilon}^{\theta}k,
 \quad (\alpha_\epsilon,\beta_\epsilon,\gamma_\epsilon)
   =(S(v_\epsilon,v_\epsilon),S(v_\epsilon,w_\epsilon),
                                      S(w_\epsilon,w_\epsilon)).
\]

These are actual restricted arc integrals, not freely chosen vectors.
They obey the quantitative bounds

\[
 \alpha_\epsilon,\gamma_\epsilon
       \leq-\frac\kappa2\epsilon^4,
 \qquad\beta_\epsilon\geq\frac\kappa2\epsilon^4,
\]
\[
 \alpha_\epsilon\beta_\epsilon,
 \gamma_\epsilon\beta_\epsilon
       \leq-\frac{\kappa^2}{4}\epsilon^8<0.              \tag{6}
\]

Consequently each natural fourfold integral for alpha*beta and
gamma*beta from (3) has a strictly negative integrand on a nonempty
open box next to the boundary label. Pointwise nonnegativity of these
paired product kernels is impossible under the stated hypotheses.
The actual local signs agree with L884's required checkerboard.

This is an obstruction to that specific unsigned integral mechanism,
not a sign determination of either full product. Explicitly, put

\[
 R_\alpha(\epsilon)=\alpha\beta-\alpha_\epsilon\beta_\epsilon,
 \qquad R_\gamma(\epsilon)=\gamma\beta-\gamma_\epsilon\beta_\epsilon.
                                                        \tag{7}
\]

The sought disjunction requires at least one of

\[
 R_\alpha(\epsilon)\geq-\alpha_\epsilon\beta_\epsilon,
 \qquad
 R_\gamma(\epsilon)\geq-\gamma_\epsilon\beta_\epsilon,
                                                        \tag{8}
\]

whose respective right sides are at least kappa^2*epsilon^8/4.
These are exact signed complementary remainders, including mixed
local/nonlocal terms; neither is estimated here. Their possible
compensation is not ruled out. No actual branch, stationary graph,
sharp L868 bound, higher sign or Xi-positivity question is settled.
The independent audit of 7 November 2026 below accepts this conditional
calculation with precisely these local and remainder qualifications.

## Proof

### Covered attempt and imported standard tools

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-11-07-actual-conjugate-primitive-sign-test.md`.
It covers an actual-series or paired-arc sign test with all Laurent
and residue terms, including an informative obstruction to the
proposed representation. L847 gives the actual G; L882 gives the
conditional simple conjugate labels; L883 supplies the exact primitive
increments. L884's strict products are the comparison target, not a
positivity premise in the calculation.

The standard complex-analysis input is the one already checked and
specialized in L883: Jiří Lebl, *Guide to Cultivating Complex Analysis*,
v1.10, 5 November 2026,
[Theorem 4.4.2 and Proposition 4.4.3, pp104-108](https://www.jirka.org/ca/ca.pdf#page=104),
and [Theorem 4.3.3/Corollary 4.3.4, pp100-101](https://www.jirka.org/ca/ca.pdf#page=100).
Use compact Laurent convergence and its primitive with the residue
separated. Proposition 4.4.3's proof is an exercise in that source;
it is an imported stated standard result, not a read proof. L883
already verifies the actual H_j. The compact-circle bounds below
justify the new termwise integrations explicitly. No source is
imported as a product-sign theorem, and no Laurent theorem is reproved.

The following elementary bilinear calculation is necessary to test
the precise actual integrand left open by the sources. It is not a
claim of a new general theorem. POTENTIALLY_NEW records only that the
prior bounded comparison did not identify this exact obstruction;
it does not certify originality. The earlier free-vector, common-line
and count-only controls do not supply the actual kernel calculation.

### Lifts, circular representatives and every Laurent term

If the original first label is lower, the increment from it to the
upper label and the increment from the upper label back to it add
to 2pi*i*r by L883. Selecting the upper label first therefore
exchanges v,w exactly. Common changes of the real lift by 2pi change
neither increment. This proves the lift qualification after (1).

For the upper label, real coefficients and L883's full H_j series give

\[
 \begin{split}
 w_j&=2a_j\theta+
       2\sum_{\substack{n\geq0\\n\ne j}}
        a_n\rho^{n-j}\frac{\sin((n-j)\theta)}{n-j},\\
 v_j&=2a_j(\pi-\theta)-
       2\sum_{\substack{n\geq0\\n\ne j}}
        a_n\rho^{n-j}\frac{\sin((n-j)\theta)}{n-j}.
 \end{split}                                             \tag{9}
\]

Here the n<j terms are the finite polar part; none has been removed.
The n=j terms are exactly the residue increments for the two arcs.
In particular v+w=2pi*r componentwise, including when d=0.

On the whole circle the Taylor series for k_j is absolutely uniformly
convergent: its absolute majorant is
sum_n a_n*rho^(n-j)=rho^(-j)G(rho)<infinity. Thus

\[
          k_j(t)=\sum_{n\geq0}a_n\rho^{n-j}\cos((n-j)t)
                                                        \tag{10}
\]

may be integrated on either compact interval. For n!=j the integral
over [0,theta] is the sine quotient in (9); for n=j it is theta.
The full half-circle integral is pi*a_j, since n-j is an integer.
This proves (2), including every term in (9). Equivalently these
are the increasing circular arcs in the same lifted homotopy classes.
The circles need not bound zero-free disks or lie inside L882's
radial domains. Formula (9) needs only the primitive increments;
G zeros on or between comparison arcs are not poles of the forms.
No unproved zero-free contour deformation is used.

The k_j are smooth on [0,pi]. Bilinearity of S and Fubini for continuous
functions on compact rectangles prove all three formulas (3).

### Exact paired kernel at the simple actual zero

From the definition of X,Y,

\[
 k(t)=\bigl(X\cos t-Y\sin t,\ \rho^{-1}X,
                     \rho^{-2}(X\cos t+Y\sin t)\bigr).
                                                        \tag{11}
\]

Substitution in S cancels the two mixed X*Y terms and proves (4).
As a normalization check, its diagonal is exactly

\[
          K(t,t)=-2\rho^{-2}\sin^2t\,|G(\rho e^{it})|^2.
                                                        \tag{12}
\]

At t=theta, G(sigma)=0 and hence k(theta)=0. Differentiating
g(t)=exp(-it)G(rho exp(it)) at that point gives
g'(theta)=i*rho*G'(sigma). In differentiating (11), the terms
containing X(theta) or Y(theta) vanish. The same bilinear identity
as in (12), now with X',Y', consequently gives

\[
       S(k'(\theta),k'(\theta))
        =-2\rho^{-2}\sin^2\theta\,|g'(\theta)|^2
        =-\kappa<0.                                    \tag{13}
\]

Strictness uses both nonreality, sin(theta)>0, and simplicity,
G'(sigma)!=0. No assumption about the phase of G'(sigma) is needed.

Define b(t)=k(t)/(t-theta) off theta and b(theta)=k'(theta).
The integral formula
b(t)=integral_0^1 k'(theta+q*(t-theta)) dq proves continuity there.
By (13) and continuity of S, choose delta as in the conclusion so that

\[
 -\frac{3\kappa}{2}<S(b(t),b(s))<-\frac\kappa2
       \quad\text{if }|t-\theta|,|s-\theta|\leq\delta.
                                                        \tag{14}
\]

This is a local, label-dependent choice, with no uniform bound on
delta asserted. The exact factorization

\[
            K(t,s)=(t-\theta)(s-\theta)S(b(t),b(s))      \tag{15}
\]

proves the strict same-side and opposite-side signs. Other zeros
elsewhere are retained; only this neighborhood of a simple zero is
used, and (14) justifies its signs without a series truncation.

On either same-side epsilon square, (14)-(15) bound K above by
-(kappa/2)*|t-theta|*|s-theta|. On the opposite-side square they
bound K below by the positive counterpart. Each one-variable
integral of |t-theta| is epsilon^2/2. Multiplication by the factor 4
in (3), for these restricted vectors, gives the first line of (6).
Multiplying its strict opposite-sign bounds proves the second line.
In particular both local products are bounded away from the sought
nonnegative threshold for every fixed epsilon in this range.

### Full product integrands and the exact unestimated remainder

Using compact Fubini again,

\[
 \alpha\beta=16\int_{N^3\times P}
                  K(t_1,t_2)K(t_3,s)\,dt_1dt_2dt_3ds,
\]
\[
 \gamma\beta=16\int_{P^2\times N\times P}
                  K(s_1,s_2)K(t,s_3)\,ds_1ds_2dt ds_3.
                                                        \tag{16}
\]

Restrict all variables to their respective open epsilon intervals
adjacent to theta. The first factor in each integrand is negative
and the second positive by (15). Each box has positive four-dimensional
measure. Its integrated contribution, with the factor 16, is exactly
alpha_epsilon*beta_epsilon or gamma_epsilon*beta_epsilon, respectively,
and satisfies (6). This proves the pointwise-nonnegativity obstruction
for the natural product kernels, conditional on the actual label.
No numerical label, replacement G, or freely chosen period vector
has been used.

The rest of each compact fourfold domain has the exact signed integral
(7). Subtracting the local contribution proves the equivalence (8).
In particular an absolute upper bound on that remainder cannot supply
the required positive compensation. L882's radial-domain information
has not here been converted to such a signed lower bound. The local
negative sectors persist under those hypotheses; this does not prove
that their further consequences cannot enforce global compensation.

Thus the bounded direct nonnegative-kernel attempt stops. A future
sign proof would need a materially additional cancellation or domain
estimate, or a different representation; repeating local pairing,
conjugate reality or the full-turn total does not provide it.

### Independent audit, 7 November 2026

STEP_ID: 2026-11-07-l885-paired-kernel-audit-67. This REPRODUCTION
uses the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-07-l885-paired-kernel-audit.md`.
The full argument was checked against L847's actual entire G,
L882's matched-conjugate hypotheses, L883's audited fixed-lift
increments and L884's strict-product comparison. The previously
inspected Lebl inputs above are reused through L883, with the stated
exercise qualification; no new source theorem is imported.

**Lifts and residues.** For m=n-j!=0, conjugate endpoints give
the H_j increment

\[
 \frac{a_n\rho^m}{m}(e^{-im\theta}-e^{im\theta})
       =-2i\frac{a_n\rho^m\sin(m\theta)}m.
\]

The tracked logarithm increment on the increasing arc from theta to
2pi-theta is i(2pi-2theta). Multiplying their sum by -i gives
v_j in (9); subtracting from 2pi*a_j gives w_j. This calculation
includes m<0 and m=0 separately, so neither the finite polar part
nor the residue is lost. Starting with the lower label gives the
complementary increment T-A, not -A. Hence v,w exchange, alpha,gamma
exchange and beta is fixed. A common lift shift adds no increment.

For fixed rho>0, positivity and entirety give the finite circle
majorant rho^(-j)G(rho) for (10). Termwise compact integration is
therefore justified. For every nonzero integer m, including negative
m, the integrals of cos(mt) on [0,theta] and [0,pi] are respectively
sin(m*theta)/m and zero. The constant term contributes a_j*theta
and pi*a_j. These facts verify (2), with its factor 2, and (3),
with its factor 4. They use no zero-free disk or log G. Only zero
is a pole of the weighted forms, and the tracked arcs avoid it.

**Kernel and local scale.** In (11), k_0=Re(e^{it}(X+iY)),
k_1=X/rho and k_2=Re(e^{-it}(X+iY))/rho^2. Thus the two
mixed X(t)Y(s) terms cancel against those with the coordinates
exchanged. The remaining terms give exactly (4), including the
factor 2/rho^2, and its diagonal gives (12).

At sigma, X=Y=0 and
g'(theta)=-i e^{-i theta}G(sigma)+i rho G'(sigma)
=i rho G'(sigma). Terms differentiating cos and sin in (11)
vanish there. Substituting X',Y' in the same diagonal bilinear
calculation gives (13), with
kappa=2 sin^2(theta)|G'(sigma)|^2>0. Both simplicity and
0<theta<pi are essential; neither is replaced by a numerical
assumption. No division by d occurs.

The displayed integral definition of b extends it continuously
through theta. Continuity of (t,s) -> S(b(t),b(s)) at
(theta,theta), whose value is -kappa, supplies one delta for
the entire closed square after shrinking it below both endpoint
distances. Consequently (14)-(15) give strict signs everywhere
claimed, including the edges |t-theta|=delta or |s-theta|=delta.
No uniformity across labels or lower bound on delta is established.

Each restricted one-variable integral of |t-theta| is epsilon^2/2.
Thus 4*(kappa/2)*(epsilon^2/2)^2=kappa*epsilon^4/2 gives
the first bounds in (6). Put A_e=kappa*epsilon^4/2>0.
From alpha_e<=-A_e and beta_e>=A_e one obtains
alpha_e*beta_e<=-A_e*beta_e<=-A_e^2; the same calculation
holds for gamma_e. This verifies the epsilon^8 exponent and
kappa^2/4 constant without reversing an inequality involving
a negative factor.

**Fourfold domains and scope.** Every k_j and K is smooth on
the compact integration intervals. Ordinary compact Fubini and
bilinearity apply repeatedly, so (16) has the factor 4*4=16.
On the indicated open boxes the same-side K is negative and the
opposite-side K positive. Their integrals are exactly the local
products, with endpoints irrelevant to integration.

For the first product, split each of its three N factors into
[theta,theta+epsilon] and its remaining interval, and its P
factor into [theta-epsilon,theta] and its remaining interval.
Up to boundaries of measure zero, the domain is partitioned into
16 rectangular choices. Removing the all-local choice leaves all
15 other choices, including every mixture of local and nonlocal
variables. For the second product make the same split in its
three P factors and one N factor. This proves that (7) is the
whole signed complement in each case, not merely the fully
nonlocal box. At epsilon<=delta both outer remaining intervals
have positive length, but their signs are not controlled.

For either product, its nonnegativity is exactly equivalent to
its remainder being at least the negative of its local product.
This checks (8) and its positive required threshold. The local
negative sector does not settle this comparison. In particular,
it is consistent with L884's necessary strict checkerboard and
cannot by itself exclude the matched branch. The conclusion is
conditional on the actual label pair, not an assertion of such
a pair, graph existence, or a counterexample to RH.

No mathematical error was found in (2)-(8). The audit establishes
the stated conditional input and verifies the existing unsigned
pairing stop; it adds no product-sign result or certified novelty.
Other zeros and multiplicities, either first-label convention and
d=0 remain covered. L882's radial-domain hypotheses remain in force
but supply no signed remainder estimate in this proof. The direct
mathematical inputs are unchanged, so no DAG edge changes are needed.

## Mathlib

Full matching and supporting coverage has not been checked for this
actual conjugate-period obstruction; no absence claim is made. The
argument uses L883's cited Laurent/primitive input, elementary real
bilinear algebra, smoothness and compact integration. It is an informal
conditional calculation accepted by the independent audit above,
not a formal verification or a proof of an actual full-product sign.
