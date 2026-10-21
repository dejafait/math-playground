# Source assessment for positive-valuation class extraction

TARGET: Assess whether, under L023's hypotheses and for m > 2h, its actual two prime-deletion classes kappa_(N/ell_i,ell_i) are classical and their span has index at most p^(3h) in Sel(Q,E[p^m]).
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the class-extraction, finite-index and rank-zero terminology listed below; compared L021/L023 with L015-L017 and ATTEMPTS/021; inspected the primary Poitou-Tate proof case in Sakamoto 2022 Corollary 4.10 and the 2021 regulator construction. No search establishes originality.
SOURCE_EVIDENCE: Sakamoto 2022, DOI 10.4171/DM/X21, Theorem 2.1/Definitions 2.3-2.4, pp. 1897-1898; Section 2.3/Definition 2.18/Theorem 2.20, pp. 1902-1904; Section 2.5, pp. 1905-1907; Proposition 3.19, pp. 1915-1916; Corollary 4.10 and its full proof, p. 1920. Sakamoto 2021, DOI 10.5802/jtnb.1189, Section 5.2/Lemma 5.4/Theorem 5.5/Proposition 5.6, pp. 1089-1093; precise scope and links below.
COMPARISON: The published mod-p basis conclusion needs residual minimality and does not match positive h. Its proof supplies a usable relaxed/classical comparison via Poitou-Tate, while Definition 2.18 controls the actual class localizations. L023 separately supplies depth-m localization surjectivity and kernel length h. No inspected theorem states this exact p^(3h) bound.
GAP: Specialize the duality comparison using L023's full localization surjection, check both local conditions for the actual components, and bound the span quotient without canceling the nonunit scalar or assuming the finite module is free.
REASON: Essential theorem-level coverage is now sufficient for one bounded specialization; import the duality theorem and class relations, then prove only the finite-depth applicability and quotient-length estimate. This review proves no extraction result.
LITERATURE_REASON: Changed target concerns actual positive-valuation cohomology classes and a span index; the prior scalar audit did not cover these conclusions. The primary proof of Corollary 4.10 is the specific newly inspected lead.
SCOPE: Retain all L021/L023 arithmetic hypotheses, granted corank two and residual-family nonvanishing; F=S/S_div, h=length_Z_p F, N one of L023's selected pairs, with tensor factors trivialized as in L023. The proposed m>2h threshold applies only to the extraction proof task and does not weaken L023's audited m>h claim.
COVERED_TARGET: Specialize Sakamoto's Poitou-Tate comparison and rank-zero class relations under L023's hypotheses for m > 2h to test classical membership of its two prime-deletion classes and the span-index bound p^(3h).

The main gap remains rational membership and comparison with complex
vanishing order. A uniform finite-index span of actual classical
classes could support a later passage to characteristic zero. Neither
compatibility as the primes vary nor rational Kummer membership would
follow merely from this finite-depth target; both remain independent
questions. No such passage or extraction is proved here.

## Sources and exact comparison

