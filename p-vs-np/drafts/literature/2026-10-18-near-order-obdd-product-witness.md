# Nearby orders: proposed bounded witness target

TARGET: Test whether Boolean-zero products of two dense width-three OBDDs whose orders differ by at most floor(log₂ M) adjacent transpositions have polynomial-full-bit Boolean/commutator affine-ABP witnesses, with M measured before the witness.
CHECKED: 2026-10-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched adjacent-swap OBDD reordering, exact Boolean/commutator witness and noncommutative-IPS terminology; followed Rudell and the Bollig–Löbbing–Wegener reference trail. Compared L026, L071's post-compilation graph component, L087, Attempt 030 and the earlier common-order/two-order assessments; details and access qualifications below.
SOURCE_EVIDENCE: Read Rudell ICCAD 1993 §§2,4–4.1 pp.42–44, including skipped cofactors, duplicate/degenerate nodes and retained references; Bryant's restored §4.3 pp.12–14 and reused its previously inspected complexity corrections; Tzameret arXiv:1004.2159v2 (1 August 2010) Definition 3.1, Lemma 3.4/Claim 3.5 pp.7,9–10 with both induction cases; Itsykson et al. STACS 2017 §1.1 p.43:3. Reused the inspected LTW/FSTW comparison and read the relevant local correction/graph proofs.
COMPARISON: Primary sources supply local Boolean reordering and formal formula-context commutation, while L026/L071 supply exact common-order correction graphs. No inspected theorem supplies this near-order full-bit affine-ABP witness statement. Formula-size or Boolean-equivalence results alone do not give its conclusion; no novelty or impossibility is inferred.
GAP: Specialize the two-level swap to an exact commutator-placeholder correction of ordered diagram representatives, aggregate it without path unfolding, bound every intermediate diagram and independent graph copy in pre-witness M, and combine with the common-order product correction while retaining the original fg. All these new applicability/accounting obligations remain unproved.
REASON: Essential Boolean-swap and formal-correction mechanisms are covered for one bounded specialization attempt on the unchanged target. The review approves source scope, not a witness theorem; a separate approval of this newly completed assessment precedes mathematical work.
SCOPE: L087's two explicit dense deterministic width-at-most-three diagrams and full pre-witness M/B encoding over free F₂, with distance at most floor(log₂ M) between the supplied permutations; exact original fg, Boolean/pair-commutator placeholders only, explicit acyclic affine-edge ABPs and all independent copies/dictionaries charged. Common-order distance zero is permitted; intermediate width three is not assumed.

## Original proposal — historical, superseded as a source gate

The following proposal is retained verbatim. Its statements that coverage
is missing or that this file approves nothing describe the initial gate;
the completed comparison below replaces that gate without proving the target.

The main gap remains unrestricted SAT decision/separation. This proposed
intermediate target could test a controlled relaxation of common-order
data without asserting a universal supplier. It is not a way to evade
L087 by assuming W₂ or its conclusion. No result about near orders is
derived or approved here.

Use L087's exact input encoding M, two supplied dense width-at-most-three
diagrams on the same listed alphabet, and their separately ordered
free-F₂ representatives f,g. The proposed distance is the minimum number
of adjacent transpositions between their supplied permutations. Require
the same formal identities H(y,0)=0 and H(y,B)=fg, with only the full
Boolean/pair-commutator dictionary B, one polynomial in the pre-witness M,
and every copied graph and dictionary charged. Do not replace fg by a
merely Boolean-equivalent polynomial. The target concerns existence of
such witnesses for Boolean-zero products; no promise tester is assumed.

Essential prospective local inputs are L026's ordered correction
interface and L087's exact representatives/encoding, with L041 only if
formal verification is needed. Their use alone does not establish the
new statement. First search exact and stronger known statements and
local duplicates/failures. Inspect the primary reordering hypotheses and
any necessary formal correction cases. Retain Attempt 030's separate
common-order availability stop and L087's unrestricted-order burden.

Continue only if source coverage supports an independently testable
polynomial full-bit target with the exact output retained; otherwise
narrow or abandon this proposed regime on the actual evidence. A
Boolean reordering bound without formal correction coverage is not a
ready certificate theorem. Arbitrary-order witnesses, general ER data,
certificate selection and unrestricted SAT remain unresolved. Mathlib
coverage for this new target is not checked. The next turn is
literature-only; this file does not approve mathematical work.

