# Positive transition to finite collision — completed source comparison

TARGET: Review source coverage for the finite-collision reduction: if 0<lambda_*<1/8 is an all-real transition for F, must F(lambda_*,.) have a real multiple zero in the compact region supplied by L488?
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Narrow local heat/literature/failure searches and exact multiple-zero/transition/Newman-constant queries; inspected Polymath Proposition 3.1(i)–(ii), its complete proof, Theorem 3.2 and Proposition 3.3's first-contact proof. No exact standalone transition theorem was located in this bounded search; no novelty inference follows.
SOURCE_EVIDENCE: D. H. J. Polymath, arXiv:1904.12438v2 (4 August 2019), Section 3, Proposition 3.1(i)–(ii), equations (28)–(33), Theorem 3.2 and Proposition 3.3; https://arxiv.org/html/1904.12438v2 and https://arxiv.org/pdf/1904.12438v2 . Reuse L488 and its saved Theorem 1.5 assessment for the common tail; do not repeat its saddle analysis.
COMPARISON: Known simple-zero continuation, zero persistence by Rouche and the common compact-time tail cover the tools. The precise transition implication still needs a local compactness specialization, not an import of a stated collision-exclusion theorem. Arbitrary finite endpoint multiplicity is allowed; its splitting law is available but unnecessary to the proposed reduction.
GAP: Write and check endpoint closure from the right, compact capture of incoming nonreal zeros and failure of simple-zero persistence at a limiting zero; these are pending applicability obligations, not results established by this literature step.
REASON: Adequate accessible primary coverage replaces the unread-splitting lead and makes a bounded standard specialization actionable. It isolates a possible finite obstruction but supplies no theta-specific exclusion, all-degree signs or RH proof.
SCOPE: Completed literature-only comparison. A separately gate-approved mathematical turn may specialize L058/L488 and standard Rouche/implicit-function/compactness arguments to the exact transition below. No lemma or mathematical script is written here; no new saddle estimate, global zero labeling or limit to lambda=0 is covered.
LITERATURE_REASON: The target changes from the uniform high-zero count to the boundary of all-real times; essential source comparison for that implication has not yet been performed.

## Exact proposed statement and test (retained nomination)

Here an all-real transition means that for some epsilon>0, every zero
of F(lambda,.) is real for lambda_*<lambda<=lambda_*+epsilon, while
there are times lambda_j<lambda_* tending to lambda_* at which F has
a nonreal zero. Restrict epsilon so the relevant interval lies inside
(0,1/8). Reality at lambda_* is part of what must be justified, not an
extra assumed conclusion. No simplicity or fixed labeling of all zeros
is assumed. The proposed output is existence of a real zero of exact
multiplicity at least two at lambda_*, with bounded real coordinate.
The statement is only a proposed target, not a result of the present turn.

Essential inputs now inspected: L018/L019/L058 for conventions and
analyticity; L488's statement, source qualifications and normalization;
the full L060/L061 proofs. L126/L128's precise scope warnings were checked;
they assert no global continuation. Keep the inaccessible KKL/CSV endpoint
route parked: it is not needed for this different compactness test.

Continue only if known results or an explicitly assessed compactness
specialization cover arbitrary multiplicity and every incoming nonreal
zero. Otherwise name the missing hypothesis and choose a different
test. Even success would leave finite-collision exclusion, lambda=0,
all-degree signs and RH unresolved. Full Mathlib coverage is unchecked.

The nomination screen also found prior failures of generic log-concavity
and universal-factor creation arguments in the September 9 and
September 21 attempt records, and L487's backward-energy obstruction.
These prevent labeling another generic shape/energy argument creative.
No new theta-specific exclusion criterion is presently justified; no
creative calculation or claim of novelty is approved here.

## Source evidence and exact comparison completed this turn

Primary source: D. H. J. Polymath, *Effective approximation of heat flow
evolution of the Riemann xi function, and a new upper bound for the
de Bruijn–Newman constant*, Research in the Mathematical Sciences **6**
(2019), article 31, version linked above. Read Section 3's complete
Proposition 3.1 proof and relevant Proposition 3.3 first-contact cases.
Proposition 3.1(i) gives a unique smooth nearby zero at a simple zero.
Part (ii) treats every repeated order m>=2 using Hermite roots, Taylor
rescaling and Rouche exhaustion. Neither assumes t>Lambda. Proposition
3.3 uses compact first contact with extra barrier hypotheses; it is not
the proposed transition theorem. Theorem 3.2 supplies the cited strip.
Theorem 1.5(i)–(ii)'s uniform tail is reused through L488, with its cited
asymptotics and independent-review qualification retained.

Local matching is already documented in L488: F(lambda,z)=8 H_(4lambda)(2z).
L018/L019/L058 fix the exact theta family, conjugation, joint entirety and
nonzero slices. No new normalization proof is needed. L058 has the
conjugation argument for a real simple branch. L061's finite-disc counting
and closedness-of-reality paragraphs already justify the standard local
tools, but its forward theorem assumes boundary nonvanishing throughout
an interval. Do not cite it as an unconditional backward theorem.
L060 handles m>=3 locally; its extra splitting work is not required to
show existence of some nonsimple endpoint zero. In particular an O(t)
location error alone must not be used to decide an odd central root's
reality. The next target asks for multiplicity >=2, not exactly two.

The proposed specialization has three explicit obligations for the later
proof: (1) endpoint reality must follow from right-hand all-real times,
without assuming it; (2) the L488 rectangle must capture every selected
incoming nonreal zero for all sufficiently large sequence indices on one
fixed positive-time interval; (3) the limiting zero must be tested against
the unique simple branch, including its nearby complex zeros, not merely
against a chosen real branch. Finite multiplicity must be justified by
nonzero entire slices. No labeling or uniform lower bound on every real
zero gap is required by this proposed finite compactness argument.
This paragraph specifies a covered test, not its completed proof.

Queries included “de Bruijn-Newman multiple zero positive”, “Newman
constant double zero Lambda”, “Ki Kim Lee 2009 multiple zeros”,
“de Bruijn Newman simple zeros Hurwitz”, and “de Bruijn-Newman transition
multiple”. General surveys, repository claims and search excerpts were
not adopted as theorems. The bounded search did not locate a stronger
direct collision-exclusion result applicable here. Previously blocked
CSV/KKL proofs were not reopened. The standard reduction is not claimed
original; the accessible primary/local inputs suffice for its separate
proof attempt.

Duplicate/failure check: L058's scope and L061's directional example
already warn of possible collisions; neither states this global transition
reduction with a common tail. L126/L128 warn against an infinite-supremum
interchange, which this target must avoid. The positive-endpoint source
comparison parks inverse-gap endpoint integrability. September 9/21
generic-shape failures and L487's recorded energy obstruction remain
unchanged; no new inference from those generic properties is proposed.

Decision: source coverage is ready for the specified standard specialization,
subject to separate supervisor approval of its newly written continuation.
No endpoint, multiplicity or collision theorem has been proved this turn.
Full matching Mathlib coverage remains unchecked, not absent.
