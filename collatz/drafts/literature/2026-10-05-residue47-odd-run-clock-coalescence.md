# Root-dependent coalescence clocks: source assessment

TARGET: Determine whether there exist integers A>=1, B>=0 and N>=1 such that every odd n=47+243k>N, k>=0, has a positive c<n with c=20 modulo 27 and T^s(c)=T^t(n) for some 0<=s,t<=A v_2(n+1)+B, retaining actual parities on both paths.
CHECKED: 2026-10-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Fourteen focused queries checked valuation-dependent clocks, the exact cylinder, adjacent-pair coalescence, fixed valuations and later odd runs; the bounded-coalescence review was reused. No matching cover or all-linear-clock obstruction was established; query and access evidence follows.
SOURCE_EVIDENCE: Reinspected LaDue arXiv:1709.02979v3, Lemma 3.1 and Theorems 3.2/4.1 including both proof cases, pp. 3–5; read the workbench's F031.6 statement and accompanying parity/lifting argument, lines 490–523, as informal comparison only; inspected Barina (2025), sections 3.1–3.3, pp. 3–7. Earlier Rozier and Sodelin theorem assessments are reused within their scopes.
COMPARISON: LaDue supplies guarded clocks linear in the initial odd-run length for a specified adjacent companion, without the required residue membership. F031.6 has an additional exit valuation in its clocks and no residue guard. L025 and the inspected unrefined-family obstructions do not settle passage beyond the initial odd run with parameter-dependent companions.
GAP: Prove the exact guarded cover with explicit A,B,N or refute every A,B,N by unbounded counterfamilies; neither convergence, residue-20 companion existence nor a bound on later runs is supplied by the checked sources.
REASON: Complete essential changed-target comparison before research. The reviewed sources suffice for one bounded test using exact parity coding, without importing an unread lead or asserting novelty.
SCOPE: The exact TARGET, including zero clocks, refined parameter families, equal-slope cases, positivity, residue membership and order against the unchanged root; a fixed-initial-valuation obstruction after the first even exit is an admissible test of this TARGET. No unrestricted convergence or later-run bound is preapproved as a theorem.
LITERATURE_REASON: The duration hypothesis changed from constant clocks to A v_2(n+1)+B in step 039; the prior ready review did not cover that change.

## Proposed relevance and test

Universal eventual descent is still missing. A root-dependent coalescence
cover on the odd portion of the surviving cylinder could transfer
convergence from smaller residue-20 companions to a hypothetical least
root. Its even portion, finite exceptions and other surviving cylinders
would remain independent gaps. No complete route is presumed.

The duration coordinate is a=v_2(n+1), which is finite and positive for
these odd roots. The proposed linear bound can pass the initial odd run;
it is not another trial of a larger constant horizon. Review whether
known adjacent-pair coalescence at an odd-run exit, or a stronger theorem,
provides the required residue-20 companion, or whether a known obstruction
already refutes this duration bound. LaDue's inspected companion n-1
does not itself satisfy the residue requirement. Do not silently drop it.

Essential inputs for the review are L025 and the prior
`drafts/literature/2026-10-05-residue47-bounded-coalescence.md` source
comparisons. L014's conditional least-root convergence-transfer argument
explains the use, but no least root, uniform clock, finite-base convergence,
companion, or entry into any additional prefix class is assumed. The old
ancestor stop and L025 remain in force on their stated scopes.

## Decision and discriminating test

Approve one separate mathematical attempt on the unchanged TARGET.
The first discriminating test is to hold a=v_2(n+1)=4 and seek, for each
proposed finite horizon, an unbounded subfamily of the odd cylinder with
no admissible companion at that horizon. Such an all-horizon obstruction
on a fixed-a subfamily would refute a clock depending only linearly on a.
This is a proposed test, not an established counterfamily or an extension
of L025. It must treat the post-exit path with its actual parities.

An all-parameter cover with explicit constants or an all-horizon
fixed-a obstruction is decisive. A finite miss is diagnostic only;
L025's witnesses with a increasing beyond the tested horizon do not
meet this new test. Continue after a finite test only if it identifies a
specific post-exit mechanism with an independently checkable prediction.
Otherwise reassess rather than raise a constant horizon. A failure of
the fixed-a obstruction test does not prove the cover.

No new lemma, script, specialization theorem or convergence result was
produced. Completed outcome: EXPLORATION; classification:
NOVELTY_UNCHECKED. This is local source coverage, not mathematical progress
beyond the checked sources. No mathematical exploration turn is spent.

## Inspected theorem statements and applicability

### Adjacent-pair theorem