## Completed literature comparison — step 339, 2026-10-19

**Gap, target and use.** Unrestricted SAT decision/separation remains the
main gap. TARGET asks only for restricted alternative witnesses, with one
fixed full-bit polynomial in the input before H exists. Success could
supply a controlled relaxation of the common-order witness interface;
it would not provide faithful diagrams for arbitrary ER, arbitrary-order
witnesses, alternative-certificate hardness or decision transfer.

**Search and local comparison.** Actual queries included `OBDD adjacent
variable swap size factor 2 reordering Sieling Wegener`, `OBDD
noncommutative IPS commutator variable order reordering polynomial
certificate`, `"OBDD" "commutator" certificate reordering`, `"OBDD"
"adjacent" "factor of 2"`, `"OBDD" "noncommutative" proof systems`,
`"Dynamic Variable Ordering for Ordered Binary Decision Diagrams" pdf`,
and `"On the effect of local changes" "pdf"`. Searches located sources;
snippets were not accepted as theorem evidence. The named local
assessments, Attempt 030, and histories 336–338 contain no completed
near-order supplier. Read L026's ordered-multilinear injectivity and
equations (4)–(12), L087's hypotheses/M/B convention, and L071's explicit
value/K/W graph construction and post-compilation audit passages.
L071's graph component realizes the identical correction polynomials;
its whole treewidth-two compilation theorem is not invoked without its
treewidth hypothesis. These inputs neither certify a swap correction nor
bound intermediate reordering size. Attempt 030's universal common-order
availability obstruction remains independent and unchanged.

