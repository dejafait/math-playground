# W-intersection simultaneous count — completed bounded exploration

Approved target: Determine whether L043's recovery equations and triple gates allow at most eleven distinct nonuniversal candidate parameters for every tau=1 local pencil.

Reuse `drafts/literature/2026-10-08-nine-union-simultaneous-recovery-count.md` (EXPLORE), saved before invocation. Main gap: arbitrary sixteen-error equality. Intermediate test: use the h equations of two d-tagged candidates in audited L048–L049's surviving W-intersection case to fix p,q, then test simultaneous recovery for other tags. A conditional count restriction could exclude part of a twelve profile; fewer than two d-tags, other patterns, extraction and ABF26 remain independent.

Inputs: L010, audited L041–L043, audited L048–L049, and only the scoped checked five-value/same-d uses of L046. No L044 descent or full L045–L046 audit is assumed. Keep F=F_(97^20), all distinct original finite gamma_i, lambda!=0, p*q*(1-p-q)*r*(1-r)!=0, mu,nu!=0,-1, E deletions, arbitrary extension-field weights, relaxed fourth weights and distinct-parameter counting.

Continue for a new uniform simultaneous restriction or a fully gated twelve-parameter witness. Stop a proposed exclusion if a fully verified compatible configuration survives it; bounded finite subclasses do not establish a uniform count. ATTEMPTS/022's isolated-degree stop and the opposite-label finite_count test are preserved and not repeated. The ready assessment supplies primary recurrence coverage; no new browsing or cross-notebook input is needed.

The working checkpoint above was saved before the calculation. This step
chose one independently testable finite subclass: h=1, Y={8,12},
Z={18,70}, with every W, d and two-d-tag pair passing the ratio and
h-recovery tests in this scope. This is not a symmetry representative
for arbitrary Y,Z or a repeat of the earlier opposite-label test.
Other labelings and pencils without two d-tags remain outside the test.

## Reduction and duplicate check

