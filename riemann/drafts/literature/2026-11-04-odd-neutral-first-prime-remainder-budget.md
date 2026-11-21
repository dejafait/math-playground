# Odd-centered first-prime remainder comparison — source-assessed specialization

TARGET: Test whether Q_2(f)<=R_B(f)/2 for every complex globally neutral f in C_c^infinity(0,4log3) whose centered function h(y)=f(y+2log3) is odd.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step302 searched odd/parity-sensitive Pitt and logarithmic uncertainty bounds, sine-transform and arithmetic-delay comparisons; inspected primary Gorbachev--Ivanov--Tikhonov sector results and checked the named local failure records. Exact queries, inspected ranges and unread leads appear below; no direct matching delay theorem or novelty certification was obtained.
SOURCE_EVIDENCE: Gorbachev--Ivanov--Tikhonov arXiv:1505.02958v1, Thm2.1 p.3, Cor3.2 p.6, definitions pp.1-2/4-5, sector proof (3.7)-(3.8) p.6 and differentiation proof (4.4)-(4.5) pp.7-8; corroborating arXiv:1507.06445v1 Cor4.2 p.11. Reuse Beckner math/0701939v6 Thm4/(12), p.5 and assessed complex/n=1 scope. NIST DLMF 5.5.4 supplies digamma reflection; L743 (1) fixes the coefficient.
COMPARISON: Sharp sector Pitt constants are known and explicitly cover the complex one-dimensional odd sector. This replaces an uncovered coercivity mechanism by a known input needing routine logarithmic specialization and Fourier scaling. No inspected theorem states the actual log2 delay allocation with this resource; L746's even counterexample and the prime-only/carrier stops do not settle the odd restriction.
GAP: Complete the source-specialization calculation, including differentiation justification, both Fourier conventions and the bounded complex shift comparison, before asserting the target. Even-sector control, full-energy corrections, other prime powers and support propagation remain independent gaps.
REASON: Essential source scope is accessible and the separate changed-parity comparison is now complete enough for one REPRODUCTION attempt. Cite the sector theorem rather than reprove a purported new odd uncertainty principle; the exact allocation remains unproved in this literature-only turn.
SCOPE: Only the exact TARGET at L=4log3: complex centered odd smooth tests, both global moments, actual coefficient, entire resource and half allocation. Permitted specialization uses sector identification, the cited Pitt family near parameter zero, justified differentiation, Fourier scaling, digamma reflection and Cauchy--Schwarz for the zero-extended delay. No full-energy sign, even-sector extension, numerical spectral certificate or singular endpoint test is authorized.
LITERATURE_REASON: Step302 resolves the essential changed-parity coverage missing at invocation; it reuses Beckner and does not repeat literature on an already-ready odd target. Further unchanged-scope browsing is unnecessary for the subsequent mathematical attempt.

## Exact proposed test and relevance

Use L746's definitions without altering the window or normalization:
a=log2, b=2log3, L=2b, c=sqrt(2)log2, h(y)=f(y+b), and

    Q_2(f)=c Re integral h(y-a) conjugate(h(y)) dy,
    R_B(f)=(1/4) integral integral
       |sqrt(|y|)h(y)-sqrt(|z|)h(z)|^2 /
                       (|y-z|sqrt(|yz|)) dy dz.

All integrals defining the resource are over the whole real line(s).
The proposed tests satisfy h(-y)=-h(y) and both exact constraints
integral_0^L exp(+-x/2)f(x)dx=0; they may be complex. These are
new restrictions of the already defined forms, not a claimed inequality.
The literal finite smooth class avoids any endpoint domain assumption.

The main gap remains unconditional actual-Xi mixed positivity. A valid
odd-sector payment could control that part of the first-prime term
within a later complete-energy argument, while leaving the even sector
and all complementary estimates unresolved. L746 makes the unrestricted
half allocation unavailable. Its even center mechanism cannot be
silently reused as an odd witness. Conversely no positivity on this
subclass would recover the unrestricted assertion or resolve RH.