**Primary swap construction.** Richard Rudell, *Dynamic Variable Ordering
for Ordered Binary Decision Diagrams*, ICCAD 1993, pp.42–47,
[readable paper scan](https://www.larshj.dk/PUMA/references/Dynamic%20variable%20ordering%20for%20ordered%20binary%20decision%20diagrams%20-%20p42-rudell.pdf),
§§2,4–4.1, pp.42–44 (PDF pages 1–3). The tuple convention puts the
positive cofactor first. Section 4.1 rewrites a node using its four
two-variable cofactors, with two candidate new child nodes. It treats a
missing second test by retaining the old child, permits degenerate or
already existing children, and retains a referenced old node rather than
freeing it. Its claim is preservation of the Boolean function, not of an
ordered free-ring polynomial. Ordinary undecorated edges meet the target;
the discussion of attributed edges is unnecessary. No optimal-order or
sifting guarantee is imported. A deterministic full-bit ledger and dense
unreduced specialization still need justification; hash-table timing and
garbage collection are not mathematical encoding bounds. Do not import
an unread factor-two theorem from this passage.

The Toronto copy of the same paper returned no extracted lines and its
screenshots exposed no inspectable images; shell retrieval failed DNS.
The alternative scan above supplies readable primary text, including the
essential cases. These initial failures are resolved for this scoped
review, rather than a continuing source blocker.

**Boolean combination and the stronger-looking leads.** Randal E.
Bryant, *Graph-Based Algorithms for Boolean Function Manipulation*, IEEE
TC 35(8), 677–691 (1986),
[author-restored copy](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf),
§4.3, restored pp.12–14, gives the memoized pair algorithm, terminal and
unequal-index cases and its size analysis. The shared input order is
explicit in §1.1. Reuse the earlier assessment's inspected Table 1
correction for reduction cost; only a conservative polynomial bound is
needed. The restored p.14 note refutes the proposed input-plus-output
linear bound. Neither the Boolean algorithm nor canonicity witnesses
the difference between the original differently ordered product and its
reordered representative.

Bollig–Löbbing–Wegener, *On the effect of local changes in the variable
ordering of ordered decision diagrams*, IPL 59(5), 233–239 (1996),
[DOI 10.1016/0020-0190(96)00119-6](https://doi.org/10.1016/0020-0190(96)00119-6),
was located through the factor-two reference trail, but only its abstract
was accessible. Its quantitative theorem is **unread and not imported**.
Rudell's inspected explicit operation suffices to formulate the bounded
size test without that sharper claim. Drechsler–Sieling's 2001 survey
§2.4/Figure 8 was inspected as orientation only; the primary operation,
rather than a survey assertion, supplies coverage.

**Formal correction coverage and its limit.** Iddo Tzameret,
[*Algebraic Proofs over Noncommutative Formulas*](https://arxiv.org/pdf/1004.2159v2),
arXiv:1004.2159v2, 1 August 2010, 20-page PDF as retrieved 2026-10-19, Definition 3.1 p.7,
Lemma 3.4 and Claim 3.5 pp.9–10. Read the single-occurrence context
statement and both addition/product induction cases. NFPC uses the
original Boolean and commutator axioms, with left/right variable
multiplication; the lemma supplies polynomial formula-size commutator
proofs. It does not state our single affine-ABP certificate bound in
shared diagram size. Unfolding all diagram paths to invoke it is not
licensed. The archived assessment
`drafts/literature/2026-10-05-obdd-reduced-data.md` already inspects LTW
arXiv:1412.8746v4 Lemmas 3.6–3.7 pp.17–18, including exact
zero-at-zero rewrite/commutator witnesses and their formula-size scope,
and FSTW ToC 17(10) Propositions 4.5–4.6 pp.30–32, whose multilinear
corrections are commutative. Reuse those comparisons: neither removes
the exact free-ring/ABP reception obligation. No reproof of their
general commutation or multilinearization results is needed.

Itsykson–Knop–Romaschenko–Sokolov,
[*On OBDD-Based Algorithms and Proof Systems That Dynamically Change
Order of Variables*](https://drops.dagstuhl.de/opus/volltexte/2017/6991/pdf/LIPIcs-STACS-2017-43.pdf),
STACS 2017, §1.1 p.43:3, allows reordering but retains a common order
for conjunction inference. Its arbitrary-order hardness warning gives
no lower bound for this logarithmic-distance regime or for alternative
affine-ABP witnesses. L087 likewise supplies no distance bound on its
hard pairs, so its NP=coNP conditional is not automatically inherited
by the restricted target.

**Approved scope and discriminating test.** After separate approval of
this assessment, attempt exactly TARGET. The proposed mechanism is
local adjacent reordering followed by the existing common-order product
interface. First test an exact commutator-only swap correction for the
original ordered state polynomial, with graph propagation above the swap
and no path unfolding. This is a proposed applicability test, not a
formula or lemma derived here. A Boolean-equivalent output alone fails.
Then test whether all intermediate diagrams, retained correction graphs
and their compositions admit one fixed polynomial in original M across
at most floor(log₂ M) swaps. A polynomial cost raised recursively to the
number of swaps does not meet that threshold. Intermediate diagrams may
have greater width; every layer, terminal, repeated successor, unused
state, copied suffix, name and full B dictionary must be counted. Finally
the original fg, rather than a reordered replacement, must be recovered
by formal witnesses that vanish when placeholders are zero. L026's
injectivity may only compare representatives in the same ordered
multilinear subspace. No semantic-promise tester, W₂ or finder is assumed.

Continue if these interfaces yield H(y,0)=0 and H(y,B)=fg with a bound
K(M+2)^c for fixed K,c. Narrow or abandon this mechanism on an explicit
identity failure or an unavoidable superpolynomial copying/state cost;
a failed naive implementation alone is not a nonexistence theorem.
Do not extend coverage to arbitrary orders, general weighted diagrams
or arbitrary ER. Those are different targets. Mathlib coverage of the
full target and the new specialization is **not checked**; no absence
claim is made.

**Outcome and exact main problem.** This is a completed source comparison,
not a new witness result or progress beyond the checked sources. No
lemma, mathematical script, PROOF.md or DAG.md was changed. On 2026-10-19
the [Clay page](https://www.claymath.org/millennium/p-vs-np/) still lists
the problem as unsolved; its linked [Cook description](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf),
§1 pp.1–2, retains ordinary deterministic polynomial-time languages and
one polynomially bounded checking relation. This is the version already
fixed in foundations/01-model-and-target.md. Restricted witness success
would leave that exact main gap unresolved.
