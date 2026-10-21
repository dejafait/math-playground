# Concrete quadratic coefficient at seven — proposed implementation scope

TARGET: Produce a finite L027 quadratic-coefficient enclosure for E=[0,1,1,-2,0] at p=7 using audited L032 symbols and C=0, certifying ordinarity, Teichmuller residues and unit-root precision, testing n=2,3,4 with M=n+1 and stopping at the first strict bound min(n-1,M)>v_7(b).
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused exact queries and inspected primary coverage in the 2026-10-06 primitive-error, finite-error and critical-audit assessments; searched the named local coefficient/calibration records and ATTEMPTS/022--023. No duplicate concrete coefficient certificate was found in those records; no novelty inference or broad rediscovery.
SOURCE_EVIDENCE: Stein--Wuthrich, Math. Comp. 82 (2013), Section 3 pp. 1762--1766, Propositions 3.1/3.5, Corollary 3.3 and essential divisibility proof, https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=6; Conrad, Hensel’s Lemma, Theorem 4.1 printed p. 6, https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf#page=6; both reopened 2026-10-08. Full canonical L027 and audited L032 read; foundations/05 and L031 point-count proof range compared.
COMPARISON: Known ordinary modular-symbol algorithms and audited L027 cover the enclosure; audited L032 supplies exact normalized symbols and all-level C=0. The remaining work is their finite p=7 implementation and independent exact replay, with ordinarity still an instance obligation. No source guarantees the scheduled depths succeed.
GAP: No p=7 point count, unit-root approximation, residue table, concrete b or strict inequality is certified in this literature turn. Full path and summation certificates remain required; independent L026 premises and the general rank gap remain unresolved.
REASON: Separate scope comparison is complete: the proposed finite implementation fits the inspected construction and L027/L032 without changed theorem hypotheses. SPECIALIZE authorizes REPRODUCTION of the finite algorithm, not a theorem reproof or a BSD claim.
LITERATURE_REASON: New finite coefficient implementation scope, including a chosen prime and bounded precision schedule, was not covered by the approved L032 audit target.

Main gap: rank equality for arbitrary analytic order at least two.
The proposed intermediate output is an independently replayable finite b
and N=min(n-1,M), with N>v_7(b). It could supply L026's coefficient
premise only if all its other arithmetic and Selmer hypotheses hold.

Essential local inputs: L027, L028, L030, L031, L032; full relative-t2,
twist-five and calibrated-symbol certificate/verification/audit sets.
Use only L031's arithmetic point-count evidence, if relevant to the
chosen prime; do not import its unused rank data. Retain the complete
full-relative integral presentation and all path-orientation witnesses.
No cross-notebook input is proposed.

The next source review should reuse the inspected Stein--Wuthrich
Section 3 and Propositions 3.1/3.5 and Conrad Hensel coverage in L027's
assessments, compare the exact finite formula and p-adic coordinate,
and check existing failure records ATTEMPTS/022--023. Their stops on
conditional repetition are preserved; actual audited symbol inputs
make this proposed output independently testable. No source is declared
blocked and no new theorem or source reproof is proposed.

The bounded mathematical test, after approval, is n=2,3,4 with M=n+1,
C=0 and p=7. Verify good ordinary reduction before using the unit root;
stop this chosen-prime target if that hypothesis fails. Certify all
Teichmuller residues and unit-root residuals, all rational symbol values,
and the complete binomial-weighted sum, with full disk certificates
and a distinct exact replay. Stop at the first N>v_7(b); if no tested
depth passes, retain the complete failed inequalities and reassess
before extending the budget. Neither approximate zero nor a finite
P_n coefficient alone establishes nonvanishing of the limiting a_2.

At proposal time (2026-10-07), no calculations or approval were supplied; the separate source approval below now covers the unchanged TARGET.
Full matching Mathlib implementation coverage remains not checked.
Uniform production, the other L026 premises, finite F, divisible Sha,
rational membership and complex-order comparison remain unresolved.

## Separate implementation-scope approval, 2026-10-08

SCOPE: Only the exact TARGET above, E=[0,1,1,-2,0], primitive untwisted trivial branch, total minimal real period, kappa(gamma)=8, L032 normalization F=-phi and all-level C=0; good ordinary p=7 must be certified before applying L027. Use n=2,3,4, M=n+1, with an independent exact replay. No additional L026 hypothesis or rank datum is approved as established by this assessment.

