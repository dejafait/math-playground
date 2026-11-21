# Bulk-pole microscopic test — working record, step 135

Invocation-start gate: unchanged EXPLORE assessment
`literature/2026-11-03-centered-gap-bulk-pole-pairing.md`.
The only target is its prescribed eventual one-zero count, tested through
the constant-plus-linear Taylor comparison. Main gap: actual-Xi
all-degree mixed positivity; downstream hope: scalar zero-pole charge
compensation. A single disk does not pay aggregate charge, control the
complete spatial mean, or give H/support or Xi realization.

Inputs read: L666 exact rational continuation (6), L699 fixed profile,
reflection and residue (7), L694 summability/cap, L696 prescribed-center
interface, and L700 Sections 1–2 as a fixed-index contrast. Reused the
supplied primary gamma/remainder/Rouche assessment without browsing.
Scoped duplicate and failure checks retain steps 115/127/129/131/133;
no bulk microscopic count was found. No cross-notebook input.

Preserve the exact fixed selected profile, d=5/4, U=121/64, A=27/10,
n=12q+3, j=(n-1)/2, -2q<=m<2q, unit original masses, anchor, j=0
product factor, inverse angle and every downstream M moment.

## Initial reduction (unfinished)

Put z=-Un*u/d and w(y)=(1-i*y/d)^(-1). Then the target disk is
|z-j|<1/4. Define finite products

    P_n(z)=product_(k=1)^(n-1)(1-z/k),
    T_n(z,w)=product_(k=1)^(n-1)(1-w*k*z/(U*n^2)).

Exact division in L666 gives

    W_(x+i*y)(u)=w(y)*P_n(z*w(y))*T_n(z,1)
                    /[P_n(z)*T_n(z,w(y))].

Thus the analytic numerator to study is the original finite sum
S_n(z)=sum_(a in Z) w(Im a)*P_n(z*w(Im a))/T_n(z,w(Im a)),
including the anchor w=1. The pole-removed function has the nonzero
local prefactor -(d/(UnR))*(z-j)*T_n(z,1)/P_n(z).
Holomorphy, asymptotics, Taylor-root location and strict boundary error
remain to be checked. No conclusion is asserted in this checkpoint.

## Endpoint mechanism under investigation

Let Y=9/20, v(y)=w(y)/2 and use principal logarithms. Put

    I(v)=integral_0^1 log(1-v*t/U) dt,
    g(y)=(1-v)*log(1-v)+v*log(v)-i*pi*v-I(v),
    b0(y)=w*[log(v/(1-v))-i*pi+integral_0^1 t/(U-v*t) dt].

The reflected gamma product and complex Stirling suggest an endpoint
sum of two conjugate exponentials, with phase n*Im(g(Y)), rather than
a numerator whose root stays at the pole. Exact top ordinates are
Y-A*(l+1)/n+A*e_(2q-1-l)/n. Their fixed-l shifts tend to zero.
To justify the geometric endpoint limit one must prove monotonicity
of Re(g) and a uniform absolute estimate, including y=0 where the
sine factor can vanish. Then summability/cap should control the exact
profile without a finite Picard approximation. This is partial reasoning,
not an established bulk limit or zero-count result.

The candidate limit has now been reduced to

    F_n(s)/C_n = (pi*s/sin(pi*s))
       *[D*exp(i*n*theta)*exp(b*s)
           +conjugate(D)*exp(-i*n*theta)*exp(conjugate(b)*s)] + o(1),

uniformly on |s|<=1/2, with C_n>0, theta=Im(g(Y)),
D=a(Y)*exp(-b0(Y)/2)/(exp(A*g'(Y))-1),
a(y)=i*w*sqrt((1-v/U)/(v*(1-v)))/sqrt(2*pi),
b=b0(Y)-integral_0^1 t/(U-t/2)dt. The prime is a y derivative.
Proof checks still to finish: branch choices and uniform Stirling error,
the geometric endpoint domination, normalization and derivative transfer.

For t=y/d in [0,9/25], an elementary lower bound gives
d Re(g)/dt>9/20, hence d Re(g)/dy>9/25. This is the proposed
endpoint domination; no interchange based only on pointwise asymptotics
is permitted. The exact positive endpoint is Y-A/n+Ae_(2q-1)/n.

A preliminary ordinary-double evaluation (not certificate evidence)
gave b approximately 0.564657-2.176165i and 12*theta/pi approximately
-5.256153. The attempted mpmath import failed because it is unavailable;
no package installation was attempted. A standard-library exact rational
constant certificate will replace this diagnostic if the proof succeeds.

If the phase increment is nonresonant, geometric-sum averaging gives
infinitely many n with cos(n*theta+arg D)^2>=49/100. For those phases,
normalization by the nonzero center amplitude leaves

    H_t(s)=(pi*s/sin(pi*s))*exp(alpha*s)
                 *(cos(beta*s)-t*sin(beta*s)),
    alpha=Re b, beta=Im b, |t|<=21/20.

The actual planned Taylor comparison can then have zero roots: its
limiting polynomial is 1+(alpha-beta*t)*s. Candidate bounds on |s|=1/4
are |polynomial|>7/25 and |H_t-polynomial|<1/5. If certified and the
uniform o(1) is proved, analytic Rouche would give zero zeros for the
exact F_n at infinitely many n, refuting the approved eventual-one
target for each fixed profile. This is still pending proof/certificate
completion and is not an RH disproof.

Continuation/abandonment test: prove a strict full-circle linear Rouche
margin and one interior comparison root for every fixed profile
eventually, or record an exact obstruction/unpaid term. Finite n or an
approximate Picard array cannot refute the universally eventual target.

## Completed attempt

The full proof is now canonical in L701, with the exact-rational
certificate `scripts/one-sided-hankel/centered-gap-bulk-pole-certificate-135.json`.
The certificate passed: limiting linear boundary lower 0.2870375,
remainder upper <0.186627, required >7/25 and <1/5. Complete log and
coefficient records were inspected, not just a preview or a finite grid.
The uniform endpoint asymptotic and geometric phase average yield
infinitely many exact-profile disks with zero zeros, via the prescribed
Taylor comparison. This refutes the eventual-one local target, subject
to a separate conceptual audit; it does not refute RH or scalar charge
compensation. No effective or profile-uniform onset is claimed.
The original one-root comparison is abandoned for this radius/index.
The next nomination is critical review of this proof, with a new
REVIEW_REQUIRED audit-scope assessment; no new target is approved here.
