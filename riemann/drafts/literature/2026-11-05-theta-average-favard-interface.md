# Actual theta-average sequence: Favard/Jacobi source gate

TARGET: Assess whether the actual L795 polynomial sequence admits a common positive-measure Favard/Jacobi realization, and source-gate a degree-three recurrence obstruction test using its theta moments.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step503 searched Favard positive-measure recurrence, orthogonal Jensen classification and orthogonal Brenke generating functions; inspected DLMF and Dimitrov–Ben Cheikh Lemma1/Theorem1 with all four source proofs. Narrow local searches found no actual-sequence recurrence test; earlier finite-model and flow/CD stops have different hypotheses.
SOURCE_EVIDENCE: https://dlmf.nist.gov/18.2 (i),(iv),(vi),(viii), especially (18.2.11_4)–(18.2.11_9); Dimitrov–Ben Cheikh, JCAM233(3)(2009),703–707, DOI10.1016/j.cam.2009.02.039, (2.1), Lemma1 p705 and Theorem1/all four proofs p706, primary author text linked below. L019/L021/L795 fix the sequence; L791/step478 supplies an audited coefficient interface.
COMPARISON: Orthogonal Jensen sequences are already classified as Laguerre families up to stated equivalences. Favard supplies a necessary recurrence, not actual-theta realization. A finite theta-prefix obstruction remains uncomputed; it is a known-criterion specialization, not a new classification or failure of individual real-rootedness.
GAP: Actual prefix feasibility, forbidden coefficient and beta signs are uncomputed; no actual moment mismatch, common measure or all-degree sign is established. Classification alone is not a checked exclusion of the theta sequence.
REASON: Replace unrestricted common-measure construction with one finite necessary-condition test using existing audited actual-coefficient enclosures; cite classification rather than reprove it. Actual specialization remains needed.
LITERATURE_REASON: The completed logarithmic variation review supplies only upper oscillation bounds and no independent signs. This nomination changes to actual-sequence orthogonality and requires new essential theorem/classification coverage.
SCOPE: Completed literature-only source gate for the exact TARGET; the nomination below is historical. A separately nominated degree-three test is source-ready subject to separate next-turn approval. No recurrence algebra, numerical test, lemma or mathematical script was performed here.

Main gap: actual-Xi all-degree mixed positivity. The intermediate
candidate is common positive-measure orthogonality of the actual P_d
sequence from L795, after monic normalization. This is an intentionally
strong sufficient realization to assess, not a consequence of
individual real-rootedness and not an established representation.

The intended bounded later test is to inspect the multiplication-by-x
recurrence through P_3 and determine whether the forbidden lower-basis
coefficient vanishes with the necessary positive recurrence parameters.
Do not derive its formula in the source turn. Exact theta moments and
their normalization must remain fixed; a test on an arbitrary positive
measure or a fitted Jacobi model would change the target.

Read primary Favard hypotheses, including nondegeneracy, support and
positivity qualifications, and check orthogonal Brenke/Jensen
classifications or stronger known obstructions before approving a
finite test. Distinguish an arbitrary real orthogonality support from
positive roots. Even a valid first prefix cannot supply an infinite
positive Jacobi operator, support on (0,infinity), the desired signs or
a degree-uniform route to RH.

Essential prospective inputs: L019/L021/L795. L776 is unnecessary unless
its coefficient convention is used. No cross-notebook result is
nominated. Unresolved assumptions are the recurrence condition, actual
moment relation, positive recurrence coefficients, common-measure
existence/support and all-degree transfer. Mathlib matching coverage
is unchecked.

Duplicate checks to reuse: the shift-zero Jacobi matching assessment
matches a separate comparison family in fixed degree; it does not make
P_0,P_1,... one orthogonal sequence. L530's two-atom Pollaczek flow and
L565's diagonal Hermite CD cone do not establish this particular
recurrence obstruction. Their proofs need not be reopened without a
specific mathematical input. The L795 stop and step502 source-direction
stop remain intact.

Continuation/abandonment test: approve one exact finite recurrence test
only if primary sources show its noncircular necessary role and no
ready known classification already settles the actual sequence. Import
a matching known obstruction instead of reproducing it as new work.
If the realization is target-equivalent without independently testable
content, duplicates a recorded failed construction, or has no useful
root-count consequence, park it with the exact reason.

This is a conventional realization/obstruction candidate, not a creative
proof attempt or an RH candidate. Missing independent theta signs and
unassessed source coverage currently block justified creative routing.
The next invocation reviews sources only; any ready mathematical
continuation receives separate supervisor approval.

## Completed comparison — step503, 5 November 2026

The paragraphs above preserve the original nomination rather than a
second current action. The main gap remains actual-Xi all-degree mixed
positivity. Common orthogonality of the actual sequence would be an
independent real-root mechanism. A finite necessary-condition failure
could eliminate that stronger mechanism while leaving other gaps open.

### Favard hypotheses and interface

