# Lemma 370: zero-safe discriminant decomposition and absolute envelope-curvature control

**Hypotheses.** Use the actual real functions F=F_0 and G, positive
envelope A, and real normalized jets P_j,V_j of L367. Put
T=1+|t|, L=log(2+|t|), and work on |t|≥40. Primes are ordinary
real-frequency derivatives. There is no regulator curve or zero
hypothesis. Write

\[
 \mathscr L(u)=u'^2-uu'',\qquad
 B_* =2F'G'-FG''-F''G,
\]
\[
 \ell_F=\frac{\mathscr L(F)}{A^2L^2},\quad
 \mathcal B=\frac{B_*}{A^2T^2L^2},\quad
 \mathcal C=\frac{\mathscr L(G)}{A^2T^4L^2},\quad
 \Delta=\mathcal B^2-4\ell_F\mathcal C.
 \tag{1}
\]

These are exactly the coefficients of L367's fixed-regulator quadratic
pencil. The identities below also hold for arbitrary real C² functions
F,G and a positive C² common envelope A on an open real interval;
the bounds additionally use the actual-family inputs of L367 and L369.

**Conclusion.** Define the polynomial minors

\[
 W=FG'-F'G,\qquad W'=FG''-F''G,\qquad K=F'G''-F''G'.
\]

Then, including all zeros of either function,

\[
 B_*^2-4\mathscr L(F)\mathscr L(G)=W'^2-4WK,
 \tag{2}
\]
\[
 \Delta=(P_0V_2-P_2V_0)^2
       -4(P_0V_1-P_1V_0)(P_1V_2-P_2V_1).
 \tag{3}
\]

For f=F/A, g=G/A and q=(log A)'', put

