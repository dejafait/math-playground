# Lemma 613: full triangular horizontal contrast is below the fixed-test error

## Hypotheses

Use the finite lattice parameters of corrected L612. Explicitly, all
logarithms are natural, H0=3.0610046·10^10, T≥2H0, and

    L=log T, d=1/L, h=4/L, n=floor(T/h), N=n+1,
    gamma_j=T+jh (0≤j≤n), H=2T, A=log H.

The two finite multisets, including every listed multiplicity, are

    R_T={1/2+d+i gamma_j, 1/2−d+i gamma_j : 0≤j≤n},
    R_T^0={two copies of 1/2+i gamma_j : 0≤j≤n}.

For r(alpha)=(1−|alpha|)_+, use the entire Fourier transform

    rhat(z)=(sin(pi z)/(pi z))^2, rhat(0)=1,
    Phi_H(u)=rhat(iuA/(2pi)) 4/(4−u^2).

Define the FULL ordered-pair difference

    Delta_T=sum_(rho,rho' in R_T) Phi_H(rho−rho')
              −sum_(rho,rho' in R_T^0) Phi_H(rho−rho').

These are algebraic squares in the definition of rhat. Neither multiset
is assumed to be an actual-zeta zero set or to satisfy the BGST pair
theorem. In particular the slab starts with gamma_0=T and retains
gamma_n=2T whenever equality occurs; no dyadic subtraction is used.

## Conclusion

For every stipulated T, Delta_T is real and nonnegative, and

    0≤Delta_T≤4 sinh^2(3/2)/sin^2(3)+(e^3/3)T.             (1)

Consequently Delta_T=O(T)=o(T sqrt(log T)). The full contrast of these
two multisets is therefore below the additive fixed-test error scale
O(H sqrt(log H)) from the cited BGST theorem. It cannot provide robust
separation at that scale. This does not assert that either multiset
matches the actual-zeta main term, that all other tests have small
contrast, or that individual mixed pairs are nonnegative. No charged-
union estimate, Xi realization, coefficient sign or RH conclusion follows.

## Proof