For a d-tag root cubic f, the scoped checked five-value input in L048
gives f(z)=u W(z), -mu*f(y)=u W(y), and
(q-mu*p)f(h)=u W(h). Thus u=f(z_1)/W(z_1),
mu=-u W(y_1)/f(y_1), and a=u W(h)/f(h) all lie in F_97.
The root sets avoid every evaluation label, so all these divisions
are valid. The two candidates have distinct mu,nu by L043 (5).
Their h equations therefore fix

    p=(a-a')/(nu-mu), q=a+mu*p.

This elementary solve repeats the algebra displayed in L044 (5),
read specifically for duplicate checking. No new descent lemma or
full L044 conclusion is asserted or used. r remains arbitrary.

Audited L049's complete ratio partition supplies every possible triple
W,S,S' for the selected Y,Z. Its eleven groups of size at least three
contain all relevant possibilities; W differs from S,S' because mu=-1
is excluded. Every possible d is enumerated outside h,Y,Z,W,S,S'.
The h gates p*q*(1-p-q)!=0 are checked before counting. Identical
(d,W,p,q) configurations are counted once; their admitted parameter
sets do not depend on which pair originally selected that tuple.

For each resulting (d,W) labeling, all 1820 four-subsets are classified
using the complete four-row solve

    -mu F_K Y + sum_(x in {h,d} minus K) beta_x F_K v_x = -F_K Z.

L043 justifies the solve and every exceptional quotient case. The
original three supports and K_* are excluded; mu=0,-1 are excluded.
All other rows retain exactly q-mu*p=beta_h/c_h when h is absent,
and r=(1-beta_d/c_d)/(1+mu) when d is absent. Distinct mu values are
counted once even if multiple supports witness them. Fourth weights
may vanish. E deletions are omitted only as an overapproximation:
an arbitrary original chart can delete candidates but cannot add any.

The test includes every r in F, rather than assuming L044 descent.
When d is absent the required r is in F_97; therefore for any r outside
F_97 exactly the rows with d present can survive. These produce the
stored `nonprime_r_mus` set. All 95 prime-field r!=0,1 are counted
separately. No original parameter, rho or lambda is assumed rational.

The recurrence citation is the already inspected and specialized input
in L043: Chojecki, *Shortening Bounds for Reed–Solomon MCA*, live author
TeX v9.2 (July 17, 2026), lines 2785–2935, DR2
`drc:lem-locator-recurrence` and DR6–DRC `drc:thm-exact-compiler`,
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
It is not identified with the ePrint version. No standard theorem is
reproved. The saved ready assessment covers the known-result comparison;
no fresh literature or cross-notebook result is used.

## Complete evidence and limitations

Reproduce with `python3 scripts/simultaneous-recovery/w_intersection_count.py`.
The complete classifications, all r candidate sets, pair records and
independent maximizing-configuration checks are saved in
`scripts/simultaneous-recovery/w-intersection-count-result.json`.

The script reports 240 distinct pair-weight configurations on 192
(d,W) labelings, 349440 classified supports, 22800 prime-field r cases
and 240 nonprime-r cases. The maximum is **3**, versus **12** required
for refutation and **11** sought uniformly. The prime-field count
histogram is 22490 cases with two candidates and 310 with three;
every nonprime-r case has exactly two. Every configuration attains
three at some prime-field r.

At the first maximizing r of each of the 240 configurations, an
independent test checks all 95 eligible mu against all 1816 retained
supports: recover weights from moments 1–4, then compare moments 5–8.
It uses no recurrence rows or recovered beta values. All 41404800
memberships give exactly the counted sets. All 720 admitted records
have full weights. For each selected case the script additionally
constructs an actual triple at gamma=(0,1,rho), lambda=1, choosing
rho in F_97 to avoid every admitted E=0, and verifies all eight moments
of every admitted error against the resulting original finite pencil.
This verifies one maximizing r per configuration, not every maximizing
r or every weight choice.

Complete record integrity was checked as well: all 192 support
partitions, all 22800 r sets, all 240 maximizing records and all 720
admitted moment records. Reproduce this supplementary check with
`python3 scripts/simultaneous-recovery/check_w_intersection_records.py`.
It checks stored evidence, not every rejected RREF system; the primary
calculation supplies the exhaustive membership checks above. The small full certificate is
`scripts/simultaneous-recovery/w-intersection-count-integrity.json`.
No failures were reported. The complete `/summary`, first full
`/cases/0/count` and `/verifications/0` were inspected; the checks read
the complete artifacts, not selected previews.

For the first case, d=22, W={27,33,47}, S={27,50,64},
S'={27,85,89}, (p,q,r)=(88,79,90), gamma=(0,1,2), lambda=1.
The admitted (mu,T,K) records are
(32,40,{22,27,50,64}), (83,16,{50,64,85,89}) and
(93,96,{22,27,85,89}). The middle witness avoids B; it demonstrates
why other support types must remain in a simultaneous count.
Their complete weights and eight-moment vectors are in the selected
verification record; no new bad-count theorem is claimed.

Outcome: EXPLORATION. This is new local testing evidence under the
ready EXPLORE coverage, not a uniform mathematical advance, a matching
known-result import, or certified originality. No lemma, DAG or
PROOF.md change is justified. Full Mathlib coverage was not checked.
The unchanged approved eleven target remains unresolved, as do full
L044–L046 audits, fewer-than-two-d-tag branches, arbitrary extraction,
other patterns and challenge source identification. Mathematical
exploration usage is one since L049 validation.

Continue the unchanged target with an argument on the all-label recovery
equations using the two fixed p,q equations; do not expand or rerun this
same finite subclass as a putative uniform proof. Continue only for a
uniform simultaneous restriction or a fully gated twelve witness;
abandon a test that supplies only isolated degrees or more positive
samples. The essential inputs and unresolved assumptions at the start
of this record remain in force.
