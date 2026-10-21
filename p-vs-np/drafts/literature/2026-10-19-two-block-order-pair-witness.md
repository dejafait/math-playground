# Two exchanged variable blocks — completed source comparison

TARGET: Construct an original-M polynomial Boolean/commutator affine-ABP witness for the exact Boolean-zero product of two supplied dense width-three OBDDs with orders A·B and B·A, retaining each block's internal order and allowing both block sizes to be unbounded.
CHECKED: 2026-10-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 352 searched two-block exchange, cyclic shifts, bounded-width block reordering, two-order conjunction and noncommutative OBDD witnesses; compared L026/L035/L071/L087–L090 and Attempts 018/030. No inspected full target match; actual queries, primary reading and unread leads are recorded below, without a novelty claim.
SOURCE_EVIDENCE: Reopened Rudell ICCAD 1993 §4.1 p.44, Bryant IEEE TC 35(8) (1986) §4.3 pp.12–14, and Li–Tzameret–Wang arXiv:1412.8746v4 Lemmas 3.6–3.7 pp.17–18 with essential cases; read Bryant's author-hosted 2018 chapter §7 pp.13–14 and Meinel's primary publication listing. Reused previously inspected graph-composition and formula-commutation assessments; links, versions and receiving qualifications follow.
COMPARISON: Sources supply Boolean swaps/common-order Apply and formula-sized formal commutation; local L035 and L026/L071 supply graph-sized commutators and common-order corrections. No inspected theorem covers both unbounded blocks with the original-fg free-ring identities and original-M encoding bound. L088–L090 and the arbitrary-order hardness comparison do not settle this restriction.
GAP: Establish a block-boundary construction with a fully paid formal correction retaining the original fg and one fixed full-bit polynomial in pre-witness M, without unfolding paths or enumerating assignments to an unbounded block. Neither a suitable construction nor its bound is proved here.
REASON: Essential component coverage and a bounded discovery search support one mathematical test of the unchanged block-exchange target; no essential inaccessible theorem is assumed. Optional unread block-sifting leads are not inputs. The new block-boundary interface and ledger remain proof obligations, not imported results.
SCOPE: Exactly two supplied dense deterministic width-at-most-three OBDDs over the same named alphabet, orders A·B and B·A for disjoint nonempty unbounded lists preserving both internal orders; exact free-F₂ representatives, Boolean-zero fg promise, complete original B/dictionaries and pre-witness M from L087; explicit acyclic affine-edge H only, with no semantic tester, treewidth or arbitrary-order witness premise.

## Original proposal and relevance

The following proposal is retained; its initial REVIEW_REQUIRED gate is
discharged by the completed comparison below. It asserts no construction.

The main gap remains unrestricted SAT decision/separation. The intermediate
target is an alternative restricted interface toward L087's arbitrary-order
W₂ question. A and B are disjoint nonempty lists whose union is the whole
named alphabet; the orders are precisely their two concatenations. Neither
length has a logarithmic or constant bound. Retain L087's pre-witness M,
complete original B/placeholder dictionaries and original representatives
f,g. Retain fg(a)=0 on all Boolean assignments as a promise, not an oracle.
The output sought has H(y,0)=0 and H(y,B(y))=fg, with one fixed polynomial
full-bit bound in M.

A possible avenue to assess is use of the explicit state information at
the block boundaries together with paid formal order corrections. No
sufficiency theorem, state-count bound or correction identity for this
avenue has been derived or approved here. Check standard OBDD block-order
results, stronger representation statements, their width/encoding dependence
and known obstructions. A theorem about Boolean equivalence alone still
requires an assessed original-polynomial correction interface.

Potential local inputs to assess are L026's ordered identities, L035's
x-only commutator graphs, L071's post-compilation component and L087's
B/M convention. L090 is an audited small-set comparison, not coverage of
arbitrary block sizes. L085's common-order weighted graph component is a
possible additional local lead only if needed; its applicability here has
not been assessed. No cross-notebook input is proposed. Preserve Attempts
018/030: repeated approval supplies no mathematics, and restricted value
availability obstructions do not establish all-witness hardness here.

Continue to mathematics only after IMPORT, SPECIALIZE or EXPLORE coverage
identifies the exact formal interface and full resource threshold. A cost
exponential in either unbounded block, an identity only in the Boolean
quotient or an unassessed semantic zero tester fails this target; record
the specific obstruction or choose a materially different test. Do not
weaken the target silently. General W₂, ER data availability and SAT
transfer remain open even if the restricted construction succeeds.
Mathlib coverage is not checked; no absence claim is made.

