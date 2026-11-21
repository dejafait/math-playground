# C032v audit: source coverage1567

18 November 2026. Literature-only scope approval; no proof audit or
new mathematical derivation is performed.

## Exact target and relevance

The TARGET in assessment1566 is unchanged. The main gap is actual-Xi
all-degree positivity in L030-L032/C032a. The intermediate target is
critical review of C032v's bounded-test obstruction and conditional
convolution iteration for the qualified widths1,2 family. Its downstream
use is deciding whether the recorded sufficient-mechanism stop is valid,
without promoting it to failure of the actual reverse comparison.
Continue to the audit if every required tool is covered; otherwise park
the missing dependency. In the audit, a genuine defect requires repair;
a pass accepts only the stated mechanism stop.

Read complete C032v; C032m's hypotheses, lift definitions and uniform
regularity interface; C032q's hypotheses/conclusion and bounded signed
integration argument; C032t's endpoint assembly; C032u's hypotheses,
conclusions, cited construction and factorization. These readings identify
the audit's needed inputs, not a new critical certification of their proofs.
Reuse full source coverage from notes1552/1562/1565 and review1564.
Read stop1566 and history1566; searched only first-odd literature and
ATTEMPTS for one-jump,1566,M+log and M+k. The recorded stop remains
pending audit. Prior coverage already distinguishes mixture criteria,
stochastic order and generic density bounds from actual all-Borel
comparison; those unsuccessful imports are not reopened. No broader
archive-wide duplicate or originality claim follows.

## Primary tools and applicability

Jean Bertoin, *Subordinators, Levy processes with no negative jumps,
and branching processes*, Maphysto2000,
[Theorem1.2 pp7-8 and finite-activity case p9](https://www.maphysto.dk/oldpages/events/LevyBranch2000/notes/bertoin.pdf).
Revisited the statement, complete converse construction and finite-activity
paragraph. The jump measure is positive on (0,infinity), integrates
min(1,t), and killing/drift are nonnegative. The converse constructs the
jump sum using a Poisson point process. Finite jump mass with zero drift
is the compound-Poisson case; the subsequent exclusion of that case does
not apply to this theorem. C032u already supplies the finite positive Pi
and zero killing/drift needed by the audit. No density or finite first
moment is required. Earlier source coverage is reused, not replaced by a
new general construction proof.

Steven P. Lalley, *Levy processes, stable processes, and subordinators*,
PDF dated12 April2007,
[Definition5.1, (5.2)-(5.4), printed p12](https://galton.uchicago.edu/~lalley/Courses/385/LevyProcesses.pdf).
Revisited the definition and complete conditioning argument. Jumps are
iid and independent of a positive-rate Poisson count; conditional on n
jumps the sum has the n-fold convolution law. Nonnegative jumps permit
the stated Laplace transform. This covers C032u's positive series. The
PDF text extraction corrupts symbols in the displayed transforms, so
the readable conditioning argument and Bertoin's explicit exponent,
with prior notes1552, are the coverage used; no inference from a corrupted
display is needed. This source is dated, improving the earlier undated
citation record without changing the theorem imported.

Ante Mimica, *Laplace transform*, Dresden course27 April-1 May2015,
[Proposition1.4(iv), printed pp6-7](https://web.math.pmf.unizg.hr/~amimica/lt.pdf).
Revisited the full statement, Borel convolution definition and complete
part(iv) proof, which integrates exp(-lambda*(x+y)) against the positive
product measure. The half-line measures have finite transforms at every
positive parameter. Finite positive measures meet this condition; no
endpoint derivative or moment assumption is needed. The setwise definition
also supplies the interface for auditing positive convolution. The audit
must still justify its own induction and summation; the source does not
state the family-specific threshold. Reuse notes1552 for C032u's already
established uniqueness import; no new inversion or endpoint formula is used.

C032m's holomorphy and primitive definitions, C032q's bounded integral
interface, C032t's width-ordering input and C032u's finite positive series
are existing local inputs. They leave no essential unread theorem for
this narrowly specified audit. They do not pre-approve the mass term,
Taylor arithmetic, strict comparison of constants, or implication scope
in C032v. Those are precisely next turn's mathematical checks. No new
source is needed merely to reprove general compound-Poisson or transform
facts, and no new actual-family inequality is derived here.

## Decision and limitations

SPECIALIZE: sources cover the general tools; the audit checks the local
application. Classification of the completed literature turn is
NOVELTY_UNCHECKED; this gate makes no originality judgment. The planned
audit may be REPRODUCTION, using the now-ready assessment1566. No new
external keyword search was necessary beyond the recorded discovery:
the target and assumptions stay within notes1552/1562/1565.

C032v remains unaudited. Retain actual divisor/multiplicity,
zero-ordinate exclusion, strip/counting, verification through100,
first-zero/tail, heat and the two fixed-v1 external-preprint qualifications.
Neither source-wide correctness nor finite-zero data is recertified.
No RH, profile positivity, law density, moment, full J_eta=0 or unsmoothed
Xi realization is added. Mathlib matching coverage remains unchecked and
unknown. A central creative target still lacks a concrete continuum
witness or controlled dual approximation; that blocker is not overcome
by approving an audit. No lemmas, mathematical scripts, DAG or PROOF
changes are warranted by this step.
