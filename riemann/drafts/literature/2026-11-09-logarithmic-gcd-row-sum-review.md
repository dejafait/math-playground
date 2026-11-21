# Prime-power row sum for the critical logarithmic gcd form — source review

TARGET: Review source coverage for sum_(2<=r<=x) Lambda(r)/phi(r)<=log x+C0 (absolute C0, all real x>=2) and its applicability to L737's unchanged weighted Schur argument for F_(2 log N)>=-C Q.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step227 searched the exact Lambda/phi sum, weighted Mertens estimates and stronger prime-weighted bounds; local logarithmic-gcd assessments, working notes and attempt/history records contain no completed endpoint argument. An external citation-ledger lead was followed to Goldfeld's primary PDF; snippets were not used as theorem evidence.
SOURCE_EVIDENCE: Goldfeld, Mathematika16(1969),23-27, Section2 printed pp23-24, unnumbered Mertens display on p24 and reference[2] p27; Tao, 254A Notes1(2014-11-23), Section2 Proposition12 and Theorem13 eqs(20),(22)-(24), complete proofs. L737 (5)-(11) and its separate audit fix the finite Schur interface. Extraction qualifications and unused leads are recorded below.
COMPARISON: Goldfeld records the totient-weighted Mertens asymptotic, with an extraction limitation detailed below; Tao supplies a fully inspected independent first-Mertens input with all real cutoffs. The scalar lead belongs to standard Mertens estimates, not an originality claim. Neither source states the full signed gcd coercivity inequality; its finite-prefix/denominator and complex Schur specialization is a later mathematical task.
GAP: No full-form endpoint inequality is proved this turn. The later specialization must obtain one absolute constant for all real cutoffs, handle empty rows, and verify the additive Schur remainder without dropping complex cross terms. Conditioning, moment errors, realization and Xi signs remain independent gaps.
REASON: Essential source comparison now supports the single bounded COVERED_TARGET below. Import the standard estimate and prove only its finite applicability; do not reprove Mertens or enlarge the parked pilot. This newly ready continuation requires separate next-turn approval.
SCOPE: Exact TARGET and COVERED_TARGET below; all prime powers, Euler phi, natural logarithms, small cutoffs, absolute constants, all integers N>=2, arbitrary complex c and full kappa/cross terms. No multiplier-length, projection, moment or Xi-sign extension. No originality conclusion.
COVERED_TARGET: Specialize the cited Mertens estimate to prove F_(2 log N)(c)>=-C Q(c) with one absolute C>=0 for every integer N>=2 and every complex c, using L737's unchanged divisor identities and weighted Schur argument.

## Invocation-start nomination (preserved)

The paragraphs below describe the previously unassessed lead. Their
unread-source statements are historical; the completed review follows.

The main gap remains L030–L032/C032a actual-Xi mixed positivity.
The intermediate question is uniform critical coercivity. Sharper
arithmetic norm control might guide multiplier lengths; conditioning,
charged moment errors, microscopic realization and signed transfer
remain independent unresolved assumptions.

Essential input: audited L737 (5)–(9),(11). Reuse the November9
critical-form assessment for its exact comparisons and the November4
assessment within its scope. Search the displayed sum, Mertens-type
weighted von Mangoldt estimates, stronger results and small-x
qualifications. Retrieve primary hypotheses and relevant proof cases
before deciding applicability. No theorem citation is supplied from
memory and no estimate is claimed.

Continue only if an inspected theorem covers the required uniform
additive remainder or leaves a concrete justified specialization.
Check the exact row/column weights against the critical threshold;
do not discard kappa or complex cross terms entrywise. If hypotheses
do not permit use, record the mismatch and park the mechanism. Do not
repeat the dyadic pilot. Matching Mathlib coverage is unchecked;
no cross-notebook input or ready mathematical continuation is proposed.

## Completed comparison — 9 November 2026, step227

### Relevance and duplicate/failure check

The main gap remains actual-Xi all-degree mixed positivity. The single
intermediate target is an absolute additive lower bound for the unchanged
critical logarithmic gcd form. Its plausible use is to assess arithmetic
norms before considering longer microscopic-observer dictionaries. Even
success would not pay coefficient conditioning, moment remainders,
realization or signed transfer.

Reused the November9 critical-form assessment and the November4
arithmetic-multiplier source assessment. Read L737's finite proof and
separate audit, the step261 audit note, and the step225/226 logarithmic-gcd
records. Targeted searches for `Lambda.*phi`, `Mangoldt`, `Mertens` and
`row.sum` in those records found the nomination, not an endpoint result.
The completed dyadic pilot supplies no lower spectral bound; its stop
remains. L737's short-dictionary exclusion remains valid at its length.
No new actual-theta/contact premise justifies reopening the earlier stops.
No local sibling notebook or cross-notebook theorem was used.

### Primary input ready for import

Terence Tao, *254A, Notes 1: Elementary multiplicative number theory*,
23 November 2014, [Section2, Proposition12 and Theorem13](https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/),
equations(20),(22)-(24). Read the definitions, both theorem conclusions,
and complete proofs, including prime-power removal. Theorem13 states

    sum_(n<=x) Lambda(n)/n = log x + O(1),  all real x>=1.

