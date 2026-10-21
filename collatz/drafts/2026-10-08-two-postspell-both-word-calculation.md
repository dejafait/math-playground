# Both-word restriction — saved proof attempt

The approved target is the maximum of 4J_i+H_i over both actual closed
words. Main gap: universal eventual descent. Downstream use: constrain
the represented odd count in later closure analysis, with independent
tails, total length and closure exclusion still unresolved.

Coverage reused: `drafts/literature/2026-10-07-two-postspell-both-word-joint-bound.md`
(SPECIALIZE). Relevant proofs L031/L035/L036/L037 were read, including
the L037 audit; Attempt 019's guard-only failure was preserved. No
new source search or general transcendence/parity reproof is needed.

Saved reasoning before final write-up: choose b=min(n,x) with its own
word parameters J,H,a, and write s=b+23/11. L037 gives
log s<(133/10)log K+8 and 4J+H<50log N+33. For this word's other
endpoint m, G=(27/16)^J(3/2)^H and the exact identities give
z=Gs-(12/11)(3/2)^H-1, m=z/2^a. Since a>=2 and s>=540/11,
m+23/11<Gs/4+23/11<Gs. Also log G<(4J+H)/2 from
27/16<(3/2)^4 and log(3/2)<1/2. Therefore
log(m+23/11)<(383/10)log N+49/2.

At either junction r, its own valuations and height identity give
4J_r+H_r<(15/4)log(r+23/11)+3. Applying this to m gives
4J_m+H_m<(1149/8)log N+759/8<144log N+95.
The selected word already satisfies the smaller L037 bound. Both index
orders and x=n use actual words and are admitted; no local-minimum
chaining, relative growth or bounded-tail assumption is used.

Continuation test: accept this attempt only if all endpoint shifts,
strict signs and constants survive the canonical proof with independent
tails and repetition. If the transfer needs an unsupported junction
comparison or yields only the selected-index estimate, abandon it.
This is a REPRODUCTION specialization, not an originality claim or a
complete Collatz candidate. The canonical write-up and separate audit
remain to be completed when this draft is first saved.

Completion: the full proof is now in
`lemmas/L038-two-postspell-both-word-joint-parameter-bound.md`.
The transfer, generic other-word inequality, rational constants and both
index cases survived the write-up. Only the separate critical audit is
pending; no additional mathematical target was attempted.