Inspected NIST DLMF 18.2(i),(iv),(vi),(viii), online on the checked date,
including [monic recurrence](https://dlmf.nist.gov/18.2#E11_5),
[positivity](https://dlmf.nist.gov/18.2#E11_6),
[Jacobi form](https://dlmf.nist.gov/18.2#E11_9) and
[measure qualifications](https://dlmf.nist.gov/18.2#viii).
Monic real orthogonal polynomials Q_n of degree n with positive norms
require xQ_n=Q_(n+1)+alpha_n Q_n+beta_n Q_(n-1), with real alpha_n,
beta_n=h_n/h_(n-1)>0 for n>=1, Q_0=1 and Q_1=x-alpha_0.
Conversely, these conditions at every degree give a positive measure
on R, not necessarily absolutely continuous or unique. Require finite
moments and positive norms at every degree; finite support cannot support
the infinite nondegenerate sequence. Section(vi) supplies real simple
zeros/interlacing; positive support remains additional. A finite prefix
does not give a unique or bounded infinite Jacobi operator.

Here Q_n will mean P_n divided by its nonzero leading coefficient;
L021 supplies the needed nonvanishing. The theta averaging measure in
u is not an orthogonality measure in x. A finite recurrence test requires
no unproved interchange or infinite-limit interface. It is not executed
in this source turn.

### Stronger known classification

D. K. Dimitrov and Y. Ben Cheikh, *Laguerre polynomials as Jensen
polynomials of Laguerre–Pólya entire functions*, Journal of Computational
and Applied Mathematics **233**(3) (2009), 703–707,
[DOI](https://doi.org/10.1016/j.cam.2009.02.039),
[primary author-uploaded full text](https://www.researchgate.net/publication/223123039_Laguerre_polynomials_as_Jensen_polynomials_of_Laguerre-Polya_entire_functions).
Read (2.1), the g_n definition, Lemma1 (p705), Theorem1 and its complete
four short proofs (p706). Their g_n=sum binom(n,j)gamma_j x^j matches
L795 with gamma_j=(-1)^j j!m_j/((2j)!m_0), nonzero by L021. This only
identifies the existing coefficient convention; no recurrence is derived.

Theorem1 classifies orthogonal Jensen sequences as Laguerre families,
with its stated equivalence under linear variable changes. Lemma1 uses
formal power series with nonzero coefficients. The four algebraic proof
routes use exponential Brenke generation, reciprocal Appell structure,
differential recurrence or multiplication. They require no assumption
of actual-Xi membership in Laguerre–Pólya; do not assume the earlier
Jensen real-zero criterion is already proved for Xi. Retain normalizations
and variable-change qualifications. The theorem does not itself check
actual theta exclusion or supply a degree-three numerical certificate.

The authors' four published proofs cite Chihara1968, Toscano1956,
Al-Salam–Chihara1972 and Feldheim1940. Those original underlying papers
remain unread and are not independently audited here. The matching
published Theorem1 is the citation to use, without a classification
reproof. No original theorem about the actual theta moments is claimed.

Access: the DOI endpoint failed; the UNESP repository record has only
an abstract, restricted access and no file. The author-uploaded article
text includes the load-bearing theorem and proofs; its PDF button gave
404. Thus access is sufficient despite failed endpoints. Chihara's
Project Euclid page rendered only an iframe. Chaggara–Gahami's publisher
introduction and arXiv2310.11734v1 abstract were inspected as broader
Brenke leads; their 2-orthogonality/four-term classification is not
imported. No conclusion relies on an inaccessible original reference.

### Overlap, data reuse and bounded continuation

Queries included: Favard theorem positive measure three term recurrence
infinite support; orthogonal Brenke/Jensen classification; Laguerre
polynomials as Jensen polynomials pdf; Chihara orthogonal Brenke
generating functions. Search snippets were discovery only. Narrow local
searches in drafts/literature, ATTEMPTS and relevant 5November history
found no existing actual-P_n common recurrence certificate. This is not
a novelty claim. Reused L530/L565 triage without reopening their proofs;
read the fixed-model shift-zero assessment and L791 with its step478 audit.

L791's actual gamma(j)=j!m_j/(2j)! enclosures for j=0..4 are independent
of its fitted Jacobi model. Its audited analytic coefficient-error and
software contracts permit reuse of that actual-data portion alone.
Later inspect the complete selected stored intervals and provenance,
preserving all errors; rounded summaries are insufficient. No numerical
certificate was read or replayed here. No fresh quadrature source gate
or integral implementation is required. No cross-notebook input is used.

The new overlap changes the decision: unrestricted orthogonal Jensen
construction would reproduce a known rigid family. Limit work to
[one finite actual recurrence test](2026-11-05-theta-average-degree-three-recurrence.md).
Stop common nondegenerate positive-measure realization on a certified
nonzero forbidden coefficient or nonpositive required beta. A passing
or undecided prefix is inconclusive for the infinite family; it does
not authorize a degree extension. Individual roots, nonorthogonal
mechanisms and all-degree signs remain open.

This is a source-overlap NEGATIVE and a completed source gate, not a
theta counterexample, new mathematics or progress beyond the inspected
sources. The finite test is conventional specialization. No independent
theta signs justify creative routing at the central gap. Mathlib full
matching coverage is unchecked. No lemma, script, PROOF or DAG changes.