\[
 w=fg'-f'g,\qquad w'=fg''-f''g,\qquad k=f'g''-f''g',
\]
\[
 \Delta_0=\frac{w'^2-4wk}{T^4L^4}.
\]

There is the exact common-envelope identity

\[
 \Delta=\Delta_0+E_q,\qquad
 E_q=\frac{4q w^2}{T^4L^4}
     =\frac{4q}{L^2}(P_0V_1-P_1V_0)^2.
 \tag{4}
\]

In particular all first derivatives of the envelope cancel from this
discriminant transformation. There is a finite unevaluated constant K_q
such that |q|≤K_q/T² on |t|≥40, and hence the retained-jet bound is

\[
 |E_q|\le\frac{4K_q}{T^2L^2}(P_0V_1-P_1V_0)^2.
 \tag{5}
\]

Let E_0,E_1,D_0,D_1 be the actual-family constants from L367 (9), (15),
so |P_j|≤E_j T^(1/2)L^(−j) and |V_j|≤D_j for j=0,1.
With M=E_0D_1+E_1D_0, a coarser absolute bound is

\[
 |E_q|\le\frac{4K_q M^2}{TL^2}=o(1)
                \quad (|t|\longrightarrow\infty).
 \tag{6}
\]

This does not give a relative bound against Δ_0 or sign it. The residual
−4wk is signed; no control of it for the actual functions is asserted.
The constants in (5)–(6) and an onset for any further comparison are not
numerically evaluated. No total L367 margin or actual-theta sign follows.

**Proof.** This is a **REPRODUCTION** of finite polynomial algebra and
the already established common-envelope identities, with an actual-family
absolute bound. The saved pointwise EXPLORE assessment found no matching
full result; this is not a claim of originality. The Wronskian convention
is the standard one in NIST [DLMF 1.13.4](https://dlmf.nist.gov/1.13.E4).
No Abel identity, common differential equation, or nonvanishing of F or G
is used. Recomputing the algebra is necessary to check the precise pencil
normalization and curvature at zeros.

At one point write a=F, b=F', c=F'', d=G, e=G', h=G''.
Expanding the left side of (2) gives exactly

\[
 (2be-ah-cd)^2-4(b^2-ac)(e^2-dh)
 =a^2h^2+c^2d^2-2acdh
       -4abeh+4ace^2+4b^2dh-4bcde.
\]

The first three terms are (ah−cd)². The last four are
−4(ae−bd)(bh−ce). These are precisely W'² and −4WK.
This polynomial identity requires no division, so includes arbitrary
vanishing jets. Differentiating W uses only two derivatives, since the
F'G' terms cancel. From the definitions of the six L367 jets one has

\[
 \frac{W}{A^2T^2L}=P_0V_1-P_1V_0,\qquad
 \frac{W'}{A^2T^2L^2}=P_0V_2-P_2V_0,\qquad
 \frac{K}{A^2T^2L^3}=P_1V_2-P_2V_1.
 \tag{7}
\]

The denominator of both terms in (1) defining Δ is A⁴T⁴L⁴.
Dividing (2) by it and using (7) proves (3). These are pointwise
normalizations of ordinary jets, not differentiation rules for P_j,V_j.

For the envelope calculation put a_A=A'/A, so a_A'=q. Product
differentiation gives

\[
 F'=A(f'+a_Af),\quad
 F''=A(f''+2a_A f'+(q+a_A^2)f),
\]

and the identical formulas with g in place of f. Multiplying these
expressions and subtracting yields

\[
 W=A^2w,\qquad W'=A^2(w'+2a_Aw),\qquad
 K=A^2\{k+a_Aw'+(a_A^2-q)w\}.
 \tag{8}
\]

For the third formula the terms containing a_A linearly are
a_A(fg''−f''g)=a_Aw'. The terms in q+a_A² contribute
−(q+a_A²)w, while the remaining quadratic terms contribute
2a_A²w. Thus its full coefficient of w is a_A²−q.
Substitute (8) into (2). Cancellation is exact:

\[
 \frac{W'^2-4WK}{A^4}
 =(w'+2a_Aw)^2
      -4w\{k+a_Aw'+(a_A^2-q)w\}
 =w'^2-4wk+4qw^2.
\]

This proves the first form of (4). Equations (7) and (8) give
w/(T²L)=P_0V_1−P_1V_0, proving its second form. As a separate
coefficient check, L369 (7), applied also with equal arguments, gives
after division by A²,

\[
 \mathscr L(F)/A^2=\mathscr L(f)-qf^2,\quad
 \mathscr L(G)/A^2=\mathscr L(g)-qg^2,\quad
 B_*/A^2=2f'g'-fg''-f''g-2qfg.
\]

Their discriminant has cancelling q² terms; its q coefficient is
4{g²\mathscr L(f)+f²\mathscr L(g)
−fg(2f'g'−fg''−f''g)}=4(fg'−f'g)², confirming (4).
We use g=G/A throughout. Replacing g by G/(AT²) inside a
Wronskian without retaining derivatives of T² would change the formula.

For the bound use L369 (6) with its full common envelope. Explicitly,
p=t²+1/4, s=1/4+it/2, and Ψ=Γ'/Γ give

\[
 q=\frac2p-\frac{4t^2}{p^2}-\tfrac14\operatorname{Re}\Psi'(s)
       =O(t^{-2})\quad(t\longrightarrow+\infty).
\]

L369 proves this with separately controlled polygamma remainders,
specializing [DLMF 5.15.8](https://dlmf.nist.gov/5.15.E8) in a closed
admissible sector. We import that estimate; no bare asymptotic error is
differentiated here. A is even, by conjugation of Γ, so q is even.
Moreover q is continuous on |t|≥40. Since T/|t|≤41/40 there,
the asymptotic bound and the maximum on the remaining compact set give
a single finite K_q with |q|≤K_q/T². Taking absolute values in
(4) proves (5).

Finally L367's bounds and L>1 give

\[
 |P_0V_1-P_1V_0|
 \le (E_0D_1+E_1D_0/L)T^{1/2}\le M T^{1/2}.
\]

Substituting into (5) proves (6). These bounds use only positive
divisors A,T,L. In particular zeros of F or G, and zeros of w, cause
no singularity. If w=0, (4) gives Δ=w'²/(T⁴L⁴) exactly.

The limitations are visible already in arbitrary real jets with A=1.
At t=0 the pair f=cos t, g=sin t has w=1, w'=0, k=1,
so its unscaled discriminant is −4. The pair f=cosh t, g=sinh t
has w=1, w'=0, k=−1 and unscaled discriminant +4.
Both tests occur at g=0. These are checks of the polynomial residual's
indefiniteness, not assertions about actual zeta jets, and require no
specialization of the actual-family asymptotic bound. The absolute o(1)
curvature correction therefore leaves a substantive signed arithmetic
problem. Without a lower bound on |Δ_0| there is no relative-curvature
comparison; none is assumed or obtained. ∎

L368's eventual positive C and L369's negative linear-coefficient mean
remain available, but neither controls the residual here or the total
L367 sign margin. The SOURCE_BLOCKED sharp discriminant mean is not
used, and L365's stopped fixed-regulator route is not reopened. Higher
positivity, heights above forty and the endpoint arithmetic margin remain
unresolved. This finite identity is local progress in the notebook, not
a new positivity range or an RH candidate.

**Verification.** Run `python3 scripts/discriminant/check_pointwise_identity.py`.
The standard-library script expands integer sparse polynomials in all six
jets and the independent envelope variables a_A,q. Its three checks
verify (2), the unscaled (4), and the third minor in (8), with zero
nonzero residual coefficients required and obtained in each case.
The complete certificate is
`scripts/discriminant/pointwise-identity-certificate.json`; its full
`/checks` value was inspected. The manual proof above additionally checks
the positive normalization, the analytic q input and the bound. The
certificate verifies algebra only, not actual-function signs, a numerical
constant or relative control.

**Critical audit, 2026-10-06.** Equations (2)–(8) survive with the
original domain and bounds. Independently expanding the two sides of
(2) gives the seven coefficients displayed in the proof. In the variable
order (f,f′,f″,g,g′,g″,a_A,q), the complete saved certificate has exactly
those seven discriminant monomials and the three curvature monomials
4q f²g′²−8q ff′gg′+4q f′²g². Rerunning the inspected integer-polynomial
verifier gives zero residual coefficients in all three checks; the full
checks and both complete polynomials were inspected, not just their pass
flags. The proof's product differentiation checks their interpretation.

In particular, W, W′ and K carry the respective factors
A²T²L, A²T²L² and A²T²L³ in (7). Both W′² and WK therefore have
the required factor A⁴T⁴L⁴. The two terms defining Δ in (1) have
that same divisor. The parameter of L367's normalized pencil is
δ=εT²; identifying its coefficients uses fixed-ε ordinary jets,
without differentiating δ, T or L. The common-envelope calculation
uses g=G/A, whose ordinary derivatives do retain the changing T²
scale implicit in the V_j. Under the stated C² hypotheses, A>0
ensures f,g are C²; (8) uses q but never a derivative of q.

The polynomial check allows all six real jets independently. If F=G=0
at the point, W=W′=0 and the physical discriminant is exactly zero,
even when F′ and G′ are nonzero. If just one function vanishes, the
same identity still applies without division by that function. If w=0,
the correction is exactly zero and Δ=w′²/(T⁴L⁴). No continuity
argument from nonzero function values or simplicity assumption is needed.

For analytic uniformity, differentiating log A=log p+log|Γ(s)|
−(log π)/4 gives (log A)′=2t/p−Im Ψ(s)/2 and hence the displayed
exact q formula. The separate expansion of Ψ′ in L369 applies in
a fixed sector containing both rays s=1/4+it/2; alternatively evenness
reduces to its positive ray. Its leading real part satisfies
Re(1/s)=(1/4)/(1/16+t²/4)=O(t⁻²), and the remaining stated terms
are O(t⁻²). Thus choose t_*≥40 and C_q finite with
|q(t)|≤C_q/t² for |t|≥t_*. One admissible finite constant is
K_q=max{(41/40)²C_q, max_(40≤|t|≤t_*) T²|q(t)|}.
The latter maximum exists: Γ has neither a pole nor a zero on
Re s=1/4, so A is smooth and positive there. This verifies a uniform
existence bound, not an evaluated numerical constant.

L367 (9), (15) supply constants independent of t and ε; their
growth input uses fixed R=1, η=3/4 and a circle of radius 1/4,
followed by the positive gamma lower bound, with no critical-line
lower bound. Therefore |P_0V_1−P_1V_0|≤
(E_0D_1+E_1D_0/L)T^(1/2)≤M T^(1/2) since L>1.
Squaring this inequality in (5) gives precisely (6). This verifies
absolute o(1), with no bound relative to Δ_0. The audit finds no
defect requiring a changed conclusion and supplies no new sign range,
residual estimate, total margin or RH candidate.

**Mathlib.** Full matching discriminant transformation and actual-family
bound: **not checked**. Wronskian/determinant support alone would not
cover (4)–(6). No source search for Mathlib coverage was needed for this
finite algebra; unknown availability is not evidence of absence.
