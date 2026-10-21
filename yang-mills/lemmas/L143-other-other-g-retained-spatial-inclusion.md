# L143 — Complete retained G spatial inclusion at cutoff 96

## Hypotheses

Import L140(1),(14)'s physical form B_(i,G) and its exact finite
tensor, L132's full symmetric probe rows, and L142's retained moment
scope. Use SU(2), both actual L010 probes i=3,6, direction-1 straight
lower-rooted forest, relative fixed-link box D=(-4,4)^4, flow time
1/16, and fixed-mesh bare small-coupling coefficients before refinement.
This step takes no new continuum limit. Retain both displacement
sectors, both shear polarizations, all allowed zero edge indices, the
upper primitive's endpoint constant and the lower constant prefix.
Both mode labels have every coordinate at most K=96.

The numerical inputs are precisely L082's 1156 certified compact
moments and L133's additional 192 certified degree-2 moments, together
with their enclosed pi and zero-mode normalization. The cutoff,
frequency convention, saved table and exact-rule qualifications are
unchanged. Write omega=pi/8, r=rho, f=x rho and

    F_h(n)=integral_(-3)^3 x^h rho(x) exp(i n omega x) dx.

These inputs enclose h=0,1,2 for |n|<=192 and h=3 for |n|<=96.
Only the numerical intervals are imported; no previous physical
contraction value or time-error prefactor is assigned to G.

## Conclusion

All 259682 real entries in the 28 distinct one-dimensional spatial
matrices needed by L140's cutoff-96 tensor are enclosed by the saved
dyadic center/radius pairs. The largest radius is exactly

    R_max = 0x1.32cb9092f9a43p-27 < 8.929e-9 < 1e-6.       (1)

The hexadecimal expression denotes the exact dyadic rational.
The auxiliary threshold 1e-6 checks spatial resolution only; it is
not a bound on the completed tensor error. All 24 G rows and the
48/192 full probe rows are retained. The moment-key union is the
same complete set of 1348 keys as in L142.

Every new upper-primitive axial entry (18528 entries) also passes
an independent real product-to-sum check, including all 96 constant
prefix entries. Exact rational coefficient checks verify j_n'=-v_n
and j_n(4)=0 for each n=1,...,96. The full entry replay and exact
dyadic-containment audit have zero failures.

No retained double-time/tensor inclusion, B_(i,G) value or actual G
sign follows. L141's scalar interval must be multiplied only after
that physical enclosure is complete. R, the triplet transverse-H
sign, joint compensation, finer powers/logarithm, other response jets,
finite matching, interacting error <=c_box/2, continuum axioms,
reflection positivity, infrared control and finite positive mass
remain unresolved. This is local reproduction of the already-assessed
Fourier/IBP inclusion method, without a novelty or candidate claim.

## Proof

### 1. Extend only the two missing elementary factors

L133's ordinary bases are v_n=sin(n omega(x+4))/2 and
e_n=cos(n omega(x+4))/2 for n>0, with e_0=1/sqrt(8).
Their lower primitives are p_n=sin(n omega(x+4))/(2 n omega)
and p_0=(x+4)/sqrt(8). Their first derivatives are already included.
For either ordinary basis b_n and n>0, direct differentiation gives

    b_n''=-(n omega)^2 b_n.                                (2)

For e_0 the second derivative is exactly zero. There is therefore
no division by a zero frequency and no new moment domain in (2).

The only new primitive is exactly L140(10):

    j_n=[cos(n omega(x+4))-(-1)^n]/(2 n omega), n>=1.       (3)

Its two nonconstant Fourier coefficients, at frequencies sign*n,
are i^(sign*n)/(4 n omega); its frequency-zero coefficient is
-(-1)^n/(2 n omega). These phases are exact fourth roots of unity,
since omega*4=pi/2. Differentiation of the nonconstant coefficients
multiplies them by i sign*n omega, yielding the negatives of v_n's
coefficients; the constant derivative is zero. Evaluating at x=4
makes each shifted phase equal (-1)^n, so the two cosine
coefficients sum to (-1)^n/(2 n omega), canceled by the retained
constant. This proves j_n'=-v_n and j_n(4)=0 for every n>0.
The certificate's 96 rational complex-coefficient checks are exact
finite instances of these identities, rather than sampled evidence.

### 2. Include every weighted integral

Use L140's complete J_T rows: six diagonal negative-second-derivative
rows and six mixed-first-derivative rows, paired with both direct and
negative-prefix rows of L_F. These give 24 signed component terms,
with weight ell u_1=(ell f) tensor r tensor f' tensor r.
The component-1 J_T input is exactly zero, but the component-1 input
in the right prefix is retained. Q_3 and Q_6 are the unchanged
48 and 192 rows from L132/L133. The certificate matches every
component, rational coefficient and coordinate key to L142, and
matches every Q row to L133's saved full-probe row lists.

For each coordinate, multiply the two elementary Fourier-polynomial
factors. In an axial G factor first multiply by ell=x+4. Then use
the identities imported from L082/L133:

    integral rho g   = sum c_(n,h) F_h(n),
    integral f g     = sum c_(n,h) F_(h+1)(n),
    integral rho' g  = -integral rho g',
    integral f' g    = -integral f g',
    integral f'' g   = integral f g''.                    (4)

