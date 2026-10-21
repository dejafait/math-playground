# Compiled coordinate serializer — stopped before build

WHY IT FAILS: The step-262 approval requires accounting for compiler children
and their peak memory, and explicitly stops at the build boundary if that
accounting is unavailable. Step 263's process-tree sampler cannot execute:
the sandbox rejects `/bin/ps` with PermissionError/EPERM. The earlier
child-free heartbeat can monitor a worker but does not account for a compiler
and its overlapping descendants. No approved alternative was established in
this bounded attempt. No compiler, checkpoint load or serializer test ran;
this is an environment/interface negative, not a serialization impossibility
or a counterexample to a mathematical result. Canonical evidence and precise
limitations are in [L068 §11](../lemmas/L068-general-actual-tree-output-zero-receiver.md).
Park this compiled-build route in the current environment; do not retry the
same sampler, omit descendant accounting or raise caps. The proposed existing
Python bounded-cache adaptation is a different, compiler-free target needing
separate review, not a completed implementation or an approved workaround.
