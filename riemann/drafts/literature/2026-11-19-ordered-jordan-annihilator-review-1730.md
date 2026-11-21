# Ordered Jordan signs: source assessment1730, completed review1731

TARGET: Establish whether C033g excludes every nonzero finite signed Borel annihilator of C032m's odd-kernel family whose signs change at most once on [1,2], including endpoint atoms and singular parts.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1731 checked scoped C032/C033 duplicates, stops1534/1536/1711 and park1725, and searched Chebyshev annihilating measures, ordered signed measures and stochastic-order equality; exact queries and access outcomes are in drafts/literature/2026-11-19-ordered-jordan-source-notes-1731.md. No novelty inference.
SOURCE_EVIDENCE: Shaked--Shanthikumar, Stochastic Orders (Springer2007), Note p1, Section1.A pp3-5/8, Theorems1.A.1/1.A.8: publisher chapter https://link.springer.com/chapter/10.1007/978-0-387-34675-5_1 ; inspected reproduced primary book pages https://www.slideshare.net/slideshow/stochastic-orders-1st-edition-moshe-shaked-j-george-shanthikumar-eds/279576121 ; publisher definition preview https://page-one.springer.com/pdf/preview/10.1007/978-0-387-34675-5_1 (read1731; unavailable through web reader1732). Complete relevant proofs and access qualifications recorded in source-notes1731. Bass2011 Theorem12.8/p97 and complete proof https://webspace.science.uu.nl/~kraai101/SignedMEasures ; reuse Musin's density-scope comparison1709.
COMPARISON: The known equality theorem concerns arbitrary real probability laws and finite expectations; Musin's continuous-density theorem is unnecessary. Applying it to the qualified positive kernel test and strictly monotone ratio requires local Jordan weighting, normalization and ordered-support checks, including all cut/endpoint atoms; those checks are not yet a theorem here.
GAP: Write the precise Borel-measure specialization for the unchanged ordered-sign class, including zero Jordan masses, arbitrary boundary atom and endpoint cuts. General-law source coverage is ready; kernel exclusion remains unproved. Unrestricted signs, constant-span completeness, positive output, moments and Xi realization remain open.
REASON: Separate literature-only review1731 covers the changed measure scope without deriving it; recovery1732 places direct source URLs in this field and checks their access while reusing that coverage. One routine reproduction/application is justified using the already audited sign input. The target and hypotheses are unchanged; supervisor separately approves the repaired ready continuation. This repair is not a mathematical advance.
SCOPE: C032m's full kernel kappa_w(s)=exp(-E_s(w))*sinh(O_s(w)), its jointly continuous entire interface, C033g's qualified f(s)=Im(kappa_(i/8)(s))>0 and strict g/f decrease on [1,2]; finite real signed Borel eta with all inherited divisor/source qualifications, no density assumption.

## Exact proposed mathematical test (preserved nomination1730)

For this target, "at most once" means: there are c in [1,2] and
epsilon in {-1,1} such that epsilon*eta restricted to [1,c) is a
nonnegative measure and epsilon*eta restricted to (c,2] is a
nonpositive measure. The atom at c may have either sign. This includes
measures of one sign, endpoint atoms, zero restrictions, and singular
continuous parts. The annihilator condition is J_eta(w)=0 for every
complex w with the integral and normalization of C032m. No density,
positive output or mass-one condition is built into this proposed test;
the eventual use would include C032q's mass-one subclass.

At nomination, the required next turn was literature-only: check the exact statement, standard
Chebyshev/ordered-sign measure terminology, stronger known conclusions,
and obstructions. Retrieve primary hypotheses and essential proof cases;
reuse the existing continuous-density comparison rather than reopen
the Gaussian minor sources. Distinguish a direct import from any needed
Borel-measure specialization. Do not silently apply Musin to atoms.
At nomination no source access attempt had failed for this new target.
Review1731's access outcomes and alternative primary-text access are
now recorded in source-notes1731; none remains an essential blocker.

Continue to one mathematical application only if the assessment covers
the full ordered-sign class just defined. Its acceptance test is an
exclusion proof covering arbitrary cuts and atoms, or a rigorous
nonzero counterexample satisfying the complete annihilator condition.
Finite-grid cancellation of f and g alone is not a counterexample to
J_eta identically zero. If known results apply only to densities, record
that difference and review the precise specialization rather than claim
the full statement. The condition must not be strengthened silently.

## Comparison of three possible continuations

1. More Gaussian minor estimates: another two-point replay is exhausted
   as a task, while higher minors need new sign estimates and still do
   not decide unrestricted cancellation. Not selected.
2. Direct recurrence or compact-support transform: stops1534/1536 retain
   the missing constant-coefficient span closure and the audited growth
   obstruction. No new coordinate or closure mechanism is proposed;
   these are not reopened.
3. Ordered Jordan-sign exclusion: selected as a different, independently
   testable restriction on the signed measures themselves. C033g is now
   ready as an input; the source gate covers the changed measure scope
   before a proof is attempted. No new bound or exclusion is derived now.

This is a modest intermediate application, not a creative central RH
mechanism. No justified central creative test is ready: the relation
between unrestricted cancellation/positive output and an actual-Xi
realization remains unproved, and this two-point input does not supply
one. Do not label a routine Chebyshev specialization creative to satisfy
a scheduling preference. Matching Mathlib coverage is unchecked/unknown.

## Completed source decision1731

SPECIALIZE covers the exact TARGET and sign-cut definition above,
without excluding atoms or singular parts. Use source-notes1731's
inspected general-law equality theorem and reused Jordan theorem;
prove only their applicability. Do not reprove the general coupling
or equality theorem, repeat the Gaussian sign estimate, or claim
the ordered-sign exclusion already holds. No new kernel identity,
measure exclusion or counterexample was derived in this literature
turn. The continuation's test remains a full proof for this exact
class or a counterexample satisfying the entire J_eta=0 condition.
