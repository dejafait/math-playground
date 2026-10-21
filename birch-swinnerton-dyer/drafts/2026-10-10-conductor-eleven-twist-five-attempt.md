# Conductor-eleven independent twist-five calculation — working record

Gate: the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-10-conductor-eleven-twist-five-certificate.md`
predates this invocation. Main gap: arbitrary analytic-order-at-least-two
rank equality. Intermediate target: independently recover
q=L(E^5,1)/Omega(E^5) for [0,-1,1,-10,-20]. A nonzero result could
calibrate audited L039 via L028; it supplies no rank comparison by itself.
Preserve ATTEMPTS/023--024 and the parked uniform-q blocker.

Inputs: audited L039's minimality, Delta=-11^5, N=11 and modularity;
L028's conventions only; L031's exact interval methodology only. Import
the precise optimality/torsion, unitary-cusp, analytic and period sources
from the ready comparison. Full proof will be canonical if completed.

Before calculation, Wuthrich Proposition 1 gives [a/5]^+ in (1/10)Z:
c_infinity=1, torsion order 5, optimal base and Manin constant one.
All four cusps are unitary since gcd(5,11)=1. Cremona's oriented character
identity and Pal's positive minimal-twist factor one identify q with
sum chi(a)[a/5]^+, since the total base period is its least real period.
Thus q is in (1/10)Z and reduced denominator <=10. This is independent
of the unknown L039 scalar and applies even when q=0.

The completed-square cubic is H(x)=4x^3-4x^2-40x-79; H(4)=-47,
H(5)=121. Negative discriminant gives one real root r in (4,5).
Write the other roots u+iv,u-iv, u=(1-r)/2, v>0. Vieta gives
v^2=(3r^2-2r-41)/4; put d=(3r-1)/2 and R=sqrt(d^2+v^2).
For z=sqrt(r-u-iv) with positive real part, |z|=sqrt(R) and
Re(z)=sqrt((R+d)/2). These are the positive real arguments in
Cremona Section 3.7's pi/AGM(|z|,Re(z)) formula. Use one real
component and the minimal differential, followed by division by sqrt5.
All branches/positive radicands must be certified outward.

Continuation/abandonment test: only (T,b)=(128,48),(256,64),(512,96),
with full all-n tail, outward arithmetic and enumeration of every reduced
fraction of denominator <=10. One nonzero rational continues toward
calibration; sole zero stops this twist; unresolved essential coverage
stops dependent work. Independent points, quadratic coefficients,
rational membership, Sha elimination and general complex-order comparison
remain unresolved. This paragraph preserves the pre-calculation checkpoint.

## Completed bounded attempt

The canonical proof is L040, with the complete certificate and separate
finite replay under `scripts/conductor-eleven/twist-five/`. The first
pair (128,48) isolated 5 with width 25/17592186044416<1/100; all seven
grouped replay checks pass, including a_121=1. No further pair was used.
This produces one independent fixed-input q by known methods, not a new
theorem or a general BSD result. Its separate critical audit is pending;
current routing belongs only to PROGRESS.md.
