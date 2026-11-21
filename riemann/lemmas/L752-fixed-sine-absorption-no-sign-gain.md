# L752: Fixed-sine absorption is the original neutral sign problem

## Hypotheses

Use exactly L751's L=9log3, b=L/2, a=pi/L, zero-extended
h(x)=sin(ax), residual R_h, complete pole-free form Q_0 and
transformed remainder D_h (the last two lines of L751(3)).
Retain every prime power 2<=n<19683 and both directed shifts.
Put R_-(x)=max(-R_h(x),0).

Use L750's unchanged T=8log3, delta=T/40, smooth cutoff chi,
phi_k=chi*sin(k*pi*x/T), k=1,...,6, and zero extensions. Put
M_k=integral exp(x/2)phi_k(x)dx and define

    v_1=phi_3-(M_3/M_1)phi_1,
    v_2=phi_5-(M_5/M_1)phi_1,
    v_3=phi_4-(M_4/M_2)phi_2,
    v_4=phi_6-(M_6/M_2)phi_2.                         (1)

The tested space V is their complex span. Coefficients in (1) are
exact integrals. L750 proves M_1>0, M_2<0 and that these functions
form the exact common moment kernel. They have compact support in
(0,T), hence in (0,L). Analytic inputs are L751's specialized p=2
identity and scalar/kernel estimates, and L750's audited energy
enclosure method. No RH, positive complement or gap is assumed.

## Conclusion

The complete residual satisfies

    R_h(x)<-73/162,                    every 0<x<L.        (2)

Consequently, for every f in V,

    D_h(f)-integral R_-(x)|f(x)|^2dx=Q_0(f)=E_L(f).        (3)

By the same identity (3) holds for any compact smooth neutral test
in (0,L). Thus coefficient-one absorption is exactly neutral
positivity on the tested class: no positive residual part is removed.
This scope limitation does not disprove the inequality or RH.

The bounded outward calculation on V is **inconclusive**. Its
Hermitian energy matrix has two real symmetric parity blocks and
exact zero entries between them. The block determinants satisfy

    det A_even in [-0.000022358, 0.000013797],
    det A_odd  in [-0.000044257, 0.000034358].              (4)

Both intervals cross zero. No negative witness or positive block
is certified. All six individually enclosed trials below are
positive, which does not sign arbitrary linear combinations.
The negative-witness threshold was an energy upper bound <0;
it was not attained. Diagnostic eigenvalues are not proof.

## Proof

### Whole-interval residual, including killing and all edges

Fix x in (0,L). For 0<u<=b, x-u and x+u lie in
(-L/2,3L/2). At arguments outside (0,L) in this range,
sin(a*y)<=0. Hence the zero extension satisfies

    htilde(x-u)+htilde(x+u)
       >=sin(a(x-u))+sin(a(x+u))=2h(x)cos(au).

For u>b the sum of zero-extended values is nonnegative.
Since h(x)>0 and k(u)>=0, and all arithmetic numerators in
L751(4) are nonnegative and subtracted, this gives

    R_h(x)<=m_0+integral_0^b k(u)(1-cos(au))du
                   +integral_b^infinity k(u)du.           (5)

The second integral bounds the full continuous exterior term;
it is not dropped. Every finite arithmetic term has been bounded
in the direction appropriate to an upper bound, including exact
zeros. There is no prime-only truncation. Near zero the majorant
is k(u)a^2u^2/2, which is integrable; at infinity it is k(u).
L751 already proves residual existence and the applicable bounds.
Exactly L751(13)-(15) give m_0<-9/2 and the sum of integrals
in (5) <328/81. Their sum is -73/162, proving (2).
There is no division at an endpoint. L751 proves finiteness
of all terms on compact smooth tests. Now R_-=-R_h, so its
identity (3) proves the first equality in our (3). Both exact
moment cancellations give Q_0=E_L. This reuses the standard
identity, not a new positivity theorem.

### Exact matrix and the bounded test

L750 gives M_-(phi_k)=(-1)^(k+1)exp(-T/2)M_k, proving
both exact moments vanish in (1), as well as independence and
smooth compact support. Let A be the Hermitian polarization
of Q_0 in that basis. On real tests it is real symmetric:
m is real and even, and shifts occur with their adjoints.
Reflection x->T-x preserves the full-line form Q_0 and the
complete arithmetic sum. The first two basis functions are
symmetric and the last two antisymmetric, so the cross-parity
entries vanish exactly, also in the complex Hermitian extension.
This reflection is about T/2, not L/2; the full-line form and
zero extensions justify it without changing the outer window.

Enlargements of the six outward energy enclosures are:

| Trial | Complete energy enclosure |
| --- | --- |
| v_1 | [0.0007555410, 0.0020929426] |
| v_2 | [0.0046573793, 0.0067633363] |
| v_3 | [0.0024494584, 0.0039718464] |
| v_4 | [0.0090663537, 0.0113729577] |
| v_1+v_2 | [0.0100543449, 0.0155867571] |
| v_3+v_4 | [0.0219218336, 0.0278209479] |

