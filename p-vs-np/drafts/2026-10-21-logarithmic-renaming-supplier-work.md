# Step 394 — restricted renaming supplier work

Approved target: construct the exact-fg witness under the original global
floor(log₂ Q) renaming-line cutoff, or identify its precise failure.
Reuse step 393's EXPLORE coverage; no new source review is undertaken.

Main gap: unrestricted SAT decision/separation. Intermediate target:
normalize this supplied restricted proof to ordinary Frege with a full
original-Q polynomial, then receive L098. This would supply a conditional
witness class, leaving short-proof availability and M-only bounds open.

Proposed invariant, saved before the all-size argument: a request (i,S)
asks for the i-th source formula under the composite of the renaming
lines in the descending ordered subset S encountered from the output.
MP retains S on both parents; crossing renaming line j adds j and
composes its map before the outer context. Every encountered index
strictly decreases. Thus there should be at most N·2^r requests, including
all axiom occurrences needed at any later stage. Materialize ordinary
axiom/MP lines only; a renaming request aliases its transformed parent.
Keep original variables until the entire normalization is complete.

Continuation test: prove exact syntactic endpoints and acyclicity for
noninjective maps, constants and repeated references, and pay all maps,
formula/axiom-instance strings, references and dictionaries before using
2^r≤Q. Then use L098's audited ordinary-proof occurrence/guard and
complement interfaces on the unchanged F and occurrence pair. Abandon
this implementation if contexts require more than ordered subsets or
one of these receptions needs an additional unproved premise. No
compression of L100's isolated aggregate is attempted.

Status at save: proposed invariant only, not yet a proved supplier.

Completed disposition: the invariant closes by eliminating renaming at
the source-proof level, before occurrence substitution or extraction.
The full proof, exceptional cases and original-Q size/time ledger are
canonical in L101. All initial requests, all required later axiom seeds
and every requested context are retained. This meets the bounded target
informally and awaits a separate critical audit; no implementation was
run. Attempts 020/032/033 remain unchanged. This draft is a saved work
record, not the current checkpoint.
