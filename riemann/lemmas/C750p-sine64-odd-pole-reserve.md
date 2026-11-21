# C750p: A complete odd-pole reserve on the unchanged sine64 complement

## Hypotheses

Use C750m's complex H=L2((-b,b);C) with unweighted measure,
inner product <f,g>=integral f*conj(g), linear in f, b=log(101)/2,
and its complete orthonormal Dirichlet sine basis

    phi_j(x)=b^(-1/2)sin(j*pi*(x+b)/(2b)), j>=1.

P projects onto exactly phi_1,...,phi_64 and Q=I-P. Put
s(x)=sinh(x/2), c(x)=cosh(x/2). The negative odd-pole component
of C750m(7) is the negative of the positive rank-one operator

    Bf=2<f,s>s.

All other C750m parameters, both poles, all35 arithmetic terms and
the original form R are unchanged. They are not estimated here.
This step uses the approved SPECIALIZE assessment1173, at its exact
odd-pole target, and its reused elementary enclosure coverage1167.

## Conclusion

As an operator on the unchanged QH (or on H by zero on PH),

    nu_odd=||QBQ||=2||Qs||^2
           <1148/9375<1/8,
    1/8-1148/9375=191/75000.                         (1)

In particular -2|<f,s>|^2>=-(1148/9375)||f||^2 for all f in QH.
This pays only the negative odd-pole component. It supplies no
all-direction signed-multiplier floor, full R/E positivity, head or
coupling control, all-support extension, actual-Xi transfer or RH proof.
C750n's clipped-loss obstruction and C750o's single-even-vector result
are contrasts, not premises of (1), and are not undone by this reserve.

Outcome1174 is a local ADVANCE, RESEARCH/REPRODUCTION: a quantitative
specialization of known rank-one/Parseval methods, with no claim of
progress beyond the literature checked. Separate audit1176 below accepts
this component bound without strengthening its conclusion.

## Proof

### Complex compression and parity

For arbitrary complex f let u=<f,c>, v=<f,s>. The two moments are
u+v and u-v, so their pole product is
2Re((u+v)conj(u-v))=2|u|^2-2|v|^2. This is exactly C750m(7);
no real restriction or vanishing-moment constraint is imposed.
Orthogonal projection is self-adjoint, hence

    QBQ f=2<Qf,s>Qs=2<f,Qs>Qs.

Cauchy-Schwarz bounds its norm by 2||Qs||^2; if Qs!=0, equality
holds at f=Qs/||Qs||, and the zero case is immediate. This proves
the rank-one norm identity over C as well as over R.

The odd-index phi_(2k-1) are even functions, so their coefficients
against the odd function s vanish. For k>=1 set alpha_k=k*pi/b.
Then phi_(2k)(x)=(-1)^k b^(-1/2)sin(alpha_k x). An antiderivative is

    integral sinh(x/2)sin(alpha x) dx
      =[(1/2)cosh(x/2)sin(alpha x)
                          -alpha sinh(x/2)cos(alpha x)]/(alpha^2+1/4).

Differentiation cancels the cross terms and leaves the integrand.
At x=+/-b, sin(alpha_k b)=0 and cos(alpha_k b)=(-1)^k.
Multiplication by the basis sign and normalization therefore gives

    <s,phi_(2k)>=-2alpha_k sinh(b/2)
                              /(sqrt(b)(alpha_k^2+1/4)).           (2)

All these functions are real, so this coefficient convention is
compatible with the complex inner product. There are precisely32
nonzero coefficients removed by P; completeness and Fourier sine
Parseval on (-b,b) give the COMPLETE, nonnegative convergent tail

    nu_odd=(8b sinh(b/2)^2/pi^2)
             *sum_(k>=33) k^2/(k^2+a^2)^2, a=b/(2pi).             (3)

