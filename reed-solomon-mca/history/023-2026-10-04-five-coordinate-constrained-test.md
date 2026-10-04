# 023 — 2026-10-04 — Five-coordinate test and eleven-count specialization

Completed one mathematical attempt on the saved actual-pencil
COVERED_TARGET under the existing SPECIALIZE assessment. Shared and
local instructions, the complete overview, DAG, prior coverage and
unfinished changes were read and preserved. No browsing was needed.

[L015](../lemmas/L015-five-coordinate-projective-reduction.md) reduces
a nonpersistent pencil representable on a five-set to five possible
coordinate cancellations and a rational configuration of 330 external
support points. It proves the field passage for arbitrary F_(97^20)
weights, distinctness, rank-one handling and 273 free multiplicative
orbits. Its unconditional conclusion is |B|<=5+M(A); sixteen with a
three-coordinate support overlap would require eleven collinear points.

The [test](../drafts/2026-10-04-five-coordinate-constrained-test.md)
enumerates all 14819805 point pairs and records every orbit's maximum.
The maximum is six, with an independent complete Python configuration
check and independent membership checks of all 273 stored maximal lines.
This class stop has explicit computational dependence and gives no
global upper bound for arbitrary pencils. Its exact certificates are in
[the result](../scripts/coefficient-feasibility/five-coordinate-result.json)
and [orbit records](../scripts/coefficient-feasibility/five-coordinate-orbits.jsonl).

The best actual line has eleven bad parameters. A redundancy check
identifies it as an invertible change of the inputs in a partition
already covered by L013. [C013a](../lemmas/C013a-eleven-challenge-partition-specialization.md)
uses that theorem: the partition has a size-four fiber at ratio 55,
and its residual factor X+20 adds parameter 77. This exact application
improves the achieved global lower bound from ten to eleven independently
of the search or enumeration. Reproof of L013 is unnecessary.

Outcome: ADVANCE for that local lower-bound improvement;
STEP_KIND: RESEARCH; STEP_CLASSIFICATION: REPRODUCTION. The geometric
reduction specializes existing moment/MDS facts, and the explicit
witness is an application of local L013. No progress beyond the checked
literature or originality is asserted. The main interval remains
11/q–16/q against an allowable fifteen; no complete candidate appeared.

Stop this five-coordinate generator as a sixteen-count search. The next
test reuses the preapproved actual-pencil target with two four-error
representatives whose union has at least six coordinates, imposing a
third support constraint before the equality checks. No next calculation
is made here. Consecutive uninformative mathematical turns used: zero;
resultant-target mathematical attempts: three; five-set tests: one.
The stopped orbit/two-block and parked July/four-block failures, including
their old exhaustion evidence, remain intact.

Validation: `python3 scripts/coefficient-feasibility/five_coordinate.py`
checks the full finite configuration, actual determinants, inverse
compatibility, power residuals, factor multiplicities, exact extension
splitting and the original event on all 2517 supports for two affine
charts. An initially overstrong squarefree-residual assertion failed;
the retained triple-incidence factor is checked correctly below fourfold
multiplicity. The final factor audit passes. Direct mathematical inputs
were reviewed: L015 uses L010's moment kernel, distance and same-support
criterion; C013a uses L013's fiber theorem. The finite search motivates
the corollary but is not its proof premise. Prior local artifacts and
all other notebooks were preserved; no shared or runner files were edited.

The documentation checker with `--problem reed-solomon-mca` passes with
seventeen nodes and eleven edges. Current metadata retains exactly one
Next action matching a preexisting COVERED_TARGET in the unchanged ready
assessment; the completed step is RESEARCH/REPRODUCTION with ADVANCE
supported by the explicit corollary. The exact check command passes all
reported arithmetic and original-event checks.
