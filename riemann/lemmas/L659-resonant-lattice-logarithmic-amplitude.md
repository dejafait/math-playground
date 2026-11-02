# Lemma 659: a uniform diagonal envelope and a resonant lattice logarithmic amplitude

## Hypotheses

Retain L649's complete integer-mass family: n>=5, x=-d=-5/4,
R=11/8, U=R^2=121/64, eta=1/100, r_*=R-eta=273/200 and
t_j=j/n, 0<=j<n. The common distinct poles a lie on Re(a)=x,
obey |a|<=r_*, and include x. Their original residues r_a are
positive integers with M=sum_a r_a<=n/3. Set

    B_u(v)=product_(j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    c_k(u)=R^(-1) sum_a r_a W_a(u)(a/R)^k,
    G(u,zeta)=sum_(0<=k<M)c_k(u)zeta^k,
    D=sum_a r_a^2 mean_u |W_a(u)|^2/(U-|a|^2),
    H=max_(|u|=1) mean_zeta log|G(u,zeta)|.

All circle measures are normalized, and all logarithms are natural.
Every grid factor and the conjugated denominator angle are retained.
L658 supplies finiteness, attainment and the paid-arc localization of H.
No separation, symmetry or integrality of polynomial coefficients is
assumed in the general assertion. Write sigma^2=137/5000 and
kappa=31/1000<1/32.

For the additional lattice assertion, restrict n=6q+3, q a positive
integer, and define from this same full grid

    A_j=1/(d-t_j),       b_j=t_j/(U-d*t_j),
    lambda_n=sum_(j<n)(A_j+b_j),
    a_k=x+i*(2*pi*k/lambda_n),  -q<=k<=q,
    r_(a_k)=1,          M=2q+1=n/3.                     (1)

These poles are admissible beyond one onset, as proved below. They
are fixed as u varies; the definition does not select a different
pole family at different angles.

## Conclusion

For every original admissible family, uniformly in a and |u|=1,

    |W_a(u)| <= exp(kappa*n+1),
    D <= sigma^(-2) exp(2*kappa*n+2) sum_a r_a^2.        (2)

This controls the actual squared-residue diagonal, not an unsquared
replacement. The sharper certified constants in the proof are
305617/10000000 for the coefficient of n and 27319/125000 for the
additive constant. We use the simpler (2).

For the dense spread lattice (1), there is an absolute c>0 and one
onset such that

    c_0(-1)>=c*sqrt(n),
    H >= (log n)/2+log c.                              (3)

Consequently, for this lattice family there is a connected angular
arc I_n of normalized measure n^(-2) such that, beyond one onset,

    log mu(I_n)+2 mean_(I_n x T)log|G|
                            >=log D-n/16.              (4)

More quantitatively, the left side of (4), minus its right side, is
at least n/2000-2log n-C_1 for an absolute C_1. Thus the paid
criterion holds here with C=0 after an existential onset. No explicit
numerical onset is claimed. These lattices have N=M=n/3 and a
nonshrinking limiting support interval; they are not a sparse family
or a shrinking cloud.

The uniform criterion for arbitrary dense spread integer families is
still open. In particular (2) alone does not lower-bound H. The
spacing in (1) is a hypothesis of (3)--(4), not a consequence of
integer residues. Xi realization, matching upper bounds, all-degree
signs and independent audits remain unresolved. This is a local
mathematical input, not an RH candidate or certified originality;
the result has not received a separate critical audit.

## Proof

### 1. Source scope and the amplitude test

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-localized-logarithmic-joint-moment.md`.
The target remains its complete paid-arc criterion. L649 supplies the
family and exact diagonal; L658 supplies localization at the maximum
of the spatial logarithmic mean. L651 is downstream motivation only.
No general lower bound on its S_n or projection is assumed.

Import the exact spatial root integral, including boundary roots, from
F. Brunault and W. Zudilin, *Many Variations of Mahler Measures*,
ISBN 9781108794459,
[Proposition 1.4, publisher excerpt pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf).
This is the already inspected input underlying L657/L658. For a
nonzero polynomial with nonzero constant coefficient it implies
mean log|G|>=log|G(0)| by retaining all roots and its leading factor.
We do not reprove Jensen or assert that G has no spatial zeros.
The other analytic input is the standard maximum modulus principle
on a closed disk for a function holomorphic on a neighborhood of it.
The finite product expansion and the compact-plus-tail Riemann-sum
argument below are written out to justify their n-dependent use.

The scoped comparison checked the earlier angular-evaluation and
fractional-lattice stops, the closed finite screens, and the relevant
C645r/C645w and L653--L658 statements. Their hypotheses or conclusions
do not give this diagonal envelope or this logarithmic amplitude.
The fractional dual obstruction uses different masses; no such
relaxation is made here. The previously observed pointwise Chebyshev
cancellation is not an all-angle logarithmic obstruction. No finite
family screen is repeated. The single-factor diagnostic recorded in
the working note only selected exact inequalities; it is not a premise.

### 2. A single-factor inequality on the complete vertical line

For a=x+i*y, y real, put

    T_a(w)=(x-w)/(a-w) * (U-conjugate(a)*w)/(U-x*w).

For w=t*u, |u|=1, |T_a(w)| is exactly the modulus of the ratio of
the corresponding grid factors in B_u(x)/B_u(a). Conjugation in the
second numerator is legitimate only inside this modulus identity:
|U-a*conjugate(w)|=|U-conjugate(a)*w|. All denominators of T_a
are nonzero for |w|<=1, because |a|>=d>1 and U/d>1.

Fix t in {1/2,3/4,9/10,1}; write u=c+i*s, c^2+s^2=1. Define

    N_0=d^2+t^2+2*d*t*c,
    D_0=U^2+d^2*t^2+2*U*d*t*c,
    N(y)=N_0-2*t*s*y+y^2,
    D(y)=D_0-2*U*t*s*y+t^2*y^2.

Then

    |T_a(t*u)|^2=N_0*D(y)/(D_0*N(y)).                 (5)

Here N(y)>0 and D_0>0. The desired upper bound L in (5) follows
if the quadratic L*D_0*N(y)-N_0*D(y) is nonnegative for every real y.
Its leading coefficient and constant coefficient are

    A=L*D_0-t^2*N_0,
    C=(L-1)*D_0*N_0,

and its linear coefficient is -2*t*s*(L*D_0-U*N_0). For L>1,
A>0 since

    D_0-t^2*N_0=(U-t^2)*(U+t^2+2*d*t*c)>0;
    U+t^2+2*d*t*c >=(d-t)^2+U-d^2>0.

It therefore suffices to prove the following quartic polynomial is
positive on -1<=c<=1:

    F_(t,L)(c)=(L*D_0-t^2*N_0)*(L-1)*D_0*N_0
                         -t^2*(1-c^2)*(L*D_0-U*N_0)^2. (6)

The four exact pairs are

    (t,L)=(1/2,101/100), (3/4,21/20),
          (9/10,113/100), (1,129/100).                 (7)

The exact rational certificate proves (6) on the entire interval, not
on a sample. For a polynomial sum_(j=0)^4 p_j*c^j on a cell [l,r],
first substitute c=l+(r-l)*v. Its power coefficients become

    h_k=sum_(j=k)^4 p_j*binomial(j,k)*l^(j-k)*(r-l)^k.

Its coefficients in the Bernstein basis
binomial(4,k)*v^k*(1-v)^(4-k) are

    B_k=sum_(j=0)^k h_j*binomial(k,j)/binomial(4,j).     (8)

These identities follow by the binomial theorem. The basis functions
are nonnegative and sum to one on [0,1], so positivity of all B_k
proves positivity throughout the cell. The complete partitions and
the minimum over all their B_k are as follows; successive entries in
each partition specify all adjacent cells.

| t | Partition of [-1,1] | Minimum coefficient, strictly positive |
|---|---|---|
| 1/2 | -1,-3/4,-1/2,0,1 | 64664519871/21474836480000 |
| 3/4 | -1,-7/8,-3/4,-1/2,0,1 | 318013521/137438953472 |
| 9/10 | -1,-15/16,-7/8,-3/4,-1/2,0,1 | 59516468756927/107374182400000000 |
| 1 | -1,-31/32,-15/16,-7/8,-3/4,-1/2,0,1 | 14734506387/343597383680000000 |

Every quartic power coefficient and every coefficient in (8), with
its exact rational value, is stored in
`scripts/one-sided-hankel/logarithmic-amplitude-factor-certificate.json`.
They are reproduced from (6)--(8), using only rational arithmetic, by

    python3 scripts/one-sided-hankel/logarithmic-amplitude-factor-certificate.py

The four complete covers (22 cells), all their coefficients and all
strict margins were inspected, not just a summary flag. There were
no failures. This supplies a finite checkable arithmetic part of the
proof; no floating-point assertion is used in (6).

For each fixed a, T_a is holomorphic on a neighborhood of the closed
unit disk. The maximum modulus principle extends the bound at each
endpoint t in (7) to all |w|<=t. This step is why the endpoint
certificates also bound every intervening grid factor. The proof of
(5)--(7) permits all real y; the original radius restriction is not
needed for this single-factor estimate.

### 3. The full product and the squared-residue diagonal

Assign each t_j to the four successive intervals with lengths
1/2,1/4,3/20,1/10 and upper endpoints (7). There are at most n times
the interval length plus one grid points in each. Let e=L-1. The
elementary inequality

    log(1+e)<=e-e^2/2+e^3/3,  0<=e<1,

follows by integrating 1/(1+v)<=1-v+v^2 from 0 to e. Hence the
upper bounds for (log L)/2 at the four endpoints are, respectively,

    29851/6000000, 1171/48000,
    366847/6000000, 768239/6000000.

Their interval-length-weighted sum and their unweighted sum are

    305617/10000000 < 31/1000 < 1/32,
    27319/125000 < 1.                                  (9)

The exact margins are in the same certificate. Multiplying all n
factors, including t_0=0, proves |W_a(u)|<=exp(kappa*n+1).
No angle is optimized separately and then asserted to attain the
product envelope: multiplication uses valid upper bounds at every
angle. The possibly unattainable independent maxima are harmless for
this upper bound.

The pole clearance gives U-|a|^2>=sigma^2. Multiplying the squared
bound by each original r_a^2 and integrating proves (2). For general
residues sum r_a^2<=M^2, but for (1) it is exactly M=n/3. Thus for
that lattice

    log D <=2*kappa*n+log n+2-log(3*sigma^2).           (10)

### 4. Admissibility and the exact resonant phase

The functions A(t)=1/(d-t) and b(t)=t/(U-d*t) are positive or
nonnegative and smooth on [0,1]. Their sum is increasing. Therefore

    lambda_n/n -> lambda=integral_0^1 (A(t)+b(t))dt
        =log 5+(121/100)log(121/41)-4/5.

An exact 32-cell left Riemann sum is greater than 2, so lambda>2.
The full rational sum, its terms and positive margin are in the
certificate. Its value is approximately 2.04611; that decimal is not
used as evidence. Consequently lambda_n>2n beyond one onset. For
the endpoints in (1), using the classical Archimedes bound pi<22/7,

    |2*pi*q/lambda_n| < pi/6 < 11/21,
    r_*^2-d^2-(11/21)^2=464789/17640000>0.              (11)

Thus every pole obeys the required radius bound. They are distinct,
the k=0 pole is x, and all residues are one with M=n/3. Moreover
their endpoints tend to +/-pi/(3*lambda), a strictly positive
constant, while their spacing tends to zero. This verifies both the
integer census and the dense spread description.

At u=-1 direct division of every grid factor gives the exact product

    W_(x+i*y)(-1)=product_(j<n) (1+i*b_j*y)/(1-i*A_j*y). (12)

Its logarithm near y=0 has the expansion

    log W_(x+i*y)(-1)
       =i*lambda_n*y-(V_n/2)*y^2+O(n*|y|^3),
    V_n=sum_(j<n)(A_j^2-b_j^2).                        (13)

The constant in the error is absolute for |y|<=1/8: A_j<=4 and
b_j<=64/41<2, and the logarithm power series on |z|<=1/2 has its
tail starting at degree three bounded by an absolute multiple of
|z|^3. Choose the branches continuous from y=0. Equation (13) is
only used there; the global modulus estimate below needs no branch.

To keep the quadratic coefficient and the full tail explicit, note

    b_j<=A_j/2.

Indeed this is equivalent to 3*d*t_j-2*t_j^2<=U, and the maximum of
the left side over all real t is 9*d^2/8=225/128<U=242/128.
It follows that

    12/25 <= A_j^2-b_j^2 <=16,
    V_n/n -> V=integral_0^1(A(t)^2-b(t)^2)dt,
    12/25<=V<=16.                                     (14)

For y_k=2*pi*k/lambda_n, the linear phase in (13) is exactly
2*pi*k. It is not an approximation or a discarded phase.
Writing z=k/sqrt(n), uniformly for z in any fixed compact interval,
(13)--(14) imply

    W_(a_k)(-1) -> exp(-beta*z^2),
    beta=2*pi^2*V/lambda^2>0,                          (15)

in the following precise triangular-array sense: the difference
between W_(a_k)(-1) and exp(-beta*(k/sqrt(n))^2) tends uniformly to
zero for |k|<=T*sqrt(n), for each fixed T. The error n*|y_k|^3 is
O_T(n^(-1/2)); the quadratic coefficient converges by (14).

### 5. All lattice terms and the complete spatial logarithmic mean

For all real |y|<=1, (12) gives

    log|W_(x+i*y)(-1)|
      =-(1/2)sum_j log(1+(A_j^2-b_j^2)*y^2/(1+b_j^2*y^2))
      <=-(1/2)sum_j (A_j^2-b_j^2)*y^2/(1+A_j^2*y^2)
      <=-(6/425)*n*y^2.                               (16)

Here log(1+v)>=v/(1+v) for v>=0 follows by integration, and (14)
and 1+A_j^2*y^2<=17 give the last inequality. Also lambda_n<6n,
since A_j<=4 and b_j<2. Combining this with (11) and (16), every
term of the admissible lattice, including its endpoints, satisfies

    |W_(a_k)(-1)| <= exp(-(2*pi^2/1275)*k^2/n).         (17)

For any fixed T, (15) and the ordinary Riemann sum on |z|<=T give
the corresponding integral of exp(-beta*z^2). The tails of the sum
divided by sqrt(n) are uniformly bounded by tails of the Gaussian
in (17): for k>T*sqrt(n), comparison with its decreasing integral
gives a bound tending to zero as T tends to infinity, uniformly for
large n. Since q/sqrt(n) tends to infinity, no endpoint is lost from
the central limit. Therefore

    n^(-1/2) sum_(k=-q)^q W_(a_k)(-1)
                   -> C_*:=integral_R exp(-beta*z^2)dz>0. (18)

This compact-plus-tail argument justifies the limit rather than
interchanging an uncontrolled growing sum. Positivity of the limit
is explicit: its integral over [-1,1] is at least 2*exp(-beta)>0.
The sum is real because (12) conjugates when y changes sign.
Consequently, beyond one onset,

    c_0(-1)=R^(-1)sum_k W_(a_k)(-1)
                              >=C_*/(2R)*sqrt(n).

Use c=C_*/(2R). The cited root integral gives
mean_zeta log|G(-1,zeta)|>=log|c_0(-1)|. This retains the complete
spatial polynomial: no truncation tail, root or leading coefficient
is replaced by zero. It proves (3), even if G has other zeros on or
inside the spatial circle.

L658 now supplies a centered maximizing arc I_n with mu(I_n)=n^-2
and paid logarithmic mean at least 2H-2log n-32*pi^2/9. Subtract
(10) and add n/16. By (3), the result is at least

    (1/16-2*kappa)*n-2log n
          +2log c-32*pi^2/9-2+log(3*sigma^2)
      =n/2000-2log n-C_1.                             (19)

It tends to positive infinity, proving (4) with one onset for this
specific sequence. L658's product integrability and degree-drop
qualifications remain in force. The arc is selected by the maximum
of the logarithmic mean, not by the diagonal or by a claimed
nonvanishing value at a single angular point.

### 6. Scope of the advance and verification

The new amplitude estimate (3) is for a dense spread integer family,
and (2) applies to every original admissible family. Their combination
gives a genuine H-versus-D comparison in (19), not another localization
lemma or a generic degree loss. It excludes (1) as a countersequence
to the paid criterion. It neither makes every family a lattice nor
shows that an arbitrary family has a comparable resonance. The
general numerator cancellation remains unbounded from below.

The rational certificate's four quartic checks, rate comparisons,
Riemann lower sum and geometric margins passed. Its full relevant
arrays and exact values were inspected with the shared JSON inspector.
The certificate verifies those arithmetic claims only; the analytic
maximum principle and the full limit (18) are justified above.
The optional single-factor floating-point diagnostic has no enclosure
and supplies no proof premise. No family-level numerical screen,
actual-Xi numerical evidence or source manuscript audit was performed.

## Mathlib

The reused assessment inspected
[Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html).
Supporting results include
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure` and
`Polynomial.mahlerMeasure_mul`. Nonzero hypotheses and analytic
logarithms are retained; totalized logarithms do not replace them.
Full matching coverage for the uniform rational factor envelope or
the growing resonant-lattice/paid-arc conclusion has not been checked.
The rational certificate is not a Lean formalization. No absence
claim for wider Mathlib coverage is made.
