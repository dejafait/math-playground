# Fixed Pollaczek reference poles — source comparison2026

Completed record, 20 November 2026. Literature only; no residue, root,
coefficient, metric or new lemma has been calculated.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity;
C029m's eventual full-family Hermite index at most one is unpaid.
The discovery compares only (1) the auxiliary generating function,
(2) the source's oscillatory moment/recurrence representation, and
(3) residue signs at the fixed roots of p_(N-1). The third is the
selected nominee. Its new assessment requires separate approval.

Already read: C029m in full; C029n/C029o in full; C029p and C029q
hypotheses/conclusions; source-review2001, comparison2020 and signed
comparison2025; structured-matrix discovery2009 and its limited metric
ansatz. Existing work is preserved. No cross-notebook input.

Primary passages inspected: Kuznetsov, CMB51(2008),561–569,
DOI10.4153/CMB-2008-055-0, (3)–(10), (13)–(14), Propositions4.1–4.2
and their displayed proof/weighted qualification pp567–569;
de Snoo–Winkler–Wojtylak, arXiv:1011.2081v1, 9 November2010,
definition(1.1), (1.2)–(1.5), Section2.1(2.1)–(2.6), Theorem2.2
and complete Corollary2.3 proof, manuscript pp1–5; Langer–Luger–Matsaev,
Acta Sci.Math.77(2011),425–437, Definition1.1, (1.2)–(1.3),
printed pp426–427. Source scope and continuation are recorded below.

The proposed test fixes p_5 before inspecting U_6. It would enclose
the residues of the monic-normalized ratio U_6/p_5, and test whether
at most one has the sign opposite to a Nevanlinna simple pole.
This is a coefficient-specific sufficient-condition screen, not an
isolated inertia count or a fitted reference polynomial. No residue
sign or actual negative-square classification has been established.

## Three candidates, one nomination

1. **Auxiliary generating function.** Kuznetsov's Proposition4.2 and
   proof pp567–568 concern the series with coefficients u_n/(2n+1)!!.
   Its proof uses the real-zero generating function (3), product
   truncations and Proposition4.1's sufficient coefficient-polynomial
   condition. C029m instead uses beta_n from (4), followed by different
   Jensen weights. The author explicitly distinguishes the missing
   coefficient transformation and damping. No theorem inspected pays
   that difference; park automatic import, without redoing the ready
   generic multiplier assessment.

2. **Moment/recurrence structure.** Source (7) is an oscillatory sine
   integral for a_n; (10) relates a_n to u_n. Recurrence(14) computes
   u_n, not orthogonal T_N in N, and the author warns of instability.
   These inspected identities give no nonnegative measure or bounded
   signed defect for the actual beta_n family. Saddle expressions
   (15)–(17) were located, not adopted as a rigorous uniform error
   theorem. No new contour, asymptotic estimate or sign calculation
   was made. Park this candidate without a new restriction.

3. **Fixed reference-pole residues.** Normalize U_N by its actual
   leading coefficient when degree N is established. Fix the monic
   denominator (N-1)!p_(N-1) independently of U_N's roots. The proposed
   restriction is at most one positive residue in the convention
   r/(z-lambda). Generic negative-square theory supplies the zero
   interface conditional on a verified kernel hypothesis. No source
   supplies the actual signs. Nominate only the fixed N=6 screen in
   assessment2026; it tests a coefficient condition rather than the
   numerator's inertia or the stopped inter-degree quotient.

Candidate3 is untested. Its baseline failure would park this version;
an eventual-only restart needs new asymptotic structure, not a shift
to another isolated degree.

## Primary sources, exact hypotheses and application

A. Kuznetsov, *Expansion of the Riemann Xi Function in
Meixner–Pollaczek Polynomials*, Canadian Mathematical Bulletin51(4)
(2008),561–569, DOI10.4153/CMB-2008-055-0,
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FD79D70DF68748CCEC70097E3FB9F2FA/S0008439500012492a.pdf/expansion-of-the-riemann-function-in-meixnerpollaczek-polynomials.pdf).
Read Theorem2.1/(3)–(10) and its displayed proof, finite formulas
(13)–(14) and generating-function justification p566, Propositions4.1–4.2
and displayed proof pp567–568, and weighted qualification pp568–569.
Reuse review2001 for exact coefficient extraction. Every odd coefficient
is essential. No numerical root observation is a certificate.

