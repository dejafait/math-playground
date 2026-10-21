# Changed-tail survivor prime-five attempt

Approved target: Determine whether prime 5 survives in the reduced denominator of L065's exact j=23 unshifted cyclic root by comparing its numerator and denominator modulo 25.

Coverage: `drafts/literature/2026-10-13-survivor-prime-five-diagnostic.md` (SPECIALIZE, saved before invocation). Main gap: universal eventual descent. This one-prime test can exclude this integer allocation or stop this diagnostic, but leaves other allocations and universal gaps unresolved.

Inputs inspected: L055's full J,H table; L056's formal integer offsets and coordinate match; L058's cancellation law; L064's changed-tail closure and positive Delta; L065's exact tails. The completed L065 audit and Attempts 027–028 supply relevant prior evidence, not changed-numerator residues.

Plan: evaluate all 25 weighted contributions modulo 25 and independently compose single-letter triples using exact binary powering. Check changed-tail counts, complete chronology, unit inverse of 11, both denominator powers, and the symbolic equality Phi/Delta=n_0=s_0-23/11. Stop at this modulus regardless of verdict. Pending evidence is saved before calculation. No integer/parity/residue/exact-valuation/primitive-orbit realization is assumed.

Completed evidence: L066 records Phi=21, Delta=5 modulo 25, exact valuations 0/1 and the unshifted coordinate match. The two complete arithmetic evaluations agree; 38 checks pass with no failures. Full trace and comparisons inspected in `scripts/postspell-word-count/survivor-prime-five-certificate.json`. This excludes only the approved literal integer allocation and preserves its rational real-system witness. Stop the calculation now; separate critical-audit coverage is the next proposed target.
