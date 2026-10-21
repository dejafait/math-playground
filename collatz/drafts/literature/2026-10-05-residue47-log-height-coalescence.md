# Full-height coalescence clocks — source assessment

TARGET: Determine whether, for every real C with 0<C<1/log(12) and B>=0, there are unbounded odd integers n=47+243k, k>=0, having no positive c<n with c=20 modulo 27 and T^s(c)=T^t(n) for integers 0<=s,t<=C log(n)+B, retaining actual parities on both paths.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Ten focused queries on logarithmic coalescence, lower time bounds, the exact cylinder, the coefficient and CRT found no matching theorem; queries and inspected versus unread leads are recorded below. No novelty is inferred.
SOURCE_EVIDENCE: Read Rozier (2019), Definition 1 and Lemma 1 with proof, pp. 2–3; reinspected Sodelin B-S20-ANCESTOR-DEPTH-OBSTRUCTION-001 statement and relevant proof/scope, lines 8–74. Burson arXiv:2005.09456v2 landing page identifies a withdrawn numerical study, not an inspected theorem. Reuse LaDue v3 and the L4/L5 comparisons from the two prior assessments.
COMPARISON: Standard finite parity coding and the Chinese Remainder Theorem supply the arithmetic infrastructure; audited local L026 supplies the exact guarded obstruction for each horizon. Neither that lemma nor the inspected external statements supplies the height/horizon conclusion. The difference is controlled selection of roots above L026's size threshold and comparison with the logarithmic clock.
GAP: Establish a uniform upper height estimate for selected L026 roots while keeping n>12^L, then handle every fixed real 0<C<1/log(12), B>=0 and both integer clocks. No such estimate or logarithmic obstruction is proved here.
REASON: Essential source coverage is now adequate for a separate quantitative specialization of L026 using named CRT and finite parity coding; no new coalescence proof or reproof of those standard inputs is needed.
SCOPE: The unchanged TARGET, using L026's valuation-4 progression, exact original-root order, both actual paths including zero clocks, natural logarithms and a strict coefficient below 1/log(12). Endpoint coefficient equality, larger coefficients and other cylinders are outside scope.
LITERATURE_REASON: The duration changed to full log(n) after step 042; the initial-valuation assessment did not cover quantitative root-height selection. The supervisor required this separate assessment before calculation.

Here log denotes the natural logarithm. This assessment approves one
separate mathematical attempt on the unchanged TARGET. It derives no
logarithmic-clock obstruction, root-height estimate or new lemma.
The suggested coefficient is tied to L026's existing strict size
requirement n>12^L; its applicability remains the next calculation.

The main gap is universal eventual descent. A full-height companion
clock could potentially transfer convergence to a hypothetical least
residue-20 root while allowing later path information. Quantifying a
lower obstruction to its time coefficient would distinguish this route
from the exhausted initial-valuation coordinate. It would not decide
larger logarithmic coefficients, general clocks, convergence of finite
bases, or the other surviving cylinders.

Essential local input is audited L026, with L025 only through its offset
estimate and Rozier's cited finite parity coding. Its hypotheses require
an integer L>=6, a positive n, n=47 modulo 3^(L+4),
81n+97=0 modulo 2^(L+1), and n>12^L. Its conclusion excludes every
positive residue-20 companion below the same n at both clocks at most L,
and fixes v_2(n+1)=4. The lemma's quantifier covers every qualifying
root, not just the four sampled roots. Its proof identifies one full
CRT class modulo 2^(L+1)3^(L+4), but states no controlled representative
height for the proposed clock. That is the precise missing application.

The standard named Chinese Remainder Theorem gives a unique simultaneous
class modulo the product for coprime positive moduli. These binary and
ternary moduli are coprime; the binary coefficient 81 is invertible,
as already used in L026. Reuse this theorem, then write out the necessary
representative selection and height comparison in the research turn.
Do not reprove CRT, finite parity coding, L025's offset inequality or
L026's coalescence obstruction. No convergence, least root, companion,
least positive CRT root, or convergence of a base set is assumed.

The discriminating calculation is to select roots for increasing L,
above the strict size threshold, with a uniform upper logarithmic height
estimate strong enough to imply C log(n)+B<=L for each stated fixed C,B.
Record explicit constants or a proved limiting estimate; an unbounded
progression for fixed L is insufficient, because increasing n also
increases its allowed clock. The roots must tend to infinity, retain
valuation 4, and meet all of L026's guards. A bound with excessive
exponential cost stops this particular selection mechanism; it does not
prove the cover or authorize retuning initial-valuation clocks. No
estimate sought in this paragraph is an established conclusion.