All integration-by-parts endpoint terms vanish, because rho and its
derivatives vanish outside [-3,3], strictly inside the box. Every
derivative applies to the whole row product, including ell and any
zero prefix. Multiplication convolves the frequency/degree keys;
differentiation of x^h exp(i n omega x) gives the two terms
h x^(h-1) exp(i n omega x) and i n omega x^h exp(i n omega x).
L142 proves the complete containing domain for these rows. Formula
(2) changes only coefficients; (3) includes both frequencies ±n
and zero. Thus every used moment is covered by the imported tables.

Perform this finite arithmetic with outward integer intervals at
scale S=10^180. For addition and subtraction use endpoint sums;
for multiplication use the minimum/maximum of the four endpoint
products, rounded down/up after division by S. Division similarly
uses the four endpoint quotients and directed integer rounding.
Every divisor here is n omega with n>=1, or an exact positive
integer, so its interval excludes zero. The imported normalization
interval is used multiplicatively. These operations include the
true scalar results; applying the complex product formula to real
and imaginary intervals preserves inclusion by induction. Summing
against the certified F_h(n) intervals therefore includes every
exact spatial entry. The imaginary interval contains zero because
the original elementary row products and weights are real.

Convert a real integer interval [l/S,h/S] to a dyadic center c and
radius d only after checking with exact rational arithmetic that

    c-d <= l/S <= h/S <= c+d.                              (5)

The center proposal and radius conversion need not be assumed exact:
(5) is the actual inclusion check for each saved pair. No floating
matrix multiplication or BLAS operation occurs in this spatial step.
The imported moment certifications retain their original qualifications;
future tensor inclusion will separately require its arithmetic model.

### 3. Independent upper-row formulas

Define real quantities

    T(s)=Im[i^s (F_2(s)+4 F_1(s))],
    C(n)=Re[i^n (F_3(n)+8 F_2(n)+16 F_1(n))],
    C(0)=F_3(0)+8 F_2(0)+16 F_1(0).

In the last line take the real value; all three zero-frequency moments
are real. T(s) is the integral of ell f times the shifted sine of
frequency s. For n,m>=1 the elementary identity
cos(n y)sin(m y)=[sin((m+n)y)+sin((m-n)y)]/2 gives

    integral ell f j_n v_m
      = { [T(m+n)+T(m-n)]/2 -(-1)^n T(m) }/(4 n omega).  (6)

Negative m-n is kept with its signed moment and phase. Replacing
v_m by p_m divides (6) by m omega. For the remaining right index
zero, expand ell*f*p_0=x(x+4)^2 rho/sqrt(8), obtaining

    integral ell f j_n p_0
      = [C(n)-(-1)^n C(0)]/(2 n omega sqrt(8)).            (7)

Equations (6),(7) retain the upper endpoint constant explicitly and
are algebraically the same integrals as (4). Evaluate them with the
same certified moments, independently of the polynomial-convolution
routine. For all 9216 direct and 9312 prefix entries the difference
between the two enclosing intervals contains zero. This corroborates
the implementation of the proved identities; overlapping intervals
alone would not prove the identities, which were derived above.

### 4. Complete evidence and its limits

Reproduce from the active notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/enclose_g_spatial.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/enclose_g_spatial.py --audit

The full integer endpoint records for every matrix/index pair are in
`scripts/combined-ward-response/g-spatial-integer-entries.jsonl.gz`.
All dyadic arrays are in
`scripts/combined-ward-response/g-spatial-enclosure-factors.npz`.
The certificate
`scripts/combined-ward-response/g-spatial-enclosure-certificate.json`
identifies the inputs and script hashes, all basis checks, all signed
component templates, all matrix keys/dimensions/radius maxima, used
moments and failures. The audit in
`scripts/combined-ward-response/g-spatial-enclosure-audit.json`
recomputes all 259682 integer records, verifies every saved pair by
(5), and repeats all 18528 independent axial comparisons. It checks
every mode index, not a preview or sample. The complete summary,
matrix records and failure list were inspected; the full replay
checks the larger per-entry evidence. This is same-program replay
with separately derived axial checks, not independent formal verification.

The maximum of the saved dyadic radii gives (1), checked as a rational
inequality. In particular all entries pass the chosen spatial threshold.
That threshold does not control growth when these factors are combined
in the four-coordinate signed tensor: its errors must still be
propagated through every heat feature, product and integration.

The initial run stopped before a second-derivative entry because the
interval class has no power operator. Replacing freq**2 by freq*freq
repairs that implementation error. Its incomplete entry stream and
failure description are preserved in
`scripts/combined-ward-response/g-spatial-first-run-integer-entries.jsonl.gz`
and `scripts/combined-ward-response/g-spatial-first-run-failure.txt`.
They certify no complete spatial result. The final run and replay
have no mathematical or inclusion failure.

This supplies an input to the approved complete-other/other comparison,
not an evaluated coefficient. L140's two inverse weights, retained
time errors, signed tensor errors, L142's full spectral omission and
the eventual multiplication by L141 are separate obligations. No
general Ward or flow theorem is reproved or used to infer compensation.

## Mathlib

Full matching cutoff-96 G spatial-inclusion theorem: **not checked**.
Supporting trigonometric product-to-sum, elementary differentiation,
compact integration by parts, finite complex Fourier-polynomial algebra
and interval inclusion: **not checked**. Unknown availability is not
evidence of absence. No Mathlib result is assumed as a numerical input.
