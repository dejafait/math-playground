# Scope and identity contract source review

2026-10-23, step 420. Literature/interface review only; no controls,
modules, numerical replay, lemma or mathematical script executed or written.

The main gap is arbitrary-curve rank/order comparison at analytic order >=2.
The intermediate target is a justified scope/identity interface for a separate
L105 audit. Its plausible downstream use is reliable validation of four finite
inputs to L101, not a rank theorem. Continue only if the finite preflight below
passes before numerical replay; otherwise stop and park this interface.

## Primary language inputs

Inspected official rolling Python 3.15.1 documentation on 2026-10-23:

- [Execution model §§4.2.1–2, 4.2.6](https://docs.python.org/3/reference/executionmodel.html#binding-of-names): loop targets bind names; module bindings are global, whereas function bindings are local absent global/nonlocal declarations. Free-name lookup occurs at runtime. The exec environment has special rules and is not an implicit lexical closure.
- [Built-in exec](https://docs.python.org/3/library/functions.html#exec), complete namespace cases: omitted mappings use the current scope; one explicit dictionary supplies both mappings; two distinct mappings have class-like semantics, so defined functions cannot see top-level local assignments through their globals. Default function locals changed in 3.13. This rules out relying on implicit exec locals as a repair.
- [Simple statements §§7.12–13](https://docs.python.org/3/reference/simple_stmts.html#the-global-statement): global/nonlocal are parser directives with the stated block scope; a global directive in an exec string does not govern the caller's separately parsed block.

These are documented language facts, not a theorem about arbitrary programs.
No language rule prevents explicit mutation of a passed module or dictionary.
An integer value is immutable, but its variable name can be rebound. The
contract therefore needs restricted bindings and equality checks, not an
assertion that naming a variable immutable makes it so. Record the actual
future interpreter; 3.15.1 documentation is not evidence of its installed version.

## Local comparison, duplicates and preserved failure

Read complete step-419 worker.py and signed-checks.py, the static diagnosis,
ATTEMPTS/047, history/419 and the selected full failure traceback. Search of
histories 418/419 and the named local audit assessments found the earlier
coverage and uncovered proposal, not a completed corrected audit. The worker
loads the n=3 module/path before module-scope exec; the control loop then
binds n to 2*D+1. The failure occurs at the complete report comparison.
The returned report was not persisted; later ledger/radius checks were not
reached, and no certificate defect was established. This review imports
language semantics explaining that recorded failure; it does not replay it.

Reuse drafts/source-notes/2026-10-23-four-kernel-audit-coverage.md and its
ready assessment for all unchanged analytic, signed-arithmetic and process
obligations. No changed kernel hypothesis requires new mathematical discovery.
L031 endpoint rules, L101 kernel definition, audited L102, audited L103
parameter portion and L105/step-417 remain essential. L104/step-415 is only
implementation comparison. No mathematical reproof or Mathlib claim is needed;
full Mathlib coverage remains unchecked. L035 already imports the known fixed
complex order, so this is changed certificate provenance, not a new BSD case.

## Covered implementation and finite preflight

The next implementation must define a genuine installer function whose
parameters explicitly receive replay, D, a fresh signed-counter dictionary
and the control-output callback. Nest the unchanged primitive wrapper bodies
and deterministic control loops inside that function. Their saved old
primitives and module/counters are lexical captures. Return explicitly what
the worker needs. Do not put exec of the original top-level control block
inside a function and assume closure behavior. If source generation uses
exec, execute only the function definition in a fresh single dictionary and
call the retrieved installer with explicit arguments. No separate globals/
locals dictionaries or implicit caller locals are permitted. The definition
has no top-level control loop or side effect beyond its definition; inspect
all defaults, decorators and annotations too.

The installer may replace exactly the nine named replay primitives, mutate
its own signed counters, clear the preliminary replay ledger, and write the
separate control report. Forbid global/nonlocal directives, worker-namespace
access and further dynamic evaluation in the installer/control body. Inspect
all assignments and calls against the complete retained block, with exact
body comparison except the explicit function/return interface. Renaming a
loop alone is insufficient coverage. Wrappers must retain all distinct
signed checks and original primitive references, avoiding recursive wrapping.

Represent identity as a tuple of immutable scalar/string values: index,
canonical fixed input/output path strings, unique module name and source hash.
Keep it outside the installer; never pass a mutable worker metadata mapping.
Construct every path, report index and status from this same identity. Require
one assignment site for the identity binding and forbid later rebinding by
static inspection. Separately retain and check the actual replay object,
module name/file/source hash and selected input/output paths. An identity
tuple alone does not freeze the replay module or guarantee correct selection.

Before any kernel, run a small preflight using only inert primitive doubles
and the actual installer for each of 3,4,5,6. Supply deterministic primitives
with the required signatures so all existing controls execute, but no kernel
or production/replay entrypoint can run. Check complete pre/post worker
identity, paths and module references, including a sentinel worker n distinct
from every control value. Check the exact nine permitted replacements, wrapper
capture of the intended distinct module/counters, complete control output,
zeroed post-control counters and ledger, and no extra callback writes. The
preflight must call a retained wrapper after installer return to expose lost
closures. Check all nine multiplication sign bins and zero/endpoints. Static
binding review complements the finite test; neither certifies arbitrary code.

For each real per-index module, repeat identity checks immediately before and
after installer invocation and complete replay. Separate full ledgers/counters
from controls. Persist the complete returned report before subsequent audit
comparisons; compare it in full against saved replay.json after adding exactly
n from the identity, never by dropping fields. Snapshot ledgers and nested
counter arrays by value. Check all metadata against the selected fixed
records, module and paths. Preserve complete report equality, both ledgers,
all panels/arithmetic, exact endpoints/enlargement and both strict radii.

The fresh audit inherits every original aggregate obligation: one exclusive
new directory and one clock from before setup/preflight through final writing
and observed child exits; 180 seconds/134217728 new bytes; first failure stops
all later kernels. No old audit entrypoint, producer, retry or resumption of
419 runs. Keep all original/copy identities, file sets and exact editorial
transitions, including post-419 canonical changes. Preserve historical n=1,
n=2 and step-417 timing qualifications. Preflight consumes the same cap; its
success gives no four-kernel runtime guarantee. Failure yields preserved
partial evidence, not a complete audit PASS. A future implementation is
covered conditionally, not validated by this review.

Independent gaps remain: 122 kernels, signed derivative assembly, parameter
transfer, strict zero exclusion and arbitrary-curve rational-rank comparison.