### Imported transform and its precise role

Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh, *An unconditional
Montgomery Theorem for Pair Correlation of Zeros of the Riemann Zeta
Function*, [arXiv:2306.04799v1](https://arxiv.org/html/2306.04799v1#S4),
equation (4.3), supplies the displayed triangular Fourier pair, with
convention rhat(z)=int r(alpha)exp(−2pi i alpha z)d alpha. Its compact
support makes the integral entire in z (differentiate under a uniform
compact bound); thus the identity applies also to the complex arguments
here, with the removable value at zero. This known transform is imported,
not claimed as a new result.

For the error-scale comparison only, the same source's Lemma 5,
(3.3)–(3.4), applies to fixed real-even integrable r supported in [-1,1]
and Lipschitz at zero. The fixed triangle satisfies all these hypotheses.
The complete actual-zeta ordered sum has an additive O(H sqrt(log H))
error. The cumulative correction in the same authors' *Pair Correlation
of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and
Critical Zeros*, [arXiv:2501.14545v3](https://arxiv.org/html/2501.14545v3#S3),
Section 3, MT and (3.3)–(3.5), preserves this fixed-test application.
Only its scale is a benchmark here. Its theorem is not applied to R_T
or R_T^0; no varying-test uniformity is invoked.

### Exact weight and complete finite sum

Put t_A(y)=A^(-1)(1−|y|/A)_+. This is nonnegative with integral one.
Substituting y=A alpha into the imported transform gives, for every
complex u,

    F_A(u):=rhat(iuA/(2pi))=int_R t_A(y)exp(uy)dy
           =(sinh(uA/2)/(uA/2))^2.                       (2)

The values at u=0 are removable. If |Re u|<2, elementary integration
over the positive and negative half-lines gives

    int_R exp(−2|v|)exp(uv)dv
      =1/(2−u)+1/(2+u)=4/(4−u^2).                     (3)

Define q_A(x)=int_R t_A(y)exp(−2|x−y|)dy. Multiplying (2) and
(3) and changing variable x=y+v yields

    Phi_H(u)=int_R q_A(x)exp(ux)dx,  |Re u|<2.          (4)

This Fubini step is absolutely justified: |y|≤A and
int exp(−2|v|+(Re u)v)dv<infinity. In particular the absolute
double integral is bounded by exp(|Re u|A) times this finite integral.
Tonelli also gives q_A≥0, q_A even, and int q_A=1, since both factors
in its convolution are nonnegative densities of mass one. For |x|≥A,
the sign of x−y is fixed except at a harmless endpoint, so (2) gives
the EXACT tail

    q_A(x)=exp(−2|x|) int t_A(y)exp(2y)dy
          =exp(−2|x|) sinh^2(A)/A^2.                   (5)

For x≤−A use evenness in the first equality. Evaluation at u=2 here
uses only the entire F_A, not the weight (3), whose convergence strip
is open.

All pair differences in this problem have real parts 0 or ±2/L.
Since L>4, these lie strictly inside (4)'s strip. There are finitely
many pairs, each absolutely integrable in (4); hence their sums may be
moved under that integral. For real x, put

    D_N(x)=sum_(j=0)^(N−1) exp(ijhx).

Then sum_j exp(i gamma_j x)=exp(iTx)D_N(x). Summing both horizontal
signs in R_T gives

    sum_(rho,rho' in R_T) exp((rho−rho')x)
       =4 cosh^2(x/L)|D_N(x)|^2.

Indeed the two factors sum exp(rho x) and sum exp(−rho' x) have
horizontal factors 2exp(x/2)cosh(x/L) and
2exp(−x/2)cosh(x/L), respectively, and their ordinate factors are
complex conjugates. For R_T^0 each horizontal sum instead has factor
2, retaining the collapsed multiplicity; its ordered sum is
4|D_N(x)|^2. Thus exactly

    Delta_T=4 int_R q_A(x)sinh^2(x/L)|D_N(x)|^2 dx.     (6)

This identity includes every diagonal, partner and cross-ordinate
pair. It proves reality and nonnegativity of the TOTAL difference,
without assigning signs to individual complex summands.

### Uniform central and tail bounds

Set B=3L/2. As L>4 and A=L+log 2, B>A. For 0<|x|≤B put
y=|x|/L, so 0<2y≤3<pi. The finite geometric sum gives

    |D_N(x)|≤1/|sin(hx/2)|=1/sin(2y).

Concavity of sin on [0,3] and convexity of sinh on [0,3/2] give

    sin(2y)≥(2y/3)sin 3,
    sinh y≤(2y/3)sinh(3/2).

Therefore 4sinh^2(x/L)|D_N(x)|^2 is at most
C0=4sinh^2(3/2)/sin^2(3). At x=0 its actual value is zero,
because D_N(0)=N is finite; no singular estimate at zero is needed.
Since q_A has mass one, the contribution of |x|≤B to (6) is at
most C0. In particular the central estimate does not lose a factor N.

For the remaining tails use |D_N(x)|≤N, valid everywhere, and
4sinh^2(x/L)≤exp(2|x|/L). With kappa=2−2/L>3/2, (5) yields

    tail≤[2N^2 sinh^2(A)/(A^2 kappa)]exp(−kappa B).     (7)

Both tails have been included in the factor 2. The integral converges
because kappa>0. Integer floors and all endpoints are retained by

    N=floor(TL/4)+1≤TL/4+1≤TL/2,
    N^2/A^2≤T^2/4,
    sinh^2 A≤exp(2A)/4=T^2,
    exp(−kappa B)=exp(−3L+3)=e^3 T^(−3).

The first inequality uses TL≥4, which holds throughout the stated
range. Substitution into (7) proves

    tail≤e^3 T/(2 kappa)≤e^3 T/3.

Together with the central estimate this proves (1). Dividing by the
required scale gives the explicit comparison

    0≤Delta_T/(T sqrt L)≤C0/(T sqrt L)+e^3/(3 sqrt L)→0.

Since H=2T and A=L+log 2, H sqrt(log H) is comparable to
T sqrt(log T). This is the asserted source-scale conclusion. It is
an upper bound, not an assertion that Delta_T has order T or tends
to zero absolutely. No infinite lattice limit, zero-product operation,
approximation of w, or deletion of mixed terms occurs. ∎

### Scope and reason for the specialization

The prior EXPLORE assessment checks the known transform and theorem,
but finds no inspected evaluation of this exact finite weighted contrast.
The new work is only (4)–(7) for the specified lattice and collapse.
The weight representation (3) is included because retaining that weight
is essential to this calculation; it is an elementary integral, not a
reproof of the imported triangular transform or a zeta theorem. The
result supplies an informative negative test for this particular
source-scale diagnostic, not established originality or a constraint
on all test functions. C464c and L018 motivate the horizontal/charge
interpretation; their actual-Xi assertions are not inputs to this proof.
The finite bound has the independent audit recorded below.

### Independent audit (2026-11-01)

The audit accepts (1) unchanged. It replayed the full multiplicity-four
ordered expansion after collapse, all real parts 0 and ±2/L in the open
convergence strip, absolute Fubini justification, and the exact q_A tail.
The entire F_A(2) was distinguished from the divergent weight integral
at 2. The central estimate includes x=0 with D_N(0)=N, and B=3L/2
lies above A and below the first nonzero geometric-sum singularity.
Both tails give exactly (7); the floor bound, kappa>3/2 and
exp(−kappa B)=e^3 T^(−3) yield the stated e^3 T/3 bound uniformly.
No endpoint, multiplicity or constant requires correction.

The primary transform and fixed-test hypotheses were rechecked against
the precise versions cited above, including v3's correction footnote 2
and cumulative (3.3)–(3.5). Only this imported interface and the finite
specialization are accepted; the number-theoretic source proof is not
independently audited. The verdict confirms the existing local
source-scale stop, without a stronger all-test or actual-Xi conclusion.
The full audit record is
`drafts/audits/2026-11-01-l613-full-contrast-audit.md`.

## Mathlib

Full matching coverage and supporting formalizations have not been
checked. No absence assertion, Lean verification or numerical certificate
is claimed. The proof is an analytic finite-sum bound valid for every
real T in the stated range.
