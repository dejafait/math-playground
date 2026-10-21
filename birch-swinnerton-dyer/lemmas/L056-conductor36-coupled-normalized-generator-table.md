# L056 — complete fixed conductor-36 normalized generator table

## Hypotheses

Let E be L050's globally minimal curve y^2=x^3+1 with differential
dx/(2y), exact conductor 36 and associated normalized weight-two
trivial-character elliptic newform f. Let Omega(E) be its total real
minimal period. Use the audited N=36/P-empty instance of L038's complete
integral relative module modulo torsion, with the 72 original oriented
generators in `scripts/conductor36-table/presentation.json` order.
Use audited L049's recovery framework, L051's exact coefficients through
4860, reduced-phase arithmetic and independent positive total period,
and L052's all-cusp clearing integer 24. Use L054's audited fixed coupled
T_5 geometry, infinity normalization and all uncombined occurrences,
and L055's audited H=4860 full-exponential tail plan.

The assertion concerns the new finite evidence in
`scripts/conductor36-table/table_certificate.json` and its 98 referenced
term files. Earlier structural and geometric audits are imported only
in their approved fixed-instance scope; no generic implementation
correctness, non-CM hypothesis or rank assertion is assumed.

## Conclusion

For every original generator g_i={a_i,b_i}, 0<=i<72, define

    F(g_i)=Re(2*pi*i integral_(a_i)^(b_i) f(z) dz)/Omega(E).

The complete normalized table is F(g_i)=m_i/24, with this vector in the
saved presentation order:

```text
[-4, 4, 0, 8, 6, 4, 0, 2, 0, 4, 0, -4,
 0, -2, 0, -4, -6, -8, 0, -4, 0, -8, -6, -4,
 0, -2, 0, -4, 0, 4, 0, 2, 0, 4, 6, 8,
 0, -8, -2, 4, 4, 4, 4, 4, -2, -8, -6, 2,
 -2, 6, 6, -2, 2, -6, -4, 2, -4, 8, -4, 8,
 -4, 2, -4, -2, -2, 0, -4, 4, 0, 2, 2, 4]
```

All 72 actual containing intervals have width at most

    27940579275/39614081257132168796771975168 <= 2^-60 < 2^-38.

Every scaled interval isolates its integer, including all 16 zeros.
Every source relation, saturated column and quotient reconstruction
passes exact replay. The least common multiple of the reduced generator
denominators is 12; consequently 12F is integral on the full relative
module, including every rational cusp-pair path. Complete independent
production replay passes under the stated source imports. This is fixed
known-method reproduction; its separate fixed critical audit below passes.
It supplies no coefficient, rational point, Sha or complex-order result,
and no BSD candidate. CM still excludes the L027 application.

## Proof