Primary version: Ryotaro Sakamoto, *p-Selmer group and modular symbols*,
Documenta Mathematica 27 (2022), 1891-1922, DOI 10.4171/DM/X21,
publisher's text received 2022-05-13 and revised 2022-07-20. The
[publisher PDF](https://ems.press/content/serial-article-files/29299?nt=1)
was accessible through the browser on 2026-10-05. The section setup
has p>3 with assumptions (a)-(c); at n=0 its coefficient ring is R_m
and its representation is E[p^m]. L023 retains these assumptions and
the stronger local-torsion restriction. No theorem is being applied
to a differently normalized scalar family.

- [Theorem 2.1, p. 1897](https://ems.press/content/serial-article-files/29299?nt=1#page=7): nested local conditions give the Poitou-Tate sequence ending in the two dual Selmer groups. Read the whole statement, including the Pontryagin dual and every term. Definitions 2.3-2.4, p. 1898, specify strict, relaxed and transverse modifications, exchange strict/relaxed under duality, and identify the classical structure as self-dual. Lemma 2.6 identifies the away-from-p condition with the unramified one under the Tamagawa assumption.
- [Definition 2.18, p. 1903](https://ems.press/content/serial-article-files/29299?nt=1#page=13): read all three class relations, not merely the scalar detector. The components have transverse conditions at d and a relaxed condition at the extra prime. Section 2.3's finite/transverse splitting and finite-singular comparison use P_(m,0), exactly the eligibility retained in L023. The definition of delta on p. 1904 and Theorem 2.20 concern the same system. Retain all tensor trivializations; do not compare positive valuations using Lemma 4.2's residual equivalence.
- [Corollary 4.10 and full proof, p. 1920](https://ems.press/content/serial-article-files/29299?nt=1#page=30): this is a classical mod-p basis theorem at a delta-minimal index. Its proof first uses Theorem 2.1 with strict and classical structures, then compares the relaxed group with the classical group, and finally checks the prime-deletion localizations. The theorem's residual-unit premise is unavailable for positive h. The proof's duality mechanism, rather than its basis conclusion, is the useful known input to specialize.

The other newly inspected primary text is Sakamoto, *On the theory of
Kolyvagin systems of rank 0*, J. Theor. Nombres Bordeaux 33 (2021),
no. 3, part 2, 1077-1102, DOI 10.5802/jtnb.1189.
[Section 5.2 and Lemma 5.4, pp. 1089-1091](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1189.pdf#page=14)
give the actual regulator components as contractions of Stark
components. Read that definition, its commuting diagram and the
verification of relations (5.1)-(5.3); also read Theorem 5.5 and
Proposition 5.6, pp. 1091-1093. Their setup is a zero-dimensional
Gorenstein ring with Hypothesis 2.7; the isomorphism uses Cartesian
core-rank-zero conditions and a sufficiently rich prime set. The
projection isomorphism further requires the stated dual modified
Selmer vanishing. It does not give a projection basis at L023's
positive-defect index. This general construction is a checked
comparison, not an extra input needed for the proposed shorter
Poitou-Tate attempt. Sakamoto 2022 Section 2.5 refers to this same
regulator, and Proposition 3.19 concerns the actual Kato-derived basis.
Neither is a ready finite-index extraction theorem.

No essential source remains inaccessible. An attempted shell download
of the 2021 PDF failed at DNS resolution; the browser supplied its
complete relevant text. There is no saved PDF or mathematical output
from that attempt. Screenshots were requested but their images were
not exposed in the tool response; the assessment uses the full text
reads, not an image preview.

## Local overlaps and the proposed specialization

Read L023's full selection and scalar proof, L021's hypotheses and
finite paired quotient statement, L015's class definitions and error
relations, L016's hypotheses/conclusion, and L017's transfer statement.
The earlier unit case has no such positive finite quotient at the
working depth as a granted input. L015-L017 warn against asserting
classical membership from a diagonal scalar: there are crossed
auxiliary errors, and a Stark contraction alone does not remove them.
L023 supplies a materially different hypothesis to use: the combined
finite localization is surjective on the classical group and its
dual at the working depth, with strict kernel of length h. The
existing error model does not test this strengthened package.

ATTEMPTS/021 concerns removing the finite quotient from primitivity;
the present target retains F. A finite-index classical span would
not eliminate F or identify divisible Selmer directions with points.
L015-L017 are comparisons, not additional established inputs required
for the proposed application. No lemma is a duplicate of the stated
positive-defect extraction bound among these checked local results.

The approved proof task is to apply the cited Poitou-Tate sequence to
strict and classical structures at N, using L023's surjectivity to
test whether the relaxed group equals the classical group. It must
then apply the actual rank-zero relations to both prime-deletion
components and track the resulting localization matrix with the
chosen tensor factors. The final check is a quotient-length argument
retaining the strict kernel F: the required bound is length <= 3h,
equivalently index <= p^(3h). This is a proposed proof task, not an
established consequence in this assessment. No bound has been
achieved here. Keep m>2h for this attempt; a weaker necessary depth
would require explicit justification in the mathematical turn.

No reproof of Poitou-Tate, the regulator isomorphism or the source's
Kato construction is justified. Only their necessary specialization
and the unidentified span-length difference are authorized. In
particular, positive scalar valuation does not license division by
p^h in R_m, a free-basis assertion about R_m^2 plus F, or identifying
these classes as global rational Kummer classes.

## Search record and decision test

Queries on 2026-10-05: `Sakamoto "prime" "Kolyvagin" "index" Selmer
modular symbols`; `"prime-deletion" Selmer finite index valuation`;
`Sakamoto "rank 0" "Stark" "components" Fitting`; `"Kolyvagin systems
of rank 0" "classical" Selmer`; `"Kurihara" "prime" "basis" "p^m"`;
`Sakamoto "On the theory of Kolyvagin systems of rank 0" arxiv`.
The searches found the two primary Sakamoto texts. Broader results on
Heegner and ultra-Kolyvagin systems were not inspected and supply no
coverage for this target. A Castella-Sano refined-nonvanishing result
also appeared; it is an unread lead, not evidence for these classes.

Continue with one mathematical attempt using the now-inspected
duality mechanism and exact class relations. Retain the extraction
only if both classes are classical and the actual span quotient has
length at most 3h, for every retained m>2h and selected L023 pair.
Check h=0 as well as positive h; justify each dual structure and
the nonunit localization calculation. If any essential step needs
residual minimality, new vanishing, unknown normalization or depth
compatibility, record the failure rather than insert that assumption.
Rational membership, production of corank two from complex order,
finite Sha and compatibility as primes vary remain independent gaps.

Mathlib: full matching extraction theorem and supporting coverage
not checked. No new lemma, mathematical script, extraction proof or
claim of originality is made in this literature turn.
