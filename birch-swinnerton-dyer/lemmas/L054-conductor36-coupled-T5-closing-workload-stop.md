# L054 — exact coupled T_5 closing and a fixed-cutoff obstruction

## Hypotheses

Use L050's minimal E: y^2=x^3+1, exact conductor N=36 and associated
normalized weight-two newform f with trivial character. Use L038's saved
complete integral relative presentation in
`scripts/conductor36-table/presentation.json`, with all 72 original
oriented generators and 144 endpoint occurrences. This structural
instance has complete production replay; its separate critical audit
remains pending. Use audited L049's full good-prime Hecke identity,
ordinary Gamma_0(36) transportation and conservative Fourier tail, and
audited L051's coefficients through 4860 and positive total minimal period.
Retain the twelve representatives specified by L053's finite plan in
their saved order. The assignments needed here pass the separate geometry
audit below; L053's unrelated ell=37 workload audit remains pending.

The assertion concerns only `scripts/conductor36-table/coupled_plan.json`:
T_5 closing, the saved representatives, ordinary transporting matrices
and balanced points, and the uncombined absolute-occurrence error rule.
The execution thresholds are maximum cutoff 4860, total distinct
primitive terms 1000000 and normalized two-sided tail width <=2^-38
for each original generator. No analytic sums or central vanishing are
assumed.

## Conclusion

All 72 Hecke images, including six actual infinity images, close on the
twelve saved classes. The exact coupled primitive equations have a
unique consistent solution with the infinity primitive fixed at zero.
The independent complete plan replay has zero certificate failures:
67 endpoint assignments, 139 matrices/inverses, 278 positive interior
points, 144 endpoint compositions, 72 generator rows and 98 primitive
tail/cutoff tests. It yields

    normalized rank = 12,
    max H = 5358 > 4860,
    sum H = 149244 <= 1000000,
    max normalized two-sided tail width
      = 454863562364420096 / 166638467572977606763020498997
      <= 1/274877906944 = 2^-38.

The cutoff threshold fails. More strongly, assigning H=4860 to every
fixed primitive makes the same conservative width bound for generator
28, {-1/27,0}, exceed 2^-38. No smaller cutoff allocation can satisfy
that bound on these fixed points and occurrences. This is failure of a
particular certified upper-bound convention, not a lower bound on true
analytic error or a universal integration obstruction. No new Fourier
sums, full normalized table, integer isolation, coefficient or BSD
comparison is supplied. This finite known-method specialization has
complete production replay and passes the separate geometry audit below,
under the supplied L038 structural-instance qualification.

## Proof

