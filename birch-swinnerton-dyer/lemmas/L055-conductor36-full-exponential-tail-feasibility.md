# L055 — fixed conductor-36 full-exponential tail feasibility

## Hypotheses

Use L054's saved coupled T_5 solution, all 98 distinct positive interior
primitive points, and all original uncombined generator occurrences in
`scripts/conductor36-table/coupled_plan.json`, under its supplied-input
hypotheses. In particular E is L050's minimal y^2=x^3+1, with exact
conductor 36 and associated normalized elliptic newform. The complete
N=36 structural, L053 and L054 instance critical audits remain pending.
Use audited L049's Fourier-tail identity and audited L051's Machin,
real attenuation and independent positive total minimal period evidence.
There are 72 original integral generators and 144 cusp endpoints.

Only the saved geometry and absolute-occurrence error convention are
tested. Required bounds are H<=4860 at each primitive, at most 1000000
distinct finite terms, and normalized two-sided tail width <=2^-38 at
every original generator. Neither central vanishing nor any table value
is assumed. No non-CM hypothesis is asserted for this curve.

## Conclusion

The uniform choice H=4860 passes the full-exponential tail planning test:

    distinct primitive points = 98,
    distinct heights = 16,
    distinct terms = 476280 <= 1000000,
    max H = 4860 <= 4860,
    every normalized two-sided tail width <= 2^-60 < 2^-38.

Generator 28, {-1/27,0}, has the largest certified upper width. All 72
rows pass; complete independent finite replay has zero certificate or
threshold failures. No minimal-cutoff claim is made. This is a fixed
known-method specialization; the separate fixed critical audit below passes.
It supplies no finite sums, integration table, integer recovery,
coefficient, rank assertion, Sha finiteness or complex-order comparison.
L054's dyadic obstruction and ATTEMPTS/025--028 remain valid and preserved.

## Proof