The constant is absolute; there is no RH, progression, auxiliary
parameter or coefficient hypothesis. Its proof uses the divisor identity,
the factorial sum, floor-counting error and Proposition12's Chebyshev
bound. The higher-prime-power comparison is explicitly summable.
Only this named theorem is to be imported, without reproving its
arithmetic estimates. It has denominator n; replacing it by phi(n) is
a specialization still to be written. An O(log x) theorem alone would
miss the required leading coefficient.

### Exact-sum citation and extraction qualification

Morris Goldfeld, *On the number of primes p for which p+a has a large
prime factor*, Mathematika16(1)(1969),23-27,
[author PDF](https://www.math.columbia.edu/~goldfeld/PrimeShifts.pdf),
Section2, unnumbered display on printed p24 immediately after
“using Mertens' result [2]”. Read pp23-24 and reference[2] on p27.
This is the totient-weighted Mertens citation, not Theorem1 or equation(2).
Reference[2] points to Hardy–Wright, *An introduction to the theory of
numbers* (Oxford,1965),348-349; those book pages were not accessed.

The PDF text extraction damages the display's summation subscript;
screenshots failed in both web interfaces, and local download failed
DNS. Thus a fully checked transcription of that cutoff is not claimed.
The unrelated Bombieri parameters surrounding it are not imported into
our scalar question. An external erdos-456 citation ledger located this
passage but is not theorem evidence. Source readiness rests independently
on the fully inspected Tao theorem and the explicitly scoped denominator
specialization; it does not depend on recovering this damaged display.

### Stronger comparisons and search record

Queries included `"sum" "Lambda(n)" "phi(n)" "log x"`,
`"von Mangoldt" "totient" "Mertens" sum`,
`"sum" "log p" "p-1" Mertens theorem O(1)`,
`"Lambda(n)" "varphi(n)" "log x"`,
`"Mertens" "totient" "Mangoldt"`,
`"Lambda(n)/phi(n)"`,
`"sum" "\\Lambda(n)" "\\varphi(n)" Mertens`, and
`Rosser Schoenfeld 1962 sum log p p theorem 6 pdf`.
The external citation lead was followed with
`Goldfeld "On the number of primes" "large prime factor" pdf 1969`.
No inference of novelty follows from unsuccessful exact-form searches.

Rosser–Schoenfeld, *Approximate formulas for some functions of prime
numbers*, Illinois J.Math.6(1962),64-94,
[primary-paper scan](https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf),
Theorem6 and corollary p70, gives stronger explicit prime-weighted
comparisons. The extracted statement interleaves inequalities and ranges;
the proof paragraph on p87 refers to three cutoff ranges and omits
parallel details. No explicit constant/range is imported from that
extraction. It is unnecessary for our absolute-constant question.
Tao supplies the adequate input without these access qualifications.

### Applicability and the bounded continuation

This paragraph compares existing interfaces; it proves no new inequality.
In L737's fixed Euclidean coordinates the weights remain

    h_d=1/sqrt(phi(d)),
    K_(d,n)=Lambda(n/d)sqrt(phi(d)/phi(n)) for d|n, n>d.

L737(8) gives the column sum exactly log n. Its audited row entry is
Lambda(r)phi(d)/phi(dr); (9) already bounds the row by the scalar
Lambda(r)/phi(r) sum with cutoff N/d. Thus the source concerns the
correct majorant and a coefficient-one logarithmic row bound would
match the coefficient-one column bound at the proposed threshold.
It is not legitimate to substitute an O(log N) row estimate with an
unspecified multiplicative constant at this endpoint.

Only the following finite specialization remains within COVERED_TARGET:
translate the cited first-Mertens input to the totient denominator,
explicitly bound its prime-power correction, and absorb all bounded
cutoffs into one nonnegative absolute constant. Treat 1<=N/d<2 as an
empty row. Apply the already proved complex Schur argument in L737,
checking its square-root remainder against the additive-C threshold.
Retain both cross terms, kappa>=0 and c=0; Q>0 for c!=0 follows from
L737's existing finite inversion. No inverse bound beyond that already
proved there may be assumed.

This is source-covered specialization, recommended as REPRODUCTION,
not a creative mechanism or an established full-form theorem. The
primary sources do not state this matrix conclusion; that is why a
citation alone does not complete it. No denominator correction, Schur
remainder calculation or final C has been derived in this literature
turn. Full citations and the necessary specialization belong in a
canonical lemma only after a separately approved mathematical attempt.

Continue on a proof with one C independent of N,d,c, including small
cutoffs. If the corrected row bound or the additive Schur remainder
cannot be justified, record the exact failing case and park that
mechanism. An additional grid or fixed-vector estimate is not a repair.
Successful arithmetic coercivity would still leave the RH gap open.
No full matching Mathlib theorem or supporting declaration was checked;
availability is unknown, not asserted absent.
