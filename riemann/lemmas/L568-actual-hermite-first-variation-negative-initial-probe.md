# Lemma 568: the actual Hermite first variation is negative at the initial probe

## Hypotheses

Use Xi(t)=xi(1/2+it), physicists' Hermite polynomials, and the actual
coefficients of L564:

    b_(2n)=1/[2^(2n)(2n)!] integral_R
                  u^(2n) exp(-u^2/4) Phi_R(u) du,
    P_N(t)=sum_(n=0)^N (-1)^n b_(2n) H_(2n)(t),
    R_N(t)=Xi(t)-P_N(t),
    B_N(t)=2P_N'(t)R_N'(t)-P_N(t)R_N''(t)-R_N(t)P_N''(t).

The coefficient formula and Xi expansion are imported from Dan Romik,
*Orthogonal polynomial expansions for the Riemann xi function*,
[arXiv:1902.06330v3, (2.1), Theorem 2.1/(2.2)](https://arxiv.org/html/1902.06330v3#S2),
with normalization and legitimate differentiation through order two
as established in L564. The Hermite derivative rule is
[DLMF 18.9.25](https://dlmf.nist.gov/18.9.E25).

Reuse C567a's audited enclosures for every coefficient b_(2n),
0<=n<=256. These enclose the full theta kernel and spatial integral,
with signed quadrature errors. Its negative evaluations and its
SOS conclusion are not premises for the new sign. The new calculation
does not rerun theta quadrature or independently audit Romik's source.
No RH, zero-free premise, simplicity or nonvanishing jet is assumed.

## Conclusion

At T=1, the prescribed cutoff is ceil(16(T+1)^2)=64, and t=1
belongs to [T,2T]. An exact rational certificate gives

    -2.75514*10^(-128) <= B_64(1) <= -2.75513*10^(-128) < 0.       (1)

All displayed terminating decimals are exact rational numbers.
Thus B_N(t)>=0 for every T>=1, N=ceil(16(T+1)^2), t in [T,2T]
is false, already on its first interval. This rejects that specified
sufficient signed-transfer mechanism, including a putative integral
symmetrization proving this universal sign.

This is a finite computer-assisted obstruction whose complete rational
contraction passed the separate audit below on 2026-10-31.
It is not a negative Xi discriminant,
an off-line zero, or a disproof of RH. A compensating interval margin,
a quantitative signed loss, other cutoffs or a theorem with additional
hypotheses are not excluded. No literature-originality claim is made.

## Proof

### Exact remainder decomposition and the infinite part

Set M=256. The finite identity, together with the differentiated
convergence in L564, gives for j=0,1,2

    R_64^(j)(t)=sum_(n=65)^256 (-1)^n b_(2n) H_(2n)^(j)(t)
                  +R_256^(j)(t).                              (2)

This uses the actual common coefficient sequence, not a subtraction
of independently approximated Xi and P_64. L564 (4) holds for every
integer cutoff at least one, irrespective of the moving-cutoff rule.
For 1<=t<=2, exp(t^2/2)<=exp(2)<9, since e<3. Consequently

    |R_256^(j)(t)| <= E := 45000*1029/5^256,
    0<E<5.36176*10^(-172), j=0,1,2.                            (3)

The last strict comparison is rational and checked in the certificate.
Thus the independent finite-coefficient uncertainty and the entire
infinite remainder are both retained. No sign is inferred from the
coefficient asymptotics, kernel positivity or sampled convergence.

### Applicability of the retained coefficient certificate

The source artifact is
`scripts/hermite-gram/global-dual-pairing-certificate.json`.
Its SHA-256, checked against C567a's completed replay comparison, is

    431d77c0fe35350ae5730c2fd5cee4cfe5fd12ae9fd130bd001b168e78ad7e0b.

The comparison artifact is
`scripts/hermite-gram/c567a-audit-replay-comparison.json`.
The retained parameters are 2048 fixed-point bits, exponential order
320, interpolation degree 256, 128 panels of length 1/32 on [0,4],
and 24 explicit theta terms. C567a's proof and audit cover precisely
all moment indices 0,...,256, including the derivatives' coefficients;
the change of evaluation point changes none of that quadrature.

For clarity, the new program also recomputes the complete coefficient
postprocessing, not just the imported decimal displays. Write A for
the exact sum of absolute unit-panel weights and [Q_n^-,Q_n^+] for
the retained half-line finite-theta quadrature, converted exactly from
its 2^2048 scale. The error quantities proved in C567a are

    I_n=8*2^60*(9/2)^(2n)*16^(-257),
    Theta_n=512*A*3^18*2^(-1849)*4^(2n),
    S_n=19200*3^18*4^(2n)*2^(-3072).

The full moment interval is

    [2Q_n^- - I_n - Theta_n,
     2Q_n^+ + I_n + Theta_n + S_n],                            (4)

and division by the positive integer 2^(2n)(2n)! gives b_(2n).
Every interval and every error in (4) agrees exactly with the audited
artifact. Both signs of the signed-rule theta error are indispensable;
only the genuine positive spatial integral is one-sided. No truncated
theta moment is treated as the complete coefficient.

### Complete finite contractions

At t=1 compute H_0=1, H_1=2 and

    H_(k+1)=2H_k-2kH_(k-1), 1<=k<512.

As an arithmetic consistency check, each of the 513 values is also
computed from the exact finite Hermite formula used in C567a:

    H_k(1)=k! sum_(r=0)^floor(k/2)
                   (-1)^r 2^(k-2r)/[r!(k-2r)!].              (5)

All values agree. Derivatives use H_k'=2kH_(k-1) and
H_k''=4k(k-1)H_(k-2), with both derivatives zero at k=0.
Sum every coefficient interval for n=0,...,64 to enclose P_64
and both derivatives. Independently sum every n=65,...,256 for
the finite part in (2), then add [-E,E] to each derivative interval.
There is no division by a polynomial value or its derivative.

The resulting enclosures lie within these exact rational intervals:

| Quantity at t=1 | Lower endpoint | Upper endpoint |
|---|---|---|
| P_64 | 0.485757 | 0.485758 |
| P_64' | -0.0224831 | -0.0224830 |
| P_64'' | -0.0215153 | -0.0215152 |
| R_64 | -2.07165*10^(-130) | -2.07164*10^(-130) |
| R_64' | 1.35763*10^(-129) | 1.35764*10^(-129) |
| R_64'' | 5.65835*10^(-128) | 5.65836*10^(-128) |

These already establish the sign without delicate cancellation:
P_64>0, P_64'<0, P_64''<0, R_64<0, R_64'>0, R_64''>0.
Every one of 2P_64'R_64', -P_64 R_64'', and -R_64 P_64'' is
strictly negative. For the sharper enclosure (1), the full rational
intervals, before rounding to the table, are inserted into all three
products and added.

For interval addition add endpoints. For multiplication take the
minimum and maximum of all four endpoint products; multiplication
by a negative scalar reverses endpoints. These inclusion rules are
valid even when two quantities share coefficients, so disregarding
that dependence can only widen the enclosure. There are no floating
sign decisions, omitted mixed terms or unstated infinite interchanges.

### Reproduction and scope of verification

Run, from the notebook directory,

    python3 scripts/hermite-gram/first-variation-certificate.py

The complete output is
`scripts/hermite-gram/first-variation-certificate.json`.
It records the source and audit hashes, all 257 enclosed coefficients
and their exact postprocessing checks, every exact Hermite value and
finite-formula check, all three finite and infinite-tail jet intervals,
the three signed products, the final exact rational enclosure and its
outward decimal enclosure. The latter is [-275514e-133,-275513e-133],
which is precisely (1); complete-rational containment is checked.
The error bound (3) is also rounded outward by rational comparison.

All new computation uses Python standard-library integers and exact
Fractions. The failure list is empty and the status is
NEGATIVE_WITNESS. The procedure stops at the first prescribed probe,
t=1, so the other four probes are not needed or evaluated. This
does not count an agreement of two meshes as verification. It reuses
the existing audited quadrature; it does not claim a fresh node replay
or an independent audit of this new certificate.

Finally, direct expansion gives

    D(Xi)=D(P_64)+B_64+(R_64'^2-R_64 R_64''),
    D(f)=f'^2-f f''.

A negative B_64 therefore rejects the proposed nonnegative linear
contribution only. It decides neither the sign of the whole expression
nor any of the unbounded-height or higher-degree positivity gaps.

### Independent complete certificate audit, 2026-10-31

The approved single-point audit passes without changing (1), any
coefficient enclosure, or any of the three infinite-tail allowances.
It validates the existing local obstruction; it is not a new sign
result beyond the original certificate or an independent audit of
Romik's manuscript. The original calculation and artifact are preserved.

The independent program is
`scripts/hermite-gram/l568-certificate-audit.py`; run

    python3 scripts/hermite-gram/l568-certificate-audit.py

Its full rational evidence is
`scripts/hermite-gram/l568-certificate-audit.json`.
No routines are imported from the first-variation program. The audit
checks the exact source hash above, the original certificate's source
and replay-comparison hashes, all retained parameters, and the completed
C567a audit's PASS, full-field equality and fresh-node flags. Reuse of
that audited coefficient data is the stipulated input, not a new
theta-node calculation.

For every n=0,...,256, the audit recomputes A from all 257 signed
weights, all three errors in (4), both full-moment endpoints and the
division by 2^(2n)(2n)!. All 257 intervals equal both the audited source
and the original first-variation artifact exactly. The two-sided theta
and interpolation errors, and the one-sided positive spatial tail, are
retained at every index. Their analytic justification is the completed
C567a audit; checking their arithmetic does not replace that justification.

As the primary Hermite calculation, use the integer finite formula

    H_m(1)=sum_(r=0)^floor(m/2)
       (-1)^r binomial(m,2r) [(2r)!/r!] 2^(m-2r).

Its summand equals (5) term by term. The exact integer values for all
m=0,...,512 also satisfy the recurrence and equal all original values.
The multipliers of b_(2n) for derivative orders 0,1,2 are respectively
(-1)^n H_(2n), (-1)^n 4n H_(2n-1), and
(-1)^n 8n(2n-1) H_(2n-2); the last two are zero at n=0.
For each jet, collect positive and negative multipliers separately,
using the upper coefficient endpoint for a negative multiplier's lower
contribution and the lower endpoint for its upper contribution. This
independently recovers all six exact finite jet intervals, with the
split precisely at n=64/65. All six are also contained in the stated
table after adding the infinite allowance to the remainder jets.

The infinite allowance is checked directly from L564's termwise
majorant, not from its moving-cutoff bound. With q=1/5,

    sum_(n>=257) n q^n
       =q^257 [257/(1-q)+q/(1-q)^2]
       =1029/(16*5^256).

Multiplication by 80000 exp(t^2/2), with exp(t^2/2)<9 on [1,2],
gives exactly E in (3). The rational comparison E<5.36176e-172 passes.
Add [-E,E] independently to every derivative jet. L564's summable
derivative majorants and its successive differentiation argument apply
at M=256 and t=T=1, including interval endpoints. Its normalization is
the same actual Xi, with no Gaussian or height scaling. No simplicity,
nonvanishing, relative-error estimate or complex-argument bound is used.

To check signed products independently, write an interval as
[c-r,c+r]. The exact product extrema are c_a c_b plus the minimum and
maximum of

    s r_a c_b + t r_b c_a + st r_a r_b,  s,t in {-1,1}.

Bilinearity puts the extrema at rectangle corners. This gives the same
full rational endpoints for all three signed products and their sum;
each individual product has a strictly negative upper endpoint. Shared
coefficient dependence is ignored only by enlarging to the full
rectangle, never by an unsupported narrowing. Comparing the complete
rationals, the final enclosure is contained in (1). The audit records
1330 passing checks, all complete recomputed coefficient errors and
intervals, every Hermite value and multiplier, all jet and product
intervals, and no failures. No additional probe is run.

Thus the recorded universal B_N>=0 mechanism remains stopped. A
compensating interval margin or a different quantitative signed-loss
argument is not rejected. The expansion of D(Xi) above still requires
both its polynomial contribution and quadratic remainder, and supplies
no all-height or higher-form conclusion from this negative mixed term.

## Mathlib

The full actual-coefficient certificate and mixed-remainder obstruction
have not been checked in Mathlib. Availability is unknown, not absent;
no formal verification is claimed. Hermite identities, finite sums,
rational interval arithmetic and termwise differentiation would be
supporting results, not the complete theorem. Source inputs are cited
above; general reference: https://leanprover-community.github.io/mathlib4_docs/
