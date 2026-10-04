# Lemma 359: regulated cancellation scale and small-regulator negatives

**Hypotheses.** Use exactly the regulated real spectrum in L358, with
0<ε≤1. All derivatives below are real-frequency derivatives. Write
S=S_ε(ξ) and use its positive normalization A, gamma phase φ,
ω=φ′, α=(log ε)/2 and positive beta amplitude β from that lemma.
Put q=(log A)″, b=(log β)′ and b′=(log β)″. At a real frequency set

\[
 C=e^{i\phi}S,\quad D=e^{i\phi}S',\quad E=e^{i\phi}S'',\quad
 V=S'+i\omega S,\qquad c=|S|,\ d=|S'|,\ e=|S''|,\ v=|V|.
\]

Define the following nonnegative error bounds, retaining the exact
subtraction rather than treating it as zero:

\[
 \begin{gathered}
 B_0=\beta,\qquad B_1=\beta(|b|+|\alpha|),\qquad
 B_2=\beta[(|b|+|\alpha|)^2+|b'|],\\
 Z_2=e+2|\omega|d+(|\omega'|+\omega^2)c,\\
 \mathcal E_\beta=2vB_1+B_1^2+cB_2+B_0Z_2+B_0B_2
                    +|q|(2cB_0+B_0^2),\\
 \gamma=|\omega'|/2+|q|,\qquad
 U=v^2-(\operatorname{Im}D)^2+ce+\gamma c^2+\mathcal E_\beta.
 \tag{1}
 \end{gathered}
\]

The finite signs stated below use L037's explicit outward arithmetic
contracts. The analytic inequalities do not depend on numerical arithmetic.

**Conclusion.** At every real ξ the normalized first sign obeys

\[
 \frac{F_\varepsilon'^2-F_\varepsilon F_\varepsilon''}{A^2}
 =|V|^2-(\operatorname{Im}D)^2
       -\operatorname{Re}C\operatorname{Re}E
       +\omega'\operatorname{Re}C\operatorname{Im}C
       -q(\operatorname{Re}C)^2+R_\beta,
 \qquad |R_\beta|\le\mathcal E_\beta.
 \tag{2}
\]

Consequently U<0 is a sufficient negative-sign certificate.

At fixed ε there is a finite X_ε such that any negative first sign
at ξ≥X_ε must satisfy the shrinking-value condition

\[
 |S_\varepsilon(\xi)|\le\frac{C_\varepsilon}{\omega(\xi)},\qquad
 C_\varepsilon=M_1+
       \sqrt{M_1^2+M_0M_2+M_0^2+1},\qquad
 M_j=\sum_{n\ge1}n^{-1/2}e^{-\pi\varepsilon n^2}(\log n)^j.
 \tag{3}
\]

Here ω(ξ)~(log ξ)/2. Neither C_ε nor X_ε is asserted uniform
as ε tends to zero.

There is also a conditional construction test. Fix ε, m>0 and
0≤κ<σ≤1. At sufficiently large frequencies satisfying

\[
 |\omega S-iS'|\le\kappa |S'|,\qquad
 |\operatorname{Im}(e^{i\phi}S')|\ge\sigma |S'|,\qquad |S'|\ge m,
 \tag{4}
\]

the first sign is negative, with normalized upper bound at most
−(σ²−κ²)|S′|²/2. No occurrence of (4) at arbitrarily large
frequencies or for a family ε→0 is assumed or proved.

There are also the following certified finite examples. Every decimal
endpoint in this table is an exact terminating rational; the displayed
intervals enlarge the saved outward enclosures.

| ε | ξ | enclosure of (F_ε′²−F_εF_ε″)/A² | sufficient upper certificate |
|---|---|---|---|
| 1/10000 | 2018091/10 | [−24.325, −24.324] | U<−21.387 |
| 1/100000 | 8129949/10 | [−21.649, −21.648] | U<−14.645 |
| 1/1000000 | 769857/10 | [−64.981, −64.980] | U<−59.796 |

Thus a common threshold ε_0 for nonnegativity at every real frequency
and every 0<ε≤ε_0, if it exists, must satisfy ε_0<1/1000000.
The six finite bad regulators in L358 and here do not prove bad
regulators arbitrarily close to zero. No actual-theta sign or
zero-exclusion range is extended.

**Proof.** L358 supplies the exact identity F_ε=A y, where
y=z+B, z=−Re C and B=β cos(αξ). In particular the first sign
divided by A² is y′²−yy″−q y². Direct differentiation gives

\[
 z'=-\operatorname{Re}D+\omega\operatorname{Im}C,\qquad
 z''=-\operatorname{Re}E+2\omega\operatorname{Im}D
          +\omega^2\operatorname{Re}C+\omega'\operatorname{Im}C.
\]

Expanding z′²−zz″−qz² and completing the square yields

\[
 z'^2-zz''-qz^2
 =|D+i\omega C|^2-(\operatorname{Im}D)^2
       -\operatorname{Re}C\operatorname{Re}E
       +\omega'\operatorname{Re}C\operatorname{Im}C
       -q(\operatorname{Re}C)^2.
\]

Multiplication by e^(iφ) preserves modulus, so the first square
is |V|². This is an algebraic identity for the real projection;
it does not replace the spectrum by a complex modulus square.

The exact derivatives of B are

\[
 B'=\beta[b\cos(\alpha\xi)-\alpha\sin(\alpha\xi)],\qquad
 B''=\beta[(b^2+b'-\alpha^2)\cos(\alpha\xi)
                         -2\alpha b\sin(\alpha\xi)].
\]

Their absolute values are at most B_1 and B_2, respectively,
and |B|≤B_0. Also |z|≤c, |z′|≤v and |z″|≤Z_2. The difference
between the full sign and the z expression is exactly

\[
 R_\beta=2z'B'+B'^2-zB''-Bz''-BB''-q(2zB+B^2).
\]

The triangle inequality gives its bound in (1), proving (2).
Since |Re C Re E|≤ce and
|Re C Im C|≤|C|²/2, (2) is at most U. These arguments are
pointwise and valid for every permitted ε, without a tail approximation.

For (3) only, hold ε fixed. Absolute convergence of the damped
series gives c≤M_0, d≤M_1 and e≤M_2. The differentiated gamma
estimates imported in L358 give ω~(log ξ)/2→∞, ω′=O(1/ξ),
q=O(1/ξ²), bounded b,b′, and
β=O_ε(ξ^(−1/4)exp(−πξ/4)). Thus
γ→0 and E_β=O_ε((1+ω²)β)→0. Choose X_ε so that ω>0,
γ≤1 and E_β≤1 beyond it. Equation (2) also gives the lower bound

\[
 \frac{F_\varepsilon'^2-F_\varepsilon F_\varepsilon''}{A^2}
 \ge v^2-d^2-ce-\gamma c^2-\mathcal E_\beta.
\]

A negative value therefore forces
v²<M_1²+M_0M_2+M_0²+1. The triangle inequality
ωc=|iωS|≤|V|+|S′| now proves (3).
The fixed-regulator constants can grow as ε decreases, so this
necessary condition does not settle the vanishing-regulator quantifier.

For (4), |V|=|ωS−iS′|≤κd and c≤(1+κ)d/ω. Therefore

\[
 \frac{U}{d^2}\le\kappa^2-\sigma^2
       +\frac{(1+\kappa)M_2}{m\omega}
       +\frac{\gamma(1+\kappa)^2}{\omega^2}
       +\frac{\mathcal E_\beta}{m^2}.
\]

At fixed ε the last three terms tend to zero. This proves the
claimed eventual margin at every frequency satisfying the hypotheses.
It supplies a discriminating cancellation target, not a recurrence
or existence theorem for that target.

For the finite examples, reuse L358's controlled gamma logarithm,
digamma and trigamma with its radius-one Cauchy derivative bounds,
and the geometric common tail for S,S′,S″. The last indices are
N=360,1140,3600, respectively. With m=N+1 the common series-tail
bound is exactly the one proved there:

\[
 \frac{m^2e^{-\pi\varepsilon m^2}}
 {1-((m+1)/m)^2e^{-\pi\varepsilon(2m+1)}}.
\]

Each denominator is checked positive. The same exact rational input,
70-digit directed interval arithmetic, π enclosure and elementary
logarithm/trigonometric remainders from L358 are retained. To bound a
complex modulus, form the outward interval for x²+y² and apply
exp(log(x²+y²)/2); the selected norm intervals are strictly positive.
For a positive argument below one, use log t=−log(1/t), so the
covered logarithm routine still receives arguments at least one.
An interval crossing one is handled by its monotone endpoint bounds.
All operations have the L037 contracts; no floating-point probe
enters an acceptance check.

The certificate evaluates (1) using upper modulus endpoints for its
positive error terms, retaining outward intervals for the two signed
squares. It also directly evaluates y′²−yy″−q y² using L358's exact
two differentiated formulas and checks compatibility with (2) and
the beta error bound. Both the sufficient upper and the direct sign
have negative upper endpoints in every case. The positive A makes
these negative signs of the unnormalized expression as well.
Reproduce all three with
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/gaussian-zero-mode/certify_cancellation_scale.py`;
the saved full output is
`scripts/gaussian-zero-mode/cancellation-scale-certificate.json`.
Any ε_0≥1/1000000 includes the third regulator and contradicts its
negative value, proving the stated threshold restriction. ∎

The gamma asymptotic inputs remain those precisely cited in L358,
including [DLMF 5.11.1–3](https://dlmf.nist.gov/5.11#E1) and
[5.15.8–9](https://dlmf.nist.gov/5.15#E8). This calculation reproduces
those covered tools with an elementary square completion. No theorem
of actual-theta positivity, regulator-uniform tail control or originality
is claimed. The bounded floating-point probe in
`scripts/gaussian-zero-mode/probe_cancellation_scale.py` proposed
locations only; its counts in `cancellation-scale-probe.json` are
not certified densities or tail assertions. The analytic occurrence
of the shrinking cancellation target is unresolved. Further standalone
finite-threshold scans are parked because they cannot meet the ε→0
stopping test; the pointwise inequality remains available for an
analytic construction.

**Mathlib.** Full cancellation identity, shrinking-value condition,
conditional construction test and regulated sign coverage: **not checked**.
The supporting gamma, complex norm, Fourier and interval results are
also **not checked** here. L037's arithmetic contract and L358's named
analytic inputs are reused. No full matching library theorem or library
absence is asserted; general documentation is
[Mathlib](https://leanprover-community.github.io/mathlib4_docs/).