**Known imports and changed finite scope.** The unchanged prior
SPECIALIZE assessment is
`drafts/literature/2026-10-12-conductor36-coupled-small-prime-closing.md`.
Import Cremona, *Algorithms for Modular Elliptic Curves*, corrected
second edition (1997), [Proposition 2.2.3 and proof, pp.16--17;
(2.4.1) and integration pairing compatibility, pp.18--19;
(2.9.1) and arbitrary-cusp remark, pp.31--32](https://johncremona.github.io/book/fulltext/chapter2.pdf).
Import Wuthrich, *Numerical modular symbols for elliptic curves*,
[arXiv:1608.06423v2, 23 March 2017, equation (2), Lemma 4 and its
proof pp.6--7; Section 5.1 (11), pp.11--12;
Section 5.2, pp.12--13](https://arxiv.org/pdf/1608.06423v2),
with audited L049's orientation and sign convention. The full Hecke
identity requires only a good prime; ell=5 is good since 5 does not
divide 36. It need not preserve each individual cusp class. Same-class
scalar closing from L053 is replaced by the finite coupled system.
These analytic identities are imported, not reproved. The sources do
not supply this matrix's inverse or workload. Exact assembly,
elimination, infinity consistency and full finite-bound replay are the
approved specialization; no new algorithm or general solvability
theorem is claimed.

**Complete domain and transports.** The reused independent L038
structural verifier replays all relations, saturation witnesses,
transforms/inverses, generator coordinates and original/reflected paths.
It gives 72 original generators, 144 relations, saturation rank 59 and
free rank 13, including all 144 paths and 626 segments. Every actual
structural check count equals its required count. The plan verifier
rebuilds all 67 distinct endpoints and the cumulative representatives:

    s_0,...,s_11 = infinity, 0, -1/2, -1/3, 1/3, -1/4,
                  -1/6, 1/6, -1/9, -1/12, 1/12, -1/18.

For reduced homogeneous cusps (a,m),(p,q), including (1,0), Cremona's
criterion is existence of a unit u modulo 36 with
q=u m modulo 36 and u p=a modulo gcd(m,36). The verifier enumerates
all twelve units for every assignment. All 66 distinct representative
pairs are inequivalent, with every failed unit's residues saved. Every
endpoint and every reduced Hecke image has exactly one representative.
For each finite s_i it reconstructs all six images 5s_i and
(s_i+j)/5, 0<=j<5, using reduced fractions. For infinity all six
images are infinity; these six occurrences and their transports remain.

For source s=a/m, image v=p/q assigned to s, the retained witness has
Bezout solutions a s_s-m t_s=p s_v-q t_v=1 and

    gamma = [p t_v; q s_v] [1 t; 0 1] [s_s -t_s; -m a],
    C = q s_s-m s_v-t m q.

The verifier independently multiplies these matrices, checks both
Bezout equations, determinant one, 36|C, the homogeneous cusp image
and both inverse products. It checks the adjacent congruence choices
have no smaller |C| in this family. For C!=0 take
tau=-D/C+i/|C|, gamma tau=A/C+i/|C|; for C=0 take tau=i.
The full rational Mobius formula verifies every image and both positive
heights. For C=0, A=D=+/-1 and gamma z=z+B/D with integer B/D;
Fourier periodicity makes the correction exactly zero. All 34 such
corrections remain witnessed. Integer real-coordinate shifts identify
only Fourier-periodic equal points. The 98 distinct keys account for
every nonzero correction, and all occur in the full generator plans.

**Hecke eigenvalue, coupled equations and infinity.** Independent
enumeration on the target at five gives y-lists

    x=0,1,2,3,4: [1,4], [], [2,3], [], [0].

Including infinity, #E(F_5)=6, so a_5=6-6=0. The audited coefficient
segment agrees at five; no point count is transferred from another
curve. Use P(z)=sum_(n>=1) a_n exp(2*pi*i*n*z)/n,
P(infinity)=0, with A_f({a,b})=P(b)-P(a). Cusp limits exist by
cuspidality. Put u_i=P(s_i). If v is a Hecke image assigned to s_j,
with gamma(s_j)=v, imported transportation gives

    P(v)=u_j+d_v,  d_v=P(gamma tau)-P(tau).

The full Hecke identity, all six infinity images retained, gives
a_5 u_i=sum_(v image of s_i) P(v). Let A_ij count images of s_i
assigned to s_j and d_i=sum_(v image of s_i) d_v. Thus

    M u=d,  M=a_5 I-A.

Complete fraction reduction and assignment give A=6S, where S is the
permutation matrix (S u)_i=u_(sigma(i)) and

    sigma=(0,1,2,4,3,5,7,6,8,10,9,11).

Every row's six images go to the stated class. Since sigma is an
involution, S^2=I, M=-6S and M^(-1)=-S/6. Hence the full twelve-row
system is uniquely solvable, with u_i=-d_(sigma(i))/6. This explicit
finite inverse is independently checked by the saved rational witnesses;
no spectrum assumption is used.

The infinity row is -6u_0=d_0. All six infinity corrections are
witnessed integer translations, so d_0=0. Therefore the unique solution
has u_0=0. Appending this actual normalization yields N=[M;e_0^t],
not a free-variable choice. The certificate saves rational E,E^(-1)
with both inverse products I_13 and E N=[I_12;0], proving rank 12.
For one formal variable per nontranslation Hecke correction, let B be
its 13-row RHS coefficient matrix: the first twelve rows retain every
occurrence, and the last normalization row is zero. There are 52 such
variables. The verifier reconstructs B, checks all entries of E B,
its last row is zero, its infinity solution row is zero, and
N (E B)_(first twelve rows)=B. This checks consistency as an identity
before numerical evaluation, including the full infinity Hecke equation.
The saved solution-equation weights are the first twelve rows/columns
of E and satisfy M W=I_12. The infinity row of W is -e_0^t/6, while
its actual RHS d_0 is zero. Infinity is never replaced by a finite cusp.

**Full endpoint weights and tails.** For every original endpoint r
assigned to s_i retain P(r)=u_i+P(gamma_r tau_r)-P(tau_r).
Substitute the entire solved representative expression and apply signs
-1,+1 to the two original endpoints. The independent verifier rebuilds
every occurrence and rational weight for all 72 original generators,
all 144 endpoint compositions, and every signed equal-key coefficient.
Errors use the sum of absolute uncombined weights, including repeated
occurrences; caching and signed cancellation do not reduce that sum.
Its maximum is W_max=22/3.

The independent positive-period replay rechecks audited L051's Machin
pi enclosures, positive roots and twelve outward AGM updates for the
minimal target. Its connected real locus requires component factor one.
The exact positive lower bound is

    Omega_lower=166638467572977606763020498997 / 2^95.

No period or scale is inferred from the unknown integration table.
Using L049's unchanged conservative full tail, set

    R_H(y)=2^(-floor(6Hy))/(6y),
    rho=2^-38 Omega_lower/(2 W_max)
       =499915402718932820289061496991
        /479117572624681356556431447263929641730048.

For every required positive rational height, choose the first H with
R_H(y)<=rho. Complete replay checks this inequality and failure at H-1
for all 98 keys, reconstructs their full sum H, and checks for every
generator g

    width_g=(2/Omega_lower) sum_occurrences |w_j| R_(H_j)(y_j)
            <=2^-38.

These are tail planning widths only; finite-function and new normalized
division errors remain unexecuted. The certificate does not claim an
analytic interval containing each new generator value.

**Exact cutoff obstruction.** A worst primitive is
x=-289/684, y=1/684, H=5358 and R_H=57/70368744177664.
The load-bearing transport maps -1/9 to 26/45 with

    gamma=[-395 -41; -684 -71],
    tau=-71/684+i/684,
    gamma tau=395/684+i/684.

The image's integer shift is one. This and its tau have primitive IDs
5 and 34. They occur with weights +1/6 and -1/6 in generator 28,
{-1/27,0}. Complete replay checks that row's entire occurrence list,
then reconstructs every generator width with every cutoff set to 4860.
Already the two identified contributions give

    (2/Omega_lower)(1/6+1/6) R_4860(1/684)
      =684547143360315392 / 166638467572977606763020498997
      >1/274877906944.

Here floor(6*4860/684)=42. The last strict inequality is checked by
exact integer cross multiplication; the full capped width and selected
contribution are saved in the report's `cutoff_obstruction`. Since every
term in the conservative sum is nonnegative and R_H is nonincreasing
in H, any allocation with all H<=4860 has at least these contributions.
Thus the same upper-bound rule cannot certify the threshold on these
fixed points. This is not an assertion that the true analytic error
exceeds that threshold. A sharper estimate or different geometry is
outside this tested convention, and remains possible.

Reproduction commands are

    python3 scripts/conductor36-table/build_coupled_plan.py
    python3 scripts/conductor36-table/verify_coupled_plan.py

Full evidence is `scripts/conductor36-table/coupled_plan.json` and
`scripts/conductor36-table/coupled_plan_verification.json`. The verifier
imports no producer; it reuses the unchanged structural verifier and
independent period replay only. All coupled assignments, matrix products,
equations, solution weights, endpoints and tail tests are independently
reconstructed. Zero certificate failures coexist with one threshold
failure: maximum cutoff. L053's ell=37 stop and ATTEMPTS/025--027 remain
preserved. Audited L052's clearing integer 24 is downstream only and is
not used in this proof. CM still excludes this curve from L027; no
uniform coefficient, rational-direction, Sha or complex-order input is
produced. Arbitrary-curve BSD remains unresolved.

**Separate geometry critical audit, 2026-10-12, BSD-186.** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-12-conductor36-coupled-geometry-critical-audit.md`.
This audit passes for exactly the supplied full-relative N=36 domain.
It imports the precise Cremona/Wuthrich identities cited above and the
audited L049 orientation; the finite specializations, not those standard
theorems, are independently checked. The producer, its reused transport
constructor, the complete verifier and its positive-period replay were
compared with the mathematical contract. No producer was executed or
imported by the new audit.

The full existing replay is saved separately in
`scripts/conductor36-table/geometry-critical-audit/complete-replay.json`.
It checks all 67 endpoint assignments, 66 representative comparisons,
72 Hecke images, 139 matrices and both inverses, 278 positive points,
13 normalized equations, 52 formal RHS variables, 144 endpoint
compositions, 72 complete generator rows and 98 dyadic cutoff tests.
All required structural counts pass and all 626 segments replay; this
reuses the supplied presentation and does not replace its pending
separate structural critical audit. The period replay retains all
positive branches, twelve AGM updates and component factor one.

A distinct reconstruction in
`scripts/conductor36-table/audit_coupled_geometry.py` uses extended
Euclid and Cremona Proposition 2.2.3's equivalent divisibility criterion
rather than the verifier's unit-residue test. For s=a/m, v=p/q, choose
Bezout integers a*s_s-m*t_s=p*s_v-q*t_v=1. Equivalence is tested by

    gcd(m*q,36) dividing q*s_s-m*s_v.

This includes m=0 or q=0 and is independent of the chosen Bezout
solutions: changing either changes the expression by a multiple of m*q.
The cumulative list and every image assignment reproduce the saved
representatives. All 67 L053 endpoint assignments and complete geometric
witnesses agree with L054; their different primitive-cache indices are
compared by exact point keys, including lengths, not by numerical index.
The ell=37 closing/workload portion of L053 is outside this audit.

The fresh Hecke images reconstruct the exact permutation sigma displayed
above. For each row six images go to sigma(i); sigma squared is the
identity. Thus M=-6S and W=-S/6 are verified directly without the saved
elimination transform. Every saved solution weight agrees. The existing
replay independently checks both rational elimination inverse products,
E*N=[I;0], the full transformed formal RHS and consistency. The two
checks address different witnesses for the same finite inverse.

For the connection to actual analytic values, every directly checked
Gamma_0(36) matrix supplies the imported identity
P(v)=u_j+P(gamma*tau)-P(tau). For C!=0 the new reconstruction obtains
both primitive keys directly from (-D/C,1/|C|) and (A/C,1/|C|), reducing
only by an integer translation. It does not use saved point IDs to build
the weights. For C=0 it verifies A=D=+/-1 and integral B/D, so the
correction is exactly zero by Fourier periodicity. In particular all
six infinity corrections vanish; d_0=0 and u_0=-d_0/6=0 are actual
analytic identities, not an arbitrary formal normalization.

Writing each d_i as its entire ordered primitive-occurrence list, the
new reconstruction takes u_i=-d_(sigma(i))/6 and verifies M*u=d on
all 98 primitive coordinates. It then appends each endpoint's own
transport correction and forms P(b)-P(a) for every original generator.
All 144 endpoint compositions and all 1316 uncombined signed occurrences
agree, as do the complete combined rows and absolute weights. The
uncombined list controls errors even when coordinates cancel. Full
reconstruction evidence, including every row, is
`scripts/conductor36-table/geometry-critical-audit/independent-identities.json`.
These exact identities justify the analytic specialization; formal rank
or numerical relation agreement alone would not.

The dyadic obstruction replays unchanged: the selected contributions
684547143360315392/166638467572977606763020498997 exceed 2^-38 at
H=4860. All 98 original minimal-cutoff tests and 72 full width comparisons
pass with max H=5358 and total H=149244. This remains an obstruction to
this upper-bound convention only. No downstream sharper-tail conclusion
is used as an input to the geometry audit.

Four in-memory altered-evidence cases (endpoint assignment, missing
infinity image, inverse sign and occurrence sign) are rejected. The full
results, exact obstruction and before/after hashes are in
`scripts/conductor36-table/geometry-critical-audit/report.json`; every
original input and failure record hashed there is byte-for-byte unchanged.
An initial audit-harness failure is retained separately: it incorrectly
required identical structural count dictionaries, although `segments`
is an additional actual-count field. Comparing every required field and
the explicit 626-segment count resolves that harness issue; no original
certificate or mathematical claim required repair. These rejection tests
supplement the complete mathematical/code review, not a universal
software correctness claim. Reproduce with

    python3 scripts/conductor36-table/audit_coupled_geometry.py

This establishes the fixed geometry/weight input only. No Fourier sums,
signed normalized division, rational isolation or full table is produced;
L038's structural critical audit and all stated BSD gaps remain open.

## Mathlib

Full matching coverage of this composed coupled algorithm and finite
workload certificate was not checked. Supporting source/Mathlib
qualifications in L049 and L051 are retained. No absence or generic
software correctness is inferred from unknown coverage. The fixed geometry
audit above does not change this formal-coverage qualification.
