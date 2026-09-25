# 011 — 2026-09-26 — Locator incidence narrows the regular-pencil gap

Completed one algebraic test of the proposed sixteen-challenge upper bound.
The [assessment](../drafts/2026-09-26-affine-locator-incidence.md) records
the gap, test, saved reasoning, and comparison with prior failures.
The [official statement](https://proximityprize.org/) was reread and its
unchanged preliminary parameters were recorded in the source audit.
The ABF26 definition remains uncertified. Pre-existing local edits and
the L009 artifacts were inspected and preserved; other notebooks were
not edited.

[L010](../lemmas/L010-affine-locator-incidence-bound.md) proves an upper
count of sixteen when the Hankel determinant and each coordinate locator
are nonzero polynomials. It includes singular parameter values by counting
their forced root multiplicities. It also proves the converse locator
test and same-support failure, then characterizes equality by quartic
splitting and four incidences per root. Sixteen requires distinct four-error
supports, with each coordinate in four supports. This is a uniform
algebraic result, not an extension of a finite enumeration.

Outcome: ADVANCE; exploration turns used reset to zero. The result narrows
the covered class from the available count 69 to sixteen, but fifteen is
the actual allowable count at q=97^20. Equality and identically vanishing
polynomials remain open, so no code-level safety statement follows and
the global bounds remain 10/q and 69/q. STATUS remains IN_PROGRESS;
there is no complete challenge candidate.

The reason for continuing toward equality is its rigid balanced support
incidence, which can be tested using lines meeting four disjoint error
spaces. This does not require subgroup-equivariant errors and therefore
is not a repetition of the stopped full-orbit mechanism. The concrete
partition and field are specified only in the compact current checkpoint.

The auxiliary check independently tests all 2517 admissible supports for
five covered pencils over F_97. It recovers ten bad parameters for the
two-block example and verifies the multiplicity costs for weights zero
through three. An excluded fixed-support pencil distinguishes 97 decodable
values from four bad values. These checks do not maximize over input words.
The proof is self-contained; earlier lemmas are comparisons, so the new
DAG row has no inputs. Mathlib coverage is not checked, and the supporting
ArkLib declaration names and immutable link are retained.

Validation commands: `python3 scripts/locator-incidence/check.py`,
`PYTHONDONTWRITEBYTECODE=1 python3 ../scripts/docs/check_structure.py --problem reed-solomon-mca`,
and `git diff --check -- .`. The shared checker is run without bytecode
writes so generated artifacts remain inside the active notebook.