## Step 352 — search and inspected primary inputs

Queries included `OBDD swapping two blocks variable order width bounded
block reordering`, `OBDD conjunction opposite block order bounded width
polynomial`, `noncommutative IPS OBDD commutator block variable order
polynomial certificate`, `"OBDD" "block exchange"`, `"OBDD" "cyclic
shift" "width"`, `"OBDD" "blocks" "2^" swap width`, `"OBDD" "block
swap" width`, `"OBDD" "block" "interchange" width`, and the exact
titles of the local-change and block-sifting papers below. These are
discovery searches, not proof evidence or a novelty certification.

1. Richard Rudell, *Dynamic Variable Ordering for Ordered Binary Decision
   Diagrams*, ICCAD 1993, 42–47,
   [primary scan](https://www.larshj.dk/PUMA/references/Dynamic%20variable%20ordering%20for%20ordered%20binary%20decision%20diagrams%20-%20p42-rudell.pdf),
   §4.1 p.44 (PDF p.3). Reopened the complete four-cofactor operation:
   missing second tests, degenerate/existing children and preservation of
   referenced nodes are included. The operation preserves Boolean
   functions. It provides no original-free-polynomial correction or
   all-snapshot bound for exchanging two unbounded blocks. Its hash-table
   implementation costs do not replace full explicit binary accounting.
   The Toronto mirror extracted no text; the cited alternative supplied
   the essential cases, so this is not an essential source blocker.

2. Randal E. Bryant, *Graph-Based Algorithms for Boolean Function
   Manipulation*, IEEE TC 35(8), 677–691 (1986),
   [author-restored annotated PDF](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf),
   §4.3 pp.12–14. Reopened terminal, equal-index, unequal-index and
   controlling-value cases, memoization and the complete pair-count
   analysis. Apply receives a common variable order. Reuse the inspected
   correction to the reduction-time claim from
   `drafts/literature/2026-10-05-obdd-reduced-data.md`; only a conservative
   polynomial component cost is relevant. A Boolean output diagram
   supplies no formal comparison between differently ordered inputs.
   Bryant's author-hosted *Binary Decision Diagrams: An Algorithmic Basis
   for Symbolic Model Checking* (2018 manuscript),
   [§7 pp.13–14](https://www.cs.cmu.edu/~bryant/pubdir/hmc-bdd18.pdf),
   was also read: adjacent exchanges preserve represented functions and
   sifting moves variables or small groups. This overview is orientation,
   not a block-exchange size theorem or a mathematical input.

3. Fu Li, Iddo Tzameret and Zhengyu Wang, *Characterizing Propositional
   Proofs as Non-Commutative Formulas*,
   [arXiv:1412.8746v4, 11 September 2015](https://arxiv.org/pdf/1412.8746v4),
   Lemmas 3.6–3.7 pp.17–18. Reopened both statements and all essential
   cases: placement in either product child or an addition context,
   scalar/variable bases, additive splitting and ordered product
   splitting. For formula inputs P,Q the commutator witness vanishes at
   zero placeholders, substitutes to PQ−QP and has size at most
   |P|²|Q|². F₂ is compatible, with minus equal to plus and pair-once
   commutator placeholders. This bound is in formula size; it does not
   authorize path unfolding of a shared input diagram or give the full
   present target. No general source theorem needs reproof.

Reuse `drafts/literature/2026-10-07-alternative-abp-commutator-witnesses.md`
for Raz–Shpilka's author manuscript, Definition 1 and Lemma 2 Step 1,
pp.4–6: separate-operand serial/parallel composition gives explicit
acyclic constant/linear-edge graphs. That assessment also delimits
Tzameret's July 2011 formula/context results and the two-bucket PIT and
formula factor-swap scope of Chatterjee et al., ECCC TR26-166,
Definition 1.1, Theorems 1.2–1.3 and Appendix A.3 Lemma A.8. These
unchanged comparisons supply no missing block-witness theorem. Reuse
`drafts/literature/2026-10-18-two-order-obdd-product-witness-burden.md`
for the inspected two-order consistency-hardness comparison; its
arbitrary distinct permutations are not this two-block promise.

### Unread leads and access limits

Meinel–Slobodová, *Speeding up Variable Reordering of OBDDs*, ICCD 1997,
338–343, DOI 10.1109/ICCD.1997.628892, was located. The
[author's publication listing](https://hpi.de/meinel/lehrstuhl/research/former-research/bdd-research/accelerating-the-variable-reordering-process.html)
was inspected; its ICCD/IWLS links failed to open. Abstract/search text
is not theorem evidence: the complete paper and its quantitative
statements remain unread and are not imported. Likewise, the located
Meinel–Theobald book's §9.2.5/§9.3 contents are not an inspected
block-width theorem. Bollig–Löbbing–Wegener, IPL 59(5) (1996), 233–239,
DOI 10.1016/0020-0190(96)00119-6, remains the previously recorded unread
quantitative lead. None is an essential premise of the proposed
independent block-boundary proof test. Do not claim their results are
absent or weaker without reading them; refresh coverage if relying on
any of them becomes necessary. Other search hits were not imported.

## Local comparison and the authorized mathematical test

Read L026's complete ordered representative/injectivity argument and
equations (4)–(12), L035's x-only commutator statement and marked-edge
factorization, L071's explicit value/K/P/W graph construction and its
post-compilation audit, and L087's exact B/M definition. These are
component inputs, not a theorem about exchanging blocks. In particular:

- L035 accepts supplied x-only affine ABPs and bounds a commutator-only
  graph in their full input encoding. Its interface does not accept a
  recursively generated placeholder witness as an original-only input.
- L026/L071 correct a product in one common order, retaining ordered
  factors and cancelling paths. Use only L071's post-compilation graph
  component; the whole treewidth-two theorem retains its hypothesis.
  Injectivity is confined to a single ordered multilinear subspace.
- L088's audited local swap graph is a possible component if an explicit
  sequence is chosen; its logarithmic-distance bound is not a bound for
  all intermediate diagrams here. L089 moves one variable. L090 charges
  all assignments to a small supplied deletion set. Their statements
  do not cover two unbounded blocks. No new multi-move estimate is
  inferred by iterating one of their fixed polynomials.

Attempts 018 and 030 were read and preserved. Repeated approval alone
cannot advance the target, and universal faithful common-order value
availability already fails on a different promised family. That
availability stop is neither an alternative-witness lower bound for
these pairs nor a ban on this bounded test. No cross-notebook input is
used, and L085's optional weighted interface is not needed or approved.

The main gap remains unrestricted SAT decision/separation. A successful
result here would extend the restricted witness interfaces toward
L087's arbitrary-order W₂ question, while leaving general ER data,
arbitrary orders and SAT transfer open. The intermediate target is
exactly TARGET, without a bound on either block's length.

After this literature gate, test the proposed use of explicit states at
the block boundary and independently copied block subgraphs, with L035
for any necessary x-only factor exchanges and L026/L071 for common-order
products. This describes a mechanism to investigate, not a construction,
identity, state-count theorem or size estimate established here. Prove
that any sharing/reordering preserves exact ordered representatives or
write and charge its formal correction. Retain original fg, not just a
Boolean-equivalent common-order product; no Boolean-zero tester is
assumed or supplied. Keep original M fixed before all witnesses.

Continue only on a rigorous explicit H with H(y,0)=0 and H(y,B(y))=fg
and a single K(M+2)^c full-bit bound for absolute K,c, also accounting
for polynomial construction time, actual path degree, every independent
copy, state/edge/root reference, original name and complete dictionary.
Include constants, repeated successors, unused states, singleton blocks,
zero/no-path components and boundary terminal cases. A Boolean identity,
an implicit/shared arithmetic circuit, or a cost exponential in either
unbounded block fails the sought result. On an explicit identity or
uncontrolled copying/state-growth failure, preserve it and abandon or
change that mechanism; this would not refute existence of alternative
witnesses. No complete SAT route or new theorem is asserted.

## Completed-step record

This is LITERATURE / literature_comparison / NOVELTY_UNCHECKED with
outcome EXPLORATION: fresh target-specific comparison supplies EXPLORE
coverage and an actionable mathematical test, without a source import
settling the target or progress beyond the inspected sources. No lemma,
mathematical script, DAG or argument change was made. The source-review
temporary working checkpoint is superseded by this completed assessment.
Mathematical exploration usage remains one since step 349; this
literature turn neither spends nor resets it. Mathlib coverage of the
full target and specialization is not checked; no absence is asserted.