An exact obstruction for every stated C,B is decisive for this target
and limits logarithmic companion clocks. It leaves the endpoint
coefficient, larger clocks, other surviving cylinders and universal
eventual descent unresolved. Attempt 015 and Attempt 014 keep their
stops on their respective scopes; this is a different duration coordinate.

## Primary statements and reuse

Olivier Rozier, *Parity Sequences of the 3x+1 Map on the 2-adic Integers
and Euclidean Embedding*, INTEGERS 19 (2019), A8,
[Definition 1, Lemma 1 and proof, pp. 2–3](https://math.colgate.edu/~integers/t8/t8.pdf#page=2),
states that each finite binary parity word of length j determines exactly
one integer class modulo 2^j. The affine iterate identity supplies its
congruence; section 2 extends the functions to signed integers. Thus
the existing signed-anchor prefix transfer in L026 has the correct
source domain. No real-height estimate or two-path residue-20 theorem
is provided by this finite coding result.

Sodelin, [B-S20-ANCESTOR-DEPTH-OBSTRUCTION-001](https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/lemmas/Bounded_Ancestor_Depth_Obstruction.md),
live main read 2026-10-05, lines 8–41 and 56–74, excludes smaller
residue-20 ancestors through time L for 47+3^(L+3)t. Its proof transfers
legal inverse words to anchor 47, retains the nonnegative affine offset
and includes the empty word. Its CRT extension simultaneously prevents
bounded direct descent and ancestors; lines 67 and 71 expressly leave
general coalescence open. Hence no logarithmic two-path theorem is
imported from it. Its later explicit CRT representative on a different
q5 cylinder is not a theorem about this TARGET and is not used.
This is informal public mathematics; no immutable revision or Lean
formalization was retrieved.

The ready assessments
`2026-10-05-residue47-bounded-coalescence.md` and
`2026-10-05-residue47-odd-run-clock-coalescence.md` retain the inspected
LaDue arXiv:1709.02979v3 (2017-11-15), Lemma 3.1 and Theorems 3.2/4.1,
pp. 3–5, including both parity cases. Its guarded adjacent-pair equality
has a clock depending on the initial odd-run length and a specified
companion m-1; it does not impose the required residue-20 companion.
The L4/L5 and Mersenne comparisons retain their whole-family versus
parameter-refined scope distinctions. None bounds all refined two-path
coalescence times by log(n). Their primary passages were already assessed
and were not reloaded for another audit. The optional Novgorodtsev
adjacent-pair manuscript remains unread as recorded there; that source
is not an essential dependency of this independent height calculation.

## Search and access evidence

Executed queries:

- `Collatz coalescence logarithmic time smaller integer parity sequences`
- `Collatz "coalescence" "log" residue`
- `Collatz "47" "12" coalescence logarithmic`
- `Collatz coalescence "logarithmic" smaller residue`
- `Collatz coalescence "lower bound" time logarithm`
- `"47" "243" "coalescence" Collatz`
- `"Bounded_Ancestor_Depth_Obstruction" logarithmic`
- `Collatz "coalescence" "log(n)"`
- `Collatz "coalescence" "log(12)"`
- `Collatz "coalescence" "Chinese remainder"`

Roy Burson, *On the Distribution of the First Point of Coalescence for
some Collatz Trajectories*, [arXiv:2005.09456v2](https://arxiv.org/abs/2005.09456v2),
revised 2020-10-16, is explicitly withdrawn. Its landing-page abstract
describes numerical coalescence distributions for specific pairs. The
default PDF returned 404; no theorem or proof was inspected or imported.
It is not an essential source blocker. Random-walk/stochastic cluster
coalescence hits describe other dynamics; search snippets, numerical
studies and claimed Collatz resolutions are not theorem evidence here.
No adequate matching external conclusion was established by this bounded
search; neither novelty nor absence from the literature is claimed.

Local duplicate/failure checks used L026's exact hypotheses/conclusion
and quantifier passage, L025's source statement, and Attempts 014–015.
The supplied overview keeps L024's height-independent valuation budget
failure separate. No cross-notebook input was read. No lemma or
mathematical script was written or run, and the proof overview and DAG
remain unchanged. Completed outcome is EXPLORATION and classification
NOVELTY_UNCHECKED: source coverage, without mathematical advance beyond
the inspected inputs. No mathematical exploration turn is spent.

## Mathlib

Full matching logarithmic-clock residue-20 obstruction: **not checked**.
Supporting CRT, logarithmic estimates and parity coding: **not checked**.
Unknown availability is not absence. The named CRT and precise Rozier
citation are sufficient standard inputs for the approved informal test.