For same-parity pairs,
A_ij=(Q_0(v_i+v_j)-Q_0(v_i)-Q_0(v_j))/2. It yields

    A_12 in [0.0005990330,0.0050869183],
    A_34 in [0.0032885148,0.0081525679].                  (6)

The complete unrounded matrix is in the certificate's `matrix`
field. Outward operations on those unrounded entries give (4),
not operations on this coarser printed table or on midpoints.
The positive diagonals and positive determinants would suffice
to sign both blocks; these enclosures do not prove that condition.
A negative lower endpoint is not a negative determinant proof.

### Enclosure applicability, errors and reproduction

The implementation is `scripts/sine-supersolution/absorption-324.cpp`;
its full output is `scripts/sine-supersolution/absorption-324.json`.
It includes the elementary intervals, quadrature, FFT and symbol
routines from `scripts/corrected-ims/certificate-315.cpp`, without
changing that source or its certificate. L750 Sections3-4 and its
step317 audit give the rigorous method, including precise DLMF and
quadrature citations and all tail estimates. This application changes
only the exact linear combinations and their moment enclosures.

All six M_k use composite Simpson with 262144 even subintervals
on [0,T]. L750's chi derivative bounds are independent of k;
sine derivatives are bounded by (k*pi/T)^j. Its `phiBounds(k)`
therefore applies for each k<=6. Multiplication by exp(x/2)
uses derivative bounds 81/2^j, j<=4. The resulting intervals
certify M_1>0, M_2<0; dividing exact moment enclosures gives
the exact ratios in (1). Full moment and coefficient intervals
were inspected. An approximate nullspace is never used.

Each energy uses period64, N=524288, s=1/8192 and the exact
piecewise linear interpolant q of the trial's exact nodal values.
Its second-derivative squared integral is bounded on 16384 whole
interval panels in [0,9], using the same jets on the new linear
combination and all coefficient intervals. L750(14)-(21) then
apply: full digamma head, Fourier tail, periodic image correction,
exact cubic autocorrelation and smooth interpolation errors.
The smooth function is exactly neutral, while q need not be:
the auxiliary evaluated form is A(q)-B(q), not E(q).

All 2292 prime powers n<19683 are enumerated. Of these, 1400
have n>=6561 and log n>=T. The trial and its interpolant have
support diameter <=T-2delta+2s<T, so these contributions are
exactly zero. The other 892 terms use their complete von Mangoldt
weights and both adjoints. The interpolation error has the same
support bound, justifying the active-shift norm C_prime<318.4530
in its error estimate too. No infinite prime tail is discarded.

The following upper budgets enlarge the six complete records:

| Trial order | Fourier tail | Periodic images | Interpolation energy error |
| --- | --- | --- | --- |
| 1 | 1.767e-7 | 2.147e-10 | 0.000624246 |
| 2 | 4.923e-7 | 1.626e-10 | 0.001015931 |
| 3 | 3.122e-7 | 1.853e-10 | 0.000721720 |
| 4 | 6.902e-7 | 1.518e-10 | 0.001117300 |
| 5 | 7.821e-7 | 4.721e-10 | 0.002646474 |
| 6 | 1.166e-6 | 3.967e-10 | 0.002842594 |

Elementary rounding, moment uncertainty and digamma enclosures
also enter the signed heads. No first-trial derivative or error
bound is reused for another trial. Full `trials`, `matrix`, and
`parity_block_determinants` were inspected. The failure field
explicitly records the inability to certify either sign; the
status is INCONCLUSIVE. No resolution, mode or window was enlarged.

Reproduce from the active notebook:

```sh
clang++ -O2 -std=c++17 -ffp-contract=off scripts/sine-supersolution/absorption-324.cpp -o /private/tmp/riemann-absorption-324
/private/tmp/riemann-absorption-324 > scripts/sine-supersolution/absorption-324.json
python3 ../scripts/loop/inspect_json.py scripts/sine-supersolution/absorption-324.json --pointer /matrix --full
python3 ../scripts/loop/inspect_json.py scripts/sine-supersolution/absorption-324.json --pointer /parity_block_determinants --full
```

The included original main is renamed and unused; clang warns
about its missing explicit terminal return (the original main
has an implicit return0). It is not invoked. The new executable
completed with exit0. There is no warning about interval operations.
The separate `scripts/sine-supersolution/absorption-324-replay.json`
is byte-identical to the primary certificate after the reporting-only
change that prints the determinant thresholds and failures explicitly.

The spatial comparison is an elementary extension of L751's
same upper envelope. This is local reproduction and scope
information, not an originality claim or an improvement on RH.
The finite restriction remains inconclusive. Full fixed-window
signs, unrestricted support and actual-Xi mixed signs remain open.

## Mathlib

Full matching coverage of this residual bound, restriction and
numerical enclosure has not been checked; no absence or formal
verification is asserted. Supporting named inputs are precisely
the p=2 identity and scalar estimates cited in L751 and the
quadrature/Fourier/interpolation inputs cited in L750. Their
compact smooth hypotheses and complete error bounds are retained.
