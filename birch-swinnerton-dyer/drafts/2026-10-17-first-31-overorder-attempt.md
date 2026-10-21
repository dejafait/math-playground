# First strict 31-overorder — step 293 working record

Approved target: construct and independently verify exactly one strict
31-overorder by the source lattice O_H+(1/31)B^46 U(t,1), without iteration.
Assessment: drafts/literature/2026-10-17-first-31-overorder.md, SPECIALIZE,
saved before this invocation. This is known-method reproduction.

Inputs are audited L067, L077 and C077a, original H=343h, full rank 48,
all old basis/transports/product slots and G=T^2+24 modulo 31.
No L026, cross-notebook theorem or new prime search is used.
The main gap remains arbitrary-curve complex-order/rational-rank equality.
This order correction could support later units/classes and L066 arithmetic;
all maximality, descent, localization and rational-membership gaps remain.

Plan: exact ideal powering by binary lattice multiplication through powers
2,4,8,16,32,40,44,46. Reduce the complete 2304 product generators at each
stage by reversible integer row operations. Save every intermediate basis
and operation so the independently regenerated full generator set has the
same integral lattice in both directions. Then reduce 31O_H+B^46 U to
obtain the new basis divided by 31. Retain all source coefficients and
complete finite transports/products/index evidence. No monic shortcut.

One producer and one independent replay only, each 180 seconds internally,
181 externally, with combined directory at most 134217728 bytes. On a cap
or identity failure preserve partial evidence and stop without retry or
continuation. Full success needs source equality, rank 48, both transports,
all 110592 integral product slots, 31M integral and exact index 961.
Status: implementation not yet executed; no enlarged order claimed.

## Completed bounded attempt

The single producer stopped in `ideal_power_16` with `ArithmeticError:
byte_cap`. It saved operation witnesses for powers 2, 4 and 8, but saving
`power-16.json` would make the total exceed 134217728 bytes. The failed
write was rejected before opening that output. Its exact prospective
serialized size was not recorded, so only the strict cap violation is
certified, not a sharper required-byte figure. No assertion is made that
another algorithm would need this space.

The producer reports 6.066710666986182 seconds internally; the external
watchdog reports 6.154667875031009 seconds, below 180/181. The watchdog's
pre-report directory size is 39587717 bytes. The later stopped-artifact
inventory records 39588402 bytes before adding its own small report.
Every original input hash matches after the stop (72 files inventoried).
The full failure report and file sizes are in
`scripts/seven-torsion/first-overorder-293/producer-report.json`,
`produce-watchdog.json` and `stopped-artifact-inventory.json` in that
same directory. The input inventory's actual file count is authoritative;
no input arithmetic was modified.

No replay was invoked: the gate requires stopping at a cap, and no complete
producer certificate exists. The retained power bases and reversible
operations are **unverified partial evidence**, not established intermediate
lemmas. The source polynomial lift was saved but has no independent replay.
Power 46, source-lattice equality, new basis and inverse, index 961,
new transports and all 110592 new integral product slots remain absent.
No 31-overorder or progress beyond the checked source mathematics is claimed.
Neither PROOF.md nor DAG.md changes. No retry, resumed stage, larger cap,
second enlargement, new prime search or residual factorization occurred.

This is informative negative feasibility evidence for full integral
ideal-power expansion with explicit uncompressed elementary-operation logs.
Park that implementation. A materially different next target is source
comparison for a prime-local mod-31 quotient certificate with exact
clearing/generation witnesses, independently testable from the original
L067/L077/C077a inputs. Whether that avoids full B^46 expansion while
proving the exact cited lattice remains unassessed; the new assessment is
REVIEW_REQUIRED. It is not permission to drop B, assume t integral,
or resume these stopped power stages.
