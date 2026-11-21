# Same-mesh diagonal fallback — step489

The approved symbolic test has a uniform negative answer. The complete
proof, qualifications and primary citations are in
[C792b](../lemmas/C792b-central-residual-same-mesh-obstruction.md).
It covers weak and strict full-degree positive inputs, arbitrary later
entries, the extremal alternative and degree loss in the image. This is
a specialization of known tools, not a new general multiplier theorem.

**WHY IT FAILS.** The matched prefix has equality c1^2=c0 c2. An
admissible nonextremal same-mesh q-symbol would require strict inequality;
the only extremal compatible with its first two entries has c5=1,
contrary to the actual fixed residual's c5<1. Arbitrary later entries
cannot repair either contradiction. Thus same-mesh preservation cannot
transfer all separated models with this fixed prefix. This stop is
specific to that class-preserver fallback. It says nothing against
positive-root retention with mesh loss, degree-dependent prefixes,
or the actual matched-model family. L792's finite success is preserved.
Reopen this fallback only with a changed prefix or a genuinely restricted
input family; further degrees or a different Q do not evade the result.

The separate unapproved nomination concerns quantitative disjoint-root-
disk perturbation bounds with mesh loss. It needs essential source
coverage before calculation, and still leaves actual growing-degree
model separation and signed residual bounds unresolved.
