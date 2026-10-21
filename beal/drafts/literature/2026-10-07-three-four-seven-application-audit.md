# Ordered (3,4,7) application audit coverage

TARGET: Critically audit L030's ordered (3,4,7) exclusion against Poonen–Schaefer–Stoll Theorem 1.1, checking primitivity, all 16 signs and exact square bounds, and the retained integral-completeness qualifications.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuses the exact equation, signature, stronger-result, correction and local duplicate searches in drafts/literature/2026-10-07-three-four-seven-classification-scope.md; no changed theorem hypothesis or broader signature is proposed.
SOURCE_EVIDENCE: https://math.mit.edu/~poonen/papers/pss.pdf — Poonen–Schaefer–Stoll, Duke Math. J. 137 (2007), no. 1, 103–158, Theorem 1.1; July 16, 2006 author PDF p. 1, Lemma 7.8 and Section 8 pp. 21–22, Section 13.7 p. 45; reaccessed 2026-10-07, with wider proof-case coverage retained in the scope assessment.
COMPARISON: L030 applies the known signed primitive (2,3,7) classification to (B^2,A,C); audit only the elementary applicability and full finite filter, retaining the published classification as a cited input.
GAP: The newly written local specialization has not received a separate critical application audit; no source-computation rerun or other signature exclusion is covered.
REASON: A bounded independent review should test the local proof's prime support, full sign transcription and two exact nonsquare witnesses, rather than repeat source discovery.
SCOPE: Only L030's ordered positive primitive A^3+B^4=C^7 exclusion, including unit bases and explicit source qualifications.

Inputs: L030; the full list and inspected source qualifications in drafts/literature/2026-10-07-three-four-seven-classification-scope.md; foundations/01-target-and-scope.md; complete certificate scripts/three-four-seven-specialization/finite-filter.json. L002 and L029 are not mathematical inputs. No cross-notebook input or conjectural rank, BSD, GRH or full-C5 rational-point determination is assumed.

Check the substitution identity and both implications for common prime support. Compare all 16 signed rows with the source list, particularly ±(0,1,1). Confirm that each nonpositive row is rejected for an actual required condition and both positive rows fail the integer-square requirement by exact consecutive-square bounds. The required count is zero; a surviving row, invalid bound or source-hypothesis failure requires correcting or withdrawing the local exclusion. Inspect the complete load-bearing certificate rows if using it; a summary alone is not verification. The already published classification remains imported by precise citation, not independently proved. Mathlib coverage remains not checked.

The separate literature approval and direct-source repair were completed in step 071. This preserves the completed specialization and authorizes its bounded application audit on the next research turn. No new literature discovery or mathematical derivation is claimed.

## Direct-source recovery and separate approval

On 2026-10-07 the [primary author PDF](https://math.mit.edu/~poonen/papers/pss.pdf) was reopened. Its first page defines primitive by gcd(X,Y,Z)=1 and states Theorem 1.1 for integer solutions, with the entire signed 16-triple list and no positivity or conjectural hypothesis. The author version is dated July 16, 2006 and identifies the published Duke article.

Lemma 7.8 and Section 8, author pp. 21–22, distinguish the restricted C5 subset relevant to primitive integral solutions from the undetermined full rational-point set. Section 13.7, author p. 45, establishes the subgroup index prime to 14, concludes that restricted subset is empty and finishes Theorem 1.1. These passages support the existing completeness qualification; their computations remain imported, not rerun. The earlier exact-statement, stronger-result, correction and failure comparisons remain adequate and are reused. No hypothesis or target changed, so further discovery searches are unnecessary.

LITERATURE_REASON: Supervisor-required direct-source URL repair and separate approval of the newly written L030 application-audit assessment; no expansion of ready mathematical coverage.

The decision remains SPECIALIZE. This is a process repair (STALLED), not a new exclusion, application audit or mathematical advance. Continue with the exact TARGET above; any source mismatch, surviving row or invalid square bound in that audit requires correcting or withdrawing the application. Mathlib coverage remains not checked.