Essential input IDs are L743 for the coefficient and L746 for the
precise resource and established even obstruction. L744 (6) is only
downstream energy context. L742's conditional conclusions and L745's
carrier theorem are not premises. No cross-notebook result is used.

## Separate source gate and discriminating test

Compare parity-improved logarithmic uncertainty/Pitt remainders and
the odd-sector translation form at theorem level, reusing the existing
Beckner scope assessment. In particular check exact constants, complex
scope, the centered odd condition and both moments before importing
any stronger inequality. The step299 working draft records an unused
odd-sector idea, not an established lemma or adequate source coverage.
The named half-budget, prime-only and carrier-span ATTEMPTS records
remain relevant comparisons, not global bans.

The step301 nomination required a separate source gate; step302 below
supplies that comparison under SPECIALIZE. A subsequent mathematical
step, after acceptance of this assessment, has the bounded decision test of a
proof of Q_2<=R_B/2 on the entire stated subclass or an actual smooth
exact-neutral odd witness with Q_2>R_B/2. A trial-space eigenvalue,
a real-only upper bound, or an omitted exterior/correction cost would
not decide the claim. If the necessary source scope is inaccessible,
record that specific blocker and park dependent mathematics.

The original step301 nomination supplied no estimate or source approval.
Step302 supplies source coverage only, without deriving the target or
resetting a mathematical budget. Full matching Mathlib coverage remains
unchecked. The subsequent task is a routine source-specialization
calculation, subject to the supervisor's acceptance of the changed gate.

## Step302: primary theorem comparison, 4 November 2026

### Known sector input and applicability

