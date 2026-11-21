# Dimitrov's shifted Wronskian criterion: bounded normalization audit

TARGET: Audit the printed sign and index normalization of Dimitrov 1311.0596v1 Theorem 2 on the Gaussian law pi^(-1/2) exp(-u^2) du for n=2,3, checking every hypothesis and stopping at the first mismatch.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step12 searched the exact paper, correction, and Wronskian criterion; inspected primary theorem and full relevant proof passages; narrowly compared local wronskian/dimitrov/favard assessments and moment failures. No matching local audit or inspected correction was located; no novelty or nonexistence claim.
SOURCE_EVIDENCE: Dimitrov, Lee-Yang measures and wave functions, arXiv:1311.0596v1, Section2(3)-(6), Wronskian definition, Theorem2 p6, and full Section3.3 proof p9; DLMF Table18.3.1, 18.5.18 and 18.17.23, live 2026-11-06. Links and exact qualifications below.
COMPARISON: The source supplies a claimed general criterion, not an actual-theta sign proof. Its fixed negative sign and proof indices are not yet independently checked. A Gaussian reference with known entire zero-free Fourier transform can test the printed universal claim without an RH, real-zero or theta-sign premise.
GAP: Verify the Gaussian law meets every stated moment, determinant and growth hypothesis, use positive-leading orthonormal polynomials, and check the literal n=2,3 Wronskians. No such calculation or counterexample is supplied by this source assessment.
REASON: A bounded source-integrity test is justified before any theta import of the newly inspected criterion. It is a reproduction/audit of a suspect known claim, not a new all-degree mechanism, a scalar Xi-sign refinement or a proof of RH.
SCOPE: Only Theorem2's literal sign/orientation and n=2,3 Gaussian cases, plus the source's displayed index pattern for interpretation. Stop at the first verified mismatch; a pass is limited to those cases. No repair, general Leclerc reproof, higher-degree sweep, actual-theta sign calculation or positive realization.

## Purpose and exact contract

The main gap is actual-Xi mixed positivity, L030-L032/C032a. The newly
read source offers a direct-integral/Wronskian interface but no independent
theta sign. The proposed intermediate target is the validity of its
printed normalization in a reference law. This is an integrity prerequisite,
not an actual-integral sign assertion meeting the main discovery threshold.
Its plausible downstream use is to prevent a false criterion from entering
a later actual-theta representation. Even a pass supplies no sign there.

No mathematical derivation was performed while writing this assessment.
It is newly written at the end of a literature-only discovery and requires
separate next-turn approval before research. The completed review is
`2026-11-06-direct-theta-all-degree-discovery.md` in this directory.

The primary source is Dimitar K. Dimitrov, *Lee-Yang measures and wave
functions*, arXiv:1311.0596v1, 4 November2013,
https://arxiv.org/pdf/1311.0596v1 . Read Section2, printed pp4-6,
and Section3.3, p9. Theorem2 uses an even sequence, strictly positive
even moments, positive moment Hankel determinants D_n for every n,
and limsup m_(2n)^(1/(2n))/(2n)=0. Its literal conclusion is
W(p2,...,pn;ix)<0 for every nonzero real x and every n>=2, equivalent
to all Fourier zeros being real. The Wronskian is the determinant with
successive derivatives in rows and p2 through pn in columns. Retain the
positive leading coefficient fixed by (6); flipping polynomial signs
without accounting for them would not test that statement.

The p9 proof's Appell indices n+1,n+2,n+3 were inspected in the PDF as
well as HTML. No corrected formula, parity factor or index shift is
assumed. Theorem1 and polarization are not fallback sign inputs. No
independent proof of Theorem2, Leclerc's general identity, or the whole
paper is required for this falsification/consistency test.

Use the specified probability law dmu(u)=pi^(-1/2)exp(-u^2)du. Import
classical Hermite orthogonality/norms and coefficients from NIST DLMF
Table18.3.1 and18.5.18,
https://dlmf.nist.gov/18.3#T1 ,
https://dlmf.nist.gov/18.5#E18 . These distinguish H_n with weight
exp(-u^2) from He_n with weight exp(-u^2/2). The primary Gaussian
Fourier input is18.17.23 at n=0,
https://dlmf.nist.gov/18.17#E23 ; read its stated real-variable formula
and justify any scaling and entire extension in the audit. These standard
results are cited inputs, not results to reprove. The local applicability
arguments and determinant arithmetic are the purpose of the next step.
No restriction requiring every positive quadratic exponential moment
may be added from Newman's different theorem; test this source's own
(3),(5) and Theorem2 hypotheses exactly.

The decisive test is exact agreement with the literal negative sign
for all real x!=0 in the two requested cases, under fully verified
hypotheses. One rigorous violating nonzero x suffices to reject the
printed universal statement. A symbolic polynomial can certify a whole
case if useful; no fitted numeric plot or preview is verification.
If a mismatch occurs, preserve its full evidence, park this printed
import and stop. Do not derive a correction or move to n=4. If both
cases pass, record only that bounded pass and stop; it proves neither
the source criterion nor actual-theta positivity. Missing essential
coverage must be reported without inventing the missing input.

L019/L021/L025 and L030-L032/C032a provide context only. They are not
mathematical inputs to a Gaussian source test, and no graph edge to them
is asserted. No cross-notebook theorem is used. Existing generic-kernel,
Favard, heat-contact, GHS and spectral-trace stops are preserved.
Full matching Mathlib coverage is unchecked; no absence claim is made.
The task is RESEARCH/REPRODUCTION, proof_audit/routine_audit, standard/high:
finite arithmetic and ordinary hypothesis replay, not a creative mechanism.