**Known inputs and specialization.** The assessment saved before this
attempt is `drafts/literature/2026-10-12-conductor36-coupled-generator-table.md`,
DECISION SPECIALIZE. It approves exactly this finite table execution.
Import Wuthrich, *Numerical modular symbols for elliptic curves*,
[arXiv:1608.06423v2, 23 March 2017, equation (2), Lemma 4 with
complete proof pp.6--7, Section 5.1 (11) pp.11--12 and Section 5.2
opening identity p.12](https://arxiv.org/pdf/1608.06423v2).
For P(z)=sum_(n>=1) a_n exp(2*pi*i*n*z)/n,
A_f({a,b})=P(b)-P(a), and the omitted tail at positive height y after
H terms has modulus at most q^(H+1)/(1-q), q=exp(-2*pi*y).
The full good-prime identity applies since 5 does not divide 36;
no same-class shortcut or semistable complexity theorem is used.
L054 already supplies the unique actual coupled solution with infinity
primitive zero, every transport and every oriented occurrence. These
identities are imports, not new results or reproofs in this attempt.

The complete integral domain is L038, using Cremona, *Algorithms for
Modular Elliptic Curves*, corrected second edition (1997),
[Propositions 2.2.1--2.2.3 pp.15--17, integration pairing pp.18--19,
coefficient recurrences (2.6.1)--(2.6.2) p.25 and arbitrary-cusp remark
after (2.9.1) pp.31--32](https://johncremona.github.io/book/fulltext/chapter2.pdf),
and Stein, *Modular Forms: A Computational Approach*, GSM 79 (2007),
[(3.2.1), Propositions 3.10--3.11 and Theorem 3.13
pp.40,42--44](https://wstein.org/books/modform/stein-modform.pdf).
Composite level and boundary directions are retained. L050 proves the
arithmetic hypotheses, and the new verifier independently reconstructs
all 648 good-prime counts, 1454362 x-checks, 4859 factorizations and 4861
coefficient entries (including a_0=0). The global coefficient bound
in the tail is the imported theorem, not a finite-segment inference.

Use L051's Machin identity and standard Taylor theorem with
[DLMF 4.19.2](https://dlmf.nist.gov/4.19#E2) and
[4.2.19--4.2.22](https://dlmf.nist.gov/4.2#iii), version 1.2.8,
for the real finite arithmetic. The independent minimal-target period
is the already audited specialization of Cremona,
[Section 3.7 (3.7.1), pp.97--98](https://johncremona.github.io/book/fulltext/chapter3.pdf),
and [DLMF 19.8.1--19.8.5](https://dlmf.nist.gov/19.8.i).
L052's all-cusp integer 24 is a theorem input independent of the table:
the origin-preserving degree-one X_0(36) model identification, the
cube-free differential theorem and good split torsion reduction give
12 times every cusp difference in the minimal period lattice, whose
real projection is (Omega/2)Z. Its precise citations and full applicability
proof remain canonical in L052. Neither the old -1/12 recovery nor
the new table is used to establish that integer. All source hypotheses
are unchanged; no new theorem discovery or novelty claim is made.

**Full finite containment.** Put D=2^96. An interval [L,U] represents
[L/D,U/D]. Multiplication uses the minimum and maximum of all four
endpoint products with lower floor and upper ceiling; exact rational
scaling uses both signed endpoints and the same outward rounding.
Addition is exact at this scale. Induction proves containment for every
finite operation, even with repeated variables. The producer uses integer
numerators and denominators; the verifier reconstructs operations from
Fraction endpoints and imports no producer. Every saved finite term and
partial sum is checked, rather than checking only terminal sums.

For every point x+iy and every n=1,...,4860, reduce nx exactly modulo
one into s in [-1/2,1/2). All required phase keys are reconstructed from
all 98 actual point keys, and there are exactly 3744 distinct phases.
Enclose theta=2*pi*s and check |theta|<=4. Starting at t_0=S_0=1,
perform all forty updates

    t_k=-t_(k-1)*theta^2/((2k-1)(2k)), S_k=S_(k-1)+t_k.

This is cosine's degree-80 Taylor polynomial. The absolute degree-81
remainder is bounded by 4^81/81! because every real cosine derivative
has magnitude at most one. Enlarge S_40 by ceil(D*4^81/81!) on both
sides. All 149760 term/partial-sum steps, arguments, squares, remainders
and radii are saved and replayed. Periodicity justifies the exact reduction,
including the boundary -1/2; caching identifies only equal rational phases.

At every one of the sixteen required positive heights, 0<y<=1, use
L055's fully replayed degree-160 exp(-2*pi*y) bracket q=[q^-,q^+].
Its argument is in [-8,0), its saved remainder is 3^8*8^161/161!, and
0<q^-<=q^+<1 is checked without clipping. The new verifier calls the
unchanged full tail verifier read-only; it checks all 2560 attenuation
Taylor steps and all 336 binary-power multiplications, in addition to
the complete structural, geometric and independent-period replay.

For each point separately, initialize power=1 and sum=0. For every
n=1,...,4860, including a_n=0, compute outwardly

    power <- power*q,
    product <- power*cosine(s),
    term <- (a_n/n)*product,
    sum <- sum+term.

The first update contains q^n by induction. The remaining operations
contain the corresponding real Fourier summand and its full partial sum.
Each point file saves [n,phase_id,power,product,term,sum] for every n.
Replay reconstructs exactly 4860 records per required point, checks
their order, phase use, operations, terminal power and sum, and rejects
extra or missing terms. All 476280 records are visited, including
423360 zero-coefficient records. Every phase and attenuation is used.
The total workload 476280<=1000000 is checked, not extrapolated.

For each point, L055's checked q^4861/(1-q) upper radius R is rounded
outward to r=ceil(DR). Enlarge the new finite sum by [-r,r]. Wuthrich's
full tail theorem controls all omitted coefficients, so this gives a
containing real P(x+iy) interval. No infinite limit is interchanged
with the finite verification, and no lower tail-majorant endpoint is
mistaken for a lower bound on true error. The dyadic stop remains valid
for its original convention and its original files are preserved.

**Signed geometry, period division and integer existence.** For each
of the original 72 generators, L054's full ordered list (j,w_j) expresses
Re(P(b)-P(a)) as sum w_j Re(P(z_j)). Apply every occurrence to the new
containing intervals by signed scalar multiplication and outward addition.
All 1316 uncombined occurrences, intermediate terms and partial sums are
saved and reconstructed. Repeated keys are not combined to reduce their
absolute error contribution. The analytic connection comes from L054's
actual transports and coupled solution; relation agreement alone cannot
provide it. Infinity is exactly zero and translation corrections retain
their original zero witnesses.

The positive independent total-period interval is

    [166638467572977606763020498997/2^95,
     166638467572977606763020499043/2^95].

Replay reconstructs Machin's full alternating brackets, the one-real-root
factorization (x+1)(x^2-x+1), both positive square-root branches and all
twelve AGM updates. Negative discriminant gives one real component;
there is no additional total-period factor or unknown integration scalar.
For each containing integral interval take all four integral/period
endpoint quotients, then round outwards at scale D. This remains valid
for positive, negative and zero-crossing numerators. All 288 exact quotient
endpoints and all 72 actual widths are reconstructed.

L052 gives 24F(g_i) in Z before numerical recovery. For each resulting
J_i=[l_i,u_i], the full checks give

    ceil(24 l_i)=floor(24 u_i)=m_i.

Thus the sole existent integer in 24J_i is m_i, and F(g_i)=m_i/24.
Width alone is not used for existence or rounding to an expected value.
The producer has no expected integers. The widest row is i=28,
{-1/27,0}, and its exact interval is

    [-6982778963/19807040628566084398385987584,
      13975021349/39614081257132168796771975168].

It crosses zero and its two scaled endpoint tests both isolate zero.
Its width is the maximum stated in the conclusion. Exact integer
cross multiplication checks that maximum <=2^-60<2^-38. All other
rows also isolate their integers, including all sixteen zero rows.

**Relations and the full quotient.** After recovery, exact rational
evaluation of every one of the 144 source relation rows is zero.
Evaluation on all 59 saturated-kernel columns is zero. The saved
integral quotient section has thirteen columns; evaluating the recovered
functional on them gives, in the saved basis order,

    [1/6,-1/3,1/12,1/12,-1/12,-1/12,0,-1/6,1/6,0,1/12,1/12,1/6].

Every original generator is reconstructed from its complete integral
quotient coordinates and these thirteen values, and agrees with its
independently isolated value. Both the lattice witnesses and actual
relation evaluations are replayed. The least common multiple of all
72 reduced denominators is 12 (zero has denominator one), and a table
entry of denominator 12 occurs. Integral generation therefore gives
12F(M) contained in Z on the full relative module. This is a fixed exact
normalized functional, not a p-adic coefficient computation or BSD rank
certificate.

**Evidence, bounded rejection checks and qualifications.** Reproduce
from the active notebook with

    python3 scripts/conductor36-table/build_table.py
    python3 scripts/conductor36-table/verify_table.py
    python3 scripts/conductor36-table/check_table_rejection.py

The manifest is `scripts/conductor36-table/table_certificate.json`;
all full per-term records are `scripts/conductor36-table/table-data/point-NNN.jsonl`;
the independent full report is `scripts/conductor36-table/table_verification.json`.
The latter contains every actual normalized interval/isolation, every
relation image, complete quotient reconstruction and source-replay checks.
No finite or threshold failure occurred. Two separate altered manifests
delete a required phase and corrupt a partial sum with malformed endpoints;
both are rejected, with full altered inputs and tracebacks in
`scripts/conductor36-table/table-replay-rejections/`. Preservation hashes
confirm unchanged original table, all 98 term files and the selected
historical input/report bytes during these rejection checks. These are
bounded production-replay checks, not a separate critical audit or a
universal software correctness theorem.

The result closes this fixed table construction gap under the cited
inputs. Independent gaps remain arbitrary arithmetic production,
useful coefficient nonvanishing, rational Kummer directions, Sha and
complex-order comparison. This curve is CM, so the non-CM premise of
L027 is unavailable. The entire BSD notebook stays IN_PROGRESS.

**Separate fixed critical audit, 2026-10-13, BSD-192.** The prior
SPECIALIZE assessment
`drafts/literature/2026-10-13-conductor36-coupled-table-critical-audit.md`
authorizes exactly the unchanged table audit. Reuse the precise primary
imports above and the completed L038 N=36/P-empty, L049, L051, L052,
L054 and L055 audits. In particular L054 uses the full coprime T_5
identity, not a same-class shortcut; its endpoint-assignment scope is
sufficient without L053's unrelated ell=37 workload. The all-cusp
integer 24 is established before recovery, independently of any table
value. L050 supplies the exact minimal curve and conductor. No new source
hypothesis, geometry, coefficient range or analytic error method is used.

The entire new producer and verifier were reviewed against the analytic
contract, including the invoked tail, geometry and period contracts and
the already audited structural-verifier interface. Fresh complete replay
is saved to `scripts/conductor36-table/table-critical-audit/full-replay.json`.
It checks every required point, height and phase, all 476280 ordered term
records (including 423360 zeros), all 149760 cosine Taylor steps, sixteen
attenuation brackets, 2560 attenuation Taylor steps, 336 tail-power
multiplications and 98 full tails. All coefficient counts/factorizations,
Machin brackets and positive AGM operations replay. All 1316 uncombined
signed occurrences, 288 period quotients, 72 isolations, 144 source
relations, 59 saturated columns, thirteen quotient values and 72
reconstructions pass. Required structural counts also match; the 626
segments replay. No original report is overwritten. The nested upstream
reports' historical `table_complete: false` and `unperformed` fields
describe their original planning scope, not this new completed replay.

Distinct load-bearing checks use `scripts/conductor36-table/audit_table.py`,
which imports neither producer nor replay implementation. For each of
all 3744 phase arguments [a,b], let c=(a+b)/2 and delta=(b-a)/2. Exact
rational Horner evaluation gives

    P(c)=sum_(k=0)^40 (-1)^k c^(2k)/(2k)!.

The script evaluates this polynomial from the highest degree downwards,
with no dyadic operation rounding. The complete exact rational values are
saved in `scripts/conductor36-table/table-critical-audit/cosine-containment.json`.
The independently checked interval for 2*pi*s lies in [a,b] subset [-4,4].
The already assessed real Taylor theorem gives |cos(c)-P(c)|<=4^81/81!,
and |cos(t)-cos(c)|<=|t-c| for real t gives the containing bracket

    [P(c)-delta-4^81/81!, P(c)+delta+4^81/81!].

Every one of these brackets is contained in its saved cosine bracket.
Thus this check bypasses the rounded square/term/partial-sum recurrence
while retaining its actual argument uncertainty and Taylor remainder.
It supplements complete replay; a numerical point approximation or
overlap test alone would not suffice.

For every generator the distinct script next sums the individual signed
primitive-interval endpoints exactly over Q, with no intermediate
rounding and with every repeated occurrence retained. Write this interval
as [a,b] and the independent positive period interval as [p,q], p>0.
It uses the sign cases

    a>=0: [a/q,b/p]; b<=0: [a/p,b/q]; a<0<b: [a/p,b/p].

These are the extrema of u/v on the indicated rectangle, so each contains
the actual normalized integral. Each exact sum is inside the saved
integral interval, and each sign-case quotient is inside the saved
normalized interval. There are 28 positive, 28 negative and sixteen
crossing cases. Independently, all 288 saved quotient equations are
checked by exact cross multiplication. Finite enumeration in each
exact scaled interval produces one integer m, agreeing with the saved
value, and the original wider interval [l,u] satisfies

    m-1 < 24l <= m <= 24u < m+1.

These strict adjacent-integer exclusions establish uniqueness directly,
without relying on the saved ceil/floor assertions. Existence still
comes from the all-cusp theorem and analytic containment, not from
rounding. All sixteen zero rows pass. The actual maximum width remains
27940579275/39614081257132168796771975168 <= 2^-60 < 2^-38.

At integer scale 24, column accumulation independently gives zero on
all 144 source relations and 59 saturated columns. The thirteen integral
quotient numerators reconstruct every recovered integer. Reduction by
24/gcd(24,m_i) gives common denominator 12, including denominator one
for zero. Complete signed traces, direct inequalities and integer
relation witnesses are saved in
`scripts/conductor36-table/table-critical-audit/signed-isolation-and-relations.json`;
the distinct report is `scripts/conductor36-table/table-critical-audit/distinct-report.json`.
No expected table vector enters these checks.

Four additional bounded altered-evidence cases use the unchanged full
verifier. Each altered certificate and failure is retained under
`scripts/conductor36-table/table-critical-audit/rejections/`:

- Removing point 0's final term rejects with the failed count
  (0,4859,4860,"missing terms").
- Shifting both endpoints of point 0, term 4860's partial sum by one
  integer unit at scale 2^96, retaining a well-formed ordered interval,
  rejects (0,4860,"finite operation mismatch").
- Adding 2^-96 to generator 28's first recorded quotient, a zero-crossing
  case, rejects at the quotient-endpoint equality.
- Changing the last recorded source-relation image to 1/24 rejects at
  the complete relation-record equality.

For the term cases the altered hash is updated, so hashing alone cannot
cause these rejections. New case directories refer read-only to unchanged
inputs, and every changed term file is separate. The rejection report
records four intended failures out of four required tests. Before/after
SHA-256 manifests cover all 98 original term files, original source code,
selected input certificates/reports and ATTEMPTS/025--028: all 152 files
remain byte-identical. The old dyadic cutoff failure is preserved.
These finite adversarial checks do not establish general verifier
correctness; they supplement the mathematical audit and exhaustive replay.

Reproduction commands for the separate audit, from the active notebook:

    python3 scripts/conductor36-table/verify_table.py scripts/conductor36-table/table_certificate.json scripts/conductor36-table/table-critical-audit/full-replay.json
    python3 scripts/conductor36-table/audit_table.py
    python3 scripts/conductor36-table/audit_table_rejections.py

The rejection script creates new case directories and deliberately refuses
to overwrite existing ones. The preserved before/after manifests and
existing rejection inputs allow inspection without rerunning it. Full
replay and the distinct script can be rerun with unchanged inputs.
The audit passes for this fixed normalized functional only, under the
named source inputs. It produces no additional table value or theorem
beyond the checked known methods, and changes none of the stated BSD,
CM, software-generality or Mathlib qualifications.

## Mathlib

Full matching coverage for this fixed coupled normalized-table certificate,
its complete numerical containment and independent replay has not been
checked. Supporting rational arithmetic is distinct from a theorem covering
the full elliptic/newform/period/denominator assembly. Unknown coverage is
not evidence of absence; no formal verification or novelty is claimed.