**Known source and specialization.** The pre-existing SPECIALIZE
assessment is `drafts/literature/2026-10-12-conductor36-full-exponential-tail.md`.
Import Wuthrich, *Numerical modular symbols for elliptic curves*,
[arXiv:1608.06423v2, 23 March 2017, equation (2), Lemma 4 and complete
proof, printed pp.6--7](https://arxiv.org/pdf/1608.06423v2). For an interior
point z=x+iy of the associated normalized elliptic newform, truncation
after H terms leaves complex error at most

    exp(-2*pi*H*y)/(exp(2*pi*y)-1) = q^(H+1)/(1-q),
    q=exp(-2*pi*y), H>=0, y>0.

The imported proof uses global |a_n|<=n, rather than finite coefficient
tests. Real error is bounded by complex modulus. No non-CM, unitary-cusp,
semistability or period hypothesis enters that bound. L054's balanced
points have exact rational 0<y<=1 (y=1/|C| when C!=0), so it applies to
all saved points without changing any transport. The finite powers and
weighted enclosure are the specialized difference; the analytic theorem
is not reproved. Exponential series, positivity and addition are imported
from [NIST DLMF 4.2.19--4.2.22](https://dlmf.nist.gov/4.2#iii) and the
standard Taylor theorem, with their L049/L051 audited arithmetic scope.

**Input integrity and complete geometry.** The new certificate binds
the exact bytes of the coupled plan and audited L051 analytic certificate
by SHA-256. The independent verifier calls L054's unchanged complete
replay, without writing any old report. It reconstructs the full
presentation, all assignments and matrices/inverses, exact coupled
equations and solution, all endpoint compositions, every primitive key,
and every uncombined occurrence. Its old dyadic cutoff failure is retained
in the new report as historical evidence, rather than treated as an
exponential-tail failure. The full infinity Hecke equation and zero
infinity primitive are retained. Audited L051's independent period replay
rechecks the Machin brackets, positive square roots and twelve AGM steps;
its connected real locus has total-period factor one. In particular

    Omega_lower = 166638467572977606763020498997 / 2^95 > 0.

No scale or period is inferred from unknown generator values.

**Rational exponential containment.** All interval endpoints are integers
divided by D=2^96. Multiplication takes the minimum and maximum of all
endpoint products, rounds the lower endpoint down and the upper endpoint
up; exact rational scaling does the same. Addition is exact at this scale.
Induction on these operations gives containment even with repeated
variables and signed Taylor terms. The verifier uses Fraction endpoint
arithmetic and imports no new producer code.

At each of the 16 distinct heights, enclose w=-2*pi*y using the replayed
Machin bracket and check -8<=w^-<=w^+<0. Starting at t_0=S_0=1, compute

    t_k = t_(k-1)*w/k, S_k=S_(k-1)+t_k, 1<=k<=160.

Every term and partial sum is saved. Taylor's theorem gives the approved
outward remainder R=3^8*8^161/161!: |w|<=8 and exp(8)<3^8 bound the
derivative throughout the relevant real segment. Enlarge S_160 by
ceil(D R) on each side. The resulting q interval is checked to satisfy
0<q^-<=q^+<1, without clipping or a floating-point sign assumption.
Complete replay visits all 2560 polynomial steps, the rational remainder
and its ceiling. Equal-height reuse merely caches identical certified
data, and changes no error weight.

**Complete powers and majorant endpoints.** At every height compute the
positive interval power q^4861 by binary exponentiation. Initialize the
accumulator to one and the base to the q bracket. For remaining exponent
n, multiply the accumulator by the base if n is odd; halve n, and square
the base if the remaining exponent is positive. Save each n, base,
accumulator before/after multiplication and next base. Each multiplication
rounds outward. The standard exponent identity for this finite schedule
and interval containment verify q^4861; the independent verifier checks
every saved transition and all 336 multiplications. A lower power endpoint
may round to zero and still gives a valid lower enclosure.

Writing p^-<=q^4861<=p^+, the exact rational tail-majorant bracket is

    [p^-/(1-q^-), p^+/(1-q^+)].

Both denominator endpoints are strictly positive. The verifier instead
computes all four Fraction endpoint quotients and their minimum/maximum,
checking the full saved bracket. The lower endpoint bounds the source
majorant, not true Fourier error. For the smallest height y=1/684 the
full selected bracket is

    [1604553132/362226466506258632135208535,
     3209106265/724452933012517264270416908].

All 98 primitive rows reference the completely checked bracket for their
exact height; all retain H=4860. Distinct reduced point keys and their
uses were verified by the unchanged coupled replay, so the prospective
finite sum workload is exactly 98*4860=476280. Infinity costs no terms.

**Every uncombined generator row.** For each original generator g use
the full L054 occurrence list (j,w_j), including repetitions. Define

    M_g^-/+ = (2/Omega_lower) sum_occurrences |w_j| B_j^-/+.

The source majorant width at this fixed cutoff lies in [M_g^-,M_g^+].
The true normalized two-sided tail width is at most M_g^+, because the
total period is at least Omega_lower. No signed cancellation or combination
of equal-key coefficients reduces this sum. The independent replay
reconstructs every weight and absolute-weight total and checks all 1316
occurrences, all 72 exact rational brackets and the maximum. Integer
cross multiplication verifies max_g M_g^+<=1/2^60<1/2^38. The exact
large rational endpoints of the maximum are in the certificate at
`/generators/28/normalized_tail_width_bounds` and in the verification
report at `/worst_width_bounds`; no decimal approximation is used.

The sufficient uniform radius allocation also passes: with W_max=22/3,
every primitive upper radius is <=rho=2^-38 Omega_lower/(2 W_max).
This is an additional check, while the actual conclusion is supported
by all reconstructed row bounds. There are no obstruction or inconclusive
rows. The term and cutoff comparisons use exact integers. Therefore this
full-exponential bound meets every specified planning threshold on the
unchanged fixed geometry, despite the valid dyadic-majorant stop.

Reproduction commands:

    python3 scripts/conductor36-table/build_exponential_plan.py
    python3 scripts/conductor36-table/verify_exponential_plan.py

Full rational evidence, all Taylor and power transitions and all original
occurrence rows are in `scripts/conductor36-table/exponential_plan.json`.
Complete replay, actual/required counts and failures are in
`scripts/conductor36-table/exponential_plan_verification.json`.
Replay is finite informal evidence, not a universal software correctness
theorem. Structural and earlier instance critical audits remain pending;
this new assembly's separate audit passes below. Finite arithmetic errors,
new sums, signed period division, rational isolation and table relations
are still unperformed. L052's clearing integer 24 is downstream only.
The CM curve does not satisfy L027's non-CM hypothesis. Uniform coefficient
production, rational directions, Sha and complex-order comparison remain
independent unresolved gaps; no BSD candidate is produced.

**Separate critical audit, 2026-10-12, BSD-184.** The pre-existing
SPECIALIZE assessment
`drafts/literature/2026-10-12-conductor36-exponential-plan-critical-audit.md`
approves this REPRODUCTION audit. The whole producer and verifier, their
coupled-plan replay and positive-period subroutine were inspected. Source
coverage is reused unchanged: Wuthrich's elliptic-newform tail applies
at every positive saved height; no non-CM or unitary-cusp assumption is
added. Integer powers have no branch choice; reuse DLMF
[4.2.27](https://dlmf.nist.gov/4.2#E27). The independent target period has
the same one-component factor and positive lower endpoint as audited
L051. No coefficient or normalization is inferred from a table value.

The new `scripts/conductor36-table/audit_exponential_plan.py` imports the
independent verifier, never the producer, and saves a fresh complete
replay. It checks all 16 attenuation brackets, 2560 Taylor steps, 336
rounded power multiplications, 98 primitive rows, 1316 uncombined
occurrences and 72 generator widths, with zero failures. Upstream replay
reconstructs 864 orbit assignments, 72 cosets, 144 relations, 144 paths
and 626 segments; all declared structural counts equal their required
counts. The coupled replay checks 67 endpoint and 72 Hecke assignments,
139 matrices/inverses, 66 representative-pair inequivalences, 13
normalized equations, 52 formal right-hand-side variables and 144
endpoint compositions. This is complete finite replay of those supplied
inputs, not completion of their pending separate critical audits.

The binary-power logic has the exact exponent invariant r+b*n=4861,
where the accumulator contains q^r and the base contains q^b. Initially
(r,b,n)=(0,1,4861). For an odd n add b to r; replace n by floor(n/2)
and double b if n remains positive. The invariant is preserved until
n=0 and r=4861. At each multiplication the min/max endpoint products
and outward rounding preserve inclusion, also when a lower endpoint
becomes zero. The 13 saved iterations per height include every odd
accumulator update and all 12 needed squarings. There is no last missing
factor. The four-quotient replay preserves both positive denominators;
the lower result bounds only the source majorant.

Distinct exact checks supplement this replay rather than merely rerun
its algorithm. For each of the 16 saved argument brackets [l,u], let
c=(l+u)/2 and delta=(u-l)/2. The entire interval and segment from zero
lie in [-8,0]. Reuse L051's audited real Taylor/mean-value bounds:
the degree-200 exact polynomial P(c) has error at most 8^201/201!,
and variation from c to the actual argument is at most delta, since
exp'(w)<=1 there. Exact rational Horner evaluation, with no intermediate
rounding, gives the containing bracket

    [P(c)-delta-8^201/201!, P(c)+delta+8^201/201!].

Every such bracket is contained in the saved positive q bracket. Thus
these are containing intervals, not floating-point test values. The
script saves the complete exact polynomials, errors and endpoints.

Independently of every rounded power transition, write q's endpoints as
a/D,b/D and the saved power endpoints as p/D,s/D. Full integer powers
check, for e=4861,

    0 <= p D^(e-1) <= a^e <= b^e <= s D^(e-1).

All 32 endpoint tests pass; their full integer numerators are saved in
hexadecimal, without truncation. Monotonicity of x^e/(1-x) on (0,1)
also follows directly from its two positive increasing factors.
The independent checks cross-multiply each saved tail endpoint against
a^e/[D^(e-1)(D-a)] and b^e/[D^(e-1)(D-b)]; all 32 comparisons pass.
The rational expressions and full integers are the evidence, not their
printed lengths or a preview. This covers both zero rounded lower powers
and the small-height case where the lower bound is positive.

As a further independent summation order, the audit first takes the
absolute value of each original occurrence weight and only then groups
these positive weights by height. Reconstructed exact lower/upper widths
agree with every saved generator row. All upper endpoints are <=2^-60,
and 2^-60<2^-38. Generator 28 is the maximum; its complete rational
endpoints were inspected at `/worst_width_bounds` in the new audit report.
All individual radius-allocation comparisons also pass. The actual term
count is 98*4860=476280<=1000000, with every H=4860. None of these checks
claims cutoff minimality or includes finite-sum arithmetic errors.

The audit separately reconstructs L054's two selected dyadic contributions
at generator 28, primitive IDs 34 and 5, with weights -1/6,+1/6.
Their sum remains
684547143360315392/166638467572977606763020498997 > 2^-38,
and agrees exactly with the historical report. This lower contribution
to the old majorant is compatible with the sharper new upper bound;
neither is a lower bound for true Fourier error. SHA-256 checks before
and after show that all 16 selected original certificates, reports and
ATTEMPTS/025--028 retain their bytes. No old evidence was overwritten.

Reproduce the entire new audit with:

    python3 scripts/conductor36-table/audit_exponential_plan.py

The fresh replay is `scripts/conductor36-table/exponential_audit_full_replay.json`;
the full distinct rational/integer evidence and all 72 alternate sums
are `scripts/conductor36-table/exponential_audit_containment.json`;
actual/required counts, exact maximum endpoints and zero-failure outcome
are `scripts/conductor36-table/exponential_critical_audit.json`.
This validates only the fixed feasibility claim under the stated supplied
inputs. The old production report is preserved and its historical
"separate critical audit" unperformed label is superseded by this section.
N=36 structural and L053/L054 instance audits remain pending. No finite
sums, signed integration quotient, integer isolation or table is supplied.

## Mathlib

Full matching fixed workload certificate: not checked. Supporting
interval arithmetic, Taylor remainder, positive exponential powers,
Fourier-tail and total-period formalizations: not checked. Unknown
coverage is not evidence of absence. The sources and complete finite
replay support this informal known-method specialization only.