H. de Snoo, H. Winkler and M. Wojtylak, *Zeros of nonpositive type of
generalized Nevanlinna functions with one negative square*,
[arXiv:1011.2081v1, 9 November2010](https://arxiv.org/pdf/1011.2081),
definition(1.1), (1.2)–(1.5), Section2.1(2.1)–(2.6), Theorem2.2 and
Corollary2.3 with its complete proof, manuscript pp1–5, were read.
Theorem2.2 is stated there with references [3–5], not proved there
(source-approval2027 clarification).
Membership in N_1 means real symmetry, meromorphy on C minus R,
and exactly one negative square of the divided-difference kernel.
Every upper-half-plane zero is a generalized zero of nonpositive
type; there is exactly one such point in the extended closed upper
half-plane. Theorem2.2 factors Q as one of three specified rational
factors times an N_0 function, with finite/infinite endpoint cases.
Corollary2.3's proof checks nonreal-zero simplicity; it does not assume
numerator simplicity. Theorem2.2 is imported as stated; upstream[3–5]
are not independently audited. N_0 must be treated separately.

H. Langer, A. Luger and V. Matsaev, *Convergence of generalized
Nevanlinna functions*, Acta Sci.Math.(Szeged)77(2011),425–437,
[journal PDF](https://acta.hu/download.phtml?id=3148), Definition1.1
and (1.2)–(1.3), printed pp426–427, were inspected. They specify the
general kernel convention, rational-factor characterization and
preservation of index under -1/f. The paper's convergence theorem
has extra index hypotheses and is not imported for varying Pollaczek
denominators. No limiting rational function is assumed.

The finite application remains research: check the kernel of a monic
degree-six numerator divided by a monic degree-five polynomial with
distinct real roots, including the linear term and every residue's
sign. Only after paying its kernel hypothesis may one apply the
N_0/N_1 zero theorem. This short finite algebra is an orientation and
applicability check, not a reproof of Theorem2.2. Zero residues are
real-pole cancellations; zero-containing enclosures remain unresolved.
No new interface or actual-family sign theorem is established here.

Normalization contrasts inspected: Romik,
[arXiv:1902.06330v3](https://arxiv.org/pdf/1902.06330), Section1.3,
printed p6, distinguishes Kuznetsov's tilted expansion; Inoue,
[arXiv:1412.1220v1](https://arxiv.org/pdf/1412.1220), pp1–2, defines a
different completed function/variable. Their later theorems are not
claimed as read. Reuse the ready October30 Romik moment-weight
assessment rather than redo its stopped generic test. Ou–Luger's
review located the primary negative-square sources; it is not an
independent theorem premise. Search-only q-Pollaczek and 2026 Meixner
leads were not inspected or used. No essential source blocker remains
for the finite application.

## Duplicates, failures, queries and limits

Reused review2001, affine comparison2020, signed comparison2025 and
structured-matrix discovery2009; read source-notes2000 and the
October30 actual-theta weight comparison. C029p's finite conclusion
and C029q's audited negative e_2 direction are not repeated. C029n
fixes an identity bulk; the nominated condition does not impose that
ansatz. The denominator p_5 is neither U_6' nor U_7/U_6. No fitted
metric, selected numerator zero factor or assumed low index enters.

Notebook-scoped duplicate searches for Pollaczek/Kuznetsov together
with residue, secular, Nevanlinna and fixed grid/poles found no matching
test in drafts/literature or ATTEMPTS; the earlier matrix assessment
was read in full. This is not exhaustive coverage or novelty evidence.
The finite-count and generic signed-chain stops remain preserved.

Queries included `Kuznetsov Expansion Riemann Xi Meixner Pollaczek
coefficients recurrence`, `Kuznetsov Pollaczek residues`, `Meixner
Pollaczek Nevanlinna zeros coefficients`, `Kuznetsov Pollaczek moment
coefficients`, `generalized Nevanlinna rational residues negative
squares`, and `generalized Nevanlinna partial fraction`. Results
supplied general theory, not actual-family signs. Primary PDF text
was accessible; screenshot requests returned reference labels without
image payloads, so no visual verification is claimed.

The required threshold is at most one positive residue; actual values
are uncomputed. Two certified positive residues stop this baseline
condition, not the eventual premise. A pass leaves uniform signs,
actual-degree control, initialization, general singular/cancellation
cases and C029m's qualified weighted-limit/upstream[9] input open.
Essential inputs are C029m–C029q in their stated scopes; C029p/q are
contrasts rather than residue-sign premises. No cross-notebook input.
Full matching Mathlib coverage unchecked. No lemma, mathematical
script, PROOF or DAG changed. This is EXPLORATION/source preparation,
not progress beyond the inspected general theory or an RH candidate.
The new finite assessment needs separate approval; this literature
turn spends/resets no mathematical exploration budget.
