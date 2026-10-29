# Exact conductor-389 full 5-Selmer source coverage

Date: 2026-10-26. Source comparison only; no mathematical derivation,
calculation or independent replay. Exact target and decision are in
`drafts/literature/2026-10-26-conductor389-full-five-selmer-input.md`.

## Primary source and inspected proof case

William Stein and Christian Wuthrich, *Algorithms for the arithmetic of
elliptic curves using Iwasawa theory*, Mathematics of Computation 82
(2013), 1757--1792, DOI 10.1090/S0025-5718-2012-02649-4.
Version: 36-page published author offprint, electronically published
14 September 2012, [primary PDF](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf).

Read Theorem 12.3 and entire proof, p.1788; Section 12.4,
pp.1787--1788; Algorithm 11.1, all five steps and complete proof,
pp.1783--1784, including the ordinary case. The theorem identifies 389a
and proves Sha[p]=0 for its listed primes, including 5. Its computation
uses the preceding procedure. Algorithm 11.1 requires p>2, nonadditive
reduction and surjective residual representation; it certifies rank,
regulator nondegeneracy and matching p-adic order before outputting a
Sha bound. Read Theorem 6.1, p.1776, for that matching criterion. The
ordinary bound uses its leading-term valuation and Kato divisibility,
not conjectural BSD equality. Conjectures in Proposition 11.2 concern
general termination/equality, not validity of completed upper bounds.
Step 2 cites MST/Harvey. No original proof or code replay was inspected.
Theorem 12.3 is the cited input, not a new execution of Algorithm 11.1
or correction of the printed sigma convention.

Its arithmetic Sha[p] assertion is distinct from the adjacent conjectural
order congruence. Only p=5 is needed here. The proposed import accepts a
published computational theorem under the notebook's citation policy;
independence from that computation is not claimed.

## Model and arithmetic-group coverage

J. E. Cremona, *Algorithms for Modular Elliptic Curves*, corrected
online second edition, CUP 1997:

- [Table 1, p.109 definitions and p.157 row 389A1](https://johncremona.github.io/book/fulltext/table1.pdf#page=49):
  the entry gives [0,1,1,-2,0], r=2, |T|=1; conductor 389 has one
  isogeny class and this block one curve. Definitions identify rank E(Q)
  and rational torsion order.
- [Table 2, p.255 definition and p.257 row 389A1](https://johncremona.github.io/book/fulltext/table2.pdf#page=3):
  entries are generators modulo torsion on Table 1's minimal model;
  the pair is (0,0),(1,0). Reuse L034's assessment of the published
  group result and its 2006 database account.
- [Chapter IV, pp.104--105](https://johncremona.github.io/book/fulltext/chapter4.pdf):
  read the relevant table descriptions.
  [Errata, 26 September 2003](https://johncremona.github.io/book/errata.pdf):
  read the complete one-page list; no 389A1 correction.
- [Author's ecdata description](https://johncremona.github.io/ecdata/),
  Table Two example, and [allgens row 389 a 1](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allgens/allgens.00000-09999):
  read the exact row/interpretation. These confirm label/model matching;
  the published book anchors the proposed import, not only mutable raw
  data. The website lists a 2020-11-27 update and 2019-07-22 major update.
  No current repository commit is pinned.

Arithmetic rank/torsion data alone do not give the Selmer bound.
The next application also needs the cited Sha theorem and L001's finite
Kummer relation. This source review does not perform that application.

## Discovery and alternatives

Queries on 2026-10-26: `"389a1" "5" "Selmer"`,
`"389" "5-Selmer"`, `"389" "Tate-Shafarevich" "5" Stein Wuthrich`,
`"389a" "5" "Stein" "Wuthrich" 2013`, `"389" "5-descent" elliptic`,
`"389" "Selmer" "Schaefer"`, `Fisher "Explicit 5-descent" 389`,
`Stein Wuthrich algorithms Iwasawa theory erratum 389 5`.

Stein's 15 May 2011 [Cambridge talk notes](https://wstein.org/talks/2011-05-bsd_conference/2011-05-bsd_conference.pdf),
Proposition 1.5, and author/Sage tutorial examples located the published
theorem. The talk describes its broad computation as then unfinished;
the final published result is used instead. These leads do not replace
the inspected theorem/proof. No exhaustive errata clearance or novelty
inference follows from the searches.

The [Fisher author abstract](https://www.dpmms.cam.ac.uk/~taf1000/papers/fivedesc.html)
and search results identify *Explicit 5-descent on elliptic curves*.
Its theorem/proof cases were not inspected and are unnecessary here.
A guessed `5descent.pdf` URL failed, as did a guessed Cremona chapter7
URL; neither is an essential blocker. Exact book tables were accessible.
The Schaefer--Stoll assessment dated 2026-10-15 is reused. Its primary
PDF landing text was retrieved; no fresh algorithm review is claimed.
Broad BSD claims, unrelated visibility examples, rank-only tables and
analytic Sha values in search results were not used as theorem inputs.
PDF text was read. Screenshot calls produced no inspectable image here;
no visual PDF verification is claimed.

Local comparison: L001's Kummer relation; L030's arithmetic paragraph;
L034's published basis provenance; L119's input contract;
ATTEMPTS/032/034/057; finite-certificate/full-descent assessments.
No sibling notebook, API key or mathematical script used.
Mathlib coverage of the exact arithmetic result: not checked.