[Gorbachev, Ivanov and Tikhonov, *Sharp Pitt inequality and logarithmic
uncertainty principle for Dunkl transform in L2*,
arXiv:1505.02958v1](https://arxiv.org/pdf/1505.02958v1#page=6),
Corollary3.2, printed p.6, states for
u in S(R^d) intersect R_n^d(v_k), lambda_k=d/2-1+|k|,
and 0<=beta<lambda_k+1+n:

    || |xi|^(-beta) F_k u ||_(2,dmu_k)
        <= c(beta,lambda_k+n) || |x|^beta u ||_(2,dmu_k),
    c(beta,lambda)=2^(-beta)
        Gamma((lambda+1-beta)/2)/Gamma((lambda+1+beta)/2).

The formula is Theorem2.1, p.3. Complex scope and the unitary
exp(-i x.xi) Fourier convention are explicit on pp.1-2; k=0
recovers that transform. Sector definitions and the reduction
(3.7)-(3.8) were inspected on pp.4-6. At d=1, k=0, n=1,
the sphere consists of two points and the degree-one sector is
precisely odd functions; lambda_k=-1/2. These parameter choices are
within the stated hypotheses. Centered smooth zero extensions are
Schwartz; global moments only restrict the class. This is theorem
applicability, not the proposed arithmetic comparison.

The arXiv header/submission record says v1, 12 May2015; the retrieved
PDF's internal date says 19 May2018. Use the pinned identifier and
printed theorem numbers, without silently treating the internal date
as a new arXiv version. The source's Theorem4.1 proof, (4.4)-(4.5),
pp.7-8, provides the inspected differentiation template, including
integrability near zero and Schwartz decay. Reusing it for this sector
still needs an explicit justification in the mathematical step.

A separate primary cross-check is [the same authors, *Pitt's
inequalities and uncertainty principle for generalized Fourier
transform*, arXiv:1507.06445v1, Corollary4.2, printed p.11](https://arxiv.org/pdf/1507.06445v1#page=11).
It states the sector constant c(beta,lambda_k+n,a) for
0<=beta<lambda_k+a/2+n. The inspected Theorem4.1 has
a>0 and 4lambda_k+a>=0; a=2 recovers the Fourier setting.
Its general-space Theorem5.1 is not a stronger odd-sector statement.
Read the definitions on pp.1-2 and sector proof/statement on pp.10-11;
no generalized-transform result beyond this corroboration is needed.

[NIST DLMF 5.5.4](https://dlmf.nist.gov/5.5.E4), version1.2.8
(15 September2026), states
psi(z)-psi(1-z)=-pi/tan(pi z), z not an integer.
The later constant calculation may use it. No differentiated sector
constant, resource lower bound or allocation inequality is derived here.

### Exact difference left for mathematics

Reuse the prior Beckner assessment and [Theorem4/(12), printed p.5](https://arxiv.org/pdf/math/0701939v6#page=5).
The source statement was retrieved for comparison, without redoing its
assessed Appendix argument. Beckner uses exp(+2pi i x.xi); the sector
source uses unitary exp(-i x.xi). Their logarithmic constants cannot
be subtracted until the scaling and Plancherel factors are matched.
Keep the entire resource, including exterior pairs, and complex norms.

No inspected primary statement includes Q_2. The identified difference
is a routine specialization: justify the logarithmic passage for the
odd sector, match Beckner's normalization, and compare the resulting
resource constant with the actual shift using Cauchy--Schwarz. The
source covers more functions than the moment-constrained target;
neither moment may be silently replaced by cellwise neutrality.
Reprove none of Pitt's theorem, sharpness, or Beckner's identity.
Any successful consequence is REPRODUCTION of known machinery,
not a new uncertainty principle or a certified original result.

The continuation succeeds only with a complete proof on the whole
stated complex odd class or an actual smooth strict counterexample.
A failed norm-level comparison alone would leave the target undecided;
record that precise obstruction rather than declaring the inequality
false. Do not broaden into a second mechanism in the same step.
Even a passing allocation pays only this sector's first prime.

### Search record, duplicate comparison and remaining leads

Actual query strings included:

- `Beckner logarithmic uncertainty principle odd functions Pitt inequality remainder`
- `Pitt inequality odd functions logarithmic uncertainty improved constants Beckner`
- `"Pitt" "odd functions" inequality`
- `"logarithmic uncertainty" "odd"`
- `"Pitt" "spherical harmonics" Beckner sharp`
- `"logarithmic uncertainty" "odd" "3/4"`
- `"Pitt" "odd" "Yafaev"`
- `"logarithmic uncertainty" "sine transform"`
- `"odd" "translation" "logarithmic uncertainty" Beckner`
- `"Q_2" "Beckner" remainder odd`
- `"first prime" "Beckner" remainder`
- `Yafaev "Sharp constants in the Hardy" 1999 pdf`

The sector source explicitly traces its classical Fourier result to
Yafaev, *Sharp constants in the Hardy--Rellich inequalities*, JFA168
(1999), 121-144, DOI10.1006/jfan.1999.3462. Only bibliographic/abstract
access to that original was inspected; no theorem number from it is
invented or imported. The accessible sector corollary and its relevant
proof case suffice, so this unread original is not an essential blocker.
Omri (2011), cited by the source's Hankel formula (4.1), and Soltani
(2014), cited for one-dimensional Dunkl bounds, remain unread originals.
No additional hypotheses are borrowed from their titles or abstracts.

The parity-named Cao--Li--Li--Chen paper,
DOI10.1007/s00034-015-0146-x, concerns Wigner--Ville/ambiguity forms.
Its publisher link was inaccessible; search-visible author text was
only a lead, not an inspected theorem or an input. It is unnecessary
once the precise accessible sector theorem is available. Do not
relabel this nonessential access failure as SOURCE_BLOCKED.

Local comparison read L743 (1) for the coefficient, L746's hypotheses
and resource, step299's unused odd observation, the earlier Beckner
assessment, and the named ATTEMPTS records for the half budget,
prime-only Rayleigh saving, and carrier span. The audited even witness
does not have odd parity. The other stops concern an unweighted
supremum and a restricted carrier family, respectively. No duplicate
proof of this odd allocation was identified in those relevant paths.
No claim of exhaustive archive search or novelty follows.

Full matching Mathlib coverage is not checked; no formalization claim
or cross-notebook input is made. No lemmas or mathematical scripts
were written, no target inequality was proved, and PROOF/DAG need
no change. This is one completed literature comparison, with zero
mathematical exploration usage and no counter reset.