**Primary comparison.** The 2013 final publisher offprint of
[Stein--Wuthrich, Section 3, pp. 1762--1766](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=6)
was reopened at the symbol normalization, measure, finite polynomial,
Propositions 3.1/3.5, Corollary 3.3 and its proof, and ordinary-root case.
The construction uses total real periods, the 1+p coordinate and the
untwisted measure. Convergence is coefficientwise; the adjacent error
uses the monic divisor. The ordinary hypothesis is p not dividing a_p.
The interpolation multiplier is retained. L027 matches these choices.
Reuse its uniform-denominator tail argument; the previously flagged
Lemma 3.6 wording and two-level tail constant supply no new input.
No source theorem needs reproof for this implementation.

[Conrad, Theorem 4.1, printed p. 6](https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf#page=6)
was reopened in the undated live version. Its hypothesis is
f in Z_p[X], x in Z_p, |f(x)|_p<|f'(x)|_p^2; it gives a unique nearby
root and the exact distance |f(x)/f'(x)|_p. This is the already cited
L027 input for both root certifications. It does not certify any chosen
finite x until the residual and derivative checks are supplied.

**Applicability and finite evidence obligations.** L030's audited model,
minimality, non-CM status and Delta=389 are retained as inputs, rather
than recalculated in a literature turn. L032's full proof and separate
audit provide F=-phi on the entire relative integral module, including
all-level C=0, not merely calibration paths. L028/L031 retain their
independent positive-twist total-period scale. Thus no period rounding,
new Manin-constant assumption or calibration reproof is needed.

Before using the ordinary formula, the research step must save all
finite-field counts for the original curve at seven, including infinity,
and an independent exhaustive replay; report the actual trace t and
check t is a seven-adic unit. L031's original-curve point-count evidence
may be reused with its full relevant entries and checks, not twist
coefficients or unused rank data. Good reduction follows from the
retained discriminant input and its coprimality check. Stop this chosen
prime if the good-ordinary hypothesis fails; selecting another prime
would be a changed target requiring coverage review.

For each attempted n, save all six integer Teichmuller representatives
in the prescribed range with residue, sixth-power congruence and simple
root checks; save u, its rational unit check, residue t and exact
valuation of u^2-tu+7, with M=n+1 and unit derivative check. Root
precision alone must never select nearby rational symbol arguments.
Use the least positive residues of w times 8^j modulo 7^n and the two
exact rational arguments in L027 (1). Retain every j in its stated range,
including those greater than two. L027 (2), with every binomial(j,2),
is the canonical finite formula; no Euler factor, twist or extra factor
of two is inserted or removed.

Save each oriented cusp path with determinant-one segment lifts,
endpoints and Gamma_0(389) membership witnesses, its integral generator
representative and full quotient coordinates. Evaluate using the entire
L032 functional and compare with the generator-value expression.
Retain input hashes and the relevant full prior certificates; hashes
alone do not establish their mathematics. A separate replay must check
all path equalities and symbol values, root and residue checks, and
recompute the complete rational sum without trusting saved aggregate
values. The exact reduced b, v_7(b), N=min(n-1,M), failed checks and
strict comparison must be reported, with v_7(0)=infinity. Full evidence
belongs on disk; a preview or successful exit code alone is insufficient.
These are obligations for the next research step, not checks performed
or new mathematical consequences established here.

**Duplicates, historical failures and relevance.** The targeted records
contain L027's conditional enclosure and L032's calibration, not an
actual coefficient. ATTEMPTS/022--023 stopped repeating conditional
proofs while their inputs were missing. Audited L030--L032 are materially
different actual input evidence; the present target tests production
rather than repeating those proofs. Preserve both stops and all unfinished
work. Search reuse does not establish originality; classify the finite
application REPRODUCTION.

Main gap: rational rank versus complex order for arbitrary analytic
order at least two. The intermediate target is a finite quadratic
nonvanishing enclosure; it could supply only L026's coefficient premise.
Continue at the first complete strict N>v_7(b) and stop the bounded
schedule there. If ordinarity fails, a normalization/path check fails,
or all three tested bounds fail, retain the full evidence and reassess
before any extension. No near-zero coefficient is an exact vanishing
claim. Remaining L026 premises, finite F, divisible Sha, rational
membership, complex-order comparison and uniform production are separate.

DECISION is SPECIALIZE for the unchanged TARGET. Approval covers one
bounded mathematical implementation next turn. No new lemma, mathematical
script, p=7 arithmetic result or candidate was produced here. Full matching
Mathlib algorithm coverage remains not checked; unknown is not absent.