These are standard Hilbert-space projection and Parseval identities;
the reused operator reference is Gerald Teschl, Mathematical Methods
in Quantum Mechanics, GSM99, author version12February2009,
[Section6.3, pp139-141, (6.8)-(6.18),(6.21), Lemmas6.9/6.10](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
The source's complete-basis hypotheses hold here for the normalized
Dirichlet sine basis of L2; no boundary trace is required of s or
arbitrary QH elements. In particular s need not vanish at the endpoints.
Equation(2) and the fixed numerical reserve are the required elementary
specialization, not an attempted reproof of the source's general theory.

### Complete infinite-tail payment and exact enclosures

Since a>0, every summand in (3) is strictly less than1/k^2.
Monotonicity of x^(-2) gives

    sum_(k>=33)1/k^2 < integral_32^infinity x^(-2) dx=1/32.        (4)

For example each term is less than the integral on [k-1,k];
the strict gap already from k=33 persists after passage to infinity.
Thus (4) covers every omitted coefficient, without a finite truncation
or a sampled residual.

We use deliberately coarse parameter enclosures that suffice for (1).
The positive exponential Taylor polynomial gives

    exp(14/3)>sum_(j=0)^8 (14/3)^j/j!=29874809/295245>101,
    b=log101/2<7/3.                                             (5)

The second inequality is exact rational arithmetic, recorded with all
nine terms in the certificate below; monotonicity of exp proves the
logarithmic conclusion. The Taylor series is used at one positive real
argument with positive omitted terms, so no unproved error estimate is
needed. Also sqrt101>10, and e^b=sqrt101 implies exactly

    sinh(b/2)^2=(sqrt101+1/sqrt101-2)/4
               =(102/sqrt101-2)/4<41/20.                        (6)

Finally, the alternating arctangent series at1 gives

    pi>4*sum_(j=0)^63 (-1)^j/(2j+1)>25/8.                      (7)

The series is [NIST DLMF4.24.3](https://dlmf.nist.gov/4.24.E3),
already inspected in coverage1167, valid at this real endpoint.
Its64-term partial sum ends in a negative term and is a strict lower
bound by the alternating-series theorem; the error is less than4/129.
The second comparison in (7) is again exact rational arithmetic in
the saved certificate. Here arctan(1)=pi/4 is the principal real value;
there is no multivalued addition formula or Machin branch to select.

Substituting (4)-(7) into (3), all factors being positive, proves

    nu_odd < 8*(7/3)*(41/20)/(25/8)^2*(1/32)
           =1148/9375=1/8-191/75000.

The only numerical work is finite rational verification of (5),(7)
and this last comparison. Reproduce from the active notebook with

    python3 scripts/sine64/odd_pole_reserve_1174.py

The full exact terms, sums, tail majorant, threshold, margin and failures
are saved in `scripts/sine64/odd-pole-reserve-1174.json`. The proof uses
the displayed complete tail, not a decimal preview or the certificate
alone. All checks pass, with no floating transcendental evaluations.

The successful component reserve does not repair the full clipped-loss
norm: its earlier failing witness was even and had zero odd-pole cost.
The favorable even pole remains in R; no smaller admissible subspace
has been substituted for QH.

### Separate audit1176 — 16 November 2026

The full proof and C750m's hypotheses, (2) and (7) were checked under
the separately approved assessment1174/approval1175. With the stated
linear-first inner product, <Qf,s>=<f,Qs>, so the displayed complex
compression is correct. For the pole product, its cross term is
v*conj(u)-u*conj(v), which is purely imaginary. Thus neither its
real part nor the rank-one norm calculation drops a complex direction.

Differentiating the antiderivative gives numerator
(alpha^2+1/4)sinh(x/2)sin(alpha*x): both mixed terms cancel.
The endpoint numerator difference is
-2alpha*sinh(b/2)*(-1)^k; multiplication by (-1)^k/sqrt(b)
gives (2), including its sign. Squaring (2), multiplying by2 and
substituting alpha=k*pi/b gives exactly (3)'s prefactor.
The normalized complete sine basis is an L2 basis, so no endpoint
trace condition on s is needed. The removed nonzero coordinates
are precisely k=1,...,32. The first interval [32,33] already has
a positive integral-comparison gap, retained after taking infinite
limits; hence the complete tail bound is strict.

In (5) positivity of every omitted Taylor term justifies the strict
bound; the exact polynomial excess over101 is55064/295245.
In (6), b>0 and e^b=sqrt101 give the stated identity; sqrt101>10
has the asserted upper-bound direction. In (7),64 terms end with
-1/127 and the first omitted positive term is1/129, proving the
strict lower bound and error<4/129 after multiplication by4.
Every substitution into (3) uses positive quantities in the correct
direction. The resulting margin is exactly191/75000.

Independent arithmetic replay uses a recurrence for all nine Taylor
terms and the paired expression sum_(j=0)^31 8/((4j+1)(4j+3)) for
the arctangent lower bound. It checks all64 saved arctangent terms,
both complete finite sums, all parameter/tail/norm rational fields,
each original check and the failure list. Reproduce with

    python3 scripts/sine64/audit_odd_pole_reserve_1176.py

All95 checks pass, with no failures; execution of the original generator
reproduces its certificate byte for byte. Full term-by-term evidence,
exact comparison gaps, source hash and replay output are saved in
`scripts/sine64/odd-pole-audit-1176.json`. This arithmetic replay
supplements the analytic audit above; it does not independently prove
Parseval, the compression identity or the infinite-tail comparison.
No repair, stronger constant or new mathematical dependency was needed.
Audit1176 accepts (1) only as REPRODUCTION of known methods specialized
here. No full R/E lower bound or actual-Xi positivity has been verified.

## Mathlib

Full matching coverage for this fixed P64 compression and numerical
constant has not been checked; no absence claim is made. Supporting
standard mathematics is orthogonal projection, rank-one norm,
Fourier sine Parseval, elementary hyperbolic identities, Taylor and
alternating-series bounds, and decreasing-series integral comparison.
The precise operator and arctangent references above are reused
mathematical inputs, not assertions of matching Mathlib declarations.