Mark D. LaDue, *Clusters of Integers with Equal Total Stopping Times in
the 3x+1 Problem*, [arXiv:1709.02979v3, 2017-11-15](https://arxiv.org/pdf/1709.02979v3#page=3),
Lemma 3.1 and Theorems 3.2/4.1, pp. 3–5: for odd m>1,
m=2^p(2q+1)-1, p=v_2(m+1)>=1, q>=0, the shortcut iterates
T^(p+2)(m-1) and T^(p+2)(m) agree exactly when p and q have the same
parity. The positive case checks the even exit and the two subsequent
branches; the opposite-parity case would force an intermediate value
to be -1 if equality held. Neither case assumes convergence. The
specified companion m-1 lacks our residue-20 guard. The theorem's
failure at its stated clock is not failure of later coalescence.
This source is comparison and exact-path machinery, not a matching
cover. No reproof or new residue specialization is warranted here.

### Computational-sieve comparison

The live [workbench F031 audit, “Hercher coalescence branch,” lines
490–523](https://raw.githubusercontent.com/KokunoYumeto/collatz-workbench/main/collatz_reconstruction/qa/BARINA-OLIVEIRA-ROOSENDAAL-F031-computational-verification-audit.md)
states (F031.6): for odd x>1, alpha=v_2(x+1), u=(x+1)/2^alpha,
y=3^alpha u-1, beta=v_2(y)>=2, and m=(x-1)/2,
T^(alpha+beta-1)(m)=T^(alpha+beta)(x)=y/2^beta.
Its accompanying argument uses the mod-4 guard and, for lifting from a
later low state, a separate original-root size test. The inspected text
is an informal public derivation, not the original Hercher publication;
no immutable revision was retrieved. It neither imposes S membership
nor bounds beta by alpha. It therefore does not establish our clock
bound, and is not imported as a canonical mathematical input.

David Barina, *Improved verification limit for the convergence of the
Collatz conjecture*, J. Supercomputing 81, 810 (2025),
[sections 3.1–3.3, pp. 3–7](https://d-nb.info/1370796994/34), uses the
shortcut map and exact finite parity-cylinder acceleration. Section 3.3
compares a lifted iterate with the original start; the sieve filters
finite classes and the remaining starts are tested individually. This
does not supply a universal residue-20 coalescence theorem or a clock
depending only on the initial odd run. Its numerical verification is
not used as evidence for the TARGET.

### Reused coverage and recorded failures

The prior `2026-10-05-residue47-bounded-coalescence.md` assessment contains
the inspected Rozier (2019), Definition 1/Lemma 1, pp. 2–3, finite
parity-coding input and Sodelin's L4/L5 guard semantics. Reuse them rather
than reprove affine coding. L5 bounds inverse length only for unrefined
whole binary families, and the Mersenne no-go treats forward time within
the prescribed initial odd prefix; neither licenses pruning refined
companions after that exit. Sodelin's simultaneous ancestor/direct-
descent obstruction leaves general coalescence open. These comparisons
were already assessed; their sources were not reread.

L025 and L014 were read in full. Attempt 014 stops a constant clock on
the full cylinder, and Attempt 011 stops a constant ancestor horizon.
Neither is a global ban. The supplied overview distinguishes L024's
single-coordinate postspell budget obstruction from this two-path
question; no sibling proof or cross-notebook input was used. L014's
same-root convergence transfer explains the downstream use; it does
not establish the companion, the proposed clock or convergence of a
finite base. PROOF.md and DAG.md therefore do not change.

## Search and access evidence

Queries executed on 2026-10-05:

- `Collatz coalescence "v_2" "n+1"`
- `Collatz "odd" "coalescence" "27"`
- `Collatz "LaDue" "coalescence" stopping times`
- `"Exact Synchronized Coalescence Clocks" Collatz`
- `Hercher Collatz coalescence "alpha" "beta"`
- `"Collatz" "odd-run" "coalescence" residue`
- `"Novgorodtsev" "Coalescence" v4.1`
- `"Hercher" "Collatz" coalescence verification`
- `Collatz "47" "243" "odd" coalescence`
- `Collatz "coalescence" "linear" valuation`
- `Barina "Convergence verification" pdf fit`
- `"Hercher" "coalescence" Collatz sieve`
- `Collatz "coalescence" "fixed" "valuation"`
- `Collatz "second odd run" obstruction`

Search snippets and the challenge index were discovery aids only.
Aleksei Novgorodtsev's [Zenodo record 21848913, v4.1, issued
2026-08-08](https://zenodo.org/records/21848913) was inspected at the
abstract/metadata level. It advertises synchronized adjacent-pair clocks
for a guarded dyadic family. The primary manuscript PDF failed retrieval
via its download link and direct URLs; a command-line attempt failed DNS.
No theorem or proof from that manuscript is assessed or imported. This
optional strengthening of the adjacent-pair lead is not essential to
the proposed independent fixed-a test, so it does not block that test.

The original Barina (2021) DOI and author-postprint retrievals also
failed, as did the pinned sieve-tree/code retrieval. The accessible
2025 paper and informal F031 statement were explicitly distinguished
above; original Hercher attribution remains unverified. Other search
hits, including claimed resolutions, were not read and establish neither
coverage nor novelty. No persistent essential source blocker remains.

## Mathlib

Full matching linear-clock residue-20 cover or obstruction: **not
checked**. Supporting finite parity coding, CRT, valuations and affine
iteration: **not checked**. No absence is asserted. No Lean build or
mathematical script ran during this literature-only step.
